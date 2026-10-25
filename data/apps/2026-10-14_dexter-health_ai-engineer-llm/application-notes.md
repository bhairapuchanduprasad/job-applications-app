# Application notes: dexter health, AI Engineer (LLM) - Remote

## Likely interview questions

**1. "Tell us about an AI feature that was failing and how you debugged it."**
Kniit extraction pipeline at 33% precision / 45% recall. Built evaluation against SAP-derived ground truth first, so every change could be measured. Split the work into specialised LangGraph agents (entity extraction, relationship analysis, consolidation, reflection) running in parallel, and checked failures by category. Ended at 93% / 90%. Prepare 1–2 concrete failure examples (what the model got wrong, which change fixed it) before the call; the profile has no detailed story yet.

**2. "How would you design structured output + validation + fallback for dictated care notes?"**
Schema per entry type (vitals, wound, measure, report); plausibility checks on values; grounding check that every value appears in the transcript; on failure retry once with the validation errors, then fall back to a second model; anything still uncertain is flagged for the nurse rather than guessed. Human review stays the final gate, like Expert Interface at Kniit. Measure with a labelled test set: field-level precision/recall, valid-output rate, latency. (If Care Note Structurer is built by then, show it.)

**3. "When would you use a self-hosted open-source model instead of a commercial API?"**
Control over data (health data, GDPR, EU AI Act, no-training promise), predictable cost at volume, latency if the model can be small. Commercial APIs when quality gap is large or volume low. Kniit example of the same judgment one level further: for a high-volume stream, deterministic code beat any LLM and cut a projected $200,000 LLM budget to near zero. Be honest: my self-hosted experience is QLoRA fine-tuning of Open Llama 3B; no production model serving yet.

Also prepare: "Why did you leave Kniit?" → public line from profile. "How do you use Claude Code?" → custom skills, agentic workflows, MCP service for the knowledge graph, this job-application pipeline itself is an example.

## Form fields

- **Why dexter health?** You already have the hard part working in the field: a nurse dictates, dexter drafts a structured entry, the nurse checks it, and it lands in the care software the home already uses, with a measured 20 minutes saved per carer per day. I have spent the last year making LLM extraction reliable enough that domain experts approve rather than rewrite it, and I want to apply that where the time saved goes back to residents.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000 if a range is allowed). Must be above the EU Blue Card threshold.
- **Notice period / start date:** Available from 15 November 2026.
- **Work authorisation:** EU Blue Card (Germany); no sponsorship needed for a qualifying role.
- **Location / remote:** Essen, NRW; fully remote fine, can travel to Köln for on-sites (about 1 hour away).
- **German level:** B1, improving.
- **English:** Business fluent.
