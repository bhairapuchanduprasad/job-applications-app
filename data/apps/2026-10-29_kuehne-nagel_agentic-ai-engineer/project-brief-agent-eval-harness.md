# Project brief: Agent Eval Harness, Kuehne+Nagel variant (mocked shipment-booking API, guardrails, fallback, human-in-the-loop)

Repo slug: `agent-eval-harness` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md). Created for Kuehne+Nagel Agentic AI Engineer (2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
Tool-calling LangGraph agent that handles sea-freight booking requests against a mocked shipment/TMS REST API (quote, book, track, amend) plus a mocked ERP endpoint (customer account, credit limit, invoice). K+N additions: guardrail layer (input injection filter, Pydantic schema validation of every tool payload), fallback to a deterministic rules path when validation fails, human approval node for bookings above a threshold, and an eval harness that benchmarks accuracy, p95 latency and cost per request on a golden set.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "guardrails, validation layers, fallback logic, and human-in-the-loop" | guardrail layer, schema validation, rules fallback, approval node |
| "integrate ... TMS, ERP ... APIs, databases, and event-driven platforms" | mocked TMS API + Postgres + event queue (Redis stream) for booking events |
| "monitoring, logging, and explainability" | OpenTelemetry traces → Arize Phoenix, decision log per step |
| "accuracy, reliability, latency, and operational cost through benchmarking" | golden set, N-run pass rates, p95 latency, cost per run in CI |

## Tech stack
Python, LangGraph, LiteLLM, FastAPI (mock API), Pydantic, Postgres, Redis streams, OpenTelemetry + Arize Phoenix, pytest, GitHub Actions, Docker Compose.

## Milestones
1. Mock API + agent with tools (4 h) 2. Guardrails, fallback, approval node (3 h) 3. Golden set + benchmark report in CI (4 h) 4. Tracing + README (2 h).

## CV bullet it must live up to
- Tool-calling LangGraph agent for sea-freight booking requests over mocked TMS/ERP APIs, with guardrails, a validation layer for every tool call, fallback to a rules path and human approval above a threshold; a golden-set harness in CI benchmarks accuracy, latency and cost per request, traced with OpenTelemetry.
