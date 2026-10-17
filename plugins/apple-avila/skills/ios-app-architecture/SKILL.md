---
name: ios-app-architecture
description: Use quando for necessário planejar, implementar ou revisar arquitetura de aplicativos iOS/iPadOS na Ávila Ops, incluindo SwiftUI, APIs e autenticação.
---
# Arquitetura de apps Apple — Ávila Ops

- Defina primeiro público, jornada, plataforma, dados, requisitos offline, login, push, permissões, monetização e distribuição.
- Priorize SwiftUI e componentes nativos; use camadas separadas de UI, domínio, dados, networking e serviços de plataforma.
- O CMS Ávila Ops é responsável por conteúdo, estrutura das telas configuráveis, temas, feature flags, permissões e versionamento. A aplicação compilada é responsável por funcionalidades nativas, segurança e contratos de API.
- Preserve regras de negócio no backend original: ERP, TMS, CRM e Lojas; não replique regras no cliente nem no CMS.
- Modele configuração de tela em JSON versionado com validação de esquema, migrações, fallback e rollback; nunca execute código arbitrário fornecido por conteúdo do CMS.
- Autenticação com OAuth/OIDC quando implementado e verificado; tokens no Keychain, sessão com expiração e políticas de reautenticação. Multi-tenant com isolamento validado no backend.
- Defina autorização server-side; TLS, minimização de dados, auditoria, consentimento e gerenciamento de segredos fora do repositório.
- Se o usuário solicitar código, proponha organização do projeto, contratos da API, testes unitários/UI, acessibilidade e estratégia de distribuição.
- Não afirme que compilou ou publicou sem execução e evidência; confirme se há acesso real a Xcode, Apple Developer, certificados e App Store Connect.
- Consulte documentação oficial Apple atual para requisitos e APIs antes de orientar mudanças sensíveis a versões.

## Entrega
Forneça desenho de módulos, contratos, decisões arquiteturais, riscos, backlog ordenado, requisitos de testes e critérios de aceite.
