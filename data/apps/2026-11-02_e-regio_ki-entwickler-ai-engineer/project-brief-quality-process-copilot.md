# Project brief: Netzanschluss-Copilot (Quality Process Copilot, e-regio variant)

Base brief: applications/2026-10-23_hermes-group_ai-engineer/_work/project-brief-quality-process-copilot.md (Copilot Studio copilot, Azure AI Foundry model + retrieval, Power Automate approval, Power Apps, managed solution). Build that; this file lists the e-regio changes.

## Why it matters for this JD
Proves the Microsoft stack gaps: Microsoft AI Foundry, Azure AI Services, Copilot Studio, Power Platform; plus MCP + context management, APIs/SQL, quality/cost testing and EU AI Act awareness, in the energy domain.

## Variant scope (1–2 days)
- Corpus: public grid-connection rules of a German DSO (e.g. technische Anschlussbedingungen / FAQ of a Verteilnetzbetreiber), indexed in Azure AI Search; model via Azure AI Foundry.
- Azure SQL table with synthetic grid-connection requests (Antragsnummer, Leistung, Status); small Python MCP server (FastMCP) exposing `get_request`, `list_open_requests`; connected to Copilot Studio as an MCP tool.
- Power Automate flow: copilot hands a Rückfrage to an approver (Teams/Outlook), result written back to SQL.
- Test set (20–30 questions): answer quality, latency, cost per answer; results table in README.
- EU_AI_ACT.md: one page, risk classification of the use case, transparency notice, human oversight.
- Optional: GitHub repo with GitHub Actions running the MCP server tests.

## CV bullet it must live up to (German CV)
- KI-Assistent in Microsoft Copilot Studio über öffentliche Netzanschlussregeln (Microsoft Azure AI Foundry, Azure AI Search), der Antragsdaten über einen eigenen MCP-Server aus Azure SQL abfragt und Rückfragen per Power Automate zur Freigabe gibt; Testset zu Qualität, Latenz und Kosten, Einordnung nach EU AI Act.

When built: mark `built` in profile/master-profile.md with real numbers; only then use it in cover letters.
