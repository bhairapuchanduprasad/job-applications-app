# Project brief: Text2SQL Analytics Agent (Semantic Analytics Agent variant)
Repo slug: text2sql-analytics-agent. Status: planned. For: Databricks AI FDE, 2026-11-05.
## Goal
Proves Text2SQL, multi-agent (LangGraph), evaluation, Apache Spark/Delta Lake familiarity.
## Scope (1-2 days)
Synthetic retail data; PySpark job writes Delta tables (local Spark); approved SQL views only; LangGraph agent (plan, SQL, check, answer); 30 golden questions with expected results run in CI; DuckDB/Spark SQL execution.
## Milestones
1 data + Spark job, 2 views, 3 agent, 4 golden eval in CI, 5 README.
## Demo
Ask a business question, show generated SQL, result and eval pass rate.
## CV bullet it must live up to
Analysis agent (LangGraph) that turns business questions into SQL on approved views over synthetic retail data in Delta tables written by an Apache Spark (PySpark) job, with a golden-question eval set run in CI.
