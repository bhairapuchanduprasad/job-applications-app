# Project brief (variant): Order Inbox Agent, SAP CAP/BTP + n8n track (adesso AI & Automation Developer SAP)

Base brief: applications/2026-10-22_comena_forward-deployed-engineer/_work/project-brief-order-inbox-agent.md.
SAP CAP/BTP changes: applications/2026-10-28_all-for-one_sap-cloud-ai-developer/_work/project-brief-order-inbox-agent.md (build that variant). This file lists only the extra changes for adesso.

## Why for this JD
adesso wants AI solutions hands-on in SAP landscapes (SAP BTP, CAP, SAP Build, Joule), automation with SAP Build Process Automation / Power Automate / n8n, and fast prototypes/MVPs. A real CAP service on BTP trial plus an n8n approval step gives first SAP and automation artefacts.

## Extra changes (about 2 hours)
- Low-confidence order lines go to an n8n workflow (webhook trigger) that sends an approval request (email or Teams) and posts the decision back to the agent API.
- Optional stretch: call the LLM through SAP Generative AI Hub (AI Core trial) or Azure OpenAI via LiteLLM, to cover "externe KI-Plattformen".
- Optional stretch: a Joule Studio custom skill on the BTP trial that queries the CAP order service (only if the trial allows it; otherwise leave out and do not claim).

## CV bullet it must live up to (exact, German)
- AI-Agent für Bestelleingänge: E-Mail-, PDF- und Excel-Bestellungen per LLM-Extraktion erfassen, mit dem Artikelkatalog abgleichen (exakt, Fuzzy, pgvector) und als Auftrag in einem SAP-CAP-Service auf SAP BTP (Trial) über OData anlegen; unsichere Positionen per n8n-Workflow zur Freigabe.
