# 📨 Mail

**Read and reply to your work email without switching tabs.** Gmail today; Outlook + Yahoo + custom IMAP next. Connect once via OAuth, get a unified inbox with full folder support, spam filtering, and HIPAA-grade audit on every read.

Live at [synalux.ai/mail](https://synalux.ai/mail).

---

## ✉️ Unified Inbox Across Providers
One inbox view that combines mail from every connected provider. Click a thread to read inline; reply without leaving the page.
*   **Connect once** — OAuth handshake via the [generic Connect-Integration pattern](#-connect-integration-pattern); no per-provider page changes.
*   **Folder support** — inbox, spam, all, plus user-specific labels (Gmail) / folders (Outlook).
*   **Thread view** — full RFC 2822 threading; collapses replies; expands quoted history on demand.
*   **Search** — server-side search across subject, from, body (workspace-scoped, RLS-enforced).

---

## 📤 Send + Reply In-Place
*   **Compose** — rich-text + plain-text modes; auto-saves drafts every 3 seconds.
*   **Reply / Reply-All** — threads on the original Message-ID, preserves provider-side conversation grouping.
*   **Attachments** — uploaded via the Drive module; storage_path validated against allowlist (no path traversal).
*   **Body sanitization** — `body_html` is HTML-escaped on render to close stored XSS via crafted incoming mail.

---

## 🛡️ Spam Blocker Module
Built-in spam classification with per-workspace block lists.
*   **Per-workspace block list** — admins block sender/domain; immediate effect across the workspace.
*   **Provider-side spam folder** is still respected (Gmail's classifier wins on its own labels).
*   **Phishing heuristics** — flags links pointing to recently-registered domains, mismatched SPF/DKIM, lookalike-domain tactics.

---

## 🔌 Connect-Integration Pattern
Adding a new mail provider (e.g. Outlook) is ~30 LOC because all providers go through a generic OAuth + message-provider abstraction.
*   **Connect cards** are auto-rendered from a provider declaration — no per-provider UI page.
*   **Token storage**: OAuth tokens AES-256-GCM encrypted at rest; per-workspace isolation enforced.
*   **Token refresh** is centralized; expiry detected and rotated transparently.
*   **CLI** for ops: `portal/scripts/fetch-messages.mjs` to pull mail outside the web flow (e.g. for bulk import).

---

## 🔒 HIPAA + Audit
*   **Every read writes an `oauth_token_access_log` row** with operation type (list / read / send / delete) so an auditor can reconstruct who accessed what and when.
*   **Workspace isolation guard** — `requireWorkspaceMember` runs on every endpoint; RLS double-locks at the database layer.
*   **Credential encryption** — provider tokens never stored in plaintext.
*   **No PHI in URLs** — all sensitive identifiers in POST body / signed cookies; logs scrub query strings.

---

## 🏗️ Architecture

```
GET /api/v1/mail/inbox       List threads (folder=inbox|spam|all)
GET /api/v1/mail/thread/:id  Full thread with quoted history
POST /api/v1/mail/send       Send / reply (validates attachments)
POST /api/v1/mail/sync       Force-sync from provider (bulk pull)
```

| Layer | Tech |
|---|---|
| Frontend | Next.js 15 App Router, server components |
| OAuth | NextAuth + per-provider adapter (currently Gmail) |
| Storage | Postgres (Supabase) with RLS; `mail_threads`, `mail_messages`, `oauth_tokens`, `oauth_token_access_log` |
| Encryption | AES-256-GCM via `lib/credential-vault.ts` |
| Audit | `withAudit({ module: 'mail' })` middleware |
| Provider abstraction | `lib/message-providers/` — extend with ~30 LOC for new provider |

---

## 💳 Plans

| | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| Connect 1 mail account | ✅ | ✅ | ✅ | ✅ |
| Connect multiple accounts | — | ✅ | ✅ | ✅ |
| Spam blocker | — | ✅ | ✅ | ✅ |
| Mail-to-task automation | — | — | ✅ | ✅ |
| Per-patient mail filing | — | — | ✅ | ✅ |
| Bulk archive / move / label | — | — | ✅ | ✅ |
| Custom IMAP / SMTP | — | — | — | ✅ |

[See full pricing →](https://synalux.ai/pricing)

---

## 🧰 Setup Guide
A built-in modal walks the admin through:
1. Click **Connect Gmail** on the `/chat` or `/mail` page.
2. Approve the Google OAuth consent screen — Synalux requests `gmail.readonly`, `gmail.send`, `gmail.modify`.
3. Folder sync starts in the background (typically 30-90s for the first 1000 messages).
4. Mail appears in the unified inbox; reply directly from the thread view.

For Outlook / Yahoo / custom IMAP support, watch the [Roadmap](https://github.com/dcostenco/synalux-docs/blob/main/ROADMAP.md) or contact sales.
