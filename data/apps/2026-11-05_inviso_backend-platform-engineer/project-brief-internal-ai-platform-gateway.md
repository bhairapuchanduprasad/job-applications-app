# Project brief: Internal AI Platform Gateway (variant of AI Gateway Platform / LLM Gateway)
Status: planned. Used on the Inviso Backend / Platform Engineer CV (2026-11-05).

**Goal:** Multi-tenant LLM gateway in Python/FastAPI on top of LiteLLM.
**Why for this JD:** proves AI gateway, tenancy, quotas, metering, retries, idempotency, MCP, governed data access.
**Scope (1–2 days):** tenants + per-team API keys; token quotas enforced per tenant; usage events written to an append-only table (Postgres) and aggregated for metering; provider fallback with retries/timeouts; Idempotency-Key header; a small MCP server exposing one governed internal data source; pytest suite + GitHub Actions with image scan.
**Stack:** Python, FastAPI, LiteLLM, Postgres, Docker, pytest, GitHub Actions, MCP SDK.
**Architecture:** client -> FastAPI gateway (auth, tenant lookup, quota check) -> LiteLLM -> providers; usage events -> Postgres; MCP server -> mock data API.
**Milestones:** 1 gateway + keys; 2 quotas + metering events; 3 retries/fallback/idempotency; 4 MCP server; 5 tests + CI + README.
**README outline:** problem, architecture diagram, run locally, tenant config example, failure-mode tests.
**Demo idea:** two tenants, one hits quota, one provider forced to fail and fall back.
**CV bullet it must live up to:** "Multi-tenant LLM gateway in FastAPI on LiteLLM: per-team keys, token quotas, usage metering as an event log, provider fallback with retries and idempotent requests, and an MCP server for governed internal data."
Also see applications/2026-11-03_zapp_ai-platform-engineer/_work/project-brief-ai-platform-azure.md.
