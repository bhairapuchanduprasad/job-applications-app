# Fit report: Bestandsfaktor, Founding Software Engineer (KI-Startup Köln, m/w/d), remote

**Fit score: 70/100.** Good match on the core of the role: owning a system end to end as the only developer at an early-stage start-up (Kniit, reporting to the CTO), designing pipeline architecture with data, automation and routing logic, Python backends and APIs, and AI-assisted development with Claude Code. Gaps: three years of experience for a role that owns the whole architecture and leads external developers, no hands-on leadership of freelancers, no insurance/CRM or marketing-automation domain, and German (implicit for a German founder team serving German brokers).

**Language decision:** the posting is in German but names no German requirement → English CV + cover letter (CLAUDE.md rule 3). German B1 is shown on the CV. A small German founder team working with Versicherungsmakler will very likely work in German day to day: see gaps.

Source: https://www.linkedin.com/jobs/view/4481074834. Seniority on LinkedIn: Associate. Full-time, remote ("Remote-Arbeit mit hohem Vertrauen"), start-up based in Köln. No contact person, no deadline, no salary info.

## Requirements → evidence

| Requirement (JD) | Evidence | |
|---|---|---|
| Technische Gesamtarchitektur entwickeln und verantworten | Kniit: sole developer of the knowledge-extraction system end to end (ingestion, chunking, prompts, indexing; agentic, deterministic and monolithic strategies), reporting to the CTO | ✅ (scale: one system, small team) |
| Systemlogiken für Daten, Trigger, Automatisierung und Routing | Kniit: parallel multi-agent extraction + deterministic pipeline for a second source stream; Covestro: LangGraph app routing requests to vector search, inference or summarization; thesis: event-driven AWS (Lambda, SQS, DynamoDB) | ✅ / 🟡 (no customer-event trigger system, i.e. marketing/CRM automation) |
| Schnell weiterentwickelbar ohne Chaos; Qualitätsanspruch | Clean code principles, Docker, GitLab CI/CD, ground-truth evaluation that drove precision/recall 33%/45% → 93%/90% | ✅ |
| Technische Entscheidungen mit Produktbezug | Kniit: chose a deterministic, code-based pipeline for a high-volume stream, cutting a $200,000 projected LLM budget to near-zero recurring cost; built Expert Interface so domain experts can approve graph changes | ✅ |
| Mit Gründerteam Hebel herausarbeiten | Direct line to Kniit CTO; worked with SAP domain experts; Covestro consulting (translating stakeholder workflows into a solution approach) | ✅ |
| Externe Entwickler / Freelancer technisch führen | Not in profile | ❌ |
| Moderne Entwicklungsumgebung mit KI-gestützten Workflows | Claude Code with custom skills, agentic coding workflows; MCP server integrated into Claude Code | ✅ |
| Skalierbar, robust | Kubernetes, Docker, Azure, AWS CDK; millisecond-latency retrieval service | 🟡 (no production load numbers) |
| Starke Architektur-/Systemdesign-Fähigkeiten (Wichtig) | Multi-strategy pipeline design, microservices + React app, AWS infra as code | 🟡 (3 years; founding-engineer level is a stretch) |
| Eigenständig, kein großes Unternehmen nötig | Sole developer at a pre-funding start-up | ✅ |
| Nice: Plattformprodukte, Automatisierung, datengetriebene SaaS | Automation pipelines and data-driven extraction; no SaaS product ownership | 🟡 |
| Nice: API-first, Integrationen, skalierbare Backends | FastAPI, Python microservices, MCP query service, REST testing with Postman; integration with SAP-derived data | ✅ / 🟡 (no third-party CRM/broker system integrations) |
| Nice: kleine, leistungsstarke Tech-Setups aufbauen | Built Kniit's pipeline + Expert Interface alone | ✅ |
| Nice: AI-gestützte Softwareentwicklung | Claude Code daily, custom skills | ✅ |
| German (implicit) | B1, no certificate | 🟡 / ❌ if the founders expect German as the working language |

## Gaps and honest framing
- **Leading external developers / freelancers:** never done. Frame: set up the conventions, CI and evaluation that others would work against (clean code, Claude Code skills, ground-truth tests). Don't claim leadership.
- **German:** B1. The letter states B1 once in the logistics line; in the interview be upfront that English is the working language for technical work and German is improving. Ask early whether German is required with brokers.
- **Seniority:** founding engineer owning the whole architecture with 3 years' experience. Lean on Kniit as a real "sole developer at a start-up" case; LinkedIn tags the role "Associate", which helps.
- **Domain (insurance brokers, CRM/broker management systems, outreach automation):** none. The trigger/routing project (planned) shows the pattern, but it must be built before submitting.
- **Monitoring / learning loops in production:** evaluation yes, production monitoring not in profile.

## Red flags
- Very small team ("direkter Draht zum Gründer"); no salary info. Check that the offer meets the EU Blue Card threshold.
- "Externe Entwickler führen" + "Gesamtarchitektur verantworten" is a lot of responsibility for one hire; clarify scope and budget.
- Company barely visible online (website only); the 50,000-customer figure is from the posting.

## Company hooks (sources)
1. Product: helps Versicherungsmakler grow from their existing client base with occasion-based service outreach instead of cold campaigns; three steps: analyse the portfolio and prioritise opportunities, send personalised service messages tied to real occasions, client interacts and books appointments or updates missing data. Source: https://www.bestandsfaktor.de
2. Named services: GKV-Beitrags-Wächter (annual health insurance premium increases), Neuwert-Retter Hausrat (underinsurance from inflation), 360°-Absicherungs-Radar (coverage gaps). Source: https://www.bestandsfaktor.de
3. Automatic data sync with the brokers' management system ("MVP"), so integrations are core to the product. Source: https://www.bestandsfaktor.de
4. Posting: after a few weeks the system already serves over 50,000 insurance customers of their brokers; software is the internal engine behind analysis, delivery, data capture, monitoring and learning curves; UI is secondary. Source: posting.
5. Team on the website: Thorben Schlätzer (Strategy & Management), Elisa Sedlak, Nico Möhn (Technology & Development), Moritz Oswald. No hiring manager named in the posting, so the letter uses a team greeting. Source: https://www.bestandsfaktor.de
