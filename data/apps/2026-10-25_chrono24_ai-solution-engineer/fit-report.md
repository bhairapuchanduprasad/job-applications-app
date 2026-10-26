# Fit report: Chrono24, AI Solution Engineer (m/f/d), Karlsruhe (hybrid)

**Fit score: 60/100.** Strong match on the work itself: building LLM-powered automations and POCs with existing models, prompt engineering in real use cases, APIs/HTTP/JSON and MCP, and sitting with business stakeholders to find where AI helps (Covestro AI consulting internship). Two real gaps hold the score down: the posting asks for **a minimum of 5 years** of relevant experience (I have 3, including internships and thesis) and **very good German** (I have B1, no certificate).

Language: posting in English → English CV and cover letter (CLAUDE.md rule 3). German is the top gap (see below).

Source: https://www.linkedin.com/jobs/view/4446902091 (found by the job scout 2026-10-25).

## Requirements → evidence
| Requirement | Evidence | Rating |
|---|---|---|
| Very good German and English | English business fluent; German B1, no certificate | ❌ German (top gap) |
| Minimum 5 years relevant professional experience | 3 years (Kniit, Covestro intern/thesis/intern, Cognizant) | ❌ |
| Business + technical blend; CS / information systems background | MSc AI; Covestro AI Consulting Intern: worked with business stakeholders on their decision workflows, advised where agentic AI helps, translated requirements into a solution | 🟡 (no commercial departments like Marketing/Finance) |
| Build working MVPs yourself, wiring tools, LLMs and integrations | Sole developer at Kniit; Covestro agentic app (LangGraph + FastAPI + React) built and deployed; Expert Interface web app | ✅ |
| Hands-on LLMs and prompt engineering in real use cases (Claude, GPT or similar) | Prompt engineering + multi-agent LangGraph extraction at Kniit (33/45 → 93/90 P/R); LiteLLM over LLM APIs; Claude Code daily | ✅ |
| APIs, HTTP/JSON, ideally MCP | FastAPI services, Postman API testing, Python microservices; MCP query service integrated into Claude Code | ✅ |
| Judge what data/access a use case needs | Kniit: worked with SAP experts on which source data feeds the knowledge graph; chose deterministic code over LLM for a high-volume stream (cut $200k projected LLM budget) | ✅ |
| Know when to hand off to ML / IT | Experience on both sides (built ML models, deployed infra), so can judge when a POC needs production engineering | 🟡 |
| Enable teams to help themselves | Expert Interface lets domain experts validate/approve graph changes themselves; Streamlit dashboard for chemists | 🟡 |
| Ownership: scope and ship a first version without tickets | Sole developer reporting to the CTO at a start-up | ✅ |

## Gaps and honest framing
- **German (very good required):** B1. Say it plainly in the letter (B1, actively improving) and that English is business fluent; the company is international (80+ countries). Expect this to be the main screen-out risk.
- **5 years minimum:** 3 years. Don't stretch dates. Lean on end-to-end ownership as sole developer and on the consulting internship. The role is explicitly "practical, not production-grade" MVPs, which plays to fast building.
- **Commercial departments (Growth, Marketing, Finance, People & Culture):** no direct experience with those teams. Stakeholder work so far was chemists, R&D/business stakeholders at Covestro and SAP domain experts. Don't claim marketing/finance automations.
- **No-code / iPaaS tools (Zapier, n8n, Make):** not in the JD by name, not in profile; the planned Ops MCP Server project covers tool wiring with Slack/HubSpot/Notion.

## Red flags
- "Minimum of 5 years" + "very good German": two hard-sounding filters. Apply anyway if you like the role, but expectations should be moderate.
- Role is deliberately non-production (POCs, handover to ML team); fine for this profile.

## Company hooks (sources)
1. Chrono24 is the leading online marketplace for luxury watches, HQ in Karlsruhe, buyers and sellers from 80+ countries (posting); around 540,000 watches listed by 3,000 dealers and 45,000 private sellers in 120+ countries (JCK: https://www.jckonline.com/?p=215622).
2. Watch Scanner in the Chrono24 app identifies a watch from a smartphone photo and gives brand, model and price estimate; built by a small team of developers and data scientists, trained on about 1 million images selected from 6.5 million listings (WatchPro: https://usa.watchpro.com/?p=50467).
3. The role sits on a platform the Tool Enablement team provides and hands scaled use cases to the ML team; the posting names MCP as the preferred way to expose internal systems (posting).
4. CEO Carsten Keller since January 2024 (JCK, same article). Not used in the letter.

## Project (CV Projects section)
Reuse the planned **Ops MCP Server** (Cloover brief, BaehrBots variant): MCP server giving Claude and a Slack bot typed, role-checked tools over HubSpot, GitHub and Notion SOPs. It shows exactly the JD's "connect existing tools and LLMs into working workflows" and "via APIs and, ideally, MCP". Status: planned → application is **build-first**. Variant notes for this JD in `project-brief-ops-mcp-server.md`.
