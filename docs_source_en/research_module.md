# 🔬 Research

Multi-source clinical research synthesis across academic databases, web, and internal knowledge. Used by the AI assistant to answer "what's the current evidence for X" without leaving Synalux.

---

## 🧠 What It Does
*   **Academic discovery** — parallel search across three free, high-signal sources:
    - **PubMed** (NCBI) — clinical papers, medical evidence
    - **ERIC** (Dept. of Education) — ABA, education research, special needs literature
    - **Semantic Scholar** — AI-powered academic TLDRs, cross-discipline papers
*   **Web fallback** — DuckDuckGo (free, no API key) when academic sources return insufficient results.
*   **Web search** (non-research) — Firecrawl via `POST /api/v1/web-search` for general queries (tier-gated, separate from research).
*   **Synthesis** — Gemini 2.5 Flash with thinking enabled combines all sources into a cited clinical summary.
*   **Knowledge search** — internal Prism MCP knowledge base (workspace-scoped) — see `synalux-private` for the full Prism architecture.

---

## 🩺 Clinical Use Cases
*   "What's the current evidence base for FCT versus DRO in self-injurious behavior?"
*   "Summarize recent papers on telehealth ABA outcomes for ages 3-7."
*   "What does the latest BACB Ethics Code say about consent for video recording?"

The synthesis output is **cited inline** so a clinician can verify each claim against its source.

---

## 🏗️ Architecture
*   `lib/services/research/googleSearch.ts` — discovery service (PubMed + ERIC + Semantic Scholar + DuckDuckGo fallback).
*   `lib/services/research/synthesis.ts` — Gemini 2.5 Flash synthesizer (Thinking mode enabled).
*   `POST /api/v1/research/search` — execute a research query; streams results.

---

## 💳 Plans
Available on **Advanced+**. Per-call cost surfaces in the workspace usage dashboard.
