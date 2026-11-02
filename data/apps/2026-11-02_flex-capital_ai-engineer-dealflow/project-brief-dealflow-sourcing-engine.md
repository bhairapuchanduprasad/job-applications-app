# Project brief: Dealflow Sourcing Engine (FLEX Capital; variant of Client Occasion Engine)

Base pattern: applications/2026-10-25_bestandsfaktor_founding-software-engineer/_work/project-brief-client-occasion-engine.md (trigger/rule layer, prioritisation, LLM-drafted messages, integration adapter, event log, CI). Reuse its architecture.

## Goal
A small, working sourcing tool that fills a deal-origination funnel with DACH software Mittelstand targets, ranks them, detects intent signals and drafts first outreach, with measurable hit quality.

## Why it matters for this JD
Proves: own AI tool with Python + LLM APIs + LangGraph, deployed with Docker on Azure; CRM data + data quality; screening/prioritisation logic with measured hit quality; automated enrichment; intent signals; outreach drafts; funnel dashboard; Pipedrive integration.

## Scope (1–2 days)
- Data: synthetic CSV of ~300 DACH software companies (name, revenue band, employees, founding year, owner age/structure, website text snippets, job postings, news snippets). No scraping of real personal data.
- Enrichment step: derive firmographics + ownership flags (founder-owned, no PE yet) from the synthetic fields; data-quality checks (missing fields, duplicates, plausibility).
- Screening: hard rules (revenue €5–30M, profitable, software, DACH) + LangGraph agent that scores fit and extracts intent signals (succession topic, CFO hire, slowing hiring) from text snippets, with citations to the snippet.
- Labelled set (~40 companies marked relevant/not) → precision/recall of the ranking in CI (GitHub Actions).
- Pipedrive: sync top targets as organisations/deals into a free Pipedrive trial via its REST API (required: the CV says Pipedrive-Testkonto; if no trial is possible, change the CV bullet to "Pipedrive-Sync (Mock)" before submitting).
- Outreach: LLM drafts a German first message per target (owner-focused, no hype), validated for length and forbidden claims.
- Dashboard: Streamlit funnel (sourced → qualified → contacted → replied) and conversion per segment.
- Docker image; deploy to Azure Container Apps (required: the CV says Docker auf Azure).

## Tech stack
Python, LangGraph, LiteLLM (OpenAI + Claude), Postgres, Pipedrive REST API, Streamlit, pytest, GitHub Actions, Docker, Azure Container Apps.

## Milestones
1. Synthetic data + quality checks. 2. Rules + LangGraph scoring + labelled eval. 3. Pipedrive sync + outreach drafts. 4. Dashboard + Docker/Azure + README.

## Demo idea
3-minute video: load data → ranked list with reasons and intent signals → push to Pipedrive → draft message → funnel dashboard.

## CV bullet it must live up to (German CV)
- Sourcing-Tool für synthetische Software-Unternehmen im DACH-Mittelstand: Datenanreicherung (Firmographics, Eigentümerstruktur), Priorisierung mit Regeln und LLM-Bewertung inkl. Intent-Signalen, Sync der CRM-Daten in ein Pipedrive-Testkonto, LLM-Entwürfe für die Ansprache, Funnel-Dashboard; Prüfung der Datenqualität, Testset zur Trefferqualität in der CI, Docker auf Azure.

When built: mark `built` in profile/master-profile.md with real numbers; only then use it in cover letters.
