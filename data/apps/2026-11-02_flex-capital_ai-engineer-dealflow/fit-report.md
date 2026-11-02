# Fit report: FLEX Capital, AI Engineer - Dealflow (m/w/d), Berlin

Source: https://www.linkedin.com/jobs/view/4485470605 (found by job-scout 2026-11-02)
Language: German posting, "Du sprichst verhandlungssicher Deutsch und Englisch" → German Lebenslauf + Anschreiben; German B1 = top gap (verhandlungssicher ≈ C1, but not stated as C1/C2 → prepare per scout rules).
Seniority: 2–3 years building AI-based products/tools; office in Berlin (Gleisdreieck).

## Fit score: 66 / 100
Technical core matches well (own Python tools in production use, Docker, Azure, LLM APIs in practice incl. knowing where they fail, LangGraph agent systems). Gaps: CRM data / Pipedrive, sales-prospecting tooling (enrichment, multichannel outreach), commercial/deal-origination thinking, and German at negotiation level for an investment team.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Built own tools/automations in productive use, not just prototypes | Kniit pipeline + Expert Interface (deployed on Azure, used by SAP domain experts); Covestro agentic app deployed to AWS | ✅ |
| 2–3 years building AI-based products | 3 years | ✅ |
| Python, Docker, deploy on Azure | Python ✅, Docker ✅, Azure (Expert Interface) ✅ | ✅ |
| LLM APIs (OpenAI, Claude) in practice, know limits | LiteLLM model layer, Claude Code/MCP; deterministic pipeline where LLM did not pay off ($200k → near zero) | ✅ |
| CRM data, data quality and structure | Data quality via ground-truth evaluation; no CRM | 🟡/❌ |
| Pipedrive, agent systems, LangGraph (plus) | LangGraph agent systems ✅; Pipedrive ❌ | ✅/❌ |
| Commercial thinking, measure by results | P/R and cost results; Covestro consulting with business stakeholders | 🟡 |
| Screening/prioritisation logic, hit quality | Extraction quality optimisation (P/R) is analogous | 🟡 |
| Automated data enrichment (firmographics, ownership) | Ingestion/extraction pipelines; no B2B data vendors | 🟡 |
| Dashboards/reports on funnel | Streamlit dashboard (Covestro); no BI/funnel reporting | 🟡 |
| Degree (Wirtschaftsinformatik/Data Science/Informatik/MINT) | MSc AI | ✅ |
| Verhandlungssicher Deutsch | B1 | ❌ top gap |

## Gaps and honest framing
1. **German**: B1, stated openly; investment team in DACH Mittelstand will likely need German outreach. Biggest risk.
2. **CRM / Pipedrive / outbound tooling**: none. Planned project "Dealflow Sourcing Engine" covers it; unbuilt → not proof.
3. **Deal origination / PE**: no domain experience.

## Red flags
- Outreach to company owners in DACH Mittelstand is German-language work; role may effectively require near-native German despite tooling focus.

## Company research (hooks)
1. FLEX Capital: Berlin PE fund founded by serial entrepreneurs, majority stakes in profitable, growing internet/software Mittelstand (DACH) with €5–30M revenue. Source: https://www.deutsche-startups.de/?p=409502 / https://parsers.vc/fund/flex.capital/
2. Second fund closed at €300M (Jan 2023), with an in-house operations team of ~30 experts to support portfolio companies. Source: https://www.ypog.law/hubfs/YPOG%20Pressemitteilung%20FLEX%20Capital%20%E2%82%AC%20300%20Millionen%20Closing%2019.%20Januar%202023%20(1).pdf
3. Posting: role builds a proprietary dealflow tool to reach owners before an M&A adviser is mandated; works with the FLEX leadership, investment and Data & AI teams.

## Projects on the CV
- Dealflow Sourcing Engine (planned; variant of Client Occasion Engine: prioritisation + LLM-drafted messages + integration adapter). Brief: project-brief-dealflow-sourcing-engine.md → build-first.
