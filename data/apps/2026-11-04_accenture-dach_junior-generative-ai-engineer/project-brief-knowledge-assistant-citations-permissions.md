# Project brief: Wissensassistent mit Zitaten und Berechtigungen (Knowledge Assistant for Internal Documents variant)
Repo slug: knowledge-assistant-permissions. Status: planned. For: Accenture DACH / mindcurv (Junior) Generative AI Engineer, 2026-11-04.

## Goal
Small RAG assistant that shows the JD's retrieval topics: chunking, embeddings, metadata, citations, role-based source access, plus an eval set and cost/latency logging.

## Why for this JD
Proves RAG with citations and permissions, LLM evaluation datasets + automated tests, human escalation, FastAPI, Docker, CI/CD, observability basics.

## Scope (1-2 days)
- Public documents (e.g. public German bank/insurer FAQ PDFs), tagged with a `role` metadata field.
- FastAPI service: ingestion, chunking, embeddings into Qdrant, LangGraph flow retrieve (filtered by caller role) -> answer with citations -> confidence check -> hand-off flag "needs human" if not grounded.
- Eval set (30-50 Q/A) with RAGAS + pytest in GitHub Actions; per-request latency/token/cost log.
- Docker Compose.

## Milestones
1. Ingestion + metadata. 2. Retrieval with role filter + citations. 3. Escalation. 4. Eval in CI. 5. README + demo.

## Demo
Same question as two roles: different sources cited; unanswerable question -> escalation.

## CV bullet it must live up to
RAG-Assistent ... Chunking, Embeddings und Vektorsuche mit Metadaten, Antworten mit Zitaten, Zugriff auf Quellen je nach Rolle und Rückfrage an einen Menschen bei unsicheren Antworten; Evaluationsdatensatz und automatisierte Tests mit RAGAS in der CI, Kosten und Latenz im Log; Docker.
