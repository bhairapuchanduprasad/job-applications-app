# Fit report: Just Eat Takeaway.com, Data Scientist – AI Engineering (Mid-level), Amsterdam/Berlin hybrid
**Fit score: 62/100.** Strong on LangGraph/MCP/multi-agent, RAG evaluation and Python; weak on live user-facing agents in production and agent observability.

| Requirement | Evidence | |
|---|---|---|
| Multi-step / multi-agent designs, LangGraph, MCP, tool use | Kniit LangGraph multi-agent + MCP service; Covestro LangGraph agent | ✅ |
| Evaluation datasets, metrics, regression tests | Kniit precision/recall vs SAP ground truth; Covestro thesis RAGAS/PytrecEval | 🟡 (RAG/extraction, not tool-using conversational agents; no LLM-as-judge in work history) |
| Python + SQL, engineering habits (Git, CI/CD, review) | Python daily; GitLab CI/CD; SQL/Postgres listed | ✅ |
| Data science foundation, experiment design | Covestro/Cognizant ML + time series; statistics not on CV in depth | 🟡 |
| Docker/Kubernetes (nice to have) | Docker, Kubernetes at Kniit | ✅ |
| Production user-facing agents with real users | Covestro agent deployed (internship), Kniit expert interface (internal) | 🟡 |
| Observability: tracing, dashboards, alerts (OpenTelemetry, Datadog) | none in work history | ❌ |
| Online evaluation, A/B / staged rollouts, feature flags | none | ❌ |
| Multilingual, multi-market agents | embedding benchmarking multilingual only | 🟡 |

## Gaps and framing
- Observability and live-traffic agents: covered by planned project Agent Eval Harness (OpenTelemetry traces, LLM-as-a-judge, CI); the cover letter states honestly that production-scale live agents and dashboards are new.
- Datadog, feature flags, online evaluation: left out, stay gaps. Google ADK not on profile.
- German: not mentioned in the posting (Amsterdam/Berlin, English).

## Red flags
- Role is hybrid 3 days/week in Amsterdam or Berlin: not remote. Berlin used (Germany, Blue Card). Netherlands is the other option and would need relocation/visa check.
- "Mid-level" with hands-on production agent experience requirement; likely stretch on that point.
- Listed in search as Remote EU but is not remote.

## Hooks (from the posting only; no web research in this unattended run)
- Agents that support delivery-network operations staff in real time across multiple markets and languages.
- Mission: make agents "measurably better and safe to change": evaluation harness + observability.
- Contribution to an internal community of people building user-facing agents at JET.
