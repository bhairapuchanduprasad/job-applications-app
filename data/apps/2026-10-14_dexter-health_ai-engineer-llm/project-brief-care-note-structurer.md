# Project brief: Care Note Structurer

Repo slug: `care-note-structurer` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the dexter health application.
Time box: 1–2 days with Claude Code.

## Goal
A small service that takes a dictated care note (as a transcript, German or English) and returns a draft structured entry: vital signs, wound notes, care measures, free-text report. Every draft is validated against a schema; if a model's output fails validation or the call times out, the service retries and then falls back to a second model. A review screen lets a user accept or correct each field. An evaluation script scores each model on a labelled test set.

This mirrors dexter.mobile's flow (dictate → AI drafts → nurse checks → system of record) at toy scale, using only synthetic data.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "LLM-based workflows, structured outputs, validation logic, and fallback behavior" | Pydantic schema + JSON output, validation, retry, fallback chain |
| "Work with commercial and open-source LLMs without being tied to one specific provider" | Provider adapter interface: one commercial API + one self-hosted open-source model |
| "Support self-hosted model workflows" / "self-hosted LLMs, model serving" | Local open-source model served via Ollama (or vLLM if you have a GPU) |
| "Build evaluation loops, tests, and quality checks for AI-generated outputs" | Labelled synthetic test set, field-level precision/recall per model, run in CI |
| "Improving latency, cost, quality, or reliability" | Per-request latency logging; compare models on quality vs latency |
| "Structured data extraction, documentation automation, voice workflows" | Care-note → structured entry; optional Whisper transcription step |
| "Frontend or fullstack" | Small React review screen |
| Healthcare domain | Nursing documentation categories (Vitalwerte, Wunden, Maßnahmen, Bericht) |

## Scope (keep it small)
In:
- Pydantic models: `CareEntry` with `vitals` (BP, pulse, temp, SpO2, weight; units + plausible ranges), `wound` (location, size, stage, treatment), `measures` (list), `report` (text), `uncertain_fields`.
- Validation logic beyond schema: plausibility ranges (e.g. pulse 20–250), unit normalisation, "don't invent values not present in transcript" check (every numeric value must appear in the source text).
- Adapters: commercial LLM API (Anthropic or OpenAI, JSON/structured output mode) + local open-source model via Ollama (e.g. a Llama/Qwen/Mistral instruct model). Common interface.
- Fallback chain: model A → retry with validation errors fed back once → model B. Log which path each request took.
- FastAPI: `POST /structure` (transcript in, draft + validation report out), `GET /metrics`.
- 30–50 synthetic German care-note transcripts with hand-labelled expected entries (generate drafts with Claude Code, then correct by hand). NO real patient data.
- `make eval`: field-level precision/recall, schema-valid rate, hallucinated-value rate, p50/p95 latency per model; results to a markdown table. Runs in CI (GitHub Actions) with the local model mocked or a small model.
- React page: paste transcript → see draft fields with validation flags → accept/edit.
- Optional stretch: Whisper (local) to turn a short audio clip into a transcript.
Out: auth, real care-software integration, deployment, real health data.

## Architecture
```
transcript (or audio → Whisper) ─► FastAPI /structure
                                     │
                                     ├─► adapter A (commercial LLM, JSON mode) ─┐
                                     │        validation fail / timeout         │
                                     ├─► retry A with error feedback            ├─► Pydantic + plausibility + grounding checks
                                     └─► adapter B (self-hosted, Ollama) ───────┘
                                     ▼
                         draft CareEntry + validation report ─► React review screen
                         request log (SQLite: model, path, latency, valid?) ─► /metrics
eval/ (labelled synthetic set) ─► make eval ─► results table (per model) ─► CI
```

## Milestones
1. Schema + validation rules + grounding check, with tests. (≈2.5 h)
2. Two adapters + fallback chain + request log. (≈3 h)
3. Synthetic dataset (30–50 notes) + labels. (≈2 h)
4. `make eval` + results table + CI. (≈2 h)
5. React review screen. (≈2 h)
6. README, screenshots, demo GIF. (≈1.5 h)

## README outline
Problem (documentation burden in care) → What it does → Schema & validation rules → Fallback design → Evaluation method & results table (commercial vs self-hosted: quality, valid-rate, latency) → Failure cases I found and how I debugged them → "How I used Claude Code" → Run locally → Limitations (synthetic data, not a medical device).

## Demo idea
Paste a note with a typo'd value ("Puls 7O") and a value not in the text: the draft flags the first, the grounding check blocks the second. Then stop Ollama/break the API key and show the fallback path in the log.

## CV bullets this project must live up to
- Workflow automation for healthcare documentation: turns dictated care-note transcripts into structured outputs (vitals, wound notes, measures) checked by schema validation logic, with retries and fallback between a commercial LLM API and a self-hosted open-source LLM.
- Evaluation loop with a labelled test set scoring field-level precision/recall per model and logging latency per request, run in CI; a small React review screen lets a user accept or correct each draft entry.

If something is cut while building, update these bullets in `_work/cv.tex`. When done, mark it `built` in `profile/master-profile.md`; then real numbers (e.g. per-model precision/recall, latency) may go on the CV and the project may be used in the cover letter / interview.
