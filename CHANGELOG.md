# Synalux — Changelog

## [Unreleased] — Phase 1-4 (Model Training)

### Planned
- SFT fine-tuning on Prism reasoning traces
- GRPO alignment for tool-use accuracy
- Benchmark evaluation (retrieval, tool call, reasoning, efficiency)
- GGUF export + Ollama modelfile
---

## [0.13.0] - 2026-04-18

### 📱 Mobile UI Hardening & Global AI Assistant (Portal v0.13.0)

#### Added
- **Global Floating AI Assistant** — accessible across all portal modules via FAB
  - Fixed-position anchoring with Safe Area Inset (`env(safe-area-inset-bottom)`) accounting for iOS Home Indicator
  - Sticky context retaining history via local DOM state to survive modal toggling
- **Tier-Gated AI Routing**
  - Paid/Advanced Tiers routed to `gemini-3.1-pro-preview` for clinical reasoning
  - Free and Standard Tiers routed to `gemini-2.5-flash`
- **Native OS Predictive Text** — optimized inputs across all modules
  - Added `spellCheck={true}` and `autoCorrect="on"` to core FormField
  - Uses native device keyboard algorithms instead of custom JS ghost-text, ensuring HIPAA compliance and zero layout shifts
- **Update Tool Count** — increased platform capabilities from 15 to 17 tools across 12 UI languages.

#### Fixed
- **Mobile UI Overlaps** — resolved Z-index issues between the Floating Chat (z-100) and native toolbars
- **TypeScript & CI/CD**
  - Resolved `dbUserId` / `session.user.id` discrepancies in `layout.tsx`
  - Fixed pre-initialized Supabase instances being incorrectly awaited
  - Added missing `search` state params to resolves builds in Next.js pages

---
## [0.12.14] - 2026-04-15

### 🛡️ Adversarial Behavioral Hardening — ABA Protocol v4 (Extension v0.12.14)

#### Added
- **282-Test Behavioral Verification Suite** — comprehensive regression coverage:
  - `tests/v43-aba-precision.test.ts` — 198 tests (Rules 1-7, negation variants, sycophancy, rewrite verification)
  - `tests/intent-classification.test.ts` — 84 tests (intent routing, cross-rule validation, Apr 15 regressions)
- **24 Forbidden Openers** — negation + affirmative filler detection:
  - Negation: I can't, Unfortunately, I apologize, Regrettably, I'm afraid, As an AI, I am prohibited
  - Sycophancy: Sure., Certainly, I can certainly + combo patterns
- **XML Prompt Injection Defense** — `<anti_pattern>` / `<desired_pattern>` / `<user_input>` tags stripped from user input
- **`<user_input>` Message Isolation** — user messages wrapped in XML tags before LLM context
- **Uncertainty Escape Hatch** — "Missing: [item]" for specific required variables only
- **IF/ELSE Conflict Resolution** — replaces mathematical precedence with structural logic
- **Binary Question Exception** — affirmative words permitted only for Yes/No answers

#### Changed
- **Rule 4** — renamed "No Negation/Filler Lead", covers both negation AND sycophancy
- **ABA Protocol** — 7 rules synchronized across all 3 injection points (portal, VS Code, Prism)
- **Few-shot contamination fix** — BAD→GOOD examples wrapped in XML `<anti_pattern>` tags

#### Security
- XML injection sanitization in `sanitizeMessages()` (route.ts)
- Anti-injection instruction in system prompt
- Passed 2-round adversarial code review (10 questions each round)

---

## [0.2.0] — 2026-04-15

### 🏥 ABA Practice Management & Voice-to-Action Pipeline (Portal v0.2.0)

#### Added
- **ABA Practice Management tools** — 8 robust AI-driven tools:
  - Patient CRUD, appointments, session notes, authorizations, and reports
- **Voice-to-Action Communication** — 4 new communication tools:
  - `call`, `SMS`, `email`, and `schedule` integrated with Twilio and Resend
- **Responsive Mobile-First UX QA** — Deep UI/UX visual validation:
  - Ensured tap-target button sizing (minimum 44px) and responsive views across desktop (1440x900) and iPhone portrait/landscape
- **Adversarial Security Preparedness**:
  - Automatically bundled a `repomix` archive of `tools/` and `portal/`
  - Authored an adversarial HIPAA/RBAC `REVIEW_PROMPT.md` for external auditing

---

## [0.12.2] — 2026-04-14

### 🌍 Multilingual Videos + Web Voice Input + Windows Auth Fix (Extension v0.12.2)

#### Added (Portal)
- **🎤 Voice input on web** — AI Chat now supports browser-native speech recognition
  - Uses Web Speech API (`SpeechRecognition` / `webkitSpeechRecognition`)
  - Works in Chrome, Edge, Safari (not Firefox)
  - Click 🎤 to start → 🔴 pulsing indicator → transcript streams into input in real-time
  - Click again to stop; supports continuous mode with interim results
- **📖 Text-based tutorial** — 5-step walkthrough below video guides on `/docs`
  - Account creation, role selection, dashboard, AI Chat, VS Code extension
  - Numbered steps with purple accent borders and bullet lists
- **🌐 12-language promo videos** — neural TTS narration in each language
  - EN, ES, FR, DE, PT, ZH, JA, KO, AR, RO, UK, RU
  - Audio-synced: each scene's video duration matches its narration exactly
  - Docs page auto-links to user's language (`/synalux_demo_{locale}.mp4`)
- **🎯 Role-based sidebar** — navigation filtered by user role
  - Clinical (BCBA, RBT, Office Manager): full access to all features
  - Technical (Developer, DevOps, QA, Writer, Security, Planner): AI Chat + Team Chat only
  - Restricted: AI Chat only
- **🧠 AI Chat model selector** — matches VS Code extension capabilities
  - 6 cloud models: Auto, Gemini 2.5 Flash, Claude Sonnet 4, GPT-4o, DeepSeek V3, Llama 4
  - 4 local models: DeepSeek R1 32B/14B, Qwen Coder 32B/14B
  - Backend toggle (☁️ Cloud / 🔒 Local)
  - 📎 File attachment support (.txt, .md, .json, .csv, .py)
- **📚 Comprehensive documentation** — 8 sections with full content:
  - Getting Started, Healthcare, API Reference, VS Code Extension
  - Billing, Security, i18n, Changelog (was all placeholder text)
  - Tools Reference page: dark theme with purple accents, green code blocks

#### Fixed
- **🎬 Video/audio sync** — regenerated all videos using per-scene audio-duration matching
  - Old: flat 15s per scene regardless of narration length → audio drifted from visuals
  - New: scene duration = actual TTS audio + 0.5s pause → perfect lip-sync
- **Gemini fallback** — switched from deprecated `gemini-2.0-flash` to `gemini-2.5-flash`

#### Fixed (Extension v0.12.2)
- **🚨 Windows auth timeout** — `vscode.env.openExternal()` wrapped in 8s race timeout
  - Error was: "Timed out waiting for authentication provider 'google' to register"
  - Fallback: shows "Copy URL" button for manual browser navigation
  - Root cause: VS Code's internal auth subsystem not ready on some Windows installs

---

## [0.12.0] — 2026-04-14

### 🎙️ Voice & Conversation Mode Fix — Direct Native STT (Extension v0.12.0)

#### Fixed (Critical)
- **🚨 Voice record button** — was hanging with no output for 30+ seconds
  - **Root cause**: `avrecorder` blocked for full duration, then `avstt` transcription timed out
  - **Fix**: Extension now spawns `avlisten` binary directly for single-shot recording
  - Listens in real-time, returns first complete utterance, then kills process
  - Falls back to Python pipeline only if avlisten binary missing
- **🚨 Conversation mode** — was completely non-functional (no activity after button press)
  - **Root cause**: Fatal architecture flaw — `dispatchTool()` spawns a **new Python process** for every call. `conversation_start` stored `avlisten` subprocess reference in a Python global, but that process exited immediately. `conversation_read` ran in a different process where the reference was `None`, always returning `no_data`
  - **Fix**: Extension now spawns `avlisten` directly as a TypeScript `ChildProcess` and reads JSON lines from stdout via `readline.createInterface` — zero polling, real-time event streaming
  - Orphan protection: avlisten killed on panel close, extension deactivation, or conversation stop
- **🚨 avlisten SIGABRT crash** — `SFSpeechRecognizer.requestAuthorization()` caused fatal crash in CLI/headless context
  - **Fix**: Removed `requestAuthorization` callback (same pattern as `avstt` fix), check `authorizationStatus()` only

#### Changed
- **Voice architecture** — Python `voice.py` no longer manages avlisten subprocess lifecycle
  - New `compile_avlisten`/`compile_avstt`/`compile_avrecorder` actions for TypeScript to request binary compilation
  - `conversation_start`/`stop`/`read` kept in Python for CLI testing only (deprecated for MCP use)
- **Real-time streaming** — conversation mode now uses event-driven stdout readline (was 150ms polling→Python subprocess→no_data)

#### Also Added
- **Role Management UI** — admin-only dashboard section for managing workspace roles
  - Edit role display names, descriptions, and skills (comma-separated input)
  - Delete custom roles (default roles protected)
  - Glassmorphism-styled role cards with skill chip visualization
- **Role-aware welcome panel** — extension chat panel shows current user's skill capabilities
  - Skills fetched from `/api/v1/roles?me=true` (skills field added to API response)
  - Rendered as styled chips under role title in the welcome screen
  - XSS-safe rendering via `textContent` (no innerHTML for user data)
- **`role-skills.ts`** — canonical role→skills mapping module for seed data and fallback
- **Roles API** — `GET /api/v1/roles?me=true` now returns `skills[]` alongside `tools[]`
- **Voice transcription caching** — cached STT backend selection skips slow fallback chain

---

## [0.10.8] — 2026-04-14

### 🧠 Smart Orchestrator — Zero-Config Model Routing (Extension v0.10.8)

#### Added
- **Smart Orchestrator** — auto-classifies prompts and routes to the best model:
  - `coding` → qwen2.5-coder (local) or GPT-4.1 Mini (cloud)
  - `reasoning` → deepseek-r1 (local) or Gemini 3.1 Pro (direct)
  - `clinical` → always local (HIPAA enforcement)
  - `quick` → Gemini Flash (fastest available)
  - `general` → Gemini 2.5 Flash or cloud tier default
- **Context window safety** — auto-truncates conversation history to 90% of each model's token limit
  - Model context limits map (30+ models: Gemini 1M, GPT-4.1 1M, Claude 200K, local 32K-128K)
  - System prompt always preserved; oldest messages dropped first
- **Tier-based model ACL** — portal validates user's chosen model against subscription permissions
  - `TIER_ALLOWED_MODELS` map: free (1 model), standard (8), pro (13), advanced (13), enterprise (15+)
- **Pro tier** added to `CLOUD_TIER_MODELS` (was missing — `pro` users fell back to `free`)
- **Usage badge** now shows orchestration reason (e.g., `coding · local — qwen2.5-coder:32b — 1,247 tokens`)

#### Fixed
- **Usage indicator** — fixed `_meta` telemetry never sent (duplicate `const durationMs` crashed `finally` block)
- **Usage indicator race** — webview now falls back to last `.message.assistant` DOM element when `done` arrives before `usage`
- **Duplicate Read Aloud/Translate** — guarded against double `done` events from SSE stream
- **Model routing** — portal now respects user's chosen model instead of always forcing tier default
- **Team Chat** — unlocked for `standard` and `pro` plans (was `advanced`/`enterprise` only)
- **Updated cloud tier defaults** — free: `gemma-3-12b-it`, standard: `gpt-4.1-mini`, enterprise: `claude-opus-4`

#### Changed
- **System prompt** — lists all 20 MCP tools by name so models know their full capabilities
  - Professional dev tool identity (not consumer chatbot) — eliminates model refusals on legitimate tasks
- **Button UI redesign** — SVG icons replace emoji on all input buttons (Attach, Paste, Voice, Conversation, Send)
  - Hover effects with color transitions and tooltip labels
  - Consistent 38px rounded glass-style buttons

#### Documentation
- **Smart Orchestrator section** added to portal docs page (`/docs`)
- English i18n keys added for orchestrator documentation

---

## [0.10.0] — 2026-04-14

### 💬 HIPAA-Compliant Team Chat — Secure Workspace Messaging (Extension v0.10.0)

#### Added
- **Team Chat tab** — new tab in chat panel alongside AI Chat for workspace messaging
  - Channel-based messaging (#general, #clinical, #dev, etc.)
  - Member sidebar with avatar initials and role badges
  - Unread count badges on channels and tab
- **@mention system** — structured mention autocomplete
  - `@username` — individual (email prefix, no domain for privacy)
  - `@role` — role groups (`@dev`, `@clinician`, `@reviewer`)
  - `@all` — broadcast to entire workspace
- **😀 Emoji picker** — 8 categories, ~200 emojis (smileys, affection, expressions, states, hands, hearts, medical, misc)
- **Session sharing** — ▶ button shares current AI conversation to team channel (stores `session_id` reference only — no transcript duplication)
- **File attachments** — 📎 button with MIME allowlist (PDF, PNG, JPEG, GIF, TXT, CSV), 10MB max
- **Visual message indicators** — colored left borders (blue=you, purple=others, orange=mentions, green=sessions, teal=system)
- **Long-polling** — 4-second API polling for real-time message updates

#### Security (HIPAA Compliance)
- **🔐 Pro+ only** — server-side plan gate (advanced/enterprise tiers)
- **No RLS dependence** — all authorization in TypeScript API layer (custom JWTs bypass Supabase `auth.uid()`)
- **IDOR prevention** — `workspace_id` verified on every file download request
- **No ReDoS** — client sends structured `mentions[]` array; server validates, never regex-parses content
- **PHI single-source-of-truth** — session shares store ID reference only (no transcript in `team_messages`)
- **Supabase TDE** — encryption at rest at database layer
- **Audit trail** — all send/read/delete/upload operations logged to `rbac_audit_log`
- **Soft delete** — messages never hard-deleted before 7-year retention (pg_cron weekly cleanup)
- **File safety** — MIME allowlist, 10MB limit, PRIVATE bucket, 15-min signed URLs
- **Channel limits** — max 50 per workspace, 30-char names (`^[a-z0-9-]+$`)
- **No DB exposure** — long-polling via authenticated Next.js API (no Supabase websocket access)

#### API Routes
- `POST/GET /api/v1/messages` — send/fetch messages (JWT, plan gate, RBAC)
- `POST/GET /api/v1/messages/channels` — create/list channels (admin-only creation)
- `GET /api/v1/messages/members` — mention autocomplete (username only, no email)
- `POST /api/v1/messages/read` — mark channel as read
- `POST/GET /api/v1/messages/upload` — file upload/download with signed URLs

#### Database
- `team_channels` — workspace-scoped chat rooms
- `team_messages` — messages with structured mentions, attachments, session refs
- `team_message_reads` — per-user per-channel read tracking
- SQL migration: `supabase/migrations/20260414_team_chat.sql`

---

## [0.9.0] — 2026-04-13

### 🎙️ Continuous Conversation Mode — Hands-Free Clinical Intake (Extension v0.9.0)

#### Added
- **Continuous conversation mode** — 🗣️ toggle button for hands-free clinical intakes
  - Streaming `SFSpeechRecognizer` with live partial transcription
  - VAD (Voice Activity Detection) — 2.5s silence threshold for utterance boundary detection
  - Configurable via `synalux.voiceSilenceMs` setting (500ms–10s)
  - Auto-send: transcribed speech → chat message → AI responds in text (no TTS)
  - Spacebar/Enter instant-send to skip silence wait
  - "📋 Generate SOAP Note from Session" button on conversation end
  - Full session transcript accumulation

#### Security (HIPAA Compliance)
- **🚨 On-device only** — `requiresOnDeviceRecognition = true` (no audio sent to Apple servers)
  - Fail-closed if on-device recognition unavailable for selected language
- **Forced local backend** — AI responses via Ollama only during conversation mode (no ambient PHI to cloud)
- **Orphan process protection** — `avlisten` auto-terminates on broken stdin pipe (parent crash)
  - Python `atexit` handler sends SIGKILL to zombie processes
- **Cross-process mic lock** — `~/.cache/synalux/mic.lock` prevents concurrent mic allocation

#### Technical
- **New Swift binary**: `avlisten` (compiled to `~/.cache/synalux/avlisten`)
  - `AVAudioEngine` + `SFSpeechAudioBufferRecognitionRequest` for streaming STT
  - JSON line output protocol: `partial`, `final`, `silence`, `listening`, `error`, `terminated`
  - Auto-restart recognition task during silence gaps (handles Apple's 1-min limit)
  - SIGTERM/SIGINT graceful shutdown
- **New voice tool actions**: `conversation_start`, `conversation_stop`, `conversation_read`
- **New setting**: `synalux.voiceSilenceMs` (default: 2500)
- TTS suppressed during conversation mode
- "Read Aloud" button hidden during conversation mode

#### Voice Commands & Settings Panel
- **Start/Stop Listening** — `synalux.startListening` / `synalux.stopListening` (Cmd+Shift+L)
- **Natural language triggers** — type or say "start listening" / "stop listening" in chat (12 languages)
- **⚙️ Settings strip** — in-panel toggleable bar with:
  - Language selector (12 languages with flag icons)
  - Backend selector (Local / Cloud / Gemini)
  - All selections persist to VS Code user settings across sessions
- **New setting**: `synalux.backend` (local / cloud / gemini)

#### i18n Updates
- Updated `feat_voice_desc` and `feat_healthcare_desc` in all 12 portal languages
  to highlight continuous conversation mode for clinical intakes

#### Session Audio Recording (HIPAA-Compliant)
- **Opt-in recordings** — `synalux.recordSessions` setting (default: off — data minimization)
- **Patient consent dialog** — modal confirmation before recording (HIPAA + state wiretap compliance)
- **AES-256-GCM encryption** — raw audio encrypted immediately on stop, plaintext deleted
- **Session-bound storage** — recordings organized by session ID in `~/.cache/synalux/recordings/`
- **Multiple recordings per session** — each gets unique timestamp, shares session folder
- **New voice tool actions**: `record_list` (list encrypted recordings), `record_decrypt` (decrypt for playback)
- **HIPAA audit log** — all encrypt/decrypt operations logged
- **Swift binary updated** — `avlisten` now supports `--record=/path` flag for audio file capture

#### Visual Message Indicators
- **VS Code-style scope lines** — 4px colored left borders on all messages:
  - 🔵 **Blue (accent)** — standard user prompts
  - 🟣 **Purple** — AI assistant responses
  - 🔴 **Red** — voice-transcribed messages (🎙️ badge) + recording-active responses
  - 🟢 **Green** — SOAP note generations
  - 🟦 **Teal** — system/info messages

---

## [0.8.1] — 2026-04-13

### 🔐 Gemini OAuth — Zero-Config Google Sign-In (Extension v0.8.1)

#### Added
- **Google OAuth sign-in** — users click "Sign In to Gemini" and choose their Google account
  - PKCE (S256) flow with localhost callback server
  - CSRF `state` parameter validation
  - Tokens stored encrypted via VS Code `SecretStorage`
  - Auto-refresh with 5-minute buffer before expiry
- **Quota status bar** — real-time 🟢/🟡/🔴 per-model RPM tracking
  - Enterprise users show `∞` unlimited
  - Refreshes every 10 seconds + on each request
- **Commands**: `Synalux: Sign In to Gemini`, `Sign Out from Gemini`, `Gemini Status & Quota`
- **Backend router** — prefers OAuth Bearer token over API key for Gemini requests

#### Security Hardening (14 findings fixed)
- **Concurrent sign-in mutex** — prevents double HTTP server allocation
- **refreshToken Promise mutex** — prevents Google Token Theft Protection revocation
- **`await secrets.store()`** in refresh path — prevents token loss on shutdown
- **401 handler** — explicit "session expired" message for expired OAuth
- **Quota recorded after response only** — no phantom rate limit warnings
- **CSRF state parameter** — 16-byte random hex, validated in callback
- **Callback server isolation** — 404 for non-`/callback` paths
- **Bounded requestLog** — only tracks known model IDs
- **`try/catch` on all `server.close()`** — prevents `ERR_SERVER_NOT_RUNNING` crash
- **Single timeout source** — `clearTimeout` on early settle prevents event loop leak
- **Dynamic plan check** — `auth.getPlan()` per render, not stale capture

#### Verified Safe (External Adversarial Review)
- Token theft (PKCE + 127.0.0.1 binding)
- Embedded client secret (Desktop App pattern, per Google docs)
- XSS (error param not interpolated into HTML)
- CSRF (state + PKCE double protection)
- PII leak (no tokens in logs/errors)
- Denial of service (bounded quota tracking)

---

## [0.8.0] — 2026-04-13

### 🔐 Security — JWKS + EdDSA Authentication

#### Portal
- **JWT-first auth architecture** — `synalux_sk_` API tokens demoted to refresh-only role
  - API tokens accepted ONLY on `/api/v1/auth/jwt`, `/api/v1/tokens`, `/api/v1/auth/*`
  - All other endpoints (`/chat`, `/soap`, `/roles`, etc.) require a JWT
  - Migration header: `X-Synalux-Auth-Upgrade: required` on 401 responses
- **NEW** `jwt-auth.ts` — EdDSA (Ed25519) JWKS library ported from Prism's `authUtils.ts`
  - Signs 15-minute JWTs with EdDSA via `jose ^6.2.2` (zero dependencies)
  - Verifies JWTs from external JWKS endpoints (vendor-neutral IdP support)
  - `kid` (Key ID) in JWT header for key rotation support
  - Timing-safe comparison via native `crypto.timingSafeEqual`
- **NEW** `GET /.well-known/jwks.json` — public JWKS endpoint
  - External agents (Prism, AgentLair) can verify Synalux-issued JWTs
  - Returns Ed25519 public key with 1-hour cache
- **NEW** `POST /api/v1/auth/jwt` — token → JWT exchange endpoint
  - Rate limited: 1 exchange per 30 seconds per user
  - Returns 15-minute EdDSA JWT
- **UPDATED** Centralized auth middleware — all 6 API routes migrated:
  - `chat`, `soap`, `roles`, `esign`, `integrations`, `workspaces`
  - Removed inline `validateApiToken()` calls in favor of `authenticateRequest()`
- **NEW** `jwt_auth_log` audit table — HIPAA-safe (logs `jti`, never raw token)

#### Extension (v0.7.0)
- **JWT session management** — hybrid refresh strategy (lazy + 401 fallback)
  - Lazy: refresh if JWT expires within 2 minutes before next API call
  - On-demand: auto-retry once on 401 with fresh JWT
  - JWT stored in OS keychain (`synalux.jwt` secret)
- **Cloud streaming** updated to use `getAuthHeader()` (JWT-first)
- **Post-sign-in** immediately exchanges API token for JWT

---

## [0.7.3] — 2026-04-13

### Added (Extension v0.6.2)
- **TTS Read Aloud** — 🔊 button on every AI response; speaks via MCP `tts` tool or macOS `say` fallback
  - Language auto-selected from `synalux.language` setting
  - Stop button (⏹) to cancel mid-speech
  - Animated pulse while speaking
- **Jira/Confluence integration** — new `jira` tool (10 actions)
  - Jira: `list_issues`, `get_issue`, `create_issue`, `update_issue`, `add_comment`, `search`
  - Confluence: `get_page`, `create_page`, `update_page`, `search_pages`
  - Auth via `synalux.atlassianUrl`, `synalux.atlassianEmail`, `synalux.atlassianToken` settings
- **Vitest test runner** — new `vitest` tool (6 actions)
  - `run`, `run_file`, `watch`, `list`, `coverage`, `related`
  - Parsed output: pass/fail counts, failed test names, duration, coverage %
- Tool count: **15 → 17**

### Fixed
- **Voice recording (macOS)** — removed `sox` dependency; AVFoundation Swift recorder compiled once, cached at `~/.cache/synalux/avrecorder`
  - Fallback chain: `sox` → AVFoundation → error with clear permission hint
  - Windows/Linux paths unchanged (already use native APIs)
- **Data graph output path** — `/tmp` now allowed in `security.py` safe dirs (macOS `/tmp` → `/private/tmp` differs from `tempfile.gettempdir()`)

---

## [0.7.2] — 2026-04-13

### Infrastructure
- **Azure AD** — registered `Synalux Workspace Integration` app (OAuth2 for Microsoft 365)
- **Stripe CLI** — archived 7 legacy products, added `metadata.tier` to active plans
- **Stripe webhook** — new endpoint for integrations billing events
- **VSIX** — built extension v0.6.0 (427 KB)

### Pricing & i18n (12 languages)
- Advanced tier: +4 features (BoldSign e-signature, Zoom telehealth, Google/MS Workspace, Stripe Connect)
- Enterprise tier: +3 features (DocuSign, Slack, BAA, non-repudiation audit trail)
- Updated all 12 language translations for pricing features (f1–f11)
- API calls aligned with Stripe: Standard 2K, Advanced 5K, Enterprise unlimited

### Extension Docs
- README.md updated to v0.6.0 — 9 RBAC roles, e-sign, integrations, new commands
- CHANGELOG.md — v0.6.0 entry

### Skills
- `synalux-i18n-update` — persistent skill for updating multi-language docs when features ship

---

## [0.7.1] — 2026-04-13

### Security Fixes (Adversarial Code Review)
- **🚨 CRITICAL** Tool ACL bypass — `allowedTools` now HMAC-signed in `X-Synalux-Allowed-Tools` header
- **🚨 CRITICAL** IDOR on workspace roles — membership check before returning role configs
- **🚨 CRITICAL** Webhook HMAC DoS — buffer length check before `timingSafeEqual`
- **⚠️ HIGH** Missing audit logs on role mutations — `logRbacAction()` on create/update/delete
- **⚠️ HIGH** RLS INSERT policies tightened — workspace membership required for audit + esign
- **🟡 MEDIUM** XSS via i18n — HTML tags stripped from `display_name` / `description`
- **🟡 MEDIUM** System prompt injection — immutable Core Safety Prompt prepended before admin customization

### Added (Extension v0.6.0)
- `synalux.showRole` command — shows role, tools, admin status from portal
- `synalux.requestSign` command — e-sign template picker, signer input, provider selection
- Role badge in chat panel header — color-coded per role, 👑 for admin, XSS-safe (textContent)
- Role fetched on panel load via `/api/v1/roles?me=true` (best-effort, 5s timeout)

---

## [0.7.0] — 2026-04-13

### Added
- **RBAC System (HIPAA-Compliant)**
  - Multi-tenant workspace architecture (`workspaces` table)
  - 9 default roles with i18n display names (12 languages): restricted, clinician, coder, reviewer, tester, documenter, planner, security, office_manager
  - OAuth-identity-bound admin rights — no shared passwords (HIPAA 164.312(a)(2)(i))
  - Server-side role enforcement — client never asserts its own role (confused deputy prevention)
  - Fail-closed offline behavior — sensitive tools rejected when portal unreachable
  - Role change request/approval flow via authenticated dashboard (not email links)
  - RBAC audit log (HIPAA non-repudiation) for every role mutation
  - HMAC-signed local role cache with 5-min TTL
  - New API endpoints: `/api/v1/workspaces`, `/api/v1/roles`
- **E-Signature Integration (Pro/Enterprise)**
  - BoldSign integration (Pro), DocuSign integration (Enterprise)
  - 7 clinical document templates: intake consent, HIPAA auth, BIP signing, parent consent, insurance auth, employee BAA, discharge summary
  - HMAC-verified webhooks for real-time status updates
  - Plan tier gating enforced server-side
  - New API endpoint: `/api/v1/esign`
- **Workspace Integrations (Pro/Enterprise)**
  - Zoom telehealth: create/cancel meetings, encrypted join URLs, session tracking
  - Slack alerts (Enterprise only): notification-only, zero PHI in messages
  - Google Workspace / Microsoft 365: calendar, storage (API scaffolding)
  - Stripe Connect: client billing, invoice generation (API scaffolding)
  - BAA confirmation requirement for each provider
  - New API endpoint: `/api/v1/integrations`
- **Database Migration** (`20260414_rbac.sql`)
  - 9 new tables with Row Level Security policies
  - Seed function for default workspace roles
  - Integration and telehealth session tracking

### Security
- Chat API now enforces RBAC server-side (system_prompt + tool ACL from DB)
- New users default to `restricted` role with zero tool access
- Patient-scoped PHI memory isolation: `(user_id, workspace_id, encounter_id)`
- All integration credentials encrypted at rest (AES-256)
- Zoom join URLs encrypted at rest
- E-sign API keys encrypted at rest

---

## [0.6.4] — 2026-04-12

### Added
- **26 integration tests** covering 8 categories (page rendering, API auth, Supabase data, token CRUD, plan limits, security, Stripe, response format)
- Supabase migration for `users_plan_check` constraint via CLI

### Fixed
- Portal CHECK constraint on `plan` column now enforced at database level

---

## [0.6.3] — 2026-04-12

### Added
- **Live infrastructure deployment:**
  - Supabase project linked (3 tables: `users`, `api_tokens`, `usage_logs`)
  - Stripe products/prices (Standard $19, Advanced $49, Enterprise $99) via Stripe CLI
  - Google OAuth client (GCP project `synalux-ai-portal`, ports 3000-3005)
  - Stripe webhook listener (`stripe listen → localhost:3000/api/webhooks/stripe`)
- Seeded user (`dcostenco@gmail.com`, free tier) with 3 API tokens (VSCode, CLI, CI-CD)
- Portal `.env.local` with all credentials
- CLI-First Policy rule added to `bcba-private`

---

## [0.6.2] — 2026-04-12

### Added
- **Portal polish:**
  - Root layout (`layout.tsx`) with glassmorphism navbar, Inter font, SEO metadata
  - Dashboard rebuilt: 4-tier subscription display, API token management (generate/copy/revoke), usage stats with bar charts
  - Token CRUD API (`/api/v1/tokens` — POST/GET)
  - Stripe webhook handler (`/api/webhooks/stripe`)
  - `next.config.ts` + `tsconfig.json`
- README overhaul with full platform overview

---

## [0.6.1] — 2026-04-12

### Added
- **4-tier subscription model** (Free $0, Standard $19, Advanced $49, Enterprise $99/seat)
- Updated `stripe.ts` with 4 plan configs + checkout types
- Updated `db.ts` with SQL schema, User type, and rate limits for 4 tiers
- Redesigned pricing page with 4-tier cards + FAQ section
- DOCX export script (`scripts/export_docx.py`)
- `Synalux_Business_Model.docx` (58KB, 275 paragraphs, 51 tables)

---

## [0.6.0] — 2026-04-11

### Added
- **VS Code Extension** (`synalux-vscode/`)
  - `@synalux` chat participant with slash commands for 15 tools
  - Google OAuth 2.1 via `vscode.authentication`
  - Voice input (transcribe-to-cursor)
  - Multi-agent pipeline UI
- **Client Portal** (`portal/`)
  - Next.js 15 app with Google OAuth, Supabase, Stripe
  - Landing page, pricing page, dashboard
  - API token management (SHA-256 hashed)
  - Rate limiting per plan tier
- **Multi-Agent Orchestration** (`tools/orchestrator.py`)
  - 7 roles: coder, reviewer, tester, documenter, planner, security, clinician
  - Auto-role classification from task analysis
  - Sequential/parallel/interactive pipelines
- **Voice Recognition** (`tools/voice.py`)
  - macOS (SFSpeechRecognizer), Windows (SAPI), Linux (Whisper.cpp)
  - Clinical dictation mode for SOAP notes
- Business plan sections §9.8–9.11

---

## [0.5.0] — 2026-04-11

### Added
- Cross-platform support (macOS, Windows, Linux)
- Multi-language support (10 languages, 51 TTS locales)
- 15 multimodal tools

---

## [0.1.0] — 2026-04-10

### Added
- Phase 0 data infrastructure
- Export pipeline, synthetic data generator
- SFT/GRPO/model configs
- 4 evaluation benchmarks
