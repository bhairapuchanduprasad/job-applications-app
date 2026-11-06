# Project brief: Payment Fraud Detection Pipeline, LBBW/SüdLeasing variant

Repo slug: `payment-fraud-detection` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-11-05_r-v-versicherung_data-scientist-fraud-management/_work/project-brief-payment-fraud-detection.md). Used on the LBBW Data Science Analyst CV (2026-11-06). Time box 1-2 days with Claude Code.

## Goal and scope
Risk scoring on public synthetic PaySim payments: SQL features (velocity, rolling amounts, counterparty stats), XGBoost vs Isolation Forest vs rule baseline at a fixed alert budget, SHAP reasons per alert, business-case view (prevented loss vs investigation cost). For this JD, add a calibration check (reliability curve) on the model scores as a small step toward PD-style risk parameters.

## Why it matters for this JD
Prognosemodelle for risk, Risikoanalyse, Entscheidungsvorlagen for decision makers, Python/SQL.

## CV bullet it must live up to
"Risikoanalyse und Modellierung auf synthetischen PaySim-Zahlungen: SQL-Features, XGBoost und Isolation Forest gegen eine Regel-Baseline bei festem Alert-Budget, SHAP-Begründung und Business Case als Entscheidungsvorlage."

## Milestones
1 data + schema, 2 SQL features, 3 models + baseline, 4 SHAP + business case in Streamlit, 5 README with model card.
