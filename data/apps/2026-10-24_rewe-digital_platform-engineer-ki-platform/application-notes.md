# Application notes: REWE digital, Platform Engineer Analytics & KI-Platform (m/w/d), Cologne

Apply via the REWE Group careers site (jobs.rewe-group.com); the LinkedIn posting is https://www.linkedin.com/jobs/view/4386355137. The posting asks for availability and salary expectation in the online application.

Before submitting: build the LLM Gateway with the REWE extension (Terraform on GCP Cloud Run, BigQuery logs, self-service team config). Brief: `_work/project-brief-llm-gateway.md`.

## Likely interview questions
**1. "How would you build a self-service GenAI platform for many business teams?"**
Shared gateway for LLM access (one API, per-team budgets and allowed models, logging of cost/latency), onboarding by config in a PR, templates and best-practice docs, central evaluation and monitoring. Evidence: LiteLLM as the LLM layer at Kniit; MCP service that other tools use; if built, demo the LLM Gateway.

**2. "Tell us about your infrastructure-as-code and CI/CD experience."**
AWS CDK at Covestro (agentic app on AWS; Lambda/SQS/DynamoDB for thesis evaluation); GitLab CI/CD; Docker; Kubernetes and Azure at Kniit. Be honest: no Terraform in a job; same concepts (state, plan/apply, modules).

**3. "Snowflake, BigQuery or Databricks?"**
Honest: not in a job yet. SQL, Postgres, MongoDB, Neo4j, DynamoDB in practice; BigQuery in the LLM Gateway project once built.

Also prepare: "Why platform instead of product AI work?" → you enjoyed building things other people and tools use (MCP service, Expert Interface) and want to multiply that across teams. "Why are you leaving Kniit?" → public line from profile. Expect some German; B1, improving.

## Form fields
- **Why REWE digital?** You already run GenAI for 20,000 administrative staff and process over a billion records a day; a self-service platform for analytics, ML and GenAI makes every team faster, and that is the work I want to do.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000). Must be above the EU Blue Card threshold.
- **Earliest start / availability:** 15 November 2026.
- **Work authorisation:** EU Blue Card (Germany).
- **Location:** Cologne; hybrid works well, willing to relocate.
- **German level:** B1, improving.
