# Fit report: Jobgether (for an undisclosed healthcare job-matching platform), Data Scientist - AI & Experimentation, remote Germany (office Berlin-Mitte)

**Fit score: 52/100.** Strong: Python (pandas, scikit-learn, NumPy), predictive models taken from concept to use (Covestro RF/XGBoost/LSTM with Streamlit tool for chemists; Cognizant forecasting), LLM + RAG systems with prompt engineering and output evaluation (Kniit P/R vs ground truth, RAGAS thesis), SQL, AWS, stakeholder communication. Gaps: **A/B testing / experimentation design** (none), **performance-marketing metrics** (CAC, ROAS, attribution: none), funnel analysis, e-commerce/marketplace domain, statistics depth beyond ML practice, Jira/QuickSight. Anomaly detection/trend analysis only adjacent (batch-deviation prediction, EV load forecasting).

Found by job-scout (LinkedIn 4484111092). Salary €42–75k (JD). English posting → English documents. Applications go through Jobgether's AI matching, then the partner.

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Statistics: methods, assumptions, interpretation | ML evaluation, time-series models (ARIMA/SARIMA); no formal stats role | 🟡 |
| Python (pandas, scikit-learn, NumPy), strong SQL | yes; SQL with Postgres | ✅ |
| Applied DS to real business problems | Covestro synthesis prediction, Cognizant EV load | ✅ |
| ML + AI from concept to practical use | Covestro Streamlit tool; Kniit pipeline handed over | ✅ |
| LLMs + RAG in (near-)production: prompts, retrieval quality, output eval | Kniit, thesis (RAGAS, PytrecEval, embedding benchmark) | ✅ |
| A/B testing (sample size, significance, pitfalls) | none | ❌ |
| Performance marketing (CAC, ROAS, attribution) | none | ❌ |
| Anomaly detection / trend analysis / MMM / MTA | batch deviation (adjacent), load forecasting (trend) | 🟡 |
| E-commerce / marketplace | none | ❌ |
| Jira, documentation | not stated | 🟡 |

## Gaps and honest framing
1. **Experimentation and marketing analytics:** state plainly; new project adds an A/B design with power analysis on synthetic data.
2. **Marketplace domain:** none.

## Red flags
- Partner company undisclosed; AI-screened by Jobgether.
- "Lead data science initiatives" + broad scope (marketing, pricing, matching, LLM) for €42–75k.

## Company hooks
- Partner unknown. JD facts only: digital job-matching platform in healthcare recruitment; healthcare professionals matched with employers; Berlin-Mitte office, remote in Germany.

## Projects on the CV
- **Matching Experiment Lab** (new, planned): ranking model for candidate–job matches on synthetic healthcare-recruitment data, LLM enrichment of job texts with RAG and an output-quality eval, and an A/B test of the new ranking with power analysis, sample size and significance testing plus a funnel/KPI dashboard. Brief: `_work/project-brief-matching-experiment-lab.md`. Status: build-first.
