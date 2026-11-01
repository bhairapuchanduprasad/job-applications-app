# Fit report: Almedia, AI Full Stack Engineer, Berlin

**Fit score: 70/100.** Strong match on the AI side: complex agentic systems (Kniit multi-agent LangGraph pipeline, Covestro agentic app), AI API integration (LiteLLM, LangChain, MCP), Python production backends (FastAPI, Python microservices), working with business stakeholders on their workflows (Covestro AI consulting internship, Kniit SAP domain experts, chemists). Full-stack is real but frontend is React at beginner level; no Node.js or TypeScript in a job. No marketing / user-acquisition domain experience.

Found by job-scout (LinkedIn 4365162691). English posting, no German requirement → English documents. Salary range in the posting: €60K – €130K. Seniority "Not Applicable"; they say they evaluate all skill levels.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Communicate clearly with non-technical stakeholders | Covestro AI Consulting Intern: worked with business stakeholders on decision workflows; Kniit: SAP domain experts, reported to CTO; Streamlit dashboard for chemists | ✅ |
| Experience building complex agentic systems | Kniit: parallel LangGraph agents (extraction, relationship analysis, consolidation, reflection), P/R 33/45 → 93/90; Covestro agentic routing app | ✅ |
| Integrating and working with AI APIs | LiteLLM, LangChain, Hugging Face, MCP service integrated into Claude Code | ✅ |
| Strong coding skills, engineering fundamentals | Sole developer of the Kniit pipeline end-to-end; clean code, Docker, CI/CD | ✅ |
| Full stack: front end, back end, databases | React frontends (Expert Interface, Covestro), FastAPI/Python microservices, Postgres, MongoDB, Neo4j, vector DBs. React self-rated beginner | 🟡 |
| Good prompting, uses current AI tools effectively | Prompt engineering at Kniit; Claude Code with custom skills and agentic coding workflows daily | ✅ |
| Production experience with Node.js or Python | Python in production (Kniit, Covestro) | ✅ |
| Durable AI workflows that adapt as the LLM landscape evolves | LiteLLM provider abstraction; deterministic pipeline replacing LLM calls where cheaper ($200k → near zero); ground-truth evals | ✅ |
| Make sense of fragmented data across systems | Kniit: regulatory/technical documents + SAP-derived ground truth into a knowledge graph; second high-volume source stream | ✅ |
| Nice: TypeScript | none in a job; planned project only | ❌ |
| Nice: partnering with marketing / UA / ops teams | consulting with business stakeholders at Covestro, but not marketing/UA | 🟡 |

## Gaps and honest framing
1. **TypeScript / Node.js:** not used professionally. Python satisfies the must-have ("Node.js or Python"). The planned project adds a TypeScript MCP server + React/TypeScript UI. Don't claim more.
2. **Frontend depth:** React used for two internal web apps but self-rated beginner; keep "(beginner)" in skills, describe the apps factually.
3. **Marketing / user acquisition domain:** none. Frame as: learned the energy-sector and chemistry domains quickly by sitting with the experts.

## Red flags
- Wide salary band (€60K – €130K) and "push harder" / "accelerate" language: expect a high-pace culture; ask about working hours and on-call in interviews.
- Same company also advertises "AI Engineer (Data)" and "Junior Engineer (AI)" roles (aggregators, 2026); worth checking whether those are open too.
- An earlier Almedia posting (Product Engineer, Client Platform, 2026-10-28) was skipped by the scout as TypeScript/NestJS product engineering.

## Company hooks
1. Bootstrapped since its founding in Berlin in 2020 and profitable from day one; aiming to become "Germany's second bootstrapped unicorn"; FT1000 #3 fastest-growing company in Europe 2025 (JD).
2. Flagship product Freecash: users earn rewards for completing offers, games and surveys; JD cites 95 million users (JD; Techleap: https://finder.techleap.nl/news/note/almedia-the-meteoric-growth-of-a-teenager-s-advertising-startup).
3. Acquired the German cashback platform zave.it in August 2025, moving into retail and e-commerce (Startbase: https://www.startbase.com/news/almedia-uebernimmt-zave-it/).
4. Reportedly over €100M annual revenue with no outside investors (Techleap, secondary source: don't cite the number in writing).
5. Other postings mention company-paid AI tooling built into every team's workflow (Arbeitnow listing of AI Engineer (Data): https://www.arbeitnow.com/jobs/companies/almedia/ai-engineer-data-berlin-457327).

## Projects on the CV
- **Ops MCP Server** (planned, reused; Almedia variant "Growth Ops Assistant": TypeScript (Node.js) MCP server with Zod-typed tools over synthetic campaign/offer data in Postgres, provider-agnostic model layer, Slack bot for a UA/marketing team, React + TypeScript review screen, eval set in GitHub Actions). Brief: `_work/project-brief-ops-mcp-server.md`. Status: build-first.
