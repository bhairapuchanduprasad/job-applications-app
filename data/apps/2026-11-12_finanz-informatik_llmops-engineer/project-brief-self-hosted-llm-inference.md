# Project brief: Self-Hosted LLM Inference Platform (Finanz Informatik LLMOps variant)
Base brief: applications/2026-11-03_mamgo_ai-support-engineer/_work/project-brief-self-hosted-llm-inference.md (kind + vLLM + LiteLLM + smoke tests in GitHub Actions + runbook).
## Added for this JD
- Package vLLM and the LiteLLM proxy as a Helm chart (values per environment).
- Argo CD (on kind) syncs the chart from a Git repo; an image-tag bump in Git triggers the rollout.
- GitHub Actions runs smoke tests (health, completion, streaming, latency) before the tag bump is merged.
- Optional: Redis cache for repeated prompts (stretch only; not claimed on the CV).
## CV bullet it must live up to
"Serves an open-source LLM with vLLM on a local Kubernetes cluster as a Helm chart rolled out by Argo CD, behind a LiteLLM proxy; Python smoke tests in GitHub Actions gate every image-tag bump."
Milestones: kind + vLLM (3h), Helm chart (3h), Argo CD (2h), CI smoke tests (3h), README (1h). No GitHub link on the CV.
