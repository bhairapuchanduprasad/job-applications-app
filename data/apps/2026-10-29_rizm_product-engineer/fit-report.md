# Fit report: RIZM, Product Engineer (m/f/x), Munich or Münster

**Fit score: 58/100.** Strong: LLM agents shipped to real users with grounding/evals (Kniit multi-agent LangGraph evaluated against ground truth; Expert Interface for domain experts), knows LLM cost and failure modes ($200k projected LLM budget → near zero via deterministic pipeline), LangGraph + Python, Postgres, Docker/Kubernetes, GitLab CI/CD, React frontends, time-series forecasting (EV load, sensor data), German energy sector context, Claude Code + custom skills daily. Gaps: **strong TypeScript with Vue/React + Node** (React only, no TypeScript/Node/Vue: main gap), "2–5 years building customer-facing products" (internal tools mostly), Google Cloud, Julia/optimisation.

Found by job-scout (LinkedIn 4482512593). English posting, no German requirement → English documents. Application asks for CV + "a few honest lines" on two questions instead of a classic cover letter → the letter answers those two questions.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| 2–5 years building customer-facing products, idea → launch | Kniit system end-to-end; Expert Interface; Covestro app; internal users | 🟡 |
| Strong TypeScript with Vue or React; Node; PostgreSQL | React (beginner/internal tools), Postgres; no TypeScript/Node/Vue | ❌ |
| Containers + CI/CD | Docker, Kubernetes, GitLab CI/CD, AWS CDK | ✅ |
| Shipped LLM features to real users, knows costs + failure modes | Kniit (domain experts), Covestro agent; cost cut, P/R 33/45 → 93/90 | ✅ |
| Claude Code, agents and subagents daily | Claude Code, custom skills, agentic coding workflows | ✅ |
| Agents with guardrails, grounding, evals on real customer data | ground-truth evals on SAP-derived data; reflection agent | ✅ |
| Charts, time series, maps from simulations/live data | Streamlit dashboard for chemists; time-series models | 🟡 |
| Stack: GCP, Kubernetes, GitLab CI, LangGraph, Python | Kubernetes, GitLab CI, LangGraph, Python; no GCP | ✅ |
| Industrial energy (not required) | German energy sector (Kniit) | ✅ |

## Gaps and honest framing
1. **TypeScript/Vue/Node:** none; React + Python only. Planned project is a TypeScript agent. Say it plainly.
2. **Customer-facing product:** users were domain experts and chemists, not external customers.
3. **GCP / Julia:** none.

## Red flags
- Equity "level set during the process"; salary not stated.
- Funding unclear (PitchBook lists Point Nine as investor; Dealroom says none; JD mentions next funding round ahead).

## Company hooks
1. RIZMO, the AI agent in RIZM's Energy OS; Europe's largest industrial companies (about 2% of Europe's energy demand) use it for energy decisions (JD; join.com postings).
2. Software runs at sites like BMW and BSH; grew from a Stanford research project (JD).
3. Formerly Kerith; offices Münster and Munich (Dealroom, JD). Investors per PitchBook incl. Point Nine (unverified).

## Projects on the CV
- **Energy Customer Service Agent** (planned, reused; RIZM variant: TypeScript (Node) agent + Python MCP tools over a simulated industrial-site digital twin: load, PV, tariffs; explains a proposed energy plan with grounding checks; Vue dashboard with time-series charts; eval set in GitLab CI). Brief: `_work/project-brief-energy-service-agent.md`. Status: build-first.
