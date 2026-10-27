# Project brief: Price Intelligence Copilot

Repo slug: `price-intelligence-copilot` (no link on the CV)
Status: **planned**. Build before submitting the KI Group (pricenxt) LLM Application Engineer application.
Time box: 1–2 days with Claude Code.

## Goal
A small "conversational analyst" over commodity price data, in the spirit of pricenxt: users ask "How did PP homopolymer prices in Germany move over the last 6 months and why?" and get a grounded answer that combines (a) exact numbers from a price-index database via tool calls and (b) cited explanations from market reports via RAG. Enterprise clients can reach the same data through an MCP server.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| LLM platform layer: retrieval services, embedding pipelines, well-designed APIs | FastAPI service: `/ask`, `/search`, `/alerts`; embedding pipeline for reports into pgvector |
| RAG in production: vector DB, retrieval strategies, chunking, evaluation, grounding | Hybrid retrieval (pgvector + keyword), chunking comparison, grounding check (every number must come from a tool result, every claim cites a chunk), eval set in CI |
| Conversational analyst for pricing data, semantic search, intelligent alerts | Agent with tools `get_price_series`, `compare_grades`, `search_reports`; semantic search endpoint; rule + LLM-summarised alerts on price moves |
| Function calling, tool use, prompt + context engineering | Typed tools (Pydantic), context budget, system prompt with units/currency rules |
| Assess foundation models on quality, cost, latency | LiteLLM: same eval set on two providers (e.g. Anthropic, OpenAI or Mistral), table of quality / cost / p95 latency |
| Agent architectures and MCP interfaces for enterprise customers | MCP server exposing `get_price_series` and `search_reports` |
| Python and/or TypeScript/Node.js | Backend Python; MCP server in TypeScript (Node) to cover the TS gap |
| React (nice) | Minimal React chat page with source citations and a price chart |

## Scope
In:
- Synthetic data: weekly price indices for ~10 plastics grades (PP, PE-HD, PE-LD, PVC, PET) across 3 regions, 2 years, in Postgres; 30–50 short synthetic market-report paragraphs (feedstock, demand, freight). Mark everything synthetic in the README.
- Embedding pipeline (async ingestion), pgvector, hybrid retrieval.
- Agent (plain function-calling loop or LangGraph) with typed tools; answer includes numbers + citations.
- Eval: 30 labelled questions (numeric answers + expected sources), grounding/faithfulness score, run in GitHub Actions; model comparison table.
- Alerts: weekly job flags moves > X% and writes an LLM summary with cited reasons.
- TypeScript MCP server over the same data.
- Request logging: latency, tokens, cost per request.
Out: real KI price data, auth/billing, production deployment.

## Architecture
```
reports ─► async embedding pipeline ─► pgvector ◄─┐
price indices (Postgres) ◄─ get_price_series ─────┤
user ─► React chat ─► FastAPI /ask ─► agent (LiteLLM, tools) ─► grounded answer + citations
enterprise client ─► MCP server (TypeScript) ─► same tools
weekly job ─► alerts (rules + LLM summary)
```

## Milestones
1. Synthetic data + Postgres + embedding pipeline (half day).
2. Agent with tools + grounding check + /ask (half day).
3. Eval set + model comparison in CI (2–3 h).
4. MCP server (TS) + alerts + React page + README (half day).

## Demo idea
2-minute video: ask a price question, show the chart and cited report snippets; call the MCP server from Claude Desktop; show the eval/model comparison table.

## CV bullets it must live up to
- Conversational analyst over commodity price data: an agent with typed function calling pulls exact figures from a price-index database and explains moves with cited passages from market reports retrieved by hybrid search (pgvector + keyword), with a grounding check on every answer.
- Async embedding pipeline and FastAPI services for Q&A, semantic search and price alerts; MCP server in TypeScript (Node.js) for enterprise access; labelled eval set comparing two foundation models on quality, cost and latency in CI.
