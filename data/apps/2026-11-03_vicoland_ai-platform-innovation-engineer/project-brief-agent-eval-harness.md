# Brief: Agent Eval & Tracing Harness (Vicoland variant)
Base brief and full scope: applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md (build that).
Vicoland variant: use a mocked business-platform API (projects, invoices, freelancer matching) as the agent's tools; trace with Langfuse; gate prompt/model changes in GitHub Actions.
CV bullets to live up to: (1) eval set with regression, edge and adversarial cases, deterministic checks first, LLM-as-judge second, pass rates over repeated runs; (2) every run traced in Langfuse; CI gate on changes.
