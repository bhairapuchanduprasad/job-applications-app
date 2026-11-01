# Application notes: adesso SE, Azure AI Engineer - Agentic Systems (Bremen)

## Likely interview questions
1. "Wie würden Sie ein Multi-Agenten-System für einen Kunden auf dem Azure-Stack aufbauen?" → Kniit architecture (parallel extraction agents + reflection in LangGraph, ground-truth eval), mapped to Azure: Azure OpenAI via Foundry, AI Search for retrieval, MCP tools, App Insights for observability. Be honest that Foundry/Semantic Kernel are new to you; the Starter-Kit project shows them (build it first).
2. "Wie kontrollieren Sie Token-Kosten und Qualität im Betrieb?" → $200k projected LLM budget cut to near zero by moving a high-volume stream to deterministic code; P/R 33/45 → 93/90 against ground truth; RAGAS in the thesis.
3. "Sie haben drei statt fünf Jahre Erfahrung, warum passt die Rolle trotzdem?" → 12 months as sole developer of a production multi-agent system, MCP, agentic coding daily; ask whether a (Senior) Consultant level split exists.

## Form fields
- Warum adesso: agentic solutions on the Microsoft stack for many customers, "Agent in a Day" workshops + building the solutions afterwards; reference architectures.
- Gehaltsvorstellung: 70.000 € brutto/Jahr (range 60–75k).
- Kündigungsfrist / Eintritt: ab 15.11.2026.
- Standort: Bremen (relocating; open to other adesso locations, e.g. Dresden posting is the same JD).
- Deutsch: B1 (no certificate), improving.
- Warum Wechsel: public line from profile (Kniit restructuring before funding round).
