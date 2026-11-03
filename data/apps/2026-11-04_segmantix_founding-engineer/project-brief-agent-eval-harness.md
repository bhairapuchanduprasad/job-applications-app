# Brief: Agent Harness with Evals and Guardrails (reuses planned "Agent Eval Harness")
See applications/2026-11-04_neura-robotics_agentic-ai-engineer/_work/project-brief-agent-harness.md for scope (LangGraph loop over a mocked task API, FastAPI, risk-tagged tools with human approval, 20–30 golden tasks, Langfuse traces, GitHub Actions gate on success/latency/cost).
CV bullet: Python agent harness as a FastAPI service with typed tools, guardrails, retries and human escalation, plus golden-task eval in GitHub Actions with Langfuse tracing gating releases.
