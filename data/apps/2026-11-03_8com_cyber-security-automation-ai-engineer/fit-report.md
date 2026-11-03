# Fit report: 8com Cyber Security, Cyber Security Automation & AI Engineer (m/w/d), Neustadt an der Weinstraße
Source: https://www.linkedin.com/jobs/view/4486827450

**Fit score: 66/100.** Strong match on LLM agents, MCP and Python; gaps in the local-inference toolchain and all the SOAR/security side.

| Requirement | Evidence | |
|---|---|---|
| LLM/agent engineering, MCP, context management | Kniit: LangGraph multi-agent pipeline, MCP query service in Claude Code | ✅ |
| Python, Git, CI/CD, Docker | Kniit, Covestro (GitLab CI/CD, Docker, CDK) | ✅ |
| Local models, fine-tuning, benchmarking | QLoRA fine-tuning (Meme project), embedding benchmark on 1M+ chunks | 🟡 |
| Open WebUI, llama.cpp, vLLM, Mac/Nvidia serving | none in production; planned project only | ❌ |
| Cortex XSOAR, SOAR playbooks, SOC/security background | none | ❌ |
| n8n | none | ❌ |
| German and English "sicher" | German B1, no certificate | 🟡 gap |

## Gaps and framing
- Local inference stack and XSOAR/SOC: stated openly in the letter, framed as quick to learn (Python, APIs, containers are daily work). No claims.
- German: posting is German and asks for safe German; B1 flagged openly in the letter. Documents are German (rule 3, same as earlier German postings). If B2 is a hard requirement, this is the top risk.
## Red flags
- Hardware/infra ops are half the role; no pay range stated.
## Hooks (from the posting only; no web research in this unattended run)
- 8com runs its own AI infrastructure on Apple Mac servers, adding an Nvidia server.
- LLM/agent use cases are internal to the SOC (sensitive data, hence local models).
- SOC with vulnerability management, threat hunting, DFIR; since 2004, clients in 40+ countries.
