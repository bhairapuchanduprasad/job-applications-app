# Project brief: Product Q&A Assistant (Dr. Theiss variant)

Repo slug: `product-qa-assistant` (no link on the CV)
Status: **planned**. Build before submitting the Dr. Theiss application.
Full brief (scope, architecture, milestones, README outline): `applications/2026-10-17_hotrega_ki-und-prozessmanager/_work/project-brief-product-qa-assistant.md`. Same repo, built once; this file only adds what the Dr. Theiss CV needs.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| "Unterstütze die Fachbereiche bei der Einhaltung regulatorischer Anforderungen (z. B. DSGVO, EU AI Act ...)" | PII redaction before every LLM call, "AI-generated" label, human approval, data-processing + EU AI Act notes in the README |
| "Berate zu Einsatzmöglichkeiten ... von der Bedarfsanalyse bis zum produktiven Einsatz" | README written like a consulting deliverable: problem, before/after process, decision rules, results, limits |
| "Generative AI", "LLMs", "Cloud- oder On-Premise-Umgebungen" | RAG with an LLM API; optional: add a switch to a local open-source model via Ollama (would let you talk about on-premise honestly) |
| "Bereite komplexe ... Themen zielgruppengerecht auf" | One-page summary for decision makers + short demo video for business users |

## Dr. Theiss adaptation (small)
- Use sample data sheets for pharmacy cosmetics / care products (write your own fictional sheets; no real brand content).
- Example questions: "Is the intensive cream suitable for sensitive skin?", "What are the storage conditions?".
- Optional (≈1 h): NIS2 note in the README (logging, access control, incident handling for the workflow), no legal claims.

## Exact CV bullets this project must live up to (German CV)
- KI-Assistent für Produktanfragen: ein n8n-Workflow sortiert eingehende Kunden- und Händler-E-Mails, beantwortet Produkt- und Anwendungsfragen per RAG aus technischen Datenblättern und Sicherheitsdatenblättern und leitet unsichere Fälle zur Freigabe an einen Menschen weiter.
- DSGVO und EU AI Act: personenbezogene Daten werden vor jedem LLM-Aufruf entfernt, Antworten als KI-generiert gekennzeichnet; Prompts und Entscheidungslogik sind versioniert, an einem gelabelten Fragenkatalog getestet und dokumentiert.

When done, mark it `built` in `profile/master-profile.md`; then real results may go on the CV.
