# Fit report: Amadeus Fire (client: real-estate company, Köln), KI-Spezialist (m/w/d)

Source: https://www.linkedin.com/jobs/view/4486156435 (found by job-scout 2026-11-02). Personalvermittlung, Festanstellung, Ref. 16-257762, contact Omid Abdul (Amadeus Fire Köln).
Language: German posting, "Sehr gute Deutsch- und Englischkenntnisse" → German Lebenslauf + Anschreiben; German B1 = top gap.
Seniority: "Professional/Experienced", 75–80k €, 40 h, Homeoffice option.

## Fit score: 76 / 100
Broad AI-engineer profile that covers both GenAI (LLM, RAG, agents, prompt engineering) and classic ML/DL with PyTorch/TensorFlow/scikit-learn; the profile has both. Gaps: German, MLOps/monitoring in production as a named practice, Java/C++.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Develop and implement AI/ML solutions for business needs | Kniit product; Covestro agentic app for business stakeholders | ✅ |
| GenAI/LLM apps: chatbots, AI agents, copilots | LangGraph agents (Kniit, Covestro), RAG system evaluation (thesis) | ✅ |
| Data preparation, analysis, processing | Ingestion/chunking pipelines; feature engineering on sensor time series | ✅ |
| Training, evaluation, optimisation of ML models | RF/XGBoost/LSTM (Covestro), ARIMA/Prophet/LSTM (Cognizant), RAG eval | ✅ |
| Integrate models and APIs into existing apps/processes | MCP service into Claude Code; FastAPI back ends; Expert Interface | ✅ |
| MLOps/AI infrastructure for deployment + monitoring | Docker, Kubernetes, AWS CDK, GitLab CI/CD; no MLflow/monitoring stack in profile | 🟡 |
| Monitoring incl. performance, cost, security, reliability | Cost: $200k → near zero; P/R evaluation; no production monitoring tooling named | 🟡 |
| Python; ideally Java/C++ | Python ✅; Java/C++ ❌ (ideally) | ✅/❌ |
| ML/DL frameworks PyTorch, TensorFlow, scikit-learn | All three in profile | ✅ |
| SQL + vector DBs | SQL, Postgres, Qdrant, Pinecone, Azure AI Search | ✅ |
| Cloud AWS/Azure/GCP | AWS + Azure | ✅ |
| Git, CI/CD, APIs, MLOps understanding | GitLab CI/CD, REST APIs | ✅/🟡 |
| Sehr gute Deutschkenntnisse | B1 | ❌ top gap |

## Gaps and honest framing
1. **German B1**: state openly.
2. **MLOps/monitoring**: frame as Docker/K8s/CI/CD deployments + evaluation; planned LLM Gateway project adds latency/token/cost monitoring (unbuilt → not proof in letter).
3. **Java/C++**: none; leave out.
4. **Real-estate domain**: none.

## Red flags
- Client unnamed (Personalvermittlung). Amadeus Fire already has the user's profile from the 2026-10-29 AI Solutions Engineer application (applications/2026-10-29_amadeus-fire_ai-solutions-engineer): mention that application to the recruiter; avoid sending conflicting versions.
- "Ohne Anschreiben einfach bewerben": the Anschreiben is optional; CV is what matters.

## Company research
Amadeus Fire AG: listed personnel-services company, 20+ branches; this is direct placement (Personalvermittlung) into a permanent job at the client. No info on the client beyond "renommiertes Unternehmen aus der Immobilienbranche mit Sitz in Köln". Letter uses only posting facts.

## Projects on the CV
- LLM Gateway (planned, reused; brief: project-brief-llm-gateway.md) → build-first. Covers monitoring of latency/cost/reliability.
