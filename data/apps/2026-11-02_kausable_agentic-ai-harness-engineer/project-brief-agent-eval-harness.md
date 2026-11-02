# Project brief: Agent Eval Harness (kausable variant)

**Status:** planned. Build before submitting the kausable "Agentic-AI Harness Engineer" application (or drop the Projects section).
**Repo slug:** `agent-eval-harness` (no link on the CV until it exists). Base brief: applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md

## Goal
Show the kausable job in miniature: take a raw ML model, wrap it in an agentic harness that handles multi-step, long-horizon questions, and prove with release criteria when the agent is ready to ship.

## Why it matters for this JD
Covers what the work history covers weakly: hands-on PyTorch, in-context learning, harness/inference design, hierarchical querying, Weights & Biases, CI for models, developer-facing SDK, release criteria.

## Scope (1–2 days with Claude Code)
**In:** a small PyTorch time-series forecaster (e.g. a tiny Transformer or LSTM trained on a public dataset such as electricity load) exposed as a tool; a LangGraph planner that splits long-horizon questions ("what happens to load next week if temperature drops 5°C?") into sub-queries; context curation that picks in-context examples (similar past windows) per call; a typed Python SDK (`Harness.ask()`, `Harness.forecast()`); ~30 golden tasks; eval runner; W&B logging; GitHub Actions gate; FastAPI + Docker.
**Out:** a real foundation model, PFN training, UI, multi-cloud.

## Tech stack
Python 3.12, PyTorch, LangGraph, LiteLLM, Pydantic, pytest, Weights & Biases (eval tables + runs), FastAPI, Docker, GitHub Actions.

## Architecture sketch
```
model/       train.py (PyTorch), model.pt, predict()
harness/     planner (LangGraph): decompose → choose context → call model tool → aggregate → answer
             context.py: retrieve k similar windows as in-context examples, token budget
sdk/         typed client (Pydantic), retries, timeouts
evals/       golden tasks, deterministic checks (numeric tolerance, schema), LLM judge for explanations,
             N repeated runs → pass rate + Wilson CI, failure-mode tags (wrong decomposition, bad context, tool error)
release.yml  thresholds per metric = release criteria; CI fails below them; results logged to W&B
api/         FastAPI + Dockerfile
```

## Milestones
1. Train + save the PyTorch model (2 h) 2. Harness + context curation (4 h) 3. SDK (1 h) 4. Golden tasks + eval + W&B (3 h) 5. Release gate in GitHub Actions (1 h) 6. FastAPI/Docker + README (2 h)

## README outline
Problem, architecture diagram, how context is curated, release criteria and why these thresholds, W&B screenshot, failure modes found, limits.

## Demo idea
A PR that changes the context-selection rule → CI shows the pass rate dropping below the release threshold, with the W&B run and the failing failure-mode tag.

## CV bullet it must live up to (exact)
- Agentic harness around a small PyTorch time-series model exposed as a tool: an LLM planner splits long-horizon questions into hierarchical sub-queries and curates in-context examples per call; release criteria as code (golden tasks, pass rates over repeated runs, failure-mode tags) logged to Weights & Biases and gated in GitHub Actions.
