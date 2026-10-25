# Fit report: BaehrBots GmbH, AI Integration Engineer / Specialist, Dresden

**Fit score: 63/100.** The technical core is a close match: LLM APIs, agents with tools, MCP, RAG, evals against ground truth, cost control and Python, all from the Kniit and Covestro work, plus energy-sector context. It is pulled down by the German requirement ("Sehr gute ... Deutschkenntnisse", I have B1) and by missing hands-on evidence for Linux server operations (systemd), SaaS integrations (Slack, Google Workspace, GitHub APIs, webhooks, OAuth) and secrets/DSGVO handling.

Language: posting in German and it requires very good German → German Lebenslauf + Anschreiben (CLAUDE.md rule 3). User decision: prepare anyway despite B1.

Source: https://www.linkedin.com/jobs/view/4481080810. Full-time, Dresden office (no remote mentioned). No contact person, no deadline, no salary range. Cover letter optional ("kein Muss, hilft uns aber sehr"); work samples (an agent or automation you built) welcome.

## Requirements → evidence
| Requirement (JD) | My evidence | Rating |
|---|---|---|
| **Sehr gute Deutschkenntnisse** | German B1, no certificate | ❌ **top gap** |
| Sehr gute Englischkenntnisse | Business fluent | ✅ |
| Studium Informatik / Data Science o. ä. | MSc Artificial Intelligence (THWS) + Minor CS | ✅ |
| Sehr gute Python-Kenntnisse | Python in every role since 2021; FastAPI, microservices | ✅ |
| LLM-APIs: Prompting, Tool Use/Function Calling, strukturierte Ausgaben, Kostenkontrolle | LiteLLM over LLM APIs, prompt engineering (Kniit); agents routing to tools (Covestro); MCP tools for Claude Code; deterministic pipeline cut a $200k projected LLM budget to near zero (cost control). Structured outputs not named in the profile | 🟡→✅ |
| Betrieb von Diensten auf Linux-Servern (systemd, Docker, Logs) | Docker, Kubernetes, Azure, AWS; Linux/systemd not in profile | 🟡 |
| Git/GitHub im Pull-Request-Workflow | Git + GitLab with CI/CD; GitHub account; PR workflow not explicitly in profile | 🟡 |
| API-Integrationen (REST, Webhooks, OAuth) in Slack, Google Workspace, GitHub | REST APIs with FastAPI, API tests with Postman; no Slack/Google Workspace/GitHub API, webhook or OAuth work in the profile | ❌ (planned project covers Slack/webhooks/OAuth/GitHub) |
| Sorgfalt bei Daten und Zugriffsrechten (Least Privilege, Secrets, DSGVO) | Expert approval step before knowledge-graph changes; nothing explicit on secrets/DSGVO | 🟡/❌ |
| Ehrlichkeit: LLMs halluzinieren, Prüfungen einbauen | Reflection agent + evaluation against SAP-derived ground truth (33/45 → 93/90 P/R); RAGAS/PytrecEval vs chemist ground truth | ✅ strong |
| Agenten betreiben, verbessern, mit Werkzeugen/Datenquellen verbinden | LangGraph multi-agent system (Kniit), routing agent (Covestro), MCP service | ✅ |
| Neue Automationen: erst hinterfragen und vereinfachen | Replaced LLM extraction with a deterministic pipeline where code was enough | ✅ |
| Wissensbasis (Git, Suche, RAG) | RAG, GraphRAG, vector search, knowledge graph (Neo4j), RAG thesis | ✅ |
| Monitoring, Evals, ehrliche Kennzahlen | Evals strong; monitoring/observability tooling not in profile | 🟡 |
| Team informieren, Kollegen befähigen | Worked with SAP experts and business stakeholders; Covestro AI consulting | 🟡 |
| Plus: Agent-Frameworks/SDKs | LangGraph (Claude Agent SDK, CrewAI not used) | ✅ |
| Plus: MCP, RAG, Suchsysteme | MCP service, RAG, GraphRAG, Azure AI Search | ✅ |
| Plus: Evals und Observability | Evals ✅, observability ❌ | 🟡 |
| Plus: Finanz/Backoffice, Energiehandel | German energy sector at Kniit (not trading) | 🟡 |

## Gaps and honest framing
1. **German (top gap).** B1 vs "sehr gut". Say it plainly in the letter (B1, improving), stress the international team and that English works for the technical stack; offer to use their language-course budget. Do not overstate.
2. **Linux server ops (systemd, logs).** Docker/Kubernetes deployments are adjacent; the Ops MCP Server project (BaehrBots variant) runs under Docker + systemd on a Linux server. Not claimed in experience.
3. **SaaS integrations (Slack, Google Workspace, GitHub, webhooks, OAuth).** REST/FastAPI experience is adjacent; the planned project covers Slack signed webhooks, OAuth and a GitHub tool. Google Workspace stays a gap.
4. **Secrets, least privilege, DSGVO.** Not in profile; project covers role checks and env-only secrets. Interview: talk about the human approval step in Expert Interface.
5. **Monitoring/observability, structured outputs, GitHub PR workflow.** Not named in profile; leave out of experience.
6. Confirmed hands-on list (LLM fine-tuning) does not match a JD topic, so no extra Kniit/Covestro bullets were added.

## Red flags
- Small, young company (founded 2024 per registry data); verify team size, salary vs Blue Card threshold, and who maintains the agents today.
- "Dein Erfolg misst sich an den Stunden, die du dem Team zurückgibst": expect measurable targets; good fit with the eval background.
- German is listed as a must; a B1 candidate may be filtered early.

## Company hooks (sources)
1. Energy trading start-up from Dresden, direct member of EPEX SPOT, trades power with its own Algotrader and builds its own battery storage projects. Source: posting; https://www.arbeitnow.com/jobs/companies/baehrbots-gmbh/stromhandler-power-trader-dresden-131029
2. Runs its own agents on its own servers: Moneypenny (reception/coordination), Rockefeller (finance), Columbo (independent quality control); mission "Autonomiestufe 5 ... Gemessen, nicht behauptet". Source: posting.
3. Founded 2024 in Dresden, managing director Sascha Michael Bähr (registry data, not verified against official register). Source: https://app.implisense.com/en/companies/baehrbots-gmbh-dresden--DE4V3RO1RP09
4. Another posting mentions integrating the EPEX M7 API for automated market communication and order handling. Source: https://join.com/companies/baehrbots/16249523-stromhaendler-energy-trader-mit-algo-trading-expertise-gn (search snippet; page now gone)
5. Values from posting: "Build, don't just use", "Erst hinterfragen und vereinfachen, dann automatisieren", honest metrics ("Ein grüner Haken zählt nur, wenn das Ergebnis wirklich da ist").

## Project on the CV
- Ops MCP Server (existing `planned` project, reused with a BaehrBots variant: GitHub tool + self-hosted Linux deployment with Docker and systemd). Brief: `_work/project-brief-ops-mcp-server.md`. Status: build first. It also makes a good work sample, which the posting explicitly welcomes.
