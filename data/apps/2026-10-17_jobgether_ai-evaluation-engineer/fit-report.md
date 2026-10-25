# Fit report: AI Evaluation Engineer (Jobgether partner, undisclosed)

**Fit score: 70 / 100.** The core of the role fits well: I have built LLM evaluation against ground truth twice (Kniit, Covestro thesis), and the "deterministic checks before LLM-as-a-judge" philosophy is exactly what I did at Kniit ($200k → near zero). The gaps are around the edges: GitHub Actions specifically, tracing tools, adversarial/prompt-injection testing, multi-run statistics and load testing. The biggest risk isn't skills. It's the **independent-contractor arrangement versus my EU Blue Card** (see red flags).

## Requirements → evidence

| Requirement | Evidence | |
|---|---|---|
| Python for API testing, async, automated testing | 3 yrs Python; FastAPI backends, Postman API testing (Covestro); Python microservices (Kniit). Async/headless not explicitly in profile | 🟡 |
| Hands-on LLM evaluation pipelines | Kniit: eval vs SAP-derived ground truth as quality gate, P/R 33%/45% → 93%/90%. Thesis: automated RAG generation + retrieval eval (RAGAS, PytrecEval) vs chemist ground truth on AWS Lambda/SQS/DynamoDB | ✅ |
| Statistical testing across repeated runs, confidence intervals | Precision/recall measurement, embedding benchmarks; repeated-run pass rates / CIs not in profile | 🟡 |
| CI/CD integration, GitHub Actions or similar | GitLab CI/CD (Covestro). Not GitHub Actions ("or similar" covers it) | 🟡 |
| Deterministic checks before LLM-as-a-judge (schema, regex, embedding similarity) | Kniit deterministic code-based extraction pipeline instead of LLM calls; embedding model benchmarking (1M+ chunks) | ✅ |
| Validate structured outputs: JSON schema, OpenAPI, function-calling | Structured entity/relationship extraction into a knowledge graph; FastAPI REST APIs. JSON schema / OpenAPI validation as such not stated in profile | 🟡 |
| Observability/tracing (OpenTelemetry, LangSmith, Phoenix, Weave, custom logging) | None in profile | ❌ (project covers it) |
| Own an evaluation architecture from scratch | Sole developer of the full Kniit pipeline, reporting to CTO; thesis eval system built alone | ✅ |
| Multi-turn agent test suites, tool-call loop safeguards | Built multi-agent LangGraph systems (Kniit, Covestro), not test suites for them | 🟡 (project covers it) |
| Adversarial testing / prompt injection | None in profile | ❌ (project covers it) |
| Caching/mocking to reduce LLM API calls | Cost reduction by replacing LLM calls with code (Kniit); LiteLLM. Caching/mocking not explicit | 🟡 |
| Agent frameworks (LangChain, LlamaIndex, AutoGen, CrewAI) / sandboxes | LangChain, LangGraph (both roles) | ✅ |
| Embedding models, vector DBs for similarity testing | Multilingual embedding benchmark on 1M+ chunks; Qdrant, Pinecone, Azure AI Search, vector search | ✅ |
| Load testing non-deterministic endpoints | None | ❌ (project touches it) |
| Excellent English | Business fluent | ✅ |
| 3h daily overlap with US Central Time | 15:00–18:00 CET = 08:00–11:00 CT. Easy from Germany | ✅ |

## Gaps and honest framing
- **GitHub Actions**: say GitLab CI/CD; the concepts transfer directly. The planned project uses GitHub Actions.
- **Tracing tools (OpenTelemetry / Phoenix / LangSmith)**: no work experience. Covered only by the planned project; do not claim in experience.
- **Adversarial / prompt-injection testing, load testing, multi-run CIs**: no work experience. The planned project covers these; it must be built before submitting so you can talk about it.
- **JSON schema / OpenAPI / function-calling validation**: adjacent (structured extraction, FastAPI). The project makes it concrete.
- Async Python: don't claim beyond what's in the profile.

## Red flags
1. **Independent contractor, hourly, paid by wire transfer.** My EU Blue Card is tied to employment. Self-employed or freelance work normally needs separate permission from the Ausländerbehörde (the residence permit must say "selbständige Tätigkeit gestattet"), and a foreign-client contractor deal does not satisfy the Blue Card salary rules. **Clarify before signing anything**: ask whether they can hire through an Employer of Record (Deel, Remote, Lano etc.) with a German employment contract above the Blue Card threshold. Jobgether partners with Deel and Lano, so this may be realistic.
2. **Undisclosed company.** I can't research the employer or tailor a company hook. The letter addresses the role, not the company.
3. **No benefits (contractor)**: the hourly rate has to cover health insurance, pension and holidays. €70k/yr salary ≈ €45–55/h as a contractor to come out equal.
4. **Jobgether screens with AI and checks for "inconsistencies"**: keep CV and LinkedIn consistent (dates, titles). The Kniit P/R figure (33%/45% → 93%/90%) is now consistent in profile and base CV; make sure LinkedIn matches.
5. Positive: only 12 applicants, posted 5h ago. Apply fast.

## Company research
Max searches done (4). The partner company is not named and its posting text could not be found on other boards (closest match, a Dice "AI Evaluation Engineer" independent-contract listing, is gone: HTTP 410).
- Jobgether is a remote-job platform that pre-screens applicants with AI and forwards a shortlist to the hiring company ([jobgether.com/how-jobgether-works](https://jobgether.com/how-jobgether-works)).
- Jobgether partners with EOR/contractor platforms Deel and Lano ([lano.io](https://www.lano.io/de/marketplace/ecosystem/lano-and-jobgether), [maddyness.com](https://www.maddyness.com/uk/?p=713654)), relevant for the Blue Card question.

### Hooks (from the JD itself, since the company is hidden)
1. "Founding" eval engineer: they want someone to own the architecture alone → mirrors my sole-developer role at Kniit.
2. "Deterministic checks before LLM-as-a-judge" → my strongest story ($200k LLM budget → near zero with code-based extraction).
3. "Golden datasets" → I built ground truth from SAP systems and with chemists; I know golden data is the hard part.
4. Embedding similarity testing → 1M+ chunk multilingual embedding benchmark.
