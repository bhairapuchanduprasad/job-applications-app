# Fit report: Navan, Backend Software Engineer (Expense Engineering), Berlin

Source: https://www.linkedin.com/jobs/view/4486413519 (found by job-scout 2026-11-03)
Language: English posting, no German requirement → English CV + cover letter.
Seniority: 1–3 years incl. internships. Good match.

## Fit score: 70 / 100
Backend + LLM agents in a production expense product: receipt extraction, multi-agent assistants with tool use, grounding, retrieval, evals, prompt-injection guardrails, cost/latency. Kniit (multi-agent extraction, P/R eval, deterministic-vs-LLM cost decision, MCP tools) is a strong match. Gaps: Java/Spring Boot (preferred, not mandatory), TypeScript, Kafka, payments/financial systems, streaming UIs.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| 1–3 yrs SWE incl. internships | 3 yrs (Kniit, Covestro x3, Cognizant) | ✅ |
| Backend in Java/Spring Boot, TS/Node or Python | Python/FastAPI, Python microservices | ✅ Python / ❌ Java, TS |
| APIs, relational DBs, cloud | FastAPI REST, Postgres, SQL, AWS (CDK, Lambda, SQS, DynamoDB), Azure | ✅ |
| Kafka/messaging (plus) | AWS SQS only | 🟡 |
| LLM agents: tool use, grounding, retrieval, memory, evals | LangGraph multi-agent, MCP service, RAG thesis, RAGAS/PytrecEval, P/R vs SAP ground truth | ✅ |
| Document extraction quality/latency/cost, provider failover | Extraction from regulatory docs; deterministic pipeline cut $200k LLM budget; LiteLLM | ✅ / 🟡 (no OCR/receipts) |
| Prompt injection, PII guardrails | Not in profile | ❌ (planned project) |
| Observability, quality dashboards | Streamlit dashboard; eval metrics | 🟡 |
| Financial/workflow products | none | ❌ (interest only) |
| Communication, testing, debugging | CTO reporting, SAP experts, Postman API tests | ✅ |

## Gaps and honest framing
1. Java/Spring Boot: not used; JD says preferred, not mandatory. Strong Python backend; willing to pick up Java.
2. TypeScript, Kafka: not used; SQS for queues.
3. Prompt-injection guardrails, PII handling: planned project only.

## Red flags
Navan also posts Senior Expense roles; this one is explicitly 1–3 yrs. Fine.

## Company hooks
1. March 2026: Navan launched Expense Chat, an AI agent where travelers upload receipt photos, it extracts merchant data, auto-codes and asks for missing info ([Business Wire](https://www.businesswire.com/news/home/20260304579230/en/Navan-Launches-New-AI-Agent-to-Eliminate-Manual-Expense-Reports), [CPA Practice Advisor](https://www.cpapracticeadvisor.com/2026/03/05/navan-launches-expense-chat/179311/)). Initially US-only: EMEA rollout is what the Berlin team works on (VAT, per diem, multi-entity per JD).
2. May 2026: four AI T&E tools in beta incl. an Expense Admin Companion for flagged spend and voice/video expense capture (OCR + speech-to-text) ([Pulse aggregator](https://www.pulse.bot/ai/news/navan-unveils-ai-tools-to-streamline-business-travel-0eb832f4-96fd-4ffb-a98b-144c84c2c670/)).
3. JD: "Prefer deterministic code for policy, catalogs, and tax rules; use models for language, ranking, and tool orchestration" — same principle as the Kniit deterministic pipeline.

## Project
Expense Missing-Info Agent (Agent Eval Harness variant, planned): see project-brief-expense-missing-info-agent.md.
