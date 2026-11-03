# Application notes: mamgo / YER Deutschland (client undisclosed), AI Support Engineer, Munich

Before submitting:
- Ask the recruiter for the client name and contract type (direct hire or Arbeitnehmerüberlassung); check the salary meets the Blue Card threshold.
- Build Self-Hosted LLM Inference Platform (_work/project-brief-self-hosted-llm-inference.md) or remove the Projekte section.
- Application goes through YER's online portal, with salary expectation and earliest start (both in the Anschreiben).

## Likely interview questions
1. Ein LLM-Inferenzdienst antwortet plötzlich sehr langsam. Wie gehen Sie vor?
   → Logs/metrics first (pod status, GPU/CPU, queue), reproduce with a script, compare against last version; Kniit: measured every change against ground truth.
2. Wie testen Sie eine neue Version von LiteLLM oder vLLM vor dem Rollout?
   → Smoke tests in Python (health, completion, streaming, latency), staging first, rollback plan; GitLab CI/CD and Postman API tests at Covestro.
3. Wie unterstützen Sie Entwickler bei Cursor oder Copilot?
   → Daily Claude Code use with custom skills and MCP integration; know where agentic coding tools help and where they fail.

## Form answers
- Gehaltsvorstellung: 70.000 € brutto/Jahr (range €60–75k).
- Frühester Eintritt: 15.11.2026. Blaue Karte EU. Deutsch B1.
