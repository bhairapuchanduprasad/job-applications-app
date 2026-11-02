# Project brief: Leasing-Dokumentenextraktion (Order Inbox Agent variant)
Repo slug: leasing-document-extraction. Status: planned. For: vent.io Data / Software Engineer - AI & Data (2026-11-03).

## Goal
A Python service that turns synthetic leasing offers and supplier invoices (PDF) into validated structured records, matched to an asset catalogue, with a review flag for uncertain fields.

## Why for this JD
Proves FastAPI, Pydantic, SQLAlchemy, PostgreSQL, Azure OpenAI Structured Outputs, OCR, embeddings + vector search, Databricks batch input, pytest, GitHub Actions, Docker, Azure Container Apps, Terraform.

## Scope (1–2 days)
- 30 synthetic PDFs (offers, invoices) generated from templates; 10 scanned-style images.
- OCR (Azure AI Document Intelligence free tier or Tesseract) → text.
- Extraction with Azure OpenAI Structured Outputs into a Pydantic schema (lessee, supplier, asset, net price, term, VAT).
- Asset matching: exact → fuzzy → pgvector embedding search over a 200-row asset catalogue.
- FastAPI REST endpoints (upload, get record, list flagged); SQLAlchemy models on PostgreSQL.
- Batch job that loads the asset catalogue from a Databricks Free Edition table (fallback: CSV).
- pytest: unit + a labelled set (field-level accuracy); GitHub Actions runs tests + eval.
- Dockerfile; Terraform for Azure Container Apps + Postgres Flexible Server (apply optional, plan in CI).

## Architecture
PDF → OCR → LLM (structured output) → validation (Pydantic) → matcher (exact/fuzzy/pgvector) → Postgres → FastAPI.

## Milestones
1. Data + schema + OCR. 2. Extraction + validation. 3. Matcher + DB + API. 4. Tests/eval in CI. 5. Docker + Terraform + README.

## README outline
Problem, architecture diagram, how to run, eval results table, limits.

## Demo
Upload a PDF in Swagger UI → structured record + matched asset + flag.

## CV bullets it must live up to
- REST-API mit FastAPI, Pydantic und SQLAlchemy, die synthetische Leasing-Angebote und Rechnungen per OCR einliest, Felder mit Azure OpenAI Structured Outputs extrahiert, Positionen über Embeddings und Vector Search (pgvector) einem Objektkatalog in PostgreSQL zuordnet und unsichere Felder zur Prüfung markiert.
- Batch-Pipeline lädt Stammdaten aus einer Databricks-Tabelle; pytest-Suite mit gelabeltem Testset in GitHub Actions; Docker-Image auf Azure Container Apps, bereitgestellt mit Terraform.
