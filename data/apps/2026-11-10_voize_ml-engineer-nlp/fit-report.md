# Fit report: voize, ML Engineer in NLP (Berlin)
**Fit score: 72/100.** Strong match on LLM agents, evaluation and production work; weaker on model training in production and care-domain/German-language NLP.

German requirement: No mention of German (posting in English, "Fluent English").

| Requirement | Evidence | |
|---|---|---|
| LLM agents, tool use, structured outputs, context design | Kniit LangGraph multi-agent system, MCP tool service, Covestro agentic app | ✅ |
| Evaluation, benchmarks, error analysis, regression tests | Kniit P/R 33/45 → 93/90 vs ground truth; Covestro RAGAS/PytrecEval thesis | ✅ |
| Train / adapt models, production | RF/XGBoost/LSTM at Covestro, QLoRA fine-tuning (built project), embedding benchmark | 🟡 |
| Personal-data detection, privacy | Only in planned Care Note Structurer project | 🟡 |
| Strong software engineering, tested code | FastAPI, Docker, CI/CD, clean code | ✅ |
| Latency/cost/model routing/caching | $200k budget to near-zero, ms-latency MCP, LiteLLM; no caching proof | 🟡 |
| Care/nursing domain, German-language models | none | ❌ |

## Gaps
- Fine-tuned model shipped to production (only QLoRA hobby project and Covestro retrieval fine-tuning).
- Caching / model routing as a named practice; German NLP; healthcare domain.
- Care Note Structurer is `planned`: must be built before submitting.

## Hooks
- Series A of about $50M in Nov 2025 (Balderton lead), expansion in Europe and the US (tech.eu 2025/11/17).
- Product used by 200,000+ care workers per the posting; agent stack described as young.
- Role owns evaluation from production traces; maps to my Kniit ground-truth evaluation work.
