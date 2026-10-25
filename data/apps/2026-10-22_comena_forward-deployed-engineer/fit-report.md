# Fit report: Comena (YC S25), Forward Deployed Engineer, Munich

**Fit score: 78 / 100.** Strong on the core: you built and deployed LLM agents end to end as sole developer at a small start-up (Kniit), worked against SAP (ERP) system data with SAP domain experts, built full-stack apps (React + Python/FastAPI) and deployed them to AWS/Azure, used Postgres, and did stakeholder-facing AI consulting at Covestro. Gaps: TypeScript and Django (their stack), no email/document-to-ERP order processing, no hands-on ERP API integration.

Language: English posting → English documents.

## Requirements → evidence
| JD requirement | Evidence | |
|---|---|---|
| Configure, test, deploy AI agents | Kniit multi-agent system (LangGraph), evaluated vs ground truth; Covestro agentic app deployed to AWS | ✅ |
| Integrate client data (product catalog) and systems (ERP) | Kniit: knowledge extracted from documents, checked against SAP-system data; no direct ERP API integration | 🟡 → project |
| Understand clients' custom workflows | Covestro AI consulting internship (stakeholders' decision-making workflows); SAP domain experts at Kniit | ✅ |
| Adapt backend logic and UI | Expert Interface (React + Python microservices); Covestro React + FastAPI | ✅ |
| Translate customer needs, training, adoption | Consulting internship; Expert Interface for domain experts; Streamlit tool for chemists | ✅ / 🟡 (training not documented) |
| Full-stack: TypeScript frontend, Python backend | Python ✅; React (beginner), no TypeScript | 🟡 → project |
| Django | FastAPI | ❌ → project |
| Postgres | Kniit stack | ✅ |
| Latest LLMs | LLM APIs via LiteLLM, Claude Code | ✅ |
| High agency, ownership, startup | Sole developer at an early-stage start-up, reporting to the CTO | ✅ |
| Cloud services | AWS (CDK, Lambda, SQS, DynamoDB), Azure | ✅ |

## Gaps and honest framing
- **TypeScript, Django:** say Python is your main language and you have built React frontends; the project covers both.
- **Email → ERP order processing:** the project is exactly this.

## Red flags
- "Work very hard beyond 9–5": decide if that suits you.
- Tiny team (YC lists 2), funding figures inconsistent; on-site Munich.
- Compensated take-home: good sign.
- Pay €80–150k is above your target; don't anchor low (ask €80–85k).

## Company hooks (sources)
1. **Product:** AI reads purchase orders from emails/PDFs/Excel, extracts key info, matches products to SKUs, and pushes the order to the ERP, with or without human review; claims 75–99% time savings ([YC Launch](https://www.ycombinator.com/launches/O3U-comena-ai-agents-that-automate-order-processing-for-distributors-and-manufacturers)).
2. **Founders:** Jiehua Wu (CEO; ex-Google, first sales hire at askLio YC S23) and Almo Sutedjo (CTO; first hire at Leaping AI YC W25; AWS, HubSpot, Microsoft), both TUM computer science ([YC company page](https://www.ycombinator.com/companies/comena)).
3. Industrial supply chains (fasteners, parts, MRO) still type every order into the ERP by hand ([YC Launch](https://www.ycombinator.com/launches/O3U-comena-ai-agents-that-automate-order-processing-for-distributors-and-manufacturers)). Your Kniit SAP-data work and Covestro industrial background are relevant.
4. Funding amount not verifiable (sources conflict); don't mention a number.
