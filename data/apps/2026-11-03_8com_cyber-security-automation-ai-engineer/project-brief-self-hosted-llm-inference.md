# Project brief: Self-Hosted LLM Inference Platform (variant for 8com)
Base brief: applications/2026-11-03_mamgo_ai-support-engineer/_work/project-brief-self-hosted-llm-inference.md (same project, AI Gateway Platform family). Do not build twice.

## Goal
Prove the 8com must-haves: local LLM serving (vLLM, llama.cpp, Open WebUI), local open models (Qwen, Gemma), benchmarking, Python scripting.

## Scope (1-2 days)
- vLLM (or its CPU image) and llama.cpp server each serving a small open model (Qwen2.5-1.5B-Instruct, Gemma small), via Docker.
- LiteLLM proxy in front (OpenAI-compatible endpoint, model aliases); Open WebUI pointed at it.
- `scripts/benchmark.py`: latency p50/p95, tokens/s, same prompt set against both backends; `scripts/smoke_test.py` before a model/image version bump.
- README with results table (only real measured numbers), architecture sketch, notes on Apple silicon vs Nvidia.

## CV bullet it must live up to
"Lokal betriebene Open-Source-LLMs (Qwen, Gemma) mit vLLM und llama.cpp hinter einem LiteLLM-Proxy, Open WebUI als Oberfläche; Python-Skripte für Benchmarking und Smoke-Tests neuer Modellversionen."

## Optional extension (not on CV)
SOC alert-triage agent over an MCP server with mock threat-intel/asset tools and human approval (would prove the SOAR/MCP side).
