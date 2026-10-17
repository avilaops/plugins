"""Validate, catalogue and export the local capability collection.

Does not install plugins, execute bundled code or read credentials.
"""

from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import zipfile
import xml.etree.ElementTree as ET

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_BASE = "https://agent-plugins.org/schemas/1.0.0/"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
EXCLUDED = {"__pycache__", "node_modules", ".git", ".venv", "venv"}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(root: Path, target: str) -> Path:
    if not isinstance(target, str) or not target.startswith("./"):
        raise ValueError("Package paths must start with ./")
    path = (root / target).resolve()
    if not path.is_relative_to(root.resolve()) or ".." in Path(target).parts:
        raise ValueError("Package path escapes its root")
    if not path.exists():
        raise ValueError("Referenced package path does not exist")
    return path


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("Missing YAML frontmatter")
    meta = yaml.safe_load(match.group(1))
    if not isinstance(meta, dict):
        raise ValueError("Skill metadata must be an object")
    name, description = meta.get("name"), meta.get("description")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        raise ValueError("Invalid skill name")
    if name != path.parent.name:
        raise ValueError("Skill folder does not match its name")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError("Invalid skill description")
    if not text[match.end():].strip() or path.stat().st_size > 1024 * 1024:
        raise ValueError("Skill body is empty or exceeds 1 MiB")
    return meta


def package_files(root: Path) -> list[Path]:
    files = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("Symlink in package")
        parts = path.relative_to(root).parts
        if any(part in EXCLUDED for part in parts):
            continue
        if path.is_file():
            if path.name == ".env" or (path.name.startswith(".env.") and not path.name.endswith(".example")):
                raise ValueError("Private environment file in package")
            if path.suffix.lower() in {".pem", ".key", ".p12", ".pfx"}:
                raise ValueError("Credential or certificate file in package")
            files.append(path)
    return files


def check_agent(path: Path, root: Path) -> None:
    data = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Agent YAML must be an object")
    interface = data.get("interface")
    if interface is not None:
        if not isinstance(interface, dict):
            raise ValueError("Agent interface must be an object")
        for field in ("display_name", "short_description"):
            if not isinstance(interface.get(field), str) or not interface[field].strip():
                raise ValueError(f"Missing agent {field}")
        if "default_prompt" in interface and (not isinstance(interface["default_prompt"], str) or not interface["default_prompt"].strip()):
            raise ValueError("Invalid agent default_prompt")
        for field in ("icon_small", "icon_large"):
            if field in interface:
                contained(path.parent.parent, "./" + interface[field].removeprefix("./"))
    policy = data.get("policy", {})
    if not isinstance(policy, dict) or set(policy) - {"products", "allow_implicit_invocation"}:
        raise ValueError("Invalid agent policy")
    if "allow_implicit_invocation" in policy and policy["allow_implicit_invocation"] is not None and not isinstance(policy["allow_implicit_invocation"], bool):
        raise ValueError("Invocation policy must be boolean")
    products = policy.get("products")
    if products is not None and (not isinstance(products, list) or any(p not in {"CHAT", "CODEX", "HERMES"} for p in products)):
        raise ValueError("Unsupported agent product policy")


