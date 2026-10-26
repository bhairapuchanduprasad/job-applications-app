# Application notes: IDM Innovative Digitale Medizin, Product AI Engineer (Hamburg, hybrid)

Status: **build-first**. Build `care-note-structurer` with the IDM additions (fine-tuned German encoder, MLflow, pseudonymisation; brief in this folder) before submitting; the CV describes it. Stretch application (fit 55): research-heavy role in a small senior team.
Submit via IDM's recruiting portal (linked from LinkedIn): https://www.linkedin.com/jobs/view/4483569603. English documents. Salary band €75–100k (posted).

## Likely interview questions
1. **"Walk us through training and deploying an NLP model end-to-end."** Be honest: your production NLP is LLM-based extraction (Kniit) and retrieval fine-tuning/embedding benchmarking (thesis); QLoRA fine-tuning repo. Then the Care Note Structurer once built (encoder vs LLM, MLflow, eval).
2. **"How do you evaluate extraction quality?"** Ground truth (SAP-derived; chemist-written), field-level precision/recall, 33/45 → 93/90 at Kniit; RAGAS/PytrecEval.
3. **"How would you cut latency/cost in a real-time clinical setting?"** Smaller task models where they suffice, LLM only as fallback; Kniit deterministic pipeline ($200k → near zero).

Also prepare: transformer architecture basics (encoder vs decoder, tokenization), MLflow basics, data anonymisation, research interests/publication plans (one conference paper so far), why leave Kniit (public line).

## Form fields
- **Why IDM:** production clinical AI (ORPHEUS at UKE since early 2025, 40+ hospitals per IDM), non-profit owned by UKE, real German clinical documentation.
- **Salary:** posted band €75–100k; ask within the band (e.g. €75–80k). Profile default €70k is below the band.
- **Start:** 15 November 2026.
- **Work permit:** EU Blue Card.
- **German:** B1 (helpful, not required).
