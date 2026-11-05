# Project brief: Payment Fraud Detection Pipeline, R+V Fraud Management variant

Repo slug: `payment-fraud-detection` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-28_finanz-informatik_data-scientist-compliance/_work/project-brief-payment-fraud-detection.md). Created for R+V Data Scientist Fraud Management (2026-11-05). Time box 1-2 days with Claude Code.

## Goal
Fraud scoring on public synthetic PaySim payments: SQL/Python features (velocity, rolling amounts, counterparty stats) in Postgres, XGBoost vs Isolation Forest vs rule baseline at a fixed alert budget, SHAP reasons per alert, plus a small business-case calculation (prevented loss vs. investigation cost at the alert budget) in a Streamlit view for management.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Use Cases, Scorings und Analyseansätze konzipieren und bewerten" | rule baseline vs two models at a fixed alert budget |
| "belastbare Business Cases" | prevented-loss vs investigation-cost calculation |
| "Auffälligkeiten und Muster erkennen" | velocity/amount features, Isolation Forest |
| "Python, SQL" | Postgres feature table, pandas, scikit-learn |
| "adressatengerecht für Management" | Streamlit summary view |

## Scope, stack, milestones
Stack: Python, SQL (PostgreSQL), pandas, scikit-learn, XGBoost, SHAP, Streamlit. Milestones: 1 data + schema, 2 features in SQL, 3 models + baseline comparison, 4 business-case view, 5 README with model card.
Demo: dashboard showing alerts at a chosen budget with SHAP reasons and the resulting net benefit.

## CV bullets it must live up to
- Features and scoring on PaySim payments, XGBoost and Isolation Forest compared against a rule baseline at a fixed alert budget, SHAP reasons per alert.
- Streamlit view with a business case (prevented loss vs. investigation cost) for management.
