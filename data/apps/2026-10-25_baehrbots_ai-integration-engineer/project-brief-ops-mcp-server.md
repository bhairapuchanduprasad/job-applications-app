# Project brief: Ops MCP Server (BaehrBots variant)

Repo slug: `ops-mcp-server` (no link on the CV)
Status: **planned**. Build before submitting the BaehrBots application. It doubles as the work sample the posting asks for ("Arbeitsproben, z. B. ein Agent oder eine Automation, die du gebaut hast").
Base brief (read it first, same repo): `applications/2026-10-17_cloover_ai-engineering-automation-specialist/_work/project-brief-ops-mcp-server.md`
Time box: base project 1–2 days + about half a day for this variant.

## What this variant adds to the base brief
1. **GitHub tool**: `list_open_prs` (and optionally `get_pr_status`) via the GitHub REST API with a fine-grained, read-only token. Covers "GitHub ... über Tool Use, MCP und saubere Schnittstellen".
2. **Self-hosted on Linux** instead of (or in addition to) Vercel: Docker image + `docker compose`, started by a systemd unit (`ops-mcp.service`, `Restart=on-failure`), logs via `journalctl`. Covers "Betrieb von Diensten auf Linux-Servern (systemd, Docker, Logs)" and "Own the stack: ... sicher und versioniert auf unsere Server bringen".
3. **Secrets and least privilege**: secrets only in an env file outside the repo (`chmod 600`), `.env.example` in the repo, least-privilege scopes for Slack, HubSpot and GitHub tokens, documented in the README. Covers "Least Privilege, Umgang mit Secrets".
4. **Honest checks**: the eval script must verify the answer content against expected data, not just a successful API call ("Ein grüner Haken zählt nur, wenn das Ergebnis wirklich da ist").

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| LLM-APIs an Slack, Google Workspace, GitHub anbinden, über Tool Use und MCP | MCP server with HubSpot, Notion, GitHub tools; Slack bot front end (Google Workspace stays a gap) |
| API-Integrationen (REST, Webhooks, OAuth) | HubSpot/GitHub REST, Slack Events API with signature verification, OAuth install |
| Linux-Server (systemd, Docker, Logs) | Variant item 2 |
| Least Privilege, Secrets | Variant item 3, role map |
| Monitoring, Evals, ehrliche Kennzahlen | Eval set in CI + content-level checks |
| Git/GitHub im Pull-Request-Workflow | Build it with PRs on GitHub, GitHub Actions CI |

## Milestones (variant only, after the base milestones)
1. `list_open_prs` tool + tests (≈1 h)
2. Dockerfile, compose file, systemd unit, deploy on a small Linux VM, log check (≈1.5 h)
3. Secrets/least-privilege README section, content-level eval checks (≈1 h)

## CV bullets this project must live up to (German CV)
- MCP-Server, der Claude und einem Slack-Bot typisierte, rechtegeprüfte Werkzeuge über HubSpot-Deals, offene GitHub-Pull-Requests und eine RAG-Suche über Notion-Prozessdokumente gibt, damit Teamfragen aus Live-Daten beantwortet werden.
- Slack-Webhooks mit Signaturprüfung und OAuth, Zod-Schemas für jedes Werkzeug, rollenbasierter Zugriff nach Least Privilege, Secrets nur über Umgebungsvariablen; Betrieb mit Docker und systemd auf einem Linux-Server, CI mit GitHub Actions inklusive kleinem Eval-Set, als Claude-Code-Plugin paketiert.

When done, mark it `built` in `profile/master-profile.md`; then real results may go on the CV.
