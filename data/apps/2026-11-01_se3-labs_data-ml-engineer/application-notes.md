# Application notes: SE3 Labs, Data and ML Engineer, Munich

Status: build-first. Build before submitting: Road Damage Inference Service, SE3 variant "Road Damage Dataset & Model Pipeline" (catalogue, Label Studio, DVC splits, fine-tune, per-slice eval, data-gap report; brief: `_work/project-brief-road-damage-inference.md`).
Apply via LinkedIn: https://www.linkedin.com/jobs/view/4484468104 (or SE3 careers page).

## Decisions for you
- Defence is a core application at SE3. Ask the recruiter whether a security clearance (Sicherheitsüberprüfung) is needed and whether it works for a non-German citizen on an EU Blue Card.
- A second SE3 role was prepared in the same run (Forward Deployed Engineer, Applied AI, needs fluent German). This role has no German requirement and is the better bet. Decide one or both.
- Possible extra labelling evidence: the base CV has a commented-out thesis bullet ("Deployed Streamlit app on EC2 for chemist labeling, storing responses in S3 to create a retrieval ground truth dataset."). It is not in the master profile, so it was not used. If it's true, add it to the profile and then to this CV (thesis role). Labelling is a JD must-have.

## Likely interview questions
1. "How would you organise our recordings so they're reusable?" Metadata catalogue (sensor, platform, conditions, label status), versioned datasets, ingestion pipeline with quality checks; point to the project.
2. "Tell us about training a model on messy real-world data." Covestro prepolymer sensor time series: lag/rolling features, RF/XGBoost/LSTM vs curve fitting, Streamlit tool for chemists.
3. "How do you know a model needs more data rather than a better architecture?" Per-slice evaluation, error vs sample count; Kniit: evaluation against SAP-derived ground truth (P/R 33%/45% → 93%/90%).
Also expect: C++ (none; Python), computer vision (course-level CNN/ResNet + project), field work (willing).

## Form fields
- Why SE3: TUM (Cremers group) spin-out turning research into field-ready autonomy; role builds the data foundation behind it.
- Salary: €70,000 (range €60–75k; must meet Blue Card threshold). Not stated in JD.
- Notice / start: 15 November 2026.
- Location: Munich (relocating; Erding test facility fine).
- Work permit: EU Blue Card. German: B1.
