# Project brief: Spin-off Ecosystem Data Hub (status: planned)

For: JUNI, Data & AI Engineer (applications/2026-11-03_juni_data-ai-engineer). Repo slug: `ecosystem-data-hub`. No link on the CV until built.

## Goal
A small "JUNI Core" lookalike: one Postgres data layer that joins a mock CRM with publication and patent data pulled from public APIs and scraping, resolves people/organisations across sources with rules → embeddings → LLM, and shows the source of every field.

## Why it matters for this JD
Covers the gaps: SaaS integration via APIs + webhooks with two-way sync, dedup and alerts; external data (publications, patents) via API/scraping; record linkage / entity resolution; matching evaluated against reference cases; DSGVO (consent, deletion periods, access); provenance ("Nutzer*innen sehen, woher ein Ergebnis kommt").

## Scope (1–2 days with Claude Code)
- Mock CRM: small FastAPI app (contacts, organisations) that sends webhooks on change and accepts updates back.
- Sync service: webhook receiver + periodic reconciliation, idempotent upserts (no duplicates), dead-letter table + alert (log/Slack webhook stub) on failed syncs.
- External data: OpenAlex API (publications, affiliations) for 2–3 Berlin/Brandenburg universities; patents from a small public sample (e.g. EPO/Google Patents export CSV). Plus a scraper (httpx + BeautifulSoup) for one public university spin-off/transfer page. Respect rate limits and robots.txt.
- Data model: `person`, `organisation`, `publication`, `patent`, `source_record`, `field_provenance(source, fetched_at)`, `consent`, `deletion_due`.
- Entity resolution: blocking + deterministic rules (ORCID, normalised email/name), embedding similarity (sentence-transformers) for candidates, LLM structured extraction/adjudication (LiteLLM, Pydantic output) only for unclear pairs.
- Evaluation: ~150 labelled pairs; precision/recall/F1 per stage, acceptable error rate defined per use case in `EVAL.md`; runs in GitHub Actions and fails below threshold.
- DSGVO: consent flag blocks enrichment; deletion job removes person + provenance after retention period; access log table.
- Small Streamlit view: entity page with per-field source and timestamp.

## Stack
Python, Postgres, pandas, FastAPI, SQLAlchemy, sentence-transformers, LiteLLM, Pydantic, pytest, GitHub Actions, Docker Compose, Streamlit.

## Milestones
1. Schema + mock CRM + webhook sync with idempotency tests.
2. OpenAlex + patent loaders, provenance on every write.
3. Matching cascade + labelled set + eval in CI.
4. DSGVO jobs, Streamlit entity page, README + demo GIF.

## README outline
Problem → architecture diagram → data model → sync guarantees → matching cascade + eval results → DSGVO design → how to run → what I'd do next.

## Demo idea
Change a contact in the mock CRM → webhook → hub updates → Streamlit entity page shows new value with source; then show the eval report.

## CV bullets it must live up to
- Central Postgres data model joining a mock CRM (two-way sync over REST APIs and webhooks, no duplicates, alerts on failed syncs) with publication and patent data pulled from public APIs and scraping, keeping a source and timestamp for every field so each result shows where it comes from.
- Entity resolution of people and organisations (rules, then embeddings, then LLM structured extraction for unclear cases) with a labelled reference set, precision/recall evaluation in GitHub Actions, and GDPR (DSGVO) consent and deletion handling built into the data model.
