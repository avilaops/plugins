---
name: monitor-brave
description: Diagnosticar e manter a extensão Avila Ops Monitor do Brave, medir buffer, interrupções, carregamento da página e RAM do computador e conferir a integração n8n. Usar quando Nicolas pedir testes do monitor, DevTools do Brave, reprodução travando, liberar RAM de abas inativas ou melhorias no projeto Monitor-brave.
---

# Monitor Brave

## Acessar o ambiente correto

- Descobrir ferramentas Remote Desktop Commander e listar dispositivos. Selecionar o computador Windows `hp` pelo ID atual retornado; não presumir que o servidor Ubuntu é o computador de teste.
- Usar `D:\Projetos\Monitor-brave` como projeto e `AvilaOps_VideoMonitor_Brave` como pasta da extensão. Conferir arquivos e versão atuais antes de editar.
- Ler AGENTS.md ou documentação aplicável se houver. Preservar alterações do usuário e criar backup das mudanças relevantes.
- Usar o Brave de diagnóstico autorizado, com perfil `brave-debug-profile` e CDP local em `127.0.0.1:9222`. Preservar o Brave habitual do usuário.
- Listar abas existentes antes de abrir páginas. Não reproduzir títulos ou conteúdo privado em relatórios; apresentar apenas métricas técnicas.

## Usar as ferramentas locais

- Executar `node D:\Projetos\Monitor-brave\devtools-local.cjs list` para descobrir IDs, e `monitor ID` para observar carregamento. Executar `launch` somente se a conexão de depuração estiver indisponível.
- Usar `verify-devtools.cjs` para verificar a extensão instalada: modos `start`, `history`, `inspect`, `selection`, `sidepanel`, `exportcheck` e `reloadPage`. Ler o código antes de usar: a versão inicial tem seleção de site de teste específica; adaptar a uma aba explicitamente autorizada quando necessário.
- Executar `release` apenas quando a liberação de RAM foi autorizada: descarrega abas inativas do perfil de diagnóstico, preservando ativas, fixadas, com áudio e monitoradas. Não encerrar processos do Windows para simular limpeza de memória.
- Não reiniciar o navegador ou recarregar a página sem explicar a interrupção durante reprodução. Dentro de testes autorizados, limitar a ação ao perfil e à aba de diagnóstico.
- Tratar chamadas remotas pendentes pelo `call_id`; não repetir operações de escrita enquanto pendentes. Para processos, ler saída pelo PID quando a sessão existir.

## Interpretar os resultados

- Avaliar somente o vídeo principal, preservando seleção manual quando houver. Distinguir vídeo pausado, preview, anúncio e frame externo sem acesso.
- Medir buffer ao longo do tempo, progresso da reprodução, eventos waiting, quadros perdidos e RAM disponível. Não atribuir a causa de travamentos à RAM apenas por coincidência.
- Tratar carregamento completo como evento da página, sem prometer que vídeos, lazy loading ou conteúdo sob demanda carregaram 100%.
- Usar LCP bom até 2,5 s e CLS bom até 0,1 como limites locais. Não afirmar aprovação de Core Web Vitals de campo nem nota Lighthouse. Informar INP não medido quando aplicável.
- Tratar status HTTP zero/oculto como indisponível, e não como sucesso ou falha. Nunca coletar cookies, títulos, URLs de mídia, tokens ou cabeçalhos de autenticação para telemetria.
- No preparo de buffer, pausar somente o vídeo ativo selecionado; esperar no máximo 10 s, buscar 8 s de buffer e retomar. Se pausar não aumentar buffer, evitar repetição para o mesmo vídeo e recomendar ajuste de qualidade no player.

## Verificar n8n e produção

- Localizar o workflow `Monitor de Streaming — Brave`, ID conhecido `KKHRoCJrUqObxXwH`, e conferir a versão publicada. O endpoint de métricas é `https://n8n.avilaops.com/webhook/brave-stream-diagnostics-2026`.
- Confirmar receptor de métricas habilitado, resposta JSON válida e HTTP 200 com amostras sanitizadas. Conferir casos de buffer baixo, ausência de dados, valores nulos e falhas de transferência.
- Ler tipos de nodes e validar configurações antes de alterações. Publicar somente dentro da autorização do pedido; confirmar que rascunho e versão ativa são os esperados.
- Preservar o handler central de erros Todoist, ID conhecido `dtk7UwKorqvDIqfu`, e acesso MCP. Não provocar erro real para gerar notificação sem autorização de teste de alertas.
- Tratar `timeSavedPerExecution` como minutos inteiros no conector. Manter zero até medir uma economia defensável; não atribuir um minuto economizado a cada amostra periódica só para marcar o checklist.

## Atualizar e concluir

- Validar sintaxe e comportamento; depois verificar a versão e a função em execução no service worker. Reiniciar Brave pode preservar cache antigo da extensão.
- Preferir instalação persistente via ferramenta CDP `Extensions.loadUnpacked` a carregar a extensão apenas pelo argumento `--load-extension`.
- Antes de reinstalar, preservar storage.local/session e histórico. O helper `reinstall` tem backup e restauração; ler e conferir seus parâmetros antes de usar. Reconfigurar scripts de retomada se a reinstalação os remover.
- Verificar retomada após reload, seleção manual, RAM, descarte seletivo e logs sanitizados. Conferir gráficos e painel lateral sem capturar conteúdo privado da página.
- Fechar apenas abas temporárias de teste criadas pelo assistente. Manter o monitor da aba autorizada pronto para uso.
- Relatar funcionalidades validadas, mudanças no workflow e limitações reais. Nunca substituir validação no navegador por testes simulados sem informar isso.
