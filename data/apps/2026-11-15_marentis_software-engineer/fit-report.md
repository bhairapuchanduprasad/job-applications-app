# Fit report: Marentis, Software Engineer (gn), Berlin
**Fit score: 68/100.** Python/backend, SQL, knowledge graph, agent and time-series sensor work match well; no direct MQTT/OPC UA or manufacturing-integration experience, and the role wants an experienced independent code reviewer.

German requirement: No mention of German. Posting language: English.

| Requirement | Evidence | |
|---|---|---|
| Strong Python/backend, shipped software | Kniit sole developer (FastAPI, microservices, Azure), Covestro FastAPI app on AWS | ✅ |
| SQL, database design, data validation | Postgres, Neo4j, MongoDB; graph curation/validation app | ✅ |
| Knowledge graphs and retrieval | Kniit Neo4j GraphRAG, MCP query service, RAG thesis with RAGAS/PytrecEval | ✅ |
| Agent systems | LangGraph multi-agent with reflection; MCP | ✅ |
| Sensor/time-series data, ML | Covestro prepolymer process time-series, Cognizant EV load forecasting | ✅ |
| Testing, CI | GitLab CI/CD, Postman API testing; no deep test-design story | 🟡 |
| Independent code review of PRs | Not documented in profile | 🟡 |
| MQTT, OPC UA, robot cells, simulators | none (CV project is planned, not built) | ❌ |
| Concurrency, observability, customer-environment ops | Docker/Kubernetes only | 🟡 |
| Manufacturing domain | chemical process data (adjacent) | 🟡 |

## Gaps and framing
- MQTT/OPC UA: stated honestly in the letter; planned project "Machine Telemetry Ingestion Service" covers it once built.
- Code review/testing: not claimed beyond what the profile supports.

## Red flags
- "Experienced" wording; no year count given. Early-stage startup, funding runway unknown (Atlantic portfolio company).

## Hooks (company research skipped: unattended run, hooks come from the posting only)
- Faults that originate elsewhere in a production line; similar symptoms, different causes (JD).
- Combining sensor data, machine states, alarms and expert knowledge (JD), close to the Kniit graph work.
- Small team where individual contributions shape the product (JD).
