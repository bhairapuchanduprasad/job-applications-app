# Application notes: HAIAR GmbH, Backend Software Engineer - AI Systems

Status: **build-first**. Build `autohaus-service-agent` (brief in this folder) and `llm-gateway` (brief in the Accenture folder) before submitting, or remove the Projects section.

## Likely interview questions
1. **"Walk us through the architecture of your Kniit pipeline. What would you change?"**
   Ingestion → chunking → prompt engineering → indexing with three strategies (agentic, deterministic, monolithic). Multi-agent LangGraph extraction (entity, relationship, consolidation, reflection agents in parallel), Neo4j/MongoDB/Postgres storage, MCP query service on top, Expert Interface (Python microservices + React on Azure) for expert approval. Precision/recall 33%/45% → 93%/90% against SAP-derived ground truth. Have one honest "what I'd change" ready (e.g. monitoring/observability earlier).
2. **"How do you decide between an LLM and plain code / between quality, latency and cost?"**
   The $200k case: high-volume second source stream → deterministic pipeline, near-zero recurring cost, accuracy toward 100%. Then a general rule: measure first (ground truth), use LLMs where variance in input demands it.
3. **"How would you detect hallucinations and drift in a RAG system in production?"**
   Thesis: RAGAS (faithfulness, answer relevancy) + PytrecEval for retrieval vs chemist ground truth; embedding benchmarks on 1M+ chunks. Kniit: reflection agent + ground-truth evaluation. Drift: talk about the planned scheduled eval comparison (only claim it once built).
4. Possible German-language part: B1, be upfront; prepare a 2-minute self-introduction in German.

## Ready answers for form fields
- **Why HAIAR?** CARvinci promises dealerships an AI that works without interfaces or an IT project, on German servers and DSGVO-compliant. That puts the hard problems in the backend (reliable ingestion, grounded answers, data staying in Germany), which is exactly what I built for a regulated sector at Kniit. I want to own that backend for a product that is used by non-technical people in service and sales.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000). Must meet the Blue Card threshold.
- **Notice period / earliest start:** 15 November 2026.
- **Work authorization:** EU Blue Card (Germany), no sponsorship needed.
- **Location:** Essen; remote fine, can travel to Münster for team meetings.
- **German level:** B1 (no certificate).
- **Why are you leaving Kniit?** "Kniit is an early-stage startup that restructured around a senior SAP-focused hire before its funding round; my position ended after I had built and handed over its knowledge-extraction pipeline end-to-end."