def check_plugin(root: Path, schemas: dict) -> dict:
    manifest = read_json(root / "plugin.json")
    jsonschema.validate(manifest, schemas["plugin"])
    if manifest["name"] != root.name:
        raise ValueError("Plugin folder does not match its identity")
    extension = manifest.get("extensions", {}).get("com.openai", {})
    interface = extension.get("interface", {})
    if not isinstance(interface, dict):
        raise ValueError("Plugin interface must be an object")
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if key in interface and (not isinstance(interface[key], str) or not interface[key].strip()):
            raise ValueError(f"Invalid interface {key}")
    subtitle = interface.get("shortDescription", "")
    if len(subtitle) > 30:
        raise ValueError("Plugin subtitle exceeds 30 characters")
    capabilities = interface.get("capabilities", [])
    if not isinstance(capabilities, list) or any(not isinstance(c, str) or not c.strip() for c in capabilities):
        raise ValueError("Invalid capabilities")
    prompt = interface.get("defaultPrompt")
    if prompt is not None and not (isinstance(prompt, str) and prompt.strip() or isinstance(prompt, list) and 1 <= len(prompt) <= 3 and all(isinstance(s, str) and s.strip() for s in prompt)):
        raise ValueError("Invalid plugin defaultPrompt")
    for key in ("logo", "composerIcon", "logoDark", "composerIconDark"):
        if key in interface:
            contained(root, interface[key])
    apps = {}
    if "apps" in extension:
        apps = read_json(contained(root, extension["apps"])).get("apps", {})
        if not isinstance(apps, dict) or not apps:
            raise ValueError("Empty app mapping")
        for app in apps.values():
            if not isinstance(app, dict) or not re.fullmatch(r"(?:asdk_app_|connector_|templated_apps_)[a-zA-Z0-9][a-zA-Z0-9_-]*", app.get("id", "")):
                raise ValueError("Invalid app ID")
    mcp = read_json(root / "mcp.json") if (root / "mcp.json").exists() else None
    servers = []
    if mcp is not None:
        # The canonical 1.0 schema predates documented OpenAI server extensions.
        # Validate portable fields unchanged, then validate OpenAI auth separately.
        core = json.loads(json.dumps(mcp))
        for server in core.get("mcpServers", {}).values():
            server.pop("extensions", None)
        jsonschema.validate(core, schemas["mcp"])
        for key, server in mcp["mcpServers"].items():
            if server["type"] not in {"streamable-http", "sse"}:
                raise ValueError("This collection currently supports only remote MCP packages")
            url = urlsplit(server["url"])
            if url.scheme != "https" or not url.netloc or url.username or url.fragment:
                raise ValueError("Unsafe remote MCP URL")
            if server.get("headers"):
                raise ValueError("Embedded headers need credential review before export")
            ext = server.get("extensions", {})
            if not isinstance(ext, dict) or any(not isinstance(v, dict) for v in ext.values()):
                raise ValueError("Invalid MCP extension object")
            auth = ext.get("com.openai", {}).get("auth")
            if auth is not None:
                if not isinstance(auth, dict) or auth.get("type") not in {"none", "oauth", "mixed", "api_key"}:
                    raise ValueError("Invalid MCP auth")
                if auth["type"] == "api_key" and auth.get("headerScheme") not in {"bearer", "basic", "custom_header"}:
                    raise ValueError("Invalid API key header scheme")
                if auth.get("headerScheme") == "custom_header" and not auth.get("headerName"):
                    raise ValueError("Missing custom auth header")
            servers.append({"name": key, "url": server["url"], "auth": auth or {"type": "not_declared"}})
    skill_paths = sorted((root / "skills").glob("*/SKILL.md"))
    skills = [frontmatter(path)["name"] for path in skill_paths]
    if len(skills) != len(set(skills)) or not (skills or servers or apps):
        raise ValueError("Plugin has no valid component or has duplicate skills")
    compatibility = read_json(root / ".codex-plugin/plugin.json")
    for key in ("name", "version", "description"):
        if compatibility.get(key) != manifest.get(key):
            raise ValueError(f"Compatibility manifest differs: {key}")
    if compatibility.get("interface", {}) != interface:
        raise ValueError("Compatibility presentation differs")
    for key in ("skills", "mcpServers", "apps"):
        if key in compatibility:
            contained(root, compatibility[key])
    if mcp is not None:
        legacy = read_json(root / ".mcp.json").get("mcpServers", {})
        if set(legacy) != {s["name"] for s in servers}:
            raise ValueError("Compatibility MCP server names differ")
        for key, server in mcp["mcpServers"].items():
            if legacy[key].get("url") != server["url"]:
                raise ValueError("Compatibility MCP endpoint differs")
    return {"skills": skills, "mcp": servers, "apps": apps}


def inspect(root: Path, kind: str, schemas: dict) -> dict:
    row = {"name": root.name, "kind": kind, "path": root.relative_to(ROOT).as_posix(), "errors": [], "warnings": [], "runtime": "NAO_TESTADO"}
    try:
        files = package_files(root)
        row["files"] = len(files)
        row["sha256"] = {p.relative_to(root).as_posix(): digest(p) for p in files}
        if kind == "plugin":
            row.update(check_plugin(root, schemas))
        else:
            row["description"] = frontmatter(root / "SKILL.md")["description"]
        for path in files:
            if path.suffix == ".json":
                read_json(path)
            elif path.suffix in {".yaml", ".yml"}:
                yaml.safe_load(path.read_text(encoding="utf-8-sig"))
                if path.parent.name == "agents":
                    check_agent(path, root)
            elif path.suffix == ".py":
                ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
            elif path.suffix == ".svg":
                svg = ET.parse(path).getroot()
                if path.name == "plugin-icon.svg" and (svg.get("width") != "256" or svg.get("height") != "256" or svg.get("viewBox") != "0 0 256 256"):
                    raise ValueError("Plugin icon must use the collection's 256px canvas")
            if path.suffix == ".md":
                text = path.read_text(encoding="utf-8-sig")
                if path.name in {"SKILL.md", "original.md"} and re.search(r"\b(?:odoo|medusa)\b", text, re.I):
                    raise ValueError(f"Retired platform reference: {path.relative_to(root)}")
                for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", text):
                    target = unquote(target.split("#")[0])
                    if not target or urlsplit(target).scheme or target.startswith("/") or any(c in target for c in "{}<>"):
                        continue
                    resolved = (path.parent / target).resolve()
                    if not resolved.exists() or not resolved.is_relative_to(root.resolve()):
                        row["warnings"].append(f"Reference needs review: {path.relative_to(root).as_posix()} -> {target}")
        row["structural"] = "APROVADO"
    except (ValueError, OSError, SyntaxError, yaml.YAMLError, jsonschema.ValidationError, KeyError, TypeError, ET.ParseError) as exc:
        # Do not echo configuration values in errors.
        row["errors"].append(f"{type(exc).__name__}: {str(exc).splitlines()[0] if not isinstance(exc, jsonschema.ValidationError) else 'JSON Schema mismatch at ' + '/'.join(str(v) for v in exc.path)}")
        row["structural"] = "REPROVADO"
    return row


