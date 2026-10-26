# Fit report: Rohde & Schwarz, AI / ML Engineer - Agentic AI (m/w/d), Dresden

**Fit score: 74/100.** Very close match on the technical core (agent architectures, RAG, vector search, tool calling, MCP, LiteLLM/LangChain/Hugging Face, evaluation pipelines). Main gaps: "sehr gute Deutschkenntnisse" (you have B1), limited production MLOps/monitoring and no formal safety / responsible-AI evaluation work.

Language: German posting that requires very good German → German Lebenslauf + Anschreiben (CLAUDE.md rule 3), German B1 flagged as top gap.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Agent architectures, model harnesses, prompt strategies, context management | Kniit multi-agent LangGraph extraction (4 agents in parallel + reflection), prompt engineering, chunking; Covestro agentic router | ✅ |
| RAG, vector search, multi-step orchestration, tool calling, MCP | Covestro RAG pipelines + agentic app; Kniit MCP knowledge-graph service, GraphRAG | ✅ |
| Evaluate generative behaviour, hallucinations, safety; monitoring + countermeasures | RAGAS/PytrecEval thesis (faithfulness/grounding against ground truth); Kniit P/R 33/45 → 93/90 incl. reflection agent. No formal safety/red-teaming | 🟡 |
| Reproducible evaluation pipelines, metric-driven experiments | Automated RAG eval on AWS (Lambda/SQS/DynamoDB, CDK); embedding benchmark on 1M+ chunks | ✅ |
| MLOps + software engineering to production | Docker, Kubernetes, AWS CDK, GitLab CI/CD, Azure; no model registry/monitoring stack | 🟡 |
| Mehrjährige ML experience incl. foundation models in production | 3 years (Kniit, Covestro x3, Cognizant); agents + RAG in production at Kniit | ✅ |
| Python, model APIs, Hugging Face, LiteLLM, LangChain | All in daily use | ✅ |
| Evaluation methods: automated tests, metrics, tracing | Metrics yes; tracing tools (Langfuse/Phoenix/OTel) not used → project | 🟡 |
| Privacy, safety, responsible-AI assessment | Not done formally | ❌ |
| Sehr gute Deutsch- und Englischkenntnisse | English business fluent; **German B1** | ❌ (top gap) |

## Gaps and honest framing
1. **German (top gap):** state B1 plainly, say you're improving it; technical work in English.
2. **Safety / responsible AI / tracing:** do not claim. Planned project Agent Eval Harness (reused) covers hallucination checks, prompt-injection tests, tracing with OpenTelemetry.
3. **MLOps monitoring:** frame CI/CD + Docker/K8s + AWS CDK; say monitoring is the next step.

## Project on the CV
Reused planned project **Agent Eval Harness** (Jobgether/CGI) with an R&S variant brief (`project-brief-agent-eval-harness.md`). Status planned → **build-first**.

## Red flags
- "Mehrjährige" ML experience with foundation models in production: 3 years is within range.
- Large company in test & measurement / defence-adjacent sectors; may require security clearance for some projects (not stated).

## Company hooks (research 2026-10-26)
1. July 2026: R&S and China Mobile Research Institute showed a testbed (CMX500) that measures the end-user experience of generative AI apps under different network conditions, at MWC Shanghai. ([R&S press / pressebox](https://www.pressebox.de/pressemitteilung/rohde-schwarz-gmbh-co-kg/Rohde-Schwarz-and-China-Mobile-Research-Institute-jointly-demonstrate-generative-ai-user-experience-testing/boxid/1304475), [electronics360](https://electronics360.globalspec.com/article/23997/rohde-schwarz-and-china-mobile-research-institute-jointly-demonstrate-generative-ai-user-experience-testing))
2. R&S states it researches and develops AI and already uses AI widely in its solutions. ([R&S AI page](https://www.rohde-schwarz.com/us/_256990.html))
3. Dresden has an AI/ML software team (earlier posting "Software Developer for AI/ML Functionality", Dresden). ([R&S jobs](https://jobs.rohde-schwarz.com/en_US/careers/JobDetail/Software-Developer-for-AI-ML-Functionality/15306))
4. From the JD: 15,000+ employees; Test & Measurement, Technology Systems, Networks & Cybersecurity; the role evaluates foundation models and agentic AI "für die Plattform".
