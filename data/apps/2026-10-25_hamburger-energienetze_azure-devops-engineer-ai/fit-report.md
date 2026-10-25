# Fit report: Hamburger Energienetze GmbH, Azure DevOps Engineer mit Fokus Azure AI (a*), Hamburg

**Fit score: 52/100.** Strong on the AI half (LLMs, RAG, Azure AI Search, deployment on Azure, CI/CD, infrastructure as code with AWS CDK) and a genuine energy-sector hook (Kniit, German energy sector), but the core of the role is Azure platform engineering (Azure DevOps, Terraform, Entra ID, Key Vault, Private Endpoints, Landing Zones) that the profile does not cover, and they ask for very good German (I have B1). Prepared on the user's decision.

Language: posting in German and requires "sehr gute Deutschkenntnisse in Wort und Schrift" → German Lebenslauf + Anschreiben (CLAUDE.md rule 3). German level shown honestly as B1.

Source: https://www.linkedin.com/jobs/view/4481054657. Contact: none named. Deadline: none stated. Pay: collective agreement (Tarifvertrag), "überdurchschnittlich".

## Requirements → evidence
| Requirement | Evidence | Rating |
|---|---|---|
| **Sehr gute Deutschkenntnisse in Wort und Schrift** | German B1, no certificate | ❌ **top gap** |
| Degree in Informatik, Data Science, Mathematik or comparable | MSc Artificial Intelligence (THWS) + Minor in Computer Science | ✅ |
| Azure DevOps (as a daily tool) | Azure used at Kniit (Expert Interface deployed on Azure); CI/CD in GitLab, not Azure DevOps | 🟡 / ❌ |
| Git | Git, GitLab | ✅ |
| Terraform, IaC for Azure resources | IaC with AWS CDK (Covestro: Lambda, SQS, DynamoDB, EC2); no Terraform | 🟡 (concept yes, tool no) |
| Standardised CI/CD pipelines, templates, starter kits, reference solutions | GitLab CI/CD at Covestro; deployment of containerised stacks; no template/starter-kit work in profile | 🟡 |
| Entra ID, Key Vaults, Private Endpoints, Networking, Landing Zones | AWS VPC only; none of the Azure items | ❌ |
| Monitoring | Not in profile beyond evaluation of model quality | ❌ |
| Azure AI stack: Azure OpenAI, AI Foundry, Cognitive Services, AI Search | Azure AI Search (Covestro thesis tech stack, vector DBs); Azure deployment at Kniit; no Azure OpenAI/Foundry | 🟡 |
| LLMs and RAG technologies/architectures (plus) | Kniit multi-agent LangGraph pipeline (P/R 33/45 → 93/90), GraphRAG, MCP; Covestro RAG pipelines + RAG evaluation (RAGAS, PytrecEval), embedding benchmark on 1M+ chunks | ✅ strong |
| Evaluating and implementing AI use cases with IT platform teams (advisory) | Covestro AI Consulting Intern: worked with business stakeholders, advised on agentic AI, translated requirements into a solution approach; Kniit: SAP domain experts, reported to CTO | ✅ |
| Cost control for platform operation ("wirtschaftlich") | Kniit deterministic pipeline cut a $200,000 projected LLM budget to near-zero recurring cost | ✅ (LLM cost, not cloud FinOps) |
| Moving solutions into operations | Covestro agentic app deployed to AWS; Kniit Expert Interface on Azure; Kubernetes, Docker | ✅ |
| Governance / security structures | Human validation/approval workflow (Expert Interface); no formal governance/security role | 🟡 |
| Energy sector (implicit) | Kniit: knowledge extraction for the German energy sector with SAP domain experts; Cognizant: EV load forecasting | ✅ hook |

## Gaps and honest framing
1. **German (top gap):** role wants very good spoken and written German; I am at B1 with no certificate. The posting's note says applications without sufficient German may not be considered. Anschreiben states B1 honestly. This is the most likely reason for rejection.
2. **Azure platform engineering (Azure DevOps, Terraform, Entra ID, Key Vault, Private Endpoints, Landing Zones, Monitoring):** not in profile. Frame: infrastructure as code and CI/CD with AWS CDK and GitLab, deployment on Azure and Kubernetes; the planned Projects entry (Azure AI RAG Starter-Kit) is designed to close exactly this gap and must be built before submitting. Do not claim any of these tools in experience bullets.
3. **Azure OpenAI / AI Foundry / Cognitive Services:** not used; Azure AI Search is real. LLM work went through LiteLLM; say that the patterns (RAG, evaluation, cost control) carry over.
4. **Seniority/role type:** this is a platform/DevOps role with AI focus; my profile is AI engineering first. Lean on "bringing AI use cases into operation" and the advisory part.

## Red flags
- "Applications without a valid work permit and sufficient German language skills may not be considered." Blue Card covers the permit; German is the risk.
- Large merged public utility (2,400+ staff), tariff pay: formal process, likely German-only interviews.

## Company hooks (research, 2026-10-25)
1. Hamburger Energienetze was formed on 2 Sep 2024 by merging Stromnetz Hamburg and Gasnetz Hamburg; organisational integration runs until 2027. It operates a 30,000+ km power distribution grid and a 7,800 km gas grid for about 1.4 million households, and is also the default metering operator (grundzuständiger Messstellenbetreiber). Sources: https://stadt-und-werk.de/meldung_44460_Fusion+der+Netzgesellschaften.pdf, https://www.zfk.de/unternehmen/nachrichten/senat-beschliesst-zusammenschluss-von-stromnetz-und-gasnetz-in-hamburg
2. Hydrogen: Hamburg's hydrogen network (HH-WIN), with the first 40 km planned to go live in 2027; Gasnetz Hamburg invested upfront in it. Source: https://www.zfk.de/unternehmen/nachrichten/4-millionen-euro-gasnetz-hamburg-geht-fuer-wasserstoffnetz-in-vorleistung
3. AI already on the agenda: stadt + werk 7/8 2025 ran a piece on what Hamburger Energienetze considers when using AI, and the company is also hiring a Senior IT Consultant for inhouse AI automation / Copilot agents. Sources: https://www.stadt-und-werk.de/wp-content/uploads/2025/07/stadt_werk_07_08_2025_S04_Inhalt.pdf, https://praktischkommune.de/jobs/91476424-senior-it-consultant-inhouse-ai-automation-copilot-agent-befristet-bis-31-12-2028-a-hamburg
4. Two merged companies means two IT landscapes to bring together: standardised pipelines, templates and a shared Azure AI platform (the role's tasks) fit that moment. (Inference from the merger, not a stated fact; phrase carefully.)
5. No public tech-stack details or named hiring manager found beyond the posting.

## Projects (5b)
- No `built` or `planned` project in the profile covers Azure + Terraform (LLM Gateway's Terraform variant is GCP; Quality Process Copilot is Copilot Studio; Plant Maintenance Agent is Snowflake/sensor-focused). New planned project: **Azure AI RAG Starter-Kit** (Terraform, Azure DevOps Pipelines, Azure OpenAI, Azure AI Search, Key Vault, Private Endpoints, Entra ID managed identity, Azure Monitor) over public grid-connection documents. Brief: `_work/project-brief-azure-ai-rag-starter-kit.md`. Status: build-first.
