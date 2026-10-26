# Project brief: Agent Eval Harness (Rohde & Schwarz variant)

**Status:** planned. Build before submitting the Rohde & Schwarz "AI / ML Engineer - Agentic AI" application.
**Repo slug:** `agent-eval-harness` (no link on the CV until it exists and you decide to add it)
**Base brief:** `applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md`; CGI variant adds golden conversations, security tests and quality gates (`applications/2026-10-25_cgi_ai-qa-engineer/_work/project-brief-agent-eval-harness.md`). Build one repo that satisfies all three.

## Why it matters for this JD
Covers what the work history covers weakly:
- "evaluierst generatives Verhalten, Sicherheit und Fehlerbilder wie Halluzinationen und etablierst Monitoring und Gegenmaßnahmen"
- "reproduzierbare Evaluationspipelines ... metrikgetriebene Experimente"
- "Evaluationsmethoden für generative Systeme, einschließlich automatisierter Tests, Metriken und Tracing" and "Privacy-, Safety- und Responsible-AI-Bewertung"
Keywords: Halluzinationen, Evaluationspipelines, Tracing, Tool-Calling, MCP, LiteLLM, Monitoring.

## What the R&S CV adds on top of the base brief
- Explicit hallucination / groundedness judge (LLM-as-a-judge with a rubric + deterministic citation check against retrieved context).
- Model comparison run via LiteLLM: same golden set against 2 models (e.g. one API model, one local Ollama model), report pass rate, cost, latency per model = "Foundation-Model-Bewertung".
- Optional: expose the mocked API tools via a small MCP server so the agent uses MCP tool calling.
- Tracing: OpenTelemetry → Arize Phoenix, screenshot in README.
- Privacy check: seeded PII canaries must never appear in outputs (shared with CGI variant).

## Scope (1–2 days with Claude Code)
Same as base: Python 3.12, LangGraph agent with 3 tools over a mocked API, golden YAML set (regression, edge, adversarial), deterministic checks first, then judge, N-run pass rates with Wilson confidence intervals, prompt-injection/malformed-input/tool-loop tests, LLM response caching, GitHub Actions quality gate.

## Exact CV bullets it must live up to (German)
- Evaluations- und Test-Harness für einen Tool-Calling-Agenten über eine gemockte API: Golden Dataset mit Regressions-, Grenz- und adversarialen Fällen, zuerst deterministische Prüfungen (JSON-Schema, Tool-Call-Payloads), danach LLM-as-a-Judge für Halluzinationen und Groundedness, Pass-Raten über mehrere Läufe mit Konfidenzintervallen.
- Tests für Prompt Injection, fehlerhafte Eingaben und Tool-Schleifen, Tracing mit OpenTelemetry und Arize Phoenix, Ausführung als Quality Gate in GitHub Actions.

## Demo idea
README table: two models × categories (regression, edge, adversarial, injection) with pass rate ± CI, cost/run, p95 latency; Phoenix trace screenshot of one failing hallucination case.
