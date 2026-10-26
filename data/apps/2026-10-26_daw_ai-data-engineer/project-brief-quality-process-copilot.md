# Project brief: Quality Process Copilot, DAW variant

Repo slug: `quality-process-copilot` (no link on the CV). Status: **planned**.
Base brief: `applications/2026-10-23_hermes-group_ai-engineer/_work/project-brief-quality-process-copilot.md`; FERI variant (2026-10-26) adds a PII-redaction service. This file adds the data-engineering layer DAW asks for. One repo.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Microsoft 365 Copilot, Copilot Studio, Power Automate, Power Apps, Azure AI Foundry" | Base build: Copilot Studio copilot, Foundry model + retrieval, Power Automate flow, Power Apps overview |
| "Datenpipelines, Schnittstellen und Integrationen ... ETL-/ELT-Prozesse" | Python ETL job: pulls product master data from a mock ERP REST API + CSV exports, cleans/normalises, loads to Azure SQL/Dataverse and indexes technical data sheets for retrieval |
| "Datenqualität ... Data Governance ... Sicherheitsanforderungen" | Data quality checks (schema, required fields, duplicates) with a quality report table; only approved fields reach the copilot; service principal with least privilege |
| "AI-Agenten, RAG, Vektordatenbanken" | Retrieval over data sheets (Azure AI Search index) |

## DAW-specific additions (≈ half a day on top of the base)
1. Document set: 8 fictional technical data sheets for paints/plasters (coverage, drying time, substrates, safety notes) instead of pharma SOPs (keep SOPs switchable).
2. `etl/` Python job (pandas + requests): mock ERP API (FastAPI) → validation (pydantic) → Azure SQL / Dataverse; scheduled via GitHub Actions or Azure Function timer.
3. Data quality report: rows rejected and why; copilot answers cite the data sheet version.
4. README: data flow diagram (sources → ETL → store/index → copilot → flow).

## Exact CV bullets it must live up to (German)
- KI-Assistent in Microsoft Copilot Studio über technische Produktdatenblätter (Retrieval über ein Azure-AI-Foundry-Modell und Azure AI Search), der Anfragen per Power Automate in einen Freigabeprozess überführt; Übersicht in Power Apps.
- Python-ETL-Pipeline von einer ERP-Schnittstelle (REST) nach Azure SQL mit Datenqualitätsprüfungen (Schema, Pflichtfelder, Dubletten) und Qualitätsbericht.
