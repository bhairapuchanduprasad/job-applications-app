# Fit report: Redcare Pharmacy, MLOps Engineer (m/f/d), Cologne

**Fit score: 66/100.** Good match on Python, Docker, ML evaluation and deploying AI in production; gaps on the named MLOps tooling (MLflow, Kubeflow, GitHub Actions, Jenkins) and on operating Kubernetes as a platform.

Language: English posting, no mention of German -> English CV + letter. Found by job-scout (LinkedIn 4477379832). Tagline "AI Engineer". Distinct from the earlier Platform Engineer posting (2026-10-27, Azure/Terraform/Databricks); not a duplicate.

## Requirements -> evidence
| Requirement | Evidence | |
|---|---|---|
| Deploying/operating ML/AI in production | Kniit (Python services, Docker, Kubernetes, Azure), Covestro agentic app on AWS | ✅ |
| Solid Python, testing, version control, code review | Python daily, Postman API tests, Git/GitLab; code review not documented | 🟡 |
| Docker + Kubernetes | Docker strong; Kubernetes as part of the Kniit stack, not cluster operation | 🟡 |
| CI/CD (GitHub Actions / Jenkins) | GitLab CI/CD (Covestro); no GitHub Actions/Jenkins in a job | 🟡 |
| ML lifecycle: packaging, versioning, validation, monitoring; MLflow/Kubeflow | Model validation vs ground truth (Kniit, RAGAS thesis); no MLflow/Kubeflow | 🟡 |
| Software architecture, secure delivery | Designed multi-service systems; no security-pipeline experience | 🟡 |
| Secure checks in pipelines | none in a job | ❌ |

## Gaps and honest framing
1. MLflow, Kubeflow, GitHub Actions, Jenkins: named openly in the letter; planned Model Release Pipeline project covers MLflow + GitHub Actions + kind once built.
2. Operating Kubernetes / production troubleshooting: Kniit stack only.
3. Security checks in pipelines, code review practice: not evidenced; left out.

## Projects on the CV
- **Model Release Pipeline** (`planned`, new; brief `_work/project-brief-model-release-pipeline.md`) -> build-first.

## Red flags
- Mid-Senior tag; text asks for "practical experience", no year count. Same company as the Platform Engineer application (2026-10-27): two applications at Redcare, user may want to pick one.

## Company hooks
1. Posting: ML/AI turned into "secure, maintainable, reliable production services" in cross-functional product teams.
2. Redcare's Data & AI platform runs on Azure/AKS/Databricks (see Platform Engineer fit report, careers page).
3. "Europe's No.1 e-pharmacy" (posting).
