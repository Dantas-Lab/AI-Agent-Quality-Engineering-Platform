# BUG-001 — Incorrect Document Retrieval

## Severity

High

## Component

RAG Retrieval Pipeline

## Description

The RAG pipeline may fail to retrieve the expected knowledge-base document for a user question.

## Steps to Reproduce

1. Start the application.
2. Submit a registration-related question.
3. Inspect the retrieved documents.
4. Verify whether `cadastro.md` is present.

## Expected Result

The expected document is included in the retrieved context.

## Actual Result

An unrelated document may be retrieved instead of the expected document.

## Root Cause

Semantic retrieval behavior may rank unrelated documents above the expected source.

## Investigation Method

- Pytest regression test.
- Structured application logs.
- Correlation ID.
- Loki queries.
- Grafana dashboard.

## Regression Prevention

An automated regression test validates that the expected source remains present in retrieval results.