# AI Agent Quality Engineering Platform

A Quality Engineering platform designed to test, evaluate, monitor, and analyze a Retrieval-Augmented Generation (RAG) AI assistant.

The project demonstrates how traditional Software Quality Engineering practices can be extended to AI-based systems through automated testing, deterministic AI evaluation, retrieval validation, security testing, observability, regression prevention, and CI/CD quality gates.

---

## Project Overview

The application simulates a Citizen Services AI Assistant that answers questions using information retrieved from a controlled knowledge base.

The main objective is not only to build an AI application, but to demonstrate how to engineer and validate its quality.

The platform covers:

- RAG pipeline validation
- deterministic AI evaluation
- Golden Dataset testing
- retrieval quality validation
- source attribution testing
- AI security testing
- failure classification
- quality scorecards
- release criteria
- unit testing
- API testing
- E2E testing
- regression testing
- structured logging
- observability
- CI/CD quality gates

---

## System Architecture

The application follows a modular architecture:

```text
User
  |
  v
Web Interface
  |
  v
FastAPI
  |
  v
RAG Pipeline
  |
  +-------------------+
  |                   |
  v                   v
Retriever          Prompt Builder
  |
  v
ChromaDB
  |
  v
Knowledge Base
  |
  v
LLM Provider
  |
  +-------------------+
  |                   |
  v                   v
Fake LLM           Real LLM
                        |
                        v
                    OpenAI API
```

The LLM layer uses a common provider interface, allowing the application to switch between deterministic fake responses for testing and a real LLM integration.

---

## Quality Engineering Architecture

```text
                         AI Application
                               |
                               v
                     Automated Test Strategy
                               |
        +----------------------+----------------------+
        |                      |                      |
        v                      v                      v
   Traditional QA         AI Quality             Observability
        |                      |                      |
        v                      v                      v
   Unit Tests          Golden Dataset         Structured Logs
   API Tests           RAG Evaluation         Correlation IDs
   E2E Tests           Security Tests         Loki
   Regression          Scorecards             Grafana
        |                      |
        +-----------+----------+
                    |
                    v
              CI/CD Pipeline
                    |
                    v
               Quality Gate
```

---

## Technology Stack

### Application

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite

### AI and RAG

- OpenAI API
- ChromaDB
- custom RAG pipeline
- Prompt Builder
- LLM Provider abstraction
- Golden Dataset
- deterministic AI evaluators

### Testing

- Pytest
- Pytest markers
- Pytest parametrization
- unittest.mock
- FastAPI TestClient
- Postman
- Playwright
- Page Object Model

### Code Quality

- Ruff
- Mypy
- Pre-commit

### Observability

- Structlog
- structured JSON logging
- Correlation IDs
- Promtail
- Loki
- Grafana

### CI/CD

- Git
- GitHub
- GitHub Actions
- automated quality checks
- automated test execution
- Quality Gate

---

# Application Architecture

## FastAPI

FastAPI provides the application and API layer.

The API handles:

- request validation
- chat requests
- health checks
- integration with the RAG pipeline

Pydantic models validate incoming API payloads.

---

## RAG Pipeline

The Retrieval-Augmented Generation pipeline coordinates:

1. receiving the user question;
2. retrieving relevant documents;
3. building the prompt;
4. sending the prompt to the LLM;
5. returning the generated answer;
6. providing source attribution.

The pipeline separates retrieval, prompt construction, and generation responsibilities.

---

## Knowledge Base

The application uses a controlled knowledge base containing documents related to citizen services.

The documents are ingested into the vector database before retrieval execution.

This controlled environment enables predictable evaluation and regression testing.

---

## ChromaDB

ChromaDB provides vector storage and semantic document retrieval.

The retriever queries the vector database and returns the documents considered most relevant to the user question.

Retrieval behavior is validated independently from generation behavior.

---

## Prompt Builder

The Prompt Builder combines:

- the user question;
- retrieved context;
- assistant instructions.

Separating prompt construction from the RAG pipeline improves modularity and testability.

---

## LLM Provider Abstraction

The project defines a common contract for LLM implementations.

```text
LLMProvider
     |
     +----------------+
     |                |
     v                v
 FakeLLM           RealLLM
                      |
                      v
                  OpenAI API
```

