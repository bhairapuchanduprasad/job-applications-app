# Project brief (variant): Azure AI Agent Starter-Kit (adesso Azure AI Engineer - Agentic Systems)

Base brief: applications/2026-10-25_hamburger-energienetze_azure-devops-engineer-ai/_work/project-brief-azure-ai-rag-starter-kit.md (repo slug azure-ai-rag-starter-kit). This file lists only the changes.

## Why for this JD
adesso wants agentic solutions on the Azure AI stack (Azure OpenAI, Azure AI Foundry/Microsoft Foundry, Azure AI Search), MCP integration, LLMOps (prompt management, versioning, observability, token cost control), IaC + CI/CD in the Microsoft world, and reference architectures. The work history has none of Azure OpenAI/Foundry/Terraform.

## Changes (about half a day extra)
- Deploy the chat + embedding models via Microsoft Foundry (project + Azure OpenAI deployments) in Terraform.
- Add a second agent (e.g. "document checker") exposed through an own MCP server (FastMCP) that the knowledge assistant calls as a tool; optionally orchestrate with Semantic Kernel to cover the JD framework.
- Prompts stored as versioned files with a version id logged per request; token usage and cost per request to Application Insights (custom metrics) + a small cost dashboard query.
- RAGAS evaluation as a quality gate in the Azure DevOps pipeline (as in base brief).

## CV bullet it must live up to (exact, German)
- Referenzarchitektur für einen Wissensassistenten mit RAG und einem zweiten Agenten über einen eigenen MCP-Server: Terraform und Azure-DevOps-Pipelines stellen Azure OpenAI, Azure AI Search und Key Vault bereit (Entra ID, Managed Identity); Prompt-Versionierung, Token-Kosten-Logging, Application Insights und RAGAS-Evaluation als Quality-Gate.
