# Project brief: Invoice Capture Agent (variant of Order Inbox Agent, see profile/projects.md)
**Goal:** agent that captures supplier invoices, codes them, matches payments/POs and prepares approval, over a mock Dynamics-style ERP REST API.
**Proves (Truvio JD):** tool calling, structured outputs, human review points, evals, OCR/document AI, ERP data.
**Scope (1-2 days):** 30-50 synthetic invoices (PDF, some scanned) with labels; OCR/PDF text -> LLM extraction into Pydantic (structured outputs); tool calls to a FastAPI mock ERP (vendors, POs, GL accounts, payments); confidence threshold -> review screen (Streamlit) for approval before posting; eval set run in GitHub Actions (field accuracy, coding accuracy, cost, latency); deterministic checks first.
**Stack:** Python, FastAPI, Pydantic, Postgres, Azure OpenAI or OpenAI structured outputs, Streamlit, pytest, GitHub Actions.
**Architecture:** invoice file -> OCR/text -> extractor -> coder + PO matcher (tool calls) -> confidence gate -> review UI -> mock ERP post.
**Milestones:** 1) data + mock ERP, 2) extraction, 3) coding/matching tools, 4) review UI, 5) evals + CI, 6) README with results table and demo GIF.
**CV bullet it must live up to:** reads supplier invoices (PDF/OCR), extracts fields with structured outputs, proposes GL coding and matches to POs via tool calling on a mock ERP REST API; low-confidence lines go to a human review screen, with an eval set of labelled synthetic invoices (accuracy, cost, latency) run in GitHub Actions.
