# Application notes: Comena (YC S25), Forward Deployed Engineer

## Before submitting
- Build `order-inbox-agent` (brief in this folder), or remove the Projects section. Building it is also the best prep for their take-home: same problem.
- Only 2 applicants so far: apply today.

## Founder call (30 min): what to get across
- You've been the only engineer at an early-stage start-up: you own things end to end.
- You turn messy documents into records checked against SAP data (Kniit P/R 33%/45% → 93%/90%).
- You enjoy customer work (Covestro AI consulting internship; Expert Interface for domain experts).
- Honest on TypeScript/Django; show the project if built.
- Ask: how do they onboard a new distributor today? Which ERPs (SAP Business One, Microsoft Dynamics, proAlpha…)? What does a typical week look like for the FDE? On-site days?

## Likely interview / take-home topics
1. **"A customer's orders use their own part numbers. How do you match them to our SKUs?"**
   Cascade: exact match → customer-specific mapping table (learned from confirmed orders) → fuzzy on part numbers/descriptions → embeddings; confidence threshold; human review below it; feed confirmations back into the mapping.
2. **"How do you know the agent is good enough to push orders without review?"**
   Labelled orders per customer, line-level accuracy, start with 100% review, then auto-push only above a confidence level that has proven accurate; monitor overrides.
3. **"Tell us about working with a non-technical stakeholder."**
   Covestro consulting internship; Kniit SAP domain experts and Expert Interface.

## Form answers
- **Why Comena:** AI agents that take orders from inbox to ERP for industrial distributors; I've built agents that turn messy documents into data checked against SAP, and I want the forward-deployed mix of building and working with customers.
- **Salary expectation:** €85,000 (posted range €80–150k; don't anchor at your old €60–75k).
- **Earliest start / notice:** 16 November 2026 (current role ends 13 November 2026).
- **Location:** Munich, on-site.
- **Work permit:** EU Blue Card.
- **Languages:** English business fluent; German B1.
