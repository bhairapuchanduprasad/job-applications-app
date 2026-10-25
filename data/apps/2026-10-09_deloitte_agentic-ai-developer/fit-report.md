# Fit report: Deloitte aiStudio, Agentic AI Developer (m/w/d)

**Fit score: 62 / 100.** Technically a very strong match (LangGraph multi-agent systems, MCP, Claude Code, AWS + Azure, GitLab CI/CD, full lifecycle as sole developer). The hard blocker is "Deutsch sehr gut in Wort und Schrift": you are B1. Technical fit alone would be ~82.

## Requirements → evidence
| JD requirement | Evidence | |
|---|---|---|
| Abschluss Informatik o. ä. | MSc Artificial Intelligence (THWS) + Minor CS | ✅ |
| Software mit eingebetteten KI-Agenten | Kniit: LangGraph multi-agent extraction (P/R 33/45% → 93/90%); Covestro: agentic LangGraph app deployed to AWS | ✅ |
| Gesamter Entwicklungszyklus (Anforderung → Architektur → Dev → Testing → Betrieb) | Kniit: sole owner of pipeline end-to-end, reporting to CTO; Covestro: built, containerised and deployed full stack | ✅ |
| Machine Learning, Generative AI, agentische KI | RF/XGBoost/LSTM (Covestro, Cognizant), RAG + RAG evaluation, multi-agent systems | ✅ |
| LangGraph | Kniit + Covestro | ✅ |
| Harnesses: MCP | Built MCP query service over knowledge graph, integrated into Claude Code | ✅ |
| Harnesses: APIs | FastAPI backends, Postman | ✅ |
| AWS, Azure | AWS CDK, Lambda, SQS, DynamoDB, EC2; Azure deployment (Expert Interface), Azure AI Search | ✅ |
| KI-Coding-Assistenten (Claude Code) | Daily Claude Code use, custom skills, agentic coding workflows | ✅ |
| GitLab, CI/CD | GitLab + GitLab CI/CD at Covestro | ✅ |
| Python | Primary language, all roles | ✅ |
| JavaScript | React frontends (Covestro, Kniit Expert Interface); CV lists React as "beginner" | 🟡 |
| Kunden- und Teamorientierung | Worked directly with SAP domain experts (Kniit) and chemists (Covestro) | 🟡 |
| Strands (or comparable SDK) | LangGraph counts as "vergleichbar"; no Strands experience | 🟡 |
| A2A | none | ❌ |
| RBAC, InfoSec | none in profile | ❌ |
| Trace-Router / tracing | none in profile | ❌ |
| Cursor, AWS Kiro, Azure DevOps | none (Claude Code + GitLab cover the categories) | ❌ |
| Deutsch sehr gut | B1 | ❌ (blocker) |
| Englisch sehr gut | Business fluent | ✅ |

## Gaps and honest framing
- **German (B1):** don't hide it; the CV states B1. The aiStudio builds technical products, and Deloitte offers "EU Remote Working" and international teams, so an English-first developer may still be considered, but expect rejection at screening for client-facing work. If you are actively taking a German course, say so (TODO: are you?).
- **Strands, A2A, RBAC, tracing:** covered by the tailored project below (build before submitting). After building it these become real, defensible skills.
- **JavaScript:** real React work exists; describe it as React/JavaScript frontends, no level claim beyond that.
- **Cursor / Kiro / Azure DevOps:** leave out. Claude Code + GitLab already prove the category.

## Red flags
- Language requirement is explicit; client-facing consulting at Deloitte Germany usually runs in German.
- Posting is broad ("starte deine Karriere nach deinem … Abschluss"), so the level may be junior/mid. Salary could land below your €60–75k target; ask early.
- Reposted, 100+ applicants: apply quickly.
- No cover letter required; a short one is included as optional.

## Company hooks (sources)
1. **The aiStudio stack matches AWS's agentic toolchain.** The JD names Strands, Kiro, MCP and A2A. AWS positions Kiro (spec-driven agentic IDE) + Strands Agents (open-source, supports MCP and A2A) + Bedrock AgentCore as one workflow. Your MCP and LangGraph work is the closest equivalent. ([AWS startups event](https://aws.amazon.com/startups/events/the-next-ai-wave-aws-bedrock-agentcore-kiro-and-strands-agents), [CloudThat](https://www.cloudthat.com/resources/blog/creating-scalable-ai-workflows-with-amazon-agentcore-and-amazon-bedrock))
2. **Deloitte is investing heavily in agentic transformation.** At Google Cloud Next '26 (April 2026), Deloitte committed to 100,000 Gemini Enterprise licences and set up a dedicated agentic transformation practice; it opened a London AI Studio with Google Cloud in 2026. ([ChannelWeb](https://www.channelweb.co.uk/news/2026/deloitte-google-cloud-london-ai-hub), [TechMarketView](https://www.techmarketview.com/ukhotviews/archive/2026/06/18/deloitte-launches-london-ai-studio))
3. **"Agentic AI is outpacing governance."** Deloitte's 2026 State of AI in the Enterprise report (3,235 leaders, 24 countries): AI access is high but few organisations reach transformation. This fits the JD's emphasis on RBAC/InfoSec and "sicher, skalierbar". ([Deloitte AI Fest](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/collections/global-ai-fest.html))
4. **Business & Technology Center domains** (from the JD): compliance, Datenschutz, Vertragsmanagement, Projektrisiken. Your Kniit work extracting knowledge from regulatory and technical documents for the energy sector maps directly.
- No public information found on the German aiStudio team or its lead.
