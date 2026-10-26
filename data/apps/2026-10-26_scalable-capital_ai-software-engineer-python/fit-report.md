# Fit report: Scalable Capital, AI Software Engineer – Python (m/f/x), Berlin or Munich

**Fit score: 72/100.** Strong on the core of the role (Python AI/LLM services, LangGraph agentic workflows, AWS with IaC via CDK, Docker, CI/CD, evaluation/testing of LLM outputs). Gaps: Terraform (you have AWS CDK, not Terraform), "several years" of professional Python (3 years incl. internships/thesis), production monitoring of AI systems, fintech domain.

Language: English posting, no German requirement → English CV + cover letter. Listed twice (Berlin 4482981150, Munich 4483546505); one application covers both, CV header uses Berlin (first listing). Pick the city when submitting; change `\location` + letter if you prefer Munich (`scripts/rebuild.sh`).

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Develop/maintain AI/LLM services with SE best practices | Kniit: sole developer of LLM extraction pipeline + MCP service, Python microservices; Covestro: FastAPI backend | ✅ |
| Architectures for scalable AI solutions on AWS | Covestro: Docker + AWS CDK (EC2, Lambda), Lambda/SQS/DynamoDB eval infra | ✅ |
| Extend Terraform + CI/CD | GitLab CI/CD yes; IaC via AWS CDK, **no Terraform** | 🟡 |
| Testing + monitoring for accuracy, reliability, performance | RAGAS/PytrecEval eval, P/R tracking 33/45 → 93/90, API tests with Postman; no production monitoring stack | 🟡 |
| LangGraph agentic workflows | Kniit multi-agent LangGraph; Covestro agentic router | ✅ |
| Integrate LLM APIs (OpenAI, Anthropic, Google) | LiteLLM (provider-agnostic), Claude Code; MCP | ✅ |
| Several years professional Python | 3 years (Kniit, Covestro x3, Cognizant) | 🟡 |
| Docker, CI/CD, version control | Docker, Kubernetes, GitLab CI/CD | ✅ |
| Generalist: infra + backend | Kniit end-to-end owner (ingestion → React app on Azure) | ✅ |
| Fintech / banking | None | 🟡 |

## Gaps and honest framing
1. **Terraform:** say IaC experience is AWS CDK; Terraform is the same model. Planned project LLM Gateway (AWS/Terraform variant) closes it on paper; build first.
2. **Monitoring:** describe evaluation discipline; project adds latency/cost logging + CloudWatch.
3. **Seniority:** "Mid-Senior" label; 3 years is the honest number; stress ownership (sole developer).

## Project on the CV
Reused planned **LLM Gateway** with a Scalable/AWS variant brief (`project-brief-llm-gateway.md`): Terraform on AWS (ECS Fargate or Lambda, Secrets Manager, CloudWatch), OpenAI + Anthropic + Google via LiteLLM. Status planned → **build-first**.

## Red flags
- Seniority label Mid-Senior; "several years" Python. Moderate risk.
- Regulated bank (full banking licence): expect security/compliance questions.

## Company hooks (research 2026-10-26)
1. 25 Aug 2026: Scalable opened customer accounts to ChatGPT, Claude and Grok, which can analyse portfolios, manage watchlists/alerts/savings plans and prepare orders; trades still need manual confirmation. Called a first for a European bank; >1M clients, >€60bn assets (Reuters via [WHBL](https://whbl.com/2026/08/24/german-broker-scalable-opens-investment-platform-to-major-ai-chatbots/), [capitalo](https://www.capitalo.de/anbieter/scalable-capital/news/scalable-capital-depot-agentic-investing)).
2. Earlier: in-app AI assistant ([GIGA](https://www.giga.de/tech/scalable-ki-assistent-das-kann-das-novum-beim-beliebten-neobroker--01K3650ZPB9P30X63GPTV9QQRG)).
3. From the JD: new AI work stream in the Data Science team; not training models, integrating OpenAI/Anthropic/Google APIs; AWS + Terraform; LangGraph.
