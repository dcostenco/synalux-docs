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
| Latency for real-time notes | 1–5s | **~1.1s (14B) / ~0.8s (8B) / ~1.6s (1b7)** |

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
| **Ambient AI Documentation** | Speak the session — dictates, structures into SOAP notes, and codes automatically. 16+ languages. |
| **BCBA Command Center** | Touch-optimized field interface for in-session data collection. Works offline. EVV linked to payroll. |
| **Billing & Insurance** | Insurance claims, ERA processing, real-time eligibility, Stripe Connect, Medicare-correct CPT. |
| **Banking Reconciliation** | Double-entry general ledger with bank-feed adapters (VictoriaBank, Banca Transilvania, Amex, Chase). |
| **Telehealth Suite** | 1080p video on weak Wi-Fi. Bandwidth-adaptive. No patient-side downloads. |
| **Patient Portal** | Family signs documents, pays, sees progress reports — from their phone. |
| **PrismAAC** | Augmentative & Alternative Communication for users with motor impairments. Standalone repo: [`prism-aac`](https://github.com/dcostenco/prism-aac) · [App Store](https://apps.apple.com/app/id6764692277). Phrase ranking adapts to each child; caregiver corrections become training data automatically. |
| **Prism Coder IDE** | Local-first AI IDE. Standalone macOS/Windows app + web preview at `/coder`. Repo: [`prism-coder`](https://github.com/dcostenco/prism-coder). |
| **Audit Hooks Framework** | Pre-push security audit + pre-execution safety gate. Every AI action is reviewed before it executes. |
| **Inventory & Assets** | SKU tracking, physical-count audit, purchase orders, fixed-asset depreciation (straight-line + declining balance). |
| **Staff Performance & Payroll** | KPI weights per role, bonus calculations, draft payroll viewer, manual recompute. |
| **Form Builder** | Drag-and-drop custom forms. Undo/redo, preview, publish, per-element validation rules + conditional logic. |
| **General Ledger** | Manual journal entries (balanced double-entry), full paginated ledger, monthly accrual posting with idempotency guard. |
| **Global Deploy** | Push HQ configuration (forms, KPIs, GL rules) to all branch workspaces in one click. |
| **No-Code Dashboard Builder** | Drag widgets to build practice-specific views — 10 specialty templates (ABA, dental, peds, mental health, PT, derm, vet, nutrition, family, general). |
| **Smart Scheduling** | Conflict checking + patient-provider matching. |

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
Standard → Gemini 2.5 Flash · Advanced/Enterprise → Gemini 2.5 Pro.
Free tier autocorrect/prediction runs on Gemini 2.5 Flash-Lite for cost
+ latency (Romanian diacritics + multilingual coverage validated).

[See full pricing →](https://synalux.ai/pricing)

---

## Self-hosted AI (Enterprise)

Run Prism models on your own hardware — zero cloud cost, full data sovereignty.

```bash
ollama pull dcostenco/prism-coder:1b7   # 1.1 GB  · ~1.6s · any device
ollama pull dcostenco/prism-coder:8b    # 4.7 GB  · ~0.8s · iPhone/iPad 8GB
ollama pull dcostenco/prism-coder:14b   # 8.4 GB  · ~1.1s · Mac M2+ / iPad Pro 16GB
ollama pull dcostenco/prism-coder:32b   # 16 GB   · ~0.8s · Mac M2 Ultra+ (30B-A3B MoE)
```

Set `LOCAL_LLM_URL=http://localhost:11434` in portal config.

**Desktop/server cascade** (routing): 14B → 32B → Claude Sonnet 4 fallback (100% served locally, cloud engaged 0%)  
**Mobile/offline cascade** (routing): 14B → 8B → 1b7  
**Code generation cascade** (IDE): prism-coder:14b → prism-coder:32b → Claude Sonnet 4 fallback

Routing accuracy — [102-case Prism eval](https://github.com/dcostenco/prism-coder/tree/main/tests/benchmarks/prism-routing-100), v36/v7 system prompt, 3-seed mean, May 2026:

| Model | Accuracy | Latency | AAC | Edge cases | Tier |
|---|---|---|---|---|---|
| **14B→32B cascade** (local) | **100.0%** | ~1.1s¹ | **100%** | **100%** | Desktop primary |
| **prism-coder:32b** v7 MoE (local) | **100.0%** | 0.8s | **100%** | **100%** | Desktop tier 2 |
| **prism-coder:8b** v36 (local) | **100.0%** | 0.8s | **100%** | **100%** | Mobile tier 2 |
| **prism-coder:14b** v36 (local) | **100.0%** | 1.1s | **100%** | **100%** | Desktop tier 1 |
| prism-coder:1b7 v42 (local) | **100.0%** | 1.6s | **100%** | **100%** | On-device tier 3 |
| Sonnet 4 (cloud) | 99% | 3.2s | 100% | 83% | Cloud primary |
| Claude Opus 4.7 (cloud) | 98.3% | 3.0s | 100% | 83% | Cloud fallback |

¹ 99% of requests served by 14B at 1.1s; 32B handles the remaining 1%. Opus engaged: 0%. [Cascade eval source →](https://github.com/dcostenco/prism-coder/tree/main/tests/benchmarks/cascade-14b-32b-opus/cascade_eval.py)

**All fine-tuned models now beat Opus on edge cases** (100% vs 83%) — compound/multi-intent routing where Opus confuses similar tools. All sizes score 100% on AAC and 100% on edge cases.

[Per-model solo eval →](https://github.com/dcostenco/prism-coder/tree/main/tests/benchmarks/prism-routing-100/benchmark.py) · [Ollama install](https://ollama.com/install)

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
- [Voice / TTS Architecture](https://github.com/dcostenco/synalux-docs/blob/main/docs_source_en/voice_tts_architecture.md) — 5-tier fallback (Inworld → Azure Neural → Kokoro → Web Speech → espeak)
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
  │  • Tier check: free / standard / advanced / enterprise │
  │  • Auto complexity classifier  1b7 → 8b → 14b → 32b   │
  │  • Cloud: OpenRouter (Claude/Gemini, key hidden)       │
  └──────────┬─────────────────────────────┬──────────────┘
             │ model inference              │ memory
             ▼                             ▼
  ┌───────────────────────┐  ┌──────────────────────────────┐
  │  OPENROUTER / LOCAL   │  │  prism-mcp SERVER            │
  │                       │  │                              │
  │  Cloud: Claude Sonnet │  │  Primary   — Railway         │
  │  Local:  prism-coder  │  │  Standby   — Fly.io          │
  │   :32b(100%):14b(100%)│  │  Fallback  — Supabase REST   │
  │   :8b(100%) :1b7(100%)│  │                              │
  │                       │  │                              │
  └──────────┬────────────┘  │  auto-failover chain         │
             │               └──────────────┬───────────────┘
             ▼                              ▼
  ┌───────────────────────┐  ┌──────────────────────────────┐
  │  ON-DEVICE            │  │  SUPABASE                    │
  │  prism-coder:1b7      │  │  session ledgers             │
  │  1.7B Q4_K_M, Ollama  │  │  knowledge graph             │
  │  ~50ms · offline      │  │  handoffs, billing, audit    │
  └───────────────────────┘  │  source of truth             │
                              └──────────────────────────────┘
```

## Tech Notes — Service Routing

### LLM Backends

| Surface | Primary | Fallback | Local |
|---|---|---|---|
| AI Chat (web) | Gemini 2.5 Flash (direct API) | OpenRouter → Claude Sonnet 4 | prism-coder:14b via Ollama |
| AI Chat (paid tiers) | Claude Sonnet 4 (OpenRouter) | Claude Haiku 3.5 (OpenRouter) | prism-coder:14b via Ollama |
| Prism Coder (tool-calling) | Claude Haiku 3.5 (OpenRouter) | — | prism-coder:14b via Ollama |
| TTS Steering | Claude Haiku 3.5 (OpenRouter) | Surface default (no model) | — |
| Prism AAC | Local prism-coder:14b | Gemini 2.5 Flash / Claude Sonnet 4 | prism-coder:8b / :1b7 |

### Web Search

| Surface | Primary | Fallback |
|---|---|---|
| AI Chat `@search` | Firecrawl | — |
| Prism MCP agents (cloud) | Firecrawl | — |
| Prism MCP server (local) | Firecrawl (via MCP tools) | — |
| Clinical research | PubMed + ERIC + Semantic Scholar | DuckDuckGo |

### TTS (Text-to-Speech)

| Tier | Engine | Offline |
|---|---|---|
| 1 | Inworld TTS-2 (cloud, 100+ langs) | — |
| 1.2 | Azure Neural TTS (cloud fallback) | — |
| 1.5 | Kokoro-82M neural (WASM offline) | en/es/fr/pt/ja/zh |
| 2 | OS Web Speech API | all |
| 3 | WASM espeak-ng | all |

Subsidized languages (free Inworld): `ro` `uk` `ru` `de` `ko` `ar`

### Other Services

| Service | Provider | Purpose |
|---|---|---|
| Payments | Stripe | Subscriptions, checkout, billing portal |
| Email | Resend | Transactional (invites, shares, meetings) |
| Video | LiveKit | Telehealth, case conferences |
| SMS | Twilio | Emergency alerts, caregiver notifications |
| Fax | SRFax / Phaxio / Documo | Healthcare referrals, prior auth |
| Translation | Offline phrase dictionary (1,261 × 20 langs) | AAC, Watch |

## Status

- **Production**: synalux.ai (latest tag: v14.0.0)
- **Releases**: [github.com/dcostenco/synalux-private/releases](https://github.com/dcostenco/synalux-private/releases)
- **v14 highlights**: 23 Coming Soon features implemented (inventory, GL, staff performance, form builder, AI replies, TTS, global deploy, compliance resolution); military-grade security audit — 0 CRITICAL findings across 18 new API routes
- **Current sprint**: practice-type-aware onboarding templates (roles, forms, KPIs, chart of accounts per specialty)
- **Pre-release audit**: `npm run check:dead-buttons` + Verified Shipping discipline (see `portal/docs/process/verified-shipping.md` in this private repo)

---

## License
BUSL-1.1 — see [`LICENSE`](https://github.com/dcostenco/synalux-docs/blob/main/LICENSE).
