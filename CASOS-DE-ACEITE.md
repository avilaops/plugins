# Casos de aceite

Uma entrada por pacote do acervo. Estes são cenários para execução controlada no host, não resultados já obtidos. Status inicial de todos: `NAO_EXECUTADO`. A validação estrutural do acervo não executa estes prompts nem avalia respostas do modelo.

Após executar, registre data, host, identidade/escopo autorizado, entrada, evidência da saída e resultado (`APROVADO`, `REPROVADO` ou `BLOQUEADO`). Não grave dados sensíveis ou credenciais na evidência.

## 1. agent-plugin-eval

- Nome funcional: avaliar-plugins.
- Entrada de exemplo: “Avalie este pacote local sem executá-lo e cite os arquivos que justificam cada achado.”
- Resultado esperado: Relatório com critérios de avaliação, pontuação, achados e caminhos dos arquivos que sustentam cada achado.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 2. agent-ready-cloudflare

- Nome funcional: auditar-prontidao-agentes.
- Entrada de exemplo: “Analise a prontidão deste site de teste para agentes, sem modificar infraestrutura.”
- Resultado esperado: Inventário de descoberta para agentes, evidências de robots/sitemap/formatos disponíveis e prioridades de correção; sem mudanças na infraestrutura.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 3. apple-avila

- Nome funcional: avila-apple.
- Entrada de exemplo: “Revise esta especificação iOS e liste os requisitos ausentes, sem criar releases.”
- Resultado esperado: Lista de requisitos presentes e ausentes da especificação iOS, separando arquitetura, acessibilidade, autenticação e distribuição; sem criação de release.
- Dependência: Host, skills carregadas e insumos de teste.
- Status: `NAO_EXECUTADO`.

## 4. astro-sites-manager

- Nome funcional: gerenciar-sites-astro.
- Entrada de exemplo: “Revise este projeto Astro e proponha um plano de manutenção sem alterar arquivos.”
- Resultado esperado: Plano de manutenção com estrutura Astro identificada nos arquivos, dependências verificadas, tarefas e formas de validação; sem editar arquivos.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 5. auth-md

- Nome funcional: autenticacao-agentes-auth-md.
- Entrada de exemplo: “Revise este exemplo de auth.md e aponte campos ausentes sem testar credenciais.”
- Resultado esperado: Lista de campos válidos, ausentes ou inconsistentes do auth.md fornecido e justificativas; sem uso de credenciais.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 6. automador-puro

- Nome funcional: automatizar-operacoes.
- Entrada de exemplo: “Desenhe uma automação da plataforma própria com os contratos fornecidos, sem executá-la.”
- Resultado esperado: Desenho de gatilhos, etapas, entradas, saídas, retries e idempotência baseado nos contratos próprios fornecidos; sem executar automações.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 7. avila-cms

- Nome funcional: avila-cms.
- Entrada de exemplo: “Verifique as ferramentas de avila-cms disponíveis e apresente o que é possível consultar sem alterar dados.”
- Resultado esperado: Lista das ferramentas CMS realmente disponíveis, operações de leitura possíveis e limites de escopo; indisponibilidade informada se a conexão falhar.
- Dependência: Host, MCP central autenticado e ferramentas específicas autorizadas.
- Status: `NAO_EXECUTADO`.

## 8. avila-crm

- Nome funcional: avila-crm.
- Entrada de exemplo: “Verifique as ferramentas de avila-crm disponíveis e apresente o que é possível consultar sem alterar dados.”
- Resultado esperado: Lista das ferramentas CRM realmente disponíveis e limites de acesso; se não houver adaptador, registrar bloqueio sem inventar clientes ou atividades.
- Dependência: Host, MCP central autenticado e ferramentas específicas autorizadas.
- Status: `NAO_EXECUTADO`.

## 9. avila-design

- Nome funcional: avila-design.
- Entrada de exemplo: “Revise este layout fornecido e liste problemas de hierarquia e acessibilidade.”
- Resultado esperado: Revisão do layout com evidências de hierarquia, contraste, legibilidade e navegação, acompanhada de ajustes priorizados.
- Dependência: Host, skills carregadas e insumos de teste.
- Status: `NAO_EXECUTADO`.

## 10. avila-lojas

