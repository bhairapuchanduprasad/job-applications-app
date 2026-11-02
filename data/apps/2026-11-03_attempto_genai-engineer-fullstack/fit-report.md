# Fit report: attempto GmbH & Co. KG, GenAI Engineer mit Fullstack-Hintergrund (m/w/d), Munich

Source: https://www.linkedin.com/jobs/view/4484604045 (found by job-scout 2026-11-03)
Language: German posting, "Deutsch und Englisch fließend" → German Lebenslauf + Anschreiben; German B1 = top gap (fluent, not C1 explicitly). Consulting with client workshops in German.
Seniority: not stated; no years given. OK.

## Fit score: 58 / 100
GenAI core is a strong match (RAG architectures, agentic workflows with LangGraph/LangChain, fine-tuning QLoRA, embeddings, vector DBs incl. Pinecone, guardrails/eval via RAGAS, Docker/Kubernetes, transformer understanding, Streamlit/React). Big gaps: Java/Spring Boot (required "solide"), Angular/TypeScript, OpenAPI/Swagger design, Azure OpenAI/Bedrock/Vertex named services, German fluency for client workshops and requirements engineering.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| RAG architectures, agentic workflows, GenAI use cases | Kniit LangGraph multi-agent, GraphRAG; thesis RAG pipelines | ✅ |
| LLM selection + fine-tuning | QLoRA Open Llama 3B; retrieval model fine-tuning (Covestro) | ✅ |
| Classic ML + DL for hybrid solutions | RF/XGBoost/LSTM (Covestro), Cognizant forecasting | ✅ |
| OpenAPI/Swagger + Spring Boot integration | FastAPI (auto OpenAPI) only; no Java | ❌ |
| Angular frontend, Spring Boot backend | React beginner only | ❌ |
| LLMOps, prototype → scalable deployment | Docker, AWS CDK, GitLab CI/CD, Kubernetes, Azure | ✅ / 🟡 |
| Vector DBs, orchestration of agents | Qdrant, Pinecone, Azure AI Search; LangGraph | ✅ |
| Guardrails, evaluation, performance | RAGAS/PytrecEval; P/R vs SAP ground truth; Expert Interface approval | ✅ / 🟡 |
| Stakeholder translation, customer workshops, requirements engineering | Covestro AI consulting intern | ✅ / 🟡 (German) |
| Cloud AI services (Azure OpenAI, Bedrock, Vertex) | Azure, AWS; named services not used | 🟡 |
| Fluent German | B1 | ❌ top gap |

## Gaps and honest framing
1. German fluency for workshops: B1, state openly.
2. Java/Spring Boot + Angular: not used; planned project includes a Spring Boot client and Angular UI. Unbuilt → not proof in letter.
3. OpenAPI/Swagger: FastAPI generates OpenAPI specs; say exactly that.

## Red flags
Consultancy with "regionaler und langfristiger Projekteinsatz" at clients (banking/insurance); Spring Boot/Angular is a hard requirement for integration work.

## Company hooks
1. IT consultancy since 2006 for banks, insurers, industry, retail and public sector, from consulting to software handover and maintenance; offices Munich, Karlsruhe, Münster, Frankfurt, Hannover ([get-in-it](https://www.get-in-it.de/unternehmen/attempto-gmbh-co-kg), [StepStone](https://www.stepstone.de/cmp/de/attempto-gmbh-%26-co-kg-98151/jobs)).
2. In-house academy ("attempto Akademie"; posting asks to prototype features for it).
3. Posting: GenAI embedded into existing Angular/Spring Boot web apps; regulated environments as plus.

## Project
GenAI-Service für Bestandsanwendungen (Knowledge Assistant for Internal Documents variant, planned): see project-brief-genai-service-spring-angular.md.
