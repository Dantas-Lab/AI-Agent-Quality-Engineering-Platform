# AI Agent Quality Engineering Platform

A Quality Engineering platform designed to validate, test, monitor, and analyze a Retrieval-Augmented Generation (RAG) AI assistant.

The project demonstrates how traditional Software Quality Engineering practices can be extended to AI-based systems through automated testing, deterministic AI evaluation, retrieval validation, security testing, observability, regression prevention, and CI/CD quality gates.

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
- API testing
- E2E testing
- regression testing
- structured logging
- observability
- CI/CD quality gates

## Architecture

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