# Application notes: Almedia, AI Full Stack Engineer, Berlin

Status: build-first. Build before submitting: Growth Ops Assistant (Almedia variant of Ops MCP Server; brief: `_work/project-brief-ops-mcp-server.md`). It is the only TypeScript/Node.js evidence on the CV. If you submit before building it, drop the Projects section and rebuild (`scripts/rebuild.sh`).
Apply via LinkedIn: https://www.linkedin.com/jobs/view/4365162691 (or Almedia's careers page). Salary band in the posting: €60K – €130K.
Also worth checking: Almedia advertises "AI Engineer (Data)" and "Junior Engineer (AI)" roles on job aggregators; confirm whether they are open.

## Likely interview questions
1. "Walk us through a complex agentic system you built." Kniit: four parallel LangGraph agents (extraction, relationship analysis, consolidation, reflection), ground truth from SAP data, P/R 33/45 → 93/90; when not to use an LLM (deterministic pipeline, $200k projected budget → near zero).
2. "How do you build AI workflows that survive model changes?" LiteLLM provider abstraction, evals against ground truth, deterministic code for anything that must be exact, MCP for tool access.
3. "How would you find where AI helps a marketing or UA team?" Covestro consulting approach: sit with the team, map the decision workflow, start with the most repetitive lookup, ship a small internal tool, measure. Be ready for a Node.js/TypeScript coding exercise: practise basics before.

## Form fields
- Why Almedia: profitable, bootstrapped company where internal AI tools pay off quickly; many teams and data sources (Freecash, zave.it acquisition 2025) to connect; role mixes full stack engineering with business-facing AI work, which is what I did at Kniit and Covestro.
- Salary: €70,000 (range €60–75k). Must meet Blue Card threshold.
- Notice / start: 15 November 2026.
- Location: Berlin (office-based role, central Berlin office).
- Work permit: EU Blue Card. German: B1 (not required by the posting).
