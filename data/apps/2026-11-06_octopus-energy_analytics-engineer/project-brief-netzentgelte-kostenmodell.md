# Project brief: Netzentgelte-Kostenmodell (dbt + Airflow)
**Goal:** ELT pipeline modelling direct energy costs (grid fees, levies, taxes) with effective-date versioning and a simple forecast.
**Why for Octopus Energy Analytics Engineer:** proves dbt, Apache Airflow, SQL, data quality, regulatory-change handling, forecasting.
**Scope (1-2 days), synthetic data only:**
- Seeds: synthetic tariff/charge tables per component with valid_from/valid_to (no real regulatory numbers claimed).
- Postgres via Docker Compose; dbt project: staging, intermediate (effective-dated joins), marts (cost per kWh by component/customer segment), dbt tests (not_null, unique, accepted ranges, no overlapping validity periods).
- Airflow DAG: load seeds, dbt run, dbt test, forecast task.
- Forecast: simple per-component model (e.g. Prophet or linear trend) reflecting a changed levy from its effective date.
**Milestones:** compose + seeds; dbt models + tests; Airflow DAG; forecast + README with lineage diagram.
**Demo:** change a levy row, rerun DAG, show updated mart and forecast.
**CV bullet it must live up to:** ELT pipeline for Netzentgelte, Umlagen, Steuern with dbt models (staging, marts, tests, versioned validity periods), Airflow orchestration, Postgres, simple forecast model.
