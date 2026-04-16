# ✦ Synalux

**La plataforma EHR modular — Nativa en IA, compatible con HIPAA, agnóstica de especialidad**

> Synalux es una plataforma de Historia Clínica Electrónica abierta y modular que adapta su lenguaje clínico, modelos de datos y comportamiento de IA para cualquier especialidad sanitaria — desde terapia ABA hasta pediatría y dermatología. Impulsada por grafos de conocimiento persistentes, más de 26 herramientas multimodales, multi-tenencia sin estado JWT→RLS, y un sandbox de IA "Clínico-en-el-bucle" donde **ninguna salida de IA toca sus datos sin su firma explícita**.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Clinical_Workspace-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Agentic_IDE-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language:** · [English](../../README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← Volver a la versión en inglés](../../README.md)**

---

## ⚡ Los factores "Wow"

* **🛡️ Sandbox de IA — "Clínico-en-el-bucle":** Synalux es el primer EHR donde la IA **no puede tocar sus datos sin su firma**. Cada cambio clínico generado por IA (medicamentos, signos vitales, diagnósticos) se presenta como un `ProposedChange` con un diff rojo/verde Antes→Después. El clínico debe explícitamente **Aplicar** o **Rechazar** cada cambio antes de que se escriba en la base de datos.
* **🔐 RLS sin estado — Escalado horizontal sin sobrecarga de sesión:** El aislamiento de datos multi-inquilino utiliza JWTs firmados mapeados a políticas de Seguridad a Nivel de Fila de Postgres — sin variables de sesión, sin pools de conexión por inquilino.
* **🧠 Memoria semántica persistente:** Construido sobre [Prism MCP](https://github.com/dcostenco/prism-mcp), Synalux nunca sufre de "amnesia de contexto". Recuerda historiales de tratamiento de pacientes entre sesiones.
* **🏥 Morfismo instantáneo de especialidad:** Toda la interfaz cambia su lenguaje clínico, modelos de datos y disposición de módulos según la especialidad seleccionada.
* **🎙️ Ingesta ambiental sin clics:** Los clínicos presionan "Grabar" en su iPad. Synalux usa **WASM Whisper** en el navegador (la PHI nunca sale del dispositivo) para construir informes SOAP/FBA/BIP estructurados en tiempo real.
* **⚡ RBAC a nivel de prompt:** Synalux no solo oculta botones de interfaz — firma criptográficamente las ACL de herramientas.

---

## 🎯 Capacidades clave

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

## 🚀 Primeros pasos

### Para salud y clínicas (aplicación web)
1. → [synalux.ai/app](https://synalux.ai/app)
2. Sign in with Google (MFA required for clinical roles)
3. Select **Therapy Session** from the template dropdown
4. Type or dictate your clinical notes
5. Click **📤 Generate SOAP Note**

### Para desarrolladores (VS Code)
1. Install: `ext install synalux-ai.synalux`
2. `Cmd+Shift+P` → **Synalux: Sign In with Google**
3. Chat: `@coder Scaffold a new Next.js route`

### Para clínicas que quieren 100% local
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
