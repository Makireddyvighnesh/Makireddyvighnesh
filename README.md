# M. Bala Vighnesh Reddy

AI/ML engineer interested in **RL for LLMs, robotics, vision models, and efficient models**.

I like building systems that connect model behavior with real workflows: reward design for reasoning models, retrieval systems, computer-vision pipelines, quantization, and small-model finetuning.

[LinkedIn](https://www.linkedin.com/in/makireddy-bala-vighnesh-324278253) · [Email](mailto:makireddyvighnesh@gmail.com) · [GitHub](https://github.com/Makireddyvighnesh)

---

## Current Focus

- **RL for LLMs:** GRPO, execution-based rewards, reasoning traces, Text-to-SQL evaluation.
- **Robotics:** language-action models, perception-to-action systems, embodied AI workflows.
- **Vision models:** segmentation, pose estimation, detection, medical imaging, and 3D-aware pipelines.
- **Efficient models:** LoRA, QLoRA, INT8 quantization, compact deployment, and inference optimization.

## Selected Work

### [ml-model-registry](https://github.com/Makireddyvighnesh/ml-model-registry)

Full-stack Vision AI API platform for image classification, object detection, OCR, and segmentation through developer-friendly REST APIs.

- Migrated the backend from JavaScript to TypeScript for maintainability and type safety.
- Built a React dashboard for authentication, API key management, billing, usage tracking, model browsing, and live inference testing.
- Designed JWT authentication for dashboard users and API-key access for programmatic usage.
- Added MongoDB-backed users, API keys, usage logs, subscriptions, invoice data, and model registry data.
- Integrated a FastAPI ML inference worker with YOLOv8n, ResNet50, EasyOCR, and YOLOv8n-seg.
- Added Stripe Checkout support, Docker Compose services, health checks, request IDs, and deployment planning for GCP Cloud Run / Vertex AI.

**Stack:** TypeScript, React, FastAPI, MongoDB, Redis, Docker, Stripe, YOLOv8n, ResNet50, EasyOCR

### Text-to-SQL Research

Distilled DeepSeek reasoning into Qwen3-4B using LoRA and trained with execution-based reward functions for SQL correctness.

- Generated 9,000+ chain-of-thought SQL examples for Spider and BIRD.
- Used GRPO reward design to improve performance by 10% over baseline.
- Reached 86.7% pass@4 on Spider and 70.7% pass@4 on BIRD.
- Ran efficient training experiments using 4-bit QLoRA.

**Stack:** Qwen3-4B, DeepSeek, LoRA, QLoRA, GRPO, Tinker API

### [Document Querying System](https://github.com/Makireddyvighnesh/RAG-LLM-Query-Engine)

RAG application for querying large document collections with indexed retrieval and chat-style interaction.

- Built upload, indexing, and query APIs with Node.js.
- Used LlamaIndex for retrieval-augmented generation.
- Added React chat threads, MongoDB storage, authentication, and session management.

**Stack:** LlamaIndex, Node.js, React, MongoDB

### [AutoMCQGen](https://github.com/Makireddyvighnesh/AUtoMcqGen)

Automated MCQ generation system using Llama2-7B with constrained outputs and evaluation.

- Designed preprocessing for long academic documents around the 4,096-token context limit.
- Used topic-aware chunking and schema-constrained generation.
- Built an LLM-as-judge evaluation loop with GPT-3.5.

**Stack:** Llama2-7B, LMQL, NLP, GPT-3.5

### Computer Vision Systems Internship

Internship work across fashion and medical imaging pipelines for segmentation, pose estimation, detection, enhancement, and deployment.

- Built a fashion-domain pipeline with U2-Net, P3M-Net, DWPose, and MediaPipe for segmentation and pose estimation.
- Tested SMPL for 3D body mesh estimation and used the findings to refine the pipeline direction.
- Improved low-resolution and low-light image quality with LLFormer and KANT.
- Fine-tuned and quantized ViT for medical image classification with 89% INT8 accuracy.
- Built Faster R-CNN detection and DeepLabV3 segmentation workflows for medical images.

**Stack:** PyTorch, ViT, Faster R-CNN, DeepLabV3, U2-Net, P3M-Net, MediaPipe, Gradio

## Technical Stack

**Languages:** Python, C/C++, JavaScript, HTML, CSS  
**AI/ML:** PyTorch, HuggingFace, Transformers, UnSloth, LangChain, LlamaIndex, CrewAI, MCP  
**LLM Systems:** RAG, vector databases, LoRA, QLoRA, Ollama, OpenRouter, Llama, Qwen, DeepSeek  
**Backend:** FastAPI, Flask, Node.js, Express.js, REST APIs  
**Frontend:** React, Tailwind CSS, Bootstrap, Gradio  
**Data/Cloud:** MongoDB, MySQL, GCP

## Profile Snapshot

- Building toward research engineering work in RL, LLM systems, robotics, and vision.
- Comfortable moving between model training, backend APIs, retrieval systems, and simple product interfaces.
- Strongest current themes: reward design, compact finetuning, RAG, medical/fashion vision pipelines, and model deployment.

## Open To

Research engineering and applied ML roles around:

- RL for LLMs and reasoning models
- Robotics and language-action systems
- Vision models and perception pipelines
- Efficient finetuning and deployment of compact models
