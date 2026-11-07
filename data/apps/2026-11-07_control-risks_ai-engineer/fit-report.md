# Fit report: Control Risks, AI Engineer (Berlin)

**Fit score: 82/100.** Knowledge-graph + agentic + Neo4j + LLM-API work is exactly what I did at Kniit; gaps are Graphiti, Cypher-at-scale/performance tuning and the compliance domain.

German: No mention of German (CV in English requested by posting).

| Requirement | Evidence | |
|---|---|---|
| 3+ yrs AI/ML eng, 1+ yr knowledge graphs in production | 3 yrs total; Kniit since 11/2025 (~1 yr) owning KG extraction pipeline + MCP query service | ✅ |
| Neo4j (modelling, Cypher, tuning) | Neo4j in Kniit stack, graph curation app; no Cypher performance tuning documented | 🟡 |
| LLM APIs, structured outputs, tool calling, cost mgmt | LiteLLM, LangGraph, MCP; cut $200k projected LLM budget to near zero; structured outputs/tool calling not explicitly documented | 🟡 |
| LLM vs small fine-tuned models | HF Transformers, QLoRA, embedding fine-tuning/benchmarking (Covestro) | ✅ |
| Agentic pipelines (tools, memory, state) | LangGraph multi-agent at Kniit and Covestro | ✅ |
| Python, testable, async | Python daily; async not documented | 🟡 |
| RAG (vector, hybrid) | Covestro thesis, GraphRAG, vector DBs | ✅ |
| Read research papers into prototypes | MSc thesis, RAG eval; no specific story | 🟡 |
| Graphiti / temporal KG | Not in profile | ❌ |
| Entity resolution / NER / topic modelling | Entity-extraction + consolidation agents (Kniit); NLTK IE project; no topic modelling | 🟡 |
| Evaluation frameworks for structured outputs | Precision/recall 33/45 -> 93/90 vs ground truth; RAGAS | ✅ |
| Databricks / Delta Lake, GCP | Not in profile (AWS, Azure only) | ❌ |
| Sanctions / KYC / AML, RegTech | Regulatory-document extraction only (energy) | ❌ |
| Claude Code context files | Claude Code, custom skills at Kniit | ✅ |
| .NET integration via HTTP | HTTP/FastAPI microservices; no .NET | 🟡 |

## Gaps and framing
- Graphiti, Databricks, GCP, KYC/AML: left out of CV; stated honestly as new to me. Planned project covers entity resolution + Cypher QA + eval harness (not built yet).
- Domain: frame regulatory/technical-document extraction as adjacent.

## Red flags
- Small team, "significant autonomy": likely wide scope. Job ad lists many must-haves for a 3-year profile. No salary stated.
- Notion/CLAUDE.md documentation expectations are fine.

## Company hooks (no web research in this unattended run; from the posting only)
- Control Risks is a risk consultancy; the platform is a third-party-risk / compliance knowledge graph (posting).
- Role owns the graph data model and interrogation layer: natural-language compliance questions to Cypher (posting).
- Team: CTO + data engineer + junior AI engineer (posting).
- Posting stresses evaluation harnesses before scaling pipelines, which matches my Kniit precision/recall work.
