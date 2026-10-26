# Application notes: INSTATIQ, Applied AI Engineer (Stuttgart)

Status: **build-first**. Build `plant-maintenance-agent` (brief in this folder) before submitting; the CV describes it.
Submit via the LinkedIn posting: https://www.linkedin.com/jobs/view/4481098986 (German documents; JD asks for salary + earliest start, both in the Anschreiben).

## Likely interview questions
1. **"Wie würden Sie Predictive Maintenance für den P1 angehen?"** Start with the data: which sensors the pump and boom already log (pressure, oil temperature, vibration, boom angles), how faults are recorded today. Baseline with rolling features + Isolation Forest, then a supervised model once labelled faults exist; time-based evaluation, false-alarm cost agreed with service. Same method as the Covestro off-spec batch detection (lag features, rolling windows, benchmark vs the existing approach). Mention the planned project once it is built.
2. **"Ihr Deutsch ist B1. Wie arbeiten Sie mit unseren Maschinen-Softwareentwicklern?"** Honest: B1 now, actively improving; technical work and documentation in English works today; everyday team communication in German improves fast with daily use. Be ready to answer this one in German.
3. **"Wie entscheiden Sie, ob ein AI-Use-Case sinnvoll ist?"** Kniit: chose a deterministic pipeline over an LLM for the high-volume stream ($200k projected LLM budget → near zero). Covestro AI consulting: analysed stakeholders' decision workflows before building. Criteria: value, data availability, measurable target, cost per run, risk.

Also prepare: steering external AI partners (no direct experience; how you would write specs, acceptance tests, eval sets), IT/OT integration (no OT experience; OPC UA basics), why leave Kniit (public line in profile).

## Form fields
- **Why INSTATIQ:** AI on a real machine on the construction site; the P1 (truck-mounted concrete pump base, bauma 2025) produces sensor data that suits anomaly detection and operator assistance; Mechanical Engineering bachelor + AI master fits that mix.
- **Gehaltsvorstellung:** 70.000 € brutto/Jahr (range 60–75k).
- **Frühester Eintritt / Kündigungsfrist:** 15. November 2026 (current role ends 13 Nov 2026).
- **Arbeitserlaubnis:** Blaue Karte EU, no sponsorship needed.
- **Wohnort:** will be based in Stuttgart; open to Mobile Office.
- **Deutsch:** B1 (no certificate).
