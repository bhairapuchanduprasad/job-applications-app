# Project brief: Spec-Driven Coding Agent Harness (Union Investment)

Status: **planned**. Full brief (scope, architecture, milestones, README outline, CV bullets): `applications/2026-10-23_opta-data_ai-engineer/_work/project-brief-spec-driven-agent-harness.md`. One repo covers opta data, BCG Platinion and Union Investment.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Agent Skills, MCP-Server … systematische Evaluation von KI-Systemen" | Custom skills, FastMCP server for spec/task context, evaluation suite over benchmark tasks |
| "technische Leitplanken für KI-native Lösungen" | Rule set + hooks blocking protected files and secrets; CI gates |
| "LLMOps, automatisierte Tests, Delivery-Pipelines, Logging, Tracing, Observability, wirtschaftlicher Betrieb" | CI/CD with tests, SAST, dependency scanning; Langfuse traces; cost and turns per task in the eval report |
| "wiederverwendbare Komponenten" | Harness reusable across repos (template + docs) |

## Extra for Union Investment (optional, ≈1 h)
- README section "Guardrails for regulated environments": what the hooks block, audit trail of agent runs (Langfuse), human approval before merge.

CV bullets match the opta data CV except wording: "CI/CD delivery pipeline" and "tracing and logging of every agent run go to Langfuse for LLMOps monitoring and observability". Make sure every run is traced and logged in Langfuse. Do not add metrics until built.
