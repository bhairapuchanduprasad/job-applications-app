# Project brief: Care Note Structurer (HDP variant)

Base project: `applications/2026-10-14_dexter-health_ai-engineer-llm/_work/project-brief-care-note-structurer.md` (status: planned). This variant adds what HDP's Machine Learning Engineer posting asks for.

## Goal
Turn dictated or typed case notes (synthetic accident and rehabilitation reports, in German) into validated structured entries, as a REST microservice that runs in a container image on Kubernetes, with personal data pseudonymised before any model call.

## Why it matters for HDP
- JD: "Microservice für Microservice, vom Prototyp bis in den Echtbetrieb", REST APIs + Microservices, container images for Kubernetes, "Schutz sensibler Daten und Modelle", Python + "Java ist kein Fremdwort".
- Mirrors HDP's BesA (dictated/typed site-visit notes → text suggestions) and the planned AI platform with anonymisation + container delivery.

## Scope (1–2 days)
1. Synthetic dataset: 40–60 German accident/rehab case notes (e.g. Durchgangsarzt-style), generated + hand-labelled fields (accident date, body part, injury type, incapacity for work, next appointment, measures).
2. Pseudonymisation step (names, dates of birth, addresses, insurance numbers) via regex + spaCy/Presidio, reversible mapping kept server-side.
3. Extraction: Pydantic schema, LLM call through LiteLLM with retry/fallback between a commercial API and Ollama (self-hosted open-source LLM); grounding check (every field must be supported by a span in the note).
4. FastAPI REST service (`POST /structure`, `GET /health`), slim multi-stage Docker image (non-root user, no secrets in image).
5. Kubernetes manifests (Deployment, Service, ConfigMap, Secret) deployed to kind; readiness/liveness probes.
6. Small Spring Boot (Java) client that calls the API and prints the structured entry.
7. Eval: field-level precision/recall on the labelled set; pytest + eval in GitHub Actions CI.
8. Optional: Whisper transcription of an audio note.

## Stack
Python, FastAPI, Pydantic, LiteLLM, Ollama, Presidio/spaCy, Docker, Kubernetes (kind), Java (Spring Boot), pytest, GitHub Actions.

## Architecture
note (text/audio) → [Whisper] → pseudonymiser → LLM extractor (Pydantic) → grounding check → re-identification → JSON; FastAPI in container on kind; Java client → REST.

## Milestones
Day 1: data + labels, pseudonymiser, extractor, eval script. Day 2: FastAPI, Dockerfile, k8s manifests on kind, Java client, CI, README.

## README outline
Problem, data (synthetic only), architecture diagram, privacy design (what leaves the service), eval results table, how to run (docker, kind, Java client), limits.

## Demo
`kubectl port-forward` + Java client run on 3 notes; show pseudonymised prompt vs original.

## CV bullets it must live up to
- Turns dictated or typed case notes (synthetic accident and rehabilitation reports) into validated structured entries with Pydantic checks and a grounding check; for data protection, sensitive data is pseudonymised before any model call, with retry/fallback between a commercial LLM API and a self-hosted open-source LLM (Ollama).
- Runs as a REST microservice from prototype to slim container images on a local Kubernetes cluster (kind), called by a small Spring Boot (Java) client; labelled synthetic eval set (field-level precision/recall) in GitHub Actions CI.
