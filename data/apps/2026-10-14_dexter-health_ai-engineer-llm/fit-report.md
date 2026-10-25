# Fit report: dexter health, AI Engineer (LLM) - Remote

**Fit score: 80/100.** Strong match on the core of the role (LLM workflows that turn messy input into validated structured data, evaluation against ground truth, Claude Code as daily tool, Python + React, small-team ownership). Gaps are domain (healthcare, voice) and self-hosted model serving.

Language: posting in English, asks for "clear written and spoken English"; German only a nice-to-have → English documents. German B1 shown honestly.

## Requirements → evidence

| Requirement | Evidence | Rating |
|---|---|---|
| Strong Python / backend engineering | Python across all roles; FastAPI backends (Covestro agentic app, Kniit microservices) | ✅ |
| AI-powered product features / LLM-based workflows | Kniit LangGraph multi-agent extraction pipeline (sole developer); Covestro agentic app (LangGraph, React + FastAPI, AWS) | ✅ |
| Ambiguous idea → working software quickly | Sole developer at a 4-person startup reporting to CTO; owned pipeline end-to-end; Expert Interface app built from scratch | ✅ |
| Design, test, validate, improve AI outputs | Precision/recall 33%/45% → 93%/90% against SAP-derived ground truth; reflection/consolidation agents | ✅ |
| Integrate AI workflows into production systems | Covestro: Docker + AWS CDK + GitLab CI/CD; Kniit: Azure, Kubernetes, MCP service integrated into Claude Code | ✅ |
| Debugging across logic, data, model outputs, UX | Implied by the Kniit metric work and switching a stream to deterministic extraction; no explicit story yet | 🟡 (prepare a story) |
| Evaluation / quality checks for AI outputs | RAGAS + PytrecEval automated evaluation (Covestro); ground-truth eval at Kniit | ✅ |
| Daily AI dev tools (Claude Code, Cursor, …) | Claude Code with custom skills and agentic coding workflows; built an MCP server for Claude Code | ✅ |
| Structured outputs, validation logic, fallback behaviour | Extraction into a knowledge graph with consolidation/reflection; Expert Interface for human validation. No explicit "fallback" story | 🟡 → project covers it |
| Commercial + open-source LLMs, provider-agnostic | Open Llama 3B QLoRA fine-tune (built repo); commercial LLM APIs at Kniit/Covestro | 🟡 |
| Startup / ambiguity / ownership | Kniit early-stage startup, sole owner of pipeline | ✅ |
| Clear English | Business fluent | ✅ |
| Nice: frontend / fullstack | React frontends at Covestro and Kniit (CV says React beginner in base; profile shows two shipped React apps) | ✅ |
| Nice: self-hosted LLMs, model serving, inference optimization | Only QLoRA fine-tuning of Open Llama 3B; no serving experience | ❌ / 🟡 |
| Nice: improving latency/cost/quality/reliability | $200k projected LLM budget → near-zero; millisecond-latency MCP retrieval; P/R improvement | ✅ |
| Nice: healthcare / regulated environments | None in healthcare. Regulated documents in the energy sector (regulatory/technical docs) | ❌ (adjacent) |
| Nice: structured data extraction, documentation automation, workflow automation | Kniit knowledge extraction from regulatory documents is exactly structured extraction | ✅ |
| Nice: voice workflows | None | ❌ |
| Nice: German | B1 | 🟡 |
| Nice: nursing homes / elderly care | None | ❌ |

## Gaps and honest framing
- **Healthcare / nursing domain:** say it plainly; point to the closest analogue: extracting structured data from domain documents where domain experts validate output (SAP experts at Kniit, chemists at Covestro). dexter's "Pflegekraft prüft jeden Eintrag" is the same human-in-the-loop pattern as Expert Interface.
- **Self-hosted models / serving:** QLoRA fine-tune of Open Llama 3B is real but small. The planned project (below) adds a local open-source model path. Don't claim serving or inference optimization.
- **Voice:** no experience. The planned project starts from transcripts (optionally Whisper); in the interview, say voice input is the part you'd learn first.
- **German B1:** nice-to-have only, but the end users and data are German (care notes). Mention you're improving it; a German-language product means German test data, which you can handle with multilingual models (you benchmarked multilingual embeddings at Covestro).
- **Cursor/Copilot:** not needed; Claude Code is named in the JD.

## Red flags
- 100+ applicants in 2 days on LinkedIn Easy Apply: apply fast.
- "Founder-like urgency", "fast decisions": expect long hours/high pace; small, owner-managed team (no investors), so salary may land at the lower end. Remote across Germany is fine with the Blue Card, but the salary still needs to clear the Blue Card threshold.
- "Fair compensation based on … location": no range given.

## Company hooks (sources)
1. **Human review before anything is saved.** dexter.mobile turns dictated notes (reports, vitals, wounds, measures) into draft entries that the nurse checks before they go into the care software. Same pattern as Expert Interface at Kniit. Source: https://www.dexter-health.com
2. **Writes into existing care software** (Connext Vivendi, Senso, C&S, CareCloud); the care software stays the system of record, so the AI output must be structured and valid for each target system. Source: https://www.dexter-health.com
3. **Measured outcome:** about 20 minutes less documentation time per carer per day (Rummelsberger Diakonie's own survey); 10,000+ care staff use dexter. Source: https://www.dexter-health.com and LinkedIn company page
4. **Data protection as product feature:** EU data centres, heyData-audited against GDPR and the EU AI Act, no training on customer data without explicit instruction. Explains why the JD mentions self-hosted models "for control". Source: https://www.dexter-health.com
5. **Origins:** started 2021 in Cologne with a GDPR-compliant smart speaker for care, tested in a BMBF-funded project with Ruhr University Bochum (geriatric ward); now owner-managed with no financial investors. Sources: https://news.rub.de/node/9281 , https://www.dexter-health.com
