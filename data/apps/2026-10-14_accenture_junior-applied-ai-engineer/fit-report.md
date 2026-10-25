# Fit report: Accenture DACH, Junior Applied AI Engineer (all genders)

**Fit score: 74 / 100.** Technically you are above the bar for a junior role: LLM APIs in live pipelines with real cost tradeoffs ($200k budget cut), evaluation of AI output (RAGAS, precision/recall), full stack (React + FastAPI), Docker/CI/CD/AWS/Azure, LangGraph/RAG in production, and Claude Code with custom skills. Main risk: "Very good German" (you are B1). Without that, ~88.

## Requirements → evidence
| JD requirement | Evidence | |
|---|---|---|
| Degree in CS or related | MSc Artificial Intelligence (THWS); BTech Mechanical + Minor in CS | ✅ |
| Commercial software in production | Kniit (sole developer, pipeline + Azure web app), Covestro (deployed on AWS) | ✅ |
| Python / Java / TypeScript | Python (primary) | ✅ |
| AI coding assistants in daily engineering work, with practical examples | Claude Code with custom skills and agentic coding workflows; MCP service integrated into Claude Code | ✅ |
| LLM APIs in production code; tokens, latency, cost tradeoffs | Kniit multi-agent LLM pipeline; deterministic pipeline chosen to cut projected $200k LLM spend; millisecond-latency MCP retrieval | ✅ |
| Validate, evaluate, improve AI outputs | Precision/recall 33%/45% → 93%/90% vs SAP ground truth; RAGAS + PytrecEval automation; reflection agent | ✅ |
| Agentic concepts: LangChain, LangGraph, RAG, full stack ↔ agents | LangGraph multi-agent (Kniit, Covestro), RAG pipelines + evaluation, React/FastAPI front ends to agentic backends | ✅ |
| Cloud, Docker, CI/CD | AWS CDK/Lambda/SQS/DynamoDB/EC2, Azure, Docker, Kubernetes, GitLab CI/CD | ✅ |
| SQL or NoSQL | Postgres, SQL, MongoDB, DynamoDB, Neo4j, vector DBs | ✅ |
| Agile | Agile listed in base CV | ✅ |
| JavaScript, HTML, CSS (basic) | React frontends (Covestro, Kniit); HTML/CSS not named | 🟡 |
| AI-generated tests, AI-assisted debugging/code review | Implied by Claude Code workflow, not explicitly documented | 🟡 |
| KPIs for AI-assisted workflow ROI, presented to stakeholders | You track AI *output* quality (P/R), not AI-*workflow* productivity KPIs | ❌ → project |
| LLM abstraction layer across providers | none explicit | ❌ → project |
| TypeScript | none | ❌ (not required; Python suffices) |
| Very good German | B1 | ❌ (blocker risk) |
| English | Business fluent | ✅ |

## Gaps and honest framing
- **German (B1):** stated on CV and in the letter's logistics line. Accenture has international client teams, but expect this to be the screening risk.
- **AI-workflow KPIs + LLM abstraction layer:** covered by the tailored project "LLM Gateway" (build before submitting).
- **HTML/CSS:** React work implies it; don't claim more.
- **TypeScript:** leave out.

## Red flags
- **Junior level:** with 3 years' experience you may be over-qualified; salary for junior roles at Accenture Germany is likely below your €60–75k target. Ask early; you could also look for the "Applied AI Engineer" / "Forward Deployed Engineer" non-junior variants.
- 100+ applicants in 2 days: apply fast.
- Occasional business travel required.

## Company hooks (sources)
1. **Accenture Anthropic Business Group (Dec 2025):** multi-year partnership; ~30,000 Accenture professionals trained on Claude; Accenture is a premier partner for Claude Code, with tens of thousands of its developers using it, Anthropic's largest Claude Code deployment. ([Anthropic](https://www.anthropic.com/news/anthropic-accenture-partnership), [Business Wire](https://www.businesswire.com/news/home/20251209640751/en/Accenture-and-Anthropic-Launch-Multi-Year-Partnership-to-Drive-Enterprise-AI-Innovation-and-Value-Across-Industries))
2. **Forward Deployed Engineers = "reinvention deployed engineers"** at Accenture, embedding Claude in client environments. The JD's pathway to the FDE program is this. ([Anthropic](https://www.anthropic.com/news/anthropic-accenture-partnership))
3. **Joint CIO offering to measure value of AI adoption in engineering:** matches the JD's "define and track KPIs to evaluate the ROI of AI-assisted workflows". ([Business Wire](https://www.businesswire.com/news/home/20251209640751/en/Accenture-and-Anthropic-Launch-Multi-Year-Partnership-to-Drive-Enterprise-AI-Innovation-and-Value-Across-Industries))
4. **DACH:** Kronberg is hiring heavily for agentic AI roles in 2026; Accenture-linked "Scaling the Agentic Enterprise" summit in Munich, 19 Nov 2026 (event page, not an official press release). ([ZipRecruiter listing](https://www.ziprecruiter.de/jobs/559556403-ai-analytics-advisory-senior-manager-agentic-ai-all-genders-bei-accenture))
