# Project brief: Semantic Analytics Agent, AltaSigma variant (lakehouse + own MCP server)

Repo slug: `semantic-analytics-agent` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-26_rewe-group_agentic-bi-developer/_work/project-brief-semantic-analytics-agent.md). Created for AltaSigma AI Engineer (2026-10-28). Time box: 1–2 days with Claude Code.

## Goal
An agent answers business questions over lakehouse data through its own MCP server: a PySpark job lands synthetic sales data as Delta Lake tables, the MCP server exposes approved SQL views plus a small business glossary graph, and a LangGraph agent picks metrics, writes SQL, validates it and answers with the query shown.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "PySpark und moderne Lakehouse-Formate wie Delta oder Iceberg" | PySpark ingest + cleaning job writing Delta tables (delta-spark, local) |
| "eigene MCP Server ... per SQL ... mit Quellsystemen sprechen" | FastMCP server: `list_metrics`, `describe_metric`, `run_sql` (read-only, approved views via DuckDB delta extension) |
| "Knowledge Graphen oder andere Indizierungsmethoden" | SKOS/RDF glossary (rdflib) linking business terms to metrics |
| "Modelle ... mit systematischem Benchmarking" | golden-question set, two models compared via LiteLLM on accuracy, cost, latency |
| "Robustheit, Evaluation und Betrieb" | SQL validation + refusal of forbidden data, eval in GitHub Actions CI, Docker |

## Scope (cut to 1–2 days)
In: ~100k synthetic sales rows; PySpark job → Delta (bronze/silver); 6 metrics; glossary; FastMCP server; LangGraph agent; 25 golden questions (3 must be refused); model benchmark table in README; Docker Compose; GitHub Actions.
Out: Iceberg, real auth, UI.

## Tech stack
Python 3.12, PySpark + delta-spark, DuckDB (delta extension), FastMCP, rdflib, LangGraph, LiteLLM, pytest, Docker, GitHub Actions.

## Milestones
1. Data + PySpark → Delta (3 h) 2. Views + glossary (2 h) 3. MCP server + tests (3 h) 4. Agent + SQL validation (3 h) 5. Golden set + benchmark + CI (3 h) 6. README + demo GIF (1 h).

## README outline
Problem, architecture diagram (Spark → Delta → DuckDB views → MCP → agent), how to run, eval results table, model benchmark, limits.

## Demo idea
Claude Code / agent asks "Umsatz pro Region im Q3?" via the MCP server; show SQL, answer, and a refused question.

## CV bullets it must live up to (German)
- PySpark-Job lädt synthetische Vertriebsdaten als Delta-Lake-Tabellen; ein eigener MCP-Server stellt freigegebene SQL-Views und ein Business-Glossar als Knowledge Graph (rdflib) für einen LangGraph-Agenten bereit.
- Golden-Question-Set mit Evaluation in GitHub Actions CI; Benchmarking zweier LLMs über LiteLLM nach Qualität, Kosten und Latenz.
