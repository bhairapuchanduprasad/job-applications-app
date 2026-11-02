# Project brief: BOM Emission Factor Matcher (Order Inbox Agent variant)
Repo slug: bom-emission-matcher. Status: planned. For: carbmee FDE North America (2026-11-03).

## Goal
Match item-level purchase and BOM data from a mock ERP export to emission factors, check data quality, and show an executive-level answer: where the emissions sit and which suppliers to work on.

## Why for this JD
Proves Python + SQL data modelling over transactional data and bills of materials, AI matching of items to emission factors, data quality checks, an "implementation" flow from customer export to configured model, and C-level summary.

## Scope (1–2 days)
- Synthetic SAP-style exports: material master, BOMs (3 levels), purchase orders (2,000 lines, 150 suppliers), with messy descriptions and units.
- Postgres data model: item, bom_edge, purchase_line, supplier, emission_factor, match (with method + confidence).
- Public emission factors (e.g. EXIOBASE/USEEIO or UK DEFRA set) loaded as reference.
- Matching cascade: exact code → rules on material group → embedding similarity → LLM judge (LiteLLM) only for ambiguous; unit normalisation.
- Data quality checks: missing weights, unit conflicts, orphan BOM nodes; report.
- Labelled 200-item set: match accuracy per method; coverage %.
- Streamlit: product footprint roll-up through the BOM, top suppliers by emissions, 1-page executive summary.

## Milestones
1. Data + model. 2. Matching cascade. 3. DQ checks. 4. Eval. 5. Dashboard + README.

## Demo
Load export → run matching → dashboard showing footprint per product and the top 10 reduction levers.

## CV bullets it must live up to
- Python + SQL data model over synthetic ERP exports (material master, multi-level bills of materials, purchase lines) that matches items to public emission factors through exact, rule, embedding and LLM steps, with data quality checks and match accuracy on a labelled set.
- Streamlit view rolling footprints up through the BOM with an executive summary of the largest supplier levers.
