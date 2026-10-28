# Application notes: HDP GmbH, Machine Learning Engineer

## Likely interview questions
1. **How would you add an ML feature to Cusa without disturbing a large existing system?** Start as a separate microservice with a clear REST contract, measure against labelled cases (as with the SAP-derived ground truth at Kniit), roll out behind a flag, keep a human in the loop for decisions on insured persons.
2. **When would you not use an LLM?** Kniit's second source stream: deterministic code pipeline instead of LLM calls, $200k projected LLM budget → near-zero, accuracy toward 100%.
3. **How do you protect sensitive data and models?** Be honest: no formal security role. Talk about pseudonymisation before model calls, self-hosted models for sensitive data, least privilege, no secrets in images (Care Note Structurer once built). Java: Python is main language, ready to learn Java.

## Form fields
- **Why HDP:** BesA (dictated site-visit notes → defect-report text) and the planned shared AI platform with anonymisation and container delivery; ML inside software that handles about 30% of German reportable workplace accidents.
- **Salary:** €65,000–70,000 (single number: €70,000). Blue Card threshold must be met.
- **Notice period / start:** available from 15 November 2026.
- **German:** B1, no certificate, improving.
- **Location:** willing to relocate to Alzey area; hybrid fine (also Frankfurt branch).
