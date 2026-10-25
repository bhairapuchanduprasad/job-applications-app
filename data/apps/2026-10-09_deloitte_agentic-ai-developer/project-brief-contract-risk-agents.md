# Project brief: Contract Risk Agents

Repo: `https://github.com/bhairapuchanduprasad/contract-risk-agents` (public)
Status: **planned**. Build and push before submitting the Deloitte application.
Time box: 1–2 days with Claude Code.

## Goal
A small multi-agent contract-review system: upload a contract (PDF/text), one agent extracts key clauses, a second agent checks them against compliance rules, and the user sees flagged risks with explanations in a web UI. Every agent and tool call is traced, and tools are protected by role-based access.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| Strands / Agentic SDKs | Both agents built with Strands Agents (Python SDK) |
| A2A | Clause agent and compliance agent talk over the A2A protocol |
| MCP, APIs (Harnesses) | Contract store + rule set exposed as an MCP server; FastAPI endpoint for the UI |
| RBAC, InfoSec | Roles `viewer` / `reviewer` / `admin` gate which MCP tools each caller can use |
| Trace-Router / tracing | OpenTelemetry spans for every agent step and tool call (export to console or Jaeger) |
| JavaScript | Small vanilla JS (or React) frontend |
| CI/CD, GitLab | `.gitlab-ci.yml`: lint + pytest on every push (mirror repo on GitLab, or GitHub Actions + note) |
| AWS | Amazon Bedrock as model provider (fallback: Anthropic API if no Bedrock access) |
| Deloitte domain | Vertragsmanagement / Compliance: the Business & Technology Center's own topics |

## Scope (keep it small)
In:
- 3–5 sample contracts (public NDA / SaaS templates), 8–10 compliance rules in YAML (e.g. liability cap missing, auto-renewal > 12 months, no GDPR/DPA clause, governing law outside EU).
- Clause Agent: extract parties, term, renewal, liability, termination, data protection, governing law → JSON.
- Compliance Agent: receives clauses via A2A, calls MCP tool `get_rules`, returns findings with severity + quoted clause.
- MCP server: tools `list_contracts`, `get_contract`, `get_rules`, `save_finding` (admin only).
- RBAC: role from an API key header → allowed-tools map, enforced in the MCP server; denied calls are logged.
- OpenTelemetry tracing across both agents.
- Web UI: upload/select contract, choose role, run review, show findings table.
- Tests: pytest for RBAC rules, rule evaluation, clause JSON schema. CI runs them.
Out: auth provider, database, deployment to production, fine-tuning.

## Architecture
```
Browser (JS) ──► FastAPI /review ──► Clause Agent (Strands) ──A2A──► Compliance Agent (Strands)
                                          │                               │
                                          └──────────► MCP server ◄───────┘
                                                     (contracts, rules, RBAC check)
                         OpenTelemetry spans on every hop ──► console / Jaeger
```

## Milestones
1. Repo skeleton, sample contracts, rules YAML, MCP server with 4 tools + RBAC map + tests. (≈3 h)
2. Clause Agent (Strands + Bedrock) producing validated JSON. (≈2 h)
3. Compliance Agent behind A2A; end-to-end run from CLI. (≈3 h)
4. OpenTelemetry tracing; screenshot of a trace. (≈1 h)
5. FastAPI + JS UI. (≈2 h)
6. CI pipeline, README, demo GIF. (≈2 h)

## README outline
Problem → Demo GIF → Architecture diagram → How RBAC works → Tracing screenshot → Run locally (`uv`/`pip`, env vars) → Tests/CI → Limitations & next steps.

## Demo idea
30-second GIF: pick contract → role `viewer` runs review → findings appear → switch to `viewer` trying `save_finding` → denied (RBAC) → trace view showing the A2A hop.

## CV bullets this project must live up to (German CV)
- Multi-Agenten-System zur Vertragsprüfung: Ein Klausel-Extraktions-Agent und ein Compliance-Prüf-Agent (Strands Agents, Amazon Bedrock) kommunizieren über das A2A-Protokoll; Vertragsdaten und Prüfregeln sind als MCP-Server angebunden.
- Rollenbasierte Zugriffskontrolle (RBAC) auf Agenten-Tools, Tracing aller Agenten- und Tool-Aufrufe mit OpenTelemetry, JavaScript-Weboberfläche und GitLab-CI/CD-Pipeline mit automatisierten Tests.

If any part is cut while building, update these bullets in `cv.tex` before submitting. Once built, mark the project `built` in `profile/master-profile.md` and add Strands, A2A, RBAC, OpenTelemetry to your skills.
