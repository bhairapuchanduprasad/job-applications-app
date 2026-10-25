# Application notes: BITMARCK, Software Engineer Conversational AI (m/w/d), Essen

Apply via the BITMARCK careers site or the LinkedIn posting (https://www.linkedin.com/jobs/view/4466081363). Locations: Essen, Dresden, Hamburg, München, Frankfurt, Ludwigsburg, Magdeburg, Berlin; up to 3 days mobile per week. Choose Essen.

## Likely interview questions
**1. "How would you build a RAG chatbot for a health insurer?"** Retrieval over approved documents only, citations in every answer, evaluation set with domain experts (RAGAS + ground truth, as in your thesis), fallback to a human, no personal data in prompts or logs, monitoring of answer quality. Evidence: PrismaChat evaluation, Kniit ground-truth loop (33/45 → 93/90).

**2. "Which vector database would you choose, Qdrant or pgvector?"** You used Qdrant, Pinecone and Azure AI Search; pgvector keeps vectors next to relational data in Postgres (simpler ops), Qdrant scales better for large collections and filtering. Be honest that you haven't used pgvector.

**3. "Tell us about integrating an LLM into a backend and frontend."** Covestro: LangGraph agent + FastAPI + React, Docker, AWS CDK, GitLab CI/CD. Kniit: MCP service, Expert Interface on Azure.

Also prepare: data protection and security (BITMARCK had cyberattacks in 2023); voicebot gap (speech-to-text + LLM + text-to-speech, no experience yet). "Why are you leaving Kniit?" → public line from profile.

## Form fields
- **Why BITMARCK?** You build the software most statutory health insurers run on; a chatbot there must be correct and careful with data, which is the kind of reliability work I have done.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000). Must be above the EU Blue Card threshold.
- **Earliest start:** 15 November 2026.
- **Work authorisation:** EU Blue Card (Germany).
- **Location:** Essen; open to other BITMARCK locations.
- **German level:** B1, improving.