- Nome funcional: avila-lojas.
- Entrada de exemplo: “Verifique as ferramentas de avila-lojas disponíveis e apresente o que é possível consultar sem alterar dados.”
- Resultado esperado: Lista das ferramentas de Lojas realmente disponíveis e seus escopos de consulta, sem alterar produtos, pedidos ou estoque.
- Dependência: Host, MCP central autenticado e ferramentas específicas autorizadas.
- Status: `NAO_EXECUTADO`.

## 11. avila-mail

- Nome funcional: avila-mail.
- Entrada de exemplo: “Verifique as ferramentas de avila-mail disponíveis e apresente o que é possível consultar sem alterar dados.”
- Resultado esperado: Lista das ferramentas Mail realmente disponíveis; conexão ausente ou não confirmada deve aparecer como bloqueio, sem enviar mensagens.
- Dependência: Host, MCP central autenticado e ferramentas específicas autorizadas.
- Status: `NAO_EXECUTADO`.

## 12. avila-notas

- Nome funcional: avila-notas.
- Entrada de exemplo: “Verifique as ferramentas de avila-notas disponíveis e apresente o que é possível consultar sem alterar dados.”
- Resultado esperado: Lista das ferramentas de Notas realmente disponíveis e limites para consultar documentos e coleções, sem editar ou compartilhar conteúdo.
- Dependência: Host, MCP central autenticado e ferramentas específicas autorizadas.
- Status: `NAO_EXECUTADO`.

## 13. avila-ops-skills

- Nome funcional: avila-engenharia-operacoes.
- Entrada de exemplo: “Analise este repositório de teste e proponha verificações sem modificar ou implantar.”
- Resultado esperado: Diagnóstico do repositório de teste com arquivos de evidência e plano de verificações de engenharia; sem alterações ou deploy.
- Dependência: Host, skills carregadas e insumos de teste.
- Status: `NAO_EXECUTADO`.

## 14. avila-tms

- Nome funcional: avila-tms.
- Entrada de exemplo: “Verifique as ferramentas de avila-tms disponíveis e apresente o que é possível consultar sem alterar dados.”
- Resultado esperado: Lista das ferramentas TMS realmente disponíveis; ausência de adaptador deve aparecer como bloqueio, sem inventar cargas ou entregas.
- Dependência: Host, MCP central autenticado e ferramentas específicas autorizadas.
- Status: `NAO_EXECUTADO`.

## 15. catalogue

- Nome funcional: catalogar-documentacao.
- Entrada de exemplo: “Catalogue estes três documentos fornecidos com origem e assuntos.”
- Resultado esperado: Catálogo dos três documentos com título, origem, assuntos e referências rastreáveis; informações ausentes explicitadas.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 16. coder-puro

- Nome funcional: desenvolver-software.
- Entrada de exemplo: “Revise este pequeno trecho de código e descreva a correção e sua verificação.”
- Resultado esperado: Problema identificado no trecho fornecido, proposta de correção e caso de verificação que discrimine o comportamento anterior do corrigido.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 17. coolify-operator

- Nome funcional: operar-infraestrutura-coolify.
- Entrada de exemplo: “Liste as ferramentas de consulta Coolify disponíveis sem reiniciar ou implantar serviços.”
- Resultado esperado: Inventário das ferramentas Coolify de consulta disponíveis e limites de acesso; sem reinícios, gravações ou deploy.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 18. dev-6ad0a0086b188191928c20e0cf70d6fe

- Nome funcional: app-conectado-6ad0a008.
- Entrada de exemplo: “Identifique o app referenciado e suas capacidades declaradas sem executar ações.”
- Resultado esperado: Identidade e capacidades do app obtidas do host; se não forem identificáveis, registrar a limitação e interromper ações.
- Dependência: Host e identificação/autorização do app referenciado.
- Status: `NAO_EXECUTADO`.

## 19. explica

- Nome funcional: explicar-documentacao.
- Entrada de exemplo: “Explique este documento técnico fornecido em português e indique as lacunas.”
- Resultado esperado: Explicação em português dos conceitos e relações do documento fornecido, com lacunas e termos sem definição explícitos.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 20. human-ai

- Nome funcional: editar-textos-ingles.
- Entrada de exemplo: “Revise este parágrafo em inglês preservando significado e voz.”
- Resultado esperado: Parágrafo revisado em inglês, preservando fatos, significado e voz do original, sem acrescentar afirmações.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 21. integrador-de-apis

