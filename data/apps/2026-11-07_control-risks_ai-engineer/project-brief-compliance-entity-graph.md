# Project brief: compliance-entity-graph

**Goal:** Small pipeline that loads public sanctions-list records, extracts and resolves company/person entities into Neo4j, and answers natural-language compliance questions via generated Cypher, with an evaluation harness.

**Why for Control Risks AI Engineer:** proves Neo4j + Cypher, entity resolution/disambiguation, NER/structured outputs, LLM-to-Cypher RAG, evaluation harness for structured outputs, sanctions domain, sentence-transformers.

**Scope (1-2 days):** one public list (e.g. OFAC SDN or EU consolidated list CSV) subset of ~2k records; no web research agent.

**Stack:** Python, Neo4j (Docker), LiteLLM + Claude (structured outputs via Pydantic), sentence-transformers, FastAPI, pytest.

**Architecture:** loader -> LLM entity/relationship extraction with confidence -> embedding + fuzzy blocking for entity resolution -> Neo4j MERGE with schema constraints -> question -> Cypher generator (schema-aware prompt, read-only validation) -> answer. Eval: labelled set of ~40 duplicates/non-duplicates and ~25 question/Cypher pairs.

**Milestones:** 1 schema + loader; 2 extraction + resolution; 3 Cypher QA; 4 eval harness + README with numbers.

**README outline:** problem, schema diagram, how to run, eval results, limits.

**Demo idea:** ask "Which companies are linked to person X?" and show Cypher + answer.

**CV bullet it must live up to:** "Entity resolution (sentence-transformers) over public sanctions lists into Neo4j, answers compliance questions via generated Cypher, and evaluates extraction and Cypher on a labelled test set."
