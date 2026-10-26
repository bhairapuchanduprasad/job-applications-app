# Project brief: Semantic Analytics Agent (Agentic BI over a semantic layer)

Repo slug: `semantic-analytics-agent` (no link on the CV). Status: **planned**. Created for the REWE Group Agentic BI Developer application (2026-10-26).
Time box: 1–2 days with Claude Code.

## Goal
A business user asks "Wie hat sich der Umsatz pro Filiale in der Region West im letzten Quartal entwickelt?" and an analysis agent answers from governed data only: it reads metric definitions from a semantic layer, generates SQL against approved views, respects row-level security per user, and shows its query. Synthetic grocery-retail data.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "semantische Datenmodelle ... Semantic Views, Business Rules, Ontologien, Knowledge Graphs" | dbt models + dbt semantic layer (metrics YAML) + a small SKOS/RDF KPI glossary (rdflib) linking business terms to metrics |
| "Bausteine, mit denen ... Analyse-Agenten ... erstellt werden" | Reusable LangGraph agent template + tool interface (`list_metrics`, `describe_metric`, `run_query`) |
| "Standards für Testing, Rollout und Betrieb ... Evaluation, Observability und LLMOps" | Golden question set with expected results, eval in GitLab CI, Langfuse traces |
| "nur auf freigegebene Daten ... Row- und Column-Level Security" | Snowflake row access policy + masking policy (or DuckDB views per role locally), agent runs with the user's role |
| "Snowflake, dbt, GitLab/CI/CD" | Snowflake trial (30 days) or DuckDB fallback; dbt-core; GitLab CI |

## Scope
In: synthetic data (stores, regions, products, daily sales ~100k rows); dbt staging + marts + 6 metric definitions (Umsatz, Bons, Warenkorbwert, Abschriften ...); SKOS glossary with synonyms (e.g. "Umsatz" = "Netto-Umsatz"); LangGraph agent (resolve term → metric → SQL → validate → answer with query shown); RLS/masking for 2 roles (region manager West, central controlling); 25-question golden set (incl. 3 forbidden-data questions that must be refused); Langfuse tracing; GitLab CI running dbt tests + eval.
Out: dashboards, production auth, real REWE data.

## Tech stack
Python 3.12, dbt-core (+ dbt-snowflake / dbt-duckdb), Snowflake trial, rdflib (SKOS), LangGraph, LiteLLM, Langfuse, pytest, GitLab CI.

## Milestones
1. Data + dbt models + metrics (3 h) 2. SKOS glossary + metric lookup tools (2 h) 3. Agent + SQL validation (3 h) 4. RLS/masking per role (2 h) 5. Golden set + CI eval + traces (3 h) 6. README with architecture diagram, "how to build a new analysis agent" template guide (1 h).

## README outline
Problem · Architecture (semantic layer → tools → agent) · Governance (roles, policies, refusals) · Evaluation results table · Template guide · Limits.

## Demo idea
Same question asked as two roles: region manager sees only West; controlling sees all; forbidden question refused, with Langfuse trace.

## Exact CV bullets it must live up to (German)
- Analyse-Agent mit LangGraph, der Fachfragen über einen Semantic Layer beantwortet: Kennzahlendefinitionen in dbt, Fachbegriffe als SKOS/RDF-Glossar, SQL nur auf freigegebenen Views in Snowflake.
- Row- und Column-Level Security je Rolle, Golden-Question-Set mit erwarteten Ergebnissen als Evaluation in GitLab CI, Tracing mit Langfuse.
