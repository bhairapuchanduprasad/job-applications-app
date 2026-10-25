# Project brief: LLM Gateway, REWE digital extension

Repo slug: `llm-gateway` (no link on the CV). Status: **planned**.
Base brief (scope, architecture, milestones, README outline): `applications/2026-10-14_accenture_junior-applied-ai-engineer/_work/project-brief-llm-gateway.md`. Build that first; this file adds the platform layer for REWE digital. One repo covers Accenture, HAIAR and REWE.

## Why the extension matters for this JD
| JD phrase | Covered by |
|---|---|
| "Bereitstellung und Betrieb von Plattformen für … generative KI" | Gateway as a shared GenAI platform service deployed to the cloud |
| "automatisierte Self-Services" | Teams onboard by adding one config file (allowed models, budget); CI applies it |
| "IaC-Technologien wie Terraform, CI/CD" | Terraform for Cloud Run, BigQuery dataset, service accounts; GitHub Actions plan/apply |
| "Cloud Service Providern wie GCP" | Deployed on Google Cloud Run |
| "Snowflake, BigQuery oder Databricks zur analytischen Datenverarbeitung" | Request logs streamed/loaded into BigQuery; 2–3 SQL views for cost per team, latency percentiles |
| "Best Practices bereitstellen" | README section "How to onboard your team" + example client |

## Extra scope (≈ 1 day on top of the base build)
1. `teams/<name>.yaml` config (models, max tokens, monthly budget); gateway loads all configs at start. (≈1.5 h)
2. Terraform: Artifact Registry, Cloud Run service, service account with least privilege, BigQuery dataset + table, Secret Manager for provider keys. (≈3 h)
3. Log sink: write each request log row to BigQuery (keep SQLite for local dev). SQL views: cost per team per day, p50/p95 latency, error/fallback rate. (≈1.5 h)
4. GitHub Actions: tests + eval on PR; `terraform plan` on PR, `apply` on main (or document manual apply if no GCP billing). (≈1.5 h)
5. README: platform diagram, onboarding guide, cost note (GCP free tier). (≈1 h)

## Architecture
```
team config (YAML, PR) ──► CI: tests + eval + terraform plan/apply
client app ──► Cloud Run: FastAPI gateway ──► provider A / provider B (fallback)
                         │
                         └─► BigQuery request log ──► SQL views ──► KPI dashboard (React, TS)
```

## Demo idea
Onboard a new "team" with a single PR, send traffic from two teams, show cost per team in BigQuery and on the dashboard, simulate a provider outage and show fallback.

## CV bullets this project must live up to (REWE CV)
- Provider-agnostic gateway over multiple LLM provider APIs with token budgets, streaming, retries, and fallback between providers, logging latency, token usage, and cost for every request; teams onboard self-service by adding a configuration file for their application.
- Deployed to Google Cloud Run with Terraform, with request logs loaded into BigQuery for usage and cost analysis and a KPI dashboard (React, TypeScript); a CI/CD pipeline runs the test suite and an evaluation set on every change.

If anything is cut while building, update these bullets in `_work/cv.tex`. When built, mark it `built` in `profile/master-profile.md`.
