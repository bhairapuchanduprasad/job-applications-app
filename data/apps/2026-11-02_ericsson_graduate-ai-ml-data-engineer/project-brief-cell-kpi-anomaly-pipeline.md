# Project brief: Cell KPI Anomaly Pipeline (Ericsson Graduate AI/ML and Data Engineer)

## Goal
A small end-to-end data + ML pipeline on synthetic 5G cell performance counters that proves the stack the JD names: Kafka, REST + gRPC ingestion, PySpark ETL and feature engineering, SQL storage, PyTorch model, data quality, model monitoring, Docker, CI.

## Why it matters for this JD
Covers the gaps the work history leaves open: Kafka, gRPC, PySpark, model monitoring; plus "data pipelines using REST APIs, gRPC, and Kafka", "data quality and validation", "MLOps implementation and model monitoring". Telecom domain shows interest in networks.

## Scope (1–2 days)
- Generator: synthetic per-cell KPIs every minute (PRB utilisation, throughput, RRC connections, drop rate) for ~50 cells, with injected anomalies (outage, congestion, misconfiguration). Labels kept for evaluation.
- Ingestion: Kafka topic `cell-kpis` (Redpanda or Kafka in Docker Compose); a FastAPI REST endpoint and a small gRPC service (protobuf schema) that both publish into Kafka.
- ETL: PySpark job reads from Kafka (batch or structured streaming), validates (schema, ranges, missing values), writes rolling-window features to Postgres; data-quality report per run.
- Models: Isolation Forest baseline (scikit-learn) vs. a small PyTorch autoencoder; precision/recall on injected anomalies.
- Monitoring: log score distributions per run, simple drift check (PSI) and a Streamlit page.
- Tests: pytest for schema/validation + model smoke test, GitHub Actions.

## Tech stack
Python, Kafka (Redpanda), FastAPI, gRPC (grpcio), PySpark, Postgres, scikit-learn, PyTorch, Streamlit, Docker Compose, pytest, GitHub Actions.

## Architecture sketch
generator → (REST | gRPC) → Kafka → PySpark ETL + DQ checks → Postgres features → model scoring → anomalies table → Streamlit (KPIs, anomalies, drift).

## Milestones
1. Compose stack + generator + Kafka. 2. REST/gRPC producers. 3. PySpark ETL + DQ. 4. Models + eval. 5. Monitoring page + CI + README.

## README outline
Problem, architecture diagram, how to run (`docker compose up`), data schema, DQ rules, model results table, monitoring, limitations (synthetic data).

## Demo idea
2-minute video: start stack → inject outage → anomaly appears in dashboard with its cell and KPIs.

## CV bullets it must live up to
- Data pipeline for synthetic 5G cell performance counters: Kafka producer and consumer, ingestion via REST and gRPC endpoints, PySpark ETL with feature engineering, data quality and validation checks, features stored in Postgres.
- Anomaly detection with an Isolation Forest baseline vs. a small PyTorch autoencoder, model monitoring of prediction drift, Docker Compose setup and pytest in GitHub Actions.

When built: add to profile/master-profile.md as `built` with real numbers; only then use it in cover letters.
