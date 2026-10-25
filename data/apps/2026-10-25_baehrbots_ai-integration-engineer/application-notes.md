# Application notes: BaehrBots GmbH, AI Integration Engineer / Specialist (Dresden)

Status: build-first. Build `ops-mcp-server` (BaehrBots variant, see `project-brief-ops-mcp-server.md`) before submitting; send it as the work sample the posting asks for. Cover letter is optional for them, but send it.

## Likely interview questions
1. **"Einer unserer Agenten meldet Erfolg, aber das Ergebnis fehlt. Wie gehen Sie vor?"**
   Check the output itself, not the status: compare against expected data, look at logs/traces of the tool calls, add a content-level check to the eval set so it can't pass silently again. Kniit example: reflection agent + evaluation against SAP-derived ground truth (33/45 → 93/90 precision/recall).
2. **"Wie senken Sie LLM-Kosten, ohne Qualität zu verlieren?"**
   First ask whether an LLM is needed at all: at Kniit a deterministic pipeline replaced LLM calls for a high-volume stream and cut a $200k projected budget to near zero. Then: smaller/cheaper models via LiteLLM routing, caching, prompt size, measuring quality with evals before and after a model switch.
3. **"Wie würden Sie eine Automation, die auf einem Laptop läuft, auf unsere Server bringen?"**
   Git repo + PR review, Docker image, systemd unit or compose with restart policy, secrets out of the repo in a restricted env file or secret store, least-privilege tokens, logs + a simple health check and alert. Be honest: Docker/Kubernetes/CI/CD from Kniit and Covestro; systemd from the Ops MCP Server project only.
- Also prepare: German level (B1, learning; English with the international team), MCP server design at Kniit, how to keep humans in control of trading/payments (approval step like Expert Interface).

## Form answers
- **Why BaehrBots?** You build and run your own agents on your own servers and measure autonomy instead of claiming it. I want to make Moneypenny, Rockefeller and Columbo more reliable and give the team measurable hours back, and I already know the energy sector from Kniit.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000). Check the Blue Card threshold.
- **Notice period / earliest start:** available from 15 November 2026.
- **Work authorization:** EU Blue Card (Germany), no sponsorship needed.
- **Location:** will be based in Dresden.
- **German:** B1 (no certificate), improving.
