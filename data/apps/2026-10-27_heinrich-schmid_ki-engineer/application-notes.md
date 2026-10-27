# Application notes: Heinrich Schmid (Systemhaus GmbH), KI-Engineer (m/w/d), Reutlingen

Status: **build-first** (Product Q&A Assistant, n8n, is `planned`: build it, or remove it from the CV before submitting).
Apply via: https://www.linkedin.com/jobs/view/4483644272; employer prefers applications **by email** with salary expectation and start date (both in the letter).
English docs (German posting, no German level stated). Decision for user: send a German Anschreiben instead? ATS coverage: 90%. Gaps: n8n/Make, legacy-application integration.

## Likely interview questions
1. **"Wie würden Sie ein LLM in eine bestehende (Legacy-)Anwendung bringen?"** Wrap as a FastAPI/MCP service with a clear API, start read-only, human approval for uncertain cases, logging + eval set; Kniit MCP service as the example.
2. **"RAG with your own data: how do you prepare it and decide whether to fine-tune?"** Thesis: chunking, indexing, embedding benchmarks on 1M+ chunks, RAGAS/PytrecEval; fine-tune retrieval models / QLoRA only when retrieval + prompting isn't enough.
3. **"Which AI tools would you pick for a trades company?"** Evaluate on a labelled set (quality, cost, latency, data protection); n8n for simple workflows, Python services where logic gets complex.

## Form answers
- **Why Heinrich Schmid:** AI close to real day-to-day processes in a large family-run trades group; build and integrate, not just slides.
- **Salary expectation:** EUR 70,000 gross/year (in the letter).
- **Notice period / earliest start:** 15 November 2026.
- **Work authorization:** EU Blue Card (Germany).
- **Location:** Reutlingen; mobile work possible.
- **German level:** B1 (no certificate).
- **Why leaving Kniit:** "Kniit is an early-stage startup that restructured around a senior SAP-focused hire before its funding round; my position ended after I had built and handed over its knowledge-extraction pipeline end-to-end."
