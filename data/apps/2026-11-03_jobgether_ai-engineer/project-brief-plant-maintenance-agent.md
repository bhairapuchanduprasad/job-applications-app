# Project brief: Plant Maintenance Agent (Jobgether AI Engineer, industrial AI variant)
Reused planned project (profile/projects.md). Not built: do not use as a proof story or add a link.
Goal: LangGraph multi-agent predictive-maintenance PoC on simulated pump data. Proves: agentic AI orchestration, tool use, human-in-the-loop approval gate, tracing/cost logging, FFT features on vibration, OpenCV + pretrained detector on public defect images (NEU/MVTec), FastAPI + PostgreSQL work orders, Docker, eval set in CI.
Scope (2 days): simulated sensor generator (temp, vibration, OPC UA-style tags); FFT features; Isolation Forest anomaly agent; manual-search RAG agent; orchestrator proposing actions; approval endpoint; Langfuse/OpenTelemetry traces with token cost; OpenCV frame sampling + pretrained detector; Postgres work orders; docker compose; pytest + GitHub Actions eval.
Milestones: 1 data+features, 2 agents+orchestrator, 3 approval gate+tracing, 4 vision step, 5 API/Docker/CI, 6 README + demo.
CV bullets to live up to: see Projects section of cv.tex.
