# Project brief: AI Output Quality Gates (repo slug: ai-output-quality-gates)
Status: planned. Reuses the "Agent Eval Harness" idea, framed as shared quality tooling.

**Goal:** a small Python library + CLI that teams plug into GitLab CI/CD to check LLM/agent outputs (golden set, JSON schema, regression vs previous run) and report clear diagnostics.
**Why for RepRisk JD:** proves quality-engineering frameworks/tools, CI/CD feedback, maintainability and diagnostics, pytest, Docker, GitLab CI/CD, AI-output validation.
**Scope (1-2 days):** (1) check interface + 3 built-in checks (schema, golden-answer similarity, regression diff); (2) plugin discovery so teams add checks; (3) pytest suite for the library itself (unit + one integration test); (4) Dockerfile and `.gitlab-ci.yml` running the gates on merge requests; (5) readable failure report (Markdown/JUnit XML).
**Stack:** Python, pytest, Pydantic/jsonschema, Docker, GitLab CI/CD (mirror on GitLab or equivalent).
**Architecture:** `checks/` plugins -> runner -> reporter (Markdown + JUnit) -> CI job fails on regression.
**Milestones:** library core; built-in checks; tests; CI + Docker; README with "add your own check" guide.
**README outline:** problem, quick start, writing a check, CI setup, design trade-offs (test layers).
**Demo idea:** sample mock LLM app with one deliberately regressing prompt that the pipeline catches.
**CV bullets it must live up to:** Python library and CLI running golden-set, schema and regression checks on LLM/agent outputs with a plugin interface for team-owned checks and clear diagnostics per failure; runs as a GitLab CI/CD job in a Docker image on every merge request and fails the pipeline on regressions, with docs and example checks.
