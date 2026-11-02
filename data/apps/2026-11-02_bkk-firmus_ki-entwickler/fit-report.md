# Fit report: BKK firmus, KI-Entwickler (m/w/d), Osnabrück

Source: https://www.linkedin.com/jobs/view/4484326884 (found by job-scout 2026-11-02)
Language: German posting; German not listed in the profile requirements but the LinkedIn note asks for "sufficient German language skills", and the role works with Fachbereiche of a statutory health insurer → German Lebenslauf + Anschreiben (CLAUDE.md rule 3). German B1 = top gap.
Seniority: no years stated; Einstiegsgehalt ab 50.000 € (14 Gehälter), higher by experience; 35-h week; some home-office days.

## Fit score: 72 / 100
Very good technical fit: prompts, LLM workflows and apps, rapid prototypes, use cases with departments. Gaps: German for daily work with Fachbereiche, legal requirements for AI (EU AI Act) not in profile, no health-insurance domain.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Develop prompts, workflows, LLM applications; optimise them | Kniit LangGraph multi-agent workflows + prompt engineering, P/R 33/45 → 93/90; Covestro LangGraph app | ✅ |
| Identify AI use cases with Fachbereiche, idea → implementation | Covestro AI consulting intern: mapped stakeholders' decision workflows, advised on agentic AI; Kniit with SAP domain experts | ✅ |
| Rapid prototypes, testing new AI tech | Claude Code agentic workflows; deterministic vs agentic strategies tested at Kniit | ✅ |
| Build internal GPT environment + use cases for staff | Expert Interface (internal tool for experts); MCP service for internal tooling; no company-wide GPT platform | 🟡 |
| Legal requirements for AI (EU AI Act, DSGVO) | Not in profile | ❌ |
| Degree in Informatik / Data Science / related | MSc AI | ✅ |
| Practical GenAI / LLM experience | Core of profile | ✅ |
| Knowledge of statutory health insurance (nice) | None | ❌ (nice-to-have) |
| German | B1 | ❌ top gap |

## Gaps and honest framing
1. **German B1**: say so in the Anschreiben; documents in German show willingness.
2. **EU AI Act / DSGVO**: not claimed. Planned project describes a design where data stays in-house; do not present as compliance experience.
3. **GKV domain**: none.

## Red flags
- Salary "ab 50.000 €" is below the user's 60–75k range; with 14 salaries and experience-based grading it may reach ~60k. Check Blue Card threshold (IT shortage occupation) is met.

## Company research
Web search found no public news on BKK firmus AI projects. Hooks from the posting itself: ~950 staff, ~1.2 million insured, "TOP"-Arbeitgeber, building an internal GPT environment for employees.

## Projects on the CV
- Interner GPT-Wissensassistent (= Knowledge Assistant for Internal Documents, planned, reused): local open-source LLM, cited answers, eval in CI. Brief: project-brief-knowledge-assistant-mcp.md → build-first.
