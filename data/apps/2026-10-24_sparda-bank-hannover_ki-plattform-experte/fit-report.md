# Fit report: Sparda-Bank Hannover eG, KI-Plattform-Experte (m/w/d) mit Schwerpunkt Data Science und LLM Engineering, Hannover

**Fit score: 68/100.** Unusually good match on the two technical halves they want together: classic ML for forecasting and time series (Cognizant EV load forecasting, Covestro time-series prediction) and generative AI (multi-agent LLM systems, RAG, vector databases, semantic search, MCP), plus Python, Git, CI/CD and Azure. Gaps: building and operating an AI development platform (Databricks or similar), governance/standards for in-house AI development, banking domain.

Language: German posting with no stated German requirement → English documents (CLAUDE.md rule 3). A ~400-person cooperative bank in Hannover with formal "Sie" culture almost certainly works in German internally; B1 shown honestly. This is the biggest practical risk.

Source: https://www.linkedin.com/jobs/view/4477678140. Contact: Moritz Witte, Bereichsleiter Künstliche Intelligenz (0511 3018-4610, moritz.witte@sparda-h.de). Pay: tariff, up to €80,400 gross/year full time (stated).

## Requirements → evidence
| Requirement | Evidence | Rating |
|---|---|---|
| Degree in (Business) Informatics, Data Science, Maths or comparable | MSc Artificial Intelligence | ✅ |
| Developing and operationalising ML models, esp. forecasting and time series | Cognizant: ARIMA, SARIMA, XGBoost, Prophet, LSTM for EV load (LSTM 96% test accuracy); Covestro: RF/XGBoost/LSTM on sensor time series + Streamlit dashboard | ✅ (operationalising 🟡) |
| Generative AI applications, LLMs | Kniit multi-agent LangGraph pipeline (33/45 → 93/90); Covestro agentic app deployed to AWS | ✅ |
| Python, code versioning, Git-based development, CI/CD | Python; Git, GitLab CI/CD | ✅ |
| Building/operating a modular, scalable AI development platform (ideally Databricks) | Not in profile | ❌ |
| Data architectures for GenAI: RAG, vector DBs, semantic search, MCP | RAG pipelines (chunking, indexing), Qdrant/Pinecone/Azure AI Search, embedding benchmark on 1M+ chunks, MCP query service | ✅ |
| Cloud, ideally Azure (or AWS/GCP) | Azure (Kniit Expert Interface, Azure AI Search), AWS (CDK, Lambda, EC2, SQS, DynamoDB) | ✅ |
| Processes, standards, governance for in-house AI development | Evaluation against ground truth; no formal governance role | 🟡 |
| Close work with business units on pilots | Covestro AI consulting with business stakeholders; SAP experts at Kniit | ✅ |

## Gaps and honest framing
- **Databricks / platform operation:** none. Frame: you set up the pieces of a platform (CI/CD, Docker, cloud on Azure and AWS, evaluation) and want to build one properly.
- **Governance:** say you treated evaluation and human approval as part of delivery (Expert Interface, ground truth), and would bring that into standards.
- **German:** B1; likely needed day to day. Mention that you are improving it.

## Red flags
- Small bank (about 400 employees in 2022): likely German-speaking environment; English application may be accepted but daily work probably German.
- Tariff pay: check the group within the "up to €80,400" range.

## Company hooks (sources)
1. Cooperative bank (eG) caring for its members since 1903; about 408 employees on average in 2022. Source: https://www.sparda-h.de/content/dam/f4158-0/cloud-transfer/pdf/230420_Sparda-Bank-Hannover_Jahresbericht-2022_WEB.pdf
2. Building its own AI department: also hiring an AI requirements manager / AI business analyst in Hannover. Source: https://www.stepstone.de/results/intelligence/in-hannover
3. From the posting: builds its own AI solutions where no suitable standard product exists, wants processes, standards and governance for in-house development, and pilots use cases with business units on the AI platform. kununu top employer 2023–2025.
