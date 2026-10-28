# Project brief (variant): AI Gateway Platform, Beurer AI Platform Engineer

Base brief: applications/2026-10-27_vector_devops-engineer-ai-developer-platforms/_work/project-brief-ai-gateway-platform.md. This variant swaps the Kubernetes/Flux track for a simpler Linux + Docker setup and adds Beurer's stack.

## Why for this JD
Beurer runs Open WebUI + LiteLLM + Microsoft AI Foundry as its central AI platform and wants RAG over SharePoint and internal systems. This project is a small copy of that platform.

## Scope (1–2 days)
- docker-compose on a Linux VM: LiteLLM proxy (virtual keys per team, token budgets, provider fallback, cost/latency logging to Postgres), Open WebUI wired to LiteLLM.
- Providers: Microsoft AI Foundry (Azure) deployment + one fallback provider.
- Python MCP server (FastMCP): RAG over SharePoint documents fetched via Microsoft Graph API (dev tenant or exported sample docs), embeddings in pgvector, citations.
- Config-file onboarding for a new team; pytest + GitHub Actions; README with ops runbook (update LiteLLM/Open WebUI versions, rotate keys).

## CV bullets it must live up to (German)
- Zentrale KI-Plattform: LiteLLM-Proxy (Schlüssel pro Team, Token-Budgets, Fallback, Kosten-Logging) vor Microsoft-AI-Foundry-Modellen, Open WebUI, Docker auf Linux.
- RAG über SharePoint-Dokumente (Microsoft Graph API) als wiederverwendbarer MCP-Server, Tests in CI.
