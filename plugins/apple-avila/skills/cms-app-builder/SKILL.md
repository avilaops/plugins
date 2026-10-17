---
name: cms-app-builder
description: Use para arquitetar um construtor de aplicativos dentro do CMS Ávila Ops, definindo esquema de telas, módulos, preview, dados e fluxo de publicação.
---
# App Builder no CMS Ávila Ops

Objetivo: evoluir cms.avilaops.com para plataforma multi-tenant de criação e gestão de aplicativos, mantendo separação entre configuração remota e código nativo.

## Fluxo do produto
- Projetos: tenant, proprietário, membros, nome, bundle ID, ambientes e políticas de acesso.
- Temas: design tokens versionados, light/dark, componentes e acessibilidade.
- Telas: editor com árvore de componentes permitidos; propriedades tipadas; rotas; formulários; estados vazios; condições de visibilidade.
- Dados: conexões através de APIs autorizadas do ERP, CRM, TMS, Lojas e outros serviços; validação de esquema, autorização server-side e dados de demonstração.
- Preview: renderizador de referência do esquema e prévia no runtime real; documente divergências, e não chame mock de teste nativo.
- Entrega: versões imutáveis, diff, revisão/aprovação, compilação CI com ambiente macOS quando requerido, TestFlight/App Store, histórico e rollback de configuração.
- Observabilidade: erros de configuração, crashes, métricas não pessoais, eventos de auditoria, IDs de correlação.

## Regras de segurança
- Não permitir JavaScript remoto arbitrário nem módulos desconhecidos executados no aparelho.
- Não colocar chaves de API ou credenciais do cliente no esquema enviado para dispositivos.
- Isolamento por tenant e mínimos privilégios em todas as ações.
- Separar alterações apenas de conteúdo das mudanças que exigem nova revisão da App Store; consultar política Apple atual.

## Saída padrão
Arquitetura em camadas, modelo de dados, JSON Schema de exemplo, APIs, jornadas, backlog MVP por fase, testes e critérios objetivos de aceite.
