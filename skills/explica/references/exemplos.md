# Exemplos de explicação

## SCIM e grupos Cloudflare

Explicar SCIM como protocolo para provisionar e atualizar usuários e grupos entre um provedor de identidade (IdP) e um serviço. Distinguir provisionamento de login: SCIM gerencia contas e grupos; SSO autentica o acesso.

Usar o guia enviado como exemplo de migração específica da Cloudflare: os Virtual Groups antigos mapeavam usuários a permissões; os User Groups permitem vincular políticas ao grupo. Mostrar um exemplo hipotético de grupo Financeiro no IdP sincronizado à Cloudflare com uma política apropriada. Não inventar o nome de uma função real ou afirmar que membros terão todas as permissões corretas sem verificar as políticas.

Explicar a sequência: nova integração com token pertencente à conta, sincronização de grupos, associação de políticas, testes graduais e limpeza do legado. Ressaltar a condição descrita no texto: quem nunca usou grupos vinculados a Virtual Groups não precisa migrar por esse motivo. Tratar a atualização declarada 12/10/2026 como informação do material, não como verificação atual.

## SPF, DKIM e DMARC

Explicar SPF como autorização para o servidor enviar usando a identidade de envelope verificada; DKIM como assinatura de partes da mensagem verificável por chave pública; DMARC como avaliação de alinhamento do domínio do From visível com SPF ou DKIM aprovados e publicação de política/relatórios. DMARC pode passar com um desses métodos aprovado e alinhado, não exige que ambos passem.

Não dizer que todo DKIM é necessariamente TXT manual: o provedor pode orientar CNAME ou gerenciamento próprio da chave. Não dizer que autenticação elimina spam, nem que p=none manda falhas para quarentena. Explicar que reputação, conteúdo e práticas de envio também afetam a entrega. Conferir documentação oficial antes de afirmar limites e exigências atuais dos provedores citados no artigo anexado.
