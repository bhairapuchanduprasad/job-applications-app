# Application notes: Markant Gruppe, DevOps Engineer (m/w/d) für Daten- und KI-Plattformen, Offenburg

Apply via the LinkedIn posting (https://www.linkedin.com/jobs/view/4481059896) or Markant's career page. **Build first:** the LLM Gateway Azure track (`_work/project-brief-llm-gateway.md`) is on the CV and not built yet. Expect the interview partly in German.

## Likely interview questions
**1. "Wie würden Sie einen containerisierten KI-Service auf Kubernetes betreiben?"** Be honest that Kubernetes ops is new from your side (only in the Kniit stack). Walk through the LLM Gateway once built: Helm chart, probes, requests/limits, HPA, rolling updates, rollback with `helm rollback`, logs in Log Analytics.

**2. "Wie setzen Sie Infrastructure as Code und CI/CD ein?"** Covestro: AWS CDK for the agentic app and for the thesis evaluation infrastructure (Lambda, SQS, DynamoDB), GitLab CI/CD. Then Terraform from the gateway project (plan on PR, apply on main, OIDC login, no stored secrets).

**3. "Was verstehen Sie unter Cloud Security, IAM und Governance auf Azure?"** Managed identities / workload identity instead of keys, Key Vault, least-privilege RBAC on resource-group scope, Azure Policy for allowed locations and required tags, tagging for cost (FinOps). Say clearly what you have built yourself (the project) vs. read about.

Also prepare: "Warum von AI Engineering zu DevOps?" (you know what data and AI teams need from a platform because you were the user), how you'd support Data Scientists deploying a model, Databricks/Unity Catalog basics (other Markant postings mention Azure Databricks), "Why are you leaving Kniit?" → public line from the profile (DE version).

## Form fields
- **Warum Markant?** Markant sits between ~15,000 suppliers and ~200 retailers and processes invoices, master data and payments centrally; a data and AI platform for that must be secure and reliable, and AI is already in products like m.ProductWizard. I want to build that platform with the people who use it.
- **Gehaltsvorstellung:** €70,000 gross/year (range €60,000–75,000). Must clear the EU Blue Card threshold.
- **Kündigungsfrist / frühester Eintritt:** 15 November 2026.
- **Arbeitserlaubnis:** Blaue Karte EU (Germany).
- **Standort:** will relocate to Offenburg; mobile work welcome.
- **Deutschkenntnisse:** B1 (no certificate), improving.