def refresh_schemas() -> None:
    for name in ("plugin", "mcp"):
        url = SCHEMA_BASE + name + ".schema.json"
        with urlopen(url, timeout=25) as response:
            schema = json.load(response)
        jsonschema.Draft202012Validator.check_schema(schema)
        write_json(ROOT / "scripts/schemas" / (name + ".schema.json"), schema)


def catalogue() -> list[dict]:
    schemas = {name: read_json(ROOT / "scripts/schemas" / (name + ".schema.json")) for name in ("plugin", "mcp")}
    mapping = read_json(ROOT / "relatorios/mapa-organizacao.json")
    labels = {r["name"]: r for r in mapping}
    rows = []
    for directory, kind in (("skills", "skill"), ("plugins", "plugin")):
        for root in sorted((ROOT / directory).iterdir()):
            if root.is_dir():
                row = inspect(root, kind, schemas)
                label = labels.get(root.name, {})
                row.update({"label": label.get("acervo", root.name), "purpose": label.get("funcao", ""), "previous_path": label.get("acervo", root.name)})
                rows.append(row)
    generated = datetime.now(timezone.utc).isoformat()
    write_json(ROOT / "catalogo.json", {"generated_at": generated, "validation": "Portable core JSON Schemas 1.0.0 plus documented OpenAI extensions; static checks do not prove runtime behavior.", "items": rows})
    lines = ["# Catálogo de capacidades", "", f"Gerado em {generated}.", "", "Nomes de pasta seguem os IDs dos manifestos; a coluna Função mantém os nomes descritivos.", "", "| Tipo | Identificador / pasta | Função | Estrutura | Execução |", "| --- | --- | --- | --- | --- |"]
    for row in rows:
        lines.append(f"| {row['kind']} | [{row['name']}]({row['path']}/) | {row['label']} | {row['structural']} | {row['runtime']} |")
    lines += ["", "## Integrações e limitações", "", "Veja [integrações verificadas](relatorios/integracoes.json) e [casos de aceite](CASOS-DE-ACEITE.md).", "", "## Referências que exigem revisão", ""]
    for row in rows:
        for warning in row["warnings"]:
            lines.append(f"- {row['name']}: {warning}")
        for error in row["errors"]:
            lines.append(f"- ERRO {row['name']}: {error}")
    (ROOT / "CATALOGO.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"items": len(rows), "approved": sum(r["structural"] == "APROVADO" for r in rows), "errors": {r["name"]: r["errors"] for r in rows if r["errors"]}, "warnings": {r["name"]: r["warnings"] for r in rows if r["warnings"]}}, ensure_ascii=False, indent=2))
    return rows


def export(rows: list[dict]) -> None:
    if any(row["errors"] for row in rows):
        raise ValueError("Export refused: resolve structural errors first")
    index = []
    schemas = {name: read_json(ROOT / "scripts/schemas" / (name + ".schema.json")) for name in ("plugin", "mcp")}
    for row in rows:
        root = ROOT / row["path"]
        destination = ROOT / "dist" / (row["kind"] + "s") / (root.name + ".zip")
        destination.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, strict_timestamps=False) as archive:
            for file in package_files(root):
                # Standalone skills need their name folder; plugins are at ZIP root.
                path = file.relative_to(root).as_posix()
                archive.write(file, root.name + "/" + path if row["kind"] == "skill" else path)
        with zipfile.ZipFile(destination) as archive:
            if archive.testzip() is not None:
                raise ValueError("Corrupt archive")
            if len(archive.infolist()) != row["files"]:
                raise ValueError("Archive file count mismatch")
            for file, expected in row["sha256"].items():
                member = root.name + "/" + file if row["kind"] == "skill" else file
                if hashlib.sha256(archive.read(member)).hexdigest() != expected:
                    raise ValueError("Archive content differs from validated source")
            # Check component discovery after extraction into an isolated directory.
            # This is an install-layout check, not installation into a live host.
            with tempfile.TemporaryDirectory(prefix="avila-plugin-check-") as temporary:
                staging = Path(temporary).resolve()
                target = staging / root.name if row["kind"] == "plugin" else staging
                target.mkdir(parents=True, exist_ok=True)
                for member in archive.namelist():
                    if not (target / member).resolve().is_relative_to(target):
                        raise ValueError("Archive member escapes staging directory")
                archive.extractall(target)
                installed_root = staging / root.name
                if row["kind"] == "plugin":
                    check_plugin(installed_root, schemas)
                else:
                    frontmatter(installed_root / "SKILL.md")
        index.append({"path": destination.relative_to(ROOT).as_posix(), "sha256": digest(destination), "files": row["files"], "status": "ARQUIVO_VERIFICADO", "installation_layout": "EXTRACAO_E_DESCOBERTA_VALIDADA", "host_execution": "NAO_TESTADA", "public_submission": "NAO_PREPARADO"})
    write_json(ROOT / "dist/indice.json", index)
    print(f"Exported and verified {len(index)} archives")


