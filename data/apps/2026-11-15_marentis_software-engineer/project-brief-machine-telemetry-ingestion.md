# Project brief: Machine Telemetry Ingestion Service
Repo slug: machine-telemetry-ingestion. Status: planned.
**Goal:** backend service that ingests simulated machine telemetry via MQTT into PostgreSQL and survives bad data.
**Proves for Marentis JD:** Python backend, SQL data pipelines, MQTT/OPC UA, missing/duplicate/out-of-order events, simulated device inputs, unit/integration/regression tests, CI.
**Scope (1-2 days):** Mosquitto + Python simulator (3 machines, scripted faults: gaps, duplicates, out-of-order, invalid values, broker disconnects), ingest worker (paho-mqtt), idempotent writes with event ids and per-asset ordering, validation with Pydantic and unit checks, PostgreSQL schema (asset, signal, measurement, quarantine), FastAPI read endpoints, optional OPC UA source via asyncua.
**Tech:** Python, paho-mqtt, FastAPI, PostgreSQL, Docker Compose, pytest, GitHub Actions.
**Architecture:** simulator -> Mosquitto -> ingest worker -> Postgres (+ quarantine table) -> FastAPI.
**Milestones:** 1 simulator + broker; 2 ingest + schema; 3 fault handling + tests; 4 API + CI; 5 README.
**README outline:** problem, architecture diagram, fault matrix and how each is handled, run/test instructions.
**Demo:** replay a recorded fault stream, show quarantined rows and the clean series.
**CV bullet it must live up to:** ingests simulated telemetry over MQTT into PostgreSQL, handles missing measurements, duplicate and out-of-order events, invalid values and connection failures, with a replayable simulator and unit, integration and regression tests in CI.
