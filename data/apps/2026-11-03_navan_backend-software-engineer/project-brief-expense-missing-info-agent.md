# Project brief: Expense Missing-Info Agent (Agent Eval Harness variant)
Repo slug: expense-missing-info-agent. Status: planned. For: Navan Backend Software Engineer (2026-11-03).

## Goal
A tool-calling agent that completes half-filled expenses over a mock expense API, plus the eval harness that proves it is accurate, safe and cheap.

## Why for this JD
Proves LLM agents with tool use, grounding in user history, safe partial updates, prompt-injection guardrails, PII masking, receipt extraction with provider failover, evals (accuracy, latency, cost), Java/Spring Boot API, GitHub Actions.

## Scope (1–2 days)
- Mock expense API in Java/Spring Boot (H2/Postgres): expenses, trips, users, cost centers; PATCH with field-level writes + audit log.
- Receipt extraction service (Python/FastAPI): LLM vision extraction vs OCR baseline, failover via LiteLLM; Pydantic schema (merchant, date, amount, VAT, currency).
- LangGraph agent: tools get_expense, get_user_history, get_trip, suggest_fields, patch_expense; grounding rule: every suggestion cites the source record; writes only empty fields.
- Guardrails: receipt text treated as data; prompt-injection test receipts; PII masking before model calls.
- Eval harness: 40 labelled expenses; field accuracy, wrong-write rate, p95 latency, cost per expense; GitHub Actions gate.

## Milestones
1. Spring Boot mock API. 2. Extraction service + labelled receipts. 3. Agent + tools. 4. Guardrail tests. 5. Eval in CI + README.

## Demo
CLI/Swagger: upload receipt → agent fills cost center + project with citations; injected receipt is refused.

## CV bullets it must live up to
- Tool-calling LangGraph agent that fills missing expense fields over a mock Java/Spring Boot expense API, grounding each suggestion in the user's trips and history and writing only empty fields with an audit trail; receipt extraction with LLM/OCR provider failover.
- Eval harness on labelled receipts (field accuracy, wrong-write rate, latency, cost per expense) with prompt-injection and PII-masking tests, gated in GitHub Actions.
