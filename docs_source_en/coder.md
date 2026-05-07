# 💻 Prism Coder IDE

**Local-first AI IDE.** Standalone macOS / Windows desktop app + browser preview at `synalux.ai/coder`. Repo: [`prism-coder`](https://github.com/dcostenco/prism-coder).

---

## 🧠 Local-First AI
*   **Bundled `prism-coder` model** runs against local Ollama; no cloud dependency for completion / chat / refactor.
*   **Cloud upgrade** to Claude Sonnet 4 / Gemini 3 Pro available for paid tiers via the Synalux portal — same routing as [AI chat](team_chat_communication.md).
*   **Air-gapped mode** — disable cloud entirely; works fully offline against the local Synalux Coder model.

---

## 🔌 Integrations
The browser preview at `synalux.ai/coder` ships Connect cards for:
*   **Mail** — inline email-to-task + send composed messages.
*   **Drive** — open / save documents to Synalux Drive.
*   **Source / GitHub** — repo browse, PR review, branch ops.

Same OAuth + audit posture as the rest of the platform — see [Mail](mail.md) / [Drive](drive.md) for the Connect-Integration pattern.

---

## 🪟 Windows Code-Signing
Production Windows binaries are signed via **Azure Trusted Signing** (Microsoft's cloud code-signing service that replaced traditional EV cert flows). Avoids the SmartScreen reputation grind of self-signed binaries.

---

## 🧪 Tests
Windows-22.x CI hookTimeout regression was fixed in 2026-Q2; the build now passes consistently across macOS-13/14, Windows-22/24, Linux-22/24.

---

## 💳 Plans

| | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| Web preview at /coder | ✅ | ✅ | ✅ | ✅ |
| Standalone macOS app | ✅ | ✅ | ✅ | ✅ |
| Standalone Windows app (signed) | ✅ | ✅ | ✅ | ✅ |
| Local prism-coder:7b | ✅ | ✅ | ✅ | ✅ |
| Local prism-coder:14b (32K context) | — | ✅ | ✅ | ✅ |
| Cloud upgrade — Claude Sonnet 4 | — | ✅ | ✅ | ✅ |
| Cloud upgrade — Gemini 3 Pro | — | — | ✅ | ✅ |
| Air-gapped enterprise build | — | — | — | ✅ |
