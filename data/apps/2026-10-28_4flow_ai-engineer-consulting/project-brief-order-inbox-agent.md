# Project brief: Order Inbox Agent, 4flow variant (n8n + Microsoft Teams)

Repo slug: `order-inbox-agent` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-22_comena_forward-deployed-engineer/_work/project-brief-order-inbox-agent.md). Created for 4flow AI Engineer Consulting (2026-10-28). Time box: 1–2 days with Claude Code.

## Goal
Email/PDF/Excel purchase orders → LLM extraction → catalog matching (exact, customer map, fuzzy, pgvector) → mock ERP via REST. 4flow addition: an n8n workflow triggers the agent on new mail and posts low-confidence order lines to a Microsoft Teams channel (incoming webhook / Adaptive Card) for approval.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "AI Agents, Assistenten und Automatisierungslösungen" | extraction + matching agent |
| "skalierbare AI Workflows wie z.B. n8n" | n8n trigger + approval workflow |
| "Integration ... in Microsoft-365-, Teams-Umgebungen" | Teams approval card |
| "Supply-Chain", "Prototypen, wiederverwendbare AI-Frameworks" | order intake in logistics; per-customer config |
| "LLMOps, RAG" | labelled orders eval in CI, cost/latency logging |

## Tech stack
Python, LangGraph or plain LLM calls via LiteLLM, Django or FastAPI, Postgres + pgvector, n8n (Docker), Microsoft Teams webhook, pytest, GitHub Actions, Docker Compose.

## Milestones
1. Base Order Inbox Agent per base brief (1 day) 2. n8n workflow + Teams card (3 h) 3. Eval + README (2 h).

## CV bullet it must live up to (German)
- Agent für eingehende Bestellungen (E-Mail, PDF, Excel): LLM-Extraktion, Abgleich mit dem Artikelkatalog (exakt, fuzzy, pgvector) und Übergabe an ein Mock-ERP per REST-API; ein n8n-Workflow legt unsichere Positionen in Microsoft Teams zur Freigabe vor.
