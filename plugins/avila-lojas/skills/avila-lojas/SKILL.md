---
name: avila-lojas
description: Use para consultar e operar produtos, pedidos e estoque nas lojas da plataforma própria Ávila Ops.
---

# Ávila Lojas

## Entrada

Identifique a loja autorizada pela sessão e o produto, pedido ou lote solicitado.

## Procedimento

1. Descubra as ferramentas Lojas e seus esquemas. Consulte registros antes de escrever, verifique SKU/ID e mantenha isolamento por empresa. Use os serviços do módulo responsável para preservar as regras comerciais.
2. Confirme a empresa e o acesso pela sessão; um ID informado em mensagem não comprova autorização.
3. Execute somente as operações solicitadas. Se uma leitura ou gravação falhar, registre a falha e evite repetir operações não idempotentes.
4. Confira o retorno e releia o registro após escrita quando a ferramenta permitir.

## Resultado e limites

Loja, registros e IDs, alterações confirmadas, falhas por item e estado final. Etiquetas podem gerar custos e mudanças de status podem notificar clientes; execute esses efeitos somente no escopo solicitado.

Não invente endpoints, campos, resultados ou permissões. Use o módulo da plataforma própria responsável pela entidade; não proponha substituição por plataforma externa. A regra de negócio e a autorização devem ser aplicadas no servidor.

## Verificação de leitura

Consulte um produto da loja autorizada, sem mudar preço, estoque, pedido ou publicação.

Conecte-se apenas ao MCP central autenticado da Ávila Ops. Descubra as ferramentas reais e suas entradas antes de utilizá-las. Não invente nomes, endpoints, resultados nem permissões. A presença de ferramentas de outros módulos no servidor compartilhado não autoriza seu uso fora do escopo de Ávila Lojas. Se a integração específica não estiver pronta, explique a dependência e limite-se a orientar ou analisar dados fornecidos. Nunca peça tokens no chat ou registre segredos em documentos. Confirme previamente alterações destrutivas, publicações, envios e ações com custos.
