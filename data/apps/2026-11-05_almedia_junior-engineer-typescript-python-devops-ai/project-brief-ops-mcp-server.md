# Project brief: Ops MCP Server, Almedia variant ("Growth Ops Assistant")

Repo slug: `ops-mcp-server` (same repo as the Cloover/Chrono24 version; no link on the CV)
Status: **planned**. Build before submitting the Almedia application.
Time box: 1–2 days with Claude Code.
Base brief: `applications/2026-10-17_cloover_ai-engineering-automation-specialist/_work/project-brief-ops-mcp-server.md`

## Goal
An internal tool for a marketing / user-acquisition (UA) team at a rewards app: a TypeScript (Node.js) MCP server with typed tools over synthetic campaign and offer data in Postgres plus retrieval over a few UA playbook pages, a small React + TypeScript web screen, and a Slack bot. Example: in Slack, "Which offers lost conversion rate this week and why?" returns a short answer with the numbers pulled by tools (never generated) and the matching playbook step.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Full stack applications (front end, back end, databases)" | React + TypeScript screen, Node.js MCP/API server, Postgres |
| "Build and maintain back-end services in Node.js or Python" | Node.js (TypeScript) server; Python only for the eval script if wanted |
| "Architect durable AI workflows that adapt as the LLM landscape evolves, not brittle prompt chains" | Provider-agnostic model layer (one config line to switch model/provider), typed tools with Zod, deterministic tools for all numbers, eval set gating prompt/model changes |
| "Integrate and orchestrate AI APIs" | LLM API behind a small adapter, tool calling, embeddings for retrieval |
| "Work across multiple systems and data sources, making sense of fragmented data" | Three synthetic sources (ad network spend CSV, offer/conversion table, payout table) joined in Postgres views |
| "Collaborate with business teams (marketing, UA, operations)" | Slack bot for the UA team; prompts and thresholds editable in a YAML file without code |
| Nice: TypeScript | Whole server + UI in TypeScript |

## Scope (keep it small)
In:
- Synthetic data generator (seeded): 30 offers, 5 ad networks, 60 days of spend, installs, completions, payouts. Load into Postgres (Docker Compose).
- MCP server (TypeScript, official MCP SDK): tools `offer_performance`, `compare_periods`, `network_spend`, `search_playbook`. Zod input/output schemas; read-only DB role.
- Model adapter: one interface, two providers configured (e.g. Anthropic + OpenAI), switch via config; log latency/tokens per call.
- Retrieval: 5–8 short markdown "UA playbook" pages → embeddings → pgvector.
- React + TypeScript page: ask a question, see the answer, the tool calls made and the raw numbers.
- Slack bot (Bolt for JS) with signed webhooks calling the same tool layer.
- Eval: 20 questions with expected numbers/answers; GitHub Actions runs lint, typecheck, unit tests and the eval on every PR.
Out: real ad-network APIs, writing changes back, auth beyond Slack signing + a simple role map.

## Architecture
```
Slack bot (signed webhook) ─┐
React/TS web screen ────────┼─► Node.js API + MCP server (TypeScript, Zod)
Claude Code (MCP client) ───┘        ├─► Postgres views (spend, offers, payouts)   ← seeded synthetic data
                                     ├─► search_playbook ─► pgvector (playbook pages)
                                     └─► model adapter (provider A / provider B, config switch, cost+latency log)
CI: GitHub Actions → lint, typecheck, tests, eval (20 questions)
```

## Milestones
1. Data generator + Postgres schema + views. (≈2 h)
2. MCP server with 3 data tools, Zod schemas, tests. (≈3 h)
3. Model adapter + playbook retrieval. (≈2 h)
4. React + TypeScript screen. (≈2 h)
5. Slack bot. (≈1.5 h)
6. Eval set + GitHub Actions, README, demo GIF. (≈1.5 h)

## README outline
Problem (UA team pulling numbers from several dashboards) → Architecture → Tools and schemas → Why numbers come only from tools → Switching models → Eval → How a business colleague edits prompts/thresholds → How Claude Code was used → Limitations.

## Demo idea
Ask "Which offers dropped in completion rate vs last week?" in the web screen, show the tool calls and numbers; switch the provider in config and rerun; show the CI eval passing.

## CV bullets this project must live up to
- Internal AI tool for a marketing/user-acquisition team: TypeScript (Node.js) MCP server with Zod-typed tools over campaign, offer and payout data in Postgres, retrieval over team playbooks, a React + TypeScript screen and a Slack bot.
- Provider-agnostic model layer so the model can be swapped by config, numbers only from deterministic tools, and an eval set in GitHub Actions that gates prompt and model changes.
