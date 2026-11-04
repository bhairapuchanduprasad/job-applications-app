# Project brief: Customer AI Pilot Kit (variant of Agent Eval Harness)

Base brief: applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md. Build that one and add the pieces below; one repo can serve both.

## Goal
Show the full technical-success loop for a fictional customer: business goal → success metrics → architecture → working agent → evaluation → handover. Proves "design technical approaches across architecture, integrations, data, security, governance, and evaluation" and "build demonstrations, prototypes".

## Scope (1–2 days)
- Fictional customer: an insurer's support team. Mock customer API (FastAPI) with policies, claims, customers (synthetic).
- Agent: Python, OpenAI API (Responses API with function calling) via LangGraph; tools: lookup_policy, claim_status, draft_reply; retrieval over 10–20 synthetic policy documents.
- `docs/architecture.md`: one page: integrations, data flow, PII handling, auth to the customer API, governance (human approval before sending replies), cost per conversation.
- `docs/success-metrics.md`: what "good" means for the customer (resolution rate on golden set, wrong-tool rate, latency, cost).
- Eval harness (from base brief): golden dataset (regression, edge, adversarial), deterministic checks first, then LLM-as-a-judge, prompt-injection tests; OpenTelemetry traces; GitHub Actions gate.
- `docs/handover.md` + a 30-minute workshop outline for the customer's team.

## Architecture
FastAPI mock API ← tools ← LangGraph agent (OpenAI API) → retrieval (pgvector or in-memory) ; eval runner (pytest) → report.md ; OTel → console/Phoenix.

## Milestones
1. Mock API + data (2h) 2. Agent + tools (3h) 3. Retrieval (2h) 4. Eval harness + CI (4h) 5. Docs: architecture, metrics, handover, workshop (2h) 6. README + 3-min demo video.

## README outline
Problem, customer goal, architecture diagram, how to run, eval results table, security/governance decisions, what I would do next with a real customer.

## CV bullet it must live up to
"Reference pilot for a customer support use case: tool-calling agent over a mocked customer API, architecture note on integrations, security and governance, and an evaluation harness (golden dataset, prompt-injection tests) gated in GitHub Actions."
