# Project brief: Client Self-Serve Portal
Repo slug: `client-self-serve-portal` (no link on the CV). Status: planned. Time box: 1–2 days with Claude Code.

## Goal
A minimal self-serve portal for advertiser clients of a performance-marketing company: create a campaign, see delivery and spend, download a report, request changes. Routine actions are automated; the rest is queued for the internal growth team to see and act on.

## Why for the Almedia Client Platform JD
Proves: TypeScript, NestJS, NextJS, FastAPI, PostgreSQL, strictly typed and documented (OpenAPI), LLM/agent features, features end to end, interface with a growth team.

## Scope
- Seeded synthetic data (10 clients, 40 campaigns, 60 days of delivery/spend) in PostgreSQL (Docker Compose).
- NestJS API: typed DTOs (class-validator or Zod), OpenAPI spec, auth with roles (client / growth).
- FastAPI service: pricing and delivery forecast endpoints (pydantic models), called by NestJS.
- NextJS app (TypeScript strict): client dashboard, campaign form, CSV report download; internal queue view for the growth team.
- LLM assistant limited to typed tool calls (read campaign stats, draft a change request); never writes without approval; provider swappable by config.
- GitHub Actions: lint, typecheck, unit tests (Jest, pytest), Playwright smoke test.
Out: real billing, real ad-network APIs, BigQuery/dbt (optional stretch: one dbt model).

## Architecture
NextJS → NestJS API (Postgres) → FastAPI pricing/forecast service; LLM tool layer inside NestJS; CI in GitHub Actions.

## Milestones
1. Schema + seed + NestJS CRUD with OpenAPI. 2. FastAPI pricing/forecast + integration. 3. NextJS client + internal views. 4. LLM assistant with approval queue. 5. CI + README.

## README outline
Problem, architecture diagram, run with Docker Compose, API docs, design decisions (typing, approval queue), what is synthetic.

## Demo idea
Client asks "pause my low-performing campaign and tell me why"; the assistant drafts the change, the growth team approves it in the queue.

## CV bullets it must live up to
- Self-serve portal where advertiser clients create campaigns, track delivery and download reports, with a NextJS front end, a NestJS API with typed DTOs and an OpenAPI spec, and a FastAPI service for pricing and forecasts, over seeded synthetic campaign data in PostgreSQL.
- Automates routine client requests with an LLM assistant limited to typed tool calls, shows pending actions to the internal team, and runs lint, type checks and tests in CI.
