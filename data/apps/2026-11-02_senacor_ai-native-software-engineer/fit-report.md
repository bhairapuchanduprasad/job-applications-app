# Fit report: Senacor Technologies, AI-Native Software Engineer (m/w/d), Hamburg

Source: https://www.linkedin.com/jobs/view/4484342708 (found by job-scout 2026-11-02)
Language: German posting, but the profile section names no German requirement (only the generic LinkedIn note) → English CV + cover letter per CLAUDE.md rule 3. Senacor is a consultancy with German clients, so German will matter in practice: flagged.
Seniority: no years given ("fundierte Erfahrung"); greenfield process platform.

## Fit score: 66 / 100
Strong on the AI-native part (Claude Code, skills, agentic coding as a fixed part of work; MCP; LLM concepts RAG/tool use/orchestration) and Python microservices/APIs. Gaps: TypeScript/Java/Go, distributed systems depth, authentication, observability, code reviews as a named practice, German for client work.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Microservices, APIs, automation components | Python microservices backend (Expert Interface), FastAPI (Covestro), MCP service | ✅ |
| AI-supported SDLC: coding agents, code generation, automated tests | Claude Code, custom skills, agentic coding workflows (Kniit) | ✅ / 🟡 (automated tests: Postman API tests, RAGAS eval; no unit-test framework named) |
| Translate requirements with architecture into robust solutions | Covestro consulting intern; Kniit with CTO + SAP experts | ✅ |
| Engineering standards, CI/CD, test strategy, observability | GitLab CI/CD ✅; observability ❌ | 🟡 |
| Evaluate new AI/agent/dev tools pragmatically | MCP into Claude Code; deterministic vs agentic choice | ✅ |
| AI-generated code traceable, secure, testable, production-ready | Clean code principles; no security tooling named | 🟡 |
| Backend/fullstack (TypeScript, Python, Java, Go) | Python ✅, React beginner; TS/Java/Go ❌ | 🟡 |
| Git, CI/CD, automated tests, code reviews | Git, GitLab CI/CD; code reviews not stated | 🟡 |
| Coding agents as fixed part of daily work | Claude Code workflows at Kniit | ✅ |
| APIs, data models, auth, distributed systems, LLM concepts (RAG, tool use, orchestration) | APIs, Postgres/Mongo/Neo4j data models, RAG, MCP tools, LangGraph ✅; auth/distributed ❌ | 🟡 |

## Gaps and honest framing
1. **TypeScript/Java/Go**: Python only; say so.
2. **Observability, auth, security tooling**: not in profile; planned project adds Langfuse traces + SAST (unbuilt → not proof).
3. **German**: client projects in DACH; B1 should be mentioned in letter.

## Red flags
- Consultancy model ("Kundenreisen von deinem Zuhause"): travel likely; user is fully willing to travel.

## Company research
Only job postings are public on this platform: Senacor (offices Berlin, Bonn, Frankfurt, Hamburg, München, Nürnberg, Wien, Zürich) is building a greenfield process platform (core systems + automation layers) and also hires a Platform & Automation Architect in Hamburg. Sources: https://www.whatjobs.com/company/senacor/jobs , https://en.devjobs.de/job/bdb391a4e998a04de516f368f531cf6d . Hook: greenfield platform built with an AI-native SDLC from day one.

## Projects on the CV
- Spec-Driven Coding Agent Harness (planned, reused). Brief: project-brief-spec-driven-agent-harness.md → build-first.
