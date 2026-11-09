# Project brief: Newsroom Briefing Assistant

**Goal:** Prototype that turns editorial source material (agency copy, PDFs, transcripts) into a sourced briefing for an editor.
**Why for ida (Editorial Technologist):** proves Python + React/TypeScript prototype from data layer and API to UI, LLM tool for newsrooms, structure that can move to production/CMS. Covers JD keywords: Prototypen, MVP, LLMs, TypeScript, React, API, Datenhaltung, CMS-Integration.
**Scope (1-2 days):** upload/paste a document; backend extracts text, chunks, calls an LLM for summary, key claims each linked to a source passage, and open questions; editor can accept/reject a claim (stored as feedback); simple export as Markdown.
**Stack:** React + TypeScript (Vite), Python FastAPI, Postgres, Claude API, Docker Compose.
**Architecture:** React SPA -> FastAPI (/documents, /briefings, /feedback) -> Postgres (documents, chunks, briefings, feedback); LLM client behind one service module; webhook-style export endpoint as a stand-in for a CMS integration.
**Milestones:** 1) schema + upload + text extraction; 2) briefing endpoint with passage citations; 3) React UI with claim accept/reject; 4) Docker Compose + README + demo.
**README outline:** problem, screenshot, architecture, run locally, limits (LLM can err; citations checked by string match), next steps (CMS adapter).
**Demo idea:** 3-minute screen recording with a public press release.
**CV bullet it must live up to:** "Prototype for editors: agency copy, PDFs and transcripts become a sourced briefing with a summary, key claims linked to passages, and open questions. React front end, FastAPI backend, Postgres, LLM calls behind an API so it can move into a CMS later." Note CV title lists TypeScript: the front end must be TypeScript.