- Nome funcional: integrar-apis.
- Entrada de exemplo: “Revise este contrato de API fornecido e liste riscos de autenticação e idempotência.”
- Resultado esperado: Achados no contrato fornecido sobre autenticação, erros, idempotência e webhooks, com referência a campos ou operações.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 22. lojas-clientes

- Nome funcional: avila-lojas-clientes.
- Entrada de exemplo: “Consulte somente a loja autorizada e apresente os campos de catálogo ausentes, sem salvar.”
- Resultado esperado: Relatório de campos ausentes do catálogo da loja autorizada, com escopo identificado e nenhuma gravação; falha de autorização tratada como bloqueio.
- Dependência: Host, MCP central autenticado e ferramentas específicas autorizadas.
- Status: `NAO_EXECUTADO`.

## 23. monitor-brave

- Nome funcional: diagnosticar-monitor-brave.
- Entrada de exemplo: “Analise estes logs fornecidos da extensão e liste hipóteses com evidências.”
- Resultado esperado: Hipóteses de falha vinculadas a trechos dos logs fornecidos, distinção entre evidência e hipótese e próximos passos de diagnóstico.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 24. motion-ad

- Nome funcional: produzir-anuncios-video.
- Entrada de exemplo: “Revise este briefing de anúncio e liste os insumos necessários antes de renderizar.”
- Resultado esperado: Lista de insumos faltantes do briefing, como duração, formato, conteúdo e materiais, com plano de produção antes de renderizar.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 25. n8n-avilaops

- Nome funcional: avila-n8n.
- Entrada de exemplo: “Mostre os workflows disponíveis no meu n8n, sem executá-los.”
- Resultado esperado: Lista de workflows acessíveis pela conexão autorizada, com identificadores quando retornados; nenhum workflow executado.
- Dependência: Host e autorização do MCP n8n.
- Status: `NAO_EXECUTADO`.

## 26. pier-cloud

- Nome funcional: integrar-pier-cloud.
- Entrada de exemplo: “Revise a documentação fornecida da API Lighthouse e liste os dados necessários para uma consulta.”
- Resultado esperado: Lista dos parâmetros, permissões e dados exigidos para a consulta Lighthouse com base na documentação fornecida, sem inventar contrato.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 27. sincronizador-puro

- Nome funcional: sincronizar-dados.
- Entrada de exemplo: “Planeje a sincronização entre estes contratos da plataforma própria, sem consultar produção.”
- Resultado esperado: Plano com fonte de verdade, chave de correspondência, cursor incremental, idempotência, conflitos e reconciliação baseado nos contratos fornecidos.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 28. slop-eval

- Nome funcional: auditar-design-generico.
- Entrada de exemplo: “Avalie este layout fornecido com evidências e pontuação por critério.”
- Resultado esperado: Pontuação por critério visual acompanhada de evidências observáveis do layout e correções priorizadas.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 29. startup-idea

- Nome funcional: validar-ideias-negocio.
- Entrada de exemplo: “Avalie esta ideia fornecida e separe fatos, hipóteses e perguntas de validação.”
- Resultado esperado: Avaliação separando fatos fornecidos, hipóteses de mercado e perguntas/testes de validação, sem apresentar hipótese como evidência.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 30. substack-expert

- Nome funcional: gerenciar-newsletter-substack.
- Entrada de exemplo: “Revise este rascunho de newsletter sem publicar ou enviar mensagens.”
- Resultado esperado: Revisão editorial do rascunho com ajustes de clareza, estrutura e chamada para ação, sem publicar nem enviar.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 31. ultimate-design-system-master

- Nome funcional: criar-design-systems.
- Entrada de exemplo: “Audite estes componentes fornecidos e proponha tokens sem alterar arquivos.”
- Resultado esperado: Auditoria dos componentes fornecidos, inconsistências observadas e proposta de tokens e estados, sem editar arquivos.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

## 32. vigia-de-integracoes

- Nome funcional: monitorar-integracoes.
- Entrada de exemplo: “Analise estes logs fornecidos e proponha um diagnóstico sem reiniciar serviços.”
- Resultado esperado: Diagnóstico dos logs com evidências, impacto e próximos passos de consulta ou recuperação; sem reiniciar serviços.
- Dependência: Host com a skill carregada e insumos de teste fornecidos.
- Status: `NAO_EXECUTADO`.

