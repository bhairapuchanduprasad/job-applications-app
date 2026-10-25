# Application notes: Accenture DACH, Junior Applied AI Engineer

## Before submitting (checklist)
- [ ] Build `llm-gateway` (see `_work/project-brief-llm-gateway.md`): streaming, fallback, budgets, cost/latency logging, React + TypeScript KPI dashboard, Claude-Code-generated tests in CI. If anything gets cut, edit the Projects bullets in `_work/cv.tex` and rebuild.
- [ ] Mark it `built` in `profile/master-profile.md`.
- [ ] Confirm travel: the JD requires occasional business travel. If you're fine with it, add "I am happy to travel to client sites when projects need it." to the letter's logistics line.
- [ ] If submitting after 13 Nov 2026: Kniit dates → "November 2025 -- November 2026".
- [ ] Apply quickly (100+ applicants in 2 days). Applications are handled off LinkedIn (Accenture careers site).

## Likely interview questions
1. **"Show me how you use AI coding assistants in your day-to-day work. Give a concrete example where the AI output was wrong and how you caught it."**
   Prepare one real story (profile TODO): a Claude Code skill you wrote, and a piece of generated code you fixed or rejected.
2. **"How do you manage tokens, latency and cost when calling LLM APIs in production?"**
   Kniit: deterministic pipeline instead of an LLM for the high-volume stream ($200k projected → near zero); parallel agents; then your LLM Gateway (budgets, fallback, per-request cost logging).
3. **"How do you decide an AI output is production-ready?"**
   Ground-truth evaluation: precision/recall 33/45% → 93/90% vs SAP-derived truth; RAGAS + PytrecEval at Covestro; reflection agent; domain-expert approval in Expert Interface.

## Form answers
- **Why Accenture:** "Accenture works with Anthropic through a dedicated business group, and tens of thousands of its developers already build with Claude Code. That is how I work today, and the path toward forward deployed engineering on client projects is exactly where I want to grow."
- **Why are you leaving Kniit?** "Kniit is an early-stage startup that restructured around a senior SAP-focused hire before its funding round; my position ended after I had built and handed over its knowledge-extraction pipeline end-to-end."
- **Salary expectation:** €70,000 gross/year (range €60–75k). Note: junior band may be lower; decide your floor before the call.
- **Earliest start:** 15.11.2026. **Notice period:** none after 13.11.2026.
- **Work permit:** EU Blue Card; no sponsorship needed (employer change must be reported to the Ausländerbehörde).
- **Location:** Kronberg hybrid; you're in Essen and open to relocating.
