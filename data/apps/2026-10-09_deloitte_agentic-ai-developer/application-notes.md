# Application notes: Deloitte aiStudio, Agentic AI Developer

## Before submitting (checklist)
- [ ] Build `contract-risk-agents` (see `_work/project-brief-contract-risk-agents.md`); repo public, README + demo GIF.
- [ ] Every part named on the CV exists: Strands, Amazon Bedrock, A2A, MCP, RBAC, OpenTelemetry, JS UI, GitLab CI. If you used a fallback (Anthropic API, GitHub Actions), update the Projects bullet in `_work/cv.tex`.
- [ ] After building: add a skills line "Agent Frameworks & Protocols: Strands Agents, A2A, OpenTelemetry (tracing), RBAC" and update the last About Me sentence to mention the project (reviewer items 8 + 10); rebuild, keep 2 pages.
- [ ] If submitting after 13 Nov 2026: change Kniit dates to "November 2025 -- November 2026".
- [ ] Upload: CV (English) + Hochschulzeugnisse (MSc, BTech) + Arbeitszeugnisse (Covestro; Kniit once issued). Abitur equivalent: Indian Class 12 certificate. Cover letter is optional.
- [ ] Ask Kniit for a qualifiziertes Arbeitszeugnis now (you are entitled to one).

## Likely interview questions
1. **"Walk me through your multi-agent extraction system. Why parallel agents, and how did you measure 93/90?"**
   Answer with: architecture (4 agents, reflection loop), ground truth from SAP systems, what moved precision most, and when you chose the deterministic pipeline instead ($200k LLM budget → near zero).
2. **"How would you make an agent system production-ready and secure for a client?"** (CI/CD, RBAC, InfoSec)
   Answer with: Covestro CI/CD + CDK deployment, then your Contract Risk Agents project (RBAC on MCP tools, OpenTelemetry tracing, tests in CI). Be honest that formal InfoSec work is new to you.
3. **"Our clients work in German. How do you handle that?"**
   Honest answer: English is your working language (business fluent), German currently B1; you can work on German documents technically (your Kniit pipeline processed German energy-sector documents), and say what you're doing to improve if anything (TODO).

## Form answers
- **Why Deloitte / aiStudio:** "You build agentic AI for clients in compliance, contract management and risk, and those domains live in large, complex documents. That is exactly what I've done at Kniit: turning regulatory and technical documents into structured knowledge with multi-agent systems, MCP and Claude Code. I want to do this across many clients and hyperscalers, which a studio inside Deloitte offers."
- **Why are you leaving Kniit?** "Kniit is an early-stage startup that restructured around a senior SAP-focused hire before its funding round; my position ended after I had built and handed over its knowledge-extraction pipeline end-to-end."
- **Salary expectation (Gehaltsvorstellung):** €70,000 gross/year (range €60–75k).
- **Earliest start (frühester Eintrittstermin):** 15.11.2026.
- **Notice period:** none after 13.11.2026.
- **Work permit:** Blaue Karte EU; no sponsorship needed (the employer change has to be reported to the Ausländerbehörde).
- **Preferred location:** open to all listed locations.

## Note
CV and cover letter are in English (your choice for this application). German versions are kept as `_work/cv.de.tex` and `_work/cover-letter.de.tex`.
