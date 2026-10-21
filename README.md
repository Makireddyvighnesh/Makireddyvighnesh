### Hello, I'm Bala

ML engineer at Aiverbalyze, where I train and evaluate speech recognition models and build real-time voice agents.

Outside work, I go deep on LLMs: post-training them with reinforcement learning, building the environments they learn in, and understanding how inference really works by building it myself.

[website](https://makireddyvighnesh.github.io/) · [hugging face](https://huggingface.co/makireddyvighnesh) · [linkedin](https://www.linkedin.com/in/makireddy-bala-vighnesh-324278253) · [email](mailto:makireddyvighnesh@gmail.com)

<br>

#### Projects

**[Mini LLM inference engine](https://github.com/Makireddyvighnesh/mini-inference-engine)**  
Serving Qwen3-4B on one L4 GPU, built up one bottleneck at a time: KV cache, continuous batching, paged KV with Triton kernels, CUDA Graphs, prefix caching. 370 tok/s at batch 16, against 229 for Hugging Face `generate()`.

**[Telugu RL environments + GRPO](https://github.com/Makireddyvighnesh/telugu-rl-envs)** · [model](https://huggingface.co/makireddyvighnesh/Qwen2.5-1.5B-Instruct-telugu-translit-grpo)  
RL environments for Telugu transliteration, OCR, ASR and translation, built on OpenEnv. GRPO through my own environment took a 1.5B model from 4.6% to 29.1% exact match.

**Text-to-SQL with SFT + GRPO**  
Qwen3-4B trained with a reward that executes each query: 86.7% pass@4 on Spider, 70.7% on BIRD.

<br>

#### Work

**ML Engineer, Aiverbalyze** · 2026–now  
Speech recognition for 12 Indic languages, and a voice-to-voice pipeline that answers in under ~1.2 s at p95.

**Computer Vision Intern, BigThinx** · 2025–26  
Body segmentation and pose from two photos, for fashion.

**AI/ML Intern, IF MedTech** · 2025  
Medical imaging models on small datasets.

<br>

#### Writing

[What I learned building an LLM inference engine](https://makireddyvighnesh.github.io/posts/inference-engine.html) · Oct 2026

<br>

<sub>Always happy to talk about RL, inference or speech. [Say hi](mailto:makireddyvighnesh@gmail.com).</sub>
