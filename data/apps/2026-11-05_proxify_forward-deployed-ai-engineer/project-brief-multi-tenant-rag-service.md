# Project brief: Multi-Tenant RAG Service (Knowledge Assistant variant)
Repo slug: multi-tenant-rag-service. Status: planned. For: Proxify Forward Deployed AI Engineer, 2026-11-05.
## Goal / why
Proves JD keywords: RAG pipelines, vector databases, streaming, multi-tenancy, multiple LLM providers, vLLM, containerized deployment.
## Scope (1-2 days)
FastAPI service; public docs for 2-3 fictional tenants in Qdrant with a tenant filter enforced server-side; streamed (SSE) answers with citations; LiteLLM routing to OpenAI/Anthropic with fallback to a small open model served by vLLM (CPU/small GPU or documented stub); 30-Q RAGAS eval in GitHub Actions; Docker Compose.
## Milestones
1 ingestion + tenant metadata, 2 tenant-filtered retrieval + citations, 3 streaming, 4 LiteLLM + vLLM fallback, 5 eval in CI, 6 README.
## Demo
Same question as tenant A and B returns different sources; kill the hosted provider and watch fallback.
## CV bullet it must live up to
RAG service with per-tenant isolation in the vector database, streamed answers with citations, multiple LLM providers via LiteLLM with an open-source fallback served with vLLM, RAGAS eval in CI, Docker Compose.
