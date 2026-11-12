# Fit: xHeron, AI Harness Engineer (Berlin) — 74/100
Verdict: strong match on agent orchestration, context, MCP/tools, evaluation; weaker on proven production operation, observability/tracing and idempotent real-world tool effects.
German: No mention of German. Posting language English.

| Requirement | Evidence | |
|---|---|---|
| Production Python | Kniit sole developer, FastAPI microservices, Covestro deploy | ✅ |
| Substantial LLM system (not RAG-only) | Multi-agent LangGraph pipeline, deterministic fallback, MCP service | ✅ |
| Orchestration, state, context | Kniit agents, chunking/context strategies | ✅ |
| Tools/APIs with contracts | MCP query service, FastAPI | 🟡 |
| Evaluation / regression | RAGAS, PytrecEval, SAP ground truth P/R | 🟡 (no CI regression suites in work history) |
| Observability / traces | none in work history | ❌ (Projects: Agent Eval Harness, planned) |
| Permissions, idempotency, verifying effects | none | ❌ |
| Deterministic vs agent judgement | $200k LLM budget cut | ✅ |
| 2+ yrs | 3 yrs | ✅ |

Gaps: observability/trace tooling, idempotency and permissions, production incident ownership at scale (small startup only). Not listing German (no requirement).
Red flags: JD warns against "basic RAG" and framework reliance; my LangGraph use must be framed as control-flow understanding. Hospitality/short-term-rental domain is new to me.

## Hooks
- xHeron: "Service-as-Software" for short-term rental operators; agents take responsibility for guest communication, coordination, issue resolution (from the posting).
- Process: intro with CTO Friedrich, take-home case, VSOP participation (posting). No further web research done (unattended run).
