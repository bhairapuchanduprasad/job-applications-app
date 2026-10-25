# Project brief: LLM Gateway, Markant extension (Azure Kubernetes Service)

Repo slug: `llm-gateway` (no link on the CV). Status: **planned**.
Base brief (scope, architecture, milestones, README outline): `applications/2026-10-14_accenture_junior-applied-ai-engineer/_work/project-brief-llm-gateway.md`. REWE variant (Terraform on GCP Cloud Run, team configs): `applications/2026-10-24_rewe-digital_platform-engineer-ki-platform/_work/project-brief-llm-gateway.md`. Build the base first; the team-config feature from the REWE brief is reused here. This file adds an Azure + Kubernetes deployment track in the same repo (`deploy/azure/`).

## Goal
Show that you can run an AI workload the way a DevOps engineer on a data and AI platform would: containerised on Kubernetes, infrastructure in code, secrets and identities handled properly, a basic governance guardrail, and a pipeline that deploys it.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Infrastruktur unserer Daten- und KI-Plattform auf Basis moderner Cloud-Technologien" | Gateway as a shared AI platform service on Azure |
| "Kenntnisse in Microsoft Azure sowie im Betrieb containerisierter Anwendungen mit Kubernetes" | AKS cluster, Helm chart, health probes, HPA |
| "Automatisierung, CI/CD oder Infrastructure as Code" | Terraform (azurerm), GitHub Actions: tests → image build + scan → terraform plan/apply → helm upgrade |
| "Cloud Security, IAM und Governance" | Entra Workload ID (no keys in pods), Key Vault for provider keys, least-privilege RBAC, Azure Policy assignment + required tags |
| "Data Engineers und Data Scientists bei der Bereitstellung ... unterstützen" | Teams onboard by adding one YAML config; README "How to onboard your team" |
| "technische Standards, Dokumentationen" | README + short runbook (deploy, rollback, rotate keys) |

## Scope (≈ 1 day on top of the base build)
1. Dockerfile hardening (non-root user, slim image, healthcheck endpoint). (≈0.5 h)
2. Terraform `deploy/azure/`: resource group, ACR, AKS (free tier, 1 small node, OIDC issuer + workload identity enabled), Key Vault, user-assigned managed identity with federated credential, role assignments (AcrPull, Key Vault Secrets User only), Log Analytics workspace, one Azure Policy assignment (e.g. require `owner`/`cost-center` tags or allowed locations), tags on every resource. (≈3 h)
3. Helm chart: Deployment, Service, Ingress (or LoadBalancer), readiness/liveness probes, resource requests/limits, HPA, ServiceAccount annotated for workload identity, Secrets Store CSI driver to mount Key Vault secrets. (≈2 h)
4. GitHub Actions: pytest + eval set on PR; build + push to ACR with Trivy image scan; `terraform fmt/validate/plan` on PR; apply + `helm upgrade --install` on main via OIDC login to Azure (no stored secrets). (≈1.5 h)
5. README + runbook: architecture diagram, onboarding, cost note (destroy cluster after demo; free tier + student/trial credit), security notes. (≈1 h)
If no Azure credit: run the Helm chart on `kind` locally, keep Terraform validated with `plan` only, and say so in the README.

## Architecture
```
team config (YAML, PR) ─► GitHub Actions: tests + eval ─► image build + Trivy ─► ACR
                                        └─► terraform plan/apply (azurerm) ─► helm upgrade
client ─► AKS Ingress ─► gateway pods (FastAPI, HPA) ─► LLM provider A / B (fallback)
                │  workload identity ─► Key Vault (provider keys)
                └─► logs/metrics ─► Log Analytics ─► KPI dashboard (React, TS)
Azure Policy + tags on the resource group (governance)
```

## Milestones
1. Base gateway + tests (base brief). 2. Team configs (REWE brief step 1). 3. Terraform up, cluster reachable. 4. Helm deploy with Key Vault secret mounted via workload identity. 5. CI/CD green end to end. 6. README, runbook, demo recording, `terraform destroy`.

## Demo idea
Open a PR that onboards a new team: CI runs tests, scans the image, shows `terraform plan`; merge deploys. Then kill a pod (Kubernetes restarts it), simulate a provider outage (fallback), and show that the pod reads its key from Key Vault without any secret in the repo or manifest.

## CV bullets this project must live up to (Markant CV, German)
- Anbieterunabhängiges Gateway für mehrere LLM-APIs als gemeinsamer Plattformdienst für Daten- und KI-Teams: Token-Budgets, Retries und Fallback zwischen Anbietern, Protokollierung von Latenz, Token-Verbrauch und Kosten je Anfrage; Teams binden sich per Konfigurationsdatei selbst an.
- Betrieb als containerisierter Workload auf Azure Kubernetes Service (Helm-Chart, Health Checks, Autoscaling), Infrastruktur per Terraform; Cloud Security und IAM über Microsoft Entra Workload ID, Azure Key Vault und Least-Privilege-RBAC, Governance über Azure Policy und Tags; CI/CD-Pipeline mit Tests, Image-Scan und terraform plan/apply.

If anything is cut while building, update these bullets in `_work/cv.tex`. When built, mark it `built` in `profile/master-profile.md`.
