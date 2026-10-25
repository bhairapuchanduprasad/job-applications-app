# Fit report: BITMARCK, Software Engineer Conversational AI (m/w/d), Essen (also Dresden, Hamburg, München, Frankfurt, Ludwigsburg, Magdeburg, Berlin)

**Fit score: 78/100.** Strong on LLMs (open-source and API), RAG, agents, Python, backend/REST, databases, LangChain and Hugging Face, Git and CI/CD. Gaps: no chatbot or voicebot shipped as such, pgvector and LlamaIndex not in the profile, no health-insurance domain. Essen is one of the listed locations and you live there.

Language: German posting with no stated German requirement → English documents (CLAUDE.md rule 3). Customers are statutory health insurers, so German will matter with stakeholders; B1 shown honestly.

Source: https://www.linkedin.com/jobs/view/4466081363 (LinkedIn label "Mid-Senior level"; no years stated).

## Requirements → evidence
| Requirement | Evidence | Rating |
|---|---|---|
| Chatbot/voicebot solutions on ML and GenAI | Covestro agentic LangGraph app routing user requests (vector DB queries, inference, summarisation) with React frontend; PrismaChat RAG evaluation (chat system) | 🟡 (no voicebot) |
| MLOps and DevOps methods | Docker, Kubernetes, AWS CDK, GitLab CI/CD; ground-truth evaluation loops | ✅ |
| Dialogue systems with LLMs, RAG, agents | Kniit multi-agent LangGraph pipeline; Covestro agentic app + RAG pipelines | ✅ |
| Backend + frontend to integrate AI models | FastAPI backends, React frontends (Covestro, Kniit Expert Interface), MCP service | ✅ |
| Python, OOP, backend, REST APIs, databases | Python everywhere; FastAPI, Postman; Postgres, MongoDB, Neo4j, DynamoDB | ✅ |
| Vector DBs (Qdrant, PGVector), similarity search | Qdrant, Pinecone, Azure AI Search, vector search; embedding benchmark on 1M+ chunks | ✅ Qdrant / ❌ pgvector |
| LLMs, open-source or API | LLM APIs via LiteLLM; Open Llama 3B QLoRA fine-tune (built) | ✅ |
| LangChain, LlamaIndex, Hugging Face | LangChain, Hugging Face Transformers ✅; LlamaIndex ❌ | 🟡 |
| Git, CI/CD, DevOps, agile teams | GitLab CI/CD, Git, Agile | ✅ |

## Gaps and honest framing
- **Chatbots/voicebots:** say the Covestro app was an agentic request-routing application with a React frontend and the thesis evaluated a RAG chat system (PrismaChat); no voice experience.
- **pgvector, LlamaIndex:** you used Postgres and other vector stores; LangChain instead of LlamaIndex. Quick to learn; don't claim.
- **GKV domain:** none. Analogy: regulated German energy sector, domain experts validating AI output.
- **German:** B1, improving.

## Red flags
- BITMARCK was hit by cyberattacks (2023); expect strong security and data-protection focus in interviews.
- "Mid-Senior" label; 3 years.

## Company hooks (sources)
1. Essen-based IT service provider for statutory health insurers, founded 2008 by company, guild and substitute health funds; provides the GKV software standard BITMARCK_21c|ng plus consulting, service and data-centre services. Source: https://www.cio.de/article/3661881/krankenkassen-gruenden-it-dienstleister-bitmarck.html
2. Tender documents describe more than 80% of German statutory health insurers as customers and around 25 million insured people (figures vary by source/year). Source: https://ted.europa.eu/de/notice/694561-2024/pdf
3. In November 2024 BITMARCK Service GmbH published an award for a multi-component enterprise LLM solution. Source: TED notice (via search; details not verified).
4. One of the largest IT providers in German healthcare, holding much health data; public interview on lessons from two cyberattacks. Source: https://background.tagesspiegel.de/digitalisierung-und-ki/briefing/wie-bitmarcks-cybersicherheit-nach-zwei-angriffen-aufgestellt-ist
