# Fit report: opta data Gruppe, AI-Engineer (w/m/x), Essen (hybrid)

**Fit score: 84/100.** Very strong on the core (LLM applications, RAG, agents, MCP, LLM APIs, Python, Docker/Kubernetes/CI-CD, RAGAS, fine-tuning, classic ML), and you already live in Essen. Gaps: Java, Langfuse/pgvector/Weaviate/FastMCP by name, healthcare domain, and German for daily work.

Language: posting is in German but does not state a German requirement → English documents (CLAUDE.md rule 3). Duz-Kultur and a German Mittelstand setting mean German is likely used day to day; B1 shown honestly.

## Requirements → evidence

| Requirement | Evidence | Rating |
|---|---|---|
| Informatik degree or comparable | MSc Artificial Intelligence (THWS) + Minor in CS & Engineering | ✅ |
| LLM-based applications (RAG, agents, chatbots) | Kniit multi-agent LangGraph extraction pipeline; Covestro agentic LangGraph app; Covestro RAG pipelines + PrismaChat RAG evaluation | ✅ |
| LLM APIs, prompt engineering, RAG architectures | Prompt engineering + LLM APIs (LiteLLM) at Kniit; RAG/GraphRAG; chunking, vector DBs, indexing at Covestro | ✅ |
| Python (and Java) | Python across all roles | ✅ Python / ❌ Java |
| Vector DBs (Qdrant, Weaviate, pgvector) | Qdrant, Pinecone, Azure AI Search; Postgres (not pgvector) | 🟡 |
| MCP servers | MCP query service exposing the knowledge graph to Claude Code (Kniit) | ✅ |
| LangChain / FastMCP | LangChain ✅; FastMCP not named in profile | 🟡 |
| OpenAI / Anthropic APIs, open-source models | Generic "LLM APIs" + LiteLLM; Claude Code daily; Open Llama 3B QLoRA (open-source). Provider names not in profile | 🟡 |
| GenAI to make developers more efficient (coding agents, automation, docs) | Claude Code with custom skills + agentic coding workflows; MCP service built specifically for Claude Code | ✅ (strong talking point) |
| Feasibility analyses / solution strategies | Covestro AI Consulting Intern: advised business stakeholders on agentic AI, translated requirements into the approach; Kniit: chose deterministic code over LLM for a stream | ✅ |
| Retrieval pipelines, embeddings, answer-quality evaluation | Benchmarked multilingual embedding models on 1M+ chunks; RAGAS + PytrecEval vs ground truth | ✅ |
| Monitoring/evaluation/improvement in production | Ground-truth evaluation loop (33/45 → 93/90); no production monitoring tooling named | 🟡 |
| Docker, Kubernetes, CI/CD | Docker, Kubernetes (Kniit), GitLab CI/CD (Covestro), AWS CDK | ✅ |
| Langfuse, RAGAS | RAGAS ✅; Langfuse ❌ (project covers it) | 🟡 |
| Fine-tuning | Open Llama 3B QLoRA (built repo); fine-tuning models for retrieval (Covestro) | ✅ |
| Classic ML | Random Forest, XGBoost, LSTM, ARIMA/SARIMA/Prophet (Covestro, Cognizant) | ✅ |
| Fast learner, analytical, independent | Sole developer at a startup reporting to CTO | ✅ |
| Healthcare domain (implicit) | None | ❌ |

## Gaps and honest framing
- **Java:** not in the profile. Say Python is your main language; you can read and integrate with Java services but haven't built in Java. Don't claim it.
- **Langfuse / FastMCP / pgvector / Weaviate:** adjacent experience (built an MCP service; Qdrant/Pinecone/Azure AI Search; Postgres). The planned project adds Langfuse and FastMCP for real.
- **OpenAI/Anthropic by name:** the profile says "LLM APIs". If you used specific providers at Kniit/Covestro, add them to the profile and they can go on future CVs.
- **Healthcare:** none; analogous experience is domain-expert validation (SAP experts, chemists).
- **German B1:** likely internal language. Mention you're improving it.

## Red flags
- Reposted, 100+ clicked apply: competitive; apply fast via their careers site.
- No salary range. Family company, 3,000 staff: likely structured pay bands; €70k may be at the top for this level.
- Java listed as a primary language: they may prefer someone who can also work in their Java codebases.

## Company hooks (sources)
1. **Scale and breadth:** over 60,000 customers and over 100,000 users across care, therapy (Heilmittel), medical supply (Hilfsmittel), midwives and rescue services. Source: https://www.optadata.de
2. **Many software products:** od | care, thevea, od | flow, od | focus, od | mio, the CareMan suite, plus billing and od | assist. Many products and developers means a lot to gain from developer tooling and documentation automation, which is exactly the role's second focus. Source: https://www.optadata.de
3. **Billing and approval workflows:** billing with insurers, support for approval procedures (Genehmigungsverfahren), TI connection; document-heavy processes where RAG and extraction fit. Source: https://www.optadata.de
4. **Family-run, 50+ years, Essen headquarters:** "Familiengeführt, innovativ & vorausschauend"; founded 1970 in Essen. Sources: https://www.optadata.de , https://www.startbase.com/news/essener-opta-data-gruendet-start-up-aus
5. **Innovation track record:** spun off thevea (2021) to digitalise therapy practices. Source: https://www.startbase.com/news/essener-opta-data-gruendet-start-up-aus
- No public news about opta data's AI work found.
