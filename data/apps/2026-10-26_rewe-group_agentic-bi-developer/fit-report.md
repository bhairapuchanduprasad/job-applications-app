# Fit report: REWE Group, Agentic BI Developer - Semantic Layer & AI Analytics (m/w/d), Köln

**Fit score: 62/100.** Good match on agentic AI, knowledge graphs (Neo4j, GraphRAG, plus a hands-on RDF/OWL/SPARQL/Protégé project), Python, SQL, GitLab CI/CD and evaluation. Gaps: Snowflake + dbt and semantic-layer tooling (none), KPI definitions / data catalogs / metadata management (none), row-/column-level security and access models (none), "sicher in Deutsch" for stakeholder communication (B1), platform/framework thinking at group level.

Language: German posting, German communication with engineers and management required → German Lebenslauf + Anschreiben (rule 3), B1 flagged as top gap.
Not a duplicate: earlier application `applications/2026-10-24_rewe-digital_platform-engineer-ki-platform` is a different unit (REWE digital) and role.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Semantic data models, ontologies, knowledge graphs, business rules | Kniit knowledge graph (Neo4j, GraphRAG) built from regulatory docs; KG learning resource with Protégé, RDF, OWL, SPARQL | 🟡 (no BI semantic layer) |
| Make business context understandable for humans and AI | Kniit MCP service exposes the KG to AI agents; Expert Interface for domain experts | ✅ |
| Blueprints/building blocks for analysis agents | LangGraph multi-agent designs (Kniit, Covestro) | 🟡 |
| Standards for testing, rollout, operation incl. evaluation, observability, LLMOps | RAGAS/PytrecEval eval pipeline; P/R tracking; GitLab CI/CD; no observability tooling | 🟡 |
| Agents only on approved data: permissions, RLS/CLS | Not done | ❌ |
| Enablement of teams | Covestro AI consulting with stakeholders | 🟡 |
| Mehrjährige Erfahrung as SE/DE/ML/AI Engineer | 3 years | ✅ |
| Very good Python + SQL | Python ✅, SQL/Postgres ✅ | ✅ |
| Cloud + data platforms (Snowflake, dbt, GitLab CI/CD) | AWS/Azure, GitLab CI/CD; **no Snowflake/dbt** | 🟡 |
| KPI definitions, data models, metadata/catalogs | None | ❌ |
| Ontologies, taxonomies, KGs (RDF/OWL/SKOS, SPARQL) | RDF/OWL/SPARQL/Protégé project; Neo4j KG at Kniit | ✅ |
| Communicate securely in German and English | English fluent; **German B1** | ❌ (top gap) |

## Gaps and honest framing
1. **German (top gap):** B1, improving.
2. **Snowflake/dbt/semantic layer + RLS:** do not claim; new planned project "Semantic Analytics Agent" covers it on paper. Build first.
3. **KPI/metadata catalogs:** frame KG work as semantic modelling of a domain; do not claim BI experience.

## Project on the CV
New planned project **Semantic Analytics Agent** (`project-brief-semantic-analytics-agent.md`). Status planned → **build-first**.

## Red flags
- Builds a new team's framework from scratch: expects some platform/BI seniority.
- No salary info.

## Company hooks (research 2026-10-26)
1. REWE Group Analytics (PyCon DE 2026 sponsor page): supports 40+ business units with advanced analytics and AI; data from ~8 million receipts per day from 6,500 stores, ~90 TB processed per week. ([PyCon DE 2026](https://2026.pycon.de/sponsors/rewe))
2. From the JD: new team, Agentic BI built "von Beginn an"; goal: business users get direct access to data via analysis agents; stack Snowflake, dbt, GitLab.
3. Snowflake is pushing agentic analytics in 2026 (Cortex agents, retail events), context for the stack. ([Snowflake blog](https://www.snowflake.com/de/blog/))
