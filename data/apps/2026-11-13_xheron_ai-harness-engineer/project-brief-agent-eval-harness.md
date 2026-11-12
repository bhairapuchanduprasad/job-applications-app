# Project brief: Agent Eval Harness (xHeron variant)
Status: planned. Base brief: applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md (build once, covers all variants). Build before submitting, or drop the Projects section.
Goal: show harness engineering in miniature: tool-calling LangGraph agent, typed tool contracts, retries/idempotency, human escalation, traces, golden-set evals, CI regression gate.
Stack: Python, LangGraph, LiteLLM, Pydantic, Langfuse, pytest, GitHub Actions.
Scope 1-2 days: mocked short-term-rental ops API (booking, cleaner schedule, guest message), agent with permissions + confirmation of effect, ~30 golden cases, LLM-as-judge, failure-mode tags, CI gate on pass rate over repeated runs.
CV bullet it must live up to: "Harness around a tool-calling LangGraph agent: state management, typed tool contracts with Pydantic structured outputs, permissions, retries and failure recovery, with escalation to a human. Evaluations and regression testing: golden-set evals with LLM-as-a-judge, structured traces and observability in Langfuse with failure-mode tags, and a CI check that fails when pass rates over repeated runs drop."
Demo: PR that weakens a tool contract -> CI fails, trace shows failure tag.
