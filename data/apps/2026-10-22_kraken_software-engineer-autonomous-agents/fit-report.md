# Fit report: Kraken, Software Engineer (Autonomous Agents), Berlin

**Fit score: 82 / 100.** Rare match on domain and stack: you built AI agents for the German energy sector (Kniit), an MCP server that gives agents fast access to a knowledge graph, evaluation of non-deterministic output against ground truth (P/R 33%/45% → 93%/90%, RAGAS), a domain-expert approval tool (human-in-the-loop), and you worked with stakeholders on their workflows (Covestro AI consulting internship). Gaps: TypeScript (required), customer-service/conversational AI, feature toggles, observability tools (Datadog/Sentry), Django.

Language: English posting → English documents.

## Requirements → evidence
| JD requirement | Evidence | |
|---|---|---|
| Shipped and supported production software; testing, code review | Kniit sole developer (pipeline + Expert Interface on Azure); Covestro app deployed to AWS with Docker/CDK/GitLab CI/CD; API testing with Postman | ✅ / 🟡 (no code-review evidence) |
| Python | Primary | ✅ |
| TypeScript | none (React beginner) | ❌ → project |
| LLMs, autonomous agents, MCP | LangGraph multi-agent (Kniit, Covestro); MCP service integrated into Claude Code | ✅ |
| Authentication, permissions, validation, human handoff | Expert Interface: experts approve changes before use of graph changes; no auth/permissions work documented | 🟡 → project |
| Test and monitor non-deterministic behaviour (evals) | P/R vs SAP ground truth; RAGAS/PytrecEval; reflection agent | ✅ |
| Feature toggles, gradual rollout | none | ❌ → project |
| Dashboards, monitoring, runbooks | Streamlit dashboard (Covestro); no production monitoring | 🟡 |
| Translate regulatory/business processes into plans; talk to non-engineers | Regulatory and technical documents in the energy sector with SAP experts; consulting internship with business stakeholders | ✅ |
| Energy domain | Kniit: German energy sector | ✅ |
| Bonus: conversational AI / customer service | none | ❌ → project |
| Bonus: Django, Datadog, Sentry | FastAPI instead; none of these | ❌ |
| Right to work in Germany | EU Blue Card | ✅ (see note) |

## Gaps and honest framing
- **TypeScript:** the agent side is TypeScript. Covered by the tailored project; say you're productive in Python and picking up TypeScript.
- **Customer service / conversational AI, feature toggles, observability:** covered by the project.
- **Django:** you've built REST APIs with FastAPI; Django concepts transfer.

## Red flags
- "No visa sponsorship; right to work required at time of application." Your EU Blue Card gives you the right to work in Germany; when you change employer you must inform the Ausländerbehörde, and the new job must meet the Blue Card conditions (salary threshold). You don't need sponsorship. Say "EU Blue Card holder, no sponsorship needed" in the form.
- 15 applicants in 4 hours: apply soon.

## Company hooks (sources)
1. **Independent since the Octopus spin-out:** Octopus announced in Sept 2025 it would separate Kraken into an independent company ([Business Wire](https://www.businesswire.com/news/home/20250918156123/en)); a reported $1B round values it at $8.65B ([Techleap](https://finder.techleap.nl/news/note/kraken-spins-out-of-octopus-group-at-8-65bn-valuation-and-raises-1bn)).
2. **Scale:** contracted to serve 70M+ household and business accounts; clients include EDF, E.ON Next, National Grid US, Origin Energy, Plenitude and Tokyo Gas ([Wikipedia](https://en.wikipedia.org/wiki/Kraken_Technologies)). Reusable agents across many utilities is exactly the "client-agnostic" goal in the JD.
3. **Magic Ink:** existing AI tool that summarises customer interactions, drafts responses and suggests actions like requesting a meter reading ([Energy Digital](https://energydigital.com/news/how-krakens-ai-technology-is-revolutionising-good-energy)); Autonomous Agents takes this from suggestions to agents that act.
