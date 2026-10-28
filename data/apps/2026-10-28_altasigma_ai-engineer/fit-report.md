# Fit report: AltaSigma GmbH, AI Engineer (m/w/d), Ulm (on-site focus, flexible hours)

**Fit score: 70/100.** Strong on the core: LLM + agent systems (LangGraph multi-agent), own MCP server (Kniit MCP query service), knowledge graphs (Neo4j, GraphRAG), RAG + vector DBs, systematic evaluation/benchmarking (RAGAS, embedding benchmark on 1M+ chunks), classic ML/DL + time series. Gaps: **fluent German** (top gap), PySpark + Delta/Iceberg lakehouse, Kubernetes only as part of a stack.

Found by job-scout (LinkedIn 4484460384). LinkedIn: Entry level. Language: German posting, "fließend in Deutsch" → German CV + Anschreiben (CLAUDE.md rule 3). Proofread by a native speaker before sending.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Studium Informatik/Mathe/Physik o.ä. | MSc AI | ✅ |
| Praxis als DS/ML Engineer, LLM-Systeme in Produktion | Kniit agentic extraction pipeline built end-to-end and handed over; Covestro agentic app deployed to AWS | ✅ |
| Python sicher, bis zur produktionsreifen Komponente | 3 yrs Python, FastAPI services, microservices | ✅ |
| PySpark, Delta/Iceberg | none | ❌ |
| RAG, LLM-Frameworks, Vektordatenbanken, Indizierung | Covestro thesis RAG pipelines; Kniit indexing strategies; LangChain/LangGraph; Qdrant, Azure AI Search | ✅ |
| Eigene MCP Server | Kniit MCP query service over the knowledge graph, used in Claude Code | ✅ |
| Knowledge Graphen | Kniit Neo4j graph + GraphRAG, Expert Interface curation app | ✅ |
| Data Pipelines, Datenqualität | Kniit ingestion pipeline, deterministic extraction pipeline | ✅ |
| Modellauswahl mit Benchmarking | multilingual embedding benchmark; RF/XGBoost/LSTM comparison; ARIMA/Prophet/LSTM | ✅ |
| Classic ML, Deep Learning, Time-Series | Covestro DS intern, Cognizant | ✅ |
| Container, Kubernetes, CI/CD, Cloud (plus) | Docker, Kubernetes in Kniit stack, GitLab CI/CD, AWS CDK, Azure | 🟡 |
| KI im Arbeitsalltag (Coding Agents) | Claude Code, custom skills | ✅ |
| Kundennähe | Covestro AI consulting with business stakeholders; SAP domain experts | 🟡 |
| Fließend Deutsch | B1, no certificate | ❌ |

## Gaps and honest framing
1. **German (fließend required):** B1. Say so plainly in the letter; German documents show willingness. Biggest risk for a customer-facing role.
2. **PySpark / Delta / Iceberg:** no experience. Planned project adds a PySpark job writing Delta tables; until built, interview only.
3. **Kubernetes:** part of the Kniit stack, no ownership of clusters. Don't overstate.

## Red flags
- Strong on-site preference ("großen Wert auf gemeinsame Arbeit vor Ort") → relocation to Ulm needed.
- Salary not stated ("passt zu Deiner Erfahrung").

## Company hooks
1. AltaSigma Enterprise AI Platform: "Enterprise Data & AI. Eine Plattform." with AI Platform, AI Workbench and AI Solutions layers (altasigma.com).
2. Modules: PrivateGPT-based RAG, Agentic AI with an AI-Agent-Designer, Knowledge Graph (RAG + ontologies + graph databases), Advanced Forecasting & Planning (altasigma.com).
3. Platform components incl. Model Management, Data Lakehouse, AI Governance, MLOps & AutoML (altasigma.com).
4. Data sovereignty, "100 % Made in Germany" (JD).
Note: customer logos on the site (Audi, Continental, LBBW, Telekom …) are not confirmed relationships; not used.

## Projects on the CV
- **Semantic Analytics Agent** (planned, reused; AltaSigma variant: PySpark job → Delta Lake tables, own MCP server for SQL views + glossary graph, model benchmark via LiteLLM). Brief: `_work/project-brief-semantic-analytics-agent.md`. Status: build-first.
