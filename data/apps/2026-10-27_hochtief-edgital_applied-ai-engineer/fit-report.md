# Fit report: HOCHTIEF / EDGITAL, Applied AI Engineer / Machine Learning Engineer (m/w/d), Essen

**Fit score: 62/100.** Solid on Python, PyTorch, Transformers, NumPy, Pandas, Docker, Kubernetes, Azure, Git/CI/CD, productionising AI (Kniit, Covestro). Main gap: **computer vision in production** (only study projects: CNN/ResNet on MNIST) and **Ray Serve** (never used). GitHub (vs GitLab) is a small gap. German: "Gute Deutsch- und Englischkenntnisse" required; B1 is borderline for "gut", flagged.

Language: German posting that requires German → German Lebenslauf + Anschreiben (CLAUDE.md rule 3). Found by job-scout (LinkedIn 4484012786). Location Essen (current city).

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Studium Informatik/Data Science/KI | MSc AI | ✅ |
| Exzellentes Python, Git, CI/CD, Testing | Python 3 yrs, GitLab CI/CD, API tests (Postman) | ✅/🟡 |
| PyTorch, Transformers, NumPy, Pandas | Thesis (PyTorch, HF Transformers, embedding benchmark), DS intern (Pandas, NumPy) | ✅ |
| GitHub | GitHub account with notebooks; daily work was GitLab | 🟡 |
| Docker, Kubernetes, CI/CD | Kniit (Docker, K8s, Azure), Covestro (Docker, GitLab CI/CD) | ✅ |
| CV data/inference/training pipelines | Study CNN/ResNet only | ❌ |
| Ray Serve / distributed AI workloads | none | ❌ |
| Testing + monitoring of AI in production | ground-truth evals; no production monitoring evidenced | 🟡 |
| Azure, Azure DevOps (nice) | Azure yes, Azure DevOps no | 🟡 |
| Gute Deutschkenntnisse | B1 | 🟡 (gap) |

## Gaps and honest framing
1. **Computer vision:** letter says openly it was study projects only; project brief adds a road-damage CV pipeline.
2. **Ray Serve:** letter says not used yet; the project covers it.
3. **German B1:** stated openly; German documents written.

## Projects on the CV
- **Road Damage Inference Service** (NEW, `planned`): PyTorch fine-tune on public road damage images (RDD2022), Ray Serve on Kubernetes, GitHub Actions. Brief: `_work/project-brief-road-damage-inference.md`. → build-first. This project is close to EDGITAL's product; building it is the strongest move for this application.
- **Image Classification (CNN/RNN/ResNet)** (`built`, original link).

## Red flags
- None. Spin-off of a large group ("Startup-Dynamik und Sicherheit eines Konzerns"); salary not stated.

## Company hooks
1. EDGITAL (HOCHTIEF spin-off) captures street images with a vehicle-mounted smartphone/camera; AI rates road condition, combined with usage data into urgency classes for maintenance planning ([ms-aktuell Münster](https://ms-aktuell.de/muenster/muenster-testet-erstmals-ki-gestuetzte-strassenerfassung-zur-effizienten-instandhaltung/)).
2. Rhede (Ems), ~200 km network, uses it; fewer on-site visits ([kommunal.de](https://kommunal.de/digitalisierung-im-strassenmanagement-rhede-ems-grundlage-fuer-eine-effiziente-budgetplanung)).
3. Innovation partnership with the city of Herne since 2023 ([Presseportal PDF](https://www.presseportal.de/download/document/641aede7270000fd2caf2f65-20230322-pm-digitale-ncheck-herne-de.pdf)).
4. Münster tests it in the research project "KI in der Straßenerhaltung" (same ms-aktuell source).
5. Contact named in the JD: Damian Knaak.
