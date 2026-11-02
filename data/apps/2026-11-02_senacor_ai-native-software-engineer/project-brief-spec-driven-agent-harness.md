# Project brief: Spec-Driven Coding Agent Harness (Senacor variant)

Base brief: applications/2026-10-17_bcg-platinion_ai-associate/_work/project-brief-spec-driven-agent-harness.md (scope, milestones, README). Build that; this file lists what this JD adds.

## Why it matters for this JD
Proves "KI-gestützter SDLC mit Coding Agents, automatisierter Codegenerierung und automatisierten Tests", "Engineering-Standards, CI/CD, Teststrategien, Observability", "KI-generierter Code nachvollziehbar, sicher, testbar".

## Variant additions (within 1–2 days)
- Target service: a small Python (FastAPI) microservice for a process step (e.g. "Antrag prüfen") with a typed API and Postgres data model, plus OAuth2 client-credentials auth stub, so auth and data models are visible.
- Every agent-made PR gets an automated review summary (diff, tests touched, spec coverage) to show traceability.
- CI: pytest, ruff, SAST (bandit or semgrep), dependency scan, agent eval suite; Langfuse traces linked from the PR.

## CV bullets it must live up to
- Plain-language feature request becomes a testable spec with pytest acceptance tests; Claude Code implements it under a rule set (CLAUDE.md, skills, hooks that block protected files and secrets) with an MCP server for spec context.
- GitHub Actions CI/CD runs automated tests, security checks (SAST, dependency scanning) plus an agent eval suite (pass rate, cost, turns); Langfuse traces for observability of the coding agent.

When built: mark `built` in profile/master-profile.md with real numbers; only then use it in cover letters.
