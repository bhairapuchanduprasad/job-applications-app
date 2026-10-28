# Project brief: Order Inbox Agent, Amadeus Fire / electronics-manufacturer variant (Microsoft 365 + DMS + ERP)

Repo slug: `order-inbox-agent` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-22_comena_forward-deployed-engineer/_work/project-brief-order-inbox-agent.md). Created for Amadeus Fire AI Solutions Engineer (2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
Purchase orders arrive in an Outlook mailbox (Microsoft 365 developer tenant) → Microsoft Graph API pulls mail + attachments → PDFs are filed in a SharePoint document library as the DMS with metadata → LLM extraction + catalog matching (exact, fuzzy, pgvector) → order written to a mock ERP via REST; low-confidence lines go to a review list. Model access through LiteLLM with a cloud model and an open-source model via Ollama, compared on a labelled order set (accuracy, cost, latency).

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Integration von Microsoft 365, ERP, DMS ... über APIs" | Graph API, SharePoint DMS, mock ERP REST |
| "LLMs, RAG und AI Agents" | extraction agent + pgvector catalog retrieval |
| "Cloud-, On-Premises- und Open-Source-AI-Technologien evaluieren" | cloud vs Ollama comparison |
| "vom Proof of Concept bis zum produktiven Einsatz" | Docker Compose, CI eval gate, README runbook |

## Tech stack
Python, FastAPI, Microsoft Graph SDK, SharePoint, LiteLLM, Ollama, Postgres + pgvector, pytest, GitHub Actions, Docker Compose.

## Milestones
1. Graph mail + SharePoint filing (4 h) 2. Extraction + matching + mock ERP (4 h) 3. Cloud vs open-source eval (3 h) 4. README (1 h).

## CV bullet it must live up to
- Order-intake automation: purchase orders from a Microsoft 365 mailbox (Graph API) are filed in a SharePoint DMS, extracted by an LLM, matched to the product catalog with pgvector and written to a mock ERP via REST API; a labelled order set compares a cloud LLM with an open-source model (Ollama) on accuracy, cost and latency.
