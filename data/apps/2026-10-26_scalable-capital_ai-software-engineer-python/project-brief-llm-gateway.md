# Project brief: LLM Gateway, Scalable Capital (AWS + Terraform) variant

Repo slug: `llm-gateway` (no link on the CV). Status: **planned**.
Base brief: `applications/2026-10-14_accenture_junior-applied-ai-engineer/_work/project-brief-llm-gateway.md`. Other variants: REWE digital (GCP/Terraform), Markant (Azure). This file adds an AWS track; one repo, one `infra/aws/` folder.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "integrating modern AI capabilities (via APIs from OpenAI, Anthropic, Google)" | One FastAPI layer over all three via LiteLLM, fallback between providers |
| "architectures for deploying ... scalable AI-enabled solutions on AWS" | ECS Fargate (or Lambda + API Gateway) behind an ALB |
| "Extend our Terraform infrastructure and CI/CD pipelines" | Terraform (aws provider): ECR, ECS service, IAM least privilege, Secrets Manager, CloudWatch log group + dashboard; GitHub Actions plan on PR / apply on main |
| "testing and monitoring components to ensure accuracy, reliability, and performance" | pytest + small golden eval set in CI; per-request latency/token/cost logs to CloudWatch, p95 latency + error/fallback alarms |
| "agentic workflow orchestration frameworks (e.g., LangGraph)" | Example LangGraph client workflow (2 steps + tool) calling the gateway |

## Extra scope (≈1 day on top of the base build)
1. `infra/aws/` Terraform: ECR, ECS Fargate service, task role, Secrets Manager for provider keys, CloudWatch logs/metrics/alarm. (≈3 h)
2. Structured JSON logs → CloudWatch metric filters (latency, tokens, cost, fallback). (≈1.5 h)
3. `examples/langgraph_client.py`: small LangGraph workflow (e.g. summarise a fictional portfolio statement, then draft an explanation) via the gateway. (≈1.5 h)
4. GitHub Actions: tests + eval on PR, `terraform plan` on PR, documented `apply` (free-tier note). (≈1 h)

## Exact CV bullets it must live up to
- Provider-agnostic LLM API layer in Python/FastAPI over OpenAI, Anthropic and Google models via LiteLLM, with token budgets, retries and fallback between providers, and a LangGraph example workflow as client.
- Deployed to AWS (ECS Fargate) with Terraform; per-request latency, token and cost logging in CloudWatch with alarms, pytest and a small eval set in GitHub Actions CI/CD.
