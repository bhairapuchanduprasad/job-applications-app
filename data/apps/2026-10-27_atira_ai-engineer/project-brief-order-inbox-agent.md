# Project brief (Atira variant): Order Inbox Agent

Status: planned. Main brief: `applications/2026-10-22_comena_forward-deployed-engineer/_work/project-brief-order-inbox-agent.md`. Build that; this note lists the Atira angle.

## Why it matters for Atira AI Engineer
Proves: multi-format inbound processing (email, PDF, Excel), extraction + matching against product data, ERP write-back via REST, human review of low-confidence cases, labelled eval set in CI. This is a small version of Atira's RFQ inbound flow.

## Atira-specific emphasis (optional, inside 1–2 days)
- Add one long multi-page PDF inbound (e.g. 30+ pages of spec text) to the test set to show chunking for long documents.
- Log per-order LLM cost and latency.

## CV bullets it must live up to (exact, as on the Atira CV)
- AI agent that reads purchase orders from email bodies, PDFs and Excel files, extracts customer, items and quantities, matches each line to a product catalog (exact, customer map, fuzzy, pgvector) and writes a sales order back to a mock ERP through a REST API.
- Django backend with Postgres and a TypeScript review screen where a sales rep confirms low-confidence matches; per-customer configuration and a labelled test set of orders run in CI.
