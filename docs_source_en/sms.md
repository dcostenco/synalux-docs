# 📱 SMS (Twilio)

Two-way SMS via Twilio for appointment reminders, intake links, and patient communication. Falls back gracefully when not configured.

---

## 📨 Twilio SMS — Send + Receive
*   **Outbound** — `/api/v1/sms/send` posts to Twilio's Messages API with workspace-scoped account SID + auth token.
*   **Inbound webhook** — `/api/v1/webhooks/twilio` receives replies and surfaces them in the chat thread (workspace's Twilio number → workspace inbox).
*   **Delivery tracking** — Twilio status callbacks update message rows (queued / sent / delivered / failed).
*   **Number rental** — instructions to provision a Twilio number with messaging A2P 10DLC compliance.

---

## 🏗️ Architecture

```
POST /api/v1/sms/send                Outbound SMS (workspace-scoped Twilio creds)
POST /api/v1/webhooks/twilio         Inbound + delivery status webhook
GET  /api/v1/sms/numbers             List rented Twilio numbers per workspace
```

---

## ⚖️ Compliance
*   **Consent capture** — `/sms-consent` page collects opt-in per HIPAA + TCPA. Required before first send to a patient.
*   **STOP / HELP keyword handling** — Twilio's compliance layer + Synalux's per-recipient blocklist.
*   **A2P 10DLC** — guidance for US phone-number registration in the setup modal.

---

## 💳 Plans
Available on **Standard+**. Twilio usage is billed by the workspace directly — Synalux passes through Twilio's per-message pricing (roughly $0.0079 per US SMS at 2026 rates).
