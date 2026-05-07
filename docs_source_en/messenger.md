# 💬 Facebook Messenger

Connect a Facebook Page Messenger account to send + receive messages from inside Synalux.

---

## 📨 Messenger Send / Receive
*   **Webhook** — `/api/v1/webhooks/messenger` receives Page-bound messages; Meta signature validated.
*   **Send** — `/api/v1/messenger/send` posts to Meta's `/me/messages` endpoint with `appsecret_proof` HMAC-SHA256 protection on every call (defense against access-token leak).
*   **Page-scoped** — one Facebook Page connection per workspace.
*   **24-hour window + tags** — outbound after 24h must use `MESSAGE_TAG` per Meta policy.

---

## 🔐 App Review
For Meta App Review, Synalux exposes admin endpoints to fire test calls per requested permission so the App Review counter increments:
```
POST /api/v1/messenger/admin/test-send                 Fire a test message (CRON_SECRET-gated)
POST /api/v1/messenger/admin/test-all-permissions      One Graph API call per requested permission
```
This is what gets you through Meta App Review's "exercise the API" requirement without scripting it manually.

---

## 🏗️ Architecture

```
POST /api/v1/webhooks/messenger        Meta webhook (signature-validated)
POST /api/v1/messenger/send            Outbound message (appsecret_proof on every call)
POST /api/v1/messenger/admin/test-*    App Review counter exercises
```

---

## 💳 Plans
Available on **Standard+**.
