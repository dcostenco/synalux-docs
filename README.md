# ✦ Synalux

**Run your entire practice from one screen.**

Patient charts, scheduling, billing, team chat, telehealth, clinical documentation — for ABA, pediatrics, mental health, dentistry, PT, dermatology, veterinary, nutrition, and family medicine. HIPAA-compliant. 12 languages. Works offline.

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
Gmail + Outlook + Slack + Discord + Telegram + WhatsApp + SMS — all read and replied to inside Synalux. AI-suggested quick replies. TTS read-aloud for accessibility.

### 💸 Get paid faster
Real-time insurance eligibility. EDI 837P claims. Stripe Connect for copays. Built-in CPT calculator catches the Medicare 8-minute rule and remainder rollover most practices miss.

### 🎥 Telehealth that just works
1080p video on weak Wi-Fi. No patient downloads. Picture-in-picture so you can chart while you talk.

### 📴 Works offline
Trial data on a tablet at a remote school? Collect, save, sync when you're back. Local AI models mean clinical documentation works even when the internet doesn't.

### 🔒 Provably secure — local AI eliminates the biggest PHI risk
Every PHI access is immutably logged with a tamper-evident hash chain. OAuth tokens are AES-256-GCM encrypted.

**Local AI models eliminate PHI exposure at the inference layer** — the single largest compliance gap in AI-powered clinical tools:

| Risk | Cloud AI | Synalux local-first |
|------|----------|-------------------|
| Patient data in LLM prompts | ✅ Sent to vendor | **❌ Never leaves clinic** |
| HIPAA BAA required | Yes (every model vendor) | **Not needed for on-prem** |
| Data breach surface | Cloud API + storage | **Local network only** |
| Inference cost | $2–15/clinician/day | **$0 (local GPU/Mac)** |
| Latency for real-time notes | 1–5s | **~3s (14B) / ~0.5s (1.7B)** |

