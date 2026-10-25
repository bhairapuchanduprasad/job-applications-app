# Application notes: JuicyLemons (recruiter), Product Engineer (m/f/d), Berlin

Apply via the LinkedIn posting (https://www.linkedin.com/jobs/view/4483366465). JuicyLemons is a recruiter; the client is an unnamed, VC-backed Berlin start-up using AI for medical and clinical information for healthcare professionals and patients. On the first call with the recruiter, ask: company name, funding stage, team size, salary band (must meet the EU Blue Card threshold), frontend stack (React? TypeScript? Next.js?), and how product decisions are made.

**Build first:** Clinical Info Assistant (`clinical-info-assistant`), brief in `_work/project-brief-clinical-info-assistant.md`. It is on the CV; do not submit before it exists.

## Likely interview questions
**1. "Tell us about a time you spotted friction for users and changed the product."** Expert Interface at Kniit: the knowledge graph was only useful if SAP experts could check it, so you built one place to review, validate and approve changes. Covestro data science internship: chemists could try parameter changes in the Streamlit dashboard before running a physical batch. After building the project: the one UX change the funnel data prompted.

**2. "How do you decide what to build next / how do you use data?"** Ground-truth evaluation at Kniit: measure, find the biggest error class, fix it (33/45 → 93/90 precision/recall). Choosing a deterministic pipeline for the high-volume source because the cost data said so ($200k projected LLM budget → near zero). Be honest that you have not run product analytics or A/B tests in a job; the project shows the basics.

**3. "Walk us through the architecture of a web app you built, frontend to backend, and how you tested it."** Covestro: React frontend, FastAPI backend, Postman API tests, Docker, AWS CDK, GitLab CI/CD. Kniit Expert Interface: React + Python microservices on Azure. Be honest about React depth (two internal apps, no TypeScript in a job).

Also prepare: how you would make an AI answer safe for patients vs doctors (grounding, citations, handoff), working without specs in a founding team, "Why are you leaving Kniit?" → public line from the profile.

## Form fields
- **Why this company?** Medical information is a field where an unclear answer has a real cost, and the same fact has to read differently for a doctor and a patient. I want to work on that product problem in a small team, close to the founders and the users.
- **Salary expectation:** €70,000 gross/year (range €60,000–75,000). Must be above the EU Blue Card threshold.
- **Earliest start / notice period:** 15 November 2026.
- **Work authorisation:** EU Blue Card (Germany).
- **Location:** will be based in Berlin; hybrid ~70% on-site is fine.
- **German level:** B1, improving.
