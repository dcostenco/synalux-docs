# ✦ Synalux Elite v11.1 (Private Core)

**The Cognitive Foundation for Modern Healthcare.**

This repository contains the private core infrastructure, benchmarks, and training pipelines for the Synalux Elite platform. 

---

### 🏥 Clinical Command Center

Synalux Elite v11.1 provides a unified workspace for BCBAs, RBTs, and Practice Administrators. 

![Dashboard Preview](portal/public/dashboard-preview.png)

#### Core Modules:

- **📋 Clinical SOAP Generator**: Real-time dictation synthesis with WASM-based local Whisper. Generates insurance-compliant SOAP notes in seconds.
- **📊 Data Collection & EVV**: Comprehensive clinical data tracking (DTT, Duration, ABC) with integrated Electronic Visit Verification.
- **🧠 Active Insights**: GRPO-aligned clinical reasoning identifies target mastery and plateaus automatically.
- **⏱️ Practice Management**: Integrated timesheets, authorizations tracking, and billing claims automation.

![SOAP Generator](portal/public/soap-notes-preview.png)

---

### 🧠 Cognitive Performance (Held-Out Benchmark)

Synalux v11.1 Elite utilizes **Structural GRPO (Group Relative Policy Optimization)** for tool-use and clinical reasoning alignment. Results below are from a **held-out test set** (prompts never seen during training).

| Metric | **Score** | **N** | **Target** | **Status** |
|:-------|:---:|:---:|:---:|:---:|
| **Tool Selection** | 40.0% | 15 | 95.0% | 🔧 In Progress |
| **JSON Validity** | 100.0% | 15 | 95.0% | ✅ Passing |
| **Parameter Accuracy** | 80.0% | 15 | 95.0% | 🔧 In Progress |

> **Methodology**: Results from [`training/benchmark.py`](https://github.com/dcostenco/prism-mcp/blob/main/training/benchmark.py) against `prism-coder:7b` (GRPO-aligned Qwen-7B). The benchmark uses a held-out prompt set distinct from training data. Self-validation benchmarks in `benchmarks/` evaluate training data format quality — not model inference accuracy.

---

### 📂 Repository Structure

- `portal/`: The Next.js 15 Web Portal & API layer (312 TypeScript files, 60+ API routes).
- `benchmarks/`: Python-based format validation tests (Retrieval, Tool-Call, Reasoning).
- `scripts/`: Training, synthetic data generation, and export pipelines.
- `tools/`: Multimodal clinical agents and protocol validators.
- `docs/`: Technical specifications and compliance matrices.

---

### 🚀 Rapid Start

1. **Install Dependencies**: `pip install -r requirements.txt && cd portal && npm install`
2. **Run Benchmarks (Real Inference)**: `python3 benchmarks/prism_toolcall.py --ollama`
3. **Run Benchmarks (Format Validation Only)**: `python3 benchmarks/prism_toolcall.py`
4. **Local Dev**: `cd portal && npm run dev`
5. **Run Portal Tests**: `cd portal && npx vitest run`

---
**Security Notice**: This is a private repository. PHI handling and clinical logic must follow the ABA Precision Protocol defined in `GEMINI.md`.
