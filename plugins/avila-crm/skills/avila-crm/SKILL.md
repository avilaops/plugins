---
name: avila-crm
description: Use para consultar ou organizar clientes e atividades no CRM da plataforma própria Ávila Ops, quando houver ferramentas específicas disponíveis.
---

# Ávila CRM

## Entrada

Identifique cliente, empresa e atividade desejada; peça um identificador quando houver homônimos.

## Procedimento

1. Verifique a existência de ferramentas próprias do CRM antes de acessar cadastros. Contatos de WhatsApp não comprovam integração CRM. A indicação antiga de adaptador pendente é uma dependência a verificar, não prova atual de indisponibilidade.
2. Confirme a empresa e o acesso pela sessão; um ID informado em mensagem não comprova autorização.
3. Execute somente as operações solicitadas. Se uma leitura ou gravação falhar, registre a falha e evite repetir operações não idempotentes.
4. Confira o retorno e releia o registro após escrita quando a ferramenta permitir.

## Resultado e limites

Cliente e registros efetivamente consultados ou alterados, IDs e pendências. Sem ferramenta específica, organize apenas os dados fornecidos e informe que o CRM não foi atualizado.

Não invente endpoints, campos, resultados ou permissões. Use o módulo da plataforma própria responsável pela entidade; não proponha substituição por plataforma externa. A regra de negócio e a autorização devem ser aplicadas no servidor.

## Verificação de leitura

Descubra o esquema de uma ferramenta CRM de leitura; sem adaptador, registre a dependência sem simular consulta.

Conecte-se apenas ao MCP central autenticado da Ávila Ops. Descubra as ferramentas reais e suas entradas antes de utilizá-las. Não invente nomes, endpoints, resultados nem permissões. A presença de ferramentas de outros módulos no servidor compartilhado não autoriza seu uso fora do escopo de Ávila CRM. Se a integração específica não estiver pronta, explique a dependência e limite-se a orientar ou analisar dados fornecidos. Nunca peça tokens no chat ou registre segredos em documentos. Confirme previamente alterações destrutivas, publicações, envios e ações com custos.
