# Interview questions
1. How do you load resent or changed files so no record is counted twice? (Answer: idempotent upserts on a business key, load batch IDs; Kniit pipeline reruns; honest: dbt incremental models still to learn.)
2. How do you test that a model matches the source? (Kniit: compared extraction output with SAP-derived ground truth, precision/recall 33/45 to 93/90; row counts and sums as reconciliation checks.)
3. Walk through a SQL query with a window function. (Prepare one example.)
# Form fields
- Why Grainset: they trace reported figures back to source records, SAP exports and shop data, matches my SAP-ground-truth work at Kniit.
- Salary: EUR 55,000 gross/year. Notice: free from 15 Nov 2026.
