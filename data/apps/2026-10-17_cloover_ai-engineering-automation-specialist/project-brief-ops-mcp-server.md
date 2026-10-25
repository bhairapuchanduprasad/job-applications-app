# Project brief: Ops MCP Server

Repo slug: `ops-mcp-server` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the Cloover application (and use it in the case study).
Time box: 1–2 days with Claude Code.

## Goal
A TypeScript MCP server for an operations team: typed, permission-checked tools over HubSpot (deals, contacts) plus retrieval over Notion process docs, used from Claude (Claude Code / Claude Desktop) and from a Slack bot. Example: in Slack, "/deal Müller Solar" returns the deal stage, the open tasks and the relevant step from the installation SOP in Notion.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "custom MCP servers and integrations connecting HubSpot, Slack, Notion …" | The server itself, with HubSpot + Notion tools and a Slack front end |
| "production-grade Python and TypeScript with sound schema design, security, and authorization" | TypeScript, Zod schemas per tool, role-based access, secrets handling |
| "REST APIs, webhooks, and authentication across third-party tools" | HubSpot REST API (private app token), Notion API, Slack Events API webhooks with signature verification, OAuth for Slack install |
| "deploy it on Firebase, Vercel, or GCP with proper version control and CI/CD" | Vercel deployment, GitHub Actions (lint, typecheck, tests) |
| "Build custom Claude Code skills, plugins, and connectors, then onboard colleagues" | Packaged as a Claude Code plugin + a one-page onboarding guide for non-engineers |
| "RAG pipelines, embeddings, retrieval … evaluation" | Notion docs chunked + embedded; small eval set of ops questions |

## Scope (keep it small)
In:
- Free accounts: HubSpot developer test account (sample deals/contacts), Notion workspace with 5–8 SOP pages, Slack workspace.
- MCP server (TypeScript, official MCP SDK) with tools: `find_deal`, `get_contact`, `list_open_tasks`, `search_sops`.
- Zod input/output schemas; a simple role map (ops / sales / finance) restricting which tools and fields each role sees.
- Notion retrieval: export pages → chunk → embeddings → small vector store (e.g. pgvector or an in-memory store).
- Slack bot (Bolt for JS): slash command + Events API webhook with request signing, calls the same tool layer and an LLM to answer.
- Deploy on Vercel; GitHub Actions CI; `.env.example`, no secrets in the repo.
- Eval: 15 ops questions with expected answers; script reports how many are answered correctly.
- Claude Code plugin manifest + README section "How a colleague installs this in 5 minutes".
Out: writing back to HubSpot, Aircall, multi-tenant auth.

## Architecture
```
Slack (slash cmd / events, signed webhook) ─┐
Claude Code / Desktop (MCP client) ─────────┼─► MCP server (TypeScript, Zod, role checks)
                                            │        ├─► HubSpot REST API (deals, contacts, tasks)
                                            │        └─► search_sops ─► vector store ◄─ Notion API export + embeddings
                                            ▼
                                   LLM answer with sources
CI: lint + typecheck + tests + eval (GitHub Actions) ─► Vercel
```

## Milestones
1. Accounts + sample data; MCP server skeleton with `find_deal`, `get_contact`. (≈3 h)
2. Zod schemas, role map, error handling, tests. (≈2 h)
3. Notion export + embeddings + `search_sops`. (≈2 h)
4. Slack bot with signed webhooks + OAuth install. (≈2.5 h)
5. Vercel deploy + CI + eval script. (≈1.5 h)
6. Claude Code plugin packaging, README, onboarding guide, demo GIF. (≈1 h)

## README outline
Problem (ops people switching between HubSpot, Notion and Slack) → Architecture → Tools and their schemas → Security (roles, signed webhooks, secrets) → Eval → Onboarding a colleague → How I used Claude Code → Limitations.

## Demo idea
In Slack: "/deal Müller Solar" → deal stage, open tasks, and the matching SOP step with a link. Then the same question from Claude Code via the MCP server.

## CV bullets this project must live up to
- MCP server in TypeScript that gives Claude and a Slack bot typed, permission-checked tools over HubSpot deals and contacts and retrieval over Notion process docs, so ops questions about a customer get answered from live data instead of manual lookups.
- Slack webhooks and OAuth/API-token authentication, Zod schemas for every tool, role-based access per team, packaged as a Claude Code plugin and deployed on Vercel with CI/CD.

When done, mark it `built` in `profile/master-profile.md`; then real results may go on the CV.
