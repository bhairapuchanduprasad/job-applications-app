# Project brief: n8n AI Workflow Hub (repo: n8n-ai-workflow-hub)
**Goal:** self-hosted n8n instance with AI-driven request handling workflows.
**Proves for the JL.Digital IT-Consultant Cloud & AI JD:** n8n, Claude/LLM integration, RAG, APIs and third-party systems, workflows/process automation.
**Scope (1-2 days):** Docker Compose n8n + Postgres; webhook and IMAP email trigger; LLM node (Claude API) classifies requests and drafts answers with RAG over a small markdown knowledge base (Qdrant or pgvector); results pushed to a REST API (mock CRM) ; approval step (n8n wait/webhook) before sensitive actions; error workflow + logging.
**Stack:** n8n, Docker, Postgres, Claude API, Python FastAPI mock CRM, Qdrant/pgvector.
**Architecture:** trigger -> classify -> retrieve -> draft -> approve? -> call CRM API -> log.
**Milestones:** 1 compose + trigger; 2 classify/RAG; 3 approval + CRM; 4 README + demo GIF.
**README outline:** problem, architecture diagram, setup, workflows exported JSON, limitations.
**Demo:** send a request email, watch the workflow answer and create a CRM record.
**CV bullet it must live up to:** "Self-hosted n8n workflows that take incoming customer requests via webhook and email, classify and answer them with an LLM (Claude) using a small RAG knowledge base, and push results to third-party systems through REST APIs, with logging and an approval step for sensitive actions."
