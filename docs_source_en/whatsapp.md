# 💬 WhatsApp Business

Connect a WhatsApp Business account to send + receive messages from inside the unified Synalux chat surface.

---

## 📨 WhatsApp Business Cloud API
*   **Webhook ingress** — `/api/v1/webhooks/whatsapp` receives incoming messages, validates Meta's signature, and surfaces them in the chat thread.
*   **Outbound** — `/api/v1/whatsapp/send` posts to Meta's Cloud API. Workspace-scoped credentials (Phone Number ID + access token).
*   **Templates** — pre-approved message templates for transactional sends (appointment reminders, intake confirmations).
*   **Media** — text, images, documents, audio, location pins. Audio runs through Transcription on receipt.

---

## 🔐 Setup
1. Create a Meta Business + WhatsApp Business app at [business.facebook.com](https://business.facebook.com).
2. Generate a permanent System User access token; paste into Synalux workspace settings.
3. Configure webhook URL `https://synalux.ai/api/v1/webhooks/whatsapp` with your verify token.
4. Subscribe to `messages` + `message_status` events.

The in-app setup guide modal (`/chat`) walks you through every step with the exact field names from the Meta dashboard.

---

## 🏗️ Architecture

```
POST /api/v1/webhooks/whatsapp     Meta webhook ingress (signature-validated)
POST /api/v1/whatsapp/send         Outbound (template or freeform within 24h window)
GET  /api/v1/whatsapp/templates    List approved templates for the workspace
```

Provider abstraction: `lib/message-providers/whatsapp.ts` matches the generic shape (Gmail / Telegram / SMS / etc.).

---

## ⚖️ HIPAA + Compliance
WhatsApp's terms restrict PHI for non-Meta-BAA accounts. Synalux flags any message that looks PHI-bearing and requires explicit workspace-admin opt-in to send via WhatsApp. Signed BAA with Meta is on the customer's roadmap.

---

## 💳 Plans
Available on **Standard+**. Free tier: receive only via the contact form.

[See full pricing →](https://synalux.ai/pricing)
