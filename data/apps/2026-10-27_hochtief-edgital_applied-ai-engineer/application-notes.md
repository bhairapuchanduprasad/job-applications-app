# Application notes: HOCHTIEF / EDGITAL, Applied AI Engineer / ML Engineer, Essen

Status: **build-first** (build Road Damage Inference Service: brief `_work/project-brief-road-damage-inference.md`; or remove it from the CV).
Apply via: HOCHTIEF online form (LinkedIn https://www.linkedin.com/jobs/view/4484012786). Contact: Damian Knaak.
ATS coverage: 83%. Gaps: computer vision in production, Ray Serve, Azure DevOps, German (B1 vs "gut").

## Likely interview questions
1. **"How would you take a CV model into production on Kubernetes?"** Containerised service, versioned model artefact, batch inference endpoint, autoscaling replicas (Ray Serve), latency/throughput + prediction distribution monitoring, tests in CI. Point to Kniit K8s/Azure + the road-damage project once built.
2. **"You haven't done computer vision in production. Why you?"** PyTorch/Transformers experience from the thesis, the full train-evaluate-deploy loop done several times, ground-truth evaluation discipline (Kniit P/R 33/45 → 93/90), and the road-damage project.
3. **"How do you test and monitor an AI system?"** Ground-truth sets, per-class metrics, regression tests in CI, drift in prediction distribution, human review of edge cases.

## Form answers
- **Warum EDGITAL:** KI löst ein greifbares Problem für Kommunen (Straßenzustand, Instandhaltungsplanung); Produkt in Essen.
- **Gehaltsvorstellung:** 70.000 € brutto/Jahr (Spanne 60.000–75.000 €).
- **Kündigungsfrist / frühester Start:** 15. November 2026.
- **Arbeitserlaubnis:** Blaue Karte EU.
- **Deutsch:** B1 (ohne Zertifikat).
- **Wechselgrund (DE):** "Kniit ist ein Start-up in der Frühphase, das sich vor der Finanzierungsrunde mit einer SAP-Senior-Rolle neu aufgestellt hat; meine Position endete, nachdem ich die Wissensextraktions-Pipeline vollständig aufgebaut und übergeben hatte."
