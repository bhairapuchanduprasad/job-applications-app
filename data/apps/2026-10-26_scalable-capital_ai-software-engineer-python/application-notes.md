# Application notes: Scalable Capital, AI Software Engineer – Python (Berlin / Munich)

Status: **build-first**. Build `llm-gateway` with the AWS/Terraform track (brief in this folder) before submitting; the CV describes it.
Two listings, same JD: Berlin https://www.linkedin.com/jobs/view/4482981150 · Munich https://www.linkedin.com/jobs/view/4483546505. Documents say Berlin; switch `\location` + letter line to Munich if you apply there (`scripts/rebuild.sh`).

## Likely interview questions
1. **"How would you test and monitor an LLM feature in production?"** Ground-truth eval sets in CI (RAGAS/PytrecEval thesis, Kniit P/R 33/45 → 93/90), deterministic checks first, then sampled LLM-judge; log latency/tokens/cost per request; alert on error/fallback rate. Be honest that production monitoring dashboards are the part you've done least.
2. **"Terraform?"** IaC so far with AWS CDK (Covestro, thesis infra). Concepts carry over (state, plan/apply, modules). Show the gateway repo once built.
3. **"Design an agent that helps a customer manage savings plans safely."** LangGraph with tools behind permission checks, human confirmation for any order (as Scalable's August launch does), audit log, eval set with adversarial prompts.

Also prepare: why leave Kniit (public line in profile), handling PII/regulated data, cost control of LLM calls ($200k → near zero story).

## Form fields
- **Why Scalable:** AI inside a regulated product with clear limits (Aug 2026: ChatGPT/Claude/Grok connected to accounts, trades still need confirmation); new AI work stream = chance to set the foundations.
- **Salary:** €70,000 gross/year (range 60–75k).
- **Notice / start:** 15 November 2026.
- **Work permit:** EU Blue Card, no sponsorship needed.
- **Location:** Berlin or Munich.
