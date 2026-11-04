# Application notes: Unzer
## Likely questions
1. How do you evaluate an agent's output? -> Kniit: ground truth from SAP, precision/recall 33/45 -> 93/90, reflection agent.
2. How do you use coding agents day to day, and where do they fail? -> Claude Code with custom skills, hooks, tests as the guard.
3. You have no Java: how would you get productive in a Java backend? -> same service patterns as FastAPI microservices; learn the codebase conventions, tests first.
## Form fields
- Why Unzer: AI across the lifecycle from spec to operations, in a payments setting where reliability matters.
- Salary: EUR 55,000 gross/year (EUR 60,000 only if asked for a single number at a big established company; Unzer is mid-large, 55k).
- Start: 15 Nov 2026. Location: Berlin, hybrid 2 office days, Blue Card.
## Build before sending
- Spec-Driven Coding Agent Harness (see profile/projects.md; brief: applications/2026-10-17_bcg-platinion_ai-associate/_work/project-brief-spec-driven-agent-harness.md). Base scope: spec -> pytest -> Claude Code under rules/hooks -> MCP spec server -> automated PR review summary -> GitHub Actions with SAST and eval suite.
