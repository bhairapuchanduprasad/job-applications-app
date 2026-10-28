# Project brief: Energy Customer Service Agent, RIZM variant (industrial site digital twin, TypeScript + Vue)

Repo slug: `energy-service-agent` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-22_kraken_software-engineer-autonomous-agents/_work/project-brief-energy-service-agent.md). Created for RIZM Product Engineer (2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
TypeScript (Node) agent that answers an energy manager's questions about an industrial site and explains a proposed day-ahead plan. Tools come from a Python MCP server over a simulated digital twin (15-minute load profile, PV output, battery, day-ahead prices, grid tariff). Every number in an answer must come from a tool result (grounding check); a Vue 3 + TypeScript dashboard shows load/price time series and the agent's plan; Postgres stores runs; a labelled question set runs as an eval suite in GitLab CI.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Strong TypeScript with Vue or React, comfortable across browser, Node and PostgreSQL" | Node agent, Vue dashboard, Postgres |
| "AI agents that read digital twins, run optimisations, explain plans" | MCP tools over the twin, plan explanation |
| "guardrails, grounding and evals" | grounding check, eval suite |
| "charts, time series" | Vue dashboard with ECharts |
| "containers and CI/CD", "GitLab CI" | Docker Compose, GitLab CI pipeline |

## Milestones
1. Twin simulator + MCP server (4 h) 2. TypeScript agent + grounding check (4 h) 3. Vue dashboard (3 h) 4. Evals in GitLab CI + README (2 h).

## CV bullet it must live up to
- TypeScript (Node) agent that explains day-ahead energy plans for a simulated industrial site, using Python MCP tools over a digital twin (load, PV, prices); grounding check on every figure, Vue dashboard with time-series charts, Postgres run log and an eval suite in GitLab CI.
