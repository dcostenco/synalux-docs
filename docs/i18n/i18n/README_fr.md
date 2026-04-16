# ✦ Synalux

**La plateforme DSE modulaire — Native en IA, conforme HIPAA, agnostique de spécialité**

> Synalux est une plateforme de Dossier de Santé Électronique ouverte et modulaire qui adapte son langage clinique, ses modèles de données et le comportement de son IA à toute spécialité médicale — de la thérapie ABA à la pédiatrie en passant par la dermatologie.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Clinical_Workspace-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Agentic_IDE-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language:** · [English](README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← Retour à la version anglaise](README.md)**

---

## ⚡ Les facteurs "Wow"

* **🛡️ Bac à sable IA — "Clinicien dans la boucle" :** Synalux est le premier DSE où l'IA **ne peut pas toucher vos données sans votre signature**. Chaque modification clinique générée par l'IA est présentée comme un `ProposedChange` avec un diff rouge/vert Avant→Après.
* **🔐 RLS sans état — Mise à l'échelle horizontale sans surcharge de session :** L'isolation des données multi-locataires utilise des JWT signés mappés aux politiques RLS de Postgres.
* **🧠 Mémoire sémantique persistante :** Construit sur [Prism MCP](https://github.com/dcostenco/prism-mcp), Synalux ne souffre jamais d'"amnésie de contexte".
* **🏥 Morphisme instantané de spécialité :** L'interface entière change son langage clinique selon la spécialité sélectionnée.
* **🎙️ Saisie ambiante sans clic :** Les cliniciens appuient sur "Enregistrer" sur leur iPad. Synalux utilise **WASM Whisper** dans le navigateur.
* **⚡ RBAC au niveau du prompt :** Synalux signe cryptographiquement les ACL des outils.

---

## 🎯 Capacités clés

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

## 🚀 Pour commencer

### Pour la santé et les cliniques (application web)
1. → [synalux.ai/app](https://synalux.ai/app)
2. Sign in with Google (MFA required for clinical roles)
3. Select **Therapy Session** from the template dropdown
4. Type or dictate your clinical notes
5. Click **📤 Generate SOAP Note**

### Pour les développeurs (VS Code)
1. Install: `ext install synalux-ai.synalux`
2. `Cmd+Shift+P` → **Synalux: Sign In with Google**
3. Chat: `@coder Scaffold a new Next.js route`

### Pour les cliniques souhaitant 100% local
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
