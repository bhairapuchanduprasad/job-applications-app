# Project brief: Order Inbox Agent (flaconi variant)

Base project: `applications/2026-10-22_comena_forward-deployed-engineer/_work/project-brief-order-inbox-agent.md` (status: planned). This variant swaps the mock ERP + TypeScript review screen for the flaconi stack: Google Sheets/Apps Script, Make, GitHub Actions.

## Goal
Show a spreadsheet-driven operations task turned into an automated workflow: order emails, PDFs and Excel files → LLM extraction → catalog matching → Google Sheet, with low-confidence lines routed to a person through Make, all versioned in GitHub and run on a schedule by GitHub Actions.

## Why it matters for flaconi
Covers the JD gaps: Google Apps Script (JS), Make (low-code), GitHub + GitHub Actions scheduled jobs, "converting spreadsheets and multi-step operational tasks into seamless digital pipelines", AI agents.

## Scope (1–2 days)
1. Synthetic data: 30 supplier/order emails (body, PDF, Excel) for beauty products + a product catalog sheet (SKU, name, size, EAN).
2. Python extractor (LiteLLM, Pydantic schema) for order lines; matching: exact EAN/SKU → customer alias map → fuzzy (rapidfuzz) → embeddings.
3. Google Apps Script (clasp, in the repo): web-app endpoint that appends matched lines to an "Orders" sheet and flags low-confidence lines.
4. Make scenario: watches flagged rows, sends a Slack/email approval message, writes the decision back. Export the scenario blueprint JSON into the repo.
5. GitHub Actions: scheduled workflow (cron) runs the Python sync; PR workflow runs pytest + a labelled test set (line-level precision/recall).
6. README with the process map (before/after), runbook, cost per run.

## Stack
Python, LiteLLM, Pydantic, rapidfuzz, Google Apps Script (clasp), Google Sheets API, Make, GitHub Actions.

## Milestones
Day 1: data, extractor, matching, eval. Day 2: Apps Script endpoint, Make scenario, scheduled Action, README + demo GIF.

## Demo
Drop 3 emails into the inbox folder → Action runs → rows appear in the sheet → one low-confidence line gets a Make approval message.

## CV bullet it must live up to
- Automates operational processes run on spreadsheets: order emails, PDFs and Excel files are extracted by an LLM, matched to a product catalog (exact, fuzzy and embeddings) and written to Google Sheets through Google Apps Script; a Make low-code scenario routes low-confidence lines to a person; versioned in GitHub with pull requests, run as scheduled jobs in GitHub Actions with a labelled test set.
