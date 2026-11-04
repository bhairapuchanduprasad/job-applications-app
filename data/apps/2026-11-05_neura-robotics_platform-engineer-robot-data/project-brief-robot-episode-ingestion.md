# Project brief: Robot Episode Ingestion Pipeline
**Goal:** small Python service + CLI that ingests multi-modal recording episodes, validates them, compresses video, and uploads training-ready episodes to S3.
**Proves (JD):** PyAV/FFmpeg, H.264/AV1, edge-to-cloud ingestion, data validation, Terraform, Docker, CI/CD, CLI tools, ML-ready data formats.
**Scope (1-2 days):** use a public robot dataset (e.g. a LeRobot or Open X-Embodiment sample) as the "recording"; no real hardware.
**Stack:** Python, PyAV/FFmpeg, Parquet/NumPy for joint states, boto3, Terraform (S3 + IAM), Docker, GitHub Actions, pytest, Typer CLI.
**Architecture:** CLI `ingest <episode_dir>` -> validator (frame drops, timestamp drift, missing modalities) -> transcoder (H.264, optional AV1) -> manifest (JSON: modalities, sizes, checks) -> S3 upload. Terraform for bucket + IAM role.
**Milestones:** 1) validator + tests, 2) transcode, 3) manifest + upload (localstack/moto), 4) Terraform, 5) Docker + CI.
**README outline:** problem, architecture diagram, usage, design decisions, limits.
**Demo:** run the CLI on a sample episode, show validation report, compression ratio, manifest.
**CV bullet it must live up to:** ingests multi-modal episodes (video, depth, joint states), validates quality (dropped frames, timestamp drift), compresses video with H.264/AV1 via PyAV, uploads with manifest to S3; CLI tools for operators; S3/IAM via Terraform; Docker; GitHub Actions. Depth must be handled too, or edit the bullet.
