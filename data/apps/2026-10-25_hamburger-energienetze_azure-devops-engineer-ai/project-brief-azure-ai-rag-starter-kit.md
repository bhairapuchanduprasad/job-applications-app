# Project brief: Azure AI RAG Starter-Kit (repo slug: azure-ai-rag-starter-kit)

Status: planned (must be built before submitting to Hamburger Energienetze). No link on the CV.

## Goal
A reusable starter kit that lets a platform team spin up a secure, monitored RAG reference solution on Azure per environment with Terraform and Azure DevOps Pipelines, plus a small reference app over public grid-connection documents.

## Why it matters for this JD
Proves the must-haves my work history covers weakly: Azure DevOps, Terraform / Infrastructure-as-Code for Azure resources, Entra ID, Key Vault, Private Endpoints, Networking (VNet), Monitoring, standardised CI/CD pipelines, templates / starter kits / reference solutions, Azure OpenAI, AI Search, central cost control (tags, budgets), governance/security structures.

## Scope (1–2 days)
- Terraform: modules `network` (VNet, subnets, private DNS zones), `ai` (Azure OpenAI with one chat + one embedding deployment, Azure AI Search), `security` (Key Vault, user-assigned managed identity, RBAC role assignments, public network access disabled, Private Endpoints for OpenAI/Search/Key Vault), `app` (Container App or App Service with VNet integration), `monitoring` (Log Analytics, Application Insights, diagnostic settings), `cost` (mandatory tags, consumption budget + alert). Remote state in a storage account. `envs/dev`, `envs/prod` tfvars.
- Azure DevOps YAML: `infra-pipeline.yml` (fmt, validate, tflint, plan as artifact, manual approval, apply via workload identity federation service connection) and `app-pipeline.yml` (pytest, build image, deploy, RAGAS eval as a quality gate). Pipeline templates in `templates/` so teams reuse them.
- Reference app: Python/FastAPI, ingests public PDF/HTML documents on grid connections (e.g. public technical connection rules / FAQ pages, only openly published material), chunks, embeds with Azure OpenAI, indexes into AI Search (hybrid search), answers with citations. Auth to Azure services only via managed identity (no keys in code); secrets that remain in Key Vault.
- Small labelled question set (15–25 Q&A) + RAGAS faithfulness/answer relevancy in CI.
- If no Azure subscription budget for Private Endpoints/OpenAI: keep `terraform plan` + validate in CI and document the apply step; still deploy a minimal dev env once if possible.

## Architecture sketch
Azure DevOps → (Terraform) → VNet [app subnet | private endpoint subnet] → Container App (FastAPI, managed identity) → Private Endpoints → Azure OpenAI, AI Search, Key Vault; diagnostics → Log Analytics / App Insights; budget alert per resource group; Entra ID RBAC for identities.

## Milestones
1. Terraform modules + dev env plan/apply (half day).
2. Azure DevOps pipelines with templates, approval gate (2–3 h).
3. Reference RAG app + ingestion + citations (half day).
4. Eval set + RAGAS gate, App Insights traces, budget alert, README (2–3 h).

## README outline
Purpose · Architecture diagram · Security model (identities, private networking, Key Vault) · Getting started (bootstrap state, service connection, `envs/dev`) · Pipeline templates and how teams reuse them · Monitoring and cost control · Evaluation · Limitations / next steps (landing zone integration, policy as code).

## Demo idea
2-minute screen recording: pipeline run with plan + approval, app answering a grid-connection question with sources, App Insights trace, budget view.

## CV bullets it must live up to (exact, German CV)
- Wiederverwendbare Terraform-Module und YAML-Pipelines in Azure DevOps, die eine RAG-Referenzlösung pro Umgebung reproduzierbar bereitstellen: Azure OpenAI, Azure AI Search und Key Vault hinter Private Endpoints in einem eigenen VNet, Zugriff über Entra ID (Managed Identity), Monitoring mit Azure Monitor und Application Insights.
- Python/FastAPI-Referenz-App für Fragen zu öffentlichen Netzanschluss-Dokumenten mit Quellenangaben; RAG-Evaluierung (RAGAS) als Qualitätstor in der Pipeline, Kosten-Tags und Budget-Alarme pro Umgebung, als Template mit Dokumentation für weitere Teams.
