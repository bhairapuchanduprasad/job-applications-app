# Fit report: SAP SE, AI Engineer – Development Expert (f/m/d)

**Fit score: 45 / 100.** Domain and AI fit are unusually good, seniority is not. You built an agentic pipeline for the German energy sector with SAP domain experts, use agentic AI daily with Claude Code, and have real cost/accuracy results. But this is a senior architect and team-lead role (T4, "several years of software architecture", "lead and mentor development teams", €94–172k), and your ~3 years include an internship, a master's thesis, and no people leadership.

Language: English posting, English required → English documents.

## Requirements → evidence
| JD requirement | Evidence | |
|---|---|---|
| Several years in software architecture and development | ~3 years incl. internships/thesis; sole developer and architect of the Kniit pipeline | 🟡 |
| Utilities / energy industry | Kniit: knowledge-extraction pipeline for the German energy sector with SAP domain experts | ✅ |
| Message exchange, smart meter gateway integration, metering concepts, regulation | Regulatory and technical documents processed at Kniit; no MaKo/EDIFACT/SMGW work | ❌ |
| Agentic AI, agentic orchestration | LangGraph multi-agent (parallel extraction + reflection agents), Covestro agentic router | ✅ |
| SAP Business AI | Worked against SAP-system ground truth with SAP experts; no SAP BTP / Joule / AI Core | ❌ |
| Semantic retrieval | RAG, GraphRAG, vector search, embedding benchmark on 1M+ chunks, MCP retrieval in ms | ✅ |
| Cloud-native architecture | AWS (CDK, Lambda, SQS, DynamoDB), Azure, Docker, Kubernetes | 🟡 (built, not "architect" title) |
| Optimize high-throughput systems for performance and cost | Deterministic pipeline for the high-volume stream: $200k projected LLM spend → near zero; ms-latency retrieval | ✅ |
| Governance, security, compliance, data privacy | Not documented | ❌ |
| Lead and mentor teams, architectural governance | Sole developer; reported to CTO; no team lead | ❌ |
| Customer engagement on technical requirements | Worked directly with SAP domain experts and chemists | 🟡 |
| AI in daily engineering, AI output QA, context engineering | Claude Code with custom skills; P/R 33%/45% → 93%/90% vs ground truth; RAGAS/PytrecEval | ✅ |
| Excellent English | Business fluent | ✅ |

## Gaps
- Seniority and team leadership: not fixable by a project. This is the main reason for the score.
- SAP Business AI (BTP, AI Core, Joule) and energy market communication (MaKo, smart meter gateway): learnable, and a project could show both.
- Governance/security/compliance: not documented.

## Red flags
- Career level T4 "Development Expert" usually means 8+ years. Expect an automatic screen-out on years.
- 8 applicants in 1 hour.

## Company hooks (sources)
1. **Joule for utilities:** SAP positions Joule as a "process-aware copilot" across the utilities value chain (smart metering, billing, customer experience, asset management), grounded in the SAP Knowledge Graph and Business Data Cloud. ([ASUG](https://www.asug.com/insights/sap-positions-joule-as-a-process-native-copilot-for-the-utilities-value-chain)) Your Kniit work was a knowledge graph for the energy sector checked against SAP-system data: the strongest hook.
2. **Meter-to-cash agents:** SAP mapped four agents, incl. an Implausible Meter Reading Resolution Agent and a billing document agent planned for Q3 2026; partner exnaton's energy agents (data quality, metering consistency) are available in Joule. ([ASUG](https://www.asug.com/insights/sap-bets-on-ai-agents-to-tame-utilities-most-complex-workflow)) The tailored project targets exactly this.
3. **Agent governance at Sapphire 2026:** AI Agent Hub for SAP and non-SAP agents; Business AI Platform (BTP + Business Data Cloud + AI Foundation); Joule Studio with pro-code and agent governance. ([SAPinsider](https://sapinsider.org/articles/sapphire-2026-your-sap-erp-just-got-an-ai-brain-now-what-seven-questions-every-leader-must-answer/), [WebProNews](https://www.webpronews.com/sap-admits-joule-studio-flop-rushes-2-0-overhaul-with-pro-code-power-and-agent-governance-at-sapphire-2026/))
4. Community note: Joule is mostly human-triggered so far, not an event-driven orchestrator for meter-to-cash events. ([SAP Community](https://community.sap.com/t5/artificial-intelligence-forum/btp-joule-integration/m-p/14434898)) Good interview talking point, not for the letter.
