# Project brief: GenAI Service for existing apps (Knowledge Assistant for Internal Documents variant)
Repo slug: genai-service-spring-angular. Status: planned. For: attempto GenAI Engineer mit Fullstack-Hintergrund (2026-11-03).

## Goal
Show how a GenAI feature is embedded into an existing Angular + Spring Boot business application through a clean OpenAPI contract.

## Why for this JD
Proves RAG + agentic workflow (LangGraph), OpenAPI/Swagger design, Spring Boot integration, Angular (TypeScript) UI, guardrails + evaluation, Azure OpenAI, vector DB, Docker/Kubernetes, LLMOps basics.

## Scope (1–2 days)
- Domain: public insurance product terms (AVB PDFs) as the "existing app" knowledge base.
- Python/FastAPI GenAI service: ingestion, chunking, embeddings into Qdrant/Pinecone, LangGraph agent (retrieve → answer → citation check → refuse if not grounded); Azure OpenAI via LiteLLM.
- OpenAPI spec written first (Swagger), versioned; generated Java client.
- Spring Boot backend (existing-app stand-in) calls the service via the generated client; Angular page shows answer + sources.
- Guardrails: grounding check, PII redaction, topic filter; RAGAS eval set in GitHub Actions.
- Docker Compose; Kubernetes manifests (kind).

## Milestones
1. OpenAPI contract. 2. GenAI service + eval. 3. Spring Boot client. 4. Angular UI. 5. Docker/K8s + README.

## Demo
Ask a policy question in the Angular app → cited answer; ungrounded question → refusal.

## CV bullet it must live up to
- GenAI-Service mit FastAPI und LangGraph (RAG mit Embeddings und Vektordatenbank, Azure OpenAI, Guardrails mit Grounding-Check und RAGAS-Evaluation), angebunden über eine OpenAPI/Swagger-Spezifikation an ein Spring-Boot-Backend und eine Angular-Oberfläche; Docker und Kubernetes.
