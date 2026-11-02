# Fit report: vent.io GmbH, Data / Software Engineer - AI & Data (w/m/d), Frankfurt am Main

Source: https://www.linkedin.com/jobs/view/4486194672 (found by job-scout 2026-11-03)
Language: German posting, "Du kommunizierst sehr gut auf Deutsch und Englisch" → German Lebenslauf + Anschreiben; German B1 = top gap (not C1-mandatory).
Seniority: Associate, "erste Berufserfahrung in der Softwareentwicklung". Good level match.

## Fit score: 74 / 100
Python backend + GenAI integration role in a Data Engineering Chapter: FastAPI, PostgreSQL, RAG, embeddings, vector search, Azure and Docker are all in the profile. Gaps: Databricks/Unity Catalog, Terraform, GitHub Actions (GitLab CI/CD instead), OCR, Pydantic/SQLAlchemy not named, German.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Degree in CS/engineering/science | MSc AI, BTech Mech. Eng. + CS minor | ✅ |
| First professional SW experience, very good Python | 3 years; Python everywhere | ✅ |
| Backends, REST APIs, background services (FastAPI, Pydantic, SQLAlchemy, PostgreSQL) | FastAPI at Covestro + Kniit, Python microservices (Expert Interface), Postgres | ✅ (Pydantic/SQLAlchemy not named 🟡) |
| GenAI integration: Azure OpenAI, structured outputs, OCR, embeddings, vector search (RAG) | LangGraph extraction agents, RAG thesis, embedding benchmark 1M+ chunks, Azure AI Search | ✅ / 🟡 (Azure OpenAI + OCR not named) |
| Data + batch pipelines; Databricks / Unity Catalog | Kniit ingestion pipeline + deterministic high-volume pipeline; Pandas | 🟡 / ❌ Databricks |
| Clean tested code (pytest, Ruff, mypy, SonarCloud), AI coding tools | Clean code, Claude Code daily; pytest not named | 🟡 / ✅ |
| CI/CD (GitHub Actions, Docker), Azure (Container Apps, Terraform) | GitLab CI/CD, Docker, AWS CDK, Azure deployment | 🟡 / ❌ Terraform |
| Teamwork with Data Scientists, PO, UX | Worked with CTO, SAP experts, chemists | ✅ |
| Sehr gutes Deutsch | B1 | ❌ top gap |

## Gaps and honest framing
1. German B1: state openly in the letter.
2. Databricks / Unity Catalog, Terraform, GitHub Actions: not used professionally; IaC experience via AWS CDK; GitLab CI/CD. Planned project covers them (unbuilt → not proof in letter).
3. OCR / Azure OpenAI structured outputs: extraction experience is LLM-based on text documents; say "structured extraction", not OCR.

## Red flags
None. Associate level fits well.

## Company hooks
1. vent.io is Deutsche Leasing's digital and innovation unit (founded 2021), part of the Sparkassen-Finanzgruppe, building digital products for the German Mittelstand ([Börsen-Zeitung](https://www.boersen-zeitung.de/banken-finanzen/ventio-baut-geschaeft-mit-sparkassen-aus), [job posting](https://fuchsjobs.de/job/stellenangebote--software-engineer-frontend-fmd-frankfurt-ventio-64a950)).
2. Also invests in B2B startups (construction, logistics, manufacturing, AI) ([F4 Fund](https://f4.fund/firms/vent-io)).
3. Posting: interdisciplinary product teams (Data Scientists, Frontend, UX, PO); "Start-up-Flair mit der Sicherheit der Sparkassen Finanzgruppe".

## Project
Leasing-Dokumentenextraktion (Order Inbox Agent variant, planned): see project-brief-leasing-document-extraction.md.
