# ✦ Synalux

**모듈형 EHR 플랫폼 — AI 네이티브, HIPAA 준수, 전문 분야 불가지론**

> Synalux는 임상 언어, 데이터 모델 및 AI 동작을 모든 의료 전문 분야에 맞게 조정하는 개방형 모듈식 전자 건강 기록 플랫폼입니다.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Clinical_Workspace-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Agentic_IDE-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language:** · [English](../../README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← 영어 버전으로 돌아가기](../../README.md)**

---

## ⚡ "Wow" 요소

* **🛡️ AI 샌드박스 — "임상의 루프 내" :** Synalux는 AI가 **귀하의 서명 없이 데이터를 건드릴 수 없는** 최초의 EHR입니다.
* **🔐 상태 비저장 RLS — 세션 오버헤드 없는 수평 확장.**
* **🧠 영구 의미 메모리:** [Prism MCP](https://github.com/dcostenco/prism-mcp) 기반.
* **🏥 즉시 전문 분야 변환.**
* **🎙️ 클릭 없는 주변 입력:** 브라우저 내 **WASM Whisper** 사용.
* **⚡ 프롬프트 수준 RBAC.**

---

## 🎯 주요 기능

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

## 🚀 시작하기

### 의료 및 클리닉용 (웹 앱)
1. → [synalux.ai/app](https://synalux.ai/app)
2. Sign in with Google (MFA required for clinical roles)
3. Select **Therapy Session** from the template dropdown
4. Type or dictate your clinical notes
5. Click **📤 Generate SOAP Note**

### 개발자용 (VS Code)
1. Install: `ext install synalux-ai.synalux`
2. `Cmd+Shift+P` → **Synalux: Sign In with Google**
3. Chat: `@coder Scaffold a new Next.js route`

### 100% 로컬을 원하는 클리닉용
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
