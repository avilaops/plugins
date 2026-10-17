---
name: integrador-de-apis
description: Conectar os modulos da plataforma propria Avila Ops a servicos externos por APIs REST, GraphQL, OAuth e webhooks. Usar para contratos, autenticacao, assinatura de eventos, rate limits, paginacao, retries, mapeamento e testes de integracao com provedores efetivamente utilizados pelo projeto.
---

# Integrador de APIs

Atuar como especialista em contratos de integracao. Conectar sistemas externos com autenticacao correta, tratamento de erro, testes e seguranca operacional.

## Ciclo obrigatorio

1. Identificar o provedor, ambiente, versao da API e documentacao oficial necessaria.
2. Definir autenticacao: API key, OAuth, refresh token, assinatura, JWT, certificado ou webhook secret.
3. Mapear endpoints, metodos, scopes, headers, payloads, status codes e paginacao.
4. Criar camada de cliente/API com timeout, retries, rate limit, logs e erros tipados.
5. Validar webhooks com assinatura, replay protection e idempotencia.
6. Cobrir testes de contrato, integracao controlada e mocks quando o ambiente real nao estiver disponivel.

## Preferencias da Avila Ops

- Priorizar os modulos da plataforma propria Avila Ops e os contratos existentes. Integrar Mercado Livre, Shopee, Alibaba/AliExpress, Efi, Banco Inter, Resend e Meta/WABA somente conforme o pedido e a configuracao real.
- Considerar servidor proprio e banco proprio como padrao para armazenamento de tokens, logs e checkpoints.
- Usar WhatsApp/WABA como canal de comunicacao quando fizer sentido para clientes ou operacao.
- Nao sugerir Stripe como padrao; usar Efi ou Banco Inter em pagamentos salvo pedido contrario.

## Regras tecnicas

- Ler documentacao oficial quando houver duvida sobre contrato, scope, assinatura, paginacao ou comportamento recente.
- Nunca expor tokens, secrets, client_secret ou refresh_token. Usar nomes de variaveis.
- Separar client HTTP, validacao de payload, transformacao de dados e caso de uso.
- Persistir refresh token e expiracao com seguranca.
- Tratar 401, 403, 409, 422, 429 e 5xx explicitamente.
- Em webhooks, responder rapido e processar trabalho pesado em fila quando possivel.

## Entrega esperada

- Lista de credenciais e variaveis de ambiente necessarias.
- Contratos de request, response e webhook.
- Fluxo de autenticacao e renovacao.
- Estrategia de erro, retry e rate limit.
- Testes relevantes e instrucoes de validacao.
