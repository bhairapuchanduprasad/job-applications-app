# Project brief: Next-Best-Offer Engine (insurance customers)
Goal: small end-to-end analytical-CRM demo: segmentation + next-best-offer rules + scoring model on a synthetic insurance portfolio.
Why for this JD: proves SQL, Zielgruppensegmentierung, Next-Best-Offer, Automatisierung, Handlungsempfehlungen (R+V Data Scientist analytisches CRM).
Scope (1-2 days): synthetic data generator (customers, contracts, claims, contacts) into PostgreSQL; SQL views for customer features and segments; rule set (e.g. product-gap rules); scikit-learn scoring model (logistic regression / gradient boosting) vs rules-only baseline; Streamlit dashboard; data quality checks.
Stack: Python, SQL (PostgreSQL), pandas, scikit-learn, Streamlit, Docker Compose.
Architecture: generator -> Postgres -> SQL views -> Python features -> rules + model -> offer table -> Streamlit.
Milestones: 1 data + schema, 2 segments in SQL, 3 rules + model + comparison, 4 dashboard, 5 README.
README outline: problem, data (synthetic), segments, rules, model vs baseline, how to run.
Demo idea: dashboard showing segment sizes and top offer per customer with reasons.
CV bullets it must live up to: SQL segmentation and customer features in PostgreSQL; rule set plus Scikit-Learn scoring model compared to rule-only baseline; Streamlit dashboard with recommendations; data quality checks and automated run in Python.
