# Fit report: Markant Gruppe, DevOps Engineer (m/w/d) für Daten- und KI-Plattformen, Offenburg

**Fit score: 52/100.** Stretch application. Strong on the "Daten- und KI-Lösungen" side (you build exactly the workloads this platform hosts) and solid on containerised deployment (Docker, AWS CDK as Infrastructure as Code, GitLab CI/CD, an Azure-hosted app at Kniit). Weak on the core of a DevOps role: no hands-on Kubernetes operations beyond listing it in the Kniit stack, no Terraform/Bicep, nothing on Cloud Security, IAM or governance, and the posting asks for sufficient German.

Language: German posting that requires German ("applications without ... sufficient German language skills may not be considered") → German Lebenslauf + Anschreiben (CLAUDE.md rule 3). Your German is B1 without certificate: **gap**, see below. Prepared anyway per user decision.

Source: https://www.linkedin.com/jobs/view/4481059896. No contact person, no deadline, no salary in the posting. Full-time, Offenburg, mobile work possible (Mobiles Arbeiten, Gleitzeit).

## Requirements → evidence
| Requirement (JD) | Evidence | Rating |
|---|---|---|
| Technische Ausbildung / Studium IT oder vergleichbar | MSc Artificial Intelligence; BTech with minor in Computer Science | ✅ |
| ≥ 2 Jahre Cloud-Technologien und moderne Plattformumgebungen | about 2 years with cloud deployment across roles: AWS (CDK, Lambda, SQS, DynamoDB, EC2) at Covestro 2024–25, Azure at Kniit 2025–26. Deployment of own apps, not operating a shared platform | 🟡 |
| Microsoft Azure | Expert Interface deployed on Azure (Kniit); Azure AI Search (thesis). No Azure admin/IaC depth | 🟡 |
| Betrieb containerisierter Anwendungen mit Kubernetes | Docker in every recent role; Kubernetes listed in the Kniit stack, no detail on operating clusters | 🟡 / ❌ (ops) |
| DevOps-Praktiken: Automatisierung, CI/CD, Infrastructure as Code | GitLab CI/CD (Covestro); AWS CDK as IaC for app and evaluation infrastructure; automated evaluation pipelines; deterministic pipeline automation at Kniit. No Terraform/Bicep | 🟡 |
| Cloud Security, IAM, Governance | Nothing in the profile | ❌ |
| Berührungspunkte mit Datenplattformen, Analytics, KI-Lösungen | Core of your career: multi-agent LLM systems, RAG, embedding benchmarks on 1M+ chunks, Neo4j/MongoDB/Postgres, ML models | ✅ |
| Data Engineers / Data Scientists unterstützen | You are the data scientist / AI engineer they would support; built evaluation infrastructure for PrismaChat, Streamlit dashboard for chemists | ✅ (from the other side) |
| Zusammenarbeit mit Fachbereichen, Entwicklern, Plattformteams | SAP domain experts + CTO (Kniit), business stakeholders (Covestro AI consulting) | ✅ |
| Technische Standards, Dokumentation, Wissensaustausch | Clean code principles, custom Claude Code skills; handed over the Kniit pipeline end-to-end | 🟡 |
| Eigenständig, Hands-on | Sole developer at Kniit | ✅ |
| Ausreichende Deutschkenntnisse (note in posting) | B1, no certificate | ❌ gap |

## Gaps and honest framing
- **German (biggest risk):** B1; the posting says applications without sufficient German may not be considered. State B1 honestly in the letter; say you work in German with colleagues and use English for technical documentation. Don't overclaim.
- **Kubernetes operations:** only in the Kniit tech stack. Frame as "Kubernetes in the Kniit stack, containerised services with Docker everywhere"; do not claim cluster operation. Build the LLM Gateway on AKS before the interview to have something concrete.
- **Cloud Security, IAM, Governance:** not covered by work experience. Covered only by the planned project (Entra Workload ID, Key Vault, RBAC, Azure Policy), which must be built before you talk about it. Not mentioned as proof in the letter.
- **Terraform / Bicep:** IaC experience is AWS CDK only. Terraform appears only in the planned project.
- **Seniority of the DevOps profile:** your identity is AI engineer; pitch yourself as the AI engineer who wants to move to the platform side and knows what data and AI teams need from it.

## Red flags
- "Sufficient German language skills" note at the bottom: a hard filter at some German Mittelstand-style employers.
- Markant moved its operational hub to Pfäffikon (Switzerland) in a reorganisation; Offenburg keeps services for German partners (Lebensmittel Zeitung). Not a blocker, but ask where the platform team sits.
- Posting gives no salary; check that the offer clears the Blue Card threshold.

## Company hooks (sources)
1. Markant is a back-office service provider between ~15,000 suppliers and ~200 retailers in food and non-food trade across Europe (1,200+ employees, 15 countries), acting as a single point of contact that replaces bilateral connections, e.g. central invoice processing. Source: https://www.markant.com/en
2. Its digital product line already includes AI: m.ProductWizard generates product marketing texts with AI; other services cover GDSN product master data (m.Synced), e-invoicing and NIS-2 cyber checks (m.CyberLyze). Source: https://www.markant.com/en
3. Markant opened a tech hub in Porto (joint venture with xelerate.tech, Feb 2024) to strengthen its European B2B digital platform. Source: https://www.portugalglobal.pt/en/news/2024/february/markant-opens-technology-centre-in-porto
4. Other Markant postings in Offenburg describe the stack around this role: Azure with Databricks and Unity Catalog for data, RBAC and GDPR/PII controls, a "MarkHub" cloud platform and a FinOps role for tagging and cloud policies. Source: StepStone listings (e.g. https://www.stepstone.de/results/microsoft-azure/in-offenburg). Treat as indicative, not confirmed for this team.
5. Lebensmittel Zeitung: "Markant erfindet sich neu", reorganisation with Pfäffikon as operational hub, Offenburg keeps German partner services. Source: https://www.lebensmittelzeitung.net/news/p/88741 (date not visible).

## Project chosen (5b)
Reused the planned **LLM Gateway** (already on the Accenture, HAIAR and REWE digital CVs) with a Markant extension: deployment to Azure Kubernetes Service with Terraform, Entra Workload ID, Key Vault, RBAC and Azure Policy. Brief: `_work/project-brief-llm-gateway.md`. Status: planned → application is `build-first`.
