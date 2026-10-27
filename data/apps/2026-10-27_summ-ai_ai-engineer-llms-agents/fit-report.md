# Fit report: summ AI, AI Engineer – LLMs & Agents, Munich (hybrid)

**Fit score: 70/100.** Close match on the core tasks: building LLM features and agents end-to-end (LangGraph at Kniit and Covestro, React + FastAPI), connecting models to data sources and tools (MCP service, vector DBs), evaluations (ground-truth P/R at Kniit, RAGAS/PytrecEval thesis), cost thinking ($200k projected LLM budget → near-zero), cloud deployment (AWS CDK, Azure, Docker, K8s). Weaker: "mehrjährige" software engineering (3 years), production monitoring of live features, direct customer contact with public-sector clients, and German.

Language: German posting, but no German requirement is stated → English CV + cover letter (CLAUDE.md rule 3). **Implicit gap:** the role talks directly to German public-administration customers, so German beyond B1 will likely matter. Found by job-scout (LinkedIn 4481483208).

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Mehrjährige Softwareentwicklung, features end-to-end | 3 years; full stack at Covestro (FastAPI + React) and Kniit (React + Python microservices) | 🟡 |
| Practical experience with LLM applications or agents | LangGraph multi-agent extraction (Kniit), agentic router (Covestro) | ✅ |
| Connect models to data sources and tools; prompts, context, agent flows | MCP service over the knowledge graph, vector DBs, prompt engineering | ✅ |
| Analyse errors, build evaluations, compare models on quality/speed/cost | Ground-truth evals (33/45 → 93/90), RAGAS/PytrecEval, embedding model benchmark on 1M+ chunks, $200k cost cut | ✅ |
| Deploy, monitor, cloud infrastructure | Docker, AWS CDK, Azure, K8s, GitLab CI/CD; monitoring of live usage not evidenced | 🟡 |
| Customer contact, product sense | Covestro AI consulting with business stakeholders; Kniit with SAP domain experts | 🟡 |
| Use AI tools to automate work | Claude Code with custom skills, agentic coding workflows | ✅ |
| Own projects / open source | Old GitHub notebooks (QLoRA meme LLM etc.); planned projects | 🟡 |
| Public sector interest | none in profile | 🟡 |
| German (implicit, public-sector customers) | B1 | ❌ (implicit) |

## Gaps and honest framing
1. **German for customer contact:** state B1 openly in the letter; English business fluent.
2. **Monitoring live usage:** don't claim it; Knowledge Assistant project adds request logging with latency/retrieval metrics (planned).
3. **Years:** 3 years, but as sole developer owning a pipeline end-to-end.

## Projects on the CV (both `planned` → build-first)
- **Knowledge Assistant for Internal Documents** (reused; brief applications/2026-10-11_finanz-informatik_ai-engineer/_work/project-brief-knowledge-assistant-mcp.md): RAG over process documents with cited sources, REST + MCP, RAGAS in CI, monitoring. Matches "Verwaltungswissen zugänglich machen". Optional summ-AI angle when building: use public municipal process descriptions as the corpus.
- **Agent Eval Harness** (reused; brief applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md): evaluations, "show that a change actually works better".
No new project created. summ AI says "Zeig uns, was du gebaut hast", so building at least the Knowledge Assistant first matters.

## Red flags
- None serious. Small GovTech startup; salary not stated.

## Company hooks
1. Founded 2022 in Munich by Flora Geske, Vanessa König (née Theel) and Nicholas Wolf; started with an AI plain-language translation tool for municipal websites, now also AI-based process-management software for public administrations ([Munich Startup](https://www.munich-startup.de/en/startups/summ-ai-gmbh/)).
2. Won the GovTech category of the Smart Country Startup Award 2023 (Bitkom) ([Gründerküche](https://www.gruenderkueche.de/news/gruender-news/smart-country-startup-award-2023-summ-ai-und-plan4-software-sind-die-sieger/)).
3. From the JD: making administrative knowledge accessible, simplifying processes, automating routine work; ship early and improve from real usage.
