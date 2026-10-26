# Project brief: Plant Maintenance Agent (INSTATIQ variant)

Repo slug: `plant-maintenance-agent` (no link on the CV)
Status: **planned**. Build before submitting the INSTATIQ application.
Base brief (Siemens Advanta variant, Snowflake + dbt + Claude Agent SDK + Microsoft Foundry): `applications/2026-10-21_siemens-advanta_consultant-ai-new-technologies/_work/project-brief-plant-maintenance-agent.md`. Build one repo that satisfies both: the INSTATIQ variant needs a **trained + evaluated ML anomaly model** and a **FastAPI + Docker** service layer; the Snowflake/dbt/Foundry parts from the Siemens brief are optional extras.

## Goal
Predictive-maintenance proof of concept for a mobile construction machine (concrete pump / 3D concrete printer style). Simulated sensor data (pump pressure, hydraulic oil temperature, vibration, boom position) in an OPC UA-style tag model; an ML model detects anomalies; a GenAI assistant for machine operators uses RAG over machine manuals; an agent links a detected anomaly to the right manual section and proposes a maintenance action for the operator to confirm.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Machine-Learning-Lösungen ... Predictive Maintenance, Anomalieerkennung" | Anomaly model (Isolation Forest + XGBoost on rolling features) trained and evaluated on injected faults |
| "Training, Evaluierung und Einsatz von ML-Modellen" | Train/test split by time, precision/recall per fault type, model served via FastAPI |
| "GenAI-Anwendungen ... Chatbots, Assistenzsysteme, RAG" | Operator assistant: RAG over manuals with cited sections |
| "AI-Lösungen in IT- und OT-Systeme integrieren" | OPC UA-style tag model (asset → component → tag); README sketches how it would read from a real OPC UA server |
| "Proof of Concepts und MVPs" | 1–2 day PoC with a small Streamlit operator view |
| "Integration von AI-basierten Services" | FastAPI services (`/anomalies`, `/ask`, `/propose`) in Docker Compose |

## Scope (1–2 days)
In:
- Simulator: 3 machines, 4 sensors each, 30 days at 1-min resolution with injected faults (pump wear → pressure ripple, overheating oil, bearing vibration drift, blocked line → pressure spike).
- Features: lag + rolling mean/std/z-score windows (same method as the Covestro work).
- Models: Isolation Forest (unsupervised baseline) and XGBoost classifier on labelled faults; time-based split; report precision/recall per fault.
- Manuals: 3 short machine manuals (write your own), chunked + embedded (pgvector or Qdrant).
- Agent (LangGraph): anomaly tool + manual retrieval tool → proposed action with sources → operator confirms.
- FastAPI + Docker Compose; pytest + 15 fault-scenario eval in GitHub Actions.
Out: real OPC UA server, PLC integration, production UI.

## Architecture
```
sensor simulator ─► features (rolling windows) ─► anomaly model (IsolationForest / XGBoost) ─► /anomalies
manuals ─► chunks + embeddings ─► retrieval ─► /ask (operator assistant, cited)
LangGraph agent: anomaly + manual section ─► /propose (maintenance action) ─► operator confirms (Streamlit)
CI: pytest + model metrics + 15 fault-scenario eval
```

## Milestones
1. Simulator + features (≈2 h)
2. Models + evaluation report (≈3 h)
3. Manuals + RAG assistant (≈2 h)
4. Agent + FastAPI + Docker (≈3 h)
5. Eval in CI + README (architecture, OT notes, results) (≈2 h)

## README outline
Problem, data simulator, feature + model choices, results table, assistant demo, OT integration notes, limits.

## Demo idea
Streamlit: sensor chart with the anomaly flagged → "Why?" opens the cited manual section → proposed action with Confirm button.

## CV bullets this project must live up to (German CV)
- Predictive-Maintenance-PoC für eine mobile Baumaschine: simulierte Sensordaten (Pumpendruck, Hydrauliköltemperatur, Vibration) in einem OPC-UA-ähnlichen Tag-Modell; Modell zur Anomalieerkennung trainiert und an eingespielten Fehlerszenarien evaluiert.
- GenAI-Assistenzsystem für Maschinenbediener: RAG über Maschinenhandbücher, ein Agent verknüpft erkannte Anomalien mit der passenden Handbuchstelle und schlägt eine Wartungsmaßnahme zur Bestätigung vor; FastAPI-Services in Docker, Evaluierungsset in CI.

When built, mark it `built` in `profile/master-profile.md`; then real results may go on the CV.
