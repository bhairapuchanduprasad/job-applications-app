# Fit report: Kuehne+Nagel, Agentic AI Engineer (m/f/d), Sea Logistics, Bremen

**Fit score: 70/100.** Strong: designing and optimizing multi-agent LangGraph systems benchmarked for accuracy and cost (Kniit 33/45 → 93/90 P/R, $200k projected LLM budget → near zero via deterministic fallback), human validation (Expert Interface approval flow), RAG + retrieval fine-tuning, Python, AWS + Azure, Docker/Kubernetes, SQL/NoSQL (Postgres, MongoDB, Neo4j), translating business workflows into architectures (Covestro AI consulting). Gaps: 3+ years specifically on agentic systems (~1.5 years), integration with logistics systems (TMS/WMS/ERP), event-driven platforms (only SQS), explicit guardrail frameworks, logistics domain.

Found by job-scout (LinkedIn 4476769937). English posting, no German requirement → English documents.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Autonomous agents: reasoning, planning, task execution | Kniit 4-agent LangGraph extraction with reflection; Covestro routing agent | ✅ |
| LangChain / CrewAI / ReAct / custom | LangChain, LangGraph (custom multi-agent) | ✅ |
| Integrate with TMS/ERP/CRM/WMS, APIs, DBs, event-driven | SAP-derived ground truth, MCP service over KG, FastAPI APIs, SQS | 🟡 |
| Guardrails, validation, fallback, human-in-the-loop | Expert Interface approval of graph changes; deterministic pipeline instead of LLM; ground-truth validation | 🟡 |
| Monitoring, logging, explainability | evaluation pipelines (RAGAS, PytrecEval); no production monitoring stack | 🟡 |
| Benchmark accuracy, latency, cost | P/R vs ground truth, $200k cost cut, millisecond-latency MCP, embedding benchmark 1M+ chunks | ✅ |
| 3+ years agentic AI systems | ~1.5 years agentic (Covestro 12/2024–04/2025, Kniit 11/2025–); 3 years AI total | 🟡 |
| Python, AWS/Azure/GCP | Python; AWS CDK; Azure | ✅ |
| RAG, prompt engineering, model tuning, LLM orchestration | thesis RAG, QLoRA fine-tuning, retrieval fine-tuning, LangGraph | ✅ |
| Docker, Kubernetes | Docker; Kubernetes in Kniit stack | ✅ |
| Logistics knowledge (preferred) | none | ❌ |

## Gaps and honest framing
1. **Years on agentic systems:** ~1.5 of 3 years; the rest is ML/RAG. Say it plainly, lead with depth of the Kniit system.
2. **Logistics systems integration / event-driven:** no TMS/WMS; frame SAP-system data work and API/MCP integrations. Project adds a mocked booking/TMS API.
3. **Guardrails / monitoring in production:** human approval + deterministic fallback are real; project adds explicit guardrails + tracing.

## Red flags
- Reported 2,000-job layoff tied to weak demand and an AI push (freightwaves.com headline, 2025/26); check team stability.
- Salary not stated.

## Company hooks
1. Q2 2026 results: AI embedded in myKN cut booking time "from minutes to seconds" and reduced human errors (Kuehne+Nagel Q2 2026 ad-hoc release, assets.kuehne-nagel.com).
2. CEO Stefan Paul: agentic AI is "not about replacing the human agent but rather supporting them" (search summary of company statements).
3. Several Sea Logistics agentic roles open (careers.kuehne-nagel.com): customer support agents, AI operations assistants.
4. Sea Logistics Q2 2026: net turnover CHF 2.2bn, EBIT CHF 140m, sea-freight yield pressure (ad-hoc release).

## Projects on the CV
- **Agent Eval Harness** (planned, reused; K+N variant: tool-calling LangGraph agent over a mocked shipment-booking/TMS API with input/output guardrails, schema validation, fallback to a rules path and human approval; benchmarks accuracy, latency and cost per run). Brief: `_work/project-brief-agent-eval-harness.md`. Status: build-first.
