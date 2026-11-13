# Project brief: Marketing Attribution & Media Mix Lab (repo: marketing-attribution-mmm-lab)
Goal: show attribution, incrementality, geo testing, MMM and experimentation on synthetic travel-marketing data. Proves: BigQuery, SQL, attribution, incrementality, geo testing, A/B testing, CUPED, media mix modelling, XGBoost.
Scope (1-2 days): 
1. Generator (Python): 6 channels, 12 weeks x 30 regions, spend, clicks, bookings with adstock/saturation ground truth; user-level touchpoint journeys.
2. BigQuery sandbox: tables + SQL views for last-click, first-click, position-based attribution.
3. Geo holdout: switch off one channel in matched regions, difference-in-differences incrementality estimate vs attribution claims.
4. MMM: regression with adstock + saturation (scikit-learn/statsmodels), recover ground-truth contributions, budget-allocation scenarios.
5. Experiment layer: A/B test with power analysis, sample size, significance test, CUPED; XGBoost conversion-propensity model vs logistic baseline.
6. Streamlit dashboard: channel ROI, attribution comparison, budget scenarios.
Stack: Python, SQL, BigQuery sandbox, pandas, scikit-learn, statsmodels, XGBoost, Streamlit.
Milestones: generator -> BigQuery/SQL -> geo test -> MMM -> experiments -> dashboard -> README.
README: problem, data caveats (synthetic), method comparison, results table, how to run. Demo: dashboard budget slider.
CV bullets it must live up to: (1) SQL attribution models, geo testing holdout read out for incrementality, MMM view for budget allocation on synthetic data in BigQuery; (2) A/B testing layer with power analysis, significance testing, CUPED, plus XGBoost conversion-propensity model.
