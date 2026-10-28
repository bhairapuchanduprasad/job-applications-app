# Project brief: Semantic Analytics Agent, Fusion variant (OWL + SKOS pharma commercial ontology on a triple store)

Repo slug: `semantic-analytics-agent` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-26_rewe-group_agentic-bi-developer/_work/project-brief-semantic-analytics-agent.md). Created for Fusion Consulting Knowledge Engineer (2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
Ontology-first version of the agent: an OWL ontology (classes, object properties, a few inference rules such as transitive "partOf" territories and product family subclassing) and a SKOS taxonomy of therapeutic areas for synthetic pharma commercial data (products, HCPs, territories, sales calls); SHACL shapes for data quality; loaded into a Stardog triple store (free tier; GraphDB Free as fallback); a LangGraph agent answers business questions only through approved SPARQL templates, with a golden-question eval set in CI. A short README documents the boundary between ontology, semantic data model and instance graph.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "entity hierarchies, relationship types, and inference rules" | OWL classes/properties + reasoner |
| "OWL, RDF", "SKOS", "SPARQL", "Stardog" | ontology, taxonomy, SPARQL templates on GraphDB/Stardog |
| "boundaries between the ontology, the semantic data model, and the knowledge graph" | README section + separate files |
| "conversational analytics, AI agents" | agent over SPARQL |
| "governance guidelines" | SHACL + naming/versioning conventions doc |

## Milestones
1. Ontology in Protégé + SKOS (4 h) 2. Synthetic data + SHACL + triple store (3 h) 3. Agent + SPARQL templates + eval (4 h) 4. README (1 h).

## CV bullet it must live up to
- Modeled OWL ontologies and SKOS taxonomies for synthetic life sciences (pharma) commercial data with entity hierarchies, inference rules and SHACL governance checks in a Stardog triple store, kept separate from the semantic data model; a LangGraph agent serves conversational analytics only through approved SPARQL queries, tested with a golden-question set in CI.
