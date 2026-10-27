# Application notes: Redcare Pharmacy, Platform Engineer (m/f/d), Data & AI, Cologne

Status: **build-first** (LLM Gateway, Azure/AKS/Terraform track, is `planned`: build it exactly as the CV bullets say, or cut the parts not built, or remove it before submitting). Once built, name the real CI tool in the bullet and mention it in the letter as the Terraform/AKS evidence.
Apply via: https://www.linkedin.com/jobs/view/4481883882
ATS coverage: 79%. Gaps: Terraform, AKS operations, GitOps, Databricks.

## Likely interview questions
1. **"How would you onboard a new AI team onto the platform?"** Self-service config (namespace, quotas, secrets from Key Vault via workload identity), templated Helm chart + pipeline, docs/runbook.
2. **"Walk us through a deployment you built."** Covestro: Docker + AWS CDK + GitLab CI/CD; thesis: Lambda/SQS/DynamoDB in CDK.
3. **"What do AI workloads need from a platform?"** Model/provider access with budgets and fallback, GPU/CPU scaling, secrets, eval in CI, cost and latency visibility: from building them at Kniit/Covestro.

## Form answers
- **Why Redcare:** building a next-generation AI platform on Azure/AKS/Databricks; platform role close to the AI workloads.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000).
- **Notice period / earliest start:** 15 November 2026.
- **Work authorization:** EU Blue Card (Germany).
- **Location:** Cologne (hybrid).
- **German level:** B1 (no certificate).
- **Why leaving Kniit:** "Kniit is an early-stage startup that restructured around a senior SAP-focused hire before its funding round; my position ended after I had built and handed over its knowledge-extraction pipeline end-to-end."
