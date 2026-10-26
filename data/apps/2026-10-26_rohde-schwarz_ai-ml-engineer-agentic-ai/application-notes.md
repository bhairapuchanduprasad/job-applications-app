# Application notes: Rohde & Schwarz, AI / ML Engineer - Agentic AI (Dresden)

Status: **build-first**. Build `agent-eval-harness` (R&S variant brief in this folder) before submitting; the CV describes it.
Submit via the LinkedIn posting: https://www.linkedin.com/jobs/view/4478472349 (German documents; posting requires very good German, you have B1).

## Likely interview questions
1. **"Wie evaluieren Sie ein agentisches System, z. B. auf Halluzinationen?"** Ground truth first (Kniit: SAP-derived; Covestro: chemist-provided), deterministic checks before LLM-as-a-judge, repeated runs because outputs vary, track P/R per change. Kniit 33/45 → 93/90; RAGAS + PytrecEval in the thesis. Mention the eval harness once built.
2. **"Wann setzen Sie kein LLM ein?"** Kniit high-volume stream: deterministic pipeline, $200k projected LLM budget → near zero, accuracy toward 100%.
3. **"Ihr Deutsch ist B1. Wie arbeiten Sie im Team in Dresden?"** Honest: B1, improving; technical work and documentation in English today. Be ready to answer in German.

Also prepare: MCP server design (tools, latency), MLOps beyond CI/CD (monitoring, model versioning: not done yet), responsible-AI/privacy evaluation (not done formally), why leave Kniit (public line in profile).

## Form fields
- **Why Rohde & Schwarz:** agentic AI on a measurement-driven platform; R&S already quantifies GenAI user experience (CMX500 testbed with China Mobile Research Institute, Jul 2026); evaluation is my strongest area.
- **Gehaltsvorstellung:** 70.000 € brutto/Jahr (range 60–75k), only if asked.
- **Frühester Eintritt:** 15. November 2026.
- **Arbeitserlaubnis:** Blaue Karte EU, no sponsorship needed.
- **Wohnort:** will be based in Dresden.
- **Deutsch:** B1 (no certificate).
