# Application notes: Navan, Backend Software Engineer (Expense), Berlin

Before submitting: build Expense Missing-Info Agent (_work/project-brief-expense-missing-info-agent.md) or remove the Projects section; the CV claims Java/Spring Boot, provider failover and prompt-injection tests from it.

## Likely interview questions
1. How would you improve receipt extraction quality while controlling cost and latency?
   → Kniit: measured P/R against SAP ground truth (33/45 → 93/90); deterministic path for the high-volume stream ($200k → near zero); model only where language needs it.
2. How do you stop an agent from making unsafe writes?
   → Expert Interface: domain experts approve graph changes before they are written; tools exposed via MCP with narrow scope; would add write-only-empty-fields + audit log.
3. You have not used Java. How do you ramp up?
   → Python backends (FastAPI, microservices, AWS CDK); learn via code review and small shipped changes; AI tools to read unfamiliar services.

## Form answers
- Why Navan: Expense Chat (March 2026) and admin agents in production; EMEA spend (VAT, per diem) is the harder version of the problem.
- Salary: €60,000–75,000 gross/year; single number €70,000.
- Notice/start: 15 November 2026. EU Blue Card, no sponsorship needed.
