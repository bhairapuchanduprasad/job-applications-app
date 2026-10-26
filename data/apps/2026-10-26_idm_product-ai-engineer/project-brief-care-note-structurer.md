# Project brief: Care Note Structurer, IDM variant (clinical NLP + MLOps)

Repo slug: `care-note-structurer` (no link on the CV). Status: **planned**.
Base brief: `applications/2026-10-14_dexter-health_ai-engineer-llm/_work/project-brief-care-note-structurer.md` (LLM extraction from dictated care notes with schema validation, LLM fallback, eval set, React review screen). Build that repo; this file adds what IDM's Product AI Engineer CV needs.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Klinische NLP-Modelle entwickeln und deployen ... trainieren und optimieren" | Fine-tune a German encoder (e.g. `deepset/gbert-base`) for token classification of clinical entities on the synthetic notes |
| "HuggingFace-Ökosystem (Transformers, Datasets, Tokenizers)" | Datasets for the labelled set, Tokenizers with label alignment, Trainer API |
| "Experiment-Tracking (MLflow, W&B), Model-Versionierung" | MLflow runs (params, metrics, model registry versions) |
| "Latenz, Skalierbarkeit und Ressourceneffizienz" | Compare fine-tuned encoder vs LLM extraction: F1 per field, latency, cost; ONNX/quantised CPU inference optional |
| "Docker, CI/CD für ML", "Anonymisierung" | Docker serving (FastAPI), GitLab CI/GitHub Actions running eval; pseudonymisation step for names/dates before training |

## Extra scope (≈1 day on top of the base)
1. Synthetic German care/clinical notes (~400, generated + hand-checked 80 for test), BIO labels for vitals, medication, wound, measure.
2. Fine-tune gbert-base (PyTorch, HF Trainer) on CPU/Colab GPU; log to MLflow; register best model.
3. Benchmark table: encoder vs LLM vs hybrid (encoder first, LLM fallback for low confidence): field F1, p95 latency, cost/note.
4. Pseudonymisation pre-step; README section on limits (synthetic data, not a medical device).

## Exact CV bullets it must live up to
- Clinical NLP pipeline that turns dictated care-note transcripts into structured entries (vitals, medication, wound notes): a German encoder fine-tuned with Hugging Face Transformers for entity extraction, compared against LLM extraction with schema validation and LLM fallback.
- Experiment tracking and model versioning in MLflow, field-level evaluation on a labelled test set in CI, FastAPI service in Docker with latency logging and a pseudonymisation step before training.
