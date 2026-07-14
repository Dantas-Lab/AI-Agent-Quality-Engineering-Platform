# Interview Guide

## What problem does this project solve?

It demonstrates how to systematically validate the quality of an AI application instead of evaluating responses manually.

## Why did you build a custom evaluation framework?

I wanted deterministic, transparent, and cost-controlled evaluations that could run continuously in CI/CD.

The architecture can later be extended with semantic evaluation or LLM-as-a-Judge.

## Why is a Golden Dataset important?

It creates stable expectations for AI behavior and enables automated regression detection.

## Why test retrieval separately?

A generated answer can appear correct even when the RAG system retrieved incorrect information.

Separate validation improves root cause analysis.

## What is the difference between traditional testing and AI testing?

Traditional testing generally validates deterministic inputs and outputs.

AI systems also require quality evaluation across dimensions such as relevance, faithfulness, safety, retrieval quality, and source attribution.

## How do you avoid spending money during testing?

The project uses FakeLLM implementations and deterministic evaluators for most automated tests.

Real LLM calls are isolated from the primary CI execution.

## Why use Protocol?

The LLM provider protocol defines a common contract for different LLM implementations.

This reduces coupling between the RAG pipeline and the model implementation.

## Why use correlation IDs?

They allow all events related to one request to be traced across the execution pipeline.

## Why use regression tests for RAG?

Changes to documents, embeddings, retrieval configuration, or application logic can change retrieval behavior.

Regression tests protect critical expected behavior.

## Why use POM with Playwright?

Page Object Model separates page interaction logic from test behavior, improving maintainability and readability.

## How does the Quality Gate work?

The CI pipeline executes required quality jobs.

The final Quality Gate job only succeeds when code quality, automated tests, and E2E tests pass.

## What would you improve next?

I would expand the Golden Dataset, add controlled LLM-as-a-Judge evaluation, introduce quality trend analysis, improve performance testing, and consolidate application deployment.