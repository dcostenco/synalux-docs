# 💬 Viber Bot

Connect a Viber Bot to send + receive Viber messages from the unified Synalux chat surface.

---

## 📨 Viber Bot API
*   **Webhook ingress** — `/api/v1/webhooks/viber` receives incoming user messages + delivery / seen events.
*   **Outbound** — `/api/v1/viber/send` posts via Viber's `send_message` endpoint with rich keyboards + carousel cards supported.
*   **Bot setup** — register a public account at [partners.viber.com](https://partners.viber.com), copy the auth token into Synalux workspace settings; webhook URL auto-set via `set_webhook`.

---

## 🏗️ Architecture

```
POST /api/v1/webhooks/viber    Viber events (validated against bot auth token)
POST /api/v1/viber/send        Outbound (text / picture / file / rich media)
```

Provider abstraction: `lib/message-providers/viber.ts`.

---

## 🌍 Why Viber?
Significant install base in Eastern Europe (Romania, Ukraine, Russia, Belarus, Bulgaria) — countries where Synalux serves practices that need a non-WhatsApp messenger for patient communication.

---

## 💳 Plans
Available on **Standard+**.
