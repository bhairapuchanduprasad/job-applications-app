# Project brief: industrial-graphrag-platform
**Goal:** reference platform on local Kubernetes combining OpenSearch (keyword + vector), an RDF knowledge graph with SPARQL, and a GraphRAG LLM agent over synthetic industrial data.
**Why for this JD:** proves OpenSearch, Vector Search, Milvus, RDF, SPARQL, GraphRAG, Kubernetes, CI/CD, Python/APIs, Agentic AI.
**Scope (1-2 days):** synthetic docs + sensor master data; ingest pipeline; hybrid search; SPARQL endpoint; GraphRAG agent; Helm chart; CI.
**Stack:** Python, FastAPI, OpenSearch, Milvus (optional second vector backend), rdflib/Oxigraph, kind + Helm, GitHub Actions, LiteLLM + any LLM.
**Architecture:** loader job -> OpenSearch index (BM25 + kNN) and RDF store; API: /search (hybrid), /sparql, /ask (agent picks vector, SPARQL or both, cites sources).
**Milestones:** 1) kind cluster + OpenSearch via Helm; 2) ingest + hybrid search; 3) RDF graph + SPARQL; 4) GraphRAG agent; 5) Milvus swap-in behind interface; 6) CI + README.
**README outline:** problem, architecture diagram, quick start (kind), example queries, design notes.
**Demo:** question needing both a graph hop and text passages, answered with citations.
**CV bullet it must live up to:** runs locally on Kubernetes (kind/Helm); Python pipelines load documents and master data into OpenSearch (keyword + vector) and an RDF knowledge graph; FastAPI with hybrid search, SPARQL queries and GraphRAG answers from an LLM agent; GitHub Actions CI. (Milvus is in the title: implement it or remove it from the CV.)
