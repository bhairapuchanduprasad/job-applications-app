# Fit report: maorika / nedura, AI Automation & Infrastructure Specialist (m/w/d), Hamburg

Source: https://www.linkedin.com/jobs/view/4486402654 (found by job-scout 2026-11-03)
Language: German posting, no German language requirement stated → English CV + short cover letter (CLAUDE.md rule 3). Small German D2C team; German B1 mentioned openly.
Application: "Kein Anschreiben. Zeig uns, was du gebaut hast: GitHub, eine Demo oder ein kurzes Video" + which process to automate first, via Typeform. The cover letter here is optional; reuse its text for the Typeform answers.
Seniority: Entry level. Good.

## Fit score: 66 / 100
"Claude Code is your most important tool", agents for every manual process, APIs/webhooks/data flows, internal tools and dashboards: Kniit (Claude Code + custom skills + MCP into Claude Code, agentic pipelines, React/Python internal tool for experts, Streamlit dashboards) fits the working style well. Gaps: Shopify/Amazon/Klaviyo/Gorgias/DATEV integrations, e-commerce, taking over a self-built ERP, Claude Design, nothing public on GitHub that shows recent agent work.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Lives AI, tests new models | LiteLLM, Claude Code daily workflows, QLoRA | ✅ |
| Claude Code main tool; Claude Design for UIs | Claude Code + custom skills ✅; Claude Design ❌ | ✅ / ❌ |
| Vibe-code prototypes, know when to clean up | AI-augmented engineering + clean code; deterministic rewrite at Kniit | ✅ |
| AI-first: agent before manual work | LangGraph agents; Covestro agentic workflow for stakeholders | ✅ |
| APIs, webhooks, data flows | FastAPI, MCP, Python microservices, AWS SQS/Lambda | ✅ / 🟡 (webhooks) |
| Processes that run unattended | deployed pipelines (AWS CDK, Azure) | ✅ |
| Own ERP as base; Shopify/Amazon/Klaviyo/Gorgias/DATEV | none | ❌ |
| E-commerce (plus) | none | ❌ |

## Gaps and honest framing
1. E-commerce stack integrations: none; planned Shop Support Agent (Shopify Admin API + MCP) covers part.
2. Show what you built: the four public GitHub repos are older notebooks; build the Shop Support Agent and link it in the Typeform (repo exists only after building).

## Red flags
Entry level + "fair salary" (no number). Whole infrastructure ownership in a small team. Typeform asks for a first process to automate: suggest customer-service ticket triage (Gorgias) with order lookups (Shopify) and human approval.

## Company hooks
1. maorika sells New Zealand Manuka honey graded by MGO (100+ to 1000+), lab-tested, jarred in Germany; sold via its own shop and marketplaces like Shop Apotheke ([Shop Apotheke listing](https://www.shop-apotheke.com/ernaehrung/upmHA9ZU3/maorika-manuka-honig-mgo-550.htm)).
2. Posting: maorika + nedura (bee cosmetics, premium supplements, own production); revenue more than doubled in 2026; rebuilding the company AI-first; office at Gorch-Fock-Wall, Hamburg.

## Project
Shop Support Agent (existing planned project; brief applications/2026-10-16_snocks_junior-ai-engineer/_work/project-brief-shop-support-agent.md). Variant note: add a Gorgias-style ticket inbox mock and a DATEV-style export step if building for this application.
