# 🔬 Research

Multi-source synthesis across web, internal knowledge, and recent papers. Used by the AI assistant to answer "what's the current evidence for X" without leaving Synalux.

---

## 🧠 What It Does
*   **Web search** — Brave Search API for real-time results.
*   **Paper analysis** — Gemini 2.5 Flash with thinking enabled for synthesis of clinical / technical documents.
*   **Knowledge search** — internal Prism MCP knowledge base (workspace-scoped) — see `synalux-private` for the full Prism architecture.
*   **Synthesis** — combines all three into a cited summary the assistant can quote in chat.

---

## 🩺 Clinical Use Cases
*   "What's the current evidence base for FCT versus DRO in self-injurious behavior?"
*   "Summarize recent papers on telehealth ABA outcomes for ages 3-7."
*   "What does the latest BACB Ethics Code say about consent for video recording?"

The synthesis output is **cited inline** so a clinician can verify each claim against its source.

---

## 🏗️ Architecture
*   `lib/services/research/synthesis.ts` — core synthesizer.
*   `POST /api/v1/research` — execute a research query; streams results.
*   Uses Gemini 2.5 Flash for synthesis (Thinking mode enabled — leaves the chat-default Sonnet 4 alone).

---

## 💳 Plans
Available on **Advanced+**. Per-call cost surfaces in the workspace usage dashboard.
