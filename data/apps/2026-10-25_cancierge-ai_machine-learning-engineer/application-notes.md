# Application notes: Cancierge (cancierge.ai), Machine Learning Engineer, Aachen

Apply via the LinkedIn posting (https://www.linkedin.com/jobs/view/4483193748). They say no cover letter is needed: send the CV (or LinkedIn) plus "anything you are proud of". Best candidates: the Open Llama 3B QLoRA notebook and the CNN/RNN/ResNet notebook (both on GitHub, linked in the CV). The cover letter is optional; attach it only if the form has a slot.

Process: 30-min intro call, technical deep-dive with the CTO, then Head of AI + CEO. Salary in the posting: €80,000–90,000.

## Likely interview questions
**1. "Walk us through how you'd design an evaluation harness for a model that gives treatment guidance."** Fix a labelled ground-truth set with clinical experts, pick metrics per task (precision/recall for extraction, retrieval metrics, answer correctness), version data + configs + seeds so every run is repeatable, compare setups side by side. Evidence: thesis RAGAS + PytrecEval harness against chemist ground truth; Kniit loop against SAP-derived ground truth (33/45 → 93/90 precision/recall).

**2. "How do you control overfitting and pick learning rates / hyperparameters in PyTorch?"** Train/validation/test splits (time-based for time series), early stopping, weight decay, dropout, learning-rate schedules, small search over key hyperparameters. Evidence: LSTM at Cognizant (96% test accuracy, held up on unseen data), RF/XGBoost/LSTM comparison at Covestro, QLoRA fine-tuning. Revise PyTorch internals (autograd, optimizers, schedulers, DataLoader) before the CTO round: this is the main gap.

**3. "How would you turn prototype logic from our Head of AI into production code?"** Small modules with clear interfaces, typed configs, tests around each step, evaluation in CI so every change is measured. Evidence: sole developer at Kniit reporting to the CTO; domain experts approve changes via Expert Interface.

Also prepare: text data cleaning/augmentation approaches, Docker + basic Linux, EU MDR basics (traceability, change control), "Why are you leaving Kniit?" → use the public line from the profile only.

## Form fields
- **Why Cancierge?** You give cancer patients a second opinion in minutes instead of weeks, built with oncologists and heading for MDR Class IIa. I want to build an AI core where every change is measured against what clinicians expect, which is how I already work.
- **Salary expectation:** €80,000 gross/year (posting range €80,000–90,000; profile range €60,000–75,000 is below their band, so quote the bottom of theirs).
- **Earliest start:** 15 November 2026.
- **Notice period:** none beyond 13 November 2026.
- **Work authorisation:** EU Blue Card (Germany).
- **Location:** Remote within Germany; happy to come to the monthly team days near Aachen.
- **German level:** B1 (English is their working language).
