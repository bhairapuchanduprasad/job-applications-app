# Project brief: Social Mention Enrichment Pipeline (repo: social-mention-enrichment)
Goal: NLP enrichment service that tags social posts with sentiment and named entities.
Proves for Meltwater JD: Transformer fine-tuning, transfer learning, token classification (NER), sentiment analysis, PyTorch, FastAPI, Docker, Kubernetes, Terraform, Azure.
Scope (1-2 days): fine-tune a small pretrained transformer (DistilBERT / XLM-R base) on a public sentiment dataset and a public NER dataset (CoNLL-2003 or WikiANN); per-class F1 report; optional zero-shot LLM baseline.
Stack: Python, PyTorch, Hugging Face Transformers/Datasets, FastAPI, Docker, Kubernetes manifests (kind), Terraform module for Azure (Container Apps or AKS, validate/plan only).
Architecture: train.py -> model artefacts -> FastAPI /enrich (batch + streaming) -> Docker image -> k8s Deployment/Service; terraform/ for Azure resources.
Milestones: 1 data + baseline; 2 fine-tune sentiment + NER, eval; 3 API + Docker; 4 k8s + Terraform; 5 README.
README outline: problem, data, results (real numbers only), run locally, deploy.
Demo: curl a batch of posts, show sentiment + entities JSON.
CV bullet to live up to: fine-tuned transformer for sentiment analysis, text classification and NER, served via FastAPI in Docker, with Kubernetes manifests and Terraform for Azure.
