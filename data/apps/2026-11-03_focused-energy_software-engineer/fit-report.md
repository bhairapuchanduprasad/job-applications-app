# Fit report: Focused Energy, Software Engineer (f/m/d), Berlin

Source: https://www.linkedin.com/jobs/view/4486440900 (found by job-scout 2026-11-03)
Language: English posting, no German requirement → English CV + cover letter.
Seniority: mid ("own moderately complex, well-scoped features", support available for broader architecture). No years stated.

## Fit score: 64 / 100
Forward-deployed internal-tools engineer: builds apps, data workflows, integrations and automation for scientists, finance, legal and people teams. Strong match on working with domain experts, internal web apps (Expert Interface, Streamlit for chemists), Python/React, Postgres, Azure/AWS, CI/CD, AI-assisted development. Not an AI/ML role (AI tools only as a way of working). Gaps: TypeScript (stated typed language; "similar language also relevant"), auth/RBAC/SSO, row-level security, observability/traces, monorepo.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Own well-scoped features design→deploy | Sole developer at Kniit; Covestro stack deployed to AWS | ✅ |
| SWE fundamentals, testing, version control, code review | Clean code, Postman API tests, GitLab | 🟡 (no named test frameworks) |
| TypeScript/JavaScript or similar typed language | Python (typed language not claimed); React | 🟡 / ❌ TS |
| Component-based frontend (React) | React frontends at Kniit and Covestro | ✅ |
| Relational DBs, SQL, schemas, migrations, permissions | SQL, Postgres; migrations/permissions not explicit | 🟡 |
| REST APIs, events, scheduled jobs | FastAPI REST, AWS SQS/Lambda | ✅ |
| AuthN/AuthZ, RBAC, secure data handling | not in profile | ❌ (planned project) |
| CI/CD, IaC, package mgmt | GitLab CI/CD, AWS CDK, Docker | ✅ |
| Tests, logs, metrics, traces to debug | evaluation metrics; no OpenTelemetry in work | 🟡 |
| AI-assisted development used responsibly | Claude Code, custom skills, agentic workflows | ✅ |
| Turn non-software specialists' needs into requirements | SAP domain experts, chemists, Covestro stakeholders | ✅ |
| Nice: Azure, serverless, internal tools, dashboards, data pipelines, scientists | Azure, Lambda, Expert Interface, Streamlit, ingestion pipeline, chemists | ✅ |

## Gaps and honest framing
1. TypeScript: not used; letter says so and offers ramp-up via small changes and code review.
2. Auth/RBAC/SSO, row-level security: not claimed; covered by planned project only.
3. Observability (traces): not claimed.
4. Not an AI role: fine for the user's full-stack/all-rounder identity, but less AI depth day to day.

## Red flags
- Company is hiring broadly across Germany and the US; Berlin team size unknown.
- Fusion startup: funding-dependent, though $240M Series A secured (May 2026).

## Company hooks
1. May 2026: $240M Series A (RWE, SPRIND, EIC Fund, Prime Movers Lab), funds going to the former RWE Biblis power plant site ([Business Wire](https://businesswire.com/news/home/20260527514871/en/Focused-Energy-Raises-%24240-Million-in-Series-A-Financing), [startbase](https://www.startbase.de/news/focused-energy-sammelt-240-millionen-us-dollar-fuer-laserfusion-ein/)).
2. 2021 spin-out of TU Darmstadt; "Hessen-Champion 2025" innovation award ([TU Darmstadt](https://www.tu-darmstadt.de/xchange/news_details_530560.de.jsp)).
3. Plans to spin off Sourcelight (laser-driven radiation source) ([City A.M.](https://www.cityam.com/?p=2432337)).
4. Berlin representative office listed in the Bundestag lobby register ([lobbyregister](https://www.lobbyregister.bundestag.de/suche/R005299)).

## Project
Lab Requests Portal (Ops MCP Server variant, planned): see project-brief-lab-requests-portal.md.
