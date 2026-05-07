# 📠 Fax

Send + receive fax for healthcare workflows where it's still required (referrals, prior auth, records requests with non-digital practices).

---

## 📤 Send + Receive
*   **Send** — `POST /api/v1/fax/send` with PDF attachment + recipient fax number; Synalux delivers via the configured fax provider.
*   **Receive** — inbound faxes arrive in the workspace inbox with OCR'd text + PDF attached; auto-routed to the patient if the cover sheet matches.
*   **Delivery tracking** — sent / queued / delivered / failed status updates with retry on transient failures.
*   **Honest mock-mode** — when no real fax provider is configured, the API returns a clear "mock-mode" response so test environments don't silently no-op.

---

## ⚖️ Validation
*   E.164 fax-number normalization — rejects malformed inputs at the API boundary.
*   PDF attachment validation — file size, MIME type, page count limits.
*   Per-workspace recipient allowlist option for high-security environments.

---

## 🏗️ Architecture

```
POST /api/v1/fax/send         Outbound (PDF + recipient + cover sheet)
GET  /api/v1/fax/inbox        Inbound queue (workspace-scoped)
GET  /api/v1/fax/:id/status   Delivery status
GET  /api/v1/fax/:id/pdf      Signed download URL for received PDF
```

---

## 💳 Plans
Available on **Advanced+** as part of the practice-administration tier.

Provider integration: Phaxio / Documo / SRFax (configurable per workspace).
