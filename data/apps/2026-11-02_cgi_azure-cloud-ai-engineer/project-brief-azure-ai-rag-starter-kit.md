# Project brief: Azure AI RAG Starter-Kit (CGI Azure Cloud & AI Engineer variant)

Base brief: applications/2026-10-25_hamburger-energienetze_azure-devops-engineer-ai/_work/project-brief-azure-ai-rag-starter-kit.md (Terraform modules, Private Endpoints, Azure OpenAI, AI Search, Key Vault, Managed Identity, Log Analytics/App Insights, cost tags + budget alerts, pipelines with RAGAS gate, FastAPI RAG app). Build that; this file lists the CGI additions.

## Why it matters for this JD
Proves Terraform-first IaC, Azure AI Services/Azure OpenAI, shared services (networking, monitoring/logging), CI/CD, plus MLOps via an Azure ML endpoint.

## Variant additions (keep within 1–2 days)
- Small scikit-learn model (e.g. ticket-priority classifier on synthetic data) registered and deployed as an Azure ML managed online endpoint via Terraform/CLI; request logging + data-drift note in Log Analytics.
- Pipelines in GitHub Actions or Azure DevOps (either is fine; CV says "CI/CD-Pipelines"): fmt/validate/plan with approval, apply, tests, RAGAS gate.
- Linux: run the FastAPI app in a container on Azure Container Apps; document the Linux base image hardening steps briefly.

## CV bullet it must live up to (German CV)
- Terraform-Module für eine sichere Azure-Umgebung (Private Endpoints, Azure OpenAI, Azure AI Search, Key Vault, Managed Identity, Logging mit Log Analytics) und CI/CD-Pipelines mit Tests und RAGAS-Gate für eine RAG-App (FastAPI); dazu ein ML-Modell als Azure-ML-Endpoint mit Monitoring (MLOps).

When built: mark `built` in profile/master-profile.md with real numbers; only then use it in cover letters.
