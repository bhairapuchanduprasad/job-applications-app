# Project brief: Voice Receptionist Agent

Repo slug: `voice-receptionist-agent` (no link on the CV)
Status: **planned**. Build before submitting the eGroup Voice AI Product Engineer application.
Time box: 1–2 days with Claude Code.

## Goal
A real-time phone/voice receptionist for a small business (the eGroup / virtual-office use case): it answers a call, finds out who is calling and why, answers simple questions from the business's FAQ, takes a message or books a callback, and hands over to a human with a summary when needed. Built spec-first with Claude Code, with evals.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| Audelia Voice Agent platform: speech recognition, TTS, conversational AI, real-time voice | LiveKit Agents (Python) room + Deepgram STT + ElevenLabs TTS + LLM |
| Prompts, tool calls, RAG, agent logic, conversation flows for the voicebot | System prompt per business, tools `take_message`, `book_callback`, `lookup_faq` (RAG over FAQ), `handoff_to_human` |
| Evals; define tests the AI benchmarks its own code against | Spec (SPEC.md) + pytest acceptance tests written first; text-level conversation evals (golden transcripts: intent, required slots, handoff correctness) in CI |
| Monitor after launch | Per-call log: latency (STT, LLM, TTS), turns, tool calls, outcome; small React dashboard |
| AI-compatible knowledge base | `docs/` written for agents: CLAUDE.md, decisions log, how-to-extend, kept up to date while building |
| Full stack, React | React call-log dashboard + FastAPI backend |

## Scope
In:
- LiveKit Agents (Python) worker with Deepgram (STT) and ElevenLabs (TTS); browser test client via LiveKit playground (no phone number needed; optional SIP note in README).
- Business config YAML (opening hours, FAQ, staff, handoff rules); FAQ retrieval (small vector store or BM25).
- Tools as typed Python functions; message/callback stored in SQLite/Postgres.
- Eval: 20–30 golden conversations run in text mode (no audio) through the same agent logic; checks: correct intent, required fields captured, correct handoff; pass rate in GitHub Actions.
- Call log + React dashboard (latency per stage, outcomes).
Out: real telephony contracts, billing, multi-tenant auth, Java/Angular.

## Architecture
```
caller (browser/LiveKit) ─► LiveKit room ─► agent worker: Deepgram STT ─► LLM (prompts, tools, RAG) ─► ElevenLabs TTS
                                              │
                                              ├─ tools: lookup_faq, take_message, book_callback, handoff_to_human
                                              └─ call log (Postgres) ─► FastAPI ─► React dashboard
```

## Milestones
1. SPEC.md + acceptance tests + text-mode agent with tools (half day).
2. Voice: LiveKit + Deepgram + ElevenLabs (half day).
3. Golden-conversation evals in CI (2–3 h).
4. Call log + dashboard + README + demo video (2–3 h).

## README outline
Problem · Demo video · Architecture · Spec-first workflow with Claude Code · Evals and results (real numbers only after running) · Latency breakdown · Limits · Next steps (SIP telephony, more languages).

## Demo idea
60-second screen recording: a call asking for opening hours, then leaving a message; dashboard shows the call log and latency per stage.

## CV bullets it must live up to
- Real-time voice receptionist for a small business with LiveKit, Deepgram speech recognition and ElevenLabs text-to-speech: conversation flows, prompts and tool calls (FAQ via RAG, take a message, book a callback, handoff to a human with a summary).
- Built spec-first with Claude Code against acceptance tests; golden-conversation evals in CI and a React dashboard that monitors latency per stage, tool calls and call outcomes.
