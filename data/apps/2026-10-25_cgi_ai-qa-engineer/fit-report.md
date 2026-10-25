# Fit report: CGI, AI QA Engineer – Conversational AI & GenAI-Automationen (m/w/d), Eschborn

**Fit score: 58/100.** Strong on the AI-specific half of the job (systematic LLM/RAG evaluation against ground truth, RAGAS + PytrecEval in the thesis, precision/recall as quality metrics at Kniit, RAG, tool calling via MCP, Python, API tests with Postman, GitLab CI/CD). Weak on the classic QA half (no QA/test-management role, no Selenium, no ISTQB, no voice/RPA testing, no security testing) and the language: the posting asks for very good German, I have B1.

Language: German posting that requires "Deutsch sehr gut" → German CV (Lebenslauf) + Anschreiben (CLAUDE.md rule 3). Prepared anyway at the user's decision.

Source: https://www.linkedin.com/jobs/view/4447592166 · LinkedIn level: Entry level (but the text asks for "mehrjährige Erfahrung" in QA/test automation).

## Requirements → evidence
| Requirement | Evidence | Rating |
|---|---|---|
| **Deutsch sehr gut**, Englisch gut | German B1 (no certificate); English business fluent | ❌ **top gap** |
| KI-spezifische Qualitätsmerkmale, Testverfahren | Thesis: automated RAG evaluation (generation + retrieval) with RAGAS and PytrecEval vs. chemist ground truth; Kniit: multi-agent system measured against SAP-derived ground truth, precision/recall 33/45 → 93/90 | ✅ |
| GenAI specifics: Prompting, RAG, Tool Calling, Guardrails/Evaluation | Prompt engineering, RAG/GraphRAG pipelines, MCP server exposing tools to agents, evaluation frameworks; guardrails not in profile | ✅ / 🟡 (guardrails) |
| AI Test Harness, Golden Datasets, automated regression, quality metrics | Ground-truth datasets + quality metrics (thesis, Kniit); no formal regression suite in work history → Agent Eval Harness project (planned) | 🟡 |
| Teststrategie (Testpyramide, Quality Gates, Releasekriterien) | Expert approval step before knowledge-graph changes (Expert Interface) is a human quality gate; no formal test strategy ownership | 🟡 |
| Testautomation (Selenium, API-Tests), Script Coding (Python/JS/Java) | Python (main language since 2021); API testing with Postman; React (beginner); no Selenium, no Java | 🟡 (Selenium ❌) |
| Security & Robustness (Prompt Injection, Data Leakage, Rollen-/Rechtekonzepte) | Not in work history → covered only by the planned project | ❌ |
| Voice tests (Robustheit, Latenz, Handover), E2E over GenAI/Workflow/RPA | Latency: millisecond-latency MCP retrieval; no voice, RPA or workflow-engine testing | ❌ |
| CI/CD integration, Monitoring/Betrieb | GitLab CI/CD, Docker, AWS CDK, Kubernetes, Azure; evaluation not yet wired into CI at work | 🟡 |
| Mehrjährige QA/Testmanagement-Erfahrung, agile + klassisch | 3 years AI engineering with evaluation at the core, Agile; no dedicated QA role | 🟡 |
| Zusammenarbeit mit Engineering, Architektur, Fachbereichen | CTO + SAP domain experts (Kniit); business stakeholders as AI consulting intern (Covestro); chemists (thesis) | ✅ |
| Nice to have: ISTQB TTA/TAE, Workflow/RPA/Cloud Testing | No ISTQB; cloud: AWS/Azure deployments, evaluation infra on AWS (Lambda, SQS, DynamoDB) | ❌ / 🟡 |

## Gaps and honest framing
1. **German (sehr gut required, B1 held).** Biggest risk; CGI works "direkt beim Kunden" in German. State B1 honestly in CV and letter; do not claim more. Interview: be ready to hold part of the conversation in German.
2. **Classic QA tooling and title.** No Selenium, no ISTQB, no QA job title. Frame the evaluation work as quality engineering for AI (which is what the role describes), name Postman API tests and GitLab CI/CD; ISTQB CTFL/TAE could be a near-term certification (do not claim it).
3. **Security/robustness testing (prompt injection, data leakage, roles/permissions).** Not done at work. Covered by the planned Agent Eval Harness project (must be built before submitting); in the interview, describe it only once it exists.
4. **Voice, RPA and workflow-engine testing.** None. Leave out; mention latency measurement and human handoff only where true.

## Red flags
- "Entry level" on LinkedIn vs. "mehrjährige Erfahrung" in the text: likely flexible on years, not on German.
- CGI places consultants at client sites ("Kundennähe"); German client communication is daily work.

## Company hooks (sources)
1. CGI is a strategic agentic-AI partner of Cognigy (conversational AI platform); Niklas Bläsing, Head of Data & AI at CGI Germany, describes support since Cognigy's founding year. A German aviation client's chat assistant built with CGI and Cognigy handles automated flight rebooking during disruptions, with agent-based features and persona-based responses added by CGI's team. Source: https://www.cognigy.com/blog/shaping-the-future-of-ai-service-how-cgi-and-cognigy-deliver-real-world-results-with-agentic-ai
2. CGI has a "Responsible Use of AI Framework" and an AI Strategy Framework (TBR analysis on CGI Germany's site), and a "Customer Zero" approach: GenAI use cases are tested internally before offering them to clients. Source: https://www.cgi.com/de/de/article/kuenstliche-intelligenz/tbr-analysiert-cgi-kompetenz-generative-ki
3. TBR notes clients struggle to move GenAI beyond PoCs/pilots (data, change management, ROI): fits the posting's "Produktionsreife mit klaren Qualitätsmetriken". Same source.
4. Posting: CGI is building a new team for large Conversational/GenAI programmes; regulatory requirements are built in from design onward. Source: job.md.

## Tailoring decisions
- Tagline "AI Engineer" (closest to "AI QA Engineer"); header location "Eschborn • Blaue Karte EU".
- Projects: reuse planned **Agent Eval Harness** (profile), adapted for this JD: a customer-service chatbot agent with golden conversations, quality gates in CI, prompt-injection, data-leakage and role/permission tests, human handover checks. Brief: `_work/project-brief-agent-eval-harness.md`. Status **build-first**.
- No extra "Confirmed hands-on" bullets: the only confirmed topic (LLM fine-tuning) is not a JD topic.
