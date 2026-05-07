# 🛒 Skills Marketplace

Workspace-installable AI skills + automations. Add a skill once, available across the workspace's chat surface, calendar, mail, drive, and clinical workflows.

---

## 🧩 What's a Skill?
A scoped, declared capability the chat assistant can invoke when context warrants. Examples:
*   **Insurance Eligibility** — verify a patient's benefits against the payer in real time.
*   **CPT Suggester** — given a SOAP note, propose the right billing codes.
*   **Spam Blocker** — auto-classify incoming mail per the workspace's policy.
*   **Telehealth Pre-Call Prep** — pull patient summary + last 3 sessions into a brief before the call.

Each skill declares its OAuth scopes, tool surface (functions exposed to the AI), and tier gating.

---

## 🏗️ Architecture
*   **Per-workspace install** — admins enable skills in the Marketplace UI; install writes a `workspace_skills` row that gates `/api/v1/chat`'s tool exposure.
*   **Permission scopes** — each skill declares the data it touches (mail, drive, patients, billing) — opt-in per scope.
*   **Audit-tagged** — every skill invocation writes an audit row with skill_id + tool_name + caller.
*   **Sandboxed execution** — skills can't reach beyond their declared scopes; enforced at the dispatcher layer.

```
GET  /api/v1/marketplace                List available skills
POST /api/v1/marketplace/install        Install a skill into the current workspace
DELETE /api/v1/marketplace/install/:id  Uninstall (revokes scopes + tool exposure)
GET  /api/v1/skills                     List installed skills for the user's workspace
```

---

## 💳 Plans

| | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| Browse marketplace | ✅ | ✅ | ✅ | ✅ |
| Install skills | — | ✅ 5 active | ✅ 20 active | ✅ unlimited |
| Custom workspace-private skill | — | — | — | ✅ |
| Skill SDK (build your own) | — | — | — | ✅ |

[See full pricing →](https://synalux.ai/pricing)
