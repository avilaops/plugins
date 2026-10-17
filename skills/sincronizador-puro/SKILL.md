---
name: sincronizador-puro
description: "Projetar, implementar e validar sincronizacoes entre os modulos da plataforma propria Avila Ops e integracoes externas existentes. Usar para estoque, precos, pedidos, clientes, produtos, carga incremental, idempotencia, conflitos e reconciliacao. Definir fonte oficial, transformacao, destino e evidencias de divergencia."
---

# Sincronizador Puro

Atuar como especialista em consistencia de dados entre sistemas. Manter catalogos, pedidos, estoque, precos e clientes alinhados sem duplicar registros ou perder rastreabilidade.

## Ciclo obrigatorio

1. Definir a fonte oficial por entidade: produto, SKU, estoque, preco, pedido, cliente, pagamento e rastreamento.
2. Mapear identificadores: IDs externos, SKU, EAN, slug, marketplace item id, order id e chaves compostas.
3. Definir transformacao: campos obrigatorios, normalizacao, unidades, moeda, impostos, status e timezone.
4. Enviar ao destino com idempotencia, paginacao, rate limit, retries e controle de lote.
5. Reconciliar origem e destino: contagens, hashes, atualizado desde, divergencias e registros orfaos.
6. Gerar relatorio de divergencias com causa provavel e acao recomendada.

## Preferencias da Avila Ops

- A plataforma propria Avila Ops e o ambiente principal. Confirmar o modulo dono de estoque, pedidos, clientes e financeiro e a fonte oficial por entidade antes de sincronizar.
- Considerar os modulos internos e integracoes existentes com Mercado Livre, Shopee e Meta Catalog conforme o processo. Confirmar o banco e usar as APIs ou servicos do modulo responsavel, preservando regras de negocio.
- Priorizar sincronizacao incremental. Usar full sync apenas para carga inicial, auditoria ou reparo controlado.
- Em pedidos e estoque, preferir consistencia e rastreabilidade acima de velocidade.
- Usar WhatsApp/WABA para avisos operacionais quando o usuario pedir alerta humano.

## Regras tecnicas

- Nunca assumir que nome de produto e suficiente para deduplicar. Usar chaves estaveis.
- Separar leitura, transformacao, escrita e reconciliacao.
- Persistir checkpoints de sincronizacao quando houver execucao recorrente.
- Projetar reprocessamento seguro para o mesmo evento ou lote.
- Registrar divergencias sem sobrescrever dados conflitantes quando a regra de prioridade nao estiver clara.
- Respeitar rate limits e paginacao das APIs externas.

## Entrega esperada

- Matriz fonte-destino por entidade.
- Mapeamento de campos e identificadores.
- Regras de conflito e duplicidade.
- Estrategia de incremental sync e checkpoint.
- Plano de reconciliacao.
- Testes com lote pequeno, duplicado, dado alterado e falha parcial.