This architecture reduces coupling between the RAG pipeline and specific model implementations.

---

## FakeLLM

FakeLLM provides deterministic responses for automated testing.

Benefits include:

- no API costs;
- predictable responses;
- fast execution;
- deterministic test behavior.

---

## RealLLM

RealLLM integrates the application with the OpenAI API.

Real model execution is separated from the primary automated testing strategy to control cost and avoid unnecessary non-determinism.

---

# Testing Strategy

The project combines traditional Software Quality Engineering with AI-specific evaluation techniques.

```text
Testing Strategy
       |
       +--------------------+
       |                    |
       v                    v
Traditional Testing     AI Quality Testing
       |                    |
       v                    v
Unit Tests              Golden Dataset
API Tests               RAG Evaluation
E2E Tests               Security Testing
Regression Tests        Quality Scorecards
       |                    |
       +----------+---------+
                  |
                  v
              CI/CD
                  |
                  v
             Quality Gate
```

---

## Unit Testing

Unit tests validate isolated components including:

- FakeLLM behavior;
- prompt construction;
- RAG pipeline orchestration;
- deterministic evaluators;
- retrieval evaluators;
- conversation analysis;
- failure classification;
- quality score calculation;
- quality thresholds;
- release criteria;
- report generation.

Mocks isolate dependencies when appropriate.

---

## API Testing

FastAPI endpoints are validated through automated API tests.

The suite covers:

- successful requests;
- response structure;
- schema validation;
- missing fields;
- empty messages;
- incorrect data types;
- invalid payloads;
- health checks.

Postman can also be used for manual API exploration and validation.

---

## RAG Testing

The RAG testing strategy validates retrieval separately from generation.

The suite covers:

- expected document retrieval;
- retrieval hits;
- expected sources;
- missing sources;
- source attribution;
- regression of retrieval behavior.

Separating retrieval validation from response validation improves failure isolation and root cause analysis.

---

# AI Quality Evaluation Framework

The project implements a lightweight custom AI evaluation framework.

The objective is to provide:

- deterministic execution;
- transparent evaluation logic;
- reproducible results;
- cost control;
- CI/CD compatibility.

The evaluation framework validates:

- required content;
- forbidden content;
- empty responses;
- expected sources;
- retrieval success.

This approach avoids requiring external evaluation platforms for the primary automated quality pipeline.

---

## Evaluation Models

Evaluation results are represented using structured models.

Each metric contains:

- metric name;
- score;
- pass/fail status;
- failure reason.

Individual metric results are aggregated into evaluation results for each test case.

---

## Deterministic Evaluators

The framework contains deterministic evaluators for AI behavior.

### Required Terms

Validates that expected information appears in the response.

### Forbidden Terms

Validates that prohibited information does not appear in the response.

### Empty Response

Validates that the assistant produced a response.

### Expected Sources

Validates whether required knowledge-base sources were retrieved.

### Retrieval Hit

Validates whether at least one expected document was retrieved.

---

# Golden Dataset

The Golden Dataset contains predefined evaluation cases describing expected AI behavior.

Each case can define:

- unique case ID;
- input question;
- expected sources;
- mandatory content;
- forbidden content.

Example conceptual structure:

```json
{
  "id": "GD-001",
  "question": "Example question",
  "expected_sources": [
    "document.md"
  ],
  "must_include": [
    "required information"
  ],
  "must_not_include": [
    "forbidden information"
  ]
}
```

The Golden Dataset Runner loads these cases and evaluates responses against their expected behavior.

Golden Datasets provide stable expectations for regression detection and systematic AI quality analysis.

---

# Conversation Analysis

Evaluation results can be aggregated into conversation-level quality analysis.

The analyzer calculates:

- total evaluated cases;
- passed cases;
- failed cases;
- pass rate;
- average metric score.

This converts individual evaluation results into measurable quality indicators.

---

# Failure Classification

Failed evaluations are mapped to structured failure categories.

Examples include:

- hallucination;
- missing information;
- incorrect retrieval;
- incorrect source attribution;
- unclassified failures.

The failure taxonomy supports:

- quality analysis;
- failure frequency analysis;
- root cause investigation;
- regression prioritization.

---

# Quality Scorecard

