# Project brief: Client Occasion Engine (Zurich variant)

Base brief: `applications/2026-10-25_bestandsfaktor_founding-software-engineer/_work/project-brief-client-occasion-engine.md` (status: planned). Build the base scope, plus the additions below for Zurich's Data Scientist & AI Solution Expert (Commercial Insurance).

## Why it matters for Zurich
Covers the insurance-domain gap and JD items "Risikobewertung", "Portfolio-Analysen", "intelligente Datenprodukte ... Datamarts und Data Pipelines", "gesamter ML-Lifecycle", "Datenqualität, Schnittstellen".

## Additions to the base scope (≈ +0.5 day)
1. Commercial flavour of the synthetic portfolio: add SME clients (Betriebshaftpflicht, Inhalts-/Gebäudeversicherung, Betriebsunterbrechung) with revenue, sector, location.
2. **XGBoost risk model**: label synthetic clients as "underinsured / coverage gap" via a hidden generator rule plus noise; train XGBoost on portfolio features, compare with the YAML rules baseline (precision/recall at a fixed review budget), SHAP top reasons per client.
3. ML lifecycle in small: train script → saved model with version tag → `/score` endpoint in the FastAPI service → per-model monitoring next to the per-rule metrics (score distribution drift between runs).
4. Data quality checks on the synced data (nulls, impossible sums insured) before scoring.
5. README section "Use-case canvas": problem, business impact estimate, feasibility, risks, in plain German and English, so it doubles as an ideation example.

## Stack
Python, FastAPI, Postgres, XGBoost, SHAP, Pydantic, LiteLLM, pytest, Docker, GitHub Actions.

## CV bullet it must live up to
- Aufbau eines Datenprodukts über einem synthetischen Gewerbekundenbestand: REST-Schnittstelle zu einem simulierten Bestandssystem, Postgres mit Datenqualitätsprüfungen, XGBoost-Modell zur Risikobewertung von Unterversicherung und Deckungslücken im Vergleich zu Regeln, Priorisierung der nächsten Aktion, validierte LLM-Entwürfe für Kundennachrichten, Monitoring je Regel und Modell, pytest und gelabeltes Testset in der CI.
