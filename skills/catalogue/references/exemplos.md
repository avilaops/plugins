# Exemplos de catalogação

## Migração SCIM da Cloudflare

Fonte de exemplo: texto fornecido por Nicolas em 14/10/2026; atualização declarada 12/10/2026, sem verificação externa neste exemplo.
URL: https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/
Tipo: guia de migração de fornecedor. Tags: Cloudflare, SCIM, IdP, IAM, grupos, políticas, migração.

Resumo: o guia descreve a substituição de Virtual Groups, identificados por `CF-<accountID>-<Role Name>`, por SCIM User Groups. Os grupos antigos eram placeholders para mapear grupos do IdP a membros da conta e tinham limitações de gestão. Segundo o texto, quem nunca sincronizou grupos ligados a esses Virtual Groups não precisa agir.

Procedimento da fonte: criar uma nova integração SCIM no IdP com Account Owned Token; atribuir usuários e grupos à nova aplicação; sincronizar e verificar os User Groups no Dashboard; anexar políticas de permissão; migrar usuários gradualmente testando a sincronização; remover recursos legados e mapeamentos após validar a migração.

Aplicação possível: gestão de acesso da equipe às contas Cloudflare, se existir provisionamento SCIM legado. Não confundir esse guia de fornecedor com uma obrigação de migrar todos os protocolos SCIM de todos os sistemas. Conferir configuração real, acessos herdados e documentação oficial antes de mudar políticas.

## Artigo SPF, DKIM e DMARC em `.bear`

Extrair a ficha do Markdown dentro do textbundle. Separar protocolos, requisitos de cada provedor e exemplos de DNS. Datas e limites citados por fontes secundárias precisam de confirmação oficial antes de orientar uma configuração atual. Não copiar valores de DNS de um provedor para outro. Registrar que autenticação não garante entrega na caixa de entrada.
