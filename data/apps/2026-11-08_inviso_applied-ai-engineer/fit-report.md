# Fit report: Inviso (recruiter for an anonymous client), Applied AI Engineer, Germany (remote)

**Fit score: 68/100.** Strong match on agentic systems, RAG, evaluation, MCP/tool calling and Claude. Weaker on production monitoring at scale, guardrails in a live system, and enterprise consulting experience.

German requirement: No mention of German. Posting in English. CV and letter in English.
Note: same recruiter and same boilerplate as applications/2026-11-05_inviso_backend-platform-engineer (Backend / Platform Engineer), but a different role and JD (Applied AI vs backend). Likely the same anonymous client, so a second application may be seen by the same recruiter.

| Requirement | Evidence | |
|---|---|---|
| LLM/RAG/agentic software in production | Kniit extraction pipeline (sole dev), Covestro agentic app on AWS | ✅ |
| Agent runtime, orchestration, tool calling | LangGraph multi-agent, MCP query service | ✅ |
| RAG, retrieval quality, prompt design | Covestro thesis, chunking/embedding benchmarks | ✅ |
| Evaluation harnesses, golden sets | RAGAS/PytrecEval, SAP ground truth (33/45 to 93/90) | ✅ |
| Cost, latency as constraints | $200k budget to near zero, ms-latency MCP | ✅ |
| Guardrails, untrusted retrieved content | Only via planned Agent Eval Harness project | 🟡 |
| Production monitoring | Planned Langfuse in projects; no live monitoring evidence | 🟡 |
| Model routing | LiteLLM at Kniit; planned LLM Gateway | 🟡 |
| Claude/GPT, fine-tuning, open-source | Claude Code, QLoRA Open Llama (personal project) | ✅ |
| LLM-as-judge calibrated vs human | Planned project only | 🟡 |
| A2A | none | ❌ |
| Ontologies, knowledge graphs, semantic layers | Neo4j graph, Protégé/SPARQL/OWL project | ✅ |
| Client-facing consulting | Covestro AI consulting internship | 🟡 |

## Gaps
- A2A: not on CV.
- Guardrails / monitoring / LLM-as-judge in live production: shown only through planned projects (Agent Eval Harness, LLM Gateway); build them before submitting.
- Seniority: "experienced" role from a recruiter; I have about 3 years.

## Red flags
- Recruiter posting with anonymous client ("global multi-billion dollar software conglomerate"); body text starts with "Backend / Platform Engineer", possibly a copy-paste from the other posting.

## Hooks (company research)
Skipped: the client is anonymous and Inviso is only the recruiter. Letter uses the JD's own emphasis (production over demos, evaluation in delivery).
