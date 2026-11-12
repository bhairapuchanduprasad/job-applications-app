# Project brief: Retail Demand Forecasting & Replenishment Optimizer
**Goal:** forecast demand for synthetic multi-store retail data and turn forecasts into an optimal replenishment plan.
**Why (MediaMarktSaturn Expert Data Scientist):** proves demand forecasting, inventory/replenishment optimization, BigQuery, SQL, baseline comparison, uncertainty estimates, linear programming.
**Scope (1-2 days):** synthetic daily sales for ~20 stores x 200 SKUs (seasonality, promotions, noise); BigQuery sandbox tables + SQL feature queries; baselines (seasonal naive, SARIMA) vs XGBoost; rolling-origin backtest with prediction intervals; LP (SciPy linprog) choosing order quantities under stock/capacity constraints; Streamlit view of forecast error and plan cost.
**Stack:** Python, BigQuery, SQL, SciPy, XGBoost, scikit-learn, Streamlit, pytest.
**Architecture:** generator -> BigQuery raw -> SQL feature view -> forecast models -> forecast table -> LP optimizer -> plan table -> Streamlit.
**Milestones:** 1 data generator + BigQuery load; 2 baselines + backtest; 3 XGBoost + intervals; 4 LP plan; 5 Streamlit + README.
**README outline:** problem, data, method, backtest results (real numbers only), how to run.
**Demo idea:** pick a store, see forecast vs actuals with intervals and the resulting order plan, compare plan cost to naive ordering.
**CV bullet it must live up to:** BigQuery SQL features; seasonal-naive, SARIMA, XGBoost forecasts on rolling-origin backtest with prediction intervals; LP replenishment plan (SciPy) under stock and capacity constraints.
