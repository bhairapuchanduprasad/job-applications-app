# Fit report: HAIAR GmbH, Backend Software Engineer - AI Systems (m/w/d)

**Fit score: 76/100.** Strong on the AI side (RAG, embeddings, agent workflows, evaluation); the risks are "mehrjährige" pure backend experience, explicit monitoring/drift work, and an all-German posting.

**Language decision:** posting is in German but names no German requirement → English CV + cover letter (CLAUDE.md rule 3). A small Münster team will likely speak German internally; German B1 is shown on the CV. See gaps.

## Requirements → evidence

| Requirement | Evidence | |
|---|---|---|
| Mehrjährige Backend-Erfahrung mit Python | Python across all roles; backend work: Kniit Python microservices + pipeline (11/2025–11/2026), Covestro FastAPI backend (12/2024–04/2025), AWS Lambda/SQS/DynamoDB infra (thesis). ~2 years of backend-heavy work inside 3 years total | 🟡 |
| Skalierbare Backend-Architekturen und APIs | Python microservices on Azure + Kubernetes (Kniit); FastAPI + Docker + AWS CDK (Covestro); event-driven Lambda/SQS/DynamoDB (thesis); MCP query service with millisecond-latency retrieval | ✅ |
| Produktive Systeme, nicht nur Prototypen | Kniit pipeline owned end-to-end and handed over; Expert Interface deployed on Azure for domain experts; Covestro agentic app deployed to AWS via CI/CD | ✅ |
| Technische Entscheidungen treffen und vertreten | Chose a deterministic pipeline over LLMs for a high-volume stream: $200,000 projected LLM budget → near-zero; reported directly to the CTO as sole developer | ✅ |
| RAG-Architekturen für produktive Anwendungsfälle | RAG pipeline design (chunking, vector DBs, indexing) + RAG evaluation thesis at Covestro; GraphRAG at Kniit | ✅ |
| KI-Pipelines (Ingestion, Retrieval, Kontextsteuerung, Inferenz) | Kniit: ingestion, chunking, prompt engineering, indexing; agentic / deterministic / monolithic strategies | ✅ |
| Embeddings, Retrieval-Strategien, Kontextmanagement | Benchmarked multilingual embedding models on 1M+ chunks; retrieval eval with PytrecEval | ✅ |
| Agent-Workflows inkl. Zustands- und Fehlerhandling | LangGraph multi-agent (parallel extraction, consolidation, reflection agents); Covestro LangGraph router. State/error handling not described explicitly in profile | 🟡 |
| Trade-offs Qualität / Latenz / Kosten / Skalierbarkeit | $200k cost decision; precision/recall 33%/45% → 93%/90%; millisecond-latency MCP service | ✅ |
| Stabilität, Monitoring, Wartbarkeit | Clean code, CI/CD (GitLab), Docker/K8s. No explicit monitoring/observability tooling in profile | 🟡 |
| Halluzinationen, Drift, Latenz, Evaluierung | Evaluation strong (RAGAS, PytrecEval, ground-truth P/R); reflection agent; drift: no evidence | 🟡 |

## Gaps and honest framing
1. **"Mehrjährige" backend experience:** 3 years professional, of which the last ~2 are backend-heavy AI work. Frame as "3 years building and deploying AI applications, Python backend throughout"; don't claim "senior".
2. **Monitoring / drift:** no tooling in the profile. Covered by planned projects (LLM Gateway: latency/cost/status logging + metrics; Autohaus Service Agent: weekly eval comparison for drift). Must be built before submitting. In interviews: talk about eval-as-quality-gate at Kniit.
3. **Agent state + error handling:** real LangGraph experience, but no explicit description. If true, add to profile how state/retries were handled at Kniit (would strengthen this and future applications).
4. **German:** B1, no certificate. Not required in the posting, but the whole JD is German and the team is small. Expect the interview may test German; be upfront.
5. **Seniority:** "technisch mit verantwortlich für das Backend" suggests mid-level ownership. Sole-developer ownership at Kniit is the best counter.

## Red flags
- Small company (directories say 1–10 / 11–50; 6 on LinkedIn). Salary "marktgerecht", no number; Blue Card threshold must be met.
- Product claims (3x faster, 100+ solutions) are vendor marketing, not verified.
- Kniit layoff: use the public line from the profile only.
- 48 applicants in 4 hours: apply fast.

## Company hooks (step 4)
1. CARvinci: AI for car dealerships, 100+ AI solutions for service, sales, Disposition, admin, HR, marketing; built over ~a year with 30+ pilot dealerships. Source: job post; https://himalayas.app/companies/haiar
2. Runs on German servers and is marketed as DSGVO- and EU AI Act-compliant; set up in under 5 minutes without integrations. Source: https://himalayas.app/companies/haiar
3. Offers a certified "Autohaus KI-Manager" training for dealership staff, i.e. adoption by non-technical users matters. Source: https://himalayas.app/companies/haiar
4. Works with dealer groups including Mercedes-Benz dealers; Münster-based, remote-first. Source: https://himalayas.app/companies/haiar
5. No funding news, tech-stack details or named hiring manager found (searched 4×). Only Python is listed as stack.

Hook used in the letter: the "no interfaces, no IT project" promise + DSGVO/German servers. That puts the burden on the backend (ingestion, retrieval, guardrails), which is exactly the work done at Kniit for a regulated sector.
