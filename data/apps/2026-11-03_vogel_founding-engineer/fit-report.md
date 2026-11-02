# Fit report: Vogel (Vogel Beratung), Founding Engineer (m/w/d), Munich

Source: https://www.linkedin.com/jobs/view/4486416939 (found by job-scout 2026-11-03)
Language: English posting with German FAQ; "you work in German and in person, because our advisors and clients do". Not C1-mandatory → prepare, German = top gap. English documents (posting in English).
Seniority: early-career welcome ("lower end = right after university"); range €60K–156K. Good level.

## Fit score: 62 / 100
Strong on the engineering shape: data pipelines, backend, agents with a clear line between model judgment and deterministic calculation, evaluation against closed cases. Kniit (sole developer, agentic + deterministic pipelines, ground-truth eval, Expert Interface for domain experts) maps closely. Gaps: German as working language, TypeScript, accounting/tax/DATEV, "TUM-level" bar, daily in-person in Munich.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Strong degree or strong own projects | MSc AI | ✅ |
| Shipped software others used | Expert Interface used by domain experts; Covestro dashboard used by chemists | ✅ |
| Production code in Python or TS; SQL + relational DBs | Python daily; SQL, Postgres | ✅ / ❌ TS |
| AI as everyday tool, knows where it goes wrong | Claude Code, custom skills, agentic coding workflows | ✅ |
| Breadth: data, backend, interface, agents | Kniit pipeline + MCP + React/Python app + LangGraph agents | ✅ |
| Line between model judgment and deterministic calculation | Deterministic pipeline replaced LLM for high-volume stream ($200k → ~0) | ✅ |
| Traceable results, evaluate on closed audited cases | P/R vs SAP-derived ground truth | ✅ / 🟡 |
| Work in German, in person | B1 | ❌ top gap |
| Accounting/tax/DATEV (plus) | none | ❌ |
| 1–2 yrs startup engineer (plus) | Kniit startup, 1 year | ✅ |

## Gaps and honest framing
1. German: B1; they work in German. Say it plainly, and that he is improving; advisors' domain language will be the main ramp.
2. DATEV / accounting: none. Planned project uses synthetic DATEV-style exports.
3. TypeScript: React (beginner) only.

## Red flags
"Wer 9-to-5 sucht, ist bei uns nicht die erste Adresse" (intensity); daily office presence; CTO being hired in parallel. Written task with 8 questions is the first step.

## Company hooks
1. Vogel: family-owned Mittelstand advisory since 1959 from Aalen; sites Aalen, Bopfingen, Munich as new hub ([Arbeitnow postings](https://www.arbeitnow.com/jobs/companies/vogel/operations-berufseinstieg-munchen-154622)).
2. Buy & Build: acquires advisory firms and integrates them on one base; expanding into legal, CFO advisory, digitalisation/process consulting ([CFO Buy & Build posting](https://www.remotely.de/job/vogel-beratung-cfo-buy-build-mwd)).
3. Posting: data layer above DATEV, agents for recurring work, "evaluate against closed, audited cases, not test data"; KI tools without token limit.

## Project
Advisory Data Layer & Booking Agent (Semantic Analytics Agent variant, planned): see project-brief-advisory-data-layer.md.
