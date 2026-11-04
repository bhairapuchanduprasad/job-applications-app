# Project brief: Ops MCP Server, Bloomwell variant ("Ops-Assistent mit CRM-Datenbereinigung")
Repo slug: `ops-mcp-server`. Status: **planned**. Build before submitting. 1–2 days with Claude Code. Base: `applications/2026-11-02_almedia_ai-full-stack-engineer/_work/project-brief-ops-mcp-server.md`.
## Goal
TypeScript (Node.js) MCP server with Zod-typed tools over synthetic support-ticket and CRM-contact data in Postgres (HubSpot-like schema), a Slack bot (Bolt, signed webhooks) and a Jira ticket draft that a human approves. Plus a CRM data-quality job: find duplicates, gaps and contradictions, propose cleanups.
## Why it matters for this JD
TypeScript/Node.js, webhooks, tool use/MCP, Slack + Jira + CRM, data quality in CRM, GDPR-aware use of sensitive data (PII masking before model calls), measuring impact (eval set, hours saved estimate).
## Scope
In: seeded synthetic data (500 contacts with planted duplicates/gaps, 100 tickets); tools `find_duplicates`, `data_gaps`, `ticket_summary`, `draft_jira_ticket`; PII masking step before LLM; model adapter; Slack bot; GitHub Actions: lint, typecheck, tests, eval on labelled duplicates.
Out: real HubSpot/Jira/Slack workspaces (use mocks), auth beyond Slack signing.
## CV bullet it must live up to
One bullet: MCP server, Zod tools over synthetic ticket + CRM data (HubSpot-like schema) in Postgres, Slack bot via signed webhooks, Jira ticket draft for human approval, duplicate/gap detection, PII masking before model calls, eval set in GitHub Actions.
## README / demo
README with architecture sketch, 2-min screen recording of a Slack question and a dedupe run. Also usable as the "Vorschlag für Bloomwell" prototype requested by the posting (public/example data only).
