# Project brief: Creative Asset Automation Pipeline
Goal: prototype that turns a campaign brief into product-image variants via a text-to-image API with a designer review step.
Proves for REWE JD: GenAI image workflows, API integration, Python, automation, designer-facing interface.
Scope (1-2 days): brief JSON -> prompt templates -> image API (swappable provider interface) -> brand-guideline checks (palette/size/text rules) -> FastAPI service + small web UI for approve/reject.
Stack: Python, FastAPI, a text-to-image API, simple web front end (React or HTMX).
Milestones: 1) provider interface + one model; 2) prompt templates + batch; 3) checks; 4) review UI; 5) README + demo GIF.
CV bullet it must live up to: "Proof of concept that turns a campaign brief into batches of product-image variants by calling a text-to-image API, with prompt templates, brand-guideline checks and a designer review step, served through a FastAPI interface."
