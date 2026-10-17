---
name: avila-cms
description: Use para consultar, redigir ou revisar conteúdo, páginas e mídia no CMS da plataforma própria Ávila Ops.
---

# Ávila CMS

## Entrada

Identifique o site, empresa, página ou conteúdo e a operação solicitada.

## Procedimento

1. Descubra ferramentas do módulo CMS, incluindo cms_* quando expostas, e leia seus esquemas. Localize o registro antes de alterá-lo; use rascunho quando suportado.
2. Confirme a empresa e o acesso pela sessão; um ID informado em mensagem não comprova autorização.
3. Execute somente as operações solicitadas. Se uma leitura ou gravação falhar, registre a falha e evite repetir operações não idempotentes.
4. Confira o retorno e releia o registro após escrita quando a ferramenta permitir.

## Resultado e limites

Conteúdo encontrado ou alterado, identificador, estado de publicação e pendências. Não publique, despublique ou apague mídia e redirecionamentos sem solicitação correspondente.

Não invente endpoints, campos, resultados ou permissões. Use o módulo da plataforma própria responsável pela entidade; não proponha substituição por plataforma externa. A regra de negócio e a autorização devem ser aplicadas no servidor.

## Verificação de leitura

Consulte uma página existente e confirme título, ID e estado sem gravar alterações.

Conecte-se apenas ao MCP central autenticado da Ávila Ops. Descubra as ferramentas reais e suas entradas antes de utilizá-las. Não invente nomes, endpoints, resultados nem permissões. A presença de ferramentas de outros módulos no servidor compartilhado não autoriza seu uso fora do escopo de Ávila CMS. Se a integração específica não estiver pronta, explique a dependência e limite-se a orientar ou analisar dados fornecidos. Nunca peça tokens no chat ou registre segredos em documentos. Confirme previamente alterações destrutivas, publicações, envios e ações com custos.
