# Fit report: cancierge.ai, Machine Learning Engineer, Aachen (home-office first)

**Fit score: 72/100.** Good match on Python, PyTorch, evaluation harnesses (RAGAS/PytrecEval, ground-truth evaluation), text data pipelines (document ingestion, chunking), Docker, NLP and LLM fine-tuning (QLoRA). Gaps: deep PyTorch theory and hands-on training/tuning of neural networks in production, text data augmentation, GPU programming, Rust, Linux server administration (not explicit), medical/EU MDR domain.

Language: English working language; English documents. No cover letter needed (they ask for CV or LinkedIn plus something you are proud of); a short letter is included as optional.

Source: https://www.linkedin.com/jobs/view/4483193748. Salary €80,000–90,000 (stated). Entry level per LinkedIn.

## Requirements → evidence
| Requirement | Evidence | Rating |
|---|---|---|
| Strong Python, clean modular testable code | Python in all roles; sole developer at Kniit; clean code principles | ✅ |
| Solid PyTorch incl. theory | PyTorch at Covestro thesis; CNN/RNN/ResNet image classification repo (framework not stated); MSc AI | 🟡 |
| Hands-on ML training: hyperparameters, overfitting, learning rates | RF/XGBoost/LSTM (Covestro), LSTM/ARIMA/Prophet (Cognizant, 96% test accuracy), QLoRA fine-tuning | 🟡 |
| Evaluation harnesses: metrics, reproducibility, setups | RAGAS + PytrecEval automated evaluation; SAP ground-truth evaluation; embedding benchmark on 1M+ chunks | ✅ |
| Text data pipelines incl. cleaning, augmentation | Document ingestion and chunking (Kniit); retrieval pipelines (Covestro); augmentation not in profile | 🟡 |
| Basic Linux, Docker | Docker; AWS EC2; Linux not named | 🟡 |
| English | Business fluent | ✅ |
| NLP (nice) | NLTK, Hugging Face Transformers, information extraction | ✅ |
| LLM fine-tuning (nice) | Open Llama 3B QLoRA (built repo); fine-tuning for retrieval | ✅ |
| GPU programming, Rust (nice) | None | ❌ |

## Gaps and honest framing
- **PyTorch depth:** prepare to explain backprop, optimizers, learning-rate schedules, regularisation; revise before the CTO deep-dive.
- **Production model training:** most production work is LLM pipelines; training experience is from Covestro/Cognizant and projects.
- **Medical domain / EU MDR:** none; analogy: regulated documents, expert approval.

## Red flags
- Small startup, "senior team": the deep-dive will test fundamentals hard.

## Company hooks
- From the posting: lifetime AI platform for oncology and longevity; regulated medical product (EU MDR); medical logic from Head of AI and clinical experts; remote-first with monthly team days near Aachen; fast hiring process (intro, CTO deep-dive, Head of AI + CEO).
- Cancierge gives cancer patients AI second opinions in minutes, combining treatment guidelines with real-world data on how leading oncologists treat patients (source: https://www.humanx.co/europe/sponsors/cancierge).
- MVP live at Europe's largest breast cancer center; on track for MDR Class IIa certification, aiming to be among the first certified oncology AI products in Europe (same source).
- Seven oncologists across six countries involved: two on the cap table, five clinical partners (same source). Startup sponsor at HumanX Amsterdam 2026.
- Founders, funding and tech stack: nothing public found (2 searches, 2026-10-25).

## Review and ATS (2026-10-25)
- Reviewer round 1 applied: "testable" → "modular" (no test evidence in profile), GitLab CI/CD wording, evaluation harness / text data pipeline / PyTorch wording, NLP skills line, letter hook rewritten with real company facts.
- ATS coverage 60% (12/20). Remaining honest gaps, not claimed: testable (unit tests), production, reproducibility (CV says "reproducible"), data cleaning, hyperparameters, overfitting, Linux, GPU.
