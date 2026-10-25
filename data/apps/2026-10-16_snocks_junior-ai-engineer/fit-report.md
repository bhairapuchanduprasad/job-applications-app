# Fit report: SNOCKS, Junior AI Engineer (m/w/d)

**Fit score: 80 / 100.** Strong match on the core of the job: Python, SQL, REST APIs, Git, LLMs with agents and MCP, Claude Code, AWS + Docker + CI/CD, and measuring AI output on quality and cost. The gaps are on the e-commerce side: no BigQuery or other cloud data warehouse, no Google Cloud, no Shopify/Zendesk/Klaviyo integrations, and no business-process automation (customer service, supply chain, reporting) in your work history. Your German (B1) meets their minimum.

Language: posting is in German and asks for German B1, but the team language is English (C1 required). Documents in **English** (same choice as Deloitte/Accenture); a German version can be made on request.

## Requirements → evidence
| JD requirement | Evidence | |
|---|---|---|
| Degree in CS / Data Science / related (or portfolio) | MSc Artificial Intelligence (THWS); BTech + Minor in CS | ✅ |
| Python (APIs/REST, Git, methodical debugging) | Python primary; FastAPI REST backends (Kniit, Covestro); GitLab | ✅ |
| SQL | SQL, Postgres (Kniit stack) | ✅ |
| BigQuery or comparable cloud data warehouse (ideally) | DynamoDB, Postgres, Neo4j, vector DBs; no warehouse | ❌ → project |
| LLMs + AI tools (Claude/OpenAI APIs, agents, MCP, Cursor/Claude Code), own solutions built | LangGraph multi-agent pipeline (Kniit), LiteLLM, MCP query service built and wired into Claude Code, Claude Code with own custom skills | ✅ |
| Enterprise cloud (GCP or AWS), deployment, containers, CI/CD | AWS (CDK, Lambda, SQS, DynamoDB, EC2), Azure, Docker, Kubernetes, GitLab CI/CD | ✅ (AWS; no GCP) |
| Shopify (plus) | none | ❌ → project |
| AI automations for internal processes (customer service, supply chain, reporting), prototype → production | Kniit pipeline taken end-to-end to production; not business-process automation | 🟡 → project |
| Integrate systems via APIs into the data warehouse, data for AI agents | MCP service exposing knowledge graph to agents; APIs between React front ends and agentic backends | 🟡 |
| Test results systematically, improve quality, cost, latency | P/R 33%/45% → 93%/90% vs SAP ground truth; deterministic pipeline cut $200k projected LLM spend; millisecond-latency MCP retrieval; RAGAS/PytrecEval | ✅ |
| Process understanding, stakeholder communication, honest about AI limits | Worked with SAP domain experts and CTO (Kniit), chemists (Covestro: Streamlit simulator, ground truth); chose code over LLM where LLM didn't pay off | ✅ |
| Hands-on, self-starter, ~3 projects in parallel | Sole developer at Kniit owning the pipeline end-to-end | ✅ |
| Enablement: internal tools, docs | Expert Interface (graph curation app for domain experts), Streamlit dashboard for chemists | ✅ |
| English C1 | Business fluent | ✅ |
| German B1 | B1 (no certificate) | ✅ |

## Gaps and honest framing
- **BigQuery / data warehouse / Google Cloud:** you know SQL and AWS data services; say you'd pick up BigQuery quickly. Covered by the tailored project (BigQuery sandbox).
- **Shopify / Zendesk / Klaviyo integrations, e-commerce automation:** none in work history. Covered by the tailored project "Shop Support Agent" (build before submitting).
- **OpenAI API by name:** profile says "LLM APIs" and LiteLLM, not OpenAI or the Claude API specifically. Don't name them on the CV until the project uses them.
- **German B1, no certificate:** meets the minimum. If they ask, offer to take a telc/Goethe test.

## Red flags
- **Junior level:** with ~3 years you are above junior; salary will likely sit below your €60–75k target. Decide your floor before the first call.
- **Location mismatch:** LinkedIn says "On-site Mannheim", the text says "Remote ist Standard". Ask in the first call; you're open to relocate either way.
- Posted 2 hours ago, already 50 applicants: apply today.

## Company hooks (sources)
1. **Growth:** SNOCKS grew revenue to about €83M in 2024 (+24% from ~€70M) and is aiming for €100M. ([retail-news.de](https://retail-news.de/snocks-umsatz-wachstum-profitabel-2024/))
2. **House of Brands through acquisitions:** bought the activewear label OCEANSAPART out of insolvency ([Textilwirtschaft](https://www.textilwirtschaft.de/business/news/insolventer-activewear-label-ist-gerettet-snocks-schluckt-oceansapart-248022)) and the period-underwear brand femtis in May 2025 ([FashionUnited](https://fashionunited.de/nachrichten/business/snocks-ubernimmt-anbieter-fur-periodenunterwasche-femtis/2025051561574)). Four brands now share one company setup: more customer-service volume, more systems, more reports. This is exactly where internal AI automation pays off, and it's the angle for the letter.
3. **Tool stack named in the JD:** Shopify, Zendesk/Resolvia, Sage/Anvyl, Klaviyo, a cloud data warehouse (BigQuery likely). Klaviyo itself has launched AI customer-service agents for retailers ([PowerCommerce](https://powercommerce.com/blogs/ecommerce-hub/klaviyo-launches-ai-chat-agent-revolutionizing-customer-support-for-online-retailers)).
4. No public interview found on SNOCKS' internal AI plans; don't claim any.
