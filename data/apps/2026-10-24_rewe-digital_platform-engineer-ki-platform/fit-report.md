# Fit report: REWE digital, Platform Engineer Analytics & KI-Platform (m/w/d), Cologne

**Fit score: 60/100.** Strong on the GenAI/MLOps side (hands-on GenAI projects, Python, CI/CD, Docker/Kubernetes, Azure, IaC with AWS CDK) and on solution architecture. Real gaps on the platform-tooling side: no hands-on Snowflake/BigQuery/Databricks, no Terraform, no GCP, and "mehrjährige" platform/DevOps experience is only partly covered (3 years, AI engineering with DevOps parts).

Language: posting is in German with no stated German requirement → English documents (CLAUDE.md rule 3). Large German corporate: German is likely the team language day to day; B1 shown honestly.

Source: https://www.linkedin.com/jobs/view/4386355137 (Job-ID on posting; not used in the letter).

## Requirements → evidence

| Requirement | Evidence | Rating |
|---|---|---|
| Degree in (Business) Informatics or comparable | MSc Artificial Intelligence + Minor in CS & Engineering | ✅ |
| Several years in platform, software, DevOps or data engineering | 3 years AI engineering; Docker, Kubernetes, Azure deployment (Kniit); Docker + AWS CDK + GitLab CI/CD (Covestro) | 🟡 |
| Python | Python in every role | ✅ |
| Snowflake, BigQuery or Databricks | Not in work history (only in planned/idea projects) | ❌ |
| IaC (Terraform), CI/CD | AWS CDK (IaC) and GitLab CI/CD; Terraform not in profile | 🟡 |
| Cloud providers GCP or Azure | Azure (Kniit, Expert Interface; Azure AI Search at Covestro); AWS; GCP not in profile | 🟡 |
| Hands-on MLOps or GenAI projects | Kniit multi-agent LLM pipeline + MCP service; Covestro agentic app + RAG evaluation; ML models at Covestro/Cognizant | ✅ |
| Provide and operate platforms for analytical DBs, ML, GenAI | MCP query service and Expert Interface operated for domain experts; LiteLLM as LLM API layer | 🟡 |
| Solution architecture, integration into system landscape | Sole developer designing the Kniit pipeline end to end (agentic vs deterministic choice); Covestro architecture (React/FastAPI/AWS) | ✅ |
| Automated self-services, support for business teams, best practices | Covestro advisory to business stakeholders; Expert Interface for SAP experts | 🟡 |
| Agile, self-organised cross-functional team | Agile in profile; reported directly to CTO in small team | 🟡 |

## Gaps and honest framing
- **Snowflake/BigQuery/Databricks, Terraform, GCP:** none in work history. Frame: IaC with AWS CDK, cloud on AWS and Azure, quick to transfer. The planned LLM Gateway project extension (Terraform on GCP, BigQuery usage logs) covers these by name once built.
- **Platform team experience:** your work is product-side AI engineering; emphasise the parts that were platform-like (MCP service used by other tools, deployment on Kubernetes/Azure, CI/CD).
- **German:** B1; likely needed for working with business units. Say you are improving it.

## Red flags
- Posting has been online for a while (job ID from earlier 2026 range); could be hard to fill or a pipeline posting.
- "mehrjährige Berufserfahrung" in platform engineering: they may prefer a DevOps/data platform profile.

## Company hooks (sources)
1. **Data Intelligence Platform team:** runs platforms for analytical databases, ML and generative AI for the REWE Group, supporting administration, production, logistics and markets (goals include supply security and less food waste). Source: posting; https://www.arbeitsagentur.de/jobsuche/jobdetail/12608-1385953-4078-1-S
2. **Internal GenAI chatbot:** REWE digital built a chatbot for about 20,000 administrative staff that answers from internal knowledge and opens support tickets; usage took off after a rebranding (about 5,000 automated requests a month); it had to run in Europe for compliance and data protection. Source: https://t3n.de/news/rewe-ki-chatbot-neuer-name-erfolg-1762215/
3. **Computer vision at checkout:** in-house AI to recognise fruit and vegetables at the till. Source: https://www.lebensmittelzeitung.net/tech-logistik/nachrichten/eigenentwicklung-rewe-nutzt-computer-vision-an-der-kasse-191876
4. **Scale (from posting):** over 1 billion records a day, 6 million phones, 32,000 checkouts, 7,300 stores.
5. **Customer data platform on Google Cloud** feeding AI-modelled audiences for advertisers. Source: https://www.textilwirtschaft.de/fashion-management/ki-im-einzelhandel-mit-first-party-daten-den-umsatz-steigern-94304