The project implements a weighted Quality Scorecard.

Quality dimensions include:

- correctness;
- faithfulness;
- relevance;
- completeness;
- safety;
- source attribution;
- latency.

Weighted metrics are used to calculate an overall quality score.

This demonstrates how abstract AI quality requirements can be converted into measurable engineering criteria.

---

# Release Criteria

The project defines explicit release criteria.

Examples include:

- minimum overall quality score;
- maximum hallucination rate;
- maximum critical failures;
- minimum regression pass rate;
- minimum safety score.

These criteria provide the foundation for automated release decisions.

---

# AI Security Testing

The project includes an adversarial security dataset.

Security scenarios include:

- prompt injection;
- role manipulation;
- requests for personal information;
- out-of-scope questions.

Security responses are evaluated using deterministic acceptance criteria.

The objective is not to provide a complete AI red-team platform, but to demonstrate how security requirements can be represented as repeatable automated tests.

---

# Regression Testing

Regression tests protect critical RAG behaviors.

Examples include:

- expected knowledge-base document retrieval;
- source attribution validation.

Documented bug investigations demonstrate the complete quality lifecycle:

```text
Failure
   |
   v
Detection
   |
   v
Investigation
   |
   v
Structured Logs
   |
   v
Root Cause Analysis
   |
   v
Correction
   |
   v
Regression Test
```

Regression testing protects the system against recurrence of previously identified failures.

---

# Bug Investigation

The project includes documented bug investigation reports.

The reports contain:

- severity;
- affected component;
- problem description;
- reproduction steps;
- expected result;
- actual result;
- root cause;
- investigation method;
- regression prevention.

Investigation can use:

- Pytest;
- structured application logs;
- Correlation IDs;
- Loki;
- Grafana.

---

# E2E Testing

Playwright validates the application through the browser.

The critical E2E flow validates that a user can:

1. open the application;
2. submit a question;
3. receive an assistant response;
4. receive source attribution.

---

## Page Object Model

The E2E architecture uses the Page Object Model.

```text
E2E Test
    |
    v
ChatPage
    |
    +--> Locators
    |
    +--> Page Actions
    |
    +--> UI Interaction
```

Page Object Model separates:

- page locators;
- user actions;
- test assertions.

This improves test readability and maintainability.

---

# Observability

The application implements structured JSON logging.

Observable events include:

- chat request received;
- retrieval completed;
- response generated.

Example:

```json
{
  "correlation_id": "request-id",
  "session_id": "web-session",
  "event": "chat_request_received",
  "level": "info",
  "timestamp": "timestamp"
}
```

---

## Correlation IDs

Each request receives a Correlation ID.

This allows events related to the same request to be traced across the application execution flow.

```text
Request
   |
   v
Correlation ID
   |
   +--> Request Received
   |
   +--> Retrieval Completed
   |
   +--> Response Generated
```

---

## Loki, Promtail, and Grafana

The observability stack uses:

- Promtail for log collection;
- Loki for log aggregation;
- Grafana for exploration and visualization.

This enables centralized analysis of structured application logs.

---

# CI/CD Pipeline

GitHub Actions automatically executes the project's quality strategy.

The pipeline contains four primary jobs.

```text
                  Push / Pull Request
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
    Code Quality    Automated Tests   Playwright E2E
          |               |               |
          v               v               v
        Ruff          Unit Tests        Chromium
      Formatting      API Tests      Application Start
        Mypy        Security Tests       E2E Tests
                    KB Ingestion
                   Regression Tests
          |               |               |
          +---------------+---------------+
                          |
                          v
                     Quality Gate
```

---

## Code Quality Job

The Code Quality job executes:

- Ruff linting;
- Ruff formatting validation;
- Mypy static type checking.

---

## Automated Tests Job

The Automated Tests job executes:

- unit tests;
- API tests;
- security tests;
- knowledge-base ingestion;
- regression tests.

Knowledge-base ingestion is performed in CI because GitHub Actions environments start without the local vector database.

---

## Playwright E2E Job

The E2E job:

1. installs Chromium;
2. starts the FastAPI application;
3. executes Playwright tests.

---

## Quality Gate

The final Quality Gate job depends on all required pipeline jobs.

