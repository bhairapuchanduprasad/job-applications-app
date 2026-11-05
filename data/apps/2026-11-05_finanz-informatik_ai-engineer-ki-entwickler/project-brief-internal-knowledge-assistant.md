# Project brief: Internal Knowledge Assistant (RAG + MCP)
Repo slug: internal-knowledge-assistant. Status: planned. For: Finanz Informatik AI Engineer, 2026-11-05. Reuses the planned "Knowledge Assistant for Internal Documents" idea.
## Goal
Proves JD keywords: RAG, MCP, REST API, LlamaIndex, testing, CI/CD, documentation.
## Scope (1-2 days)
FastAPI service over a small set of public/synthetic internal-style documents (policies, IT how-tos), indexed with LlamaIndex in a vector DB (Qdrant); answers with source citations; same retrieval exposed as an MCP server; pytest API tests; 30-question RAGAS evaluation in GitHub Actions; Docker Compose; short architecture and API documentation.
## Milestones
1 ingestion + index, 2 REST endpoint with citations, 3 MCP server, 4 tests, 5 RAGAS in CI, 6 README/docs.
## Demo
Ask a question via REST and via an MCP client; show citations and the CI evaluation report.
## CV bullet it must live up to
RAG assistant over internal documents with citations, exposed as a REST API and MCP server, with tests and RAGAS evaluation in CI.
