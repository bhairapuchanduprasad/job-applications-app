# Project brief: Matching Experiment Lab (new)

Repo slug: `matching-experiment-lab` (no link on the CV). Status: **planned** (new, created for Jobgether Data Scientist - AI & Experimentation, 2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
Show the experimentation + LLM side of a healthcare job-matching marketplace on synthetic data:
1. Synthetic marketplace (nurses/physicians, employers, job posts, sessions: view → apply → interview), generated with realistic drop-offs.
2. Ranking model (logistic regression baseline vs XGBoost) predicting apply probability; offline metrics (AUC, NDCG@10).
3. LLM enrichment: RAG over a small set of public German/English healthcare job-title taxonomies to normalise job titles and extract requirements; prompt + output eval (exact-match on labelled sample, hallucination check).
4. A/B test of new ranking vs baseline on simulated traffic: pre-registered metric, power analysis and sample size, two-proportion z-test and bootstrap CI, a CUPED variance-reduction variant, and a write-up of pitfalls (peeking, novelty, SRM check).
5. Funnel + KPI dashboard (Streamlit) and a one-page decision memo.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "A/B testing, including sample size estimation, statistical significance, common experimental pitfalls" | step 4 |
| "Build and improve LLM-powered product features, including RAG" | step 3 |
| "evaluation workflows to assess AI output quality ... regressions" | step 3 eval in CI |
| "conversion funnels and user journeys", "KPIs and dashboards" | step 5 |
| "predictive models ... job matching" | step 2 |

## Tech stack
Python, pandas, NumPy, SciPy, statsmodels, scikit-learn, XGBoost, LiteLLM, pgvector or FAISS, Streamlit, DuckDB/SQL, pytest, GitHub Actions.

## Milestones
1. Synthetic data + SQL funnel (3 h) 2. Ranking models (3 h) 3. LLM enrichment + eval (3 h) 4. A/B analysis + memo (3 h) 5. Dashboard + README (2 h).

## README outline
Problem → data generation → models → LLM feature + eval → experiment design and results → limitations.

## Demo idea
Streamlit: pick an effect size and traffic, see required sample size; run the simulated test; view funnel per arm.

## CV bullets it must live up to
- Job-matching experiment on synthetic healthcare-recruitment data: XGBoost ranking vs logistic baseline, LLM job-title normalisation with RAG and an output-quality eval, and an A/B test with power analysis, sample size, significance testing and CUPED, reported in a Streamlit funnel and KPI dashboard.
