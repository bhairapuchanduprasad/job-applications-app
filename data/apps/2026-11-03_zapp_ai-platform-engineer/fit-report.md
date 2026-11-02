# Fit report: Zapp Precision Metals GmbH, AI Platform Engineer (m/w/d), Schwerte

Source: https://www.linkedin.com/jobs/view/4484373124 (found by job-scout 2026-11-03)
Language: German posting, no German language requirement stated → English CV + cover letter (CLAUDE.md rule 3). Risk: a German Mittelstand manufacturer may expect German day to day; B1 to be mentioned openly in the letter.
Seniority: Associate. Degree + good Python/API/MCP knowledge, Azure experience; GenAI/agentic "idealerweise". Good level match.

## Fit score: 76 / 100
Almost every bullet maps to Kniit: agentic GenAI from prototype to stable operation, MCP service, APIs, Azure, evaluation against ground truth. Gaps: platform standards (quality gates, versioning, CI deployment as a team standard), identity/permissions/AI governance with IT security, monitoring in production.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Degree (Informatik/Data Science) | MSc AI | ✅ |
| Python, APIs, system integration, REST, MCP | Python, FastAPI REST, MCP query service (Kniit), Python microservices | ✅ |
| Azure, scalable AI architectures | Expert Interface on Azure, Azure AI Search, Kubernetes; AWS CDK | ✅ / 🟡 |
| GenAI + agentic AI from prototype to production | LangGraph multi-agent pipeline, Covestro agent deployed to AWS | ✅ |
| Standards for versioning, automated tests, deployment, operations | GitLab CI/CD, Docker, clean code | 🟡 |
| Monitoring, evaluation, quality gates | P/R evaluation vs SAP ground truth; RAGAS/PytrecEval; monitoring ❌ | 🟡 |
| Identity management, permissions, security, AI governance | Expert Interface approval workflow (domain experts approve changes); no IAM/governance work | ❌ (planned project) |
| German | not required in posting; B1 | 🟡 |

## Gaps and honest framing
1. Platform governance (Entra ID, permissions, AI governance): not done; planned project covers it.
2. Production monitoring/quality gates: evaluation yes, CI gates not yet. Say so.
3. German: posting is German; mention B1 openly.

## Red flags
Very short posting, no team size or tech stack beyond Azure. Metal manufacturer: AI platform may be early stage (good for ownership, check mentoring).

## Company hooks
1. Zapp is a family-owned group; lead company Zapp Precision Metals GmbH with headquarters in Schwerte plus Ratingen and Unna ([Zapp corporate structure](https://www.zapp.com/en-us/about-us/corporate-structure), [Wikipedia](https://en.wikipedia.org/wiki/Zapp_Group)).
2. Makes precision strip, wire and bar materials ([brochure](https://www.zapp.com/fileadmin/_documents/Downloads/PS/brochures/Brochure%20PRECISION%20STRIP.pdf)); also hires for digitalization & process quality ([posting](https://www.itjobswatch.co.uk/jv/Zapp-Precision-Metals-GmbH/Digitalization-Process-Quality-Specialist-Job-Sheffield-England-UK-4zajjh)).
3. Schwerte is ~40 km from Essen (no relocation needed; letter states based in Schwerte area per rule).

## Project
Internal AI Platform (AI Gateway Platform variant, planned): see project-brief-ai-platform-azure.md.
