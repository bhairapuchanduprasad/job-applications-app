# Application notes: Python & GenAI Developer – AWS Bedrock / Remote (recruiter)

## Ask the recruiter first (before investing more)
1. **"Handelt es sich um eine Festanstellung bei Ihnen (Arbeitnehmerüberlassung) oder um ein Freelance-Projekt?"** (Is this permanent employment with you, or freelance?) With an EU Blue Card you need employment; freelance doesn't fit. The Blue Card also generally needs a contract of at least 6 months.
2. **"Ist ein Start am 16.11.2026 möglich?"** (Your Kniit contract ends 13.11.2026; the project starts 03.11.)
3. Salary (gross per year) if employed via the agency; must meet the Blue Card minimum (€45,934.20 recent-graduate rate / €50,700).
4. Who is the end client, and is a security clearance (Sicherheitsüberprüfung) needed?

## Before submitting
- Build `it-ticket-assistant-bedrock` (brief in this folder), or remove the Projects section. Bedrock is a must-have, so at minimum do milestone 1–2 before an interview.

## Likely interview questions
1. **"Welche Erfahrung haben Sie mit Amazon Bedrock?"** (Your Bedrock experience?) Be honest: AWS yes (CDK, Lambda, SQS, DynamoDB at Covestro); Bedrock via the project (once built). Explain how Bedrock Agents/Knowledge Bases map to what you did in LangGraph/RAG.
2. **"Wie testen Sie LLM-Funktionalität?"** (How do you test LLM features?) Unit tests with mocked model calls, integration tests on a dev stack, a labelled evaluation set (Kniit P/R vs SAP ground truth; RAGAS at Covestro).
3. **"Wie gehen Sie mit personenbezogenen Daten in KI-Verfahren um?"** (Personal data in AI systems?) Data minimisation, PII masking before model calls (Guardrails), EU region, least-privilege IAM, logging, no training on customer data, human approval.

## Form answers
- **Verfügbarkeit (availability):** ab 16.11.2026.
- **Gehaltsvorstellung (salary):** €70,000 gross/year if employed (profile default); daily rate only relevant for freelance, which doesn't fit the Blue Card.
- **Arbeitsort (location):** remote, Germany.
- **Aufenthaltstitel (work permit):** Blaue Karte EU.
- **Sprachen:** Deutsch B1, Englisch verhandlungssicher.
