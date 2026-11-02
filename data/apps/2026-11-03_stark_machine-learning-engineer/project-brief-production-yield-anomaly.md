# Project brief: Production Yield & Anomaly Pipeline (Plant Maintenance Agent variant, no GenAI)
Repo slug: production-yield-anomaly. Status: planned. For: STARK Machine Learning Engineer (2026-11-03).

## Goal
End-to-end MLOps on simulated manufacturing data: pipelines from MES/ERP-style sources, a yield prediction model on the line, an anomaly model on back-office financial postings, served, monitored for drift and retrained.

## Why for this JD
Proves data pipelines from MES/ERP, ML from experiment to production, serving, monitoring, drift detection, retraining workflows, model versioning, Python, SQL, scikit-learn, PyTorch, Airflow, dbt, documentation.

## Scope (1–2 days)
- Simulated MES data (stations, cycle times, test results per unit) + ERP data (material batches, suppliers) + finance postings with injected anomalies.
- Airflow DAG (local, Docker) → Postgres; dbt models for features (rolling station stats, supplier batch quality).
- Yield model: XGBoost vs logistic baseline; small PyTorch MLP comparison; MLflow tracking + model registry.
- Finance anomalies: Isolation Forest vs rules at a fixed alert budget.
- Serving: FastAPI endpoint loading the registered model; Docker.
- Monitoring: PSI drift per feature, prediction distribution; retraining DAG triggered by drift threshold.
- Docs: pipeline, feature definitions, model card, deployment config.

## Milestones
1. Data simulation + Airflow + dbt. 2. Models + MLflow. 3. Serving. 4. Drift + retraining. 5. Docs + README.

## Demo
Inject a supplier batch shift → drift alert → retraining DAG → new model version promoted.

## CV bullets it must live up to
- Airflow + dbt pipelines from simulated MES and ERP data into Postgres; XGBoost yield prediction vs baseline and Isolation Forest for anomalies in finance postings, tracked and versioned in MLflow.
- FastAPI model serving in Docker with drift detection (PSI) that triggers a retraining workflow; documented features, model card and deployment configuration.
