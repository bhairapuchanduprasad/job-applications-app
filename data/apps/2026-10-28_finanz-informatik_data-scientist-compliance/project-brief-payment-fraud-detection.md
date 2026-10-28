# Project brief: Payment Fraud Detection Pipeline (repo slug: payment-fraud-detection)

## Goal
An explainable fraud-detection pipeline on public synthetic payment data, plus a small sanctions name-screening step, to prove PySpark, predictive ML, validation and explainability for Finanz Informatik's ZV-Datengetriebene Betrugserkennung.

## Why it matters for this JD
Covers the gaps PySpark, payments/fraud, embargo/sanctions screening, "präzise, erklärbar und regulatorisch belastbar", large data, analysis pipelines.

## Scope (1–2 days)
- Data: PaySim (Kaggle, synthetic mobile-money transactions, ~6M rows) loaded with PySpark.
- Features in PySpark: per-account velocity (txn count/amount in rolling windows), balance-delta inconsistencies, counterparty novelty, hour-of-day; written to Postgres as a small SQL feature table.
- Models: rule-based baseline (amount + velocity thresholds), Isolation Forest (unsupervised), XGBoost (supervised, time-based split).
- Evaluation: precision/recall/PR-AUC, precision at a fixed alert budget (e.g. top 0.1% of transactions), false-positive rate vs baseline.
- Explainability: SHAP top reasons per flagged transaction rendered as a text explanation.
- Sanctions screening: fuzzy name matching (rapidfuzz + normalisation/transliteration) of counterparty names against the public EU consolidated financial sanctions list; labelled small test set.
- Model card (data, metrics, limits, fairness notes), pytest for features, GitHub Actions.

## Architecture sketch
PaySim CSV → PySpark job (features) → Parquet + Postgres feature table → training notebook/script (sklearn/XGBoost, MLflow optional) → scoring script producing alerts with SHAP reasons → sanctions screener → report (Markdown/Streamlit).

## Milestones
1. PySpark features + baseline (half day). 2. Models + evaluation at alert budget (half day). 3. SHAP explanations + sanctions screening (half day). 4. Model card, tests, CI, README (half day).

## README outline
Problem, data, features, models, results table, example explained alert, sanctions screening, limits, how to run.

## Demo idea
Streamlit page: pick a flagged transaction, see score, SHAP reasons, and sanctions match result.

## CV bullets it must live up to
- Predictive ML pipeline on the public synthetic PaySim payment dataset: PySpark feature engineering (velocity, rolling amount and counterparty features), XGBoost vs. Isolation Forest, compared to a rule-based baseline on precision/recall at a fixed alert budget.
- Explainable alerts with SHAP reasons per flagged transaction, fuzzy name screening against the public EU sanctions list, SQL feature store in Postgres and a model card.
