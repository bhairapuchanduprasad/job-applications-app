# Application notes: Bestandsfaktor, Founding Software Engineer

Status: build-first. Build `client-occasion-engine` (brief in this folder) and `spec-driven-agent-harness` (brief: applications/2026-10-17_bcg-platinion_ai-associate/_work/project-brief-spec-driven-agent-harness.md) before submitting, or remove them from the CV.

## Likely interview questions
1. **"How would you design the core of Bestandsfaktor: data in, trigger, action out, learning loop?"**
   Start from the data: a sync layer per broker system that lands clients and contracts in one schema (idempotent, cursor-based). Then deterministic, configurable trigger rules first (cheap, explainable, testable), prioritisation and a per-client cool-down so nobody gets three messages in a week, LLM only where it adds value (personalised text, messy data), every trigger and outcome as an event so you can measure each rule. Tie it to Kniit: I moved a high-volume source from LLM calls to a deterministic pipeline and saved a projected $200,000; same principle.
2. **"You'd be the only engineer and lead freelancers. How do you keep quality up?"**
   Honest: I haven't led freelancers yet. What I would do is what I did for myself at Kniit: ground-truth tests that decide whether a change is better (33%/45% → 93%/90% precision/recall came from that), clean code conventions, CI on every change, Claude Code skills that encode the conventions so humans and agents work the same way. Small, reviewable PRs; I review every external PR.
3. **"Why a 50,000-customer insurance system after an energy-sector knowledge graph?"**
   Both are the same kind of problem: messy domain data turned into reliable, automated decisions that experts trust. At Kniit the experts were SAP consultants approving graph changes; here it's brokers trusting which client gets which message. And I've already done the start-up setup: direct line to the founder, no one to hand work to.

Also prepare: German. Be upfront: B1, technical work in English, improving; ask how much German the role needs with brokers.

## Form answers
- **Why Bestandsfaktor?** It is a systems problem with real leverage: deciding which action makes sense for which client and when, then learning from the outcome. With more than 50,000 clients in the system after a few weeks, the architecture decisions made now matter, and I want to own them, as I did as sole developer at Kniit.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000). Must meet the EU Blue Card threshold.
- **Notice period / earliest start:** 15 November 2026.
- **Location:** Remote; will be based in Cologne. EU Blue Card holder, no sponsorship needed.
- **Languages:** English (business fluent), German (B1).
- **Why are you leaving Kniit? (only if asked):** "Kniit is an early-stage startup that restructured around a senior SAP-focused hire before its funding round; my position ended after I had built and handed over its knowledge-extraction pipeline end-to-end."
