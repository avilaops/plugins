"""Regression checks for package boundaries and invalid input."""

import json
from pathlib import Path
import tempfile
import unittest

import jsonschema

from acervo import ROOT, check_agent, contained, frontmatter, package_files


class CollectionChecks(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_rejects_parent_traversal_even_when_target_exists(self):
        self.write("outside.txt", "data")
        child = self.root / "plugin"
        child.mkdir()
        with self.assertRaises(ValueError):
            contained(child, "./../outside.txt")

    def test_requires_existing_package_resource(self):
        with self.assertRaises(ValueError):
            contained(self.root, "./missing.png")

    def test_rejects_skill_name_different_from_directory(self):
        path = self.write("correct/SKILL.md", "---\nname: wrong\ndescription: Useful workflow.\n---\nSteps.\n")
        with self.assertRaises(ValueError):
            frontmatter(path)

    def test_rejects_empty_skill_procedure(self):
        path = self.write("correct/SKILL.md", "---\nname: correct\ndescription: Useful workflow.\n---\n")
        with self.assertRaises(ValueError):
            frontmatter(path)

    def test_refuses_private_environment_files(self):
        self.write(".env", "EXAMPLE=not-a-real-secret")
        with self.assertRaises(ValueError):
            package_files(self.root)

    def test_ignores_dependency_directories_but_keeps_examples(self):
        self.write("node_modules/dependency/file.js", "example")
        self.write(".env.example", "EXAMPLE=")
        self.assertEqual([p.name for p in package_files(self.root)], [".env.example"])

    def test_rejects_string_invocation_policy(self):
        path = self.write("skill/agents/openai.yaml", 'policy:\n  allow_implicit_invocation: "false"\n')
        with self.assertRaises(ValueError):
            check_agent(path, self.root)

    def test_rejects_unsupported_product_restrictions(self):
        path = self.write("skill/agents/openai.yaml", 'policy:\n  products: [chatgpt, api]\n')
        with self.assertRaises(ValueError):
            check_agent(path, self.root)

    def test_schema_rejects_unknown_portable_manifest_field(self):
        schema = json.loads((ROOT / "scripts/schemas/plugin.schema.json").read_text())
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate({"$schema": schema["$id"], "name": "example", "skills": "./skills/"}, schema)


if __name__ == "__main__":
    unittest.main()
