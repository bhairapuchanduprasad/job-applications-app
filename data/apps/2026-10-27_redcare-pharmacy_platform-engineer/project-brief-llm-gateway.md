# Project brief: LLM Gateway (Azure / AKS track) — Redcare Pharmacy Platform Engineer

Same project and scope as the Markant variant: applications/2026-10-25_markant_devops-engineer-daten-ki-plattformen/_work/project-brief-llm-gateway.md (base brief: applications/2026-10-14_accenture_junior-applied-ai-engineer/_work/project-brief-llm-gateway.md). No new scope; the CV bullets are the English version of the Markant bullets.

## Why it matters for this JD
Redcare's Platform Engineer builds Azure infrastructure with Terraform, operates an Azure Kubernetes-based platform for the Data & AI department with GitOps and CI/CD, and builds self-service capabilities for AI teams. The gateway shows: Terraform on Azure, AKS + Helm, self-service onboarding via config, Key Vault/Entra/RBAC security, CI/CD with image scan.

## Optional add-ons if time allows (not on the CV, don't claim until built)
- Deploy via GitOps (Flux or Argo CD) instead of pipeline-driven helm upgrade.
- A sample Databricks job calling the gateway.

## CV bullets it must live up to
- Provider-agnostic LLM gateway as a shared, self-service service of an AI platform for Data Engineers and Data Scientists: token budgets, retries and fallback between providers, latency, token and cost logging per request; teams onboard through a configuration file.
- Containerized workload on Azure Kubernetes Service (Helm chart, health checks, autoscaling) with infrastructure in Terraform; security via Microsoft Entra Workload ID, Azure Key Vault and least-privilege RBAC, governance via Azure Policy and tags; CI/CD pipeline with tests, image scan and terraform plan/apply; runbook documentation.
