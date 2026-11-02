# Fit report: JUNI, Data & AI Engineer (m/w/d), Berlin Mitte

Source: https://www.linkedin.com/jobs/view/4486457374 (found by job-scout 2026-11-03)
Language: German posting, but "Fließend Englisch, Deutsch ist ein Plus" → English CV + cover letter (CLAUDE.md rule 3).
Seniority: "Mindestens 4 Jahre Erfahrung als Data Engineer oder Data Scientist" (I have 3, incl. internships/thesis). Reports to Head of Product & Tech. Hybrid.

## Fit score: 70 / 100
LLMs and embeddings inside data pipelines with built-in evaluation is exactly the Kniit + Covestro thesis work (structured extraction, ground-truth evals, embedding benchmarks, Postgres, Python). Weaker: 4-year minimum, owning SaaS integrations with two-way sync/webhooks, record linkage/entity resolution, DSGVO-by-design.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| 4+ yrs as Data Engineer / Data Scientist, own pipelines run in production | 3 yrs: Kniit sole owner of extraction pipeline; Covestro Data Scientist intern + RAG thesis; Cognizant ML | 🟡 (1 yr short) |
| SQL and Postgres | SQL, Postgres at Kniit | ✅ |
| Python for data: pandas, notebooks, eval scripts | Pandas/NumPy at Covestro, RAGAS/PytrecEval eval scripts, notebooks (GitHub) | ✅ |
| SaaS integration over APIs + webhooks, two-way sync | REST APIs with FastAPI, Postman; no SaaS sync | 🟡 / ❌ webhooks, two-way sync |
| LLMs in data pipelines: embeddings, structured extraction, evaluation | Multi-agent extraction, P/R 33/45 → 93/90 vs ground truth; embedding benchmark on 1M+ chunks | ✅ |
| Matching / classification / ranking and measuring it | Precision/recall evaluation, retrieval evaluation (PytrecEval), model comparison | ✅ |
| Check what an API actually does | Postman API testing | 🟡 |
| DSGVO from the start | not in profile | ❌ |
| Daily Claude Code, knows where output needs review | Kniit: Claude Code, custom skills, MCP service into Claude Code | ✅ |
| Record linkage / entity resolution (plus) | Entity extraction + consolidation agents into knowledge graph (Neo4j) | 🟡 adjacent |
| Scraping external data (publications, patents) | not in profile | ❌ |
| Fluent English, German a plus | English business fluent, German B1 | ✅ |

## Gaps and honest framing
1. Experience: 3 years vs "mindestens 4". Frame: sole ownership of a production pipeline end-to-end at Kniit; don't claim 4.
2. SaaS two-way sync / webhooks / scraping: not done at work. Covered by the planned project only (no claims in letter).
3. DSGVO: not in profile; leave out of experience, project covers deletion/consent design.
4. Entity resolution: adjacent (entity extraction + consolidation agent). Say "consolidation", not "record linkage".

## Red flags
4-year minimum may be a hard filter. Small team (Head of Product & Tech, TPM, IT Ops): you'd own the data layer alone, which matches the Kniit "sole developer" story. Salary not stated ("spiegelt Erfahrung wider").

## Company hooks
1. JUNI (formerly UNITE) is the Berlin-Brandenburg Startup Factory, one of ten winners of the federal Startup Factories competition, funded with over €10M by the Federal Ministry for Economic Affairs ([berlin.de](https://www.berlin.de/en/news/9776407-5559700-berlin-bekommt-vom-bund-10-millionen-fue.en.html), [BTU](https://www.b-tu.de/en/news/article/29439-green-light-for-startup-factory-unite-turbo-for-science-based-spin-offs)).
2. Network of universities, research institutions and companies in Berlin and Brandenburg for science-based spin-offs ([Berliner Sparkasse](https://www.berliner-sparkasse.de/de/home/ihre-sparkasse/gut-fuer-berlin/wirtschaft/UNITE.html)).
3. JD: JUNI Core = central data platform joining own tools, science partners, publications, patents, investors and talent; "users must see where a result comes from" (provenance), similar to the Kniit Expert Interface where experts approve knowledge-graph changes.
4. Reported goal of 365 startups per year ([deutsche-startups.de](https://www.deutsche-startups.de/tag/brandenburg/)); unverified on JUNI's own site, so not used in the letter.

## Project
Spin-off Ecosystem Data Hub (new, planned): see project-brief-ecosystem-data-hub.md.
