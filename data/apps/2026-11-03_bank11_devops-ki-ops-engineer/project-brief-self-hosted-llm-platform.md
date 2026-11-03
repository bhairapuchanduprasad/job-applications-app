# Project brief: Self-Hosted LLM Inference Platform (variant of AI Gateway Platform)

Base brief: applications/2026-10-27_vector_devops-engineer-ai-developer-platforms/_work/project-brief-ai-gateway-platform.md. Same LiteLLM proxy idea; this variant adds vLLM serving and the developer-tooling side.

## Goal
Prove the mamgo/YER AI Support Engineer must-haves: on-prem LLM inference on Kubernetes (vLLM, LiteLLM, open-source LLMs), testing new versions before rollout, troubleshooting, Python scripting, IDE integration.

## Scope (1–2 days)
- Local Kubernetes cluster (kind or OpenShift Local/CRC if the laptop can run it; otherwise kind and note OpenShift differences in the README).
- vLLM serving a small open-source model (e.g. Qwen2.5-0.5B/1.5B-Instruct; CPU or Apple-silicon-friendly fallback via vLLM CPU image, or llama.cpp server as a documented fallback).
- LiteLLM proxy in front: OpenAI-compatible endpoint, virtual keys per team, model aliases, budget limits, request logging.
- IDE integration: VS Code (Continue extension) and Cursor (custom OpenAI base URL) pointed at the LiteLLM endpoint (screenshots in README).
- `scripts/smoke_test.py`: Python script that runs before a version bump (vLLM or LiteLLM image tag): health, chat completion, streaming, latency p50/p95, token count sanity; non-zero exit on failure. GitHub Actions runs it against kind.
- `RUNBOOK.md`: troubleshooting guide (pod CrashLoop, OOM, GPU/CPU limits, 429 budgets, slow first token), with the kubectl/log commands used.
- Prometheus metrics from vLLM + LiteLLM, one Grafana dashboard (optional if time is short).

## Milestones
1. kind + vLLM deployment (3h) 2. LiteLLM proxy + keys (2h) 3. VS Code integration (1h) 4. Smoke tests + CI (3h) 5. Runbook + README (2h) 6. Metrics (optional, 2h).

## README outline
Architecture diagram, how to run, upgrade procedure (bump tag → smoke test → rollout → rollback), runbook link, what changes on OpenShift (Routes, SCCs).

## CV bullet it must live up to (German)
"On-Premises-Setup auf einem lokalen Kubernetes-Cluster: Open-Source-LLMs als Inferenzdienste mit vLLM bereitgestellt, LiteLLM-Proxy als einheitliche OpenAI-kompatible Schnittstelle mit Schlüsseln pro Team, angebunden an VS Code und Cursor; Python-Skripte für Smoke-Tests neuer Versionen vor dem Rollout und ein Troubleshooting-Runbook mit Logs und Metriken."

## Addendum for Bank11 (2026-11-03)
Same project, retitled "Self-Hosted LLM Platform". Must also show: LiteLLM fallback routing from the local vLLM model to a cloud model when the local one is unhealthy (failover test), Prometheus metrics + alert rule, logs, per-team keys (access control). Exact CV bullet: "KI-Infrastruktur mit lokal gehosteten Open-Source-LLMs auf Kubernetes: Modell-Serving mit vLLM hinter LiteLLM-Proxy mit Zugriffskontrolle, Failover auf ein Cloud-Modell, Monitoring, Logging und Alerting mit Prometheus, Smoke-Tests vor dem Rollout."
