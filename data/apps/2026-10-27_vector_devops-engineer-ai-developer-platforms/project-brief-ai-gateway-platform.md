# Project brief: AI Gateway Platform (LLM Gateway, VECTOR variant)

Status: planned. Repo slug: `ai-gateway-platform`. Variant of the LLM Gateway project (main brief: applications/2026-10-14_accenture_junior-applied-ai-engineer/_work/project-brief-llm-gateway.md). This variant uses an off-the-shelf LiteLLM proxy instead of a hand-written FastAPI layer and focuses on the platform/DevOps side.

## Goal
Run a self-hosted AI gateway as a shared platform service for development teams, deployed and operated the GitOps way, with secrets, observability and CI.

## Why it matters for VECTOR (DevOps Engineer AI & Developer Platforms)
Their stack: Kubernetes, Flux (GitOps & CD), GitHub & GitHub Actions, Claude Code, AI gateways (LiteLLM), HashiCorp Vault, JFrog Artifactory, Grafana, Loki, Mimir. Proves: LiteLLM AI gateway, Kubernetes, GitOps with Flux, Vault, Grafana/Loki, GitHub Actions, platform service for dev teams. The user has LiteLLM, Kubernetes, Docker, CI/CD from real work; Flux, Vault, Grafana/Loki would be new.

## Scope (1–2 days)
- Local Kubernetes cluster (kind or k3d).
- LiteLLM proxy via Helm chart; two providers (e.g. OpenAI + Anthropic, or one + a local Ollama model) with fallback and retries; virtual keys per team; token budgets per key.
- Flux bootstrapped from a GitHub repo; the gateway, Postgres (LiteLLM spend DB) and monitoring are reconciled from Git.
- HashiCorp Vault (dev mode in cluster) + Vault Agent injector or External Secrets for provider API keys.
- Prometheus metrics from LiteLLM, Loki for logs, Grafana dashboard: requests, latency p50/p95, tokens, cost per team, error rate.
- Team onboarding: a YAML file per team (models allowed, budget) → PR → Flux applies.
- GitHub Actions: lint (helm lint, kubeconform), a smoke test against the gateway in a kind cluster, Trivy image scan.
- Skip: Artifactory, Mimir (mention Loki/Prometheus only), multi-cluster.

## Architecture sketch
GitHub repo (clusters/, apps/, teams/) → Flux → kind cluster: [LiteLLM proxy] ↔ [Postgres]; [Vault] → secrets; [Prometheus + Loki + Grafana]. Client: curl / OpenAI SDK with a team virtual key.

## Milestones
1. kind + Flux bootstrap, LiteLLM Helm release, one provider working.
2. Vault for API keys; second provider + fallback; virtual keys + budgets.
3. Prometheus/Loki/Grafana dashboard; team YAML onboarding.
4. GitHub Actions (lint, kind smoke test, Trivy); README + demo.

## README outline
What & why · Architecture diagram · Quickstart (make up) · Onboard a team · Dashboards · Failure drill (kill provider → fallback) · Security notes (Vault, no keys in Git) · What I'd do in production (Artifactory mirror, Mimir, SSO).

## Demo idea
Short screen recording: open a PR adding a team YAML → Flux applies → team key works → kill provider A → requests fall back to B → Grafana shows the spike and cost per team.

## CV bullets it must live up to (exact, as on the VECTOR CV)
- Self-hosted AI gateway (LiteLLM proxy) as a shared platform service for development teams: virtual keys per team, token budgets, retries and fallback between LLM providers, and logging of latency, token usage and cost for every request; teams onboard through a configuration file.
- Runs on a Kubernetes cluster deployed with Flux (GitOps) from a GitHub repository via a Helm chart, with secrets from HashiCorp Vault and Grafana dashboards over Loki logs and Prometheus metrics; a GitHub Actions pipeline runs tests and an image scan on every change.
