# Project brief: Tender Document Extraction & Review
Repo slug: tender-doc-extraction. Status: planned. For: Kuro Software Engineer - AI (2026-11-03).

## Goal
Small pipeline that turns construction tender PDFs (public sample bills of quantities, mixed scanned and digital) into structured line items with evidence links, a review UI and an eval harness.

## Why for this JD
Proves: unstructured/multi-modal document ingestion, Prefect orchestration, entity resolution across documents, human review surfaces, evals + error analysis, Langfuse tracking, Postgres.

## Scope (1-2 days)
- Prefect flow: PDF → text/OCR (digital text first, OCR fallback for scans) → LLM extraction of positions (number, text, unit, quantity, price) with a JSON schema.
- Entity resolution: match the same position across two documents (embedding + rules), store in Postgres.
- FastAPI + small React review UI: value next to source page, approve/correct.
- Eval set of ~20 hand-labelled pages, scoring + error analysis report, Langfuse traces.

## Stack
Python, Prefect, FastAPI, Postgres, React, Langfuse, any LLM via LiteLLM.

## Milestones
1. Ingest + extraction. 2. Postgres schema + entity matching. 3. Review UI. 4. Eval set + Langfuse. 5. README.

## README outline / demo
Architecture diagram, run instructions, eval results table; demo: upload PDF, review, see eval score.

## CV bullet it must live up to
"Prefect pipeline for scanned and digital construction tender PDFs: LLM and OCR extraction of line items, entity resolution across documents, a review UI linked to source pages, and evaluation with error analysis in Langfuse."
