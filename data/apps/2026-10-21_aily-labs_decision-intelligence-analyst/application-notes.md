# Application notes: Aily Labs, Decision Intelligence Analyst

## Before submitting
- Nothing to build: both projects on the CV are real repos.
- Ask early: salary range (analyst level), remote from Germany vs Munich office.

## Likely interview questions
1. **"A client's model outputs suddenly look worse. What do you do?"**
   Check data first (new source, missing fields, schema change), then compare against a labelled sample / ground truth, look at which segment degraded, fix and re-validate, tell the delivery lead and client what changed. Kniit example: per-iteration P/R against SAP ground truth (33%/45% → 93%/90%).
2. **"How do you adapt a data model to a new client's business process?"**
   Start with the decisions the users make and the data behind them (your Covestro consulting internship: stakeholders' decision-making workflows); map entities and relationships (Kniit knowledge-graph data model); load a sample, validate with domain experts (Expert Interface), then scale.
3. **"Tell us about a time you fine-tuned or optimized a model."**
   QLoRA fine-tuning of Open Llama 3B (repo); retrieval fine-tuning and embedding benchmark on 1M+ chunks in the thesis; Kniit multi-agent optimization cycles.

Prepare: a few SQL queries you'd write to check data completeness (null rates, duplicates, joins against reference tables); how you'd define "tenant health" (data freshness, completeness, output acceptance rate, model accuracy on a labelled sample, usage).

## Form answers
- **Why Aily Labs:** AI for business decisions in pharma, life sciences, supply chain and manufacturing; my work has been exactly this: running AI models on industrial data and making their outputs trustworthy for domain experts.
- **Salary expectation:** €60,000–65,000 (analyst title; profile range €60–75k); never below the Blue Card minimum (€45,934.20).
- **Earliest start / notice:** 15 November 2026 (current role ends 13 November 2026).
- **Location:** Munich office or remote from Germany.
- **Work permit:** EU Blue Card.
- **Languages:** English business fluent; German B1.
