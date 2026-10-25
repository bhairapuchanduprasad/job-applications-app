# Project brief: Autohaus Service Agent

Repo slug: `autohaus-service-agent` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the HAIAR application.
Time box: 1–2 days with Claude Code.

## Goal
A Python backend that answers dealership workshop questions ("What does the 60,000 km service on a 2021 Golf cost?", "Book a brake check next week") from a small document set, using RAG plus a LangGraph agent with real state and error handling, and with evaluation + monitoring built in from day one.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| Python-Backend mit Fokus auf KI-Systeme; APIs | FastAPI service, clean module layout (ingestion / retrieval / agent / api) |
| RAG-Architekturen für produktive Anwendungsfälle | Ingestion → embeddings in Qdrant → dense + keyword retrieval → grounded answer with citations |
| KI-Pipelines (Ingestion, Retrieval, Kontextsteuerung, Inferenz) | Explicit pipeline stages; context budget (top-k + token limit) before the LLM call |
| Agent-Workflows inkl. Zustands- und Fehlerhandling | LangGraph graph with Postgres-persisted state (checkpointer), retries on tool errors, human-handoff node |
| Trade-offs Qualität, Latenz, Kosten | Request log of latency/tokens/cost; README table comparing 2 retrieval configs |
| Monitoring, Stabilität | Per-request logging + `/metrics` endpoint |
| Halluzinationen, Drift, Evaluierung | Labelled question set; groundedness + retrieval recall (RAGAS) in CI; weekly score comparison script flags drift |
| Autohaus domain | Synthetic workshop manuals, service price lists, appointment slots |

## Scope (keep it small)
In:
- Synthetic data: 10–20 Markdown/PDF "workshop" docs (service intervals, price list, warranty rules), a JSON of free appointment slots. Write them with Claude, mark as synthetic in README.
- Ingestion script: chunk, embed (open-source embedding model or API), store in Qdrant (Docker).
- Retrieval: dense + simple keyword (BM25-style) merge, top-k, token budget.
- LangGraph agent: nodes `classify → retrieve → answer` and tool `check_slots/book_slot`; state persisted with a Postgres checkpointer; retry with backoff on tool/LLM errors; `handoff_to_human` node when retries fail or confidence is low.
- FastAPI: `POST /ask`, `POST /conversations/{id}/message`, `GET /metrics`.
- Request log table in Postgres: latency, tokens, cost, retrieval scores, status.
- Eval: 25–40 labelled questions with expected source doc + answer facts; RAGAS faithfulness/answer relevancy + retrieval recall; runs in CI (GitHub Actions or GitLab CI), stores results as JSON.
- `drift_check.py`: compares the latest eval run with the previous baseline and fails/flags if scores drop beyond a threshold.
- docker-compose (api + Qdrant + Postgres), pytest tests.
Out: frontend, auth, real dealership data, real DMS integration.

## Architecture
```
docs/ ──► ingest.py ──► embeddings ──► Qdrant
                                        │
client ──► FastAPI ──► LangGraph agent ─┤ retrieve (dense + keyword, context budget)
              │          │  state ◄──► Postgres checkpointer
              │          ├─► tools: check_slots / book_slot (retry, backoff)
              │          └─► handoff_to_human (on repeated failure)
              ▼
        request log (Postgres) ──► /metrics
eval set ──► CI: pytest + RAGAS + retrieval recall ──► drift_check.py
```

## Milestones
1. Synthetic docs + ingestion into Qdrant. (≈2 h)
2. Retrieval (dense + keyword, budget) + `/ask`. (≈2 h)
3. LangGraph agent with Postgres state, tools, retries, handoff. (≈3 h)
4. Request logging + `/metrics`. (≈1 h)
5. Eval set + RAGAS + CI + drift check. (≈3 h)
6. docker-compose, README, demo recording. (≈1.5 h)

## README outline
Problem (dealership workshop questions) → Architecture diagram → Pipeline stages → Agent state & error handling → Evaluation & drift → Trade-offs (retrieval config A vs B: quality, latency, cost) → Run locally → Limitations (synthetic data).

## Demo idea
Ask a price question (grounded answer with source), start a booking, kill the slot tool mid-conversation, show the retry and then the human handoff, then resume the same conversation id after a restart (state survives). Show `/metrics` and the CI eval report.

## CV bullets this project must live up to
- Python backend for a dealership service assistant: ingestion of synthetic workshop manuals and price lists into Qdrant embeddings, dense + keyword retrieval with a context budget, and a LangGraph agent that drafts appointment and cost-estimate answers with state persisted in Postgres, retries, and human handoff on tool errors.
- Evaluation and monitoring: a labelled question set scores retrieval recall and answer groundedness (hallucinations, RAGAS) in CI; every request logs latency, tokens, and cost, and a weekly comparison of eval scores flags drift.

If something is cut while building, update these bullets in `_work/cv.tex`. When done, mark it `built` in `profile/master-profile.md`; then real numbers may go on the CV and the project may be used in the cover letter.

Also: the CV lists **LLM Gateway** (brief: `applications/2026-10-14_accenture_junior-applied-ai-engineer/_work/project-brief-llm-gateway.md`). For HAIAR the CV bullets are slightly shorter (no TypeScript dashboard claimed): "Provider-agnostic API layer over multiple LLM provider APIs with token budgets, streaming, timeouts, retries, and fallback between providers, logging latency, token usage, and cost for every request." / "Metrics endpoint for cost per request, latency percentiles, and eval pass rate; tests and eval run in CI."
