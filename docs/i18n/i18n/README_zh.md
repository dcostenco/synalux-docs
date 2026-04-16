# ✦ Synalux

**模块化EHR平台 — AI原生、HIPAA合规、专科无关**

> Synalux是一个开放的模块化电子健康记录平台，可以将其临床语言、数据模型和AI行为适配到任何医疗专科——从ABA疗法到儿科再到皮肤科。

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Clinical_Workspace-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Agentic_IDE-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language:** · [English](../../README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← 返回英文版](../../README.md)**

---

## ⚡ "Wow" 因素

* **🛡️ AI沙箱 — "临床医生在环路中"：** Synalux是第一个AI**没有您的签名就无法触碰您的数据**的EHR。
* **🔐 无状态RLS — 无会话开销的水平扩展。**
* **🧠 持久语义记忆：** 基于 [Prism MCP](https://github.com/dcostenco/prism-mcp) 构建。
* **🏥 即时专科变换。**
* **🎙️ 零点击环境采集：** 使用浏览器内的 **WASM Whisper**。
* **⚡ 提示级别的RBAC。**

---

## 🎯 核心能力

| | Feature | Description |
|---|---|---|
| 🏥 | **Multi-Specialty EHR** | ABA, Pediatrics, Dental, Mental Health, PT, Dermatology |
| 🤖 | **26+ AI Tools** | SOAP Notes, FBA, BIP, ABC Data, Scheduling, Billing |
| 💬 | **AI Chat** | Voice-to-action clinical workflow |
| 👥 | **Team Chat** | HIPAA-compliant provider messaging |
| 📊 | **Reports** | Caseload, utilization, billing, compliance, productivity |
| 🏥 | **Patient Portal** | Appointments, documents, billing, messages |
| 📱 | **iPhone/iPad** | Full responsive PWA — works on any device |
| 🔒 | **HIPAA Security** | Ed25519 JWT, RLS, audit logs, zero LocalStorage |
| 🌐 | **12 Languages** | EN, ES, FR, PT, RO, UK, RU, DE, JA, KO, ZH, AR |
| 🧠 | **Prism Memory** | Persistent knowledge graphs across sessions |

---

## 🚀 快速开始

### 医疗机构和诊所（Web应用）
1. → [synalux.ai/app](https://synalux.ai/app)
2. Sign in with Google (MFA required for clinical roles)
3. Select **Therapy Session** from the template dropdown
4. Type or dictate your clinical notes
5. Click **📤 Generate SOAP Note**

### 开发者（VS Code）
1. Install: `ext install synalux-ai.synalux`
2. `Cmd+Shift+P` → **Synalux: Sign In with Google**
3. Chat: `@coder Scaffold a new Next.js route`

### 希望100%本地化的诊所
```bash
# 1. Install Ollama
brew install ollama

# 2. Pull a model
ollama pull qwen2.5-coder:14b

# 3. Enable CORS
OLLAMA_ORIGINS="https://synalux.ai" ollama serve

# 4. Open synalux.ai/app → toggle to "Local"
```

---

<p align="center">
  <br>
  <b>© 2024–2026 Dmitri Costenco.</b><br>
  Licensed under the <a href="LICENSE">Business Source License 1.1 (BSL-1.1)</a>.<br>
  <a href="https://synalux.ai/docs/disclaimer">Legal & Medical Disclaimer</a>
</p>
