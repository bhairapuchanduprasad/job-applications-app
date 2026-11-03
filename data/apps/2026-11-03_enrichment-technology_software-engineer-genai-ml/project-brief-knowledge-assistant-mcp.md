# Project brief: knowledge-assistant-mcp

**Status:** planned (on the Finanz Informatik CV; build before submitting)
**Repo:** github.com/bhairapuchanduprasad/knowledge-assistant-mcp (create it; do NOT link it on the CV)
**Time box:** 1–2 days with Claude Code

## Goal
A small but complete RAG assistant over internal-style documents (process descriptions, intranet pages). It runs on a locally hosted open-source LLM and is reachable via a REST API and as an MCP tool. It comes with tests, an evaluation set in CI, basic monitoring and proper documentation.

## Why it matters for this JD (Finanz Informatik, AI Engineer)
| JD keyword / must-have | How the project proves it |
|---|---|
| LlamaIndex ("moderne KI-Frameworks, z. B. LangChain, LlamaIndex") | Indexing + query engine built with LlamaIndex (your only real gap in frameworks) |
| RAG-Systeme für Unternehmenswissen | RAG over process docs + intranet pages, answers with source citations |
| Integration über APIs und MCP | FastAPI REST API + MCP server exposing the same `search` / `ask` tools |
| Testing, CI/CD | pytest unit tests + RAGAS evaluation set run in GitLab CI |
| Monitoring | request logging with latency, retrieved-chunk scores, token counts; `/metrics` endpoint |
| Dokumentation & Wissensmanagement | MkDocs site: architecture, API reference, operations runbook, "how to add a source" guide |
| FI context: own platform, open-source models, no cloud | Local open-source LLM (e.g. via Ollama), no external API calls needed |

## Scope (cut to 1–2 days)
In:
- Ingest a folder of Markdown/PDF/HTML docs (use public sample docs, e.g. a set of public German/English process or policy documents; no real company data).
- Chunking + embeddings (open-source embedding model) + local vector store (Qdrant in Docker, or LlamaIndex's simple store).
- Query engine with source citations; refuse to answer when retrieval scores are too low.
- FastAPI: `POST /ask`, `POST /search`, `GET /health`, `GET /metrics`.
- MCP server (Python MCP SDK) exposing `search_documents` and `ask_question`.
- pytest: chunking, API contract, MCP tool schema. RAGAS eval on ~20 hand-written Q/A pairs; CI fails if faithfulness or context recall drops below a threshold.
- GitLab CI (or GitHub Actions if you host on GitHub; then change the CV bullet): lint, tests, eval.
- MkDocs documentation.
Out: auth, UI beyond a minimal page, fine-tuning, SharePoint connector.

## Tech stack
Python, LlamaIndex, Ollama (open-source LLM, e.g. Mistral or Llama), open-source embedding model, Qdrant, FastAPI, MCP Python SDK, pytest, RAGAS, Docker / docker-compose, GitLab CI, MkDocs.

## Architecture sketch
```
docs/ ──ingest.py──► chunks + embeddings ──► Qdrant
                                              │
            FastAPI (/ask /search /metrics) ◄─┤ LlamaIndex query engine ──► Ollama LLM
            MCP server (search_documents,    ◄┘
                        ask_question)
logging middleware ──► JSON logs + /metrics (latency, scores, tokens)
CI: ruff → pytest → RAGAS eval (threshold gate)
```

## Milestones
1. Ingest + index + query engine with citations (half day)
2. FastAPI + MCP server sharing one service layer (half day)
3. pytest + RAGAS eval set + CI pipeline (half day)
4. Monitoring middleware + MkDocs docs + README + demo GIF (half day)

## README outline
What it is · Architecture diagram · Quickstart (`docker compose up`) · REST API examples · Using it from Claude Code / any MCP client · Evaluation results (real numbers from your run) · Monitoring · Design decisions (why local LLM, chunking choice, refusal threshold)

## Demo idea
Claude Code (MCP client) asks "Wie beantrage ich Urlaub?" against a sample policy folder; the tool returns an answer with cited sources. Then the same question goes through `curl /ask`. Show a CI run where the eval gate passes.

## CV bullets it must live up to
- RAG assistant over internal process documents and intranet pages, built with LlamaIndex and a locally hosted open-source LLM; answers cite their sources and are served through a FastAPI REST API and an MCP server, so AI agents can call it as a tool.
- pytest unit tests and a RAGAS evaluation set run in a GitLab CI/CD pipeline; request logging with latency and retrieval metrics for monitoring; MkDocs documentation of architecture, API, and operation.

When built: set status to `built` in `profile/master-profile.md`, add real eval numbers there, and you may then mention it in cover letters.
