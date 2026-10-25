# Project brief: Spec-Driven Coding Agent Harness
Repo slug: `spec-driven-agent-harness` · Status: planned (no link on the CV until it exists and the user adds it)

## Goal
A small, working "agentic software factory" in miniature: a business request goes in, a testable spec comes out, Claude Code implements it inside guardrails, and CI decides whether the change is accepted. Every agent run is traced and scored.

## Why it matters for BCG Platinion (AI Associate)
Proves the JD items your work history covers only partly:
- "rule sets, toolchains, evaluation frameworks and CI/CD integrations that govern the behavior of coding agents across the entire SDLC"
- "translate business intent into precise, testable specifications that agents can execute"
- "DevSecOps and CI/CD pipelines to automated testing"
- "agent evaluation, observability tools (e.g. Langfuse, LangSmith)", "agent loops", "MCP"
- "evaluation and governance mechanisms that ensure AI systems are secure, transparent"
Directly mirrors their "Agentic Software Factory" ("Humans govern outcomes, agents do the work").

## Why it matters for opta data (AI-Engineer, Essen) — added 2026-10-24
Same project as for BCG Platinion; one build serves both applications. For opta data it proves:
- "maßgeschneiderte Coding Agents" and "GenAI-gestützte Systeme, mit denen unsere Softwareentwickler effizienter arbeiten können" → the whole harness
- "MCP-Servern", "LangChain/FastMCP" → **build the MCP server with FastMCP** (the CV for opta data names FastMCP)
- "Monitoring, Evaluation … im Produktivbetrieb", "LLM-Evaluierung/Observability (z. B. Langfuse)" → Langfuse traces + eval suite
- "CI/CD-Pipelines" → the CI gate
Optional stretch for opta data (only if time allows, and then add it to the CV): a step that generates user documentation (Markdown) for each implemented feature, matching "Erstellung von Benutzerdokumentation".

### Exact CV bullets on the opta data CV (must be true once built)
- Harness that turns a plain-language feature request into a testable specification (acceptance criteria written as pytest tests) and lets a coding agent (Claude Code) implement it under a rule set: project conventions, custom skills, and hooks that block edits to protected files and secrets; an MCP server built with FastMCP gives the agent the spec and task context.
- A CI/CD pipeline gates every agent-written change with automated tests, static security analysis, and dependency scanning, plus an evaluation suite over benchmark tasks (pass rate, cost, turns per task); traces of the agent runs go to Langfuse for monitoring and observability.

## Scope (1–2 days with Claude Code)
In: one small target repo (e.g. a FastAPI service for a toy domain such as invoice approval), 5–8 benchmark tasks, spec → tests → agent → CI loop, Langfuse traces, evaluation report.
Out: multi-repo orchestration, a UI, fine-tuning, production deployment.

## Tech stack
Python, Claude Code (headless mode `claude -p`), Claude Code hooks + skills + CLAUDE.md, a small MCP server built with FastMCP serving specs/tasks, pytest, GitHub Actions, Bandit or Semgrep (SAST), pip-audit (dependency scanning), Langfuse (cloud free tier or Docker).

## Architecture sketch
```
feature request (markdown)
  → spec step: LLM drafts acceptance criteria → human approves → pytest tests committed (failing)
  → MCP server: exposes get_spec(task_id), list_tasks(), report_result()
  → Claude Code (headless) implements under rules:
       CLAUDE.md conventions · skills (e.g. /implement-spec) ·
       PreToolUse hooks: block writes to tests/, .github/, secrets, .env
  → GitHub Actions: pytest · Bandit/Semgrep · pip-audit · eval job
  → eval job: runs benchmark tasks, records pass rate, cost, turns, duration → eval-report.md
  → Langfuse: one trace per agent run (spans per tool call / turn)
```

## Milestones
1. Target repo + 5–8 tasks with hand-written acceptance tests (half a day).
2. Rule set: CLAUDE.md, one skill, hooks that block protected paths; a test proving the hook blocks (2–3 h).
3. MCP server for specs/tasks; agent runner script (headless Claude Code) (2–3 h).
4. GitHub Actions pipeline: tests + SAST + dependency scan + eval job (2–3 h).
5. Langfuse tracing of agent runs; eval report with pass rate / cost / turns (2–3 h).
6. README + short demo GIF.

## README outline
Problem · Architecture diagram · Rule set (what the agent may and may not do, and why) · Spec format · CI gates · Evaluation results table · Observability (Langfuse screenshot) · Limitations · How to run.

## Demo idea
A 60-second clip: paste a feature request → spec + failing tests appear → agent implements → CI green → Langfuse trace and eval row. Plus one run where the hook blocks the agent from editing a test.

## CV bullets it must live up to (BCG Platinion CV; opta data bullets are above)
- Harness that turns a plain-language feature request into a testable specification (acceptance criteria written as pytest tests) and lets Claude Code implement it under a rule set: project conventions, custom skills, and hooks that block edits to protected files and secrets; an MCP server gives the agent the spec and task context.
- A GitHub Actions CI/CD pipeline gates every agent-written change with automated testing, static security analysis, and dependency scanning (DevSecOps), plus an agent evaluation suite over benchmark tasks (pass rate, cost, turns per task); agent loop traces go to Langfuse for observability.

Once built: add real numbers (pass rate, cost per task) to the master profile and mark the project `built`.
