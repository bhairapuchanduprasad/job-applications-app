# Project brief: Ops MCP Server, enmacc variant ("Onboarding & Ops Assistant")
Status: planned. Build before submitting. Base brief: applications/2026-11-04_bloomwell_ai-automation-engineer/_work/project-brief-ops-mcp-server.md
Change vs base: synthetic customer-onboarding records (company, documents, review status) and support tickets in Postgres instead of CRM contacts; a document-check tool with human approval step.
CV bullet to live up to: MCP server in TypeScript (Node.js) with Zod-typed tools over synthetic ticket and customer-record data in Postgres, Slack bot via signed webhooks, human approval before a ticket is drafted, PII masking before model calls, eval set in GitHub Actions.
