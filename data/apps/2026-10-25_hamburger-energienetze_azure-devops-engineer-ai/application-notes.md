# Application notes: Hamburger Energienetze GmbH, Azure DevOps Engineer mit Fokus Azure AI (a*), Hamburg

Apply via the LinkedIn posting (https://www.linkedin.com/jobs/view/4481054657) or the Hamburger Energienetze careers page. Build the Azure AI RAG Starter-Kit first (brief in `_work/project-brief-azure-ai-rag-starter-kit.md`): it is on the CV and is the only evidence for Terraform / Azure DevOps / Key Vault / Private Endpoints. Expect the interview in German; German (B1) is the biggest risk.

## Likely interview questions
**1. "Wie würden Sie eine sichere Azure-AI-Zielarchitektur aufbauen?"** Landing zone with hub/spoke VNet, Private Endpoints for Azure OpenAI / AI Search / Key Vault, public access off, managed identities with Entra ID RBAC, diagnostics to Log Analytics, budgets and tags per team. Only speak from the Starter-Kit once it is built; be clear that work experience is AWS CDK + GitLab CI/CD, deployment on Azure at Kniit.

**2. "Wie bewerten Sie einen konkreten AI-Use-Case mit einem Fachteam?"** Covestro AI consulting: understood the decision workflow, advised where agentic AI helps, turned it into a solution concept, then built it. Add Kniit: success measured against SAP ground truth (33/45 → 93/90 precision/recall), human approval in Expert Interface.

**3. "Wie steuern Sie Kosten im Plattformbetrieb?"** Kniit: replaced LLM calls with a deterministic pipeline for the high-volume stream, $200,000 projected LLM budget → near-zero recurring cost. Then platform side: tags, budgets, alerts, quotas per deployment, choosing model sizes per use case.

Also prepare: Terraform state handling and module design, Azure DevOps YAML templates and approvals, monitoring of LLM apps (latency, tokens, quality), "Warum wechseln Sie?" → public line from the profile (DE version).

## Form fields
- **Warum Hamburger Energienetze?** The merger of Stromnetz Hamburg and Gasnetz Hamburg means two grids for about 1.4 million households and a hydrogen network being built; I want to build the shared Azure AI platform that lets good AI use cases spread across teams, and I already know energy-sector data from Kniit.
- **Gehaltsvorstellung:** €70,000 gross/year (range €60,000–75,000); tariff role, so check the pay group. Must meet the EU Blue Card threshold.
- **Frühester Eintritt:** 15. November 2026.
- **Arbeitserlaubnis:** Blaue Karte EU (Deutschland).
- **Standort:** Hamburg (will relocate); hybrid fine.
- **Deutschkenntnisse:** B1 (no certificate).
