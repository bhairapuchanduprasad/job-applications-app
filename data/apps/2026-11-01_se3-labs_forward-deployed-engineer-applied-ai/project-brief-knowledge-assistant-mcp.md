# Project brief: Knowledge Assistant for Internal Documents, SE3 Labs variant ("Offline Field Knowledge Assistant")

Repo slug: `knowledge-assistant-mcp` (same repo as the Finanz Informatik base version; no link on the CV)
Status: **planned**. Build before submitting the SE3 Labs Forward Deployed Engineer, Applied AI application.
Time box: 1–2 days with Claude Code. Base brief: applications/2026-10-11_finanz-informatik_ai-engineer/_work/project-brief-knowledge-assistant-mcp.md (LlamaIndex RAG, local LLM, FastAPI + MCP, eval in CI are shared).

## Goal
An LLM-powered assistant that works with no network on one laptop, the way software for operators in the field has to: spoken or typed questions over public operational manuals, cited answers, refusal when the manuals don't cover it, plus the habits of a forward deployed engineer (field-test checklist, demo script, logs for on-site debugging).

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| Applications in which LLMs play a central role, deployable in real operational environments | Local open-source LLM via Ollama (e.g. Llama 3.1 8B / Qwen 2.5 7B), LlamaIndex RAG, no cloud calls |
| Field testing & troubleshooting | `FIELD_TEST.md` checklist (airplane mode, low battery/power profile, noisy audio, cold start time); structured request logs (JSONL) + `diagnose.py` |
| Demonstrations & delivery | `DEMO.md` 5-minute script + sample questions |
| Customer integrations, maintainable and reusable | FastAPI REST API + MCP server so other tools/agents can call it; per-customer config file (doc folder, model, language) |
| Python, software architecture | Clean module layout, pytest, typed config |
| (company) voice control | Whisper (faster-whisper, local) for spoken questions |

## Scope
In: public manuals (e.g. THW/civil-protection or public equipment manuals with permissive licence; check licence); ingestion + chunking; LlamaIndex with local embeddings (bge-small); Ollama LLM; citations with page numbers; "not covered" refusal rule; faster-whisper for audio input; FastAPI + MCP server (FastMCP); labelled question set (answerable / not answerable) scored for groundedness and refusal accuracy in GitHub Actions (small model or mocked LLM in CI); JSONL logs; FIELD_TEST.md, DEMO.md.
Out: classified/military data, GPU servers, mobile app, text-to-speech.

## Architecture
```
mic/typed question ─► faster-whisper (local) ─► FastAPI /ask ─► LlamaIndex retriever (local embeddings, on-disk index)
                                                     └─► Ollama LLM ─► answer + citations | "not covered"
MCP server (ask, search_manual) ─┘          logs/*.jsonl ─► diagnose.py
```

## Milestones
1. Ingest + index + /ask with citations (half day).
2. Refusal rule + labelled question set + CI (2–3 h).
3. Whisper input + MCP server (2–3 h).
4. Field-test checklist run in airplane mode, demo script, README (2 h).

## README outline
Problem · Offline design choices · Setup on a laptop · API + MCP · Evaluation (real numbers only after running) · Field test results · Limits · Next steps.

## Demo idea
Laptop in airplane mode: ask a spoken question, get a cited answer; ask something outside the manuals, get a refusal; show the log line used to debug it.

## CV bullet it must live up to
- Built a fully offline laptop assistant where a local open-source LLM answers spoken or typed questions over public operational manuals with RAG and cites sources, served via FastAPI and an MCP server; eval set and pytest in GitHub Actions, a field testing checklist and a demonstration script.
