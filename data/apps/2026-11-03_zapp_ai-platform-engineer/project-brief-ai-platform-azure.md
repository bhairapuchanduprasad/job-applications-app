# Project brief: Internal AI Platform on Azure (AI Gateway Platform variant)
Repo slug: ai-platform-azure. Status: planned. For: Zapp AI Platform Engineer (2026-11-03).

## Goal
A small internal AI platform for a manufacturer: one gateway for all LLM use cases, one MCP server to company systems, and standard quality gates every use case must pass before deployment.

## Why for this JD
Proves AI platform architecture, Azure, MCP + REST system integration, versioning, automated tests, deployment, monitoring, evaluation, quality gates, identity/permissions (Entra ID), AI governance.

## Scope (1–2 days)
- LiteLLM proxy on Azure Container Apps: Azure OpenAI + one open-source fallback, per-team virtual keys, budgets.
- Entra ID sign-in (app registration) mapping groups to allowed models/tools.
- Python MCP server (FastMCP) over a mock ERP/MES REST API (production orders, material certificates); read-only tools, role-checked.
- Sample agent use case: "order status + certificate lookup" assistant.
- Quality gate: golden question set + LLM-as-judge in GitHub Actions; prompts and tool schemas versioned in Git; deploy only if gate passes.
- Monitoring: request logs, latency, cost, error rate to Application Insights (OpenTelemetry).
- Governance: USE_CASES.md register (owner, data classes, EU AI Act risk class, approval).

## Milestones
1. Gateway + Entra ID. 2. MCP server + mock API. 3. Use case agent. 4. Quality gate CI. 5. Monitoring + governance doc + README.

## Demo
Two users with different groups: one can call the ERP tool, the other is refused; CI run blocks a prompt change that fails the golden set.

## CV bullets it must live up to
- Internal AI platform on Azure: LiteLLM gateway with Entra ID group-based permissions and per-team budgets, a Python MCP server over a mock ERP/MES REST API, and a use-case register for AI governance.
- Quality gates in GitHub Actions (golden question set, versioned prompts and tool schemas) before deployment; latency, cost and error monitoring with OpenTelemetry in Application Insights.
