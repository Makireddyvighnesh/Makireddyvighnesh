from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    ListFlowable,
    ListItem,
)


OUTPUT = "assets/Bala-Vighnesh-AIML-Resume.pdf"


def p(text, style):
    return Paragraph(text, style)


def bullets(items, style):
    return ListFlowable(
        [ListItem(p(item, style), leftIndent=0) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=14,
        bulletFontSize=7,
        bulletOffsetY=1,
    )


def section(title, styles):
    return [
        Spacer(1, 5),
        p(f"<b><u>{title}</u></b>", styles["section"]),
        Spacer(1, 4),
    ]


def row(left, right, styles):
    table = Table(
        [[p(left, styles["role"]), p(right, styles["date"])]],
        colWidths=[13.2 * cm, 4.3 * cm],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return table


def project(title, stack, link, url, styles):
    right = f'<link href="{url}"><font color="#004C99">{link}</font></link>' if link else ""
    table = Table(
        [[p(f"<b>{title}</b> <font color='#6D6D6D'><b>: {stack}</b></font>", styles["body"]), p(right, styles["date"])]],
        colWidths=[14.2 * cm, 3.3 * cm],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return table


def build():
    base = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle(
            "name",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=16,
            leading=18,
            alignment=1,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "contact",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10,
            leading=12,
            alignment=1,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=12,
            leading=14,
            alignment=1,
        ),
        "role": ParagraphStyle(
            "role",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=11,
            leading=13,
        ),
        "date": ParagraphStyle(
            "date",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=10,
            leading=12,
            alignment=2,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=9.4,
            leading=11.2,
        ),
        "company": ParagraphStyle(
            "company",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=9.4,
            leading=10.8,
            textColor=colors.HexColor("#6D6D6D"),
        ),
    }

    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.25 * cm,
        bottomMargin=1.25 * cm,
    )

    story = []
    story.append(p("M. Bala Vighnesh Reddy", styles["name"]))
    story.append(
        p(
            '+91-9550057396 | <link href="mailto:makireddyvighnesh@gmail.com"><font color="#004C99">makireddyvighnesh@gmail.com</font></link> | '
            '<link href="https://www.linkedin.com/in/makireddy-bala-vighnesh-324278253"><font color="#004C99">LinkedIn</font></link> | '
            '<link href="https://github.com/Makireddyvighnesh"><font color="#004C99">GitHub</font></link> | '
            '<link href="https://makireddyvighnesh.github.io/Makireddyvighnesh/"><font color="#004C99">Portfolio</font></link>',
            styles["contact"],
        )
    )

    story += section("SUMMARY", styles)
    story.append(
        p(
            "AI/ML engineer with experience in <b>computer vision</b>, <b>LLM systems</b>, <b>RAG</b>, and <b>efficient model training/deployment</b>. "
            "Interested in <b>RL for LLMs</b>, robotics, vision models, and compact models. Built production-oriented ML pipelines across segmentation, pose estimation, medical imaging, Text-to-SQL reasoning, document querying, Vision AI APIs, and <b>agentic applications using MCP and Groq</b>.",
            styles["body"],
        )
    )

    story += section("EDUCATION", styles)
    story.append(row("<b>Indian Institute of Information Technology, Manipur</b>", "Nov 2021 -- Apr 2025", styles))
    story.append(p("<i>Bachelor of Technology in Computer Science and Engineering</i>", styles["body"]))

    story += section("WORK EXPERIENCE", styles)
    story.append(row("<b>Computer Vision Intern</b>", "Aug 2025 -- Feb 2026", styles))
    story.append(p("BigThinx, Bengaluru", styles["company"]))
    story.append(
        bullets(
            [
                "Built a fashion-domain computer vision pipeline combining <b>U2-Net</b>, <b>P3M-Net</b>, <b>DWPose</b>, and <b>MediaPipe</b> for foreground segmentation and pose estimation on 2-view image inputs.",
                "Tested the <b>SMPL parametric body model</b> for 3D body mesh estimation from sparse 2D observations, and used the findings to refine the pipeline direction for loose-fitting garments.",
                "Enhanced low-resolution and low-light inputs using <b>LLFormer</b> and <b>KANT</b>, improving the existing pipeline performance by <b>30%</b>; deployed the system on a VM with a <b>Gradio</b> interface for real-time inference.",
            ],
            styles["body"],
        )
    )
    story.append(Spacer(1, 5))

    story.append(row("<b>AI/ML Intern</b>", "Jan 2025 -- May 2025", styles))
    story.append(p("IF MedTech, Navi Mumbai", styles["company"]))
    story.append(
        bullets(
            [
                "Fine-tuned a <b>Vision Transformer (ViT)</b> on limited medical imaging data and quantized it to <b>INT8</b>, achieving <b>89% accuracy</b> with reduced model size and inference time.",
                "Built medical image workflows using <b>Faster R-CNN</b> for anatomical region detection and <b>DeepLabV3</b> for semantic segmentation, reaching <b>0.64 IoU</b> on limited annotated data.",
                "Implemented a medical <b>RAG application</b> over a reference book using vector embeddings and <b>Llama3-8B</b> for context-grounded query answering.",
            ],
            styles["body"],
        )
    )

    story += section("PROJECTS", styles)
    story.append(project("Text-to-SQL Research", "Qwen3-4B-Instruct, DeepSeek, QLoRA, GRPO, Tinker API", "", "", styles))
    story.append(
        bullets(
            [
                "Distilled reasoning from <b>DeepSeek</b> into <b>Qwen3-4B</b> using <b>LoRA</b>, generating <b>9,000+</b> Chain-of-Thought SQL examples for Spider and BIRD.",
                "Implemented <b>execution-based reward functions</b> for <b>GRPO</b>, using SQL correctness as a verifiable reinforcement learning signal and improving performance by <b>10%</b> over baseline.",
                "Achieved <b>86.7% pass@4</b> on Spider dev and <b>70.7% pass@4</b> on BIRD dev using compute-efficient <b>4-bit QLoRA</b> training.",
            ],
            styles["body"],
        )
    )
    story.append(Spacer(1, 5))

    story.append(project("ml-model-registry", "TypeScript, React, FastAPI, MongoDB, Docker, YOLOv8n", "GitHub", "https://github.com/Makireddyvighnesh/ml-model-registry", styles))
    story.append(
        bullets(
            [
                "Built a full-stack <b>Vision AI API platform</b> exposing image classification, object detection, OCR, and segmentation through developer-friendly REST APIs.",
                "Integrated a Python <b>FastAPI ML inference worker</b> with lightweight models including <b>YOLOv8n</b>, <b>ResNet50</b>, <b>EasyOCR</b>, and <b>YOLOv8n-seg</b>.",
                "Added a React dashboard for model catalog browsing, live inference testing, API key management, usage tracking, and billing workflows; containerized services with <b>Docker Compose</b>.",
            ],
            styles["body"],
        )
    )
    story.append(Spacer(1, 5))

    story.append(project("AutoMCQGen", "Llama2-7B, GPT-3.5, NLP, LMQL", "GitHub", "https://github.com/Makireddyvighnesh/AUtoMcqGen", styles))
    story.append(
        bullets(
            [
                "Built a multiple-choice question generator using <b>Llama2-7B</b> and <b>LMQL</b>, constraining model outputs to strict schemas and subject-aligned formats.",
                "Designed an NLP preprocessing pipeline with rule-based splitting and topic modeling to convert long academic documents into logical, topic-aware chunks.",
                "Used <b>GPT-3.5</b> as an LLM-as-judge evaluator for correctness and relevance, achieving <b>87% content alignment</b>.",
            ],
            styles["body"],
        )
    )
    story.append(Spacer(1, 5))

    story.append(project("Document Querying RAG System", "LlamaIndex, Node.js, React, MongoDB", "GitHub", "https://github.com/Makireddyvighnesh/RAG-LLM-Query-Engine", styles))
    story.append(
        bullets(
            [
                "Developed a <b>Retrieval-Augmented Generation</b> system using <b>LlamaIndex</b> to query large document collections with context-grounded responses.",
                "Created <b>Node.js REST APIs</b> for document upload, indexing, and querying, backed by <b>MongoDB</b> and a React frontend with expandable chat threads.",
                "Implemented secure authentication and session management to protect user data.",
            ],
            styles["body"],
        )
    )

    story += section("TECH SKILLS", styles)
    story.append(
        bullets(
            [
                "<b>Languages & Frameworks:</b> Python, C/C++, TypeScript, JavaScript, FastAPI, Flask, Node.js, React.js",
                "<b>AI/ML:</b> PyTorch, HuggingFace, Transformers, LLMs, LoRA, QLoRA, RAG, VectorDB, LangChain, LlamaIndex, UnSloth",
                "<b>Computer Vision:</b> ViT, Faster R-CNN, DeepLabV3, YOLOv8, EasyOCR, MediaPipe, U2-Net, P3M-Net, segmentation, detection, pose estimation",
                "<b>MLOps & Tools:</b> Docker, Docker Compose, Git, GitHub, Gradio, Ollama, OpenRouter, MongoDB, MySQL, GCP",
            ],
            styles["body"],
        )
    )

    story += section("CERTIFICATIONS", styles)
    story.append(
        bullets(
            [
                '<link href="https://coursera.org/share/66820de848d0b272fa5bef8239e27c54"><font color="#004C99"><b>Generative AI with Large Language Models</b></font></link> -- DeepLearning.AI (2024)',
                '<link href="https://coursera.org/share/f7c868b141a2761a5a0d7bc1da42d67d"><font color="#004C99"><b>Neural Networks and Deep Learning</b></font></link> -- DeepLearning.AI / Coursera (2024)',
            ],
            styles["body"],
        )
    )

    doc.build(story)


if __name__ == "__main__":
    build()
