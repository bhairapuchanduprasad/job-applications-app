# Project brief: Self-Hosted LLM Platform (variant for CreaTech)
Base brief: applications/2026-11-03_8com_cyber-security-automation-ai-engineer/_work/project-brief-self-hosted-llm-inference.md (AI Gateway Platform family). Do not build twice.

## Goal
Prove "set up, run and maintain local LLMs" for CreaTech.

## Scope (1-2 days)
- vLLM (CPU image) and Ollama each serving a small open model (Qwen2.5-1.5B-Instruct, Gemma small) via Docker.
- LiteLLM proxy in front (OpenAI-compatible endpoint, aliases), Open WebUI pointed at it.
- `scripts/benchmark.py` (latency p50/p95, tokens/s) and `scripts/smoke_test.py` run before a model/version bump.
- README with measured results only.

## CV bullet it must live up to
"Open-source LLMs (Qwen, Gemma) run locally with vLLM and Ollama behind a LiteLLM proxy and Open WebUI; Python scripts for benchmarking and smoke tests before model updates."
