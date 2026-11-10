# Brief: Agent Eval & Tracing Harness (Owkin variant, DuckDB)
Same scope as applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md. Owkin addition: the mocked API data lives in DuckDB (Parquet), the agent calls typed SQL tools over it. Golden dataset, LLM-as-a-judge, Langfuse tracing, GitHub Actions regression gate. 1-2 days.
CV bullet it must live up to: tool-calling LangGraph agent, analytical data in DuckDB, golden dataset, LLM-as-a-judge, CI regression check.