def probe() -> None:
    rows = read_json(ROOT / "catalogo.json")["items"]
    urls = sorted({server["url"] for row in rows for server in row.get("mcp", [])})
    results = []
    for url in urls:
        request = Request(url, headers={"Accept": "application/json, text/event-stream", "User-Agent": "AvilaOps-Capability-Audit/1.0"})
        try:
            with urlopen(request, timeout=15) as response:
                status = response.status
                content_type = response.headers.get("Content-Type", "")
        except HTTPError as exc:
            status, content_type = exc.code, exc.headers.get("Content-Type", "")
        except (URLError, TimeoutError, OSError):
            results.append({"url": url, "status": "FALHA_DE_REDE", "authenticated": False})
            continue
        results.append({"url": url, "http_status": status, "content_type": content_type, "status": "REQUER_AUTENTICACAO" if status in {401, 403} else "HTTP_RESPONDEU", "authenticated": False, "mcp_session": "NAO_TESTADA"})
    write_json(ROOT / "relatorios/endpoints.json", {"checked_at": datetime.now(timezone.utc).isoformat(), "note": "Unauthenticated GET only; an HTTP response does not prove MCP initialization or module access.", "endpoints": results})
    print(json.dumps(results, ensure_ascii=False, indent=2))


def preservation() -> None:
    baseline = read_json(ROOT / "relatorios/baseline.json")
    mapping = read_json(ROOT / "relatorios/mapa-organizacao.json")
    rows = []
    for entry in baseline["files"]:
        old = ROOT / entry["path"]
        current = None
        for item in mapping:
            original_root = Path(item["origem"])
            if old.is_relative_to(original_root):
                current = Path(item["destino"]) / old.relative_to(original_root)
                break
        if current is None:
            archived = ROOT / "_historico/renomeacao-inicial" / old.name
            current = archived if archived.exists() else old
        state = "AUSENTE" if not current.is_file() else "PRESERVADO" if digest(current) == entry["sha256"] else "ATUALIZADO"
        rows.append({"before": entry["path"], "after": current.relative_to(ROOT).as_posix(), "state": state})
    result = {"backup": baseline["archive"], "backup_verified": digest(ROOT / baseline["archive"]) == baseline["archive_sha256"], "original_files": len(rows), "counts": {state: sum(r["state"] == state for r in rows) for state in ("PRESERVADO", "ATUALIZADO", "AUSENTE")}, "files": rows}
    write_json(ROOT / "relatorios/preservacao.json", result)
    if not result["backup_verified"] or result["counts"]["AUSENTE"]:
        raise ValueError("Original file or backup missing")
    print(json.dumps({k: v for k, v in result.items() if k != "files"}, ensure_ascii=False, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("schemas", "validate", "package", "probe", "preservation"))
    args = parser.parse_args()
    if args.command == "schemas":
        refresh_schemas()
        return 0
    if args.command == "probe":
        probe()
        return 0
    if args.command == "preservation":
        preservation()
        return 0
    rows = catalogue()
    if args.command == "package":
        export(rows)
    return int(any(row["errors"] for row in rows))


if __name__ == "__main__":
    sys.exit(main())
