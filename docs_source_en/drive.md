# 📁 Drive

**Practice file storage with HIPAA-grade isolation.** Documents, spreadsheets, presentations, and patient-linked attachments — searchable, share-controlled, audit-logged. Lives at [synalux.ai/drive](https://synalux.ai/drive).

---

## 📄 Three Native File Types
*   **Doc** — rich-text document (collaborative editing via the [Collaborative Editors module](collaborative_editors_module.md)).
*   **Sheet** — spreadsheet with formula support.
*   **Presentation** — slide deck.

Each file is RLS-scoped to its workspace and (optionally) to a patient. A new file is created with one click and opens in the in-app editor — no external app, no provider OAuth.

---

## 📤 Upload, Share, Delete (In-Place)
*   **Upload** — drag-drop or browse; 50MB per-file boundary (hardened against partial-upload state).
*   **Share** — link or per-user invite. Emails sent via the [Mail module](mail.md); recipient name HTML-escaped in the invite body (closed stored XSS).
*   **Permission tiers** — viewer / editor / owner; revocable.
*   **Delete** — soft-delete by default with 30-day recovery window; hard-delete on admin override.

---

## 🩺 Patient-Linked Files
Attach a file to a patient record so it appears under their chart automatically.
*   **Browse from patient view** — Documents tab shows everything filed for that patient.
*   **Filter** — by file type, date, uploader, tag.
*   **HIPAA**: patient_id is part of the RLS predicate, so a clinician can never see another workspace's patient files.

---

## 🔒 Security & HIPAA
*   **RLS-scoped client** — every list/read uses `createRlsClient(session)`; the database denies cross-workspace queries even if the API code has a bug.
*   **`storage_path` validation** — uploads are written to a controlled prefix; path-traversal attempts (`../`, absolute paths) rejected.
*   **`withAudit({ module: 'drive' })`** — every list / upload / share / delete writes an audit row with operation type, user_id, file_id, IP.
*   **Workspace isolation guard** — double-locks at API layer in case RLS is misconfigured.
*   **50MB boundary** — hardened with a storage rollback transaction so a partial upload never leaves orphan bytes in object storage.

---

## 🏗️ Architecture

```
GET    /api/v1/drive               List files (RLS-scoped, filter by type/patient/search)
POST   /api/v1/drive               Create new doc/sheet/presentation
GET    /api/v1/drive/:id           Read file metadata + content
PATCH  /api/v1/drive/:id           Update content / rename / move
DELETE /api/v1/drive/:id           Soft-delete (or hard-delete with admin override)
POST   /api/v1/drive/upload        Direct file upload (50MB cap, storage_path validated)
```

| Layer | Tech |
|---|---|
| Frontend | Next.js 15 App Router, in-app editors |
| Storage | Supabase Storage (object) + Postgres metadata table `drive_files` |
| Auth | NextAuth + RLS per-workspace |
| Encryption | At-rest via Supabase Storage; TLS 1.3 in transit |
| Audit | `withAudit({ module: 'drive' })` |
| Sync conflict resolution | CRDT-based (collaborative editors) |

---

## 💳 Plans

| | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| 1 GB storage | ✅ | ✅ 10 GB | ✅ 100 GB | ✅ 1 TB |
| Doc / Sheet / Presentation | ✅ | ✅ | ✅ | ✅ |
| Patient-linked files | — | ✅ | ✅ | ✅ |
| Share by link | — | ✅ | ✅ | ✅ |
| Per-user share permissions | — | ✅ | ✅ | ✅ |
| Real-time collaborative editing | — | — | ✅ | ✅ |
| Bulk export | — | — | ✅ | ✅ |
| Custom retention policies | — | — | — | ✅ |
| BAA-grade encryption keys (BYOK) | — | — | — | ✅ |

[See full pricing →](https://synalux.ai/pricing)

---

## 🔄 Inter-Module Integration
*   **Mail** — attachments uploaded via Drive; storage_path validated.
*   **Patients** — Documents tab on every patient record reads filtered Drive list.
*   **Telehealth** — meeting recordings stored in Drive when consented.
*   **SOAP / Clinical Notes** — exported as Doc files when finalized.
*   **No-Code Dashboard Builder** — Drive widgets surface recent / patient-filtered files.
