# 📄 PDF Generation

Server-side PDF rendering for SOAP notes, progress reports, superbills, claims, intake forms, and patient-facing documents.

---

## 📑 Use Cases
*   **SOAP notes** — finalized clinical notes exported as PDFs filed to the patient chart and the [Drive module](drive.md).
*   **Progress reports** — auto-aggregated session data + graphs + mastery trends (used for ABA authorization renewals).
*   **Superbills** — patient-side billing summary for self-pay or out-of-network reimbursement.
*   **Intake packets** — multi-form bundles delivered to new patients via the [Patient Portal](patient_portal.md).
*   **Receipts / invoices** — Stripe-payment confirmations.
*   **Recall letters** — bulk-send via [Mail](mail.md).

---

## 🏗️ Architecture
*   Server-rendered via headless Chromium (per-call worker; no shared state).
*   Templates live as React components — same design system as the rest of the app, rendered to PDF via Puppeteer.
*   Optional digital signature via the e-Signature module (BoldSign integration) for docs that need execution.
*   PDF bytes uploaded to Supabase Storage with the same RLS scoping as other Drive files.

```
POST /api/v1/pdf            { template, payload, sign?: bool } → returns signed download URL
GET  /api/v1/pdf/:id        Read PDF metadata + signed URL
```

---

## ⚖️ HIPAA + Audit
*   PDFs scoped to workspace + (optional) patient — same RLS as Drive.
*   Generation logged in audit chain.
*   Download links are short-TTL (5 minutes) signed URLs.
