# Project brief: Collections Ops Workbench (iwoca CV, 2026-11-04)
Status: planned (reuses/extends the "Ops MCP Server" family: internal ops tool with React + Postgres). Build before submitting.
**Goal:** small internal tool for operations teams over synthetic loan-account data.
**Proves for the JD:** Python backend, FastAPI, PostgreSQL, React + TypeScript, internal tools, workflow automation, CI/CD, AI-assisted development.
**Scope (1-2 days):** FastAPI service, PostgreSQL schema + migrations (Alembic), synthetic data generator (accounts, applications, payments); React + TypeScript UI with two work queues (underwriting review, collections follow-up); LLM drafts customer messages that an agent approves or edits before "sending" (stub); role-based access; audit log; pytest + Vitest; GitHub Actions CI/CD; docker-compose.
**Architecture:** React/TS SPA -> FastAPI -> PostgreSQL; LLM via provider-agnostic client; background worker for queue refresh.
**Milestones:** 1 schema+data; 2 API+tests; 3 UI queues; 4 message drafting + approval; 5 CI + README.
**README outline:** problem, architecture diagram, run with docker compose, design trade-offs, tests.
**Demo idea:** 3-minute screen recording: open collections queue, approve an LLM draft, show audit log.
**CV bullet it must live up to:** "Internal tools for operations teams, built over synthetic loan-account data: FastAPI service with a PostgreSQL schema and migrations, and a React and TypeScript UI with work queues for underwriting and collections, workflow automation of customer messages (LLM drafts for agent approval), and a CI/CD pipeline with automated tests."
