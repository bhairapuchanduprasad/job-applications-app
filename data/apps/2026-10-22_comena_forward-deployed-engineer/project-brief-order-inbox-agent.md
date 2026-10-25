# Project brief: Order Inbox Agent

Repo slug: `order-inbox-agent` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the Comena application (it is also great prep for their take-home).
Time box: 2 days with Claude Code.

## Goal
An AI agent for an industrial distributor: purchase orders arrive as email bodies, PDFs or Excel files. The agent extracts customer, line items and quantities, matches each line to a product catalog (embeddings + fuzzy matching on part numbers and descriptions), and creates a sales order in a mock ERP via REST. Low-confidence matches go to a TypeScript review screen where a sales rep confirms them. Per-customer configuration (e.g. a customer's own part numbers) and a labelled test set of orders run in CI.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "automate order processing from e-mail inbox to ERP" | The whole pipeline |
| "integrating the platform with client data (e.g. product catalog) and systems (e.g. ERP)" | Catalog import + matching; REST integration with a mock ERP (or Odoo's free community API) |
| "understanding clients' custom workflows", "adapt backend logic and UI to client requirements" | Per-customer config: customer part-number mapping, units, required fields |
| "Typescript frontend and Python backend", "Python (Django), Typescript, Postgres" | Django + Django REST Framework + Postgres; React/TypeScript review screen |
| "configuring, testing, and deploying AI agents" | Labelled orders test set in CI; Docker deploy |
| "latest LLMs" | LLM structured extraction (JSON schema), fallback model |

## Scope
In:
- Product catalog: 300–500 fake industrial SKUs (fasteners, bearings, valves) with descriptions and units.
- 25 sample orders: email text, PDF (generated), Excel; some with typos, customer part numbers, unit mismatches.
- Extraction: LLM with a JSON schema → Pydantic validation.
- Matching: exact part number → customer mapping table → fuzzy (rapidfuzz) → embeddings (pgvector); confidence score.
- Django + DRF + Postgres (pgvector); endpoints `/orders/ingest`, `/orders/{id}`, `/orders/{id}/confirm`.
- Mock ERP: small FastAPI or Django app with `/sales-orders` (or Odoo community in Docker).
- TypeScript (React + Vite) review screen: order lines, suggested SKU, confidence, confirm/override.
- Eval: labelled orders → line-level match accuracy, extraction field accuracy; GitHub Actions.
Out: real email inbox (use .eml files), auth beyond a simple token, EDI.

## Architecture
```
.eml / PDF / XLSX ─► Django ingest ─► LLM extraction (JSON schema) ─► matcher (exact → customer map → fuzzy → pgvector)
                                                              │
                                     confidence high ─► mock ERP REST /sales-orders
                                     confidence low  ─► TypeScript review screen ─► confirm ─► ERP
Postgres (orders, lines, catalog, customer config) · CI: tests + eval on 25 labelled orders
```

## Milestones
1. Catalog + sample orders + Django models. (≈3 h)
2. Extraction with schema + validation. (≈2.5 h)
3. Matching cascade + confidence. (≈3 h)
4. Mock ERP + push. (≈1.5 h)
5. TypeScript review screen. (≈3 h)
6. Eval + CI + README + demo GIF. (≈2 h)

## CV bullets this project must live up to
- AI agent for order processing that reads purchase orders from email bodies, PDFs, and Excel files, extracts customer, items, and quantities, matches each line to a product catalog (embeddings plus fuzzy matching), and creates a sales order through a REST API integration with a mock ERP.
- Django backend with Postgres and a TypeScript review screen where a sales rep confirms low-confidence matches before the order is sent; per-customer configuration and a labelled test set of orders run in CI.

When done, mark it `built` in `profile/master-profile.md`; then real results (match accuracy) may go on the CV.
