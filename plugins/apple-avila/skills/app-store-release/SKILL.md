---
name: app-store-release
description: Use para preparar checklist, avaliação de conformidade, TestFlight, metadados e publicação de apps Apple pela Ávila Ops.
---
# TestFlight e App Store Connect

1. Confirme titularidade da conta Apple Developer e acesso autorizado a App Store Connect, bundle ID, equipes, assinatura e certificados.
2. Verifique requisitos atuais diretamente em developer.apple.com e nas App Review Guidelines; identifique o que foi confirmado e a data de consulta.
3. Valide privacidade, coleta de dados, permissões com textos explicativos, acessibilidade, links de suporte, capturas de tela, descrição, classificação etária, login de revisão e direitos de conteúdo.
4. Proponha pipeline de CI/CD e assinatura usando ferramentas realmente disponíveis; para iOS não prometa builds locais em Windows sem serviço macOS apropriado.
5. TestFlight -> relatório de falhas -> revisão de metadados -> submissão -> monitoramento -> plano de rollback conforme capacidades da App Store.
6. Solicite aprovação explícita antes de envio, alteração de certificados ou publicação; não assuma permissão a partir de conexão existente.
7. Consulte e aplique as regras da Apple sobre templates e apps gerados por serviços de app builder, inclusive a política 4.2.6, caso aplicável. Não garanta aprovação.

Entregue checklist com status confirmado, pendente e bloqueado, provas e próximos responsáveis.
