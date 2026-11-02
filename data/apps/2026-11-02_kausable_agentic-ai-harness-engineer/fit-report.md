# Fit report: kausable, Agentic-AI Harness Engineer (Heidelberg, hybrid)

Source: https://www.linkedin.com/jobs/view/4483994801 (found by job-scout 2026-11-02)
Language: English posting, no German requirement → English documents.

**Fit score: 62/100.** Strong on agentic systems, evaluation and production engineering; weaker on the ML-research side (PyTorch depth, in-context learning, PFNs) and the posting says they are "primarily hiring at senior level".

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Building agentic systems, multi-step tasks | Kniit: LangGraph multi-agent extraction (4 agents in parallel), P/R 33/45 → 93/90; Covestro: LangGraph routing agent | ✅ |
| Harnesses, context curation, hierarchical querying | Kniit: chunking, prompt engineering, agentic/deterministic/monolithic indexing strategies; MCP query service | ✅/🟡 (not with a custom foundation model) |
| Release criteria that show quantitatively when an agent is ready | Kniit precision/recall vs SAP-derived ground truth; thesis: RAGAS + PytrecEval automated eval | ✅ |
| Developer-facing abstractions / SDK | MCP service used from Claude Code; Python microservices | 🟡 |
| Python, strong SWE | 3 yrs Python, FastAPI, microservices, clean code | ✅ |
| Hands-on PyTorch fluency | PyTorch in thesis stack + skills; most DL work in TensorFlow/Keras | 🟡 |
| ML research / research-adjacent ML engineering | MSc AI thesis on RAG evaluation, embedding benchmark on 1M+ chunks, retrieval fine-tuning, one conference publication | 🟡 |
| In-context learning | Prompt engineering in production; no explicit ICL research | 🟡 |
| Evaluation, observability, reliability trade-offs | Eval pipelines ✅; deterministic pipeline replacing LLM ($200k → near zero) ✅; tracing/observability tools 🟡 | ✅/🟡 |
| Work with customers, researchers, product | SAP domain experts (Kniit), business stakeholders + chemists (Covestro), reported to CTO | ✅ |
| Nice: PFNs, synthetic data, probabilistic models | none | ❌ |
| Nice: Weights & Biases, model registries, CI for models | GitLab CI/CD; no W&B | ❌/🟡 |
| Nice: model serving, APIs, containers, cloud | FastAPI, Docker, Kubernetes, AWS CDK, Azure | ✅ |
| Nice: startup / 0-to-1 | Kniit pre-funding startup, sole developer end to end | ✅ |

## Gaps and honest framing
- **Seniority:** "primarily hiring at senior level, open to exceptional candidates with fewer years". Lead with ownership: sole developer of a full pipeline, reporting to the CTO, measurable jump in precision/recall.
- **PyTorch / ML research depth:** say plainly that production work has been LLM agents and evaluation; PyTorch from MSc and thesis work. Don't claim research publications beyond the one listed.
- **PFNs, in-context learning theory, W&B:** gaps. The tailored project (Agent Eval Harness, kausable variant) covers W&B + release gates, but it is not built yet.

## Red flags
- Senior-level preference (see above). Small team (9 people), research-heavy culture; expect a deep technical interview.
- Application asks for "your favorite way to drink coffee" along with the CV: add one line in the letter.

## Company hooks (sources)
1. €12M seed round (July 2026) led by UVC Partners and Entourage, with HTGF and Mätch VC; team of nine to grow. ([tech.eu](https://tech.eu/2026/07/23/kausable-raises-eur12m-to-rethink-how-ai-learns/), [HTGF](https://www.htgf.de/kausable-seed-finanzierung/))
2. Approach: train a foundation model once on synthetic causal data, then let it learn new tasks from a few examples instead of updating weights. ([pulse2](https://pulse2.com/kausable-raises-e12-million-seed-round-to-develop-self-adapting-ai-models))
3. Spun out of Heidelberg University's Department of Physics and Astronomy (EXIST project at SRH Heidelberg); founders Johannes Haux (CEO), Benjamin Herdeanu (CTO), Gregor Ramien (COO). ([tech.eu](https://tech.eu/2026/07/23/kausable-raises-eur12m-to-rethink-how-ai-learns/))
4. TipPFN: zero-shot model for forecasting rare, high-impact events. ([startuphub](https://www.startuphub.ai/startups/kausable.md))
