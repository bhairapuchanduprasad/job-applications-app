# Project brief: Product Q&A Assistant

Repo slug: `product-qa-assistant` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the HOTREGA application.
Time box: 1–2 days with Claude Code.

## Goal
An n8n automation for a cleaning-products manufacturer: incoming customer and retailer emails are sorted (product question, order, complaint, other); product and application questions are answered by a RAG assistant over technical and safety data sheets (e.g. "Can I use the WPC cleaner on oiled wood?"); uncertain answers go to a person for approval. Personal data is removed before any LLM call, answers are labelled as AI-generated, and the process is documented.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Automatisierungs-Workflows (z. B. mit n8n)" | The n8n workflow (self-hosted via Docker) |
| "KI-Assistenten und -Agenten aufbauen, testen, weiterentwickeln" | RAG assistant + labelled question set run on every change |
| "Prompts sowie Entscheidungslogiken für den produktiven KI-Einsatz" | Versioned prompts; routing rules (confidence threshold, category) in the workflow |
| "Prozess- und Ergebnisdokumentationen" | README with process diagram (before/after), results table |
| "EU AI Act und datenschutzrechtliche Anforderungen" | PII redaction step, "AI-generated" label (transparency), data-processing notes, human approval |
| "Microsoft Copilot, ChatGPT, n8n oder vergleichbar" | n8n + OpenAI/Claude API node (pick one; add a note on how it would run with Azure OpenAI / Copilot Studio) |

## Scope (keep it small)
In:
- Data: 10–15 public HOTREGA-style technical/safety data sheets (use public PDFs only for a private demo, or write your own sample sheets to avoid copyright issues).
- Ingest: Python script → chunk → embeddings → vector store (Qdrant in Docker or pgvector).
- n8n (Docker): IMAP/Gmail trigger or a webhook with sample emails → PII redaction (regex + simple NER) → classify (LLM node) → RAG answer via a small FastAPI endpoint → if confidence low or category = complaint → approval step (n8n form / email to a person) → reply draft.
- Labelled set: 25 questions with expected facts; a script scores answers (correct product, correct usage/safety fact, no invented claims).
- Docs: process diagram, prompt versions, decision rules, results, EU AI Act/GDPR notes (no legal claims).
Out: real mailbox, ERP integration, multilingual.

## Architecture
```
email / webhook ─► n8n: redact PII ─► classify ─┬─ product question ─► FastAPI /answer (RAG over data sheets) ─┐
                                                └─ other ─► route to team                                       │
                                     confidence < threshold or complaint ─► human approval ◄────────────────────┘
                                     ─► reply draft labelled "AI-generated"
eval script: 25 labelled questions ─► accuracy table in README
```

## Milestones
1. Data sheets + ingest + vector store. (≈2 h)
2. FastAPI /answer with sources. (≈2 h)
3. n8n workflow: trigger, redaction, classify, routing, approval. (≈3 h)
4. Labelled set + eval script. (≈2 h)
5. Docs: process diagram, decision rules, compliance notes, screenshots. (≈2 h)

## README outline
Problem (repeat product questions to customer service) → Process before/after → Workflow (n8n screenshot) → Decision logic → Results on the labelled set → Data protection & EU AI Act notes → Limitations → How I built it with Claude Code.

## CV bullets this project must live up to
- n8n automation workflow that sorts incoming customer and retailer emails, answers product and application questions from technical and safety data sheets with a RAG-based AI assistant, and routes uncertain cases to a person for approval.
- Prompts and decision logic are versioned and tested on a labelled question set; personal data is removed before any LLM call (GDPR), answers are marked as AI-generated, and the process documentation follows the EU AI Act transparency rules.

When done, mark it `built` in `profile/master-profile.md`; then real results may go on the CV.
