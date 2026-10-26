# Application notes: REWE Group, Agentic BI Developer - Semantic Layer & AI Analytics (Köln)

Status: **build-first**. Build `semantic-analytics-agent` (brief in this folder) before submitting; the CV describes it.
Submit via the LinkedIn posting / jobs.rewe-group.com (Job-ID 982670): https://www.linkedin.com/jobs/view/4475517466. German documents (confident German expected, you have B1).
Related: you also applied to REWE digital (Platform Engineer KI-Plattform, 2026-10-24); mention it if asked, different unit.

## Likely interview questions
1. **"Wie würden Sie einen Semantic Layer für Analyse-Agenten aufbauen?"** Metric definitions in one place (dbt semantic layer), business glossary/ontology mapping terms → metrics, agent tools that only query approved views, eval set of business questions. Kniit KG + MCP is the closest real experience; the project once built.
2. **"Wie stellen Sie sicher, dass Agenten nur freigegebene Daten sehen?"** Run queries with the user's role (row access/masking policies), no free SQL on raw tables, refusals tested in the eval set, audit logs. Honest: not done in production yet.
3. **"Wie testen und betreiben Sie Agenten (LLMOps)?"** Golden questions with known answers in CI (thesis: RAGAS/PytrecEval automation; Kniit P/R 33/45 → 93/90), traces, cost per question.

Also prepare: Snowflake/dbt basics, RDF/OWL/SKOS vs property graphs (Neo4j), why leave Kniit (public line), answering in German.

## Form fields
- **Why REWE Group:** Analytics serves 40+ business units with ~8M receipts/day from 6,500 stores; building the semantic foundation for agents in a new team from day one.
- **Gehaltsvorstellung:** 70.000 € brutto/Jahr (range 60–75k), only if asked.
- **Frühester Eintritt:** 15. November 2026.
- **Arbeitserlaubnis:** Blaue Karte EU.
- **Deutsch:** B1 (no certificate).
