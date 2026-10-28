# Project brief: Plant Maintenance Agent (IABG data-analysis variant, shown on the CV as "Plant Maintenance Analytics")

Base briefs: `applications/2026-10-21_siemens-advanta_consultant-ai-new-technologies/_work/project-brief-plant-maintenance-agent.md` and the INSTATIQ variant `applications/2026-10-26_instatiq_applied-ai-engineer/_work/project-brief-plant-maintenance-agent.md` (status: planned). This variant drops the GenAI/agent parts and focuses on classic data analysis, which is what IABG's (Junior) Data Analyst role needs.

## Goal
A documented Python data-analysis pipeline for maintenance and repair of a simulated fleet of technical systems (civil, generic: e.g. 20 vehicles/aircraft-like units; no military data): integrate, clean and link operating, sensor and logistics data, detect anomalies, visualise results.

## Why it matters for IABG
JD: "Erschließung verschiedener Datenquellen ... Betrieb, Wartung und Instandhaltung", "Sichtung, Visualisierung, Bewertung, Verknüpfung und Bereinigung", "Integration in die bestehende Datenanalysepipeline", "Python-Programme einschließlich Dokumentation", "Code Reviews".

## Scope (1–2 days)
1. Generator for 3 messy sources: operating hours/flight-hour logs (CSV), sensor readings (Parquet, with drift and gaps), maintenance + spare-part events (Excel, inconsistent IDs and dates).
2. Pipeline (Pandas, pydantic/pandera checks): ingestion → cleaning (types, units, duplicates, ID mapping) → linking per unit/component → data quality report.
3. Analysis: rolling features; Isolation Forest + XGBoost (labelled injected faults) for anomaly/failure-risk; spare-part consumption per operating hour.
4. Streamlit dashboard: fleet overview, per-unit timeline, anomalies, data-quality page.
5. Engineering: package layout, docstrings + MkDocs page, pytest, GitHub Actions, at least 3 PRs with written review comments (self-review checklist).

## Stack
Python, Pandas, pandera, Scikit-Learn, XGBoost, Streamlit, pytest, MkDocs, GitHub Actions.

## CV bullet it must live up to
- Datenanalyse für Wartung und Instandhaltung einer simulierten Flotte technischer Systeme: Integration und Bereinigung von Betriebs-, Sensor- und Logistikdaten (Betriebsstunden, Wartungsereignisse, Ersatzteile) in eine Python-Datenanalysepipeline mit Datenqualitätsprüfungen, Anomalieerkennung (Isolation Forest, XGBoost auf gleitenden Features), Visualisierung in Streamlit, Dokumentation und Reviews über Pull Requests.
