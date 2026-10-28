# Project brief (variant): Agent Eval Harness, SIGNAL IDUNA AI Governance Engineer

Base brief: applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md. Security/permission tests: see the CGI variant applications/2026-10-25_cgi_ai-qa-engineer/_work/project-brief-agent-eval-harness.md. This file lists only the governance additions.

## Why for this JD
SIGNAL IDUNA wants technical evaluation of GenAI/agent solutions and governance guardrails that are technically enforceable: models, data flows, tools, permissions, logging, operations.

## Additions
- Mocked insurance API (FastAPI): get_policy, get_claim, update_address; two roles (customer, agent) with different permissions.
- Tests: prompt injection, data leakage (agent must not reveal another customer's policy), role-permission violations, tool loops.
- Quality gates with explicit release criteria (pass-rate thresholds) in GitHub Actions; failing gate blocks merge.
- Governance sheet per agent (Markdown): model, data sources, tools + permissions, logging, human-in-the-loop points, open risks. One page, generated from config.

## CV bullets it must live up to (German)
- Test-Harness für einen tool-aufrufenden LangGraph-Agenten über eine gemockte Versicherungs-API: Golden Dataset, deterministische Prüfungen (JSON-Schema, Function Calls), dann LLM-as-a-Judge; Leitplanken-Tests auf Prompt Injection, Datenabfluss und Rollenberechtigungen.
- Qualitäts-Gates mit Freigabekriterien in GitHub Actions, Governance-Steckbrief pro Agent, Traces mit OpenTelemetry und Arize Phoenix.
