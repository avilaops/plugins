---
name: avila-tms
description: Use para consultar transportes, cargas, entregas e comprovantes no TMS próprio da Ávila Ops quando houver ferramentas específicas disponíveis.
---

# Ávila TMS

## Entrada

Identifique empresa, carga, entrega ou comprovante pelo identificador fornecido.

## Procedimento

1. Descubra ferramentas específicas do TMS e leia seus esquemas. Ferramentas fiscal_* não equivalem a acesso geral a cargas ou motoristas. Verifique a dependência de adaptador registrada no pacote original, sem afirmar que ele está conectado.
2. Confirme a empresa e o acesso pela sessão; um ID informado em mensagem não comprova autorização.
3. Execute somente as operações solicitadas. Se uma leitura ou gravação falhar, registre a falha e evite repetir operações não idempotentes.
4. Confira o retorno e releia o registro após escrita quando a ferramenta permitir.

## Resultado e limites

Registro de transporte consultado ou alterado, ID, status confirmado e pendências. Preserve dados de motoristas e clientes; mudanças que notifiquem pessoas exigem solicitação correspondente.

Não invente endpoints, campos, resultados ou permissões. Use o módulo da plataforma própria responsável pela entidade; não proponha substituição por plataforma externa. A regra de negócio e a autorização devem ser aplicadas no servidor.

## Verificação de leitura

Verifique a presença de ferramenta TMS de leitura; se não existir, relate a dependência sem simular dados.

Conecte-se apenas ao MCP central autenticado da Ávila Ops. Descubra as ferramentas reais e suas entradas antes de utilizá-las. Não invente nomes, endpoints, resultados nem permissões. A presença de ferramentas de outros módulos no servidor compartilhado não autoriza seu uso fora do escopo de Ávila TMS. Se a integração específica não estiver pronta, explique a dependência e limite-se a orientar ou analisar dados fornecidos. Nunca peça tokens no chat ou registre segredos em documentos. Confirme previamente alterações destrutivas, publicações, envios e ações com custos.
