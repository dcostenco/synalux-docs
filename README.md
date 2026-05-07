# ✦ Synalux

**Run your entire practice from one screen.**

Patient charts, scheduling, billing, team chat, telehealth, clinical documentation — for ABA, pediatrics, mental health, dentistry, PT, and dermatology. HIPAA-compliant. 12 languages. Works offline.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Try_It-Free-43e97b?style=for-the-badge" alt="Try Free"></a>
  <a href="https://synalux.ai/pricing"><img src="https://img.shields.io/badge/Pricing-See_Plans-764ba2?style=for-the-badge" alt="Pricing"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/HIPAA-Ready-blue?style=for-the-badge" alt="HIPAA"></a>
</p>

🌐 **Translations:** [Español](docs/i18n/README_es.md) · [Français](docs/i18n/README_fr.md) · [Português](docs/i18n/README_pt.md) · [Română](docs/i18n/README_ro.md) · [Українська](docs/i18n/README_uk.md) · [Русский](docs/i18n/README_ru.md) · [Deutsch](docs/i18n/README_de.md) · [日本語](docs/i18n/README_ja.md) · [한국어](docs/i18n/README_ko.md) · [中文](docs/i18n/README_zh.md) · [العربية](docs/i18n/README_ar.md)

---

## What you get

### 🎙 Stop typing notes
Speak the session. Synalux dictates, structures into SOAP, codes, and files it. Audio never leaves your device.

### 📅 One calendar, every account
Google Calendar + Outlook in one view. Schedule with **Google Meet, Microsoft Teams, or Zoom** in one click — never bounces you out to another tab.

### 📨 Mail without switching tabs
Gmail + Outlook + Slack + Discord + Telegram + WhatsApp + SMS — all read and replied to inside Synalux.

### 💸 Get paid faster
Real-time insurance eligibility. EDI 837P claims. Stripe Connect for copays. Built-in CPT calculator catches the Medicare 8-minute rule and remainder rollover most practices miss.

### 🎥 Telehealth that just works
1080p video on weak Wi-Fi. No patient downloads. Picture-in-picture so you can chart while you talk.

### 📴 Works offline
Trial data on a tablet at a remote school? Collect, save, sync when you're back.

### 🔒 Provably secure
Every PHI access is immutably logged with a tamper-evident hash chain. OAuth tokens are AES-256-GCM encrypted. See the public [Auth & MFA module page](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/auth_mfa.md); full Pattern C OAuth token isolation spec lives in the private engineering repo.

---

## Try it

