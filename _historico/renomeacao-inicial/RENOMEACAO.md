# Nomes do acervo local

As 32 pastas foram analisadas pelos manifestos, metadados, procedimentos das
skills, recursos e configuracoes de integracao. O mapa completo, incluindo a
funcao de cada pasta e o nome anterior, esta em `renomeacao-pastas.json`.

## Convencao

- Nomes em minusculas, sem acentos e separados por hifens.
- Skills avulsas recebem nomes que descrevem a atividade.
- Plugins corporativos mantem a marca `avila` no inicio.
- Nomes de produtos e protocolos sao preservados quando identificam o escopo.
- O app sem descricao funcional recebe um nome neutro com parte de seu ID.

## Limites da alteracao

A renomeacao abrange somente as pastas externas deste acervo. Os arquivos,
metadados `name`, comandos de invocacao, IDs de apps, referencias de autoria,
licencas e configuracoes MCP permanecem intactos. Os nomes externos deste acervo
nao substituem os identificadores internos para invocar ou instalar skills.
Ao instalar uma skill avulsa, a pasta de instalacao deve acompanhar o `name`
declarado em seu `SKILL.md` original.

As embalagens duplicadas de `auth-md` e `automador-puro` foram preservadas.
Nao houve instalacao de plugins nem verificacao de conectividade dos servicos.
Configuracoes externas que apontem para os caminhos antigos nao foram alteradas.

## Achados da leitura

- CRM e TMS registram adaptadores pendentes nas respectivas skills.
- Mail registra integracao ainda nao confirmada.
- O pacote de n8n configura MCP e nao contem skills.
- O conjunto de engenharia e operacoes contem cinco skills.
- A skill de edicao de texto atende ingles, nao portugues.
- O pacote de anuncios produz videos; nao se limita a animacao de interfaces.
- O app `6ad0a0086b188191928c20e0cf70d6fe` tem descricao generica `app`;
  nao foi atribuida a ele uma funcao de negocio sem evidencia.
- Os pacotes avulsos de automacao e sincronizacao citam Odoo e Medusa, enquanto
  o conjunto corporativo de engenharia orienta nao adota-los como padrao.
  Essa divergencia de instrucoes foi identificada e preservada: sua revisao
  nao faz parte da renomeacao.

## Verificacao

`verificacao-renomeacao.json` registra o resultado da comparacao SHA-256 de
todos os arquivos dos pacotes antes e depois da renomeacao.
