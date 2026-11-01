# Project brief: Road Damage Inference Service, SE3 Labs variant ("Road Damage Dataset & Model Pipeline")

Repo slug: `road-damage-inference` (same repo as the HOCHTIEF/EDGITAL version; no link on the CV)
Status: **planned**. Build before submitting the SE3 Labs Data and ML Engineer application.
Time box: 1–2 days with Claude Code. Base brief: applications/2026-10-27_hochtief-edgital_applied-ai-engineer/_work/project-brief-road-damage-inference.md (training + eval part is shared; Ray Serve/Kubernetes part is optional here).

## Goal
Show the data side of ML on real-world recordings: a shared data store with a metadata catalogue, cleaning, a repeatable labelling workflow, versioned dataset splits, then fine-tuning + evaluation that feeds back into a data-gap report ("what to collect next").

## Why it matters for this JD
| JD phrase | Covered by |
|---|---|
| Shared data store, organised, categorised, easy to find and reuse | `ingest.py` → Parquet/DuckDB catalogue (source, country, camera, time of day, weather if derivable, resolution, label status) + `query_catalog.py` |
| Data preparation & labelling workflows | Label Studio project config + import/export scripts; label QA checks (empty boxes, class balance, near-duplicates via perceptual hash) |
| Pipeline from collection to usable data | `make data`: ingest → clean → dedupe → label export → versioned splits (DVC) |
| ML training & fine-tuning on real-world data | Fine-tune pretrained torchvision model (classification of damage type per image/tile, or Faster R-CNN detection) |
| Evaluation, data gaps | Per-class and per-condition (country/camera) precision/recall; `gap_report.md` ranks slices by error and sample count |
| Building for reuse | Dataset card + model card; catalogue lets others pull a subset by query |
| Python and/or C++ | Python |

## Scope
In: RDD2022 subset (a few thousand images, 2–3 countries as "recording conditions"); DuckDB catalogue; Label Studio (local Docker) for relabelling a small sample; DVC with a local remote; PyTorch fine-tune; eval + gap report; pytest for data checks; GitHub Actions (lint, tests, tiny smoke train).
Out: real sensor/UAV data, GPU cluster, 3D, serving (optional from base brief).

## Architecture
```
raw images + annotations ─► ingest.py ─► catalogue (DuckDB/Parquet) ─► clean/dedupe ─► Label Studio (sample relabel)
                                                                         └─► splits (DVC versioned) ─► train.py ─► eval.py ─► metrics per class/slice ─► gap_report.md
```

## Milestones
1. Ingest + catalogue + dedupe (half day).
2. Label Studio round trip + label QA checks (2–3 h).
3. DVC splits + fine-tune + eval per slice (half day).
4. Gap report, dataset/model cards, CI, README (2–3 h).

## README outline
Problem · Data source & licence · Catalogue schema · Labelling workflow · Dataset versions · Results table (real numbers only after running) · Data-gap report · Limits/next steps (sensor/UAV data, active learning).

## Demo idea
Query the catalogue ("all images from country X without labels"), open them in Label Studio, re-run `make train`, show the gap report changing.

## CV bullets it must live up to
- Data pipeline for real-world street images (public RDD2022): shared data store with a metadata catalogue, cleaning, a repeatable labelling workflow in Label Studio and versioned dataset splits with DVC.
- Fine-tunes a pretrained PyTorch computer vision model, evaluates precision/recall per class and recording condition, and reports data gaps that guide the next data collection.
