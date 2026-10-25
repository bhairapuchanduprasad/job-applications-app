# Application notes: Kraken, Software Engineer (Autonomous Agents)

## Before submitting
- Build `energy-service-agent` (brief in this folder), or remove the Projects section. It also gives you TypeScript to talk about.
- Form question "Do you require sponsorship?" → **No.** "Right to work in Germany?" → **Yes, EU Blue Card.** (When you switch employers, you notify the Ausländerbehörde; the new job must meet the Blue Card salary threshold.)
- 15 applicants in 4 hours: apply today.

## Likely interview questions
1. **"Design an agent that lets a customer submit a meter reading. What can go wrong?"**
   Authenticate first; only the tools that customer may use; validate the reading (plausibility vs history, like implausible-read checks); confirm before writing; hand over with full context on doubt or complaint; log every tool call; ship behind a toggle for one client first; evals for the journey.
2. **"How do you test something non-deterministic?"**
   Labelled set + metrics (Kniit P/R 33%/45% → 93%/90% vs SAP ground truth; RAGAS at Covestro), regression evals in CI, check tool choice and handoff decisions, not just text; monitor in production (handoff rate, tool errors).
3. **"Tell us about turning a messy business process into software."**
   Kniit: regulatory/technical documents and SAP experts → extraction rules, ground truth, Expert Interface for approval. Covestro consulting internship: stakeholders' decision-making workflows → agentic app on AWS.

Prepare: MCP basics (tools, resources, transports, auth), TypeScript basics, feature-flag rollout patterns, Django at concept level, why you left Kniit (public line in profile).

## Form answers
- **Why Kraken:** agents that act for energy customers (bills, meter readings) with safe handoff, built once for 70M+ accounts across many utilities; my last year was AI agents and an MCP server for the German energy sector.
- **Salary expectation:** €70,000 (profile default).
- **Earliest start / notice:** 16 November 2026 (current role ends 13 November 2026).
- **Location:** Berlin, hybrid.
- **Work permit:** EU Blue Card, no sponsorship needed.
- **Languages:** English business fluent; German B1.
