# Variant brief: Cell KPI Anomaly Pipeline as "Kubernetes Data Pipeline Lab" (adesso Cloud Native Data Engineer)
Base brief: applications/2026-11-02_ericsson_graduate-ai-ml-data-engineer/_work/project-brief-cell-kpi-anomaly-pipeline.md

**Goal:** show Kafka, Spark, Airflow, Kubernetes, Helm on a small, reproducible data platform.
**Scope (1-2 days):** synthetic cell KPI stream -> Kafka (Docker/kind) -> PySpark ETL with data-quality checks -> Postgres; Airflow DAG orchestrating the batch job and a daily quality report; everything packaged as a Helm chart and deployed to a local kind cluster (Secrets for credentials); GitLab/GitHub Actions CI building images and running `helm lint`; ArgoCD sync optional.
**Milestones:** 1) Kafka producer/consumer; 2) PySpark ETL + checks; 3) Airflow DAG; 4) Dockerfiles + Helm chart; 5) kind deploy + CI; 6) README with architecture diagram.
**CV bullets it must live up to:** Kafka-Streaming, PySpark-ETL mit Datenqualitätsprüfungen, Airflow-Orchestrierung, Deployment per Helm-Chart auf Kubernetes (kind), CI/CD. No metrics claimed.
