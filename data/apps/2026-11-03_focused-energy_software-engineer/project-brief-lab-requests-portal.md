# Project brief: Lab Requests Portal (variant of Ops MCP Server: TypeScript + role checks)

Related base brief: applications/2026-10-17_cloover_ai-engineering-automation-specialist/_work/project-brief-ops-mcp-server.md (TypeScript, role-checked tools). This variant drops the MCP/Slack parts and focuses on an internal CRUD app with proper auth.

## Goal
Prove the Focused Energy gaps: TypeScript, auth/RBAC/SSO, Postgres schema + migrations + row-level security, scheduled jobs, tests/logs/traces, CI/CD + IaC on Azure, clean handover.

## Scope (1–2 days)
- Domain: research teams file lab/equipment requests (laser time, diagnostics, materials); approvers (lab leads) approve/reject; finance sees cost centre totals.
- Frontend: React + TypeScript (Vite), component library, forms with Zod validation.
- Backend: TypeScript (Node.js, Fastify or Express) REST API, OpenAPI spec.
- DB: PostgreSQL, migrations (Drizzle or Prisma), row-level security policies per team/role.
- Auth: Entra ID single sign-on (MSAL), roles researcher / lab-lead / finance; server-side checks + RLS.
- Scheduled job: nightly sync of an equipment list from a mock CSV/REST source, idempotent upserts.
- Tests: Vitest (unit + API), one Playwright end-to-end flow. Structured logs (pino), request metrics (Prometheus endpoint), OpenTelemetry traces.
- CI/CD: GitHub Actions (lint, test, build, image), deploy to Azure Container Apps + Azure Database for PostgreSQL via Bicep (infrastructure as code); secrets in Key Vault.
- HANDOVER.md: how to run, operate, extend; known limits.

## Milestones
1. Schema + migrations + RLS (3h) 2. API + auth (4h) 3. Frontend (3h) 4. Scheduled job (1h) 5. Tests + logs/traces (2h) 6. CI/CD + Bicep (2h) 7. HANDOVER + README.

## CV bullets it must live up to
- "Internal web application where research teams file and track lab and equipment requests: React + TypeScript frontend, TypeScript (Node.js) REST API, PostgreSQL schema with migrations and row-level security, single sign-on with Entra ID and role-based access control, and a scheduled job that syncs equipment data."
- "Automated tests (Vitest, Playwright), structured logging, request metrics and OpenTelemetry traces, CI/CD in GitHub Actions deploying to Azure Container Apps, and handover documentation for the long-term owner."
