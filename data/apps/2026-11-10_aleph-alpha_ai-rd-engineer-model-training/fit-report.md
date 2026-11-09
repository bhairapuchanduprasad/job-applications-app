# Fit report: Aleph Alpha, AI R&D Engineer - Model Training (Berlin)

**Fit score: 55/100.** Engineering-minded, junior-friendly role in an LLM training team; Python, Kubernetes, CI, clean code and eval work match, but there is no pre-training / cluster-scheduling / RL-infrastructure experience.

| Requirement | Evidence | |
|---|---|---|
| Dive into a codebase, change it, leave it better tested and clearer | Kniit: sole owner of a multi-component pipeline, clean-code practice; Covestro RAG eval codebase | 🟡 |
| Low coupling / high cohesion, incremental refactoring | Kniit microservices, separate extraction strategies behind one pipeline; clean code principles | 🟡 |
| TDD | Not in profile as TDD (API testing with Postman only) | ❌ |
| Trunk-based development | Not in profile | ❌ |
| Continuous integration | GitLab CI/CD (Covestro) | ✅ |
| Domain Driven Design | Not in profile | ❌ |
| Python | Main language, 3 years | ✅ |
| Kubernetes | Listed in Kniit tech stack | 🟡 |
| Rust | None | ❌ |
| Model training pipelines / cluster scheduling | PyTorch, QLoRA/LoRA fine-tuning of open LLMs (Meme-me project, retrieval fine-tuning at Covestro); no pre-training or scheduler work | 🟡 |
| Large-scale code execution for RL | None | ❌ |
| Evaluation codebase, inference throughput | RAG evaluation framework (RAGAS, PytrecEval), 1M+ chunk embedding benchmarks | 🟡 |
| Pair/mob programming, collaboration | Worked with CTO, SAP experts, chemists; not explicitly pair programming | 🟡 |

## Gaps and framing
- TDD, trunk-based development, DDD, Rust, RL infrastructure, cluster scheduling: real gaps, not claimed on the CV. The cover letter says plainly that the work is application-side and offers testing/refactoring habits from the pipeline work.
- Foundation-model pre-training: no experience; frame via LoRA/QLoRA fine-tuning and evaluation work only.
- Salary/seniority: posting welcomes every career stage.

## Red flags
- Requires on-site 2 days a week, plus a few days in Heidelberg about every second month if in Berlin; most of the team is in Heidelberg.
- No German-language requirement (the posting only says models "understand German").
- Posting says "AI R&D Engineer" but is mostly software engineering for research-heavy teams.

## Hooks (from the posting only; no web research was done in this unattended run)
- Kolibri-1, their recently released foundation model, trained with the pipeline this team maintains.
- Team practices: Extreme Programming, trunk-based development, mob programming.
- Focus on German-capable, EU-regulation-compliant models for finance, manufacturing, public administration.
