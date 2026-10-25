# Project brief: Meter Read Plausibility Agent

Repo slug: `meter-read-plausibility-agent` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the SAP application.
Time box: 1–2 days with Claude Code.

## Goal
A small agentic system for one step of meter-to-cash: implausible smart-meter readings. Rule-based checks screen every 15-minute interval read quickly and cheaply; only the ambiguous cases go to an LLM agent. The agent retrieves the relevant metering rules from a small document set (semantic retrieval), explains what is wrong and proposes a resolution (e.g. estimate, request re-read, flag device), which a human approves. Every decision is logged with its sources; personal data is masked before any LLM call.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "solutions and agents in metering concept management / distributed energy resources" | Agent for implausible meter readings (SAP itself plans an Implausible Meter Reading Resolution Agent) |
| "optimizing complex, high-throughput systems for performance and cost efficiency" | Rules screen all reads; LLM only for the ambiguous few; cost and latency logged per read |
| "agentic engineering, agentic orchestration" | LangGraph graph: classify → retrieve rules → reason → propose → human approval |
| "semantic retrieval", "context engineering" | Embedded rule documents (validation rules, VDE/BDEW-style plausibility checks written as your own summaries), top-k retrieval into the agent context |
| "governance, security, compliance, data and privacy" | Audit log (decision, sources, model, cost), PII masking (customer name, address, meter ID hashing), read-only tools |
| "AI output quality assurance" | Labelled set of 50 synthetic cases scored in CI (correct resolution, cites the right rule) |
| "cloud-native patterns" | FastAPI service, Docker, CI/CD; optional deploy |

## Scope (keep it small)
In:
- Synthetic data generator: households with 15-min load profiles + PV feed-in; inject faults (negative consumption, spikes, gaps, counter reset, swapped feed-in/consumption).
- Rule engine (pandas): flags clear errors and clear passes; marks the rest "ambiguous".
- Rule documents: 8–12 short markdown files written by you (no copyrighted standards text), embedded into a local vector store.
- LangGraph agent with tools: `get_meter_history`, `search_rules`, `propose_resolution`; LLM via LiteLLM (any provider or local Ollama).
- PII masking layer before LLM calls; audit log in SQLite/Postgres.
- FastAPI endpoints: `/check` (batch), `/cases/{id}`, `/approve`.
- Eval: 50 labelled cases; CI reports accuracy, share sent to LLM, cost per 10k reads, p95 latency.
Out: real MaKo/EDIFACT messages, SAP system integration, UI beyond a simple table.

## Architecture
```
meter reads (synthetic) ─► rule engine ──clear──► pass / auto-flag
                               │
                           ambiguous
                               ▼
                 LangGraph agent ──► search_rules (vector store of rule docs)
                      │           └► get_meter_history
                      ▼
            PII masking ─► LLM (LiteLLM) ─► proposed resolution ─► human approval (/approve)
                      ▼
                 audit log (decision, sources, tokens, cost, latency)
CI: pytest + eval on 50 labelled cases
```

## Milestones
1. Data generator + fault injection. (≈2 h)
2. Rule engine + throughput test (e.g. 1M reads). (≈2 h)
3. Rule docs + embeddings + retrieval tool. (≈2 h)
4. LangGraph agent + masking + audit log. (≈3 h)
5. FastAPI + eval + CI. (≈2 h)
6. README with architecture diagram and trade-offs. (≈1 h)

## README outline
Problem (implausible reads block billing) → Architecture → Why rules first, LLM second (throughput and cost) → Governance (audit, masking, human approval) → Eval results → Limitations (synthetic data, no MaKo) → How I used Claude Code.

## CV bullets this project must live up to
- Agentic workflow for implausible smart-meter readings at utilities: rule-based checks screen every interval read at high throughput, and only ambiguous cases go to an LLM agent that retrieves the relevant metering rules by semantic retrieval and proposes a resolution for human approval.
- Governance by design: every agent decision is written to an audit log with its sources, personal data is masked before any LLM call, and a labelled test set checks accuracy, cost, and latency in a CI/CD pipeline.

When done, mark it `built` in `profile/master-profile.md`; then real numbers (reads/second, share sent to the LLM, eval accuracy) may go on the CV.
