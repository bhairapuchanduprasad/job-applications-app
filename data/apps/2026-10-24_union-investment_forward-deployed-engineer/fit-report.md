# Fit report: Union Investment, Forward Deployed Engineer (m/w/d) KI-native Entwicklung, Berlin

**Fit score: 76/100.** Very close to your actual work: agentic systems with tool calling and orchestration, MCP servers, RAG, systematic evaluation, agent skills (Claude Code custom skills), working directly with business units and translating requirements. Gaps: Agent SDKs by name, TypeScript, tracing/observability tooling, regulated-finance experience (nice-to-have), and "mehrjährige" operation of production software.

Language: German posting with no stated German requirement → English documents (CLAUDE.md rule 3). Large German financial firm, "mehrheitliche Anwesenheit vor Ort": German will be used with business units; B1 shown honestly.

Source: https://www.linkedin.com/jobs/view/4465867033

## Requirements → evidence
| Requirement | Evidence | Rating |
|---|---|---|
| Several years building/operating modern software + practical LLM/agent experience | 3 years; Kniit multi-agent LangGraph system (sole developer); Covestro agentic app deployed to AWS | 🟡 years / ✅ agents |
| Python, TypeScript or similar; maintainable code | Python everywhere; React frontend; TypeScript not in profile | ✅ / ❌ TS |
| Agent SDKs, Agent Skills, MCP servers, RAG, prompt governance, systematic evaluation | Claude Code custom skills; MCP query service; RAG + RAGAS/PytrecEval; ground-truth evaluation loop (33/45 → 93/90); Agent SDKs not used | ✅ (SDK ❌) |
| Tool calling, orchestration, context and memory management | LangGraph parallel agents with consolidation and reflection; request routing across tools (Covestro) | ✅ |
| LLMOps, automated tests, delivery pipelines, logging, tracing, observability, economical operation | GitLab CI/CD, Docker, AWS CDK; cost decision ($200k budget → near zero via deterministic code); tracing tooling not named | 🟡 |
| Prototyping, experiments, iterative validation | Agentic vs deterministic vs monolithic strategies compared at Kniit; embedding benchmarks | ✅ |
| Integrating LLMs, agents, data sources, enterprise apps end to end | Kniit: documents → knowledge graph → MCP → Claude Code; Expert Interface for SAP experts | ✅ |
| Close work with business units / architects | SAP domain experts, CTO (Kniit); Covestro AI consulting with business stakeholders | ✅ |
| Regulated environments (banking/fintech) helpful | Regulated energy-sector documents; no finance | 🟡 |

## Project
Reuses the planned **Spec-Driven Coding Agent Harness** (already on the opta data and BCG Platinion CVs): agent skills, hooks as guardrails, MCP server, CI/CD with tests and security scanning, evaluation suite, Langfuse tracing. Covers Agent Skills, Leitplanken, systematic evaluation, LLMOps/tracing/observability. Brief: `_work/project-brief-spec-driven-agent-harness.md` (points to the full opta data brief). Must be built before submitting.

## Gaps and honest framing
- **Agent SDKs, TypeScript:** not used; Python + LangGraph instead. Don't claim.
- **Observability/tracing:** say evaluation loops yes, production tracing tooling not yet (project adds Langfuse).
- **Banking:** none; regulated energy-sector documents are the closest analogue.
- **German:** B1, improving; majority on-site in Berlin.

## Red flags
- "Mehrjährige Erfahrung … im Betrieb": may expect more ops experience than 3 years.
- Role is at the Merantix AI Campus, Berlin (stated in the JD); contact: Katharina Beck.

## Company hooks (sources)
1. Asset manager of the cooperative financial group (Volksbanken Raiffeisenbanken); launched an AI-based fund asset management offer ("WertAnlage") with LAIC in December 2024, where AI proposes the allocation from over 125 million data points a day, combined with human advisers. Sources: https://www.it-finanzmagazin.de/union-investment-startet-vermoegensverwaltung-mit-kuenstlicher-intelligenz-219764 , https://www.cash-online.de/a/vermoegensverwaltung-auf-ki-basis-union-investment-und-laiqon-tochter-kooperieren-689114
2. Capital-markets experts see AI as a potential game changer through productivity gains. Source: https://www.boersen-zeitung.de/kapitalmaerkte/union-investment-traut-ki-gewaltiges-potenzial-zu
3. CEO names digitalisation and demographic change as major challenges; processes should be digitised as far as possible. Source: https://www.boersen-zeitung.de/banken-finanzen/union-investment-chef-reinke-sieht-kein-ma-unter-deutschen-top-asset-managern-2
4. From the posting: a KI-native development team with Forward Deployed Architects and KI Reliability & Quality Engineers; reusable components, agent skills and guardrails.
- No public sources found on their agentic AI work specifically.
