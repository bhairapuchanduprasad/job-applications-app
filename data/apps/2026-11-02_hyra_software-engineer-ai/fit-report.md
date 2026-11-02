# Fit report: Hyra (client: established financial services company, not named), Software Engineer (AI), Berlin, hybrid

Source: https://www.linkedin.com/jobs/view/4486137373 (found by job-scout 2026-11-02)
Language: English posting, no German requirement → English documents.
Seniority: LinkedIn "Mid-Senior level"; text asks for "proven experience", no years given.

## Fit score: 80 / 100
The task list reads like the Kniit job description: retrieval pipelines with indexing and evaluation logic, structured context (knowledge graph via MCP), multi-step agentic workflows, prompting strategies, cost-efficiency. Gaps are enterprise-platform integration at a large financial group and seniority wording.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Develop/optimise data retrieval pipelines, indexing, evaluation logic | Kniit ingestion→chunking→indexing pipeline; evaluation vs SAP ground truth; RAGAS/PytrecEval thesis | ✅ |
| Integrate structured context systems for automated workflows | Neo4j knowledge graph exposed via MCP service to Claude Code | ✅ |
| Multi-step agentic workflows and orchestration logic | LangGraph 4-agent parallel pipeline with reflection; Covestro routing agent | ✅ |
| Prompting strategies and context preparation | Prompt engineering + chunking strategies at Kniit and Covestro | ✅ |
| Integrate models into enterprise platforms; performance + cost-efficiency | Deterministic pipeline cut $200k LLM budget; Expert Interface on Azure; AWS CDK deployments | ✅ / 🟡 (no large financial-enterprise platform) |
| Proven software development with LLMs and intelligent systems | 3 years, current role fully LLM-based | ✅ |
| Retrieval architectures + structured knowledge systems | GraphRAG, Neo4j, vector DBs, embedding benchmark on 1M+ chunks | ✅ |
| Performance benchmarking and optimisation | Embedding model benchmark, P/R improvement, millisecond-latency MCP retrieval | ✅ |
| Collaborate with platform engineers, cross-functional | CTO, SAP domain experts, chemists | ✅ |

## Gaps and honest framing
1. **Financial services domain**: none. Frame regulated-document work (energy-sector regulation) as adjacent.
2. **Seniority ("Mid-Senior")**: 3 years; keep letter factual about scope (sole owner of pipeline).
3. **Large enterprise platform integration**: Covestro is an enterprise; mention Azure/AWS deployments only.

## Red flags
- Recruiter (Hyra) posting, client unnamed; ask for the company name and salary band.

## Company research
Hyra is a recruitment platform; client is not named and searching would be guesswork. No hooks; letter focuses on the work described.
