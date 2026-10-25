# Fit report: Dr. Theiss Naturwaren GmbH, Solution Consultant KI-Plattformen (m/w/d), Homburg (Saar)

**Fit score: 62/100.** Technically a close match (Data Science, Machine Learning and Generative AI all covered by real work; LLM implementation on AWS and Azure; Python; stakeholder advisory on agentic AI at Covestro as an AI Consulting Intern). Held back by German: the role is the central interface between business departments and IT in a German Mittelstand company, and the posting says applications without sufficient German may not be considered. Second gap: hands-on regulatory work (DSGVO, EU AI Act, NIS2).

Source: https://www.linkedin.com/jobs/view/4481053663 (seniority "Not Applicable", full-time, on-site Homburg, IT team).

Language decision (CLAUDE.md rule 3): posting is in German AND requires "ausreichende Deutschkenntnisse" → **German Lebenslauf + Anschreiben.** Prepared on the user's decision despite B1.

## Requirements → evidence
| Requirement (JD) | My evidence | Rating |
|---|---|---|
| **Sufficient German** (important note in posting; daily work with Fachbereiche, decision makers) | German B1, no certificate | ❌ **top gap** |
| Studium Informatik / Data Science o. ä. | M.Sc. Künstliche Intelligenz (THWS), B.Tech + Minor Computer Science | ✅ |
| Erste/mehrjährige Erfahrung in der Begleitung von KI-, Daten- oder Plattformprojekten | 3 years: Kniit (sole developer, end-to-end, with CTO and SAP experts), Covestro (3 roles), Cognizant | ✅ |
| Implementierung von KI-Lösungen (LLMs, Cloud oder On-Premise) | LangGraph multi-agent system on Azure (Kniit); agentic app deployed to AWS with Docker/CDK (Covestro); RAG evaluation infra on AWS; open-source LLM fine-tuning (QLoRA). On-premise operation not in profile | ✅ (on-prem 🟡) |
| Beratung und Umsetzung von KI-Anwendungen; Bedarfsanalyse bis produktiver Einsatz | Covestro AI Consulting Intern: analysed stakeholders' decision workflows, advised on agentic AI, turned requirements into the solution, built and deployed it | ✅ |
| Schnittstelle Fachbereiche ↔ IT | SAP domain experts + CTO (Kniit), chemists (thesis, Data Scientist intern), business stakeholders (Covestro consulting) | ✅ (in English) |
| Data Science → ML → GenAI breadth | Time-series ML (Covestro, Cognizant), RAG/agents/evaluation (Kniit, thesis) | ✅ |
| Implementierungs- und Einführungsprojekte with internal teams and **external service providers** | Built and handed over systems; no documented vendor management | 🟡 |
| Komplexe Themen zielgruppengerecht aufbereiten (Entscheider, Fachanwender, Tech) | Expert Interface for domain experts; reporting to CTO; dashboard for chemists; publication | 🟡 (no explicit training/presentation evidence; German) |
| **Regulatorik: DSGVO, EU AI Act, NIS2** | Not in profile. Planned project Product Q&A Assistant covers PII redaction + EU AI Act transparency notes; NIS2 nothing | ❌ |
| Interest in AI trends, learning | Claude Code, MCP, agentic workflows at Kniit; Udemy certificates | ✅ |
| Nice: Python | Main language since 2021 | ✅ |
| Nice: ML or Generative AI | Core of every role | ✅ |

## Gaps and honest framing
- **German (B1):** say it plainly in the Anschreiben logistics line ("Deutschkenntnisse auf B1-Niveau, die ich aktiv ausbaue"). Lean on: documentation and technical teams often work in English; German letter shows willingness. Do not claim more than B1. Expect this to be the main screening risk.
- **DSGVO / EU AI Act / NIS2:** no hands-on compliance work. Frame: human approval steps and expert validation built into Kniit/Covestro systems (true), plus the planned Product Q&A Assistant (PII removal before LLM calls, AI-generated labels, EU AI Act notes). Read up on AI Act risk classes and NIS2 basics before an interview. Never claim compliance experience.
- **External service providers / rollout management:** not documented. Leave out; in interview talk about handover of the Kniit pipeline and working with SAP experts.
- **On-premise LLMs:** only cloud deployments and open-source fine-tuning; leave out of claims.

## Red flags
- "Applications without sufficient German may not be considered": real filter. Low probability unless they accept English in the IT team.
- On-site in Homburg (Saar), relocation needed. Salary unknown; check Blue Card threshold (Mittelstand pharma/cosmetics may pay below €60k range).
- Seniority open ("Erste oder mehrjährige Erfahrung"): fits junior-to-mid.

## Company hooks (sources)
1. Founded 1978 by pharmacist Prof. Dr. Peter Theiss out of the Markt-Apotheke in Homburg; brands include Medipharma Cosmetics, Lacalut, Allgäuer Latschenkiefer, Dr. Theiss and proff; Dolorgiet (topical ibuprofen) acquired 2015. Source: https://www.apotheke-adhoc.de/nachrichten/detail/markt/die-frauenversteher-aus-homburg-dr-theiss-naturwaren/ (2018), https://www.apotheke-adhoc.de/nachrichten/detail/markt/kosmetikhersteller-theiss-hofft-auf-dolorgiet/
2. International footprint: products in 60+ countries, ~20 subsidiaries, most revenue from abroad (2018 figures, treat as dated). Source: apotheke-adhoc 2018 article above.
3. Own GMP-certified production in Homburg for skin, body, hair care and decorative cosmetics, "Made in Germany"; pharmacy products regularly awarded ("Beste Neueinführung", "Top Marke"). Source: the posting.
4. The role sits in the IT team and covers Data Science, ML and GenAI platforms plus DSGVO / EU AI Act / NIS2: suggests an early-stage, cross-department AI platform build-up. Source: the posting. No public news on their AI or IT strategy found (2 searches).

## CV tailoring decisions
- Tagline: "AI Engineer" (broadest of the three for a platform consultant role spanning DS, ML and GenAI).
- Location: Homburg (Saar).
- Project: reuse planned **Product Q&A Assistant** (RAG over technical/safety data sheets, PII redaction, human approval, EU AI Act/GDPR documentation), framed for pharmacy/cosmetics product data. Covers DSGVO/EU AI Act and Fachbereich process thinking. Status: planned → application is **build-first**.
- Built project kept: QLoRA fine-tuning of Open Llama 3B (only if space allows).

## Build result
- CV 2 pages, Anschreiben 1 page, 0 overfull boxes. Reviewer round 1: all MUST and SHOULD fixes applied (internship wording, "prognostiziert", Profil wording, header icons, grammar).
- ATS coverage 75% (15/20). Honest gaps not added: Solution Consultant (title), Einführung (rollout), NIS2, On-Premise, Präsentation.
- Status build-first: build `product-qa-assistant` before submitting; if not built, remove the Projekte section.
