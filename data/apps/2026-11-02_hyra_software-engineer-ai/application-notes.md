# Application notes: Hyra (financial services client, not named), Software Engineer (AI), Berlin hybrid

Ask Hyra first: client name, salary band, team (platform vs product), hybrid days.

## Likely interview questions
1. How did you design the indexing and evaluation for your retrieval pipeline?
   → Kniit: ingestion → chunking → agentic/deterministic/monolithic indexing; ground truth from SAP system; P/R 33/45 → 93/90.
2. How do you keep LLM workflows cost-efficient?
   → Deterministic pipeline for high-volume stream, $200k projected LLM budget → near zero; LiteLLM model layer.
3. How do you expose structured knowledge to agents?
   → Neo4j knowledge graph via MCP query service, millisecond latency, used from Claude Code.

## Form answers
- Why this role: the task list matches the Kniit work (retrieval, indexing, evaluation, agentic orchestration) and moves it into a regulated, high-scale domain.
- Salary: €60,000–75,000 gross/year; single number €70,000.
- Start: 15 Nov 2026. Work authorisation: EU Blue Card.
