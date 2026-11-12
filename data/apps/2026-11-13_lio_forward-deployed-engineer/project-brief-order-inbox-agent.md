# Order Inbox Agent (reused planned project) for Lio Forward Deployed Engineer
Existing full briefs: see profile/projects.md line "Order Inbox Agent" (e.g. applications/2026-11-05_dataclue_junior-forward-deployed-engineer/_work/project-brief-order-inbox-agent.md).
Why Lio: proves enterprise integration over APIs and ERP-style systems, FastAPI, PostgreSQL, React, human approval, Docker; turns a customer need (order emails) into a reusable service.
CV bullet to live up to: integration service turning inbound customer order emails into structured ERP-style order records (synthetic article master in PostgreSQL), exposed via FastAPI REST API with retrying webhook sync and a React review screen with human approval before posting.
Scope 1-2 days: Python + FastAPI + PostgreSQL + Docker Compose; LLM extraction with Pydantic schema; match against article master; mock ERP endpoint with retry/backoff; React review UI for low-confidence lines; README with demo.
