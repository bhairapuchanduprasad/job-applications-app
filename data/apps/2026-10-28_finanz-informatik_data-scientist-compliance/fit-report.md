# Fit report: Finanz Informatik, Data Scientist für Compliance (m/w/d), Frankfurt am Main / Münster / Hannover

**Fit score: 60/100.** Solid on Python ML (Random Forest, XGBoost, LSTM, time series), feature engineering, model validation against ground truth, SQL/databases, analysis pipelines; 3 years experience fits "mindestens 2–3 Jahre". Gaps: **PySpark** (named must-have, none in profile), **payments/fraud/compliance domain**, no production ML-model operations in a bank. The recent work is GenAI, not classic DS, so the DS story rests on the Covestro intern + Cognizant roles.

Language: German posting, but no German level stated → English CV + cover letter per CLAUDE.md rule 3 (same call as Heinrich Schmid on 2026-10-27). **Decision for you:** FI is a German bank-IT house; a German Anschreiben could be safer. Found by job-scout (LinkedIn 4484272559). Unit: ZV-Datengetriebene Betrugserkennung. Kennziffer 650/B (enter in the form only, not in the letter).

Not a duplicate: the 2026-10-11 FI application is "AI Engineer / KI-Entwickler" (E 362/B), a different unit. (Today's FI AI Engineer posting 4484271560 is another repost of that one and was skipped.)

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Fachbezogenes Studium + 2–3 J. Erfahrung | MSc AI, 3 yrs | ✅ |
| Python, PySpark, SQL, Analysepipelines | Python + SQL + Pandas pipelines; PySpark none | ✅/❌ |
| Prädiktive ML-Modelle entwickeln, evaluieren, optimieren | Covestro RF/XGBoost/LSTM, Cognizant forecasting | ✅ |
| Konzeption, Validierung, Optimierung datenbasierter Modelle | ground-truth validation at Kniit and Covestro thesis | ✅ |
| Komplexe Datenbankmodelle | Neo4j/MongoDB/Postgres use; no explicit data modelling | 🟡 |
| Große Datenmengen | 1M+ chunk benchmark; not big data/Spark | 🟡 |
| Frameworks, Server, Entwurfsmuster | FastAPI, Docker, K8s, clean code; Entwurfsmuster: no explicit evidence | 🟡 |
| Fraud / compliance (embargo, sanctions) | none | ❌ |
| Kommunikation, Präsentation | stakeholder work at Covestro/Kniit | 🟡 |

## Gaps and honest framing
1. **PySpark:** letter says openly not used in production. Project covers it.
2. **Fraud/compliance domain:** letter says openly; project uses PaySim + EU sanctions list.

## Projects on the CV
- **Payment Fraud Detection Pipeline** (NEW, `planned`). Brief: `_work/project-brief-payment-fraud-detection.md` → build-first.
- **Life Expectancy Analysis** (`built`, original link).

## Red flags
- None. Tarifvertrag, salary by qualification. Department sits in Hannover/Münster/Frankfurt (the AI Engineer post said "ausschließlich Hannover"; check for this unit).

## Company hooks
1. KIXpertS (FI group AI competence centre) feasibility study with Kreissparkasse Köln: AI recognised known fraud cases and cut false alarms vs rule-based systems ([IT Finanzmagazin](https://www.it-finanzmagazin.de/poc-ki-betruegern-auf-der-spur-120410/)). Used.
2. Same source: each flagged transaction is explained by its deviation from typical customer behaviour. Used.
3. SEPA Instant Payments regulation: receiving since Jan 2025, sending since Oct 2025, so screening has to be real-time ([ki-syndikat.de](https://www.ki-syndikat.de/usecases/finanzen/18-ki-zahlungsverkehr-monitoring/)); not used (secondary source).
4. JD: models "präzise, erklärbar und regulatorisch belastbar"; embargo and sanctions screening in scope.
5. Contact: Julia Werner, +49 511 51022 4343, karriere@f-i.de.
