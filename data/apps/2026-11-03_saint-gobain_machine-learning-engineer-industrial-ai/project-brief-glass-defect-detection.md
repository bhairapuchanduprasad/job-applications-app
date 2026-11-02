# Project brief: Glass/Surface Defect Detection (Road Damage Inference Service variant)
Repo slug: glass-defect-detection. Status: planned. For: Saint-Gobain ML Engineer Industrial AI (2026-11-03).

## Goal
Image-based quality inspection on public industrial surface-defect data, plus a process-data model, from data analysis to a containerised inference service.

## Why for this JD
Proves computer vision (Bilddaten), quality inspection (Qualitätsprüfung), PyTorch, scikit-learn, data quality checks, prototype evaluation, Docker, CI/CD, light MLOps (MLflow).

## Scope (1–2 days)
- Data: MVTec AD (glass-like categories: e.g. bottle, tile) or NEU surface defects; data quality report (class balance, duplicates, blur).
- PyTorch: fine-tune a pretrained ResNet/EfficientNet; per-class precision/recall, confusion matrix, threshold for "send to manual check".
- scikit-learn baseline on simple image features for comparison.
- MLflow tracking + model versioning.
- FastAPI inference service in Docker; pytest + GitHub Actions.
- Short value note: false-reject vs. missed-defect trade-off.

## Milestones
1. Data + quality report. 2. Baseline + CNN. 3. Evaluation + threshold. 4. MLflow + API + Docker. 5. CI + README.

## Demo
Upload an image → defect class + confidence + "manual check" flag.

## CV bullet it must live up to
- Bildbasierte Qualitätsprüfung auf öffentlichen industriellen Oberflächenfehler-Daten: Fine-Tuning eines vortrainierten CNN mit PyTorch gegen eine scikit-learn-Baseline, Datenqualitätsprüfung, Precision/Recall pro Fehlerklasse, MLflow-Tracking und FastAPI-Inferenzdienst im Docker-Container mit CI/CD in GitHub Actions.
