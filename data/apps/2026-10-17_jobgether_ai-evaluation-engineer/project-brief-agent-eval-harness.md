# Project brief: Agent Eval Harness

**Status:** planned. Build before submitting the Jobgether "AI Evaluation Engineer" application.
**Repo slug:** `agent-eval-harness` (no link on the CV until it exists and you decide to add it)

## Goal
An evaluation, testing and observability harness for a small tool-calling AI agent. It shows the full stack an "founding AI Evaluation Engineer" is hired to build: golden dataset, layered deterministic checks before LLM-as-a-judge, repeated-run statistics with confidence intervals, adversarial tests, tracing, caching/mocking, a load test, and CI in GitHub Actions.

## Why it matters for this JD
Covers the must-haves my work history covers only weakly:
- GitHub Actions + SDK-level execution (I only have GitLab CI/CD)
- Observability/tracing: OpenTelemetry, Arize Phoenix (none in profile)
- Adversarial testing: prompt injection, malformed inputs, unexpected tool responses
- Statistical evaluation: pass rates across N runs, confidence intervals
- Structured output validation: JSON schema, function-calling payloads, OpenAPI
- Multi-turn tests: context retention, state consistency, tool-calling loop safeguards
- Caching/mocking to reduce LLM API calls; load testing non-deterministic endpoints; async Python
Keywords: golden datasets, regression testing, LLM-as-a-judge, embedding similarity, JSON schema validation, function calling, prompt injection, confidence intervals, OpenTelemetry, GitHub Actions, load testing.

## Scope (1–2 days with Claude Code)
**In:** one small agent (LangGraph, 3 tools against a mocked "order/support" API), ~40 golden cases, the eval runner, the report, CI.
**Out:** UI, real external APIs, multiple agent frameworks, a hosted dashboard beyond local Phoenix.

## Tech stack
Python 3.12, LangGraph, LiteLLM (any provider, plus a cheap model for the judge), pytest + pytest-asyncio, jsonschema / Pydantic, sentence-transformers (embedding similarity), OpenTelemetry SDK + Arize Phoenix (OpenInference instrumentation), httpx + asyncio (load test), diskcache (LLM response cache), GitHub Actions.

## Architecture sketch
```
golden/                cases.yaml (single-turn, multi-turn, edge, synthetic, adversarial)
agent/                 LangGraph agent + tools (order_lookup, refund, search_kb) over a mocked API
                       mocked API can return: 200, 500, timeout, malformed JSON, injected text
evals/
  checks.py            Layer 1, deterministic: JSON schema of output, tool-call payload schema
                       (generated from tool signatures / OpenAPI spec), regex, API status, max tool calls
  similarity.py        Layer 2: embedding similarity vs reference answer
  judge.py             Layer 3: LLM-as-a-judge only for cases layers 1-2 can't decide
  stats.py             N runs per case → pass rate + Wilson 95% CI; flag flaky cases
  runner.py            async runner, concurrency limit, cache, writes report.json + report.md
load/                  async load test: ramp concurrency, p50/p95 latency, error rate, pass rate under load
tracing.py             OpenTelemetry → Phoenix; one trace per case, spans per tool call
.github/workflows/eval.yml   PR: deterministic + cached run; nightly: full N-run with live LLM
```

## Milestones
1. Agent + mocked API with fault injection (2–3 h)
2. Golden dataset (40 cases incl. 8 multi-turn, 8 adversarial) + deterministic checks (3 h)
3. Embedding similarity + LLM judge + response cache (2 h)
4. Repeated runs + Wilson CI + flaky detection + report (2 h)
5. OpenTelemetry/Phoenix tracing (1–2 h)
6. Load test (1–2 h)
7. GitHub Actions workflows + README (2 h)

## README outline
Problem, architecture diagram, eval layers and why deterministic first, how to add a case, how to read the report (pass rate ± CI), adversarial cases and what they caught, cost per eval run with and without cache, load-test results, CI setup, limitations.

## Demo idea
A PR that breaks a prompt → CI fails with a report showing pass rate dropping from X% (CI a–b) to Y% on specific cases, plus the Phoenix trace of a failing multi-turn case that loops on a tool.

## CV bullets it must live up to (exact)
- Evaluation pipeline for a tool-calling LangGraph agent: golden datasets for regression testing (edge cases, synthetic multi-turn scenarios); deterministic checks run first (JSON schema validation of structured outputs and function calling payloads, regular expressions, API status checks, embedding similarity), and LLM-as-a-judge scores only what they cannot decide.
- Statistical evaluation runs each case several times and reports pass rates with confidence intervals; adversarial testing covers prompt injection, malformed inputs, unexpected tool responses, and tool-calling loop limits.
- Runs in GitHub Actions with caching of LLM responses and mocking of tools to cut API calls; observability and tracing via OpenTelemetry and Arize Phoenix; asynchronous load testing of the non-deterministic endpoint.

Once built, record real numbers (cost per run with/without cache, pass rates, what adversarial cases caught) in `profile/master-profile.md` and mark it `built`.
