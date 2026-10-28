# Project brief: Clinical Info Assistant, paddy variant (Next.js + Vercel AI SDK + promptfoo + Arize Phoenix)

Repo slug: `clinical-info-assistant` (no link on the CV). Status: **planned** (reused; base brief: applications/2026-10-25_juicylemons_product-engineer/_work/project-brief-clinical-info-assistant.md). Created for paddy AI Product Engineer (2026-10-29). Time box: 1–2 days with Claude Code.

## Goal
Medicine Q&A web app over public drug label texts with separate professional and patient journeys and cited sources. paddy variant: full-stack TypeScript (Next.js App Router, Drizzle, Zod, Tailwind), Vercel AI SDK for streaming + tool calls through a LiteLLM proxy, pgvector retrieval in Postgres, grounding guardrail that blocks uncited answers, promptfoo eval suite (quality, refusal, cost, latency) in GitHub Actions, OpenTelemetry traces into Arize Phoenix.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Full-stack TypeScript: Next.js, Drizzle, Postgres", "Zod", "Tailwind" | whole app |
| "Vercel AI SDK, promptfoo, LiteLLM, Arize Phoenix, pgVector" | exact stack |
| "Evals, Guardrails und AI Observability ... Qualität, Kosten und Latenz" | promptfoo suite + grounding guardrail + Phoenix traces with cost/latency |
| "End-to-End shippen" | deployed demo (Vercel or Scaleway) |

## Milestones
1. Next.js app + Drizzle schema + pgvector ingestion (5 h) 2. AI SDK chat with citations + guardrail (3 h) 3. promptfoo suite in CI (2 h) 4. Phoenix traces + README (2 h).

## CV bullet it must live up to (German)
- Q&A-Web-App über öffentliche Arzneimittel-Fachinformationen in Full-Stack-TypeScript (Next.js, Drizzle, Zod) mit Vercel AI SDK, LiteLLM und pgVector; Grounding-Guardrail gegen unbelegte Antworten, promptfoo-Evals zu Qualität, Kosten und Latenz in CI und Traces in Arize Phoenix.
