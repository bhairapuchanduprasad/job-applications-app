# Fit report: INSTATIQ, Applied AI Engineer (m/w/d), Stuttgart

**Fit score: 62/100.** Strong on GenAI (RAG, assistants, agents), Python, training/evaluating ML models and taking prototypes to deployed services. Main gaps: "verhandlungssichere" German (you have B1), no hands-on predictive maintenance / OT integration, no experience steering external development partners.

Language: German posting that requires negotiation-level German → German CV + Anschreiben (CLAUDE.md rule 3, same as the CGI / Markant / Dr. Theiss applications). Salary expectation and earliest start are explicitly asked for, so both are in the Anschreiben.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Degree in Applied CS / AI / ML | MSc Artificial Intelligence, TH Würzburg-Schweinfurt | ✅ |
| Mehrjährige Berufserfahrung AI/ML | 3 years: Kniit, Covestro (3 roles), Cognizant | ✅ |
| Sehr gute Python-Kenntnisse | Python across every role; FastAPI, Python microservices | ✅ |
| ML methods + modern GenAI | RF/XGBoost/LSTM (Covestro), ARIMA/Prophet/LSTM (Cognizant); LangGraph multi-agent, RAG, GraphRAG, QLoRA | ✅ |
| GenAI apps: chatbots, assistants, RAG | Covestro agentic app (vector search, inference, summarisation), RAG evaluation thesis, Kniit MCP knowledge service | ✅ |
| Training, evaluation, deployment of ML models | Covestro prediction models benchmarked vs curve fitting + Streamlit dashboard; RAGAS/PytrecEval eval; Kniit P/R 33/45 → 93/90 | ✅ |
| Developing + integrating AI-based services | FastAPI backends, MCP service, Docker, AWS CDK, Azure, Kubernetes | ✅ |
| PoC/MVP fast, evaluate use cases | Kniit sole developer from scratch; Covestro AI consulting (use-case advisory) | ✅ |
| Predictive maintenance / anomaly detection / process optimisation | Adjacent: ML on sensor time-series process data (Covestro: early detection of off-spec batches), load forecasting. No predictive maintenance on machines | 🟡 |
| Integration into IT and OT systems | IT side yes (APIs, cloud). No OT (PLC, OPC UA, machine software) | ❌ |
| Steer external AI developers/partners | None directly; adjacent: worked with CTO, SAP experts, chemists, business stakeholders | 🟡 |
| Verhandlungssichere Deutsch- und Englischkenntnisse | English business fluent; **German B1** | ❌ (top gap) |
| Construction / machinery domain | None (mechanical engineering BTech is a small bridge) | 🟡 |

## Gaps and honest framing
1. **German (top gap):** state B1 plainly in the letter and CV; say you are improving it. Expect this to be the deciding factor; the team works with machine software developers and departments in German.
2. **Predictive maintenance / anomaly detection:** frame Covestro sensor time-series work (lag features, rolling windows, early detection of deviating batches) as the closest evidence. Planned project (below) closes it on paper; build it before submitting.
3. **OT integration:** do not claim. Mechanical engineering degree + OPC UA-style tag model in the project are the honest bridge.
4. **Managing external partners:** do not claim; mention stakeholder work.

## Project on the CV
Reused planned project **Plant Maintenance Agent** (already on the Siemens Advanta CV), with an INSTATIQ variant brief: trained + evaluated anomaly model on simulated pump/printer sensor data, RAG assistant over machine manuals, FastAPI services, Docker. Status: planned → application is **build-first**.

## Red flags
- "erfahrenen" + "mehrjährige" + leading external partners suggests they may want someone a bit more senior than 3 years, but no year count is given.
- Startup spin-off (backed by Putzmeister), so role scope will be broad; one-person AI function is likely.

## Company hooks (research 2026-10-26)
1. INSTATIQ is the Putzmeister spin-off for 3D concrete printing; its mobile printer **INSTATIQ P1** builds on a truck-mounted concrete pump, was launched at **bauma 2025**, prints load-bearing walls on site layer by layer with up to 26 m reach and 10 cm/s print speed. ([Putzmeister, bauma 2025](https://www.putzmeister.com/web/european-union/news-article-detail/-/asset_publisher/instatiq-the-putzmeister-3d-printer-for-solid-construction-at-bauma-2025))
2. Origin: 2016 research cooperation, prototype 2022, first building printed with **Züblin** in 2023; trial on a housing development in Metzingen. ([3DNatives interview, Jul 2025](https://www.3dnatives.com/de/instatiq-interview-3d-betondruck-fuer-transformative-bauindustrie-090720251/), [Concrete Connect](https://www.concreteconnect.co.uk/news/zublin-tests-large-scale-3d-concrete-printing))
3. "First mobile 3D-printed basement" in **Weisenhorn**. ([3Printr](https://www.3printr.com/world-premiere-in-weisenhorn-first-mobile-3d-printed-basement-in-the-world-5186334/))
4. July 2026: published German patent application DE102025100368A1 for a delta-robot fine-positioning unit at the print head of the pump boom. ([Fabbaloo](https://www.fabbaloo.com/?p=238726))
5. Stated mission: bring 3D concrete printing into the mass market. AI angle for the letter: a machine that runs on a construction site produces sensor data (pump pressure, boom position, material flow) that suits predictive maintenance and anomaly detection, and operators need assistance systems over manuals and print plans.
