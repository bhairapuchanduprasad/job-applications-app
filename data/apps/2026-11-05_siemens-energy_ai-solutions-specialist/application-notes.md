# Application notes: Siemens Energy
## Likely interview questions
1. How would you support citizen developers who build their own tools? (Expert Interface at Kniit: domain experts approving changes; reusable templates and guardrails.)
2. Tell us about an AI agent you took from prototype to production. (Kniit LangGraph pipeline; Covestro agentic app on AWS.)
3. How do you handle security and data privacy for AI use cases? (Be honest: access control and human approval; no formal governance role yet.)
## Form fields
- Why Siemens Energy: energy domain experience at Kniit, digitalization of the gas turbine fleet, enabling many teams.
- Salary: EUR 60,000 gross/year (large corporate).
- Notice period / start: 15 November 2026. EU Blue Card.

## Application form answers (Siemens Energy portal, 2026-11-05)

**1. Can you describe a business problem you translated into an AI-enabled or digital solution? How did you understand the requirements and decide on the right approach?**

During my time as GenAI Developer (AI Consulting Intern) at Covestro, I worked with business stakeholders whose decisions depended on information spread across internal documents and data. Finding the right information, and summarising it, took a lot of manual effort.

I started by sitting with the stakeholders to understand how they actually made these decisions: which questions came up repeatedly, which sources they trusted, and where time was lost. It became clear that the requests were not all the same. Some needed a precise lookup in internal documents, some needed general reasoning, and some needed a summary of a large amount of text. A single chatbot would have handled all of these the same way and done none of them well.

So I advised an agentic approach. I built an application with LangGraph that first classifies each request and then routes it to the right path: vector-database search for document questions, general LLM inference, or summarisation. I chose this because it matched how the users worked, and each path could be tested and improved separately.

I built it as a React front end with a Python/FastAPI backend, containerised it with Docker, and deployed it to AWS with CDK through GitLab CI/CD, so the business could actually use it rather than see a demo.

**2. Tell us about an AI application, agent, or automation you personally built. Which technologies did you use, how did you connect data and systems, and what did you implement yourself?**

At Kniit, a startup serving the German energy sector, I was the sole developer of an agentic knowledge-extraction pipeline. I owned it end to end and reported directly to the CTO.

The system turns complex regulatory and technical documents into a knowledge graph. I implemented:
- Ingestion and chunking of the source documents, plus all prompt engineering.
- A multi-agent extraction layer in LangGraph: entity-extraction, relationship-analysis, consolidation and reflection agents running in parallel, with LiteLLM as the model gateway. Against ground truth derived from the SAP system, this raised precision from 33% to 93% and recall from 45% to 90%.
- A deterministic, code-based pipeline for a second high-volume source, where rules were more reliable and far cheaper than an LLM.
- Storage in Neo4j for the graph and MongoDB for documents and intermediate results.
- A Model Context Protocol (MCP) service exposing the graph with millisecond retrieval, integrated into Claude Code for our development workflows.
- An Expert Interface: a React front end with Python microservices on Azure, where SAP domain experts validate and approve graph changes before they go live.

Everything ran in Docker on Kubernetes on Azure. Connecting the systems meant clear APIs between each step, so the extraction, the graph, the MCP service and the expert review tool could each change without breaking the others.

**3. Imagine you have built a successful AI prototype that should now be used by a larger business organization. What steps would you take to move from the initial idea to a sustainable enterprise solution?**

1. Confirm the value and the owner. Agree with the business on the problem it solves, how success is measured (time saved, error rate, adoption), and who owns the solution after launch.
2. Measure quality before scaling. Build an evaluation set with the domain experts and test against it on every change. I did this in my Master's thesis at Covestro (RAG evaluation with RAGAS and PytrecEval against chemist-provided ground truth) and at Kniit (precision/recall against SAP-derived data). Without this, nobody can trust the results at scale.
3. Clarify governance, security and data privacy early. Map which data the solution uses, who may see it, and where it is processed. Then align with IT security, data protection and compliance before rollout, not after.
4. Rebuild the prototype for production. Containerise it, use infrastructure as code (I used AWS CDK), add CI/CD, logging, monitoring and cost tracking per use case, and connect to enterprise systems through proper APIs and connectors instead of manual exports.
5. Keep humans in the loop. Where decisions matter, add a review step like the Expert Interface I built at Kniit, so experts can check and correct outputs. This also creates feedback that improves the system.
6. Roll out in stages. Start with a pilot group, collect feedback, fix issues, then expand. Offer short trainings and documentation, and turn common patterns into reusable templates so citizen developers can build similar solutions safely on platforms like Power Platform.
7. Plan the lifecycle. Define who maintains it, how models and prompts are versioned and updated, and how to retire it if the need changes. A solution only stays sustainable if someone is responsible for it after launch.
