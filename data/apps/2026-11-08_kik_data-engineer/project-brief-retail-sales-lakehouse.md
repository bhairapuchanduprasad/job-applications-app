# Project brief: Retail Sales Lakehouse (planned)
Repo slug: `retail-sales-lakehouse`. For KiK Data Engineer (2026-11-08). No link on CV until built.

## Goal
Medallion (bronze/silver/gold) pipeline on Databricks (Free Edition) for synthetic retail data.
## Why for this JD
Proves Databricks, PySpark, ELT, data modelling, data quality checks, pipeline tests, CI/CD.
## Scope (1-2 days)
- Synthetic generator: stores, articles, orders (CSV, JSON, Parquet).
- Bronze ingest (Auto Loader or batch), silver cleaning/conformance, gold sales-by-store/article model.
- Data quality: expectations (null, uniqueness, ranges), quarantine table, run report.
- pytest on transformation functions with local PySpark; GitHub Actions; Databricks Asset Bundle for deployment.
## Stack
Databricks, PySpark, Delta Lake, SQL, pytest, GitHub Actions.
## Milestones
1 generator + bronze; 2 silver + DQ; 3 gold + tests; 4 CI/bundle + README.
## README outline
Problem, architecture, data model, DQ rules, how to run, next steps.
## Demo idea
Inject bad rows, show quarantine table and DQ report, gold tables updating.
## CV bullet it must live up to
Medallion pipeline (bronze, silver, gold) on Databricks: PySpark ELT of synthetic store and sales data into Delta tables, automated data quality checks, pytest tests and CI.
