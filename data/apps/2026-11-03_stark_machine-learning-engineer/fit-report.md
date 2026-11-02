# Fit report: STARK, Machine Learning Engineer (All genders), Munich (Operations Excellence / OAA team)

Source: https://www.linkedin.com/jobs/view/4485757108 (found by job-scout 2026-11-03)
Language: English posting, "send us your CV in English" → English CV + cover letter.
Seniority: "4–7 years in data engineering or ML engineering" (he has 3 incl. internships) → below the range but not >5 required. Security clearance eligibility required (defence).

## Fit score: 54 / 100
Content fit is good: ML for production line (yield prediction) and back-office (financial anomaly detection), pipelines from MES/ERP, deployment + monitoring. Covestro prepolymer work (process time series, batch deviation, Streamlit for chemists), Cognizant forecasting, Kniit pipelines with SAP-derived data and production deployment cover much of it. Gaps: 4–7 years, MLOps fundamentals (versioning, serving, drift, retraining), Airflow/dbt, MES data, security clearance as a non-EU national (Indian citizen with Blue Card): eligibility unclear.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| 4–7 yrs DE/MLE | ~3 yrs | ❌ (below range) |
| ML models deployed to production, not notebooks | Kniit pipeline in use; Covestro agent deployed to AWS; Covestro dashboard used by chemists | ✅ / 🟡 (classic ML in prod) |
| Python, SQL | yes | ✅ |
| scikit-learn, PyTorch | yes | ✅ |
| MLOps: versioning, serving, monitoring, retraining | Docker, CI/CD, AWS CDK; no model registry/drift | 🟡 |
| Pipelines from MES/ERP + back-office | Kniit ingestion; SAP-derived ground truth; Covestro sensor data | 🟡 |
| Airflow/dbt (plus) | none | ❌ |
| Cloud AWS/GCP/Azure (plus) | AWS + Azure | ✅ |
| Industrial/time-series/financial data (plus) | process + sensor time series, EV load forecasting | ✅ |
| MSc DS/CS/Stats | MSc AI | ✅ |
| Security clearance eligibility | non-EU citizen; unknown | ❓ decision for user |

## Gaps and honest framing
1. Experience below 4 years: lead with production results.
2. MLOps / drift / retraining: planned project covers it.
3. Security clearance: German Sicherheitsüberprüfung for non-EU nationals depends on the level; ask early.

## Red flags
Defence company (counter-check personal preference); clearance requirement; "Operations Excellence" team in the COO org (internal ML, not drone autonomy).

## Company hooks
1. €500m Series C co-led by Sequoia and Founders Fund, closed 23 June 2026, valuation above €3.5bn; unicorn since January 2026 ([Grosswald](https://www.grosswald.org/stark-defence-500-million-series-c-sequoia-founders-fund-loitering-munition/)).
2. Bundeswehr contract (~€269m initial) for strike drones alongside Helsing ([Resilience Media](https://resiliencemedia.co/germany-awards-stark-and-helsing-contracts-to-deliver-next-generation-strike-drones)).
3. Scaling production: Swindon (UK) plant producing thousands of drones a year ([Grosswald](https://www.grosswald.org/stark-defence-500-million-series-c-sequoia-founders-fund-loitering-munition/)) → yield prediction on the line matters.

## Project
Production Yield & Anomaly Pipeline (Plant Maintenance Agent variant, planned): see project-brief-production-yield-anomaly.md.
