# Application notes: SAP SE, AI Engineer – Development Expert

## Before submitting
- Build `meter-read-plausibility-agent` (brief in this folder), or remove the Projects section from the CV.
- Senior role (T4). If SAP screens you out on years, ask the recruiter (Nola O'Connor) whether the Industry AI ENR unit has a T2/T3 AI engineer opening; your energy + agentic profile fits that unit well.

## Likely interview questions
1. **"Walk us through the architecture of your Kniit pipeline. What would you change at 10x volume?"**
   Ingestion → chunking → parallel LangGraph agents (entity, relationship, consolidation, reflection) → knowledge graph (Neo4j) → MCP retrieval + Expert Interface for approval. At 10x: rules or deterministic extraction first, LLM only where needed (the $200k example), batch and cache LLM calls, queue-based workers (you used SQS + Lambda at Covestro), per-document-type evaluation.
2. **"How do you make sure agent output is correct enough for utility customers?"**
   Ground truth from SAP systems; precision/recall per document type (33%/45% → 93%/90%); reflection agent; human approval in Expert Interface; regression tests on a labelled set; audit trail.
3. **"You haven't led a team. How would you guide developers on architecture?"**
   Be honest. Point to working directly with the CTO and SAP domain experts, writing Claude Code skills that encode team conventions (a form of setting standards), and that you'd start by pairing and design reviews. Ask what support the team has.

Also prepare: SAP BTP basics (AI Core, Generative AI Hub, Joule Studio), meter-to-cash process, MaKo / market communication and the smart meter gateway at concept level, why you left Kniit (public line in profile).

## Form answers
- **Why SAP:** Joule for utilities is grounded in the SAP Knowledge Graph and business data, and SAP is building agents for meter-to-cash steps. I've built agents for the German energy sector that are grounded in a knowledge graph and checked against SAP data, so I can contribute from day one on the AI side.
- **Salary expectation:** the posting shows €94.2k–171.8k. If asked, say €95,000 (bottom of their range; your profile range €60–75k is below it, don't anchor low here).
- **Earliest start / notice:** 15 November 2026 (current role ends 13 November 2026).
- **Location:** Essen, will relocate to Munich/Garching; hybrid fine; travel 0–10% fine.
- **Work permit:** EU Blue Card, no sponsorship needed.
- **Languages:** English business fluent; German B1.
