# Project brief (variant): Azure Dokumenten-Assistent (adesso Software Engineer Azure AI, Leipzig)

Base: applications/2026-11-02_cgi_azure-cloud-ai-engineer/_work/project-brief-azure-ai-rag-starter-kit.md (slug azure-ai-rag-starter-kit). Only changes listed.

## Why
JD wants Azure AI Services, Azure OpenAI, Document Intelligence, Azure AI Search, Docker, Kubernetes, Azure DevOps, microservices. Work history has none of Azure OpenAI, Document Intelligence, Azure DevOps.

## Changes (about half a day extra)
- Ingest sample PDFs/invoices with Azure AI Document Intelligence (layout/prebuilt model) into chunks; index in Azure AI Search (hybrid + semantic ranking).
- Answers via Azure OpenAI (RAG) behind a FastAPI microservice, Dockerfile.
- Deploy to AKS (small cluster, manifests/Helm) from an Azure DevOps pipeline (build, test, push to ACR, deploy).
- No metrics claims.

## CV bullet it must live up to (exact, German)
Dokumentenverarbeitung mit Azure AI Document Intelligence, Suche in Azure AI Search, Antworten über Azure OpenAI (RAG); FastAPI-Microservice in Docker, per Azure DevOps auf Kubernetes (AKS) bereitgestellt.
