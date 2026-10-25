# Project brief: Quality Process Copilot (Microsoft Power Platform)

Repo slug: `quality-process-copilot` (no link on the CV; export the solution + screenshots to a repo)
Status: **planned**. Build before submitting the HERMES application (Power Platform is their must-have).
Time box: 1–2 days. Free: Power Apps Developer Plan (includes Power Automate, Dataverse, Copilot Studio trial) + Azure free credits for Azure AI Foundry.

## Goal
A copilot for a pharma manufacturer's quality team. Employees ask questions about SOPs (e.g. "What do I do if a tablet batch fails the weight check?") in Microsoft Copilot Studio; answers come from SOP documents via an Azure AI Foundry model with retrieval. If something went wrong, the copilot starts a deviation report. A Power Automate flow routes the report for review and approval and stores it in SharePoint/Dataverse; a Power Apps screen gives quality managers the overview. Built as reusable components (solution, environment variables, connection references) with documented standards.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Power Platform, insbesondere Power Automate und Power Apps" (must) | Approval flow + canvas/model-driven app |
| "Microsoft Copilot Studio" | The SOP copilot with a "report deviation" topic |
| "Azure, Azure AI Foundry" | Model deployment + retrieval over SOP docs in Azure AI Foundry |
| "KI-Agenten, Copilots ... Optimierung von Geschäftsprozessen" | Copilot + automated deviation process |
| "Integrationen, Workflows ... Anbindung von APIs und Datenquellen" | Copilot → Power Automate → SharePoint/Dataverse; Foundry endpoint via custom connector |
| "Qualitäts- und Betriebsverantwortung" | Test questions with expected answers; flow error handling and run history |
| "wiederverwendbare Komponenten, technische Standards, Best Practices" | Managed solution, environment variables, naming conventions doc |

## Scope
In:
- 6–8 short SOP documents (write your own, generic GMP topics: weighing, cleaning, deviations, labelling).
- Azure AI Foundry: deploy a model; add the SOPs as a data source (retrieval); expose via endpoint.
- Copilot Studio: generative answers over the SOPs (via Foundry or the built-in knowledge source), topic "Report a deviation" collecting batch, product, description.
- Power Automate: triggered by the copilot; creates the record in Dataverse/SharePoint list; approval to quality manager; notification back.
- Power Apps: list + detail screen for deviations with status.
- Test set: 15 SOP questions with expected answers; record pass/fail in README.
- Docs: architecture, naming conventions, how to import the solution into another environment.
Out: real GMP validation, real user data.

## Architecture
```
Employee ─► Copilot Studio copilot ─► knowledge: SOPs (Azure AI Foundry model + retrieval)
                    │ topic "Report a deviation"
                    ▼
            Power Automate flow ─► Dataverse/SharePoint "Deviations" ─► Approval (quality manager) ─► notification
                                                         ▲
                                             Power Apps screen (overview, status)
Solution package: environment variables, connection references, docs
```

## Milestones
1. Environments + SOP docs + Foundry deployment. (≈2.5 h)
2. Copilot Studio copilot with knowledge + deviation topic. (≈3 h)
3. Power Automate approval flow + data store. (≈2 h)
4. Power Apps overview. (≈2 h)
5. Test questions, solution export, README, screenshots. (≈2 h)

## CV bullets this project must live up to
- Copilot in Microsoft Copilot Studio that answers employees' questions from pharma SOP documents through an Azure AI Foundry model with retrieval, and starts a deviation report when something goes wrong in production.
- Process automation on the Microsoft Power Platform: a Power Automate flow routes each deviation report for review and approval and stores it in SharePoint; a Power Apps screen gives quality managers the overview, built as reusable components with documented standards and best practices.

When done, mark it `built` in `profile/master-profile.md`.
