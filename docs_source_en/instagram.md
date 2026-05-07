# 💬 Instagram Direct

Connect an Instagram Business / Creator account to receive + reply to Instagram DMs from inside Synalux.

---

## 📨 Instagram Direct Messaging
*   **Built on the Messenger Platform** — Instagram DMs use Meta's Messenger infrastructure under the hood; Synalux uses the same provider abstraction.
*   **Webhook ingress** — `/api/v1/webhooks/instagram` receives DMs from connected Instagram Business accounts.
*   **Send** — `/api/v1/instagram/send` posts via Meta's `/me/messages` endpoint with `appsecret_proof` on every call.
*   **Story mentions, comment replies** — receive notifications when your account is mentioned or commented on; reply inline.

---

## 🔐 Setup
1. Connect a Facebook Page to your Instagram Business account.
2. Authorize Synalux for `instagram_basic` + `instagram_manage_messages` + `pages_messaging` scopes.
3. Subscribe the Facebook Page to messaging webhooks (auto-handled by Synalux on connect).

---

## 🏗️ Architecture

```
POST /api/v1/webhooks/instagram        DMs / story mentions / comment replies
POST /api/v1/instagram/send            Outbound DM (appsecret_proof protected)
```

---

## 💳 Plans
Available on **Standard+**. Free tier: receive only via the contact form.
