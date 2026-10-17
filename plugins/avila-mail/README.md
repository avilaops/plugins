# avila-mail

![Ícone de avila-mail](assets/plugin-icon.svg)

## Identificação e função

- ID técnico preservado: `avila-mail`.
- Nome funcional: `avila-mail`.
- Função: E-mail corporativo; a skill registra integracao nao confirmada.

O manifesto portátil fica em [plugin.json](plugin.json); o manifesto de compatibilidade fica em [.codex-plugin/plugin.json](.codex-plugin/plugin.json). O nome funcional não substitui o ID técnico.

## Skills incluídas

- [avila-mail](skills/avila-mail/SKILL.md).

## Conexão e dependências

Endpoint declarado: `https://mcp.avilaops.com/mcp`, transporte `streamable-http`, autenticação `api_key` com esquema `bearer`. Configure a credencial individual no host; o pacote não contém token.

Dependência para o aceite: Host, MCP central autenticado e ferramentas específicas autorizadas. A orientação completa está em PLATAFORMA.md no acervo central.

## Exemplo de leitura ou análise

> Verifique as ferramentas de avila-mail disponíveis e apresente o que é possível consultar sem alterar dados.

## Validação e limites

Instalação local no host: não realizada. Execução deste pacote por modelo/host: `NAO_TESTADO`. Caso de aceite: `NAO_EXECUTADO`. Execute o prompt de exemplo acima e registre a saída, a data, o host e o escopo autorizado. A matriz completa fica em CASOS-DE-ACEITE.md no acervo central.

A configuração aponta para o MCP central, mas a inspeção do grafo central não identificou nós específicos deste módulo. É necessário descobrir e testar suas ferramentas antes de declarar integração operacional.

A presença de arquivos, ícone ou configuração não comprova disponibilidade de ferramentas nem autorização. Use dados de teste e respeite o escopo do usuário. A documentação de exportação fica no README.md do acervo central. Os ZIPs são privados/locais e não representam submissão pública.


## Plataforma própria e verificação local

A Ávila Ops usa plataforma própria. Não adote Odoo ou Medusa como dependência padrão. Descubra os contratos e ferramentas reais; não presuma stack, endpoints, dados ou permissões. O servidor deve impor autorização e isolamento por empresa.

Na raiz do acervo central, execute a validação estrutural antes de exportar:

```powershell
py -3 scripts/acervo.py validate
```

Esse comando pertence ao acervo central, não ao ZIP isolado. Para o aceite deste pacote, a resposta ao prompt deve usar somente as fontes fornecidas ou ferramentas disponíveis, explicitar bloqueios e não realizar gravações. Validação estrutural não substitui essa execução no host.

