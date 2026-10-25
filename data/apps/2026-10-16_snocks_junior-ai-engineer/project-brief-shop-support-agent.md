# Project brief: Shop Support Agent

Repo slug: `shop-support-agent` (no link on the CV, per your rule)
Status: **planned**. Build before submitting the SNOCKS application.
Time box: 1–2 days with Claude Code.

## Goal
An internal AI automation for an online shop: an agent reads incoming customer-service tickets ("where is my order?", "I want to return this"), looks up the real order in Shopify through an MCP server, and drafts a reply that a human approves before it is sent. A scheduled job loads orders and tickets into a BigQuery data warehouse and builds a weekly support report. A labelled ticket set measures reply quality, cost per ticket and latency on every CI run.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "AI-Automationen für interne Prozesse wie Customer Service … Reporting, vom Prototyp bis in den produktiven Betrieb" | Ticket-reply agent + weekly report job, deployed as a container |
| "Systeme über APIs (z. B. Shopify, Zendesk …) verbinden, an das Data Warehouse anbinden, Daten den AI Agents zur Verfügung stellen" | Shopify Admin API → MCP server → agent; orders + tickets → BigQuery |
| "BigQuery oder vergleichbares Cloud Data Warehouse", "Google Cloud" | BigQuery sandbox (free), Cloud Run |
| "Claude/OpenAI APIs, Agents, MCP, Claude Code" | Claude API agent with MCP tools, built with Claude Code |
| "testest die Ergebnisse systematisch und verbesserst sie messbar in Qualität, Kosten und Latenz" | Labelled ticket set (20–30 tickets) scored in CI: correctness of order facts, tone check, cost/ticket, p50/p95 latency |
| "Container und CI/CD", "Shopify ist ein Plus" | Dockerfile, GitHub Actions or GitLab CI, Shopify dev store |
| "Enablement … dokumentierst Ergebnisse" | README written for a non-technical support lead |

## Scope (keep it small)
In:
- Shopify **development store** (free via a Shopify Partner account) with ~20 sample orders.
- Ticket source: a JSON/CSV file of sample tickets (Zendesk-like fields). Optional: Zendesk trial API.
- MCP server (Python) with tools: `get_order(order_number|email)`, `get_fulfillment_status`, `get_return_policy`.
- Agent (Claude API) that classifies the ticket, calls the MCP tools, drafts a reply, and marks uncertain cases "needs human".
- Approval step: a minimal Streamlit page listing drafts with approve/edit/reject.
- Python job: load orders + tickets into BigQuery (sandbox); SQL view for the weekly report (volume, reasons, share answered by the agent, approval rate).
- Eval: labelled ticket set; checks that the draft names the correct order status/tracking, flags returns correctly, stays under a length limit; logs tokens, cost and latency per ticket.
- Dockerfile, CI running tests + eval; deploy to Cloud Run (free tier) or just document the deploy command.
Out: sending real emails, auth, multi-brand config.

## Architecture
```
tickets.json ─► agent (Claude API) ──tools──► MCP server ──► Shopify Admin API (dev store)
                    │
                    ├─► drafts ─► Streamlit approval page
                    └─► run log (tokens, cost, latency, eval tag)
loader job ─► BigQuery (orders, tickets, run log) ─► SQL view ─► weekly support report
CI: pytest + eval on labelled tickets ─► pass rate, cost/ticket, p95 latency
```

## Milestones
1. Shopify dev store + sample orders; MCP server with 3 tools. (≈3 h)
2. Agent: classify → tool calls → draft; "needs human" path. (≈3 h)
3. Labelled tickets + eval script; cost/latency logging. (≈2 h)
4. BigQuery loader + report view. (≈2 h)
5. Streamlit approval page. (≈1.5 h)
6. Docker, CI, README, screenshots. (≈1.5 h)

## README outline
Problem (support team answering the same order questions) → Architecture → How the agent decides when to hand over to a human → Eval results (quality, cost/ticket, latency) → Weekly report screenshot → "How I used Claude Code" → Run locally → Limitations.

## Demo idea
Feed 20 tickets, show the drafts with real order data, approve a few, then open the BigQuery report and the CI eval summary.

## CV bullets this project must live up to
- AI agent that drafts replies to customer service tickets (order status, returns) from live order data in the Shopify Admin API, exposed to the agent through an MCP server, with a human approval step before anything is sent.
- Scheduled Python job loads orders and tickets into a BigQuery data warehouse and builds a weekly support report; a labelled ticket set tests reply quality, cost per ticket, and latency in a CI/CD pipeline, packaged with Docker for Google Cloud Run.

If something is cut while building, update these bullets in `_work/cv.tex`. When done, mark it `built` in `profile/master-profile.md`; then real numbers (eval pass rate, cost per ticket) may go on the CV.
