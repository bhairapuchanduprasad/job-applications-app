# Fit report: Atira, AI Engineer, Munich

**Fit score: 72/100.** Strong match on the core: agent harnesses/orchestration (LangGraph multi-agent at Kniit), evals against ground truth, deterministic guardrails vs. LLM (the $200k deterministic pipeline), ontology/context layer (Neo4j knowledge graph + MCP), heavy Claude Code use with skills. Gaps: scale (millions of LLM calls/day), sandboxing, TypeScript, "strong technical university" signal, multi-modal CAD/drawings.

Language: English posting, "German is not required" → English CV + cover letter. Found by job-scout (LinkedIn 4483596232). Atira also posted a Forward Deployed Engineer role (prepared separately, German needed) and a Software Engineer / Deployment Strategist role (skipped).

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Build agent runtime, harnesses, orchestration layer | Kniit: LangGraph harness with 4 parallel agents incl. reflection; Covestro: LangGraph router | ✅ |
| Quality & evals | Kniit evals vs SAP ground truth, P/R 33/45 → 93/90; thesis RAGAS/PytrecEval | ✅ |
| Fuse deterministic guardrails with flexible harnesses | Kniit deterministic pipeline replacing LLM calls ($200k → ~0) | ✅ |
| Ontology / context layer, tools & skills | Neo4j knowledge graph, MCP tool service, Claude Code custom skills | ✅ |
| Multi-modal, data-heavy inbounds (1000s pages, Excel, drawings, CAD, ERP tables) | Long regulatory/technical docs; no CAD/drawings | 🟡 |
| Scale: millions of concurrent LLM requests, sandboxes, observability | Docker/K8s/Azure/AWS; no high-scale LLM infra, no sandboxing | ❌ |
| Strong Python or TypeScript | Python strong; TypeScript only in planned projects | 🟡 |
| Serious AI-assisted development (Claude Code etc.) | Claude Code daily, custom skills, MCP integration | ✅ |
| Ownership evidence (company, OSS, side project, owned outcome) | Sole developer at Kniit reporting to CTO | ✅ |
| CS/AI degree from strong technical university | MSc AI, TH Würzburg-Schweinfurt (University of Applied Sciences) | 🟡 |
| English | Business fluent | ✅ |

## Gaps and honest framing
1. **Scale (millions of calls/day, sandboxing, cost/latency observability):** say it openly (done in the letter) and point to cost thinking (deterministic pipeline). Agent Eval Harness project adds OpenTelemetry/Phoenix tracing and async load testing on paper; build it first.
2. **TypeScript:** Python is the main language; Order Inbox Agent adds a TypeScript review screen. Don't claim more.
3. **"Strong technical university":** can't change; lean on what was built ("where you trained matters less than what you've built").
4. **Multi-modal (drawings/CAD):** none; Order Inbox Agent covers email/PDF/Excel → ERP write-back.

## Projects on the CV (both `planned` → build-first)
- **Agent Eval Harness** (reused, brief: applications/2026-10-17_jobgether_ai-evaluation-engineer/_work/project-brief-agent-eval-harness.md; Atira notes in `project-brief-agent-eval-harness.md` here).
- **Order Inbox Agent** (reused, brief: applications/2026-10-22_comena_forward-deployed-engineer/_work/project-brief-order-inbox-agent.md; Atira notes in `project-brief-order-inbox-agent.md` here).
Both briefs already exist; one build serves several applications.

## Red flags
- Very high bar wording ("gone further than most", "strong technical university", millions of calls/day). Seed-stage (12 people): intensity, equity-heavy pay.
- Expect a deep technical interview on agent failure modes and trade-offs ("there is no free lunch").

## Company hooks (research 2026-10-27)
1. Sept 2026: $15M seed led by Accel (plus $2.5M pre-seed, ~$17.5M total); UVC Partners, Fortino, BOOOM; angels incl. Celonis co-CEO Bastian Nominacher and Whirlpool's Marc Bitzer ([tech.eu](https://tech.eu/2026/09/03/atira-raises-175m-to-bring-ai-orchestration-to-industrial-sales/), [Fortune](https://fortune.com/2026/09/03/exclusive-german-ai-startup-atira-raises-17-5-million-to-unclog-the-paperwork-bottleneck-in-industrial-dealmaking/)).
2. Founders: Florian Diegruber (CEO, ex-Palantir), August DuMont Schütte (CTO, ex-Google); founded Munich, Nov 2024 ([Munich Startup](https://www.munich-startup.de/en/news/ai-company-atira-raises-13-million-euros)).
3. 15+ customers since commercial launch in 2025; orchestration layer between CRM and ERP for built-to-order manufacturers (tech.eu).
4. From the JD: team of 12; agents handle RFQ requirement extraction, documentation, configuration recommendations, ERP write-backs.
