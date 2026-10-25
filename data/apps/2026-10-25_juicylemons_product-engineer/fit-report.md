# Fit report: JuicyLemons (recruiter) for an unnamed Berlin AI healthcare startup, Product Engineer (m/f/d), Berlin (hybrid, ~70% on-site)

**Fit score: 62/100.** Solid on the AI side and on "build the whole thing": full web apps with a React frontend and Python/FastAPI backend (Expert Interface on Azure, Covestro agentic app on AWS), AI/ML-driven products, cloud on AWS and Azure, close work with the people who use the tool (SAP experts, chemists, business stakeholders), and small-team start-up experience reporting to a CTO. Weaker on what makes this a *product* engineer role: frontend depth (React is listed as beginner in the base CV, no TypeScript/Next.js), data-informed prioritisation from user behaviour (no product analytics in the profile), formal testing, and the "Mid-Senior" level. No healthcare work experience.

Language: English posting, no German requirement → English documents. B1 German is a plus in a Berlin team, mention only in forms.

Source: https://www.linkedin.com/jobs/view/4483366465. JuicyLemons is a recruiter; the client is a "VC-backed, fast-growing Berlin startup using AI to transform how medical and clinical information reaches healthcare professionals and patients". Hybrid ~70% on-site in Berlin.

## Requirements → evidence
| Requirement | Evidence | Rating |
|---|---|---|
| Strong engineering fundamentals, solving ambiguous problems | Sole developer of the Kniit pipeline end to end; chose agentic vs deterministic strategies per data source ($200k LLM budget → near zero) | ✅ |
| Product-minded, understands the "why" | Deterministic pipeline chosen for cost; Expert Interface built because experts needed to validate graph changes; Covestro consulting: mapped stakeholders' decision workflows before building | 🟡 (no formal product role) |
| Modern frontend + backend web development | React frontend + Python microservices (Expert Interface, Azure); React + FastAPI (Covestro); Streamlit dashboards | 🟡 (React depth; base CV says beginner) |
| Build/improve the web app of an AI-driven product | Expert Interface; Covestro agentic app; Streamlit tool for chemists | ✅ |
| Identify friction in user journeys, turn insights into workflows | Expert validation/approval workflow; Streamlit "simulate before running a batch" for chemists; Covestro workflow advisory | 🟡 |
| Use data and user behaviour to prioritise | Evaluation against ground truth drove what to fix next; no product analytics / A/B tests in profile | ❌/🟡 |
| Partner with product and design | Worked with CTO, SAP domain experts, chemists, business stakeholders; no designer/PM collaboration in profile | 🟡 |
| Architecture decisions | Owned architecture of the extraction pipeline (agentic, deterministic, monolithic strategies), MCP service, microservices | ✅ |
| Clean, tested, maintainable code | Clean code principles, Postman API testing, GitLab CI/CD; unit-test practice not detailed in profile | 🟡 |
| Communication in a small team | 4+4 person start-up, direct line to CTO | ✅ |
| Nice: Python + modern JS framework | Python (expert), React | ✅/🟡 |
| Nice: AI/ML-driven products | Core of the profile (LLMs, RAG, agents, evaluation) | ✅ |
| Nice: Cloud (AWS/GCP/Azure) | AWS (CDK, Lambda, EC2, SQS, DynamoDB), Azure | ✅ |
| Nice: side projects showing product thinking | Old notebooks only; new planned project (see below) | 🟡 (build first) |
| Healthcare domain | None at work; regulated-domain documents (energy) and chemist-facing tools | ❌ |
| Mid-Senior level | 3 years, of which ~1.5 in internships/thesis | 🟡 |

## Gaps and honest framing
- **Frontend depth / TypeScript:** say what is true: React frontends for two internal web apps, paired with Python backends. Don't claim TypeScript or Next.js. Planned project uses React + TypeScript so there is something to show.
- **Product analytics / data-informed prioritisation:** not in the profile. Frame the evaluation loops (measure against ground truth, fix the biggest error class first) as the same habit; the planned project adds simple usage events + a funnel view.
- **Testing:** clean code, API testing with Postman, CI in GitLab; have a concrete testing story ready.
- **Healthcare:** none professionally. Closest: tools for domain experts (chemists, SAP experts) who must trust the output.
- **Seniority:** "Mid-Senior" is LinkedIn's default label for many roles; apply, lean on end-to-end ownership at Kniit.

## Red flags
- Recruiter posting with the client unnamed; ask JuicyLemons for the company name, stage and salary band before investing in interviews (Blue Card threshold must be met).
- ~70% on-site in Berlin: needs a move to Berlin (fine per profile).

## Company hooks (sources)
Research: 4 searches. Nothing public about JuicyLemons as an agency or about the client's identity turned up, so no hooks beyond the posting. Do not guess the company name in any document.
1. AI that changes how medical and clinical information reaches healthcare professionals and patients. Source: posting.
2. Product engineers have a voice in product decisions and work directly with the founding team; not "implement specs". Source: posting.
3. Small team, VC-backed, Berlin, hybrid ~70/30. Source: posting.

## Project for this application (5b)
Planned: **Clinical Info Assistant** (`clinical-info-assistant`), brief in `_work/project-brief-clinical-info-assistant.md`. Covers: React/TypeScript + Python/FastAPI web app, AI-driven product in the medical-information domain, separate HCP and patient journeys, usage events + funnel view (data and user behaviour), tests in CI. Status `build-first`.
