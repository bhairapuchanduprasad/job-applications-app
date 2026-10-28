# Fit report: Alago, Founding AI Engineer (Munich, hybrid 3 days)

Source: https://www.linkedin.com/jobs/view/4482287193 (found by job-scout 2026-10-28)

**Fit score: 76/100.** Strong match on the core problem (multi-agent extraction/reasoning/evaluation over long technical documents, graph memory, production reliability); the gap is the TypeScript/Next.js frontend stack.

| Requirement | Evidence | |
|---|---|---|
| Multi-agent harnesses (extraction, reasoning, evaluation stages) over long documents | Kniit: LangGraph entity-extraction, relationship-analysis, consolidation, reflection agents on regulatory/technical documents; P/R 33/45 → 93/90 | ✅ |
| Context / what to remember and surface | Kniit chunking + indexing strategies (agentic, deterministic, monolithic); MCP query service over the knowledge graph | ✅ |
| Project memory / decision graph | Kniit knowledge graph in Neo4j, GraphRAG, Expert Interface for curating graph changes | ✅ |
| Measure everything, reliability | SAP-derived ground truth eval at Kniit; RAGAS/PytrecEval thesis | ✅ |
| Reason from user pain to outcome; non-technical customers | Kniit SAP domain experts; Covestro AI consulting with business stakeholders, chemists | ✅ |
| Postgres + pgvector, LangChain | Postgres, LangChain, vector search (Kniit); pgvector only in planned projects | 🟡 |
| TypeScript, React, Next.js | React frontends (Kniit Expert Interface, Covestro); TypeScript/Next.js not in profile; CV says React (beginner) | 🟡/❌ |
| Vercel, Supabase, Vercel AI SDK, LangFuse | Not in profile (LangFuse only in a planned project) | ❌ |
| Prototype fast, own end to end, startup | Sole developer at an early-stage startup reporting to CTO; Claude Code workflows | ✅ |
| German for customer calls | Not required; B1 | ok |

## Gaps and framing
- Both CV projects (Order Inbox Agent, Spec-Driven Coding Agent Harness) are status planned: build both before submitting; they carry the only TypeScript, pgvector and LangFuse evidence.
- TypeScript/Next.js: say React frontends shipped at Kniit and Covestro; TypeScript is the next step. Don't claim it.
- Vercel/Supabase/Vercel AI SDK/LangFuse: leave out of CV; LangFuse via the planned Spec-Driven Coding Agent Harness project (build first).
- Messy German protocols: B1 German is enough to read structure, but not to claim fluency.

## Red flags / notes
- Pre-seed, 0.5–1.5% equity, 1.5-year cliff (longer than usual 1 year). Salary not stated: check it meets the Blue Card threshold.
- 3 days/week on-site in Munich; onsite case study with ~4h prep.
- Same company also posts "Founding AI Engineer – Full-Stack" and "Founding Full-Stack Engineer" (join.com); this posting is the AI one.

## Hooks (research)
1. Pre-seed round (seven-figure, oversubscribed) led by Realyze Ventures with D11Z. Ventures and CDTM Venture Fund, announced June 2025 (Heuking: https://www.heuking.de/en/news-events/latest-news/article/heuking-advises-munich-based-ai-contech-startup-alago-on-its-pre-seed-funding-round.html).
2. Platform turns meeting minutes, emails, contracts and invoices into structured data for construction project management (seedtable/dealroom summaries).
3. JD: live on an autobahn programme and an S-Bahn transit programme; 25+ live customers; decision graph built from meeting transcripts.
4. JD: "The model isn't the moat. The project memory is." Matches the Kniit knowledge-graph work directly.
