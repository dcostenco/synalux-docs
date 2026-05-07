# 🌍 Translation

Sentence-level translation across 16+ languages. Offline-first via bundled dictionary; cloud upgrade via Gemini Flash for richer phrasing when online.

---

## 📚 Two-Path Translation Engine

| Path | Engine | When | Quality | Latency | Offline |
|---|---|---|---|---|---|
| **Offline dictionary** | Bundled `offlineDictionary.ts` (4000+ word pairs × 14 locales) | Always tried first; sole engine when offline | Word-level: good. Phrase-level: limited. | <10ms | ✅ |
| **Cloud (Gemini 2.5 Flash)** | `/api/v1/translate` → Gemini Flash | When online + dictionary miss / sentence-level | Excellent — preserves tense, idiom, register | ~700ms | — |

The Prism AAC keyboard's "translate this sentence" feature uses both: dictionary fallback ensures the device always responds, cloud upgrade kicks in when online for better phrasing.

---

## 🌐 Language Coverage

Bundled offline:
`en` · `es` · `fr` · `pt` · `ja` · `zh` · `de` · `ko` · `ar` · `ro` · `uk` · `ru` · `it` · `nl`

Cloud-only (uses Gemini's 100+ language coverage when online):
`hi` · `bn` · `tr` · `pl` · `vi` · `th` · ...

---

## 🩺 Why Offline-First Matters
*   AAC users in school / clinic / remote settings can't depend on Wi-Fi.
*   Patient communication during home visits — clinician's offline dictionary + premium TTS keeps the conversation going.
*   School deployments — bandwidth is throttled or filtered; translation must still work.

---

## 🏗️ Architecture

```
POST /api/v1/translate         { text, sourceLang, targetLang, mode? }
                                 → { translated, source, model }
                                 mode: 'word' | 'sentence' (default: auto)
```

Client-side path (in `services/translateService.ts`):
1. If targetLang in offline dictionary: try local lookup → if hit + mode≠'sentence', return.
2. Else call `/api/v1/translate` (5s timeout matching `/text/correct`).
3. On timeout / error: return original text — never block.

---

## 🔄 Inter-Module Integration
*   **Prism AAC keyboard** — "translate" toggle pre-translates outgoing speech.
*   **AAC chat** — response auto-translated to the user's locale before display.
*   **Mail** — incoming non-locale messages get a one-tap translate-inline.
*   **Patient portal** — UI auto-translates per the patient's preferred language (cookie + browser detect).

---

## 💳 Plans
Available on every tier — translation is an accessibility primitive, not a billing surface. Cloud-translation usage is rate-limited on free tier (200 calls/user/day, same as autocorrect) to control cost.
