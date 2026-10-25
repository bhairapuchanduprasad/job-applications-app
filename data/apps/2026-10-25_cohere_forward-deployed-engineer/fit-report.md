# Fit report: Cohere, Forward Deployed Engineer, Agentic Platform (Europe), Berlin / Germany (remote-friendly)

**Fit score: 76/100.** Close match on the core: LLM-powered agents with tools and orchestration (LangGraph multi-agent system), RAG, systematic evaluation against ground truth, Python, end-to-end ownership as sole developer, and customer-facing translation of ambiguous needs (Covestro AI consulting). Gaps: "production-grade" enterprise deployments at scale, named agent patterns (ReAct, Plan-and-Execute), latency/safety evaluation, enterprise security/compliance, and this is a senior-leaning role ("lead the design", "set architectural standards").

Language: English posting, no German requirement → English documents. German customers: B1 is a plus point to mention only if asked.

Source: https://www.linkedin.com/jobs/view/4418823251 (same role also listed as Berlin 4418824220 and Frankfurt 4418816639). Travel 20–40%.

## Requirements → evidence
| Requirement | Evidence | Rating |
|---|---|---|
| Production-grade Python, clean/testable/observable code | Python in all roles; FastAPI services; Docker, AWS CDK, GitLab CI/CD; clean code principles | 🟡 (scale) |
| RAG and agentic apps; agents that plan and execute multi-step tasks | Kniit multi-agent LangGraph (extraction, relationships, consolidation, reflection); Covestro routing agent; RAG pipelines | ✅ (ReAct/Plan-and-Execute not named) |
| LLM stack: frontier models, vector DBs, orchestration | LiteLLM over LLM APIs; Qdrant, Pinecone, Azure AI Search; LangGraph, LangChain | ✅ |
| Evaluation frameworks for accuracy, safety, latency | Ground-truth evaluation (33/45 → 93/90); RAGAS + PytrecEval; latency: millisecond MCP retrieval; safety evals not in profile | 🟡 |
| Customer work, translating ambiguous needs into specs | Covestro AI Consulting Intern; SAP domain experts and CTO at Kniit | ✅ |
| Own a use case end to end | Sole developer at Kniit | ✅ |
| Frontend when needed | React (Covestro, Expert Interface) | ✅ |
| Regulated industries, auditability (bonus) | Regulatory energy-sector documents; expert approval step | 🟡 |
| Travel 20–40% | Fully willing | ✅ |

## Gaps and honest framing
- **Scale/production:** systems used by a small team of experts; don't inflate user numbers.
- **Agent patterns:** explain your LangGraph designs in ReAct / plan-execute terms in the interview; prepare one example.
- **Safety evaluation:** not done formally; talk about grounding checks and human approval.
- **Seniority:** the role says "lead"; apply anyway (they encourage it), lean on end-to-end ownership.

## Red flags
- Global company with many FDE openings: competitive; apply via careers page or LinkedIn quickly.
- AI-assisted screening (stated in posting): keyword coverage matters.

## Company hooks (sources)
1. North: AI workspace platform combining LLMs, search and agents; can run in private, including air-gapped, environments. Source: https://betakit.com/cohere-launches-customizable-enterprise-ai-workspace-platform-north/
2. Enterprises using North to deploy agents include RBC, Dell, LG CNS, Ensemble Health Partners and Second Front; RBC co-develops "North for Banking". Sources: https://www.constellationr.com/insights/news/cohere-launches-north-aims-be-ai-agent-workspace , https://www.maginative.com/article/cohere-launches-north-a-secure-ai-workspace-for-enterprise-productivity/
3. Security-first enterprise AI company with its own frontier models; Berlin office. Source: posting.
