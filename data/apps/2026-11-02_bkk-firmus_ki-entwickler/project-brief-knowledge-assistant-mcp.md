# Project brief: Knowledge Assistant for Internal Documents (BKK firmus variant)

Base brief (full scope, milestones, README outline): applications/2026-10-11_finanz-informatik_ai-engineer/_work/project-brief-knowledge-assistant-mcp.md. Build that; this file only lists what this JD adds.

## Why it matters for this JD
Proves: LLM applications for staff on an internal GPT-like environment, prompts + workflows, rapid prototype that is evaluated, data protection by design (local LLM, nothing leaves the house).

## Variant additions (optional, keep within 1–2 days)
- Corpus: public German statutory-health-insurance texts (e.g. public GKV-Spitzenverband guidelines, a BKK's public FAQ) so the demo is German and in the domain.
- A short DATA_PROTECTION.md: which data is processed, where the model runs, logging without personal data; plus a one-page EU AI Act risk classification of the use case (learning goal for the gap).
- Dockerfile + docker-compose; CI runs lint, pytest and the RAGAS eval.

## CV bullet it must live up to
- (German CV) (title: Interner GPT-Wissensassistent) RAG-Assistent über interne Prozessdokumente mit einem lokal betriebenen Open-Source-LLM, datenschutzkonform, da keine Daten das Haus verlassen; Antworten nennen ihre Quellen, Bereitstellung über eine FastAPI-REST-API und einen MCP-Server; pytest und RAGAS-Evaluationsset in GitLab CI/CD, Request-Logging für das Monitoring.

When built: mark `built` in profile/master-profile.md with real eval numbers; only then use it in cover letters.
