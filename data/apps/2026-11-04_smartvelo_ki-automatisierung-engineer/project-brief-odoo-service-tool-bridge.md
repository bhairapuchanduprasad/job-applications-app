# Project brief: Odoo Service-Tool Bridge (SMARTVÉLO variant)
**Goal:** small Python service that connects an internal service tool with Odoo ERP and drafts service reports with an LLM.
**Why for this JD:** proves internal tools, Schnittstellen/Integrationen, Odoo ERP, KI-Automatisierung.
**Scope (1-2 days):** Odoo Community in Docker with demo data (vehicles/products, service orders); FastAPI bridge via Odoo JSON-RPC (read/create service orders, parts); webhook + scheduled sync with retries and logging; LLM endpoint drafting a service report from order data, human approves before it is written back; tiny React or Streamlit service screen.
**Stack:** Python, FastAPI, Odoo (JSON-RPC), Postgres, Docker, pytest, an LLM via LiteLLM.
**Architecture:** Service tool UI -> FastAPI bridge -> Odoo; sync worker + approval queue.
**Milestones:** 1 Odoo + demo data; 2 read/write bridge; 3 sync + retries; 4 LLM draft + approval; 5 tests, README, demo GIF.
**README outline:** problem, architecture, run with docker compose, API, limits.
**CV bullet it must live up to:** FastAPI over Odoo JSON-RPC with sample data (vehicles, service orders), webhook sync with retries and logging, LLM service-report draft with human approval.
