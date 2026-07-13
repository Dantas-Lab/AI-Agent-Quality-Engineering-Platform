# Risk Matrix — Assistente Virtual RAG (Atendimento ao Cidadão)

Escala: Probabilidade (1-Baixa, 2-Média, 3-Alta) × Impacto (1-Baixo, 2-Médio, 3-Alto,
4-Crítico) → Severidade = Probabilidade × Impacto.
Prioridade: **Crítica** (≥9), **Alta** (6–8), **Média** (3–5), **Baixa** (≤2).

| ID | Risco | Descrição | Prob. | Impacto | Severidade | Prioridade | Mitigação | Requisito(s) relacionado(s) |
|---|---|---|---|---|---|---|---|---|
| R-01 | Hallucination | Sistema gera informação plausível mas não fundamentada na base de conhecimento | 3 | 4 | 12 | Crítica | Groundedness/faithfulness checks, golden dataset, prompt engineering restritivo, RAG com citação obrigatória | REQ-001, REQ-002 |
| R-02 | Incorrect Information | Resposta tecnicamente incorreta mesmo com fonte citada (erro de interpretação ou base desatualizada) | 2 | 4 | 8 | Alta | Curadoria/aprovação de conteúdo, versionamento da base, revisão periódica, testes de acurácia com especialistas de domínio | REQ-001, REQ-011 |
| R-03 | Sensitive Data Disclosure | Exposição de dados pessoais sensíveis de terceiros | 2 | 4 | 8 | Alta | Filtro de PII, regras de recusa (REQ-003), mascaramento na base, testes de segurança dedicados | REQ-003, REQ-016, REQ-017 |
| R-04 | Prompt Injection | Usuário manipula o modelo via instruções embutidas para burlar políticas | 3 | 3 | 9 | Crítica | Sanitização de input, guardrails, testes adversariais automatizados, isolamento de instruções de sistema | REQ-005 |
| R-05 | Wrong Document Retrieval | Recuperação de documentos irrelevantes ou desatualizados leva a resposta ruim | 2 | 3 | 6 | Alta | Avaliação de retrieval (precision/recall), tuning de embeddings, re-ranking, testes de regressão de retrieval | REQ-001, REQ-004 |
| R-06 | Missing Source Attribution | Resposta gerada sem citar a fonte usada | 2 | 3 | 6 | Alta | Validação estrutural de resposta (fonte obrigatória no output), testes automatizados de formato | REQ-002 |
| R-07 | API Failure | Falha na API do LLM (timeout, indisponibilidade) | 2 | 3 | 6 | Alta | Retry/circuit breaker, fallback para atendimento humano, monitoramento e alertas | REQ-015 |
| R-08 | Database Failure | Falha no banco vetorial/documental afeta retrieval | 2 | 3 | 6 | Alta | Réplicas, health checks, fallback gracioso, testes de resiliência (chaos testing) | REQ-015 |
| R-09 | High Latency | Tempo de resposta acima do aceitável degrada experiência do cidadão | 2 | 2 | 4 | Média | Testes de carga/performance, cache de embeddings, otimização de pipeline, autoscaling | REQ-013, REQ-018 |

**Observação:** riscos com prioridade Crítica/Alta (R-01, R-04, R-03, R-02, R-05, R-06,
R-07, R-08) devem ter cobertura de teste obrigatória antes de qualquer release para
produção, conforme critérios de saída definidos em `docs/test_strategy.md`.
