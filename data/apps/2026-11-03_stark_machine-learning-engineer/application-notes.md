# Application notes: STARK, Machine Learning Engineer (Operations Excellence / OAA), Munich

Decision for you: STARK is a defence company (strike drones) and requires eligibility for a security clearance. As a non-EU national on a Blue Card, eligibility is unclear: ask in the first recruiter call. Posting asks 4–7 years (you have ~3). Before submitting: build Production Yield & Anomaly Pipeline (_work/project-brief-production-yield-anomaly.md) or remove the Projects section.

## Likely interview questions
1. Tell us about an ML model on production/process data.
   → Covestro: sensor time series, lag/rolling features, RF/XGBoost/LSTM vs curve fitting, Streamlit for chemists; Cognizant LSTM 96%.
2. How do you take a model from notebook to production and keep it healthy?
   → Docker, Kubernetes, AWS CDK, GitLab CI/CD; honest: registry/drift/retraining not yet in a job; plan: MLflow, PSI drift, retraining DAG.
3. How would you scope an ML use case with stakeholders?
   → Covestro AI consulting: map decisions first; Kniit: measure against ground truth, use code where a model isn't needed ($200k → near zero).

## Form answers
- Why STARK: fast production scale-up (Bundeswehr contract, Swindon plant), ML on real line and back-office data.
- Salary: €60,000–75,000 gross/year; single number €70,000.
- Start: 15 November 2026. EU Blue Card. CV in English (requested).
