# Project brief: Payment Fraud Detection Pipeline, Union Investment variant (Databricks + MLflow + LLM alert summary)

Repo slug: `payment-fraud-detection` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-28_finanz-informatik_data-scientist-compliance/_work/project-brief-payment-fraud-detection.md). Created for Union Investment Data Scientist KI-Kompetenzzentrum (2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
PySpark feature pipeline on public synthetic PaySim payments (velocity, rolling amounts, counterparty stats) as Delta tables on Databricks (Free Edition); XGBoost vs Isolation Forest vs rule baseline at a fixed alert budget, tracked in MLflow; SHAP reasons per alert; an LLM (Azure OpenAI or Databricks-served model) writes a short German alert summary from the SHAP reasons, checked against the features (grounding check).

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Python und Databricks", "Databricks/Spark" | PySpark + Delta + MLflow on Databricks |
| "Machine-Learning-, Predictive-Analytics- und Generative-AI-Use-Cases" | XGBoost/Isolation Forest + LLM alert summaries |
| "Statistik" | precision at alert budget, PR curves, bootstrap CIs |
| "Git und CI/CD" | GitHub Actions running unit tests on feature functions |
| "KI-Standards ... Governance" | model card + data/feature documentation |

## Tech stack
Python, PySpark, Databricks Free Edition, Delta Lake, MLflow, XGBoost, scikit-learn, SHAP, Azure OpenAI (or Databricks Foundation Model API), pytest, GitHub Actions.

## Milestones
1. PySpark features + Delta (4 h) 2. Models + MLflow + statistics (4 h) 3. SHAP + LLM summary + grounding check (3 h) 4. Model card + README (1 h).

## CV bullet it must live up to (German)
- PySpark-Features auf synthetischen Zahlungsdaten (PaySim) als Delta-Tabellen in Databricks; Vergleich von XGBoost, Isolation Forest und Regel-Baseline bei festem Alert-Budget mit MLflow-Tracking, SHAP-Begründungen und LLM-generierten Alert-Zusammenfassungen mit Grounding-Check.
