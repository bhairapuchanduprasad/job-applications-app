# Project brief: Quality Process Copilot, FERI variant

Repo slug: `quality-process-copilot` (no link on the CV). Status: **planned**.
Base brief: `applications/2026-10-23_hermes-group_ai-engineer/_work/project-brief-quality-process-copilot.md` (pharma SOP copilot, Copilot Studio + Azure AI Foundry + Power Automate + Power Apps). Build that repo; this file lists what the FERI CV adds.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Automatisierungen ... mit individueller Softwareentwicklung und Microsoft Power Automate" | Power Automate approval flow + a small Python/FastAPI service called from the flow via custom connector |
| "KI-Agenten sowie agentenbasierte Anwendungen" | Copilot with a process topic that starts the workflow |
| "Sicherheit, Datenschutz, Berechtigungen, Monitoring und technische Dokumentation" | Role-based access (only approvers see the approval list), no personal data in prompts (redaction step in the Python service), flow run history + error notifications, README docs |

## FERI-specific additions (≈ half a day on top of the base)
1. Second document set: 5 generic internal process guidelines of a fictional asset manager (e.g. onboarding a new reporting request, access request to a data source). Keep the pharma SOP set too; the copilot switches by environment variable.
2. Python/FastAPI endpoint `/redact` (removes names, IBANs, emails before text reaches the model) called by Power Automate via custom connector; pytest tests in GitHub Actions.
3. Permissions: approver security role in Dataverse; document it.
4. Monitoring: flow failure notifications + a simple run log table.

## Exact CV bullets it must live up to (German)
- KI-Assistent in Microsoft Copilot Studio über interne Prozessrichtlinien (Retrieval über ein Azure-AI-Foundry-Modell), der aus einer Anfrage einen Genehmigungsprozess in Power Automate startet und das Ergebnis in SharePoint/Dataverse ablegt.
- Python/FastAPI-Service zur Entfernung personenbezogener Daten vor dem Modellaufruf, angebunden per Custom Connector; Rollen und Berechtigungen für Genehmiger, Fehlerbenachrichtigungen, Tests in CI und technische Dokumentation.
