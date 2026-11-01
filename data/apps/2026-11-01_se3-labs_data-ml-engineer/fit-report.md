# Fit report: SE3 Labs, Data and ML Engineer, Munich

**Fit score: 60/100.** Solid on the ML half: models trained and evaluated on real sensor time-series (Covestro prepolymer data: lag/rolling features, RF/XGBoost/LSTM, benchmark vs curve fitting), data pipelines and evaluation datasets (Kniit ingestion/chunking/indexing, ground truth from SAP data; thesis eval pipeline on AWS SQS/Lambda/DynamoDB, 1M+ chunks), fine-tuning (QLoRA, retrieval fine-tuning), PyTorch, MSc AI, coordination with chemists/SAP experts. Weak on the domain half: no 3D computer vision, robotics/UAV sensor data, field data collection or labelling tooling; no C++.

Found by job-scout (LinkedIn 4484468104). English posting, fluent English required, no German requirement → English documents. Munich (SE3 also tests in Erding). Seniority not stated; profile reads junior/mid (Master's or equivalent).

## Requirements → evidence
| Requirement | Evidence | |
|---|---|---|
| Ownership, organising, coordinating people, putting processes in place | Kniit sole developer reporting to CTO; worked with SAP domain experts; Covestro chemists | 🟡 (no formal coordination of data campaigns) |
| Hands-on ML on real-world data, training on practical datasets | Covestro sensor time-series models; Cognizant EV load forecasting | ✅ |
| Data quality / preparation and its effect on models | lag features + rolling windows; ground-truth validation; chunking strategies | ✅ |
| Collect, clean, organise datasets from real-world systems | process sensor data (Covestro), regulatory documents (Kniit), chemist ground truth (thesis) | 🟡 |
| Master's in ML/DS/Robotics/CS | MSc Artificial Intelligence | ✅ |
| Python and/or C++ | Python ✅; C++ ❌ | 🟡 |
| Cross-team requirements, data gaps → collection plans | eval datasets vs ground truth; no field campaigns | 🟡 |
| Sensor integration, field data collection | none (mechanical engineering BTech; publication on autonomous indoor vehicles) | ❌ |
| Bonus: pipelines for training/fine-tuning/eval | thesis eval pipeline, retrieval fine-tuning, QLoRA | ✅ |
| Bonus: robotics, UAV, sensor data | process sensors only | 🟡 |
| Computer vision / perception models (implied by company) | course projects only (CNN/ResNet on MNIST) | ❌ |

## Gaps and honest framing
1. **Computer vision / 3D perception:** no professional work. Course-level CNN/ResNet project (built, linked) + planned dataset/fine-tuning project. Say so.
2. **Robotics/UAV sensor data and field collection:** none; publication on autonomous indoor vehicles and mechanical engineering degree are adjacent. Frame as willing to go to the field.
3. **C++:** none; JD says Python and/or C++.
4. **Defence:** SE3 says defence is a core application; as a non-German (EU Blue Card) citizen a security clearance may be needed or slow. Ask the recruiter.

## Red flags
- Defence domain + possible Sicherheitsüberprüfung for non-German citizens.
- Two SE3 roles prepared in the same run (also Forward Deployed Engineer, Applied AI); decide whether to send one or both. If both are sent, the letters must not repeat the same Covestro/Kniit paragraphs word for word.

## Company hooks
- Spin-out of Daniel Cremers's computer vision group at TUM; co-founders Lukas Köstler, Simon Klenk, Daniel Cremers (TUM press release, 2026-07-06: https://www.tum.de/en/news-and-events/all-news/press-releases/details/how-autonomous-systems-learn-to-understand-their-environment; https://nordic9.com/companies/se3-labs/).
- Came out of stealth in June 2026 with a ~€5.5M seed led by Lakestar (https://thesaasnews.com/news/se3-labs-raises-5-5m-seed). Figures vary across sources: don't quote the amount.
- Product lets operators direct several autonomous systems by voice, hardware-independent (https://sifted.eu/articles/se3-labs-voice-control-drones-lakestar).
- Early customers reportedly include the Bundeswehr; MoU with Hensoldt at ILA 2026 (https://simplify.jobs/c/SE3-Labs). Secondary source: not used in the letter.

## Projects on the CV
- **Road Damage Inference Service**, SE3 variant (planned, reused): dataset store with metadata catalogue, labelling workflow, versioned splits, fine-tuning + per-class evaluation and a data-gap report. Brief: `_work/project-brief-road-damage-inference.md`. Status: build-first.
- **Image classification (CNN, RNN, ResNet)** (built, linked in base profile): real result 93% accuracy.
