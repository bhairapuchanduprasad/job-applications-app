# Project brief: LLM Gateway (Amadeus Fire KI-Spezialist variant)

Base brief: applications/2026-10-14_accenture_junior-applied-ai-engineer/_work/project-brief-llm-gateway.md (scope, milestones, README outline). Build that; this file lists what this JD adds.

## Why it matters for this JD
Proves the JD items the work history covers weakest: "Monitoring und kontinuierliche Verbesserung von KI-Lösungen, einschließlich Performance, Kosten, Sicherheit und Zuverlässigkeit" and "MLOps-/AI-Infrastrukturen für Deployment und Monitoring".

## Variant additions (within 1–2 days)
- Docker image + GitHub Actions/GitLab CI running tests and a small eval set on every change.
- `/metrics` endpoint: cost per request, latency percentiles, error rate, fallback rate; a simple dashboard (Streamlit is fine).
- Example client: a small RAG chatbot for real-estate FAQs (public tenancy-law FAQ texts) calling the gateway.

## CV bullet it must live up to (German CV)
- Anbieterunabhängige API-Schicht über mehrere LLM-Anbieter mit Token-Budgets, Timeouts, Retries und Fallbacks zwischen Anbietern; Monitoring von Latenz, Token-Verbrauch und Kosten je Anfrage, Tests und Evaluierung in CI.

When built: mark `built` in profile/master-profile.md with real numbers; only then use it in cover letters.
