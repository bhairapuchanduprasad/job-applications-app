# Project brief: IT-Ticket-Assistent (Amazon Bedrock)

Repo slug: `it-ticket-assistant-bedrock` (no link on the CV, per your rule)
Status: **planned**. Build before submitting (or at least before the first interview: Bedrock is a must-have).
Time box: 1–2 days with Claude Code. AWS free tier + Bedrock pay-per-token (a few euros); enable model access in eu-central-1.

## Goal
An AI assistant for IT operations: incoming incident tickets are classified by a **Bedrock Agent**, which searches matching solutions in runbooks via a **Bedrock Knowledge Base** and proposes an answer that a person approves. **Bedrock Guardrails** filter personal data; access only via IAM roles; every answer logged. Unit and integration tests in CI; deployment with AWS CDK (you already know CDK); an operations manual (Betriebshandbuch) as documentation.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Praktische Erfahrung mit Amazon Bedrock" (Muss) | Bedrock models, Bedrock Agents, Knowledge Bases, Guardrails |
| "Agenten-Frameworks (z. B. LangChain, Bedrock Agents)" | Bedrock Agent with action groups (Lambda) |
| "Prompt Engineering" | Versioned agent instructions + classification prompts, tested |
| "Datenschutz/Informationssicherheit bei KI-Verfahren (hoher Schutzbedarf)" | Guardrails PII filters, least-privilege IAM, CloudWatch audit log, no data leaves eu-central-1 |
| "Unit-/Integrationstests, Qualitätssicherung" | pytest unit tests (mocked Bedrock via botocore Stubber), integration tests against a dev stack, eval set |
| "Dokumentation (technische Doku, Betriebshandbuch)" | README + `docs/betriebshandbuch.md` (deploy, monitoring, rollback, incident steps) |
| "KI zur Automatisierung und Qualitätsverbesserung in IT-Prozessen" | Ticket triage and answer drafting for IT operations |

## Scope
In:
- 15–20 synthetic IT tickets (password reset, VPN, printer, disk full, application error) + 8–10 runbook pages (markdown → S3).
- Bedrock Knowledge Base over the runbooks (S3 + OpenSearch Serverless or the cheaper vector option).
- Bedrock Agent: instructions + action group (Lambda) `classify_ticket`, `lookup_runbook`, `propose_answer`; returns "needs human" when unsure.
- Guardrail: PII (names, emails, phone, IPs) masked; denied topics.
- FastAPI or Lambda endpoint `/tickets/{id}/suggest`; approval flag stored in DynamoDB.
- CDK stack for all of it; GitHub Actions/GitLab CI: lint, unit tests, integration test on a dev stack.
- Eval: labelled tickets → category accuracy + "correct runbook cited" rate.
- Docs: architecture, data protection notes, Betriebshandbuch.
Out: real ticket system integration, UI beyond a minimal page.

## Architecture
```
ticket ─► API (Lambda/FastAPI) ─► Bedrock Agent ─► action group Lambda (classify, lookup, propose)
                                      │                 └► Bedrock Knowledge Base (runbooks in S3)
                                      └► Guardrail (PII masking, denied topics)
                         ─► suggestion + sources ─► DynamoDB (status: pending/approved) ─► human approval
CloudWatch logs (audit) · IAM least privilege · CDK · CI: unit + integration tests + eval
```

## Milestones
1. Tickets + runbooks; S3 + Knowledge Base via CDK. (≈2.5 h)
2. Agent + action group Lambda. (≈3 h)
3. Guardrail + IAM + logging. (≈1.5 h)
4. API + DynamoDB approval flow. (≈1.5 h)
5. Tests (unit with Stubber, integration) + eval + CI. (≈2.5 h)
6. Docs: README, data protection notes, Betriebshandbuch. (≈1 h)

## CV bullets this project must live up to (German CV)
- KI-Assistent für IT-Betriebsprozesse: ein Bedrock Agent klassifiziert eingehende Störungstickets, sucht passende Lösungen in Runbooks über eine Bedrock Knowledge Base und schlägt eine Antwort zur Freigabe durch einen Menschen vor.
- Datenschutz und Informationssicherheit bei hohem Schutzbedarf: Bedrock Guardrails filtern personenbezogene Daten, Zugriff nur über IAM-Rollen, Protokollierung jeder Antwort; Unit-Tests und Integrationstests in einer CI/CD-Pipeline, Deployment mit AWS CDK, Betriebshandbuch als Dokumentation.

When done, mark it `built` in `profile/master-profile.md`; then real results may go on the CV.
