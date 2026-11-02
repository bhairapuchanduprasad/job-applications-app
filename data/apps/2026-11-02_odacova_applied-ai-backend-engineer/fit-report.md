# Fit report: odacova, Applied AI & Backend Engineer (m/w/d), Dortmund

Source: https://www.linkedin.com/jobs/view/4484323085 (found by job-scout 2026-11-02)
Language: posting in German, requires "Sehr gute Deutsch- und Englischkenntnisse" → German CV + Anschreiben (CLAUDE.md rule 3).
Seniority: entry level (MID-Assistent funded role), hybrid (2 office days/week), unbefristet, 40–60k €.

## Fit score: 72 / 100
Strong technical match (Python backend + LLM integration + own ML models, 50/50 split fits my profile exactly); main gap is German (B1 vs "sehr gut"), plus no Firebase/GCP.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Degree in CS / Data Science / MINT | MSc Artificial Intelligence, THWS (04/2025) | ✅ |
| Funding rule: exam date ≤ 2 years before start | MSc finished 04/2025, start by 18.12.2026 → ~20 months | ✅ (confirm exam date on certificate) |
| Sehr gute Python-Kenntnisse | 3 years Python: Kniit, Covestro, Cognizant | ✅ |
| Python backend services, REST APIs, data models, app logic | FastAPI backend (Covestro), Python microservices backend for Expert Interface (Kniit), MCP query service | ✅ |
| Integration of external services/interfaces | LiteLLM model layer, MCP service integrated into Claude Code, AWS services via CDK | ✅ |
| Integration of models and LLM APIs in production | Multi-agent LangGraph pipeline (93%/90% P/R), LiteLLM, deployed agentic app on AWS | ✅ |
| Own ML models on domain data | RF/XGBoost/LSTM on process time-series (Covestro), EV load forecasting (Cognizant) | ✅ |
| BI tools, AI-supported analysis & reporting | Streamlit dashboard for chemists; no classic BI tool (Power BI/Looker) | 🟡 |
| Data engineering | Ingestion/chunking/indexing pipeline, deterministic extraction pipeline for high-volume stream | ✅ |
| Automated tests, documentation | RAGAS/PytrecEval automated evaluation, Postman API tests; pytest not explicitly in profile | 🟡 |
| Deployments, monitoring, CI/CD | Docker, AWS CDK, GitLab CI/CD, Azure, Kubernetes; monitoring not explicit | 🟡 |
| Linux/Ubuntu | Not stated in profile (implied by Docker/K8s/AWS work, not claimed) | 🟡 |
| Git | Git, GitLab | ✅ |
| ML / GenAI / LLM fundamentals + first practical AI applications | Core of profile | ✅ |
| Sehr gute Deutschkenntnisse | German B1, no certificate | ❌ top gap |
| Nice: Docker / CI/CD | Docker, GitLab CI/CD | ✅ |
| Nice: PostgreSQL, Firestore | Postgres, MongoDB, Neo4j; no Firestore | 🟡 |
| Nice: Firebase / Google Cloud / serverless | AWS Lambda (serverless) + Azure; no GCP/Firebase | 🟡 |
| Nice: reliable operation of data/AI apps | Deployed Expert Interface on Azure, agentic app on AWS | ✅ |

## Gaps and honest framing
1. **German (B1 vs "sehr gut")**: state B1 openly in the Anschreiben, offer to work in German day to day and continue the course. Biggest risk for this application.
2. **Firebase / Google Cloud / Firestore**: not used. Frame: cloud deployments on AWS (incl. serverless Lambda) and Azure; GCP is a transfer. Tailored project (planned) uses Cloud Run + Firestore.
3. **Classic BI tooling**: only Streamlit dashboards; frame as "KI-gestützte Analyse- und Reporting-Funktionen" via the Covestro dashboard, nothing more.
4. **Linux, pytest, monitoring**: not explicit in profile; not claimed on CV.

## Red flags
- Salary range 40–60k € is below my 60–75k expectation; the top of their range is close to my floor. Blue Card salary threshold must be met by the offer (IT shortage-occupation threshold applies); check before accepting.
- Entry-level role funded via MID-Assistent: exam-date condition (see above) must be documented with the MSc certificate.
- Health/nutrition domain: GDPR-sensitive health data (they stress employer gets no access to personal data).

## Company hooks
1. odacova rates whole canteen dishes with a personalised "Gesundheits-Score" based on DGE recommendations (not the Nutri-Score) and gives employers an anonymised company-level "Gesundheits-KPI". Source: https://www.odacova.de
2. Menus are imported automatically from ERP/inventory systems as nutrient data or as recipes analysed via the Bundeslebensmittelschlüssel; integration via SDK/API and white-label. Source: https://www.odacova.de
3. Partners include Aramark (Food-Coach), Dussmann (Food Campus Neubiberg), WISAG, Klinik Dr. Lauterbach. Source: https://www.odacova.de
4. First financing round closed (news dated 28.04.2026); Cologne impact investor capacura invested (May 2026). Sources: https://www.odacova.de, https://startupvalley.news/de/odacova-plattform-betriebskantinen-investment/
5. Founded by TU Dortmund computer-science graduates Timo Sievernich (CEO, nutrition science) and Robin Wiebusch (CTO). Source: https://www.deutsche-startups.de/2026/06/01/5-neue-startups-norta-odacova-profitize-lg-fashion-labs-veltivo/?amp=1

## Projects section
No `planned` project in the profile covers canteen/nutrition data, Firebase/GCP and BI reporting together, so a new one was created: **Canteen Menu Insights** (planned, build-first). Brief: `_work/project-brief-canteen-menu-insights.md`.
