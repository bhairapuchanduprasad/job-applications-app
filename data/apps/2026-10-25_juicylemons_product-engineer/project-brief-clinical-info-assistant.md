# Project brief: Clinical Info Assistant

Repo slug: `clinical-info-assistant` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the JuicyLemons (Berlin AI healthcare startup) Product Engineer application.
Time box: 1–2 days with Claude Code.

## Goal
A small web app that answers questions about medicines from public product information (synthetic or public-domain drug label texts, e.g. a handful of openFDA/EMA-style leaflets), with two user journeys:
- **Healthcare professional view:** precise answer with dosage/interaction detail and citations to the exact label section.
- **Patient view:** the same source, rewritten in plain language, with a clear "ask your doctor or pharmacist" handoff when the question is about personal treatment.

Every answer shows its sources. Users can rate an answer or mark "didn't help". The app records simple usage events (question asked, source opened, answer rated, journey abandoned) and shows a small funnel view, so you can point at a friction point and the change you made because of it.

This mirrors the client's product at toy scale: AI that changes how medical information reaches HCPs and patients, built with product thinking (journeys, friction, data).

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Build and improve the web application powering an AI-driven healthcare product" | Full web app, React + FastAPI, LLM answers over medical label texts |
| "Identify friction in user journeys … better workflows" | Two journeys (HCP vs patient), rating + "didn't help" flow, one documented UX change |
| "Use data and user behavior to inform prioritization" | Event log (Postgres) + funnel view; README section "what the data told me" |
| "Experience across modern frontend and backend web development" / "Python and modern JavaScript framework" | React + TypeScript frontend, Python/FastAPI backend |
| "Write clean, tested, maintainable code" | pytest for API + retrieval, Vitest/React Testing Library for the UI, GitHub Actions CI |
| "Contribute to architecture decisions" | Short ADRs in `docs/adr/` (retrieval approach, where audience rewriting happens) |
| "Experience with AI/ML-driven products" | RAG with citations, answer grounding check, small eval set |
| "Cloud experience" | Docker image; optional deploy to Azure Container Apps or AWS |
| "Side projects … that demonstrate your product thinking" | The project itself + README framed as a product write-up |

## Scope (keep it small)
In:
- 5–10 public-domain or synthetic drug label texts, chunked by section (indications, dosage, contraindications, interactions, side effects).
- FastAPI: `POST /ask` (question, audience = hcp|patient) → answer + cited sections; `POST /events`; `GET /funnel`.
- Retrieval: embeddings + a small vector store (pgvector in Postgres, or Qdrant), section-aware.
- LLM via LiteLLM (any provider). Audience-specific prompt; grounding check: answer must cite at least one retrieved section, else "I can't answer that from the label".
- Safety rule: questions about personal treatment in patient view → fixed handoff text.
- React + TypeScript UI: journey switch, question box, answer with expandable sources, rating buttons.
- Events table + funnel page (asked → opened source → rated helpful).
- Eval: 20–30 labelled questions (expected section + must-contain facts); `make eval` reports citation hit rate and grounding failures; runs in CI.
- Tests: pytest (API, retrieval, grounding check), Vitest for 2–3 UI components. GitHub Actions.
- Docker Compose (api, web, postgres).
Out: auth, real patient data, medical-device claims, production deployment.

## Architecture
```
React + TS (HCP | patient journey) ──► FastAPI /ask ──► retriever (pgvector) ──► LiteLLM (audience prompt)
        │                                   │                                        │
        │                                   └──── grounding check (citations) ◄──────┘
        └──► /events ──► Postgres events ──► /funnel ──► funnel view
eval/ (labelled questions) ──► make eval ──► CI (GitHub Actions) + pytest + Vitest
```

## Milestones
1. Data prep + chunking by section + retrieval with tests. (≈2.5 h)
2. `/ask` with audience prompts, citations, grounding check, handoff rule. (≈3 h)
3. React + TS UI with both journeys and source display. (≈3 h)
4. Events + funnel page. (≈1.5 h)
5. Eval set + CI (pytest, Vitest, eval). (≈2 h)
6. Use it yourself / with 2–3 friends, change one thing based on the funnel, write it up. README, screenshots, ADRs. (≈2 h)

## README outline
Problem (medical information is hard to find and hard to read) → Who it's for (HCP vs patient) → Demo GIF → Architecture + ADRs → Grounding and safety rules → Evaluation results → "What the usage data told me and what I changed" → Testing → Run locally → Limitations (not medical advice, sample labels only).

## Demo idea
Ask the same interaction question in HCP and patient view; show the different answers citing the same label section. Then ask "should I stop taking it?" in patient view and show the handoff. End on the funnel view and the one UX change it prompted.

## CV bullets this project must live up to
- Web app that answers questions about medicines from drug label texts, with separate journeys for healthcare professionals and patients, cited sources on every answer, and a handoff when a patient question needs a doctor.
- React and TypeScript frontend on a Python FastAPI backend with retrieval and a grounding check; usage events and a funnel view to find friction in the journeys; pytest, UI tests and a labelled eval set run in CI.

If something is cut while building, update these bullets in `_work/cv.tex`. When done, mark it `built` in `profile/master-profile.md`; then real results may go on the CV and the project may be used in the cover letter / interview.
