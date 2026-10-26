# Fit report: IDM Innovative Digitale Medizin gGmbH, Product AI Engineer, Hamburg (hybrid)

**Fit score: 55/100.** Matches the tooling (Python, PyTorch, Hugging Face Transformers, LLMs, fine-tuning with QLoRA/LoRA and for retrieval, embedding benchmarking on 1M+ chunks, evaluation pipelines, Docker, Kubernetes, GitLab CI) and NLP-adjacent production work (LLM extraction from documents). Gaps: training and owning clinical NLP models end-to-end (your NLP work is mostly LLM/RAG-based, not trained task models), MLflow/W&B experiment tracking, GPU/CUDA work, publications at top ML/NLP venues, research leadership (research agenda, mentoring students, grant writing), healthcare data / anonymisation. The posting is research-heavy and the team is "small senior"; risk that 3 years reads junior for them.

Language: German posting, German "nicht erforderlich, aber hilfreich" → English CV + cover letter. Salary €75–100k (above your range; Blue Card fine).

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| 3+ years hands-on ML/AI with NLP focus | 3 years ML/AI; NLP via LLM extraction (Kniit), RAG + embeddings (Covestro thesis), NLTK info extraction project | 🟡 |
| Deep Python + PyTorch | Python ✅; PyTorch used in thesis / fine-tuning | 🟡 |
| Hugging Face (Transformers, Datasets, Tokenizers) | Transformers in thesis (embedding benchmarks, retrieval fine-tuning); QLoRA fine-tuning of Open Llama 3B (built repo) | ✅ |
| Modern NLP architectures (Transformer, LLMs, encoder/decoder) | LLM work + embedding models; Udemy LLMs Mastery: Transformers & Generative AI | ✅ |
| MLOps (MLflow, Docker, CI/CD for ML) | Docker, GitLab CI/CD, automated eval on AWS; **no MLflow/W&B** | 🟡 |
| SE fundamentals (Git, testing, code review, docs) | Git/GitLab, API tests, eval tests | ✅ |
| Own projects idea → deployment | Kniit sole developer end-to-end | ✅ |
| Publications at top venues (plus) | One conference paper (autonomous indoor vehicles), not ML/NLP top venue | 🟡 |
| Clinical/medical data (plus) | None | ❌ |
| Research leadership, mentoring, grant writing | None | ❌ |
| Real-time latency/resource optimisation | MCP millisecond retrieval; deterministic pipeline cost cut | 🟡 |
| Data anonymisation/harmonisation across heterogeneous data | None formally | ❌ |
| German (helpful, not required) | B1 | 🟡 |

## Gaps and honest framing
1. **Trained clinical NLP models:** frame thesis retrieval fine-tuning + QLoRA repo + embedding benchmarking; do not claim clinical NLP. Planned project (Care Note Structurer, IDM variant: fine-tuned German encoder vs LLM extraction, MLflow) closes it on paper. Build first.
2. **MLflow / W&B:** not used; project adds MLflow.
3. **Research leadership/publications:** don't stretch the one paper.

## Project on the CV
Reused planned **Care Note Structurer** (dexter health) with an IDM variant brief (`project-brief-care-note-structurer.md`). Status planned → **build-first**.

## Red flags
- Hybrid ML engineering + research leadership; "kleines Senior-Team". Fit is borderline (55), apply as a stretch.
- Medical device certification context: expect regulatory/quality questions.

## Company hooks (research 2026-10-26)
1. IDM is a non-profit, wholly owned subsidiary of UKE Hamburg-Eppendorf, founded 2024, no venture capital. ([IDM company page](https://www.idmedizin.de/en/company))
2. ORPHEUS (AI speech recognition + ambient documentation) runs at UKE since early 2025 and, per IDM, at 40+ hospitals and 500+ practices; on-prem for large hospitals, hosted in Germany for practices. ([IDM](https://www.idmedizin.de/en))
3. Models trained on millions of German-language patient records (IDM cites 7 million UKE records), used anonymised. ([IDM](https://www.idmedizin.de/en), [heise podcast listing](https://apx-security-es.audible.es/pd/B0GVQ1869N))
4. IDM argues for a sovereign medical AI for Europe (heise KI-Update). ([IDM news](https://www.idmedizin.de/en/news/heise-ki-update-kliniken-sprachmodelle))
5. IDM is pursuing medical-device-manufacturer certification. ([IDM](https://www.idmedizin.de/en/company))