```text
Code Quality --------+
                     |
Automated Tests -----+----> Quality Gate
                     |
Playwright E2E ------+
```

The Quality Gate only succeeds when all required quality checks pass.

---

# Running the Project

## Clone the Repository

```bash
git clone <repository-url>
cd AI-Agent-Quality-Engineering-Platform
```

## Create the Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file based on `.env.example`.

Never commit real API keys.

## Ingest the Knowledge Base

```bash
python -m scripts.knowledge_base.ingest_documents
```

## Start the Application

```bash
uvicorn app.main:app --reload
```

---

# Running Tests

## Complete Test Suite

```bash
pytest
```

## Unit Tests

```bash
pytest -m unit
```

## API Tests

```bash
pytest -m api
```

## Security Tests

```bash
pytest -m security
```

## Regression Tests

```bash
pytest -m regression
```

## E2E Tests

```bash
pytest -m e2e --browser chromium
```

## E2E Tests with Visible Browser

```bash
pytest -m e2e --browser chromium --headed
```

## Code Quality

```bash
pre-commit run --all-files
```

## Static Type Checking

```bash
mypy app quality tests
```

---

# Project Structure

```text
.
├── .github/
│   └── workflows/
│
├── app/
│   ├── api/
│   ├── database/
│   ├── llm/
│   ├── observability/
│   └── rag/
│
├── datasets/
│   ├── golden/
│   └── security/
│
├── docs/
│   ├── architecture/
│   ├── bug-reports/
│   ├── interview/
│   └── screenshots/
│
├── quality/
│   ├── analyzers/
│   ├── evaluators/
│   ├── release_gate/
│   ├── scorecards/
│   ├── security/
│   └── taxonomy/
│
├── scripts/
│
├── tests/
│   ├── api/
│   ├── e2e/
│   ├── regression/
│   ├── security/
│   └── unit/
│
├── .pre-commit-config.yaml
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Key Engineering Decisions

## Why use deterministic AI evaluation?

AI-based evaluations can introduce cost, latency, and non-deterministic results.

The project prioritizes deterministic evaluation for continuous integration while keeping the architecture extensible for future semantic evaluation and LLM-as-a-Judge integration.

---

## Why use FakeLLM and RealLLM?

The LLM Provider abstraction allows deterministic testing without API costs while preserving integration with a real LLM.

This provides:

- lower testing costs;
- faster execution;
- predictable test behavior;
- reduced coupling.

---

## Why test retrieval separately from generation?

A RAG system can fail even when the generated response appears plausible.

Potential failure points include:

- incorrect retrieval;
- missing documents;
- incorrect context;
- generation errors;
- hallucination;
- incorrect source attribution.

Separating retrieval validation from generation validation improves failure isolation and root cause analysis.

---

## Why use a Golden Dataset?

Golden Datasets provide stable expectations for AI behavior.

They support:

- regression detection;
- repeatable evaluation;
- quality comparison;
- systematic analysis.

---

## Why integrate observability with testing?

AI failures may involve multiple components.

Correlation IDs and structured logs make it possible to trace requests through retrieval and response generation during failure investigation.

---

## Why use a Quality Gate?

The Quality Gate converts the project's quality strategy into an automated release decision.

Code changes are only accepted by the pipeline when required quality checks succeed.

---

# Project Results

The final project demonstrates the integration of:

- Software Quality Engineering;
- AI Quality Engineering;
- Retrieval-Augmented Generation;
- automated testing;
- deterministic AI evaluation;
- Golden Dataset validation;
- security testing;
- regression prevention;
- failure classification;
- Quality Scorecards;
- release criteria;
- structured observability;
- E2E automation;
- CI/CD Quality Gates.

The result is not only an AI assistant, but a platform designed to systematically validate and monitor AI system quality.

---

# Future Improvements

Potential future improvements include:

- LLM-as-a-Judge evaluation;
- semantic similarity metrics;
- expanded Golden Dataset;
- advanced RAG evaluation;
- quality trend analysis;
- consolidated Docker deployment;
- cloud deployment;
- performance and load testing;
- expanded AI red-team testing;
- automated scorecard integration with the CI/CD Quality Gate.

---

# Author

**Gabriel Dantas Santana**

Quality Engineering | Software Testing | Systems Engineering | AI Quality