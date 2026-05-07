# 💬 Direct Messages

Internal staff-to-staff direct messaging within the workspace. Slack-like 1:1 + group threads with HIPAA-grade audit logging.

---

## 💬 What It Does
*   **1:1 DMs** between staff members in the same workspace.
*   **Group threads** for ad-hoc conversations.
*   **PHI-aware** — messages can reference patients via `@patient` mentions, automatically writing audit rows for cross-staff PHI access.
*   **Searchable** — full-text search across the workspace's DM history (admin-permission required for cross-user search).

---

## 🏗️ Architecture

```
GET  /api/v1/direct-messages                         List threads visible to user
POST /api/v1/direct-messages                         Send a new message (creates or appends to thread)
GET  /api/v1/direct-messages/:thread/messages        Read thread history
PATCH /api/v1/direct-messages/:thread/read           Mark read (write receipt)
```

| Layer | Tech |
|---|---|
| Storage | Postgres `direct_messages` + `dm_threads` with RLS (workspace + participant predicates) |
| Realtime | Supabase Realtime channels per thread |
| Audit | `withAudit({ module: 'direct-messages' })` on every send |
| PHI mentions | Trigger function writes `phi_access_log` row when `@patient:<id>` syntax detected |

---

## 💳 Plans
Available on **Standard+** as part of the unified chat experience. Free tier: receive only.
