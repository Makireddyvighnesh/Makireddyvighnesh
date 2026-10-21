<h1 align="center">Bala Vighnesh Reddy</h1>

<p align="center">
  ML Engineer at Aiverbalyze &nbsp;·&nbsp; LLM inference &nbsp;·&nbsp; RL post-training &nbsp;·&nbsp; Speech
</p>

<p align="center">
  <a href="https://makireddyvighnesh.github.io/"><img src="https://img.shields.io/badge/Website-111111?style=flat-square&logo=googlechrome&logoColor=white" alt="Website"></a>
  <a href="https://huggingface.co/makireddyvighnesh"><img src="https://img.shields.io/badge/Hugging_Face-111111?style=flat-square&logo=huggingface&logoColor=FFD21E" alt="Hugging Face"></a>
  <a href="https://www.linkedin.com/in/makireddy-bala-vighnesh-324278253"><img src="https://img.shields.io/badge/LinkedIn-111111?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://makireddyvighnesh.github.io/resume.pdf"><img src="https://img.shields.io/badge/Resume-111111?style=flat-square&logo=readthedocs&logoColor=white" alt="Resume"></a>
  <a href="mailto:makireddyvighnesh@gmail.com"><img src="https://img.shields.io/badge/Email-111111?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
</p>

<br>

I train and evaluate speech recognition models and build real-time voice agents at Aiverbalyze. Outside work, I go deep on LLMs: post-training them with reinforcement learning, building the environments they learn in, and understanding how inference really works by building it myself.

### Featured projects

| Project | What it is | Result |
| :-- | :-- | :-- |
| **[mini-inference-engine](https://github.com/Makireddyvighnesh/mini-inference-engine)** | An LLM serving engine built from a plain decode loop upward: KV cache, continuous batching, paged KV with Triton kernels, CUDA Graphs, prefix caching. Qwen3-4B on one L4 GPU. | 370 tok/s at batch 16, vs 229 for HF `generate()` |
| **[telugu-rl-envs](https://github.com/Makireddyvighnesh/telugu-rl-envs)** | RL environments for Telugu transliteration, OCR, ASR and translation on OpenEnv, with reward-hacking guards. GRPO-trained [model on Hugging Face](https://huggingface.co/makireddyvighnesh/Qwen2.5-1.5B-Instruct-telugu-translit-grpo). | Exact match 4.6% → 29.1% on a 1.5B model |
| **Text-to-SQL with SFT + GRPO** | Qwen3-4B fine-tuned on 9,000+ chain-of-thought SQL examples, then trained with a reward that executes each query. | 86.7% pass@4 on Spider, 70.7% on BIRD |

### Experience

| Role | Company | Focus | When |
| :-- | :-- | :-- | :-- |
| ML Engineer | Aiverbalyze | ASR for 12 Indic languages; voice-to-voice pipeline under ~1.2 s at p95 | 2026 – now |
| Computer Vision Intern | BigThinx | Body segmentation and pose from two photos, for fashion | 2025 – 26 |
| AI/ML Intern | IF MedTech | Medical imaging models on small datasets | 2025 |

### Writing

- [What I learned building an LLM inference engine](https://makireddyvighnesh.github.io/posts/inference-engine.html): six techniques, one L4 GPU, and the bottleneck each one actually removes. *Oct 2026*

### Tools I use

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)
![Triton](https://img.shields.io/badge/Triton-222222?style=flat-square)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)

<br>

<p align="center"><sub>Always happy to talk about RL, inference or speech. <a href="mailto:makireddyvighnesh@gmail.com">Say hi</a>.</sub></p>
