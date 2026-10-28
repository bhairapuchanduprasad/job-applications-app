# Project brief: Order Inbox Agent, getpress variant (LangGraph + Next.js + feedback loop)

Repo slug: `order-inbox-agent` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-22_comena_forward-deployed-engineer/_work/project-brief-order-inbox-agent.md). Created for getpress Backend Engineer - Agentic AI (2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
Email/PDF/Excel purchase orders → LLM extraction → catalog matching (exact, fuzzy, pgvector) → mock ERP via REST. getpress additions: orchestration as a LangGraph graph with Postgres-persisted state, a Next.js (TypeScript) review screen for low-confidence lines, and a feedback loop: reviewer corrections are stored in Postgres and retrieved as few-shot examples for later orders.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "TypeScript", "Next.js" | Next.js review screen in TypeScript |
| "Memory, Context-Engineering, Retrieval und Orchestration" | Postgres-persisted LangGraph state, retrieved correction examples in the prompt |
| "Self-Learning-Loops" | correction → example store → better next extraction, measured on the eval set |
| "relationale Daten- und Vektor-Datenbanken" | Postgres + pgvector |
| "Docker, Git, GitHub" | Docker Compose, GitHub Actions |

## Tech stack
Python, LangGraph, LiteLLM, FastAPI, Postgres + pgvector, Next.js + TypeScript, pytest, GitHub Actions, Docker Compose.

## Milestones
1. Base agent per base brief (1 day) 2. Next.js review screen + correction store (4 h) 3. Eval before/after corrections + README (2 h).

## CV bullet it must live up to (German)
- Agent für eingehende Bestellungen (E-Mail, PDF, Excel) als LangGraph-Graph mit Zustand in PostgreSQL: LLM-Extraktion, Abgleich mit dem Artikelkatalog (exakt, fuzzy, pgvector) und Übergabe an ein Mock-ERP per REST-API; Korrekturen aus einer Next.js-Prüfoberfläche (TypeScript) fließen als Beispiele in spätere Extraktionen zurück.
