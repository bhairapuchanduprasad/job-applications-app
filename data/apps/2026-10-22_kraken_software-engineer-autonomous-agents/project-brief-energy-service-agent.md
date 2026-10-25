# Project brief: Energy Customer Service Agent

Repo slug: `energy-service-agent` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the Kraken application.
Time box: 2 days with Claude Code.

## Goal
A customer service agent for a (fictional) energy supplier: TypeScript agent on one side, Python backend with MCP tools on the other. A customer can ask "why is my bill higher this month?" or submit a meter reading. The agent authenticates the customer, calls only the tools that customer is allowed to use, validates inputs (e.g. implausible meter readings), and hands over to a human with the full conversation context when it should. New journeys ship behind feature toggles; an eval set checks correctness and handoff decisions in CI.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Python on the Kraken side and TypeScript on the agent side" | Python (FastAPI) backend + MCP server; TypeScript agent (official MCP TypeScript SDK + an LLM API) |
| "MCP interfaces into Kraken" | MCP server exposing `get_account`, `explain_bill`, `submit_meter_reading`, `handoff_to_human` |
| "authentication, permissions, validation and human handoff" | Session token per customer; tool permissions per customer/role; Pydantic/Zod validation; handoff with transcript + extracted context |
| "feature toggles", "roll out gradually across clients" | Simple toggle config per client (`client_a.yaml`, `client_b.yaml`) enabling journeys |
| "client-agnostic, reusable components" | Journeys defined once, client config injects tariffs, wording, enabled tools |
| "test and monitor behaviour that is less predictable" | Eval set of 25 labelled conversations (correct answer, correct tool, correct handoff) in CI; structured logs per tool call |
| "dashboards, monitoring and runbooks" | Small metrics view (handoff rate, tool errors, eval pass rate) + RUNBOOK.md |
| "Conversational AI / customer service automation" (bonus) | The whole project |

## Scope
In:
- Fake data: 10 customers, tariffs, 6 months of bills and meter readings (SQLite/Postgres).
- Python: FastAPI + MCP server (Python MCP SDK) with 4 tools; auth middleware; per-tool permission checks; meter-reading plausibility validation.
- TypeScript: agent loop using the MCP TypeScript client + an LLM API; system prompt per client; handoff when: low confidence, complaint, failed validation, or customer asks for a person.
- Feature toggles per client (YAML) controlling which journeys are on.
- Evals: 25 conversations; script scores tool choice, answer facts, handoff correctness; GitHub Actions runs unit tests + evals.
- Observability: JSON logs per tool call, simple metrics page; RUNBOOK.md.
Out: real Kraken APIs, voice, email channel (mention as next step).

## Architecture
```
customer chat ─► TypeScript agent (LLM API, client config, toggles)
                        │  MCP (stdio/HTTP)
                        ▼
              Python MCP server ─► auth + permissions ─► tools: get_account, explain_bill,
                        │                                       submit_meter_reading, handoff_to_human
                        ▼
                   Postgres/SQLite (customers, bills, readings)
handoff ─► ticket with transcript + extracted context
CI: unit tests (pytest, vitest) + evals (25 labelled conversations) · logs ─► metrics page
```

## Milestones
1. Data + Python MCP server with 4 tools, auth, validation. (≈4 h)
2. TypeScript agent loop with MCP client, client config, toggles. (≈4 h)
3. Handoff with context. (≈1.5 h)
4. Evals + CI. (≈2.5 h)
5. Logging, metrics page, RUNBOOK.md, README. (≈2 h)

## CV bullets this project must live up to
- TypeScript customer service agent for an energy supplier that explains a bill and accepts a meter reading through MCP tools on a Python backend, with authentication, per-customer permissions, input validation, and a human handoff that passes the full conversation context.
- Client-agnostic journeys configured per client and shipped behind feature toggles, with guardrails on every tool call; an eval set of labelled conversations tests correctness and handoff decisions in CI, and tool calls are logged for observability and monitoring, with documentation and a runbook.

When done, mark it `built` in `profile/master-profile.md`; then real results may go on the CV.
