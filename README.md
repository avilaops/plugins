# Acervo Ávila Ops

Acervo local de **20 skills avulsas e 12 plugins**, organizado para revisão, validação e exportação privada. Não houve instalação dos pacotes no host nem execução dos 32 fluxos por um modelo.

## Navegação

- [Catálogo completo](CATALOGO.md) e [dados do catálogo](catalogo.json).
- [Plataforma própria e integrações](PLATAFORMA.md).
- [Casos de aceite](CASOS-DE-ACEITE.md).
- [Galeria dos 12 ícones](IMAGENS.html).
- [Mapa dos caminhos e nomes](relatorios/mapa-organizacao.json).
- [Baseline de preservação](relatorios/baseline.json).

## Estrutura

`skills/<name>/SKILL.md` contém skills independentes. `plugins/<name>/` contém o manifesto portátil `plugin.json`, a configuração MCP quando aplicável e o manifesto de compatibilidade em `.codex-plugin/plugin.json`.

Os identificadores técnicos foram preservados. Os diretórios usam o `name` declarado para manter coerência com os manifestos e a instalação das skills. O nome funcional da organização anterior é um rótulo do catálogo, não um novo ID de instalação. Por exemplo, `avila-engenharia-operacoes` corresponde ao plugin `avila-ops-skills`. Os originais preservados ficam em `_historico/`; os registros da renomeação inicial ficam em `_historico/renomeacao-inicial/`.

## Comandos

Execute na raiz deste acervo, com Python 3. Instale as dependências somente se ainda não estiverem disponíveis:

```powershell
py -3 -m pip install -r scripts/requirements.txt
```

Valide estrutura, manifestos, caminhos, frontmatter e arquivos; o comando atualiza o catálogo e os relatórios:

```powershell
py -3 scripts/acervo.py validate
```

Execute os testes do validador:

```powershell
py -3 -m unittest discover -s scripts -p test_acervo.py
```

Exporte os pacotes após a validação:

```powershell
py -3 scripts/acervo.py package
```

Os ZIPs ficam em `dist/plugins/` e `dist/skills/`; `dist/indice.json` registra hashes. A exportação confere o conteúdo contra a fonte validada e extrai cada ZIP em uma pasta temporária isolada para validar a descoberta dos componentes. Essa simulação verifica o layout de instalação, sem instalar ou executar um plugin no host. São arquivos para distribuição privada/local, sem preparação para submissão pública.

Verifique a resposta HTTP dos endpoints sem autenticação:

```powershell
py -3 scripts/acervo.py probe
```

O resultado fica em `relatorios/endpoints.json`. Esse comando usa GET sem credenciais: não inicializa sessão MCP nem comprova acesso aos módulos.

Para atualizar os schemas usados pelo validador:

```powershell
py -3 scripts/acervo.py schemas
```

O cache fica em `scripts/schemas/`. A atualização exige rede; a validação utiliza os arquivos locais.

Confira a preservação contra o baseline:

```powershell
py -3 scripts/acervo.py preservation
```

O resultado fica em `relatorios/preservacao.json`. Use esse relatório para distinguir arquivos preservados, alterações deliberadas e novos artefatos.

## Instalação e execução

O acervo não instala pacotes automaticamente. Escolha o ZIP e o mecanismo de importação aceito pelo host, confirme identidade e permissões da conexão e execute o caso de aceite correspondente. O diretório das skills nos ZIPs avulsos mantém seu `name`; os plugins têm seus arquivos na raiz do ZIP.

Não coloque tokens, certificados ou arquivos privados nos pacotes. Configure credenciais no host autorizado. Validação estrutural e integridade do ZIP não comprovam execução do fluxo, autorização externa ou isolamento de clientes.

## Manutenção

Após qualquer alteração em instruções, documentação, ícones ou manifestos, rode `validate`, os testes pertinentes e `package` novamente. Registre no aceite o host, a data, a entrada, a saída observada e eventuais limites; não promova `NAO_EXECUTADO` a aprovado sem evidência.

## Referências de formato

- [Empacotamento oficial OpenAI](https://developers.openai.com/plugins/build/plugins).
- [Criação de skills](https://developers.openai.com/plugins/build/skills).

O validador usa os schemas portáteis Agent Plugins 1.0.0 e verificações adicionais para os campos OpenAI utilizados neste acervo. O schema MCP publicado não inclui o campo de extensão documentado pela OpenAI: o núcleo portátil é validado separadamente das opções de autenticação em `extensions.com.openai`. Não é um teste de conformidade de todos os recursos possíveis de um host.
