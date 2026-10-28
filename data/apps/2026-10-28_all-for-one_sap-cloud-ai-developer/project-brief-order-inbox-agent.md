# Project brief (variant): Order Inbox Agent, SAP CAP / BTP track (All for One)

Base brief: applications/2026-10-22_comena_forward-deployed-engineer/_work/project-brief-order-inbox-agent.md. This file lists only the SAP-specific changes.

## Why for this JD
All for One wants AI agents and LLMs integrated into SAP applications via APIs, built on SAP BTP and CAP. Replacing the mock ERP with a real CAP service on a BTP trial gives a first hands-on SAP artefact.

## Changes (about 1 extra day)
- CAP project (Node.js, cds) with entities SalesOrder, SalesOrderItem, Product, Customer; OData V4 service; deploy to SAP BTP trial (Cloud Foundry) with SQLite/HANA Cloud trial.
- Python agent posts validated orders to the CAP OData service (OAuth client credentials via XSUAA), reads the product catalog from it for matching.
- Optional: call the LLM through SAP Generative AI Hub (AI Core trial) instead of a direct provider.
- README section: how this maps to an S/4HANA sales order API (API_SALES_ORDER_SRV).

## CV bullets it must live up to (German)
- AI-Agent für Bestelleingänge: E-Mail-, PDF- und Excel-Bestellungen per LLM-Extraktion erfassen, mit dem Artikelkatalog abgleichen (exakt, Kundenzuordnung, Fuzzy, pgvector) und als Auftrag in einem SAP-CAP-Service auf SAP BTP (Trial) über OData anlegen.
- Prüfmaske für unsichere Positionen, Konfiguration pro Kunde, Evaluation mit gelabelten Bestellungen in CI.
