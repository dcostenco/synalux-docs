# 🔐 Authentication, MFA & Break-Glass

NextAuth-backed OAuth (Google, Microsoft) with multi-factor enrollment, session heartbeat, and break-glass admin override for emergency clinical access.

---

## 🔑 Sign-in Methods
*   **Google OAuth** — primary; enforced for new workspaces.
*   **Microsoft OAuth** — for organizations on Microsoft 365.
*   **Telegram Login Widget** — see [Telegram](telegram.md).
*   **Magic-link email** — fallback for users without Google/Microsoft.

---

## 🛡️ Multi-Factor Authentication
*   **TOTP** (authenticator app) — RFC 6238; 30-second window.
*   **WebAuthn / Passkey** — preferred; platform authenticator (Touch ID / Windows Hello / Android biometrics).
*   **Per-workspace policy** — admins can require MFA for any role; clinical roles enforced by default.
*   **Recovery codes** — 10 single-use codes generated at enrollment.

---

## 🚨 Break-Glass Override
For HIPAA-compliant emergency access when primary access path is unavailable.
*   **Audit-logged on use** — every break-glass invocation writes a row that can NEVER be deleted (append-only audit table).
*   **Notifies workspace admins immediately** via [Mail](mail.md) + [SMS](sms.md).
*   **Time-bounded** — 60-minute access window; automatic re-lockout after.
*   **Justification required** — admin must enter a reason at break-glass invocation; reason becomes part of the audit record.

---

## 💗 Session Heartbeat
*   Client pings `/api/v1/session/heartbeat` every 60s while active.
*   Idle timeout (configurable per workspace; default 15min for clinical roles, 60min for admin).
*   Force re-auth on sensitive actions (export, delete, payment) regardless of heartbeat state.

---

## 🏗️ Architecture

```
GET  /api/v1/auth/session         NextAuth session (cookie-backed, JWT)
POST /api/v1/auth/mfa/enroll      Begin TOTP / WebAuthn enrollment
POST /api/v1/auth/mfa/verify      Verify code at sign-in
POST /api/v1/break-glass          Initiate break-glass override (admin-gated)
POST /api/v1/session/heartbeat    Idle-keepalive ping
```

| Layer | Tech |
|---|---|
| Session | NextAuth + Postgres adapter; JWT cookies, HttpOnly + Secure + SameSite=Lax |
| MFA storage | Encrypted at rest (AES-256-GCM via `lib/credential-vault.ts`) |
| Audit | `withAudit({ module: 'auth' })` on every endpoint; break-glass rows pinned to immutable table |

---

## 💳 Plans

| | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| OAuth sign-in | ✅ | ✅ | ✅ | ✅ |
| TOTP MFA | ✅ | ✅ | ✅ | ✅ |
| WebAuthn / Passkey | — | ✅ | ✅ | ✅ |
| Workspace-enforced MFA policy | — | — | ✅ | ✅ |
| Break-glass override | — | — | ✅ | ✅ |
| SAML / SSO | — | — | — | ✅ |
| Custom session policy | — | — | — | ✅ |

[See full pricing →](https://synalux.ai/pricing)

See also: [`portal/docs/security/oauth-token-isolation.md`](https://github.com/dcostenco/synalux-private/blob/main/portal/docs/security/oauth-token-isolation.md) (private) for the full Pattern C OAuth token isolation spec.
