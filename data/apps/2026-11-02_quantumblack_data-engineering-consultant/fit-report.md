# Fit report: QuantumBlack, AI by McKinsey, Data Engineering Consultant, Düsseldorf

Source: https://www.linkedin.com/jobs/view/4423060815 (found by job-scout 2026-11-02)
Language: English posting; asks "Strong communication skills ... in German and English" (no level) → English documents; German B1 flagged.
Seniority: Entry level, 2+ years building and deploying data solutions.

## Fit score: 62 / 100
The GenAI side of the JD (data prep for LLM systems, embeddings, vector search, LangChain, agent evaluation, coding agents) fits the Kniit/Covestro work closely. The classic data-platform side (Spark, dbt, Databricks/Snowflake/BigQuery, Terraform, streaming) is not in the profile, and McKinsey's client-facing consulting plus German communication are further gaps.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| CS/Engineering degree | MSc AI, BTech Mech Eng + minor CS&E | ✅ |
| 2+ years building/deploying data solutions | 3 years | ✅ |
| Python + SQL, production-grade code across environments | Python everywhere; SQL/Postgres; deployments to AWS (CDK) and Azure | ✅ |
| End-to-end pipelines for agentic/GenAI: data prep, embeddings, vector search, integration (Spark, dbt, LangChain) | Kniit pipeline, embedding benchmark 1M+ chunks, vector DBs, LangChain ✅; Spark/dbt ❌ | 🟡 |
| System design, data storage, reliability (Databricks, Snowflake, BigQuery, PSQL) | Postgres, MongoDB, Neo4j ✅; Databricks/Snowflake/BigQuery ❌ | 🟡 |
| MLOps/LLMOps: CI/CD for data workflows, automated agent eval (LangSmith, Opik, Langfuse), IaC (Terraform) | GitLab CI/CD, RAGAS/PytrecEval automated eval ✅; Langfuse/LangSmith/Opik ❌; IaC = AWS CDK (not Terraform) 🟡 | 🟡 |
| Structured vs unstructured, streaming vs batch, AWS/Azure/GCP | Unstructured docs + structured DBs, batch ✅; streaming ❌; AWS + Azure ✅ | 🟡 |
| Autonomous work, time management | Sole developer, reports to CTO | ✅ |
| Client-facing / senior stakeholder (beneficial) | CTO reporting; Covestro AI consulting intern with business stakeholders | 🟡 |
| Coding agents (plus) | Claude Code, custom skills | ✅ |
| German + English communication | English business fluent; German B1 | 🟡/❌ |

## Gaps and honest framing
1. **Spark, dbt, Databricks/Snowflake, Terraform, Langfuse**: none in profile. Planned project "Agent-Ready Data Platform" (Semantic Analytics Agent variant) covers them; unbuilt → not proof.
2. **IaC**: AWS CDK is IaC; say "CDK", don't claim Terraform.
3. **German**: B1, stated.
4. **Consulting with external clients**: only internal stakeholders (Covestro).

## Red flags
- McKinsey process is case-interview heavy; travel to client sites likely (user is fully willing to travel).
- Earlier QuantumBlack posting (Data Science Consultant, 4291654028) was skipped as unreadable; no prior QuantumBlack application.

## Company research (hooks)
- QuantumBlack is McKinsey's AI arm; QuantumBlack Labs builds internal tools and open-source projects such as Kedro, a Python framework for reproducible data and ML pipelines (well known; not re-verified this run, letter mentions Kedro only as something to learn).
- Posting: Data Engineering community in Germany, cross-functional agile teams with data scientists and ML engineers, R&D initiatives on agentic systems.

## Projects on the CV
- Agent-Ready Data Platform (planned; variant of Semantic Analytics Agent). Brief: project-brief-agent-ready-data-platform.md → build-first.
