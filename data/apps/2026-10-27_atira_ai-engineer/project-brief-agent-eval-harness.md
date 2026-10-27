# Project brief (Atira variant): Agent Eval Harness

Status: planned. Main brief (scope, stack, milestones, README outline): `applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md`. Build that; this note only lists what Atira cares about.

## Why it matters for Atira AI Engineer
Proves: evals, harnesses, self-verification, observability, "no silent failures, cost blowouts, or latency explosions", tool loops/guardrails.

## Atira-specific emphasis (fits in the 1–2 day scope)
- Make the mocked API look like Atira's world: an RFQ-to-quote tool-calling agent (tools: get_product_spec, check_configurator_rule, get_price_list) over a mocked ERP.
- Report cost per run and p95 latency next to pass rates (cache on/off).
- Keep the tool-loop limit and malformed-tool-response tests prominent; they map to "deterministic guardrails".

## CV bullets it must live up to (exact, as on the Atira CV)
- Evaluation harness for a tool-calling LangGraph agent over a mocked API: golden datasets (regression, edge cases, synthetic multi-turn, adversarial), deterministic checks first (JSON schema, function-calling payloads, regex, API status, embedding similarity), then LLM-as-a-judge only for what they cannot decide.
- Runs each case several times and reports pass rates with confidence intervals; tests prompt injection, malformed inputs, unexpected tool responses and tool-loop limits; LLM response caching and tool mocking in GitHub Actions, tracing and observability with OpenTelemetry and Arize Phoenix.
