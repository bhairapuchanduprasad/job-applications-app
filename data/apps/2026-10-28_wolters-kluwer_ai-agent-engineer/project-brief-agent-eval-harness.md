# Project brief (variant): Agent Eval Harness, Wolters Kluwer AI-Agent Engineer

Base brief: applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md (build that; this file lists only the additions for this CV).

## Why for this JD
Wolters Kluwer wants agents in production with guardrails, validation, observability, evaluation and clear autonomy limits (human-in-the-loop). The harness proves exactly these keywords.

## Additions for this variant (1 extra half-day)
- Mocked accounting API (FastAPI): list open receipts (Belege), propose booking (Buchungsvorschlag), post booking.
- LangGraph agent with tools over that API; an autonomy rule: postings above an amount threshold or with low confidence go to a human approval step (interrupt + resume).
- Golden dataset includes approval-required cases; tests assert the agent stops and asks.

## CV bullets it must live up to (German)
- Evaluations-Harness für einen tool-aufrufenden LangGraph-Agenten über eine gemockte Buchhaltungs-API: Golden Dataset, deterministische Validierung (JSON-Schema, Function Calls), dann LLM-as-a-Judge; Human-in-the-Loop-Freigabe oberhalb einer Autonomiegrenze.
- Guardrail-Tests gegen Prompt Injection, fehlerhafte Eingaben und Tool-Schleifen; Observability mit OpenTelemetry und Arize Phoenix, Tests in GitHub Actions.
