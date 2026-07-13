# Requisitos — Assistente Virtual RAG (Atendimento ao Cidadão)

Formato: `shall` statements, testáveis e rastreáveis. IDs referenciados na
Risk Matrix e na Traceability Matrix.

---

## Requisitos Funcionais

**REQ-001**
The system shall answer citizen questions using only information available in
the approved knowledge base.

**REQ-002**
The system shall provide the source documents (title, section/article, and
version/date) used to generate each answer.

**REQ-003**
The system shall refuse requests for sensitive personal information about
third parties.

**REQ-004**
The system shall detect when retrieved context is insufficient to answer
the question and shall escalate the conversation to a human agent instead
of generating a speculative answer.

**REQ-005**
The system shall reject or safely handle attempts to override its
instructions, role, or safety policies embedded in user input (prompt
injection).

**REQ-006**
The system shall restrict its responses to the defined domain of citizen
public services and shall politely decline out-of-scope requests.

**REQ-007**
The system shall log every interaction (query, retrieved documents,
generated answer, confidence score, timestamp, knowledge base version) for
audit purposes.

**REQ-008**
The system shall allow the citizen to submit feedback (helpful / not
helpful) on each answer.

**REQ-009**
The system shall support multi-channel access (web, WhatsApp, mobile app)
with consistent answer quality across channels.

**REQ-010**
The system shall never present fabricated procedural data (deadlines,
fees, protocol numbers, process status) that is not confirmed by the
knowledge base or an integrated backend system.

**REQ-011**
The system shall version and only serve knowledge base content that has
passed the approval workflow.

**REQ-012**
The system shall present a confidence indicator or disclaimer when
retrieval confidence is below the defined threshold.

---

## Requisitos Não Funcionais

**REQ-013**
The system shall respond to 95% of queries within 3 seconds (P95 latency)
under nominal load.

**REQ-014**
The system shall remain available with an uptime of at least 99.5% monthly.

**REQ-015**
The system shall degrade gracefully (fallback message + human escalation
option) upon LLM API or vector database failure.

**REQ-016**
The system shall encrypt data in transit and at rest for all logged
interactions.

**REQ-017**
The system shall retain interaction logs in compliance with applicable
data protection regulation (e.g., LGPD) retention limits.

**REQ-018**
The system shall be able to scale to handle peak concurrent sessions
defined by the business (e.g., 5,000 simultaneous users) without
violating REQ-013.
