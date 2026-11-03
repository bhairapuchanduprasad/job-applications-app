# Fit report: Deutsche Rentenversicherung Bund, Anwendungsentwickler*in GenAI, Berlin

Source: https://www.linkedin.com/jobs/view/4484604438 (found by job-scout 2026-11-03)
Language: German posting; "Die Tätigkeit erfordert verhandlungssichere Deutschkenntnisse in Wort und Schrift" → German Lebenslauf + Anschreiben (CLAUDE.md rule 3). Not C1/C2 by name, so prepared per scout rules.
Details: DRV Bund IT, IT-Servicemanagement, Berlin. E11 TV EntgO-DRV. Start 01.01.2027. Bewerbungsfrist 30.11.2026 (Ausschreibungsnummer 11-147-2026; for the form only, not in the letter). Part-time possible.

## Fit score: 58 / 100
The technical core (LLM orchestration/integration into applications, Python/SQL data work, Docker/Git, AWS) matches well, and the reused Bedrock project fits their "idealerweise AWS Bedrock" and IT-Servicemanagement context. The score is held down by the German requirement (verhandlungssicher vs B1) and the "nachweisbare dreijährige" LLM-production experience (about 2 years of LLM work: Kniit + Covestro thesis/intern).

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Hochschulabschluss IT (Bachelor/Diplom FH) | MSc Artificial Intelligence (+ BTech Mechanical with CS minor) | ✅ |
| 3 Jahre Analyse großer Datenmengen mit Python/SQL | Covestro Data Scientist intern, 1M+ chunk embedding benchmark, Cognizant time series, Kniit high-volume source stream; SQL/Postgres | 🟡 (~3 yrs incl. internships) |
| 3 Jahre Orchestrierung/Integration von LLMs in produktive Anwendungen | Kniit (LangGraph multi-agent, LiteLLM, MCP), Covestro agentic app deployed on AWS, RAG thesis | 🟡 (~2 yrs) |
| 3 Jahre Data-Science-Tools Git, Jira, Docker | Git/GitLab, Docker; Jira not in profile | 🟡 / ❌ Jira |
| AWS Bedrock (ideal) | AWS (CDK, Lambda, SQS, DynamoDB); Bedrock only in planned project | 🟡 |
| MLOps-/DevOps-Prozesse optimieren/warten | GitLab CI/CD, Docker, Kubernetes, AWS CDK; automated RAG eval | 🟡 |
| Frontend- oder Backend-Entwicklung | FastAPI, Python microservices, React | ✅ |
| Zusammenarbeit mit Product Ownern, agil | CTO + SAP experts, Covestro stakeholders, Agile | ✅ |
| Verhandlungssichere Deutschkenntnisse | B1, no certificate | ❌ TOP GAP |

## Gaps and honest framing
1. German (top gap): B1 stated plainly in CV and letter; no claim beyond it. Public employer, the posting explicitly says applications without sufficient German may not be considered. Realistic chance is low unless they accept B1 with a learning plan.
2. "Nachweisbar dreijährig" LLM production experience: public-sector wording that is often checked formally against Arbeitszeugnisse. Present the dates honestly.
3. Jira: not in profile, leave out.
4. AWS Bedrock: only in the planned IT-Ticket-Assistent project.

## Red flags
- Formal public-sector process: Zeugnisse/certificates needed, deadline 30.11.2026, start date 01.01.2027 (later than my 15.11 availability, fine).
- E11 TV EntgO-DRV salary is fixed by tariff and likely below the €60–75k expectation; check against the Blue Card threshold. Decision for the user.

## Company hooks
1. DRV Bund is the largest German pension insurer: 24.2M insured, 10.8M pensioners (from the JD).
2. DRV Bund runs a central AI lab with an AI expert team and a "use-case factory" that brings AI into the departments ([DRV job posting, AI Transformation Manager](https://www.deutsche-rentenversicherung.de/Bund/DE/Karriere/Stellenangebote/hauptverwaltung-diverse-standorte/2026-06-08-ai-transformation-ma-berlin)).
3. DRV Bund contributes expertise to an EU advisory body supporting the Commission on implementing the AI Act ([DRV press releases 2026](https://www.deutsche-rentenversicherung.de/Bund/DE/Presse/Pressemitteilungen/pressemitteilungen_aktuell/2026/Pressemitteilungen-2026_node)); summary from search results, not opened directly.
4. Other DRV Bund GenAI postings (Prozessentwickler*in GenAI, Data Scientist with productive GenAI/RAG) show a growing GenAI team in Berlin ([praktischkommune.de](https://praktischkommune.de/jobs/230917-prozessentwickler-in-genai-berlin)).

## Project
IT-Ticket-Assistent (Amazon Bedrock), existing planned project, reused: base brief applications/2026-10-21_bedrock-projekt_python-genai-developer/_work/project-brief-it-ticket-assistant-bedrock.md; DRV variant notes in project-brief-it-ticket-assistant-bedrock.md here.
