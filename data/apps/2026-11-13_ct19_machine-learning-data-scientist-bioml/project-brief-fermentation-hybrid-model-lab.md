# Project brief: Fermentation Hybrid Model Lab (repo: fermentation-hybrid-model-lab)
**Goal:** hybrid mechanistic/ML model of simulated fed-batch fermentation with surrogate and uncertainty.
**Why (CT19 BioML):** proves kinetic/ODE models, hybrid mechanistic/ML, synthetic training data, surrogate models, uncertainty, sensor time series.
**Scope (1-2 days):** (1) SciPy solve_ivp Monod fed-batch model (biomass, substrate, product, DO-like state), parameter sampling to generate synthetic runs with sensor noise. (2) Hybrid: ODE prediction + PyTorch residual network trained on noisy "real" runs from a perturbed parameter set; compare vs pure ML (XGBoost) and pure ODE. (3) Surrogate MLP trained on ODE simulations, speedup measured. (4) Uncertainty: deep ensemble, calibration/coverage check. (5) Optional Streamlit plot page.
**Stack:** Python, SciPy, NumPy, Pandas, PyTorch, XGBoost, Matplotlib, Streamlit, pytest.
**Architecture:** sim/ (ode.py, generator.py) -> data/ -> models/ (hybrid.py, surrogate.py, ensemble.py) -> eval/ -> app.py.
**Milestones:** ODE+generator; baselines; hybrid; surrogate; ensemble UQ; README.
**README outline:** problem, model equations, results table (hybrid vs ODE vs ML, surrogate speedup, interval coverage), limitations (simulated data only).
**Demo:** plot of predicted growth/titer with uncertainty band vs noisy measurements.
**CV bullet it must live up to:** "Hybrid mechanistic/ML model of a simulated fed-batch fermentation: kinetic/ODE models (Monod growth, substrate and product balances) generate synthetic training data, a neural network learns the residual against noisy sensor-style data, a surrogate model replaces the ODE solver, and ensembles give uncertainty bands on growth, titer and yield."
