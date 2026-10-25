# Application notes: SNOCKS, Junior AI Engineer

## Before submitting
- Build `shop-support-agent` (brief in this folder), or remove the Projects section from the CV.
- Posted 2 hours before /apply ran, 50 applicants already: submit quickly.

## Likely interview questions
1. **"Tell us about an AI use case you took from prototype to production and how you measured it."**
   Kniit pipeline: first prototype → LangGraph multi-agent extraction in production; tested against SAP-derived ground truth; precision/recall 33%/45% → 93%/90%. Then the counter-example: for the high-volume stream an LLM wasn't worth it, so a deterministic pipeline took a projected $200k LLM budget to near zero. Shows judgment about where AI hits its limits (they ask for exactly that).
2. **"We have Shopify, Zendesk, Klaviyo and BigQuery. How would you start automating customer service?"**
   Start with ticket data in the warehouse: which reasons are most common (order status, returns)? Pick the top one, give an agent read-only tools over order data (MCP), draft replies with human approval, measure accuracy, cost per ticket and latency on a labelled set, then widen. (If built: walk through Shop Support Agent.)
3. **"How do you explain to a business team that the AI isn't good enough yet?"**
   Show numbers against ground truth, not opinions; Kniit: experts saw P/R per document type; Covestro: chemists' ground truth for RAG answers. Offer a human-in-the-loop version first.

Also prepare: BigQuery basics (datasets, partitioned tables, cost per query), Shopify Admin API (orders, fulfillments), why you left Kniit (public line in profile).

## Form answers
- **Why SNOCKS:** You've grown from one brand to four (OCEANSAPART, femtis, Les Lunes) on one company setup; internal automation across customer service, supply chain and reporting is where my experience in taking LLM systems to production and measuring them is directly useful. I also like the "whole setup, not single projects" view in the ad.
- **Salary expectation:** €70,000 (profile default; junior title may mean a lower offer, decide your floor before the call).
- **Earliest start / notice:** 15 November 2026 (current role ends 13 November 2026).
- **Location:** Essen; remote, or relocate to Mannheim/Hamburg/Berlin.
- **Work permit:** EU Blue Card, no sponsorship needed.
- **German:** B1. **English:** business fluent (C1+).
