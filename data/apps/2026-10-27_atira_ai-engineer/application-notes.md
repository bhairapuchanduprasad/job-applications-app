# Application notes: Atira, AI Engineer

Status: **build-first** (build Agent Eval Harness and Order Inbox Agent before submitting; briefs in this _work folder point to the main briefs). Both are shared with the Atira FDE application.
Apply via: https://www.linkedin.com/jobs/view/4483596232 (or Atira careers page).

## Likely interview questions
1. **"Tell us about something that broke in your agent system and how you traced it."**
   Kniit: LangGraph harness with entity, relationship, consolidation and reflection agents; changes were measured against an SAP-derived ground truth (P/R 33/45 → 93/90). Prepare one concrete failure story before the interview (profile story field is still empty).
2. **"Deterministic vs. agentic: how do you decide?"**
   Kniit second source stream: deterministic code instead of LLM calls, projected $200k LLM budget → near-zero, accuracy toward 100%. Trade-off: flexibility vs. cost, latency and reproducibility.
3. **"How would you scale to millions of LLM calls a day with sandboxes and observability?"**
   Honest: not done at that scale. Talk through queueing, caching, rate limits/fallbacks via LiteLLM, tracing (OpenTelemetry/Phoenix from the eval-harness project), per-tenant cost budgets, Kubernetes.

## Form answers
- **Why Atira:** Turning RFQs with thousands of pages, price lists and drawings into correct configurations is the same document-understanding problem I solved for energy-sector documents, with a direct line to revenue.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000).
- **Notice period / earliest start:** 15 November 2026.
- **Work authorization:** EU Blue Card (Germany), no sponsorship needed for a qualifying role.
- **Location:** will be based in Munich.
- **German level:** B1 (not required for this role).
- **Why leaving Kniit:** "Kniit is an early-stage startup that restructured around a senior SAP-focused hire before its funding round; my position ended after I had built and handed over its knowledge-extraction pipeline end-to-end."
