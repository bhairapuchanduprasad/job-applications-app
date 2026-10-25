# Application notes: AI Evaluation Engineer (Jobgether partner)

## Before submitting
1. Build `agent-eval-harness` (brief: `_work/project-brief-agent-eval-harness.md`). The CV describes it; interviewers will ask about Wilson CIs, Phoenix traces, the adversarial suite.
2. Check LinkedIn matches the CV (titles, dates, 33%/45% → 93%/90%); Jobgether's AI screen checks for inconsistencies.
3. Decide on the contractor question (below) before investing in interviews.

## Contractor vs. Blue Card (ask at the first screening)
"I hold an EU Blue Card, which is tied to employment in Germany. Can you engage me through an Employer of Record such as Deel or Remote with a German employment contract? A freelance contract would need separate approval from the immigration office."
If it's freelance only: get advice from the Ausländerbehörde before accepting. As a contractor, ask for €45–55/h to match €70k gross plus benefits.

## 3 likely interview questions
1. **"How would you evaluate a multi-turn agent that calls tools?"** Golden cases per conversation; deterministic checks first (tool-call payload schema, max tool calls / loop guard, final-state assertions, regex), then embedding similarity, then an LLM judge only for the rest. Run each case N times and report pass rate with a confidence interval, not a single run. Tie it to Kniit: measured each agent/prompt iteration against SAP-derived ground truth, P/R 33/45 → 93/90.
2. **"When would you NOT use LLM-as-a-judge?"** When a deterministic check can decide: schema, exact values, status codes. Kniit story: replaced a $200k projected LLM budget with code-based extraction and accuracy went toward 100%. Judges cost money, add variance, and need their own calibration.
3. **"Tell me about building something from scratch alone."** Kniit: sole developer of the whole extraction pipeline (ingestion → chunking → prompts → indexing → MCP query service → Expert Interface), reporting to the CTO. Thesis: built the RAG evaluation (RAGAS, PytrecEval, AWS Lambda/SQS/DynamoDB via CDK) and benchmarked embedding models on 1M+ chunks.

## Form fields
- **Why this role:** "Evaluation is the part of AI engineering I've owned in my last role and my Master's thesis: building ground truth, measuring every iteration, choosing deterministic checks where they're enough. A founding role where I design the evaluation architecture is the next step."
- **Why are you leaving Kniit:** "Kniit is an early-stage startup that restructured around a senior SAP-focused hire before its funding round; my position ended after I had built and handed over its knowledge-extraction pipeline end-to-end."
- **Salary / rate:** employment: €70,000 gross/year (range €60–75k). Contractor: €50/h (only after the Blue Card question is answered).
- **Notice period / start:** last day at Kniit 13 Nov 2026; available from 15 November 2026.
- **Location / time zone:** Essen, Germany (CET); can overlap 3+ hours with US Central (15:00–18:00 CET = 08:00–11:00 CT).
- **Work authorization:** EU Blue Card (Germany).
- **English:** business fluent. **German:** B1.
