# Project brief: Ops MCP Server (Chrono24 variant)

Repo slug: `ops-mcp-server` (no link on the CV)
Status: **planned**. Build before submitting the Chrono24 application.
Base brief (read it first, same repo): `applications/2026-10-17_cloover_ai-engineering-automation-specialist/_work/project-brief-ops-mcp-server.md`
Other variant (GitHub tool, Linux/systemd hosting): `applications/2026-10-25_baehrbots_ai-integration-engineer/_work/project-brief-ops-mcp-server.md`
Time box: base project 1–2 days + about half a day for this variant.

## What this variant adds to the base brief
1. **Team-editable configuration**: prompts, answer templates and the role map live in one YAML file (`team-config.yaml`) that a non-technical owner can edit; the server reloads it on start and validates it with a Zod schema, failing with a readable error. Covers "equip teams to run, adjust, and maintain simple solutions themselves".
2. **Handover guide** (`HANDOVER.md`): one page for the business team: what the bot does, how to change a prompt or add a role, how to read the logs, who to call. Plus a short **"when to hand off"** section: signals that a use case needs the ML team (volume/cost, monitored production, self-hosting), Tool Enablement (new integration) or IT (access, security). Covers "Know when to hand off ... and route it cleanly".
3. **Use-case intake note** (`docs/use-case-canvas.md`): a filled-in one-page canvas for the demo use case (team, manual steps today, data needed, systems and access, success check). Covers "Know our systems: judge what has to be made accessible, and articulate the requirement clearly".
4. Keep the base eval set in CI (GitHub Actions).

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| Connect existing tools and LLMs into working workflows fast | MCP server + Slack bot over HubSpot and Notion, Claude as the model |
| APIs, HTTP/JSON and, ideally, MCP | HubSpot/Notion REST, Slack Events API, MCP tools with Zod schemas |
| Hand over working first versions; teams adjust and maintain them | Variant items 1 and 2 |
| Know which systems/data a use case needs | Variant item 3, role-based access per team |
| Applied AI with Claude / GPT, prompt engineering | Prompts in `team-config.yaml`, eval set checks answer content |

## Milestones (variant only, after the base milestones)
1. `team-config.yaml` + Zod validation + reload (≈1.5 h)
2. `HANDOVER.md` incl. hand-off section (≈1 h)
3. Use-case canvas for the demo (≈0.5 h)

## Demo idea
In Slack, a sales/ops person asks "/deal Müller" and gets stage, open tasks and the relevant SOP step; then, live, edit a prompt in `team-config.yaml`, restart, and show the changed answer without touching code.

## CV bullets this project must live up to (English CV)
- MCP server that gives Claude and a Slack bot typed, permission-checked tools over HubSpot deals and contacts and retrieval over Notion process docs, so a business team's everyday questions get answered from live data instead of manual lookups.
- Slack webhooks with request signing and OAuth, Zod schemas for every tool, role-based access per team, prompts and settings the team can adjust without code, a handover guide for running it, a small eval set in CI with GitHub Actions, packaged as a Claude Code plugin.

When done, mark it `built` in `profile/master-profile.md`; then real results may go on the CV.
