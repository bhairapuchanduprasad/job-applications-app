# Project brief: Spec-Driven Coding Agent Harness, Event Inc variant (edge cases, feature flags, rollbacks)

Repo slug: `spec-driven-agent-harness` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-17_bcg-platinion_ai-associate/_work/project-brief-spec-driven-agent-harness.md). Created for Event Inc AI Engineer (2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
Plain-language feature request → spec with explicit edge cases → pytest acceptance tests → Claude Code implements under a rule set (CLAUDE.md, skills, hooks that block secrets and protected files), MCP server for spec/task context. Event Inc additions: demo app is a small venue-availability API integrating an external SaaS mock; deploy pipeline in GitHub Actions ships behind a feature flag with automatic rollback when a smoke test fails; structured logs + a simple error-rate alert; agent eval suite (pass rate, cost, turns).

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "spec-first: Anforderungen und Edge Cases definieren, mit KI umsetzen, kritisch prüfen" | spec → tests → agent implementation → review gate |
| "Secrets- und Zugriffsmanagement" | hooks blocking secrets, GitHub Actions secrets, least-privilege token |
| "sichere Releases (Feature Flags, Rollbacks)", "Monitoring" | flag + auto-rollback + error-rate alert |
| "Prompts, Workflows und Learnings ... teilen" | skills + README as a team playbook |

## Milestones
1. Harness + skills + hooks (4 h) 2. Venue API + SaaS mock + tests (3 h) 3. Flagged deploy + rollback + logging (3 h) 4. Eval suite + README (2 h).

## CV bullets it must live up to
- Spec-first harness: a feature request becomes a spec with edge cases and pytest acceptance tests; Claude Code implements it under skills, an MCP server for spec context and hooks that block secrets.
- GitHub Actions ships each change behind a feature flag with monitoring of error rates, automatic rollbacks, structured logging and an agent eval suite.
