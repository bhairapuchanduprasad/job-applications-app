# Project brief: Customer Service Assistant on AWS (variant of IT-Ticket-Assistent) — status: planned
Base brief: applications/2026-10-21_bedrock-projekt_python-genai-developer/_work/project-brief-it-ticket-assistant-bedrock.md. Build that, with a customer-service domain and a Lex front.
## Why for Slalom: Bedrock, Lex, Lambda, DynamoDB, "AWS AI services for customer service"; Amazon Connect is out of scope (optional: contact flow calling the Lex bot).
## Scope (1–2 days): Lex bot (intents: order status, return, FAQ, human handoff) → Bedrock Agent + Knowledge Base over synthetic FAQ docs; Lambda action groups reading/writing tickets and orders in DynamoDB; Guardrails (PII masking); handoff with conversation summary; AWS CDK; unit + integration tests in CI.
## Stack: Bedrock, Lex V2, Lambda (Python), DynamoDB, S3, CDK, GitHub Actions.
## CV bullet it must live up to: "Lex bot hands requests to a Bedrock Agent with a Knowledge Base over FAQ documents; Lambda actions read and write ticket data in DynamoDB, Guardrails mask personal data, deployed with AWS CDK."
## Milestones: CDK skeleton + DynamoDB; Knowledge Base; agent + Lambda actions; Lex bot; Guardrails + handoff; tests/CI; README + demo.
