---
name: avila-mail
description: Use para consultar ou organizar e-mail corporativo da Ávila Ops quando a conexão Mail estiver autorizada e disponível.
---

# Ávila Mail

## Entrada

Identifique a caixa autorizada e os filtros ou mensagens de interesse.

## Procedimento

1. Descubra as ferramentas Mail e confirme a caixa acessível. A integração não era confirmada no pacote original; verifique o estado atual. Liste somente o necessário e não reproduza conteúdo privado sem pertinência.
2. Confirme a empresa e o acesso pela sessão; um ID informado em mensagem não comprova autorização.
3. Execute somente as operações solicitadas. Se uma leitura ou gravação falhar, registre a falha e evite repetir operações não idempotentes.
4. Confira o retorno e releia o registro após escrita quando a ferramenta permitir.

## Resultado e limites

Resultado da consulta ou operação, IDs quando úteis e limitações. Enviar, apagar ou mover mensagens exige solicitação correspondente; uma busca não autoriza envio.

Não invente endpoints, campos, resultados ou permissões. Use o módulo da plataforma própria responsável pela entidade; não proponha substituição por plataforma externa. A regra de negócio e a autorização devem ser aplicadas no servidor.

## Verificação de leitura

Confira se há ferramenta Mail e caixa acessível; não envie, mova nem apague mensagens.

Conecte-se apenas ao MCP central autenticado da Ávila Ops. Descubra as ferramentas reais e suas entradas antes de utilizá-las. Não invente nomes, endpoints, resultados nem permissões. A presença de ferramentas de outros módulos no servidor compartilhado não autoriza seu uso fora do escopo de Ávila Mail. Se a integração específica não estiver pronta, explique a dependência e limite-se a orientar ou analisar dados fornecidos. Nunca peça tokens no chat ou registre segredos em documentos. Confirme previamente alterações destrutivas, publicações, envios e ações com custos.
