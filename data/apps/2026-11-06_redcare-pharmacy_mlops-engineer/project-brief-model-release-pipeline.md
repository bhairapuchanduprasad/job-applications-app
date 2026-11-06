# Project brief: Model Release Pipeline (Redcare MLOps Engineer)

**Goal:** small but complete MLOps path for one scikit-learn model on a public tabular dataset.
**Why it matters:** proves MLflow, model packaging/versioning, validation gate, Docker + Kubernetes, GitHub Actions CI/CD, monitoring/observability, automated security checks (JD keywords).
**Scope (1-2 days):** training script logs runs to MLflow, registers model; promotion script blocks on metric thresholds + data checks; FastAPI serving in Docker; kind cluster deploy via manifests/Helm; GitHub Actions: pytest, ruff, image scan (Trivy), build, deploy to kind; request/latency logging (Prometheus metrics endpoint), Evidently data-drift report.
**Stack:** Python, scikit-learn, MLflow, FastAPI, Docker, Kubernetes (kind), GitHub Actions, Trivy, pytest.
**Milestones:** 1 train+track+register; 2 validation gate; 3 serve+container; 4 kind deploy; 5 CI pipeline with scan; 6 monitoring + drift report; 7 README.
**README outline:** architecture diagram, how to run, promotion flow, monitoring, limits. **Demo:** push a worse model, show gate blocking it.
**CV bullet it must live up to:** MLflow tracking, packaging, versioning, registry with validation gate; FastAPI in Docker on kind; GitHub Actions CI/CD with pytest, image scan and secure delivery checks; latency logging and drift report.
