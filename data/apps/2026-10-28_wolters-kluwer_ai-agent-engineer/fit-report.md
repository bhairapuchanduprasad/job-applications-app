# Fit report: Wolters Kluwer Tax & Accounting, AI-Agent Engineer (m/w/d), Ludwigsburg

**Fit score: 64/100.** Strong on the core of the role (agentic workflows with LangGraph, orchestration, tool integration via MCP, evaluation against ground truth, human-in-the-loop review, Python, Azure, AI coding agents). Main gaps: **Java/Kotlin on production JVM systems** (a stated must-have, none in the profile) and **German "hervorragend"** (B1). Seniority reads mid-level ("architectural responsibility"), not senior-titled.

Language: German posting that requires excellent German → German Lebenslauf + Anschreiben (CLAUDE.md rule 3). Found by job-scout (LinkedIn 4419309422). Location Ludwigsburg, mobile work on set days.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Agentenbasierte Systeme gebaut (Orchestrierung, State Handling, Tool-Integration) | Kniit multi-agent LangGraph pipeline; MCP query service; Covestro LangGraph routing agent | ✅ |
| LangChain / LangGraph (Koog, Pydantic AI) | LangGraph + LangChain daily; Koog / Pydantic AI not used | ✅/🟡 |
| Python für Agent Logic und Evaluation | Python 3 yrs; RAGAS/PytrecEval evaluation; Kniit P/R evaluation | ✅ |
| Cloud-native auf Microsoft Azure | Kniit Expert Interface on Azure, Kubernetes, Docker | ✅/🟡 |
| Guardrails, Validierung, Observability für LLMs | ground-truth evaluation, human approval in Expert Interface; no production observability stack evidenced | 🟡 |
| Human-in-the-Loop vs. Autonomie | Expert Interface (experts approve graph changes); deterministic vs agentic choice at Kniit | ✅ |
| KI-gestützte Entwicklung (AI-Coding-Agents) | Claude Code, custom skills, agentic coding | ✅ |
| Starker SE-Hintergrund, Architekturverantwortung, verteilte Systeme | sole developer end-to-end, Python microservices; not large distributed systems | 🟡 |
| Java und Kotlin in produktiven JVM-Systemen | none | ❌ |
| Tax & Accounting Domäne (Bereitschaft) | none, willing; regulated energy domain shows transfer | 🟡 |
| Hervorragend Deutsch, gut Englisch | German B1, English business fluent | ❌ (top gap) |

## Gaps and honest framing
1. **German (top gap):** "hervorragend Deutsch" required; B1. Letter states it openly. Not C1 explicitly, so prepared per scout rules, but this is the most likely rejection reason.
2. **Java/Kotlin:** letter says openly not used productively; willing to learn. Not on the CV.
3. **Production observability/guardrails:** covered by the Agent Eval Harness project (planned).

## Projects on the CV
- **Agent Eval Harness** (`planned`, reused). Variant for this CV: mocked accounting API and a human-in-the-loop approval step above an autonomy limit. Brief: `_work/project-brief-agent-eval-harness.md` → build-first.

## Red flags
- Interview policy: no AI tools during interviews, no virtual backgrounds, on-site interviews possible.
- Salary not stated.

## Company hooks
1. ADDISON KI-Assistent: generative AI for tax practices, callable from other ADDISON apps with current program context ([taxandbytes.de](https://www.taxandbytes.de/tools/ki-recherche-assistenz/addison-ki-assistent)).
2. Wolters Kluwer frames ADDISON AI as a copilot where the user stays the responsible "pilot" ([wolterskluwer.com](https://www.wolterskluwer.com/de-de/solutions/steuern-rechnungswesen/ki-in-addison)). Used in the letter.
3. TAA Deutschland: ADDISON, SBS Software, AKTE; HQ Ludwigsburg ([pressebox](https://www.pressebox.com/newsroom/wolters-kluwer-tax-accounting-deutschland)).
4. No public announcement of autonomous ADDISON agents found; the JD says a shared "Agentic Platform" is being built.
5. Contact named in the JD: Michele Kenmogne (Senior Recruiter).
