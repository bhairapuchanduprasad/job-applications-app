# Project brief: npc-memory-service
**Goal:** FastAPI + PostgreSQL service giving game NPCs persistent player memory, plus a prompt-flow simulator CLI.
**Why for welevel:** proves FastAPI, PostgreSQL schema design/indexing, real-time API design, Docker, CI/CD, prompt-flow test tooling.
**Scope (1-2 days):** tables players, npcs, memories, world_facts; indexes on (player_id, npc_id, created_at); POST /dialogue builds context from memory and calls an LLM (LiteLLM); POST /memories; CLI that replays YAML scripted sessions and prints prompt/response diffs.
**Stack:** Python, FastAPI, PostgreSQL, SQLAlchemy/Alembic, Docker Compose, GitHub Actions, pytest.
**Architecture:** client -> FastAPI -> Postgres (memory) + LLM via LiteLLM; simulator CLI -> same API.
**Milestones:** 1 schema+migrations; 2 endpoints; 3 simulator; 4 Docker+CI; 5 README, EXPLAIN-based index demo.
**README outline:** problem, architecture, schema, running, simulator demo, index benchmark.
**Demo idea:** scripted 3-session playthrough where the NPC recalls an earlier player choice.
**CV bullets to live up to:** both bullets on the welevel CV (schema + indexes + dialogue endpoint; prompt-flow simulator CLI, Docker, CI/CD pipeline).
