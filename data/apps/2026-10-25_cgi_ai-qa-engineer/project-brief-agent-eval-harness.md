# Project brief: Agent Eval Harness (CGI variant)

**Status:** planned. Build before submitting the CGI "AI QA Engineer – Conversational AI & GenAI-Automationen" application.
**Repo slug:** `agent-eval-harness` (no link on the CV until it exists and you decide to add it)
**Base brief:** `applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md` (same repo). This file lists what the CGI CV adds on top; build one repo that satisfies both.

## Goal
A test harness for a small conversational (chat) agent with tool calling, showing what CGI's AI QA Engineer builds: golden datasets/conversations, automated regression, deterministic checks before LLM-as-a-judge, security and robustness tests, quality gates with release criteria in CI, monitoring via tracing.

## Why it matters for this JD
Covers must-haves my work history covers weakly or not at all:
- "Aufbau eines AI Test Harness inkl. Golden Datasets/Conversations, automatisierter Regression und relevanter Qualitätsmetriken"
- "Security & Robustness (z. B. Prompt Injection, Data Leakage, Rollen-/Rechtekonzepte)"
- "Teststrategie ... (Testpyramide, Quality Gates, Releasekriterien)" and "Integration von Testautomatisierung in CI/CD ... Monitoring"
- "Handover" (bot → human) as a tested conversation outcome
- GenAI specifics: Tool Calling, Guardrails/Evaluation
Keywords: AI Test Harness, Golden Datasets, Golden Conversations, Regression, Qualitätsmetriken, Prompt Injection, Data Leakage, Quality Gates, Releasekriterien, CI/CD, Monitoring, Tool Calling, Conversational AI.

## Scope (1–2 days with Claude Code)
**In (on top of the base brief):**
- The agent is a customer-service chat agent (e.g. order/booking support) with 3 tools over a mocked API and a `handoff_to_human` tool.
- Golden conversations: multi-turn YAML cases with expected tool calls, expected final state and expected handover.
- Roles: two user roles (customer, agent-supervisor) with tool permissions; tests check a customer cannot trigger supervisor-only tools (role/permission test).
- Data leakage tests: seeded secret in system prompt + other-customer PII in the mocked API; assert neither appears in any answer (regex + canary strings).
- Prompt injection tests: injected instructions in user turns and in tool responses.
- Test pyramid in the README: unit tests of tools/validators → deterministic eval layer → LLM-as-a-judge → E2E conversation runs.
- Quality gates: `gates.yaml` with release criteria per category (e.g. security 100% pass, regression pass-rate lower CI bound ≥ threshold); GitHub Actions fails the PR when a gate fails.
**Out:** voice, RPA/workflow engines, Selenium UI tests, hosted dashboard.

## Tech stack
Python 3.12, LangGraph, LiteLLM, pytest, jsonschema/Pydantic, sentence-transformers, OpenTelemetry + Arize Phoenix, diskcache, GitHub Actions.

## Architecture sketch
```
golden/        conversations/*.yaml (multi-turn, edge, handover), security/*.yaml (injection, leakage, roles)
agent/         LangGraph chat agent, tools (order_lookup, change_booking, handoff_to_human), role-based tool permissions
evals/         checks.py (schema, payloads, regex/canaries, API status) · judge.py · stats.py (N runs, Wilson CI) · runner.py
gates.yaml     release criteria per category → gate.py exits non-zero
.github/workflows/eval.yml   PR: unit + deterministic + cached run + gates; nightly: full N-run
tracing.py     OpenTelemetry → Phoenix
```

## Milestones
1. Chat agent + mocked API + roles (3 h)
2. Golden conversations + security cases + deterministic checks (3 h)
3. Judge, N-run stats, report (2 h)
4. Quality gates + GitHub Actions (2 h)
5. Tracing + README with test pyramid (2 h)

## README outline
Problem, test pyramid, golden conversation format, security tests and what they caught, quality gates and release criteria, how to read the report, CI, limitations (no voice/RPA).

## Demo idea
A PR that weakens the system prompt → leakage/injection cases fail → the security gate blocks the merge; Phoenix trace of the failing conversation.

## CV bullets it must live up to (exact, German)
- AI Test Harness für einen Agenten für Conversational AI mit Tool Calling über eine gemockte API: Golden Datasets und Golden Conversations (Multi-Turn, Edge Cases, Handover an einen Menschen) für automatisierte Regression; deterministische Prüfungen (JSON-Schema, Tool-Calling-Payloads, API-Status) vor LLM-as-a-Judge.
- Security- und Robustheitstests für Prompt Injection, Data Leakage, Rollen-/Rechteprüfung der Tools und fehlerhafte Eingaben; Qualitätsmetriken als Passrate mit Konfidenzintervall über mehrere Läufe.
- Teststrategie nach Testpyramide bis zu End-to-End-Tests; Testautomatisierung in der CI/CD-Pipeline (GitHub Actions) mit Quality Gates und Releasekriterien; Mocking von LLM-Aufrufen, Monitoring per Tracing mit OpenTelemetry und Arize Phoenix.

Once built, record real numbers (pass rates, what the security cases caught, cost per run) in `profile/master-profile.md` and mark it `built`.