| Surface | URL | What |
|---|---|---|
| **Web app** | [synalux.ai/app](https://synalux.ai/app) | Full clinical UI |
| **Mail** | [synalux.ai/mail](https://synalux.ai/mail) | Unified mailbox |
| **Calendar** | [synalux.ai/calendar](https://synalux.ai/calendar) | Cross-provider scheduling |
| **Drive** | [synalux.ai/drive](https://synalux.ai/drive) | Practice file storage |
| **Chat** | [synalux.ai/chat](https://synalux.ai/chat) | AI assistant + messaging integrations |
| **Coder** | [synalux.ai/coder](https://synalux.ai/coder) | Browser IDE preview; desktop app for full editor |
| **Patient Portal** | [synalux.ai/patient-portal](https://synalux.ai/patient-portal) | Where families sign forms + pay bills |

---

## Modules

| | What it does |
|---|---|
| **Ambient AI Documentation** | Whisper WASM transcription, automatic SOAP structuring, ABC data extraction. 16+ languages. |
| **BCBA Command Center** | Touch-optimized field interface. Trial data offline (Dexie.js + IndexedDB). EVV linked to payroll. |
| **Billing & Insurance** | EDI 837P, 835 ERA parser, real-time eligibility, Stripe Connect, Medicare-correct CPT. |
| **Banking Reconciliation** | Double-entry GL. Native bank-feed adapters (VictoriaBank, Banca Transilvania, Amex, Chase). |
| **Telehealth Suite** | LiveKit SFU. Bandwidth-adaptive. No patient-side downloads. |
| **Patient Portal** | Family signs documents, pays, sees progress reports — from their phone. |
| **PrismAAC** | Augmentative & Alternative Communication for users with motor impairments. Standalone repo: [`prism-aac`](https://github.com/dcostenco/prism-aac). |
| **Prism Coder IDE** | Local-first AI IDE. Standalone macOS/Windows app + web preview at `/coder`. Repo: [`prism-coder`](https://github.com/dcostenco/prism-coder). |
| **No-Code Dashboard Builder** | Drag widgets to build BCBA / Admin / RBT views. |
| **Smart Scheduling** | Conflict checking + patient-provider matching. |

---

## Plans

| | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| AI assistant | ✅ Gemini 2.5 Flash | ✅ Claude Sonnet 4 ¹ | ✅ Claude Sonnet 4 ¹ | ✅ Claude Sonnet 4 ¹ |
| Mail / Calendar / Drive | ✅ | ✅ | ✅ | ✅ |
| Telehealth | — | ✅ | ✅ + Zoom | ✅ + Zoom |
| Voice (Inworld 2.0) | ✅ default voice | ✅ all voices | ✅ + clinical dictation | ✅ + voice cloning |
| BoldSign e-Signature | — | — | ✅ 7 templates | ✅ unlimited |
| Browser automation | — | — | ✅ | ✅ |
| Banking & GL | — | — | ✅ | ✅ |
| Multi-workspace HQ | — | — | — | ✅ |

¹ Tier-aware automatic fallback when Anthropic API is unavailable:
Standard → Gemini 3 Flash Preview · Advanced/Enterprise → Gemini 3 Pro Preview.
Free tier autocorrect/prediction runs on Gemini 2.5 Flash-Lite for cost
+ latency (Romanian diacritics + multilingual coverage validated).

[See full pricing →](https://synalux.ai/pricing)

---

## For developers

This is a monorepo (private engineering repo). Public-facing docs live at
[github.com/dcostenco/synalux-docs](https://github.com/dcostenco/synalux-docs)
— including 25+ per-module pages under
[`docs_source_en/`](https://github.com/dcostenco/synalux-docs/tree/main/docs_source_en).

Top-level layout (private):

| Path | What |
|---|---|
| `portal/` | Next.js 15 web app (`synalux.ai`) — see `portal/README.md` |
| `prism-coder-ide/` | Electron desktop IDE — see `prism-coder-ide/README.md` |
| `supabase/` | Top-level migrations |
| `docs/` | i18n README translations + internal architecture docs |

Quickstart for the portal:
```bash
cd portal
npm install
npm run dev    # http://localhost:3000
```

Full env-var matrix, security docs, and the Verified Shipping discipline are in `portal/README.md` (private repo).

---

<details>
<summary>📚 Detailed docs</summary>

**Public** ([synalux-docs](https://github.com/dcostenco/synalux-docs)) — 60+ pages in `docs_source_en/`. Highlights:
- [Auth & MFA](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/auth_mfa.md) — sign-in, TOTP/passkey, break-glass override
- [Voice / TTS Architecture](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/voice_tts_architecture.md) — 4-tier fallback (Inworld → Kokoro → Web Speech → espeak)
- [Telehealth (LiveKit)](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/telehealth_livekit.md) — bandwidth-adaptive video
- [Language Support Matrix](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/language_support.md) — coverage per surface across 25 locales
- [Prism AAC](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/prism_aac.md), [Mail](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/mail.md), [Drive](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/drive.md), [Calendar](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/calendar.md), and [more](https://github.com/dcostenco/synalux-docs/tree/main/docs_source_en).

**Internal** (this private repo, not publicly accessible):
- `portal/docs/security/` — OAuth token isolation (Pattern C), audit chain integrity, KEK rotation, encryption design
- `portal/docs/process/verified-shipping.md` — Verified Shipping discipline
- `portal/docs/process/copy-ui-parity.md` — Rule 11: every feature claim must have a clickable flow
- `portal/docs/PHASE_3_PORTAL_ENDPOINTS.md` — Synalux portal API endpoints reference
- `portal/docs/tts-1.5-vs-tts-2.md` — Inworld TTS upgrade rationale
- `docs/COMPLIANCE_MATRIX.md` — HIPAA / regulatory matrix
- `docs/feature-gap-assessment.md` — vs CentralReach / SimplePractice / WebPT / Healthie
- `docs/web_manual.md` — end-user manual
- `docs/Synalux_Manual_Test_Cases.docx` — manual test plan

The original 2443-line README is preserved in git history. To browse the prior version: `git show HEAD~1:README.md`.

</details>

---

## Status

- **Production**: synalux.ai (latest deploy: v12.4.0)
- **Releases**: [github.com/dcostenco/synalux-private/releases](https://github.com/dcostenco/synalux-private/releases)
- **Current sprint**: chat-provider expansion (Telegram, SMS, WhatsApp, FB Messenger, Viber)
- **Pre-release audit**: `npm run check:dead-buttons` + Verified Shipping discipline ([`portal/docs/process/verified-shipping.md`](portal/docs/process/verified-shipping.md))

---

## License
BUSL-1.1 — see [LICENSE](LICENSE).
