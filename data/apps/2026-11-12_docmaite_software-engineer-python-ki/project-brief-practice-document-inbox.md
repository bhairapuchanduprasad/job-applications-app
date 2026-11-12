# Project brief: Practice Document Inbox (repo slug: practice-document-inbox)
**Goal:** Django app where practice staff upload scanned letters/lab reports; a local model classifies each document and extracts key fields into PostgreSQL; Bootstrap review screen for corrections.
**Why for DOCMAiTE JD:** proves Django, PostgreSQL, Bootstrap, local models, Dokumentenklassifikation/Extraktion, automated tests, CI, Docker.
**Scope (1-2 days):** synthetic documents only (no real patient data). Upload -> OCR/text -> classify (small Hugging Face model or Ollama model) -> extract fields (name, date, doc type) -> review/correct screen.
**Stack:** Python, Django, PostgreSQL, Hugging Face Transformers, Ollama, Bootstrap, Docker Compose, pytest, GitHub Actions.
**Architecture:** Django app + `ModelService` interface (local vs cloud backend) + Postgres models Document/Extraction + simple Django templates with Bootstrap.
**Milestones:** 1 Django skeleton + Postgres + Docker; 2 upload + classification; 3 field extraction + review screen; 4 pytest + CI; 5 README + demo.
**README outline:** problem, architecture, run with Docker Compose, model swap, eval on 20 synthetic docs, limits.
**Demo idea:** upload 5 mixed synthetic documents, show classification and correction.
**CV bullet it must live up to:** Django web app where practice staff upload scanned letters and lab reports; a locally running model classifies each document and extracts key fields into PostgreSQL, with a Bootstrap review screen for corrections; covered by pytest tests and a CI pipeline, packaged with Docker Compose.
