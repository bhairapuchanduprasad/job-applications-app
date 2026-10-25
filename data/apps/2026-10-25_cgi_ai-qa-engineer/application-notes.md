# Application notes: CGI, AI QA Engineer – Conversational AI & GenAI-Automationen (Eschborn)

Status: **build-first** (build `agent-eval-harness`, CGI variant, before submitting; brief in `_work/project-brief-agent-eval-harness.md`).

## Likely interview questions
1. **"Wie testen Sie einen Chatbot, dessen Antworten nicht deterministisch sind?"**
   Layered: deterministic checks first (schema, tool-call payloads, expected handover, forbidden strings), then semantic similarity, LLM-as-a-judge only for what remains; each case run several times, pass rate with confidence interval. Real proof: Kniit ground-truth evaluation (precision/recall 33/45 → 93/90 after prompt and agent changes); thesis RAGAS + PytrecEval separating generation from retrieval.
2. **"Sie haben noch keine klassische QA-Rolle und kein Selenium – warum passen Sie trotzdem?"**
   The role is about AI-specific quality; that has been the core of my work for two years (thesis, Kniit). API testing with Postman, GitLab CI/CD, Docker, AWS CDK cover the delivery side. Selenium/ISTQB: honest gap, open to certifying (ISTQB CTFL → TAE).
3. **"Wie würden Sie Prompt Injection und Data Leakage testen?"**
   Only talk from the harness once it is built: injected instructions in user turns and tool responses, canary secrets in system prompt and other-customer data in mocked APIs, role-based tool permissions, security gate at 100% in CI. At work: expert approval step before graph changes (human quality gate).
Also prepare: a short part of the interview in German (B1).

## Form fields
- **Warum CGI?** CGI builds a new team for large conversational/GenAI programmes and brings chat assistants into production with Cognigy (e.g. flight rebooking for a German aviation client); "Customer Zero" testing of GenAI use cases internally fits my evaluation background.
- **Gehaltsvorstellung:** €70,000 gross/year (range €60,000–75,000).
- **Kündigungsfrist / frühester Eintritt:** available from 15 November 2026.
- **Arbeitserlaubnis:** Blaue Karte EU, no sponsorship needed.
- **Standort / Reisen:** will be based in Eschborn; happy to travel to client sites.
- **Deutschkenntnisse:** B1 (no certificate); English business fluent.
