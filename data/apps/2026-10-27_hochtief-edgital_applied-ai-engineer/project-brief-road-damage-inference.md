# Project brief: Road Damage Inference Service

Repo slug: `road-damage-inference` (no link on the CV)
Status: **planned**. Build before submitting the HOCHTIEF / EDGITAL Applied AI Engineer application.
Time box: 1–2 days with Claude Code.

## Goal
A small but production-shaped computer-vision service: a PyTorch model that detects/classifies road damage (cracks, potholes) in dash-cam style street images, with a training pipeline, an inference service on Kubernetes with Ray Serve, tests, CI/CD and basic monitoring.

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| Integration und Produktivsetzung moderner KI-Modelle | Model packaged and served behind an HTTP API, versioned model artefact |
| Daten-, Inferenz- und Trainingspipelines für Computer Vision | `prepare_data.py` → `train.py` (PyTorch, torchvision or Hugging Face Transformers image model) → `evaluate.py` |
| Kubernetes und Ray Serve | Ray Serve deployment on a local kind/minikube cluster (KubeRay operator or `serve run` in a pod), autoscaling replicas config |
| Testing und Monitoring von KI-Systemen | pytest (data checks, model I/O shape, API contract), latency/throughput logging, prediction distribution check |
| Git, GitHub, CI/CD | GitHub Actions: lint + tests + small smoke-train on a tiny subset + Docker image build |
| PyTorch, Transformers, NumPy, Pandas | Training code; Pandas for label tables / eval reports |
| Nice: Azure / Azure DevOps | Optional: README section on running the same image on AKS |

## Scope
In:
- Public dataset: RDD2022 (Road Damage Dataset, crowdsensing street images) subset, or a few hundred images; classification (damage type per image/tile) or detection with a pretrained torchvision Faster R-CNN / a Hugging Face ViT/DETR fine-tune. Keep it small: fine-tune a pretrained backbone.
- `train.py` with config (YAML), seed, metrics per class (precision/recall/F1, confusion matrix) saved as JSON/CSV.
- Inference: batch endpoint (`POST /predict` with images) via Ray Serve; Docker image; Kubernetes manifests (kind) + README commands.
- Monitoring: request latency, images/s, per-class prediction counts logged; simple Grafana-free report script.
- GitHub Actions CI.
Out: real EDGITAL data, GPU cluster, labelling tool, UI.

## Architecture
```
images ─► prepare_data.py ─► train.py (PyTorch) ─► model.pt + metrics.json
                                                   │
client ─► Ray Serve deployment (K8s, Docker) ─► preprocess ─► model ─► damage classes + scores
                                   └─► logs: latency, throughput, class counts
```

## Milestones
1. Data subset + loader + baseline fine-tune (half day).
2. Eval report + tests (2 h).
3. Ray Serve app + Dockerfile + kind manifests (half day).
4. GitHub Actions + README + monitoring script (2 h).

## README outline
Problem · Dataset (license) · Model + results table (real numbers only after you run it) · Serving on Kubernetes with Ray Serve · Tests/CI · Limits · Next steps (AKS, active learning).

## Demo idea
`kubectl port-forward` + `curl` with three street images; show predicted damage classes and latency log.

## CV bullets it must live up to (German CV)
- Computer-Vision-Pipeline mit PyTorch: Feinabstimmung eines vortrainierten Bildmodells zur Erkennung von Straßenschäden (Risse, Schlaglöcher) auf öffentlichen Straßenbildern, mit Trainings- und Evaluierungspipeline (Precision/Recall pro Klasse).
- Inferenzservice mit Ray Serve auf Kubernetes (Docker), pytest-Tests und GitHub Actions CI/CD, Logging von Latenz, Durchsatz und Vorhersageverteilung für das Monitoring.
