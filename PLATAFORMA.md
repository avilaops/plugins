# Plataforma própria Ávila Ops

## Fonte das regras

O usuário confirmou que a empresa usa sua própria plataforma e deixou de usar Odoo e Medusa. Novas automações e sincronizações devem partir dos sistemas próprios e dos contratos efetivamente encontrados no projeto.

Não presumir stack, tabelas, endpoints, autenticação, módulos ou regras de negócio. Leia a documentação e o código do sistema envolvido e descubra as ferramentas disponíveis antes de propor uma integração. Referências históricas preservadas não são instruções operacionais atuais.

## Responsabilidades

A skill orienta a sequência de trabalho. O plugin distribui instruções e configurações. O servidor MCP ou a API própria executa operações e impõe autorização, isolamento por empresa e regras de negócio.

Uma descrição de ferramenta não concede acesso. Preços, estoque, clientes, pedidos e dados fiscais devem vir da fonte autorizada; informações ausentes ou falhas precisam aparecer no resultado.

## Conexões declaradas

| Pacotes | Endpoint | Autenticação declarada |
| --- | --- | --- |
| avila-cms, avila-crm, avila-lojas, avila-mail, avila-notas, avila-tms, lojas-clientes | https://mcp.avilaops.com/mcp | API key, esquema bearer |
| n8n-avilaops | https://n8n.avilaops.com/mcp-server/http | Manifesto sem tipo explícito; autorização do próprio n8n |
| apple-avila, avila-design, avila-ops-skills | Sem MCP empacotado | Dependem dos recursos disponíveis no host |
| dev-6ad0a0086b188191928c20e0cf70d6fe | Referência a app em .app.json | Identidade, função e acesso a confirmar no host |

## Evidência e limites

Na inspeção de 17/10/2026, uma chamada à ferramenta n8n `search_workflows` respondeu. O workflow central `IwW8JvEPEkBb6yah` estava ativo, com `activeVersionId=e82fb45d-1a9b-4aa7-b755-ef3de1552bef` e `sameAsDraft=true`.

O grafo inspecionado continha nós de CMS, Notas, Lojas e Fiscal. Isso confirma presença na configuração, sem comprovar acesso funcional a cada módulo. Não foram identificados nós de CRM, TMS ou Mail nesse grafo; a ausência nessa inspeção não demonstra inexistência em toda a plataforma.

GET sem autenticação para o MCP central retornou HTTP 401. Esse resultado indica exigência de autenticação; não é validação de uma sessão MCP autenticada.

Os pacotes deste acervo não foram instalados no host. Sua execução por modelo/host permanece `NAO_TESTADO`; os casos de aceite permanecem `NAO_EXECUTADO`. Uma conexão existente na sessão não equivale à instalação dos ZIPs locais.

## Critério de integração concluída

1. Identificar o usuário, empresa e recurso autorizado.
2. Confirmar ferramenta ou contrato real e autenticação pelo host.
3. Executar uma leitura mínima sem alteração de dados.
4. Registrar saída, horário e limitações sem expor credenciais.
5. Testar gravações somente dentro do escopo solicitado e conferir o resultado persistido.

CRM, TMS e Mail exigem descoberta e teste de ferramentas específicas antes de anunciar integração operacional. O app de ID técnico preservado exige identificação da função antes de uso.

