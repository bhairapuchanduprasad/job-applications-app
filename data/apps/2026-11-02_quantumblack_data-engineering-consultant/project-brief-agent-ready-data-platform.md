# Project brief: Agent-Ready Data Platform (QuantumBlack; variant of Semantic Analytics Agent)

Base: applications/2026-10-26_rewe-group_agentic-bi-developer/_work/project-brief-semantic-analytics-agent.md (dbt models, approved views, LangGraph analysis agent, golden questions, Langfuse). AltaSigma variant adds PySpark: applications/2026-10-28_altasigma_ai-engineer/_work/project-brief-semantic-analytics-agent.md.

## Why it matters for this JD
Covers the data-platform gaps: Spark, dbt, Snowflake, Terraform, CI/CD for data workflows, automated agent evaluation with Langfuse, structured + unstructured data.

## Scope (1–2 days)
- Structured path: synthetic retail CSVs → PySpark ingestion/cleaning → dbt models + dbt tests on Snowflake (trial) with DuckDB fallback for local runs.
- Unstructured path: synthetic product/policy documents → chunking → embeddings → pgvector.
- LangGraph analytics agent: SQL only on approved dbt views + vector search over docs, answers with sources.
- Terraform: Snowflake warehouse/db/roles (Snowflake provider) or the cloud resources used; plan/apply in CI with approval.
- GitHub Actions: dbt build + tests, pytest, agent eval on a golden-question set; Langfuse traces and scores.

## CV bullets it must live up to
- Batch pipeline on synthetic retail data (PySpark ingestion, dbt models and tests on Snowflake with a DuckDB fallback) plus an unstructured-document path (chunking, embeddings generation, pgvector search) feeding a LangGraph analytics agent.
- Terraform for the cloud resources, CI/CD for data workflows in GitHub Actions, and automated agent evaluation with a golden-question set and Langfuse traces.

When built: mark `built` in profile/master-profile.md with real numbers; only then use it in cover letters.
