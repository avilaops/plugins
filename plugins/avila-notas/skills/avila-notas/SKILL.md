---
name: avila-notas
description: Use para consultar, criar ou organizar documentos e coleções do Notas da plataforma própria Ávila Ops.
---

# Ávila Notas

## Entrada

Identifique assunto, coleção ou documento e se o pedido é consulta, criação ou atualização.

## Procedimento

1. Use a conexão autenticada existente pelo MCP central; não crie um gateway separado. Descubra ferramentas Notas e seus esquemas. Antes de criar, procure por título e origem; antes de editar, leia a versão existente e preserve conteúdo pertinente.
2. Confirme a empresa e o acesso pela sessão; um ID informado em mensagem não comprova autorização.
3. Execute somente as operações solicitadas. Se uma leitura ou gravação falhar, registre a falha e evite repetir operações não idempotentes.
4. Confira o retorno e releia o registro após escrita quando a ferramenta permitir.

## Resultado e limites

Documento consultado ou salvo, ID ou link retornado, alteração realizada e pendências. Criar ou editar somente dentro do pedido; excluir exige solicitação correspondente.

Não invente endpoints, campos, resultados ou permissões. Use o módulo da plataforma própria responsável pela entidade; não proponha substituição por plataforma externa. A regra de negócio e a autorização devem ser aplicadas no servidor.

## Verificação de leitura

Descubra ferramentas Notas e consulte metadados de um documento autorizado; não grave alterações.

Conecte-se apenas ao MCP central autenticado da Ávila Ops. Descubra as ferramentas reais e suas entradas antes de utilizá-las. Não invente nomes, endpoints, resultados nem permissões. A presença de ferramentas de outros módulos no servidor compartilhado não autoriza seu uso fora do escopo de Ávila Notas. Se a integração específica não estiver pronta, explique a dependência e limite-se a orientar ou analisar dados fornecidos. Nunca peça tokens no chat ou registre segredos em documentos. Confirme previamente alterações destrutivas, publicações, envios e ações com custos.
