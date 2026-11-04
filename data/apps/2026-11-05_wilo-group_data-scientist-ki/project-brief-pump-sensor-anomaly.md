# Project brief: Anomalieerkennung auf Sensor-Zeitreihen (Plant Maintenance Agent / Stark variant)
Repo slug: pump-sensor-anomaly. Status: planned. For: Wilo Data Scientist KI (2026-11-05). No new scope beyond the existing Stark "Production Yield & Anomaly Pipeline" brief (applications/2026-11-03_stark_machine-learning-engineer/_work/project-brief-production-yield-anomaly.md).

## Goal
Anomaly detection and failure prediction on simulated pump/plant sensor time series, tracked and served like a production model.

## Why for this JD
Proves Zeitreihenanalyse, Explainable AI, MLflow, Docker/CI/CD, Modellüberwachung, Datenqualität.

## Scope (1–2 days)
- Simulated sensor data (flow, pressure, vibration, power) with injected faults and drift; data quality checks.
- Statistical baseline vs Isolation Forest vs XGBoost; SHAP explanations.
- MLflow tracking + registry; FastAPI in Docker; PSI drift monitoring; pytest + CI.

## CV bullet it must live up to
- Anomalieerkennung auf simulierten Anlagen-Sensordaten: statistische Baseline vs. Isolation Forest vs. XGBoost, Datenqualitätsprüfung, Erklärbarkeit (SHAP), MLflow-Versionierung, FastAPI-Dienst in Docker mit Drift-Monitoring und CI/CD.

README outline: problem, data simulation, models, explainability, serving, monitoring. Demo: API returns anomaly score + top SHAP features.
