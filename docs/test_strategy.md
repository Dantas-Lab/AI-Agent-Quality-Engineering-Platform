# Test Strategy — Assistente Virtual RAG (Atendimento ao Cidadão)

**Documento:** docs/test_strategy.md
**Versão:** 1.0
**Referência de requisitos:** docs/requirements.md
**Referência de riscos:** docs/risk_matrix.md

---

## 1. Scope

### In Scope
- Pipeline RAG completo: retrieval (busca na base vetorial/documental) + generation
  (resposta do LLM).
- Qualidade e acurácia das respostas frente à base de conhecimento aprovada.
- Citação e rastreabilidade de fontes.
- Regras de recusa (dados sensíveis, fora de escopo, prompt injection).
- Escalonamento para atendimento humano.
- Integrações de canal (web, WhatsApp, app).
- Logging/auditoria e conformidade com retenção de dados.
- Desempenho, disponibilidade e resiliência a falhas (LLM API, banco vetorial).

### Out of Scope
- Testes de sistemas transacionais de backend não integrados diretamente
  (ex.: sistemas legados de emissão de documentos), exceto pelos contratos de API
  consumidos.
- Testes de UI visual pixel-perfect (cobertos por time de design/frontend
  separadamente).

---

## 2. Test Levels

| Nível | Foco | Responsável |
|---|---|---|
| Unit | Funções de pré-processamento, chunking, prompt templates, parsers de resposta | Dev |
| Integration | Integração retrieval ↔ vector DB ↔ LLM API ↔ backend de serviços | Dev/QA |
| System | Fluxo completo pergunta → resposta, incluindo escalonamento e logging | QA |
| Acceptance | Validação com stakeholders de negócio/compliance sobre casos reais de atendimento | QA + Negócio |
| Regression | Reexecução de suíte crítica a cada nova versão de modelo/base de conhecimento | QA (automatizado) |

---

## 3. Test Types

- **Functional testing:** validação dos REQ-001 a REQ-012 (respostas corretas,
  citação de fonte, recusa de dados sensíveis, escopo, escalonamento).
- **Non-functional testing:**
  - Performance/Load (REQ-013, REQ-018) — latência P95, throughput sob pico.
  - Reliability/Resilience (REQ-015) — chaos testing em falha de API/DB.
  - Security testing — prompt injection, jailbreak, exfiltração de dados sensíveis
    (REQ-003, REQ-005).
  - Data privacy/compliance testing — LGPD, retenção e criptografia (REQ-016, REQ-017).
- **RAG-specific quality testing:**
  - Retrieval evaluation (precision/recall dos documentos recuperados).
  - Groundedness/faithfulness (a resposta é sustentada pelos documentos recuperados?).
  - Hallucination testing (golden dataset com perguntas armadilha sem resposta na base).
  - Adversarial/red-team testing (prompt injection, manipulação de contexto).
- **Usability testing:** clareza da linguagem, tom institucional, acessibilidade.
- **Exploratory testing:** sessões manuais para descobrir falhas não cobertas por
  casos escritos, especialmente em ambiguidade de linguagem natural.

---

## 4. Automation Strategy

- **Pirâmide de automação:**
  - Base: testes unitários de componentes determinísticos (chunking, parsing,
    formatação de citação) — alta cobertura, execução em cada commit (CI).
  - Meio: testes de integração de API (retrieval, LLM, backend) via contract testing
    e mocks/stubs para reduzir custo e flakiness.
  - Topo: testes end-to-end (E2E) sobre um **golden dataset** curado de perguntas
    reais com respostas esperadas/critérios de aceitação, executados via pipeline
    de avaliação (LLM-as-judge + regras determinísticas).
- **Golden dataset / Regression suite:** conjunto versionado de pares
  (pergunta, contexto esperado, resposta esperada/critério) cobrindo casos felizes,
  casos de recusa, casos de escalonamento e casos adversariais. Executado a cada
  deploy de modelo, prompt ou atualização relevante da base de conhecimento.
- **Métricas automatizadas de qualidade RAG:** faithfulness/groundedness score,
  answer relevance, retrieval precision/recall (ex.: via frameworks tipo
  Ragas/DeepEval ou avaliação própria com LLM-as-judge + validação humana amostral).
- **Testes de segurança automatizados:** biblioteca de prompts adversariais
  (prompt injection, jailbreak) executada como suíte de regressão de segurança.
- **Testes não determinísticos:** para saídas geradas por LLM, usar critérios de
  aceitação semânticos (similaridade, presença de fonte citada, ausência de dados
  proibidos) em vez de igualdade exata de string.
- **CI/CD:** testes unitários e de integração em todo pull request; suíte de
  regressão RAG completa e testes de segurança antes de cada release para produção;
  smoke tests pós-deploy.

---

## 5. Environments

| Ambiente | Finalidade | Dados |
|---|---|---|
| Dev | Desenvolvimento e testes unitários/integração | Dados sintéticos/mascarados |
| QA/Staging | Testes de sistema, regressão, segurança, performance | Cópia da base de conhecimento aprovada + dados sintéticos |
| UAT | Validação de negócio/compliance com casos reais anonimizados | Dados anonimizados |
| Production (canário/shadow) | Monitoramento contínuo, shadow testing de novas versões de modelo antes do rollout completo | Dados reais (com governança/log) |

---

## 6. Entry Criteria

- Requisitos (docs/requirements.md) revisados e aprovados.
- Base de conhecimento de teste carregada e versionada no ambiente de QA.
- Golden dataset de regressão disponível e revisado por especialista de domínio.
- Ambiente de QA/Staging disponível e estável (health check OK).
- Casos de teste mapeados na matriz de rastreabilidade para os requisitos da release.
- Build/versão do modelo e prompts congelada para o ciclo de teste.

## 7. Exit Criteria

- 100% dos requisitos críticos (segurança, dados sensíveis, prompt injection,
  citação de fonte) com testes executados e aprovados.
- Taxa de hallucination no golden dataset abaixo do limiar aceito (ex.: <2%,
  a definir com negócio).
- Nenhum defeito crítico ou de alta severidade aberto sem mitigação/aceite formal.
- Métricas de performance (REQ-013, REQ-018) dentro do SLA em ambiente de staging.
- Testes de segurança/adversariais executados sem falha crítica não tratada.
- Sign-off de QA, Compliance/Privacidade e stakeholder de negócio.
