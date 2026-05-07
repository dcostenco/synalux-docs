# 🧩 Synalux VSCode Extension

Bring the Synalux AI assistant + chat panel into VSCode without leaving your editor.

---

## ✨ Features
*   **Chat panel** — same AI assistant as `synalux.ai/chat` (Claude Sonnet 4 paid default, tier-aware Gemini-3 fallback) but rendered in VSCode's sidebar.
*   **Backend router** — same model routing logic as the web `/chat` (gemini direct → OpenRouter → fallback chain).
*   **Gemini OAuth** — sign-in via Gemini OAuth supported as an alternative to NextAuth Google.

---

## 🔐 Auth Flow
On first use the extension opens `/auth/vscode` in the browser → user signs in → page shows an auth code → user pastes into VSCode. One-time setup; tokens persist in the OS keychain.

---

## 🏗️ Architecture
Source: `synalux-vscode/src/` in `synalux-private`.
*   `backend-router.ts` — picks Gemini direct vs OpenRouter based on user's tier + selected model
*   `chat-panel.ts` — VSCode webview hosting the chat UI
*   `gemini-oauth.ts` — alternative auth flow when user prefers a Gemini account over their workspace login

---

## 💳 Plans
Available on every tier — feature parity gated on the underlying chat backend (free → Gemini 2.5 Flash, paid → Claude Sonnet 4 + tier-aware fallback).

See the [Mobile AI](mobile_ai.md) page for the equivalent on phones.
