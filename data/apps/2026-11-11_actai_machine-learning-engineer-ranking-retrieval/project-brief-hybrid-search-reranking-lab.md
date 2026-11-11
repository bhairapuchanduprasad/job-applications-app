# Project brief: hybrid-search-reranking-lab
Goal: retrieval benchmark comparing BM25, dense embeddings and hybrid search with a cross-encoder reranker, plus a serving layer that reports latency and cost.
Why for ActAI ML Engineer Ranking & Retrieval: proves embeddings, hybrid search, reranking, retrieval evaluation, accuracy/latency/cost trade-offs, PyTorch, inference services.
Scope (1-2 days): public corpus (e.g. BEIR subset such as SciFact/FiQA), ~1-2k queries with qrels.
Stack: Python, PyTorch, sentence-transformers, rank_bm25, Qdrant, cross-encoder reranker, FastAPI, pytest.
Architecture: ingest -> BM25 index + Qdrant dense index -> hybrid fusion (RRF) -> cross-encoder rerank -> FastAPI /search with per-stage timing.
Milestones: 1) corpus + qrels loader, BM25 baseline; 2) dense + hybrid RRF; 3) reranker; 4) eval harness (nDCG@10, MRR, recall@k) + regression gate vs stored baseline; 5) FastAPI service with latency/cost table; 6) README.
README outline: problem, data, configs compared, results table (real numbers only after running), latency/cost, how to run.
Demo: curl /search with ?mode=bm25|dense|hybrid|rerank and the results table.
CV bullets it must live up to: (1) benchmark with BM25, dense, hybrid + cross-encoder reranker scored with nDCG, MRR, recall@k and a regression check flagging metric drops; (2) FastAPI service reporting latency and cost per query per configuration.
