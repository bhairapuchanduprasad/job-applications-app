# Fit report: Sportradar, Forward Deployed AI Engineer (m/f/d), Leipzig (on-site, 5 days)

**Fit score: 82/100.** Very close match: internal-consultant style role (talk to departments, find problems, build LLM/agent solutions, evaluate). Covestro AI consulting + Kniit sole-developer agentic system + RAG evaluation thesis cover nearly every point. Gaps: quality dashboards for LLM evals (not shown in work), SQL/data pipelines only moderate, no sports/betting domain.

Language: English posting, no German requirement → English CV + letter. Found by job-scout (LinkedIn 4484093079; identical JD also posted as 4481885941, skipped as duplicate: apply once).

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| ~2+ yrs SWE or applied ML | 3 years (Kniit, Covestro x3, Cognizant) | ✅ |
| Talk with colleagues, understand workflows, pain points, data | Covestro AI consulting intern; Kniit with SAP domain experts | ✅ |
| Propose where AI makes sense and where not | Kniit deterministic pipeline instead of LLM ($200k → ~0) | ✅ |
| Build/test/deploy LLM apps and agents, prototype → production | LangGraph agents (Kniit, Covestro), AWS CDK deploy, Azure | ✅ |
| RAG, tool integrations, prompts, context handling | RAG/GraphRAG, MCP service, prompt engineering | ✅ |
| Evaluations: test sets, automated checks, quality dashboards | Ground-truth P/R (Kniit), RAGAS/PytrecEval (thesis); dashboards only Streamlit for ML | ✅/🟡 |
| Data pipelines feeding these systems | Kniit ingestion/indexing pipeline; AWS SQS/Lambda eval pipeline | ✅ |
| Python + SWE fundamentals (testing, version control, APIs) | Python, FastAPI, Postman, GitLab CI/CD | ✅ |
| SQL or data pipelines + a cloud (AWS/Azure/GCP) | Postgres/SQL, AWS + Azure | ✅ |
| Work independently, plan, give updates, document | Sole developer reporting to CTO | ✅ |
| Nice: consulting / stakeholder-facing | Covestro AI consulting intern | ✅ |

## Gaps and honest framing
1. **Quality dashboards for LLM evaluations:** not in work history; Agent Eval Harness project (planned) covers it once built.
2. **Sports / media / betting domain:** none; frame as learning from department colleagues.
3. **Fully on-site 5 days in Leipzig:** fine (willing to relocate), stated in letter.

## Projects on the CV
- **Agent Eval Harness** (`planned`, reused; brief applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md). For Sportradar add a small sports-data angle when building: golden set of questions over a mocked match-data API, plus a quality dashboard page. → build-first.
- **Meme Generation using LLMs** (`built`, original link).

## Red flags
- Same JD posted twice (two LinkedIn IDs, different industry tags). Process includes a take-home task.

## Company hooks
1. Sportradar runs a generative AI team (Leipzig among locations) that turns live sports data into match reports, previews and articles with agentic workflows and systematic LLM evaluation (rule-based + human-in-the-loop); stack mentions LangGraph, LangChain, Google ADK ([Sportradar AI Engineer listing](https://anyreality.jobboardly.com/jobs/software-engineer-ai-m-f-d-d966f3fe)).
2. Bundesliga renewed its Sportradar deal adding AI-driven engagement tools ([Inside World Football](https://insideworldfootball.com/?p=131849)).
3. 2025 launches: Live Player Markets (real-time tracking data + AI for in-play betting) and 4Sight Streaming with AI overlays ([Soloazar](https://soloazar.com/en/category/sportsbook/sportradar-and-bundesliga-international-deepen-partnership-with-2025-26-product-launch)).
