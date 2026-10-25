# Project brief: Plant Maintenance Agent

Repo slug: `plant-maintenance-agent` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the Siemens Advanta application.
Time box: 2 days with Claude Code (Snowflake 30-day trial, dbt Core, Azure free credits).

## Goal
A multi-agent proof of concept for industrial maintenance. Simulated machine sensor data (temperature, vibration, pressure per asset, tagged like an OPC UA address space) lands in Snowflake and is modelled with dbt. One agent detects anomalies in the time series, a second agent searches equipment manuals (PDF) for the relevant fault and procedure (document intelligence), and an orchestrator proposes a maintenance action with sources for the plant operator to confirm.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "agentic AI frameworks (Google ADK, OpenAI Agents SDK, Claude Agents SDK)" | Agents built with the Claude Agent SDK (note in README how ADK would map) |
| "Azure, incl. Microsoft Foundry" | Model deployment + agent hosting via Microsoft Foundry (Azure AI Foundry) |
| "Data Warehousing & Engineering (Snowflake & dbt)" | Raw → staging → marts in dbt on Snowflake; tests in dbt |
| "AI applied to industrial data (time series, process optimization, document intelligence)" | Anomaly agent on sensor time series; manual search agent |
| "exposure to IT/OT architecture or industrial standards" | OPC UA-style tag model (asset → component → tag), ISA-95 levels sketched in README |
| "from plant operators to top management" | Operator view (proposed action + sources) and a one-page management summary in README |
| "proof of concepts, production-grade code" | Typed Python, tests, CI, eval set |

## Scope
In:
- Data generator: 5 assets, 3 sensors each, 30 days at 1-min resolution with injected faults (bearing wear → vibration drift, overheating, pressure drop).
- Snowflake trial: raw tables; dbt models `stg_sensor_readings`, `fct_asset_health` (rolling stats, z-scores), dbt tests.
- Manuals: 3–4 short equipment manuals (write your own or use public ones privately), chunked + embedded.
- Agents (Claude Agent SDK): `anomaly_agent` (SQL tool on Snowflake marts), `manual_agent` (retrieval tool), `orchestrator` (combines, proposes action, asks for confirmation).
- Microsoft Foundry: deploy the model endpoint / run the agent there; document the setup.
- Eval: 15 injected-fault scenarios with expected action; CI reports how many are correct.
Out: real OPC UA server, PLC integration, UI beyond a simple Streamlit page.

## Architecture
```
sensor simulator ─► Snowflake (raw) ─► dbt (staging ─► fct_asset_health)
                                                     │ SQL tool
manuals (PDF) ─► chunks + embeddings ─► retrieval tool│
                                                     ▼
              orchestrator (Claude Agent SDK) ◄─ anomaly_agent, manual_agent
                         │
                proposed maintenance action + sources ─► operator confirms (Streamlit)
CI: dbt test + pytest + eval on 15 fault scenarios
```

## Milestones
1. Simulator + Snowflake raw load. (≈2 h)
2. dbt models + tests. (≈2 h)
3. Manual ingestion + retrieval tool. (≈2 h)
4. Agents with the Claude Agent SDK. (≈3 h)
5. Microsoft Foundry deployment. (≈2 h)
6. Eval + CI + README (architecture, IT/OT notes, management summary). (≈2 h)

## CV bullets this project must live up to
- Multi-agent proof of concept for industrial maintenance: one agent analyses machine sensor time series (OPC UA-style tag model) for anomalies, another searches equipment manuals with document intelligence, and an orchestrator proposes a maintenance action for the plant operator to confirm.
- Sensor and maintenance data modelled with dbt in Snowflake; agents built with the Claude Agent SDK and deployed via Microsoft Foundry on Azure, with an evaluation set run in CI/CD.

When done, mark it `built` in `profile/master-profile.md`; then real results may go on the CV.
