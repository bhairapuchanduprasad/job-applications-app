# Fit report: Amadeus Fire (Personalvermittlung) for an electronics manufacturer, AI Solutions Engineer (m/w/d) LLM, RAG & Automation, Saarbrücken

**Fit score: 70/100.** Strong: GenAI/LLM/RAG + AI agents from PoC to production use (Kniit pipeline end-to-end, Covestro agent deployed to AWS, RAG thesis), Python, APIs (FastAPI), SQL, working with business units (Covestro AI consulting, SAP experts), evaluating cloud and open-source options (LiteLLM, QLoRA on open-source LLMs, embedding benchmark), SAP-derived data. Gaps: Microsoft 365 / DMS / production-system integrations (none directly), on-premises deployment, "fundierte Erfahrung in der Softwareentwicklung" at Professional/Experienced level (~3 yrs), German not stated (B1).

Found by job-scout (LinkedIn 4484493775). Recruiter: Amadeus Fire AG, Niederlassung Mannheim, contact Robert Thome; client unnamed ("etabliertes, international tätiges Unternehmen aus dem technologie- und energienahen Industrieumfeld", Elektronikhersteller). Salary range €65–85k (JD). Hybrid up to 2 days/week.
Language: German posting, no German requirement stated → English documents (CLAUDE.md rule 3; same call as the HDP case). Note for the user: a German client in Saarbrücken likely expects German at work; consider a German version if the recruiter asks.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Studium Informatik/Data Science/… | MSc AI | ✅ |
| Softwareentwicklung Python, APIs, SQL | 3 yrs Python, FastAPI, Postgres/SQL | ✅ |
| GenAI, LLMs, RAG (praktisch) | Kniit, thesis, Covestro | ✅ |
| AI Agents (ideal) | Kniit multi-agent, Covestro LangGraph | ✅ |
| PoC → produktiver Einsatz | Kniit pipeline built and handed over; Covestro deployment | ✅ |
| Integration M365, ERP, DMS, Produktionssysteme über APIs | SAP-derived ground truth; MCP API over KG; no M365/DMS | 🟡 |
| Cloud, On-Prem, Open-Source AI evaluieren | AWS, Azure; open-source LLM fine-tuning (QLoRA), LiteLLM; no on-prem | 🟡 |
| Prozesse digitalisieren mit Fachbereichen | Covestro AI consulting; SAP experts | ✅ |

## Gaps and honest framing
1. **M365 / DMS / production systems:** not done; project adds Microsoft Graph + DMS step.
2. **On-premises:** none; open-source models via QLoRA and LiteLLM are the closest.
3. **German:** not stated; B1 in the letter.

## Red flags
- Recruiter role, client unnamed; agency says "ohne Anschreiben" (letter optional).
- Professional/Experienced level; range €65–85k suggests mid-level.

## Company hooks
- Client unknown; only JD facts usable (electronics manufacturer, technology- and energy-related industry, international). No research possible on the client.

## Projects on the CV
- **Order Inbox Agent** (planned, reused; variant: orders from an Outlook mailbox via Microsoft Graph API, PDFs filed to a DMS (SharePoint document library), extraction + catalog matching, write to a mock ERP via REST; open-source LLM option via Ollama behind LiteLLM). Brief: `_work/project-brief-order-inbox-agent.md`. Status: build-first.
