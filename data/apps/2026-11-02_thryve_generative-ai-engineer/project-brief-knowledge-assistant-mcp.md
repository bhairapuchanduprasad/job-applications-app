# Project brief: Knowledge Assistant for Internal Documents (THRYVE / Sparkassen-KIPilot variant)

Base brief (full scope, milestones, README outline): applications/2026-10-11_finanz-informatik_ai-engineer/_work/project-brief-knowledge-assistant-mcp.md. Build that; this file only lists what this JD adds.

## Why it matters for this JD
Proves: Python backend development, NLP, DevOps (CI/CD, Docker), an assistant for employees over internal documents with a self-hosted open-source LLM (the S-KIPilot runs in own data centres).

## Variant additions (optional, keep within 1–2 days)
- Corpus: public German bank documents (e.g. public product terms, Sparkasse-style FAQ pages) so the demo is in the banking domain and German.
- A "draft customer letter" endpoint that drafts a reply from retrieved passages, with cited sources (mirrors the KIPilot use case).
- Dockerfile + docker-compose; CI runs lint, pytest and the RAGAS eval.

## CV bullet it must live up to
- RAG assistant over internal process documents with a locally hosted open-source LLM, answers with cited sources, served through a FastAPI REST API and an MCP server; pytest and a RAGAS evaluation set in a GitLab CI/CD pipeline, request logging for monitoring.

When built: mark `built` in profile/master-profile.md with real eval numbers; only then use it in cover letters.