Enterprise deployments run `prism-coder:14b` and `:32b` on a Mac or GPU server inside the clinic network. All AI inference stays on-premises. No cloud model vendor agreement needed for HIPAA. See [Auth & MFA module](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/auth_mfa.md).

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
| **PrismAAC** | Augmentative & Alternative Communication for users with motor impairments. Standalone repo: [`prism-aac`](https://github.com/dcostenco/prism-aac). Phrase ranking + caregiver-correction harvesting use [Prism v14.0.0 algorithms](https://github.com/dcostenco/prism-coder/blob/main/docs/WOW_FEATURES.md) (spreading activation, ACT-R decay, lesson-rate gotcha persistence). |
| **Prism Coder IDE** | Local-first AI IDE. Standalone macOS/Windows app + web preview at `/coder`. Repo: [`prism-coder`](https://github.com/dcostenco/prism-coder). |
| **Audit Hooks Framework** | Pre-push security audit + pre-execution prompt-audit gate, both grounded in cited Prism v14.0.0 algorithm exports (327 tests pin the constants). Lives at `~/.agent/skills/hooks/`. |
| **Inventory & Assets** | SKU tracking, physical-count audit, purchase orders, fixed-asset depreciation (straight-line + declining balance). |
| **Staff Performance & Payroll** | KPI weights per role, bonus calculations, draft payroll viewer, manual recompute. |
| **Form Builder** | Drag-and-drop custom forms. Undo/redo, preview, publish, per-element validation rules + conditional logic. |
| **General Ledger** | Manual journal entries (balanced double-entry), full paginated ledger, monthly accrual posting with idempotency guard. |
| **Global Deploy** | Push HQ configuration (forms, KPIs, GL rules) to all branch workspaces in one click. |
| **No-Code Dashboard Builder** | Drag widgets to build practice-specific views — 10 specialty templates (ABA, dental, peds, mental health, PT, derm, vet, nutrition, family, general). |
| **Smart Scheduling** | Conflict checking + patient-provider matching. |

---

## Self-hosted AI (Enterprise)

Run Prism models on your own hardware — zero cloud cost, full data sovereignty.

```bash
ollama pull dcostenco/prism-coder:1b7   # 2.2 GB — fast tier
ollama pull dcostenco/prism-coder:14b   # 9.3 GB — standard tier
ollama pull dcostenco/prism-coder:32b   # 19 GB  — enterprise/reasoning
```

Set `LOCAL_LLM_URL=http://localhost:11434` in portal config. Auto-routing: 1.7B → 14B → 32B → cloud fallback.

Routing accuracy — [100-case Prism eval](https://github.com/dcostenco/prism-coder/tree/main/tests/benchmarks/prism-routing-100), 3 rounds, May 2026:

| Model | Accuracy | Avg latency | Invented tools |
|---|---|---|---|
| Sonnet 4 (cloud) | **99%** | 3.2s | 0 |
| prism-coder:14b (local) | **100%** | 9.0s | 0 |
| Opus 4.7 (cloud) | **98%** | 3.0s | 0 |
| prism-coder:32b (local) | **100%** | 3.6s | 0 |
| prism-coder:1b7 (local) | **96%** | 6.0s | 0 |

[Ollama install](https://ollama.com/install)

---

## Plans

| | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| AI assistant | ✅ Gemini 2.5 Flash | ✅ Claude Sonnet 4 ¹ | ✅ Claude Sonnet 4 ¹ | ✅ Claude Sonnet 4 ¹ |
| Mail / Calendar / Drive | ✅ | ✅ | ✅ | ✅ |
| Telehealth | — | ✅ | ✅ + Zoom | ✅ + Zoom |
| Voice (Inworld TTS-2) | ✅ default voice | ✅ all voices | ✅ + clinical dictation | ✅ + voice cloning |
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
| `portal/` | Next.js 15 web app (`synalux.ai`) — 339 test files, 4993 tests — see `portal/README.md` |
| `prism-coder-ide/` | Electron desktop IDE — see `prism-coder-ide/README.md` |
| `synalux-vscode/` | VS Code extension for Synalux integration |
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

## Infrastructure

```
  CLIENTS
  ┌─────────────────────┐  ┌──────────────────────────────┐
  │  prism-aac (iOS/web)│  │  Synalux Portal (web)        │
  │  Vercel             │  │  Vercel                      │
  └──────────┬──────────┘  └──────────────┬───────────────┘
             │ AAC inference               │ portal + AI chat
             ▼                             ▼
  ┌────────────────────────────────────────────────────────┐
  │  SYNALUX ROUTER  (Vercel)                              │
  │                                                        │
  │  POST /api/v1/prism-aac/inference                      │
  │  • JWT auth required  (no anonymous access)            │
  │  • Subscription tier check  (free / standard / advanced / enterprise)   │
  │  • Auto complexity classifier  1.7B → 14B → 32B        │
  │  • Proxy to RunPod  (secret key, never exposed)        │
  └──────────┬─────────────────────────────┬──────────────┘
             │ model inference              │ memory
             ▼                             ▼
  ┌───────────────────────┐  ┌──────────────────────────────┐
  │  RUNPOD SERVERLESS    │  │  prism-mcp SERVER            │
  │                       │  │                              │
  │  prism-coder:14b ✅   │  │  Primary   — Railway         │
  │  (warm, keepalive)    │  │  Standby   — Fly.io          │
  │  prism-coder:32b ✅   │  │  Fallback  — Supabase REST   │
  │  (cold start, pro+)   │  │                              │
  │                       │  │                              │
  └──────────┬────────────┘  │  auto-failover chain         │
             │               └──────────────┬───────────────┘
             ▼                              ▼
  ┌───────────────────────┐  ┌──────────────────────────────┐
  │  ON-DEVICE            │  │  SUPABASE                    │
  │  prism-coder:1b7-v19  │  │  session ledgers             │
  │  Qwen3-1.7B Q8, Ollama│  │  knowledge graph             │
  │  ~50ms · offline      │  │  handoffs, billing, audit    │
  └───────────────────────┘  │  source of truth             │
                              └──────────────────────────────┘
```

## Status

- **Production**: synalux.ai (latest tag: v13.0.0, v14 features shipping)
- **Releases**: [github.com/dcostenco/synalux-private/releases](https://github.com/dcostenco/synalux-private/releases)
- **v14 highlights**: 23 Coming Soon features implemented (inventory, GL, staff performance, form builder, AI replies, TTS, global deploy, compliance resolution); military-grade security audit — 0 CRITICAL findings across 18 new API routes
- **Current sprint**: practice-type-aware onboarding templates (roles, forms, KPIs, chart of accounts per specialty)
- **Pre-release audit**: `npm run check:dead-buttons` + Verified Shipping discipline (see `portal/docs/process/verified-shipping.md` in this private repo)

---

## License
BUSL-1.1 — see [`LICENSE`](https://github.com/dcostenco/synalux-docs/blob/main/LICENSE).
