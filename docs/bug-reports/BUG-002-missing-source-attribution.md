# BUG-002 — Missing Source Attribution

## Severity

High

## Component

RAG Response Pipeline

## Description

Retrieved documents may be returned without valid source metadata.

## Steps to Reproduce

1. Submit a question to the RAG pipeline.
2. Inspect the retrieved documents.
3. Validate the source metadata.

## Expected Result

Every retrieved document contains valid source attribution.

## Actual Result

A retrieved document may contain missing or empty source metadata.

## Root Cause

Source metadata validation was not enforced by regression testing.

## Investigation Method

- Pytest regression test.
- Structured logs.
- Loki.
- Grafana.

## Regression Prevention

An automated regression test validates source metadata for every retrieved document.