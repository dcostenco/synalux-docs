# 💬 Telegram Bot

**Two ways to use Telegram in Synalux:** as a chat provider for your team and patients, or as a sign-in method via Telegram Login Widget.

---

## 📨 Telegram Bot API Integration
Send and receive Telegram messages from inside Synalux's unified chat surface. No separate Telegram app for staff to monitor.
*   **Webhook-driven** — incoming messages POST to `/api/v1/webhooks/telegram` and surface in the Synalux chat surface in real time.
*   **Send** — outbound replies via `/api/v1/telegram/send`. Workspace-scoped bot token; one bot per workspace.
*   **Bot setup** — provide your bot token from `@BotFather` in the workspace settings; webhook URL auto-registers via `setWebhook`.
*   **Media support** — text, images, documents, voice notes (transcribed via the Transcription module on receipt).

---

## 🔐 Telegram Login Widget
End-to-end implementation of the Telegram Login Widget for sign-in.
*   Users click a Telegram-blue button on `/auth`; Telegram OAuth flow returns user identity (telegram_id, name, photo).
*   Identity is bound to a Synalux user record; subsequent sign-ins are one-tap.
*   `bot_token` HMAC validation per the [Telegram Login Widget spec](https://core.telegram.org/widgets/login) — replay-attack proof.

---

## 🏗️ Architecture

```
POST /api/v1/webhooks/telegram      Webhook ingress (validated against bot token + IP allowlist)
POST /api/v1/telegram/send          Outbound message (workspace-scoped)
GET  /api/v1/telegram/auth/callback Login Widget callback (HMAC-validated)
```

Provider abstraction: `lib/message-providers/telegram.ts` — same shape as Gmail / Outlook / Slack so the unified chat surface lights up automatically.

---

## 🧪 Tests
24+ tests cover bot routes + lib (auth callback HMAC validation, webhook ingestion, send queue, error paths, retry logic). See `portal/src/app/api/v1/telegram/__tests__/`.

---

## 💳 Plans
Available on **Standard+** as part of the unified chat experience. Free tier: receive only via the public landing page contact form.

[See full pricing →](https://synalux.ai/pricing)
