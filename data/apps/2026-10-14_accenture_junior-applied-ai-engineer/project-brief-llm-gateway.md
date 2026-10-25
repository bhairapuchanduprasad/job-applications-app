# Project brief: LLM Gateway

Repo slug: `llm-gateway` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the Accenture application.
Time box: 1–2 days with Claude Code.

## Goal
A small, provider-agnostic gateway that application code calls instead of calling LLM providers directly. It handles token budgets, streaming, retries and fallback between providers, and logs latency, tokens and cost for every request. A small dashboard shows the KPIs an engineering lead would ask about: cost per request, latency percentiles, and how often outputs pass an evaluation set.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "calling AI provider APIs in live code, managing token limits and latency, building initial abstraction layers" | The gateway itself: one interface over 2+ providers, token budgeting, timeouts, retries, fallback |
| "token management, latency, and cost tradeoffs" | Per-request logging of input/output tokens, latency, computed cost; budget limits per caller |
| "Define and track KPIs … present AI productivity and quality metrics" | KPI dashboard (cost/request, p50/p95 latency, eval pass rate) |
| "AI-generated tests, AI-assisted debugging, AI-accelerated code review" | Tests generated with Claude Code and reviewed by hand; note in README what you kept, fixed or rejected |
| "Own the quality of AI-generated outputs … know when it is production-ready" | Small evaluation set (10–20 prompts with expected properties) run in CI; pass rate tracked |
| TypeScript, JavaScript/HTML/CSS | Dashboard in React + TypeScript |
| CI/CD | CI runs tests + eval on every push |

## Scope (keep it small)
In:
- Python package + FastAPI service: `POST /v1/complete` (and streaming variant) with provider adapters for 2 providers (e.g. Anthropic + OpenAI, or one + a local mock provider if you lack a key).
- Config per "client app": allowed models, max tokens, monthly budget.
- Retries with backoff, timeout, fallback to the second provider on error or timeout.
- SQLite log table: timestamp, app, provider, model, tokens in/out, latency ms, cost, status, eval tag.
- `/metrics` endpoint aggregating KPIs.
- React + TypeScript dashboard reading `/metrics`: 3 charts + a table.
- Eval set (YAML) with simple checks (contains/JSON-valid/length); `make eval` runs it and stores pass rate.
- Tests (pytest) generated with Claude Code, reviewed; CI workflow runs tests + eval.
Out: auth provider, multi-tenant billing, deployment.

## Architecture
```
App code ──► FastAPI gateway ──► adapter: provider A ─┐
                 │      │                             ├─► fallback on error/timeout
                 │      └────────► adapter: provider B ┘
                 ▼
            SQLite request log ──► /metrics ──► React + TS dashboard
            eval set (YAML) ──► CI: pytest + eval pass rate
```

## Milestones
1. Adapter interface + 2 adapters + token counting + cost table. (≈3 h)
2. Retries, timeouts, fallback, budgets; tests via Claude Code, reviewed. (≈3 h)
3. Request logging + `/metrics`. (≈1.5 h)
4. Eval set + `make eval`. (≈1.5 h)
5. React + TypeScript dashboard. (≈2.5 h)
6. CI, README, screenshots. (≈1.5 h)

## README outline
Problem → Architecture → How fallback & budgets work → KPI definitions → Dashboard screenshot → "How I used Claude Code" (what it generated, what I changed, what I rejected) → Run locally → Limitations.

## Demo idea
Send 50 requests via a script, kill provider A (mock outage), watch the dashboard show fallback to provider B with latency and cost changes.

## CV bullets this project must live up to
- Provider-agnostic abstraction layer over multiple LLM provider APIs with token budgeting, streaming, retries, and fallback between providers, logging latency, token usage, and cost for every request.
- KPI dashboard (React, TypeScript) for cost per request, latency percentiles, and evaluation pass rate on a test set; test suite generated with Claude Code and reviewed by hand, running in a CI pipeline.

If something is cut while building, update these bullets in `_work/cv.tex`. When done, mark it `built` in `profile/master-profile.md`; then real numbers (e.g. measured latency, fallback behaviour) may go on the CV.
