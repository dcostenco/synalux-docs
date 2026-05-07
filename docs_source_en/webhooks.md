# 🪝 Webhooks

Outbound webhooks for workspace events. Receive HTTP POSTs at your endpoint when a patient is created, an appointment is scheduled, a SOAP note is signed, etc.

---

## 📡 Event Catalog
*   `patient.created` / `patient.updated`
*   `appointment.created` / `appointment.cancelled` / `appointment.completed`
*   `soap_note.signed`
*   `claim.submitted` / `claim.paid` / `claim.denied`
*   `mail.received`
*   `meeting.started` / `meeting.ended`
*   `auth.signed_in` (admin-only)
*   `break_glass.invoked` (always sent + admin-emailed)

---

## 🔐 Signing
*   Every payload signed with HMAC-SHA256 over the body using the workspace's webhook secret.
*   Signature delivered in `X-Synalux-Signature` header — verify in your endpoint to reject spoofs.
*   Timestamp in `X-Synalux-Timestamp` header — reject if older than 5 minutes (replay protection).

---

## 🔁 Delivery
*   **Retry policy**: exponential backoff (1m, 5m, 30m, 2h, 12h) for non-2xx responses.
*   **Dead-letter queue** after 5 failures — admin gets an email + the failed event surfaces in the workspace inbox.
*   **Idempotency** — every event has a stable `event_id` you can use as a deduplication key.
*   **Inbound webhooks** for messaging providers (Telegram / WhatsApp / Viber / SMS / Messenger / Instagram) live at `/api/v1/webhooks/<provider>` — see each provider page.

---

## 🏗️ Architecture

```
POST /api/v1/webhooks                       Configure outbound endpoints (admin)
GET  /api/v1/webhooks                       List configured endpoints
DELETE /api/v1/webhooks/:id                 Remove
GET  /api/v1/webhooks/:id/deliveries        Recent delivery attempts (success / fail / status)
POST /api/v1/webhooks/:id/replay/:event_id  Manual replay of a failed delivery
```

---

## 💳 Plans
Available on **Advanced+** for outbound; inbound webhooks for messaging providers ship on **Standard+**.
