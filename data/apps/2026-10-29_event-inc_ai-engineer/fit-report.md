# Fit report: Event Inc Group, AI Engineer (Mensch), Hamburg

**Fit score: 62/100.** Strong: daily AI-coding-agent work with a critical eye (Claude Code, custom skills, agentic coding workflows at Kniit), clean code, API and cloud integration (FastAPI, Postman, AWS CDK, Azure), working with non-technical stakeholders (CTO, SAP domain experts, Covestro business users), getting productive in a new domain fast. Gaps: "mehrere Jahre als Software Engineer" in product teams (~3 years total, AI-focused), production reliability practices (monitoring, feature flags, rollbacks: not in profile), secrets/access management, multi-repo refactoring in unfamiliar languages (Python + some React only).

Found by job-scout (LinkedIn 4482512956; English twin 4482523366 "AI-Native Software Engineer (Human)" skipped as duplicate). Posting is German but "Sehr gute Englischkenntnisse; Deutsch ist ein Plus" → English documents (CLAUDE.md rule 3). Contact: Hellen, Talent Acquisition Manager.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Spec-first features, AI implements, critical review | Claude Code + skills at Kniit; ground-truth checks before trusting output | ✅ |
| Quickly productive in unfamiliar codebases/languages | energy regulation domain at Kniit; React beginner | 🟡 |
| External APIs, cloud (AWS/GCP/Azure), SaaS, secrets | FastAPI, AWS CDK (Lambda, SQS, DynamoDB), Azure; no secrets mgmt evidence | 🟡 |
| Reliability: monitoring, debugging, feature flags, rollbacks | evaluation pipelines; no production ops | ❌ |
| Product/Design/non-technical stakeholders | CTO, SAP experts, chemists, Covestro business users | ✅ |
| Share prompts/workflows, team AI fluency | custom Claude Code skills (internal) | 🟡 |
| Several years SE, clean testable code | ~3 yrs, clean code principles, Postman API tests | 🟡 |
| English excellent, German plus | English business fluent, German B1 | ✅ |

## Gaps and honest framing
1. **Production reliability:** no on-call/monitoring/feature-flag experience; project adds CI gates and traces; say it in the letter.
2. **Breadth of languages:** Python first; React beginner.

## Red flags
- Benefits modest (€300 learning budget); salary not stated.

## Company hooks
1. Founded 2014, Hamburg; largest event-location platform in the German-speaking region; group formed 2021 with smart and more; 4 acquisitions in 3 years incl. HONEST (2023 press release, blog.eventinc.de; startbase.de).
2. Repositioning as an AI-first platform for events, meetings and hotels (Event Inc job posting on arbeitnow.com).
3. AI agents "fester Bestandteil unseres Engineering-Alltags" (JD).

## Projects on the CV
- **Spec-Driven Coding Agent Harness** (planned, reused; Event Inc variant: spec with edge cases → acceptance tests → Claude Code implementation under hooks that block secrets; adds a feature flag + rollback step in the GitHub Actions deploy and structured logging). Brief: `_work/project-brief-spec-driven-agent-harness.md`. Status: build-first.
