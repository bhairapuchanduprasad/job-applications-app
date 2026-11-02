# Project brief: Advisory Data Layer & Booking Agent (Semantic Analytics Agent variant)
Repo slug: advisory-data-layer. Status: planned. For: Vogel Founding Engineer (2026-11-03).

## Goal
A tiny version of Vogel's own software: nightly load of DATEV-style exports into an own data layer, figures defined once, and an agent that proposes bookings for recurring bank transactions with every decision traceable.

## Why for this JD
Proves data pipelines out of DATEV-like systems, relational modelling, "define every figure once", agents with a hard line between model judgment and deterministic calculation, traceability (version, source, decision), evaluation against closed cases, a small interface advisors would use, Python + TypeScript.

## Scope (1–2 days)
- Synthetic data: 3 client firms, DATEV-style CSV exports (Buchungsstapel, SKR03 accounts), bank statements; one "closed year" with final bookings as ground truth.
- Nightly pipeline (Python, scheduled GitHub Action or cron) → Postgres; row-count and balance checks from day one.
- dbt models: one definition per KPI (revenue, personnel costs, liquidity), used by all reports.
- Booking agent: deterministic rules first (known counterparties, amounts, tax keys); LLM (LiteLLM) only for unmatched transaction texts, proposing account + tax key; every proposal stores rule/model version, source rows, reason.
- Evaluation on the closed year: accuracy per firm, share handled by rules vs model, wrong-proposal rate.
- Small TypeScript (Next.js) review screen: advisor accepts/rejects, decisions logged.

## Milestones
1. Data + pipeline + checks. 2. dbt metrics. 3. Rules + agent + trace table. 4. Eval on closed year. 5. Review screen + README.

## Demo
Run nightly load → open review screen → accept proposals → show trace for one decision and the eval table.

## CV bullets it must live up to
- Nightly Python pipeline from synthetic DATEV-style exports into a Postgres data layer with checks and dbt models that define each figure once; booking agent where deterministic rules handle known transactions and an LLM proposes accounts only for unmatched texts, each decision stored with version, source and reason.
- Evaluated against a closed accounting year (accuracy, rules vs model share, wrong proposals); TypeScript review screen for advisors to accept or reject proposals.
