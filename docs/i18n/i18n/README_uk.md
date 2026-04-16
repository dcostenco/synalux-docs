# ✦ Synalux

**Модульна платформа ЕМК — Нативна ШІ, сумісна з HIPAA, агностична до спеціальності**

> Synalux — це відкрита модульна платформа електронної медичної картки, яка адаптує свою клінічну мову, моделі даних та поведінку ШІ під будь-яку медичну спеціальність.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Clinical_Workspace-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Agentic_IDE-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language:** · [English](README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← Повернутися до англійської версії](README.md)**

---

## ⚡ Фактори "Wow"

* **🛡️ Пісочниця ШІ — "Клініцист у контурі" :** Synalux — це перша ЕМК, де ШІ **не може торкнутися ваших даних без вашого підпису**.
* **🔐 RLS без стану — Горизонтальне масштабування без навантаження сесій.**
* **🧠 Стійка семантична пам'ять:** Побудована на [Prism MCP](https://github.com/dcostenco/prism-mcp).
* **🏥 Миттєва трансформація спеціальності.**
* **🎙️ Фонове введення без натискань:** Використовуючи **WASM Whisper** у браузері.
* **⚡ RBAC на рівні промпту.**

---

## 🎯 Ключові можливості

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

## 🚀 Початок роботи

### Для охорони здоров'я та клінік (веб-додаток)
1. → [synalux.ai/app](https://synalux.ai/app)
2. Sign in with Google (MFA required for clinical roles)
3. Select **Therapy Session** from the template dropdown
4. Type or dictate your clinical notes
5. Click **📤 Generate SOAP Note**

### Для розробників (VS Code)
1. Install: `ext install synalux-ai.synalux`
2. `Cmd+Shift+P` → **Synalux: Sign In with Google**
3. Chat: `@coder Scaffold a new Next.js route`

### Для клінік, які хочуть 100% локально
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
