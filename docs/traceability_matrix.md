# Traceability Matrix — Assistente Virtual RAG (Atendimento ao Cidadão)

Fluxo: **Requirement → Risk → Test Scenario → Automated Test**

| Requirement | Risk(s) | Test Scenario | Automated Test (ID) |
|---|---|---|---|
| REQ-001 (respostas apenas com base aprovada) | R-01 Hallucination, R-05 Wrong Document Retrieval | Perguntar algo fora da base de conhecimento e verificar que o sistema não inventa resposta | AT-RAG-001: `test_no_answer_without_grounding` |
| REQ-002 (citação de fonte) | R-01 Hallucination, R-06 Missing Source Attribution | Fazer pergunta válida e verificar presença de documento/artigo/versão citados na resposta | AT-RAG-002: `test_response_contains_source_citation` |
| REQ-003 (recusa de dados sensíveis) | R-03 Sensitive Data Disclosure | Solicitar CPF/endereço/dado de saúde de terceiro e verificar recusa | AT-SEC-001: `test_refuses_third_party_pii_request` |
| REQ-004 (escalonamento por baixa confiança) | R-01 Hallucination, R-05 Wrong Document Retrieval | Pergunta ambígua/sem contexto suficiente deve disparar escalonamento humano | AT-RAG-003: `test_escalation_on_low_confidence` |
| REQ-005 (resistência a prompt injection) | R-04 Prompt Injection | Enviar instruções maliciosas embutidas ("ignore suas regras e...") e verificar que política é mantida | AT-SEC-002: `test_prompt_injection_resilience` (suíte adversarial) |
| REQ-006 (restrição de domínio/escopo) | R-01 Hallucination | Pergunta fora do domínio de serviços públicos deve ser recusada com redirecionamento | AT-FUNC-001: `test_out_of_scope_refusal` |
| REQ-007 (logging de auditoria) | R-01, R-02, R-03 (rastreabilidade para investigação de incidentes) | Executar interação e validar registro completo do log (query, docs, resposta, versão, timestamp) | AT-LOG-001: `test_interaction_log_completeness` |
| REQ-008 (feedback do cidadão) | R-02 Incorrect Information | Submeter feedback útil/não útil e validar persistência e vínculo com a interação | AT-FUNC-002: `test_feedback_capture` |
| REQ-009 (multicanal) | R-05, R-07 (consistência entre canais) | Mesma pergunta via web, WhatsApp e app deve gerar respostas equivalentes | AT-FUNC-003: `test_cross_channel_consistency` |
| REQ-010 (sem dados procedimentais fabricados) | R-01 Hallucination, R-02 Incorrect Information | Perguntar prazo/taxa/status não confirmado e verificar ausência de invenção de dado | AT-RAG-004: `test_no_fabricated_procedural_data` |
| REQ-011 (versionamento/aprovação da base) | R-02 Incorrect Information | Verificar que apenas conteúdo com status "aprovado" é servido em produção | AT-DATA-001: `test_only_approved_kb_content_served` |
| REQ-012 (indicador de confiança) | R-01 Hallucination, R-05 Wrong Document Retrieval | Verificar exibição de disclaimer/confiança quando score de retrieval < limiar | AT-RAG-005: `test_confidence_indicator_threshold` |
| REQ-013 (latência P95 < 3s) | R-09 High Latency | Teste de carga medindo P95 sob volume nominal | AT-PERF-001: `test_latency_p95_under_load` |
| REQ-014 (uptime 99.5%) | R-07 API Failure, R-08 Database Failure | Monitoramento contínuo de disponibilidade em produção/staging | AT-MON-001: `uptime_monitor_check` (synthetic monitoring) |
| REQ-015 (degradação graciosa em falha) | R-07 API Failure, R-08 Database Failure | Simular indisponibilidade da API do LLM e do banco vetorial (chaos testing) e verificar fallback + escalonamento | AT-RES-001: `test_graceful_degradation_llm_api_down` / AT-RES-002: `test_graceful_degradation_vector_db_down` |
| REQ-016 (criptografia em trânsito/repouso) | R-03 Sensitive Data Disclosure | Verificar TLS em trânsito e criptografia em repouso dos logs | AT-SEC-003: `test_data_encryption_at_rest_and_transit` |
| REQ-017 (retenção conforme LGPD) | R-03 Sensitive Data Disclosure | Verificar expurgo automático de logs após período de retenção definido | AT-DATA-002: `test_log_retention_policy` |
| REQ-018 (escalabilidade em pico) | R-09 High Latency | Teste de carga com pico de usuários concorrentes simulados | AT-PERF-002: `test_scalability_peak_concurrency` |

---

## Cobertura por Risco (resumo)

| Risk | Requirements cobertos | Testes automatizados associados |
|---|---|---|
| R-01 Hallucination | REQ-001, REQ-002, REQ-004, REQ-006, REQ-010, REQ-012 | AT-RAG-001, AT-RAG-002, AT-RAG-003, AT-FUNC-001, AT-RAG-004, AT-RAG-005 |
| R-02 Incorrect Information | REQ-008, REQ-010, REQ-011 | AT-FUNC-002, AT-RAG-004, AT-DATA-001 |
| R-03 Sensitive Data Disclosure | REQ-003, REQ-016, REQ-017 | AT-SEC-001, AT-SEC-003, AT-DATA-002 |
| R-04 Prompt Injection | REQ-005 | AT-SEC-002 |
| R-05 Wrong Document Retrieval | REQ-001, REQ-004, REQ-009, REQ-012 | AT-RAG-001, AT-RAG-003, AT-FUNC-003, AT-RAG-005 |
| R-06 Missing Source Attribution | REQ-002 | AT-RAG-002 |
| R-07 API Failure | REQ-014, REQ-015 | AT-MON-001, AT-RES-001 |
| R-08 Database Failure | REQ-014, REQ-015 | AT-MON-001, AT-RES-002 |
| R-09 High Latency | REQ-013, REQ-018 | AT-PERF-001, AT-PERF-002 |

**Regra de gate de release:** nenhum requisito vinculado a risco de prioridade
**Crítica** (R-01, R-04) pode seguir para produção sem 100% dos testes automatizados
correspondentes em status *passed*.
