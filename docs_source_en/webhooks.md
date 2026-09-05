# 🪝 Webhooks

Webhooks let another system receive an HTTP POST when something happens in Synalux. This page describes what the current customer portal provides, and what it does not, so an integration is not built against a capability that is not yet exposed.

---

## Inbound webhooks (available)

Messaging providers deliver inbound messages to Synalux through provider webhooks. Each provider page documents its connection and boundary:

*   Telegram, WhatsApp, Viber, SMS, Facebook Messenger and Instagram post to `/api/v1/<provider>/webhook`.
*   Payment providers post to their own verified endpoints; those are configured by Synalux, not by the customer.

Inbound message webhooks ship on **Standard+**. Inbox access is restricted separately from integration management; see each provider page.

---

## Outbound webhooks (current boundary)

The customer portal does **not** currently provide a self-service outbound webhook workflow. There is no screen or API for a customer to register an endpoint URL, choose events, or view deliveries for their workspace, and no workspace events are published to external endpoints today.

What exists is a platform-operated delivery layer, used by Synalux operations rather than by customers:

*   Deliveries are HTTPS-only and signed with HMAC-SHA256 over the request body. The signature is sent in the `X-Synalux-Signature` header as `sha256=<hex>`.
*   Every delivery attempt is recorded (endpoint, status, HTTP response code, last error) and can be retried manually from the Synalux platform console.
*   Endpoints that are not HTTPS, that embed credentials, or that resolve to private network addresses are refused.

Not part of the current product: an event catalog (`patient.created`, `appointment.*`, `soap_note.signed`, `claim.*`, `mail.received`, `meeting.*`, `auth.signed_in`, `break_glass.invoked`), automatic retry with backoff, a dead-letter queue with administrator email, a timestamp header for replay protection, or a stable `event_id` for deduplication. Do not build an integration that depends on them.

---

## If you need outbound events

Contact [Synalux support](https://synalux.ai/support) with the workspace, the events you need, and the receiving system. Requirements gathered this way decide the shape of the first customer-facing release of outbound webhooks.

---

## 💳 Plans
Inbound webhooks for messaging providers ship on **Standard+**. Outbound webhooks are not yet available on any plan.
