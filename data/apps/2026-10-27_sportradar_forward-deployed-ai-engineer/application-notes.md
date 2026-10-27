# Application notes: Sportradar, Forward Deployed AI Engineer, Leipzig (on-site)

Status: **build-first** (Agent Eval Harness is `planned`: build it, or remove it from the CV before submitting). For Sportradar, build it over a mocked match-data API.
Apply via: https://www.linkedin.com/jobs/view/4484093079 (identical posting 4481885941: apply once).
ATS coverage: 91%. Gaps: quality dashboards for LLM evals, sports/betting domain.
Process: screening → take-home task → 2 technical interviews.

## Likely interview questions
1. **"A department says 'we want AI'. How do you start?"** Sit with them, map the workflow and data, find the costly step, decide if an LLM is needed at all (Kniit: deterministic pipeline beat the LLM for the high-volume stream, $200k → ~0), build a small version, measure it against a test set.
2. **"How do you evaluate an LLM/agent solution?"** Ground-truth test set + precision/recall (Kniit 33/45 → 93/90), RAGAS/PytrecEval (thesis), deterministic checks first then LLM-as-judge, run in CI.
3. **"Tell us about working independently with competing priorities."** Sole developer at Kniit reporting to the CTO; planning own work, SAP domain experts as stakeholders.

## Form answers
- **Why Sportradar:** sports data at scale and generative AI already in the product (match reports/previews from live data); FDE role = consulting + building, which matches Covestro + Kniit.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000).
- **Notice period / earliest start:** 15 November 2026.
- **Work authorization:** EU Blue Card (Germany).
- **Location:** Leipzig, on-site 5 days; travel fine.
- **German level:** B1 (no certificate).
- **Why leaving Kniit:** "Kniit is an early-stage startup that restructured around a senior SAP-focused hire before its funding round; my position ended after I had built and handed over its knowledge-extraction pipeline end-to-end."
