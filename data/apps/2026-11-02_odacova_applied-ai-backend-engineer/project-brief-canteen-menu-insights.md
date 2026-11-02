# Project brief: Canteen Menu Insights (status: planned, build before submitting to odacova)

## Goal
A small, honest Python backend in odacova's domain (canteen menus + nutrition) that proves the JD's 50/50 split: Python backend + REST APIs + data model, and applied AI (own ML model + LLM API for reporting). Synthetic data only, no health data of real people.

## Why it matters for this JD
- Proves: REST-APIs, Datenmodellierung, Anbindung externer Schnittstellen, eigene ML-Modelle auf domänenspezifischen Daten, Integration von LLM-APIs, KI-gestützte Reporting-Funktionen, automatisierte Tests, CI/CD, Deployment.
- Closes nice-to-have gaps: Firestore / Firebase, Google Cloud (Cloud Run, serverless).

## Scope (1–2 days)
1. Synthetic data generator: 3 canteen sites, 8 weeks of menus (dishes with recipe ingredients and Big-7 nutrient values), daily orders per dish with weekday/season/weather-like noise.
2. Import endpoint: POST recipes/nutrient data (JSON, like an ERP export) → validated with Pydantic → stored in Firestore (emulator locally).
3. Data model in Firestore: sites, dishes, menus (date → dishes), orders. Document the model in the README.
4. Demand model: XGBoost per-dish daily demand vs naive baseline (same weekday last week); report MAE on a held-out final 2 weeks.
5. REST API (FastAPI): /menus, /dishes/{id}, /forecast?site&date, /report?site&week.
6. LLM report: /report builds weekly KPIs (orders, top dishes, avg nutrient profile) and has an LLM (via LiteLLM) write a short German summary; a check verifies every number in the text matches the KPI table, otherwise falls back to a template.
7. Tests: pytest for import validation, forecast endpoint, report number check (LLM mocked). GitHub Actions runs tests on every push.
8. Docker image deployed to Google Cloud Run (free tier) with Firestore in native mode; structured request logging.

## Tech stack
Python 3.12, FastAPI, Pydantic, google-cloud-firestore (+ emulator), XGBoost, pandas, LiteLLM, pytest, Docker, GitHub Actions, Google Cloud Run.

## Architecture sketch
synthetic generator → import API → Firestore ← FastAPI service (forecast: XGBoost model artefact; report: KPI query → LLM → number check) → Cloud Run

## Milestones
- M1 (half day): data generator, Firestore model, import endpoint + tests.
- M2 (half day): XGBoost vs baseline, forecast endpoint.
- M3 (half day): KPI report + LLM summary + number check.
- M4 (half day): Docker, GitHub Actions, Cloud Run deploy, README.

## README outline
Problem, data model diagram, API table, model results (real numbers from the run), report example, how to run locally (emulator), deployment, limits.

## Demo idea
curl the import endpoint with a new menu, request a forecast, then the weekly German report for one site.

## CV bullet it must live up to
"Python-Backend mit REST-APIs und Datenmodell in Firestore über synthetischen Kantinen-Speiseplänen, eigenes XGBoost-Modell zur Nachfrageprognose je Gericht und eine LLM-gestützte Reporting-Funktion mit Prüfung gegen die Kennzahlen; pytest in GitHub Actions (CI/CD), Docker-Deployment auf Google Cloud Run."
