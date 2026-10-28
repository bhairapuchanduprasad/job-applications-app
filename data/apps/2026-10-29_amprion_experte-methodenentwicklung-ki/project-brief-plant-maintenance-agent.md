# Project brief: Plant Maintenance Agent, Amprion variant (grid assets on Azure AI Foundry)

Repo slug: `plant-maintenance-agent` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-21_siemens-advanta_consultant-ai-new-technologies/_work/project-brief-plant-maintenance-agent.md). Created for Amprion Experte Methodenentwicklung KI (2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
Asset-management assistant for grid equipment: simulated transformer/substation sensor time series (oil temperature, load, dissolved gas) plus inspection notes → data quality checks → anomaly/condition model (Isolation Forest vs XGBoost vs statistical baseline) → agent that explains flagged assets with RAG over public maintenance manuals/standards, using Azure OpenAI in Azure AI Foundry. Results documented as a short method note.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Asset Management" | condition ranking of grid assets |
| "statistische und probabilistische Methoden ... Machine-Learning" | statistical baseline vs Isolation Forest vs XGBoost comparison |
| "Large Language Models ... RAG- und Agentensysteme" | LangChain agent with RAG over manuals |
| "Azure AI Foundry, Azure OpenAI Service" | model + retrieval hosted in Azure AI Foundry |
| "Qualitätssicherung großer heterogener Datensätze" | data quality checks report |
| "Dokumentation", "Veröffentlichung" | method note in the repo (Markdown) |

## Tech stack
Python, Pandas, Scikit-Learn, XGBoost, LangChain, Azure OpenAI (Azure AI Foundry), Azure AI Search, FastAPI, pytest, GitHub Actions.

## Milestones
1. Simulated data + quality checks (3 h) 2. Model comparison (3 h) 3. RAG agent on Foundry (4 h) 4. Method note + README (2 h).

## CV bullet it must live up to (German)
- Asset Management für Transformatoren: Qualitätsprüfung simulierter Sensordaten, Zustandsbewertung mit statistischer Baseline, Isolation Forest und XGBoost, RAG-Agent über Wartungshandbücher mit Azure OpenAI in Azure AI Foundry.
