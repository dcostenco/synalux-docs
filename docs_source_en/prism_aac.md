# 🗣️ Prism AAC

**Help nonverbal kids talk.** Augmentative & Alternative Communication for children with motor impairments and complex communication needs. Tap pictures, build sentences, hear them spoken aloud — in 16+ languages. Works on any tablet or laptop, with or without internet.

Open source ([AGPL-3.0](https://github.com/dcostenco/prism-aac/blob/main/LICENSE)). Hosted free at [prism-aac.vercel.app](https://prism-aac.vercel.app). Standalone repo: [`prism-aac`](https://github.com/dcostenco/prism-aac).

<details>
<summary>View Interface / Diagram</summary>

![Prism AAC home screen](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/prism_aac_home.png)
*Home screen — quick categories, math panel, schedule, games, and settings.*

</details>

---

## 🖼️ Pictures → Words → Speech (PECS-style)
The core AAC primitive. Tap picture tiles to build a sentence; the app reads it aloud in the child's language.
*   **22 default categories** — Food, Feelings, School, Body, Animals, Colors, Time, Help/Needs, Quick Talk, etc. Caregiver-extendable.
*   **Pictogram library** — high-contrast, high-readability symbols designed for low-vision users.
*   **Sentence bar** — tap-and-build, then 🔊 to speak. Long-press to edit a tile.
*   **Per-child layouts** — a BCBA can lock categories visible to a specific child.

<details>
<summary>View Interface / Diagram</summary>

![Pictogram categories](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/prism_aac_categories.png)
*Pictogram categories — tap to build a sentence, hear it spoken.*

</details>

---

## ⌨️ Keyboard + Word Prediction
For older or higher-functioning users, a full keyboard with multilingual prediction.
*   **Per-user learning** — prediction model adapts to the child's vocabulary over weeks.
*   **Autocorrect** — fixes hurried/motor-impaired typing (typos, dropped letters, missing diacritics) via Gemini 2.5 Flash-Lite. Multilingual: en/ru/ro/es/uk/pl + Cyrillic/Hebrew/Arabic script detection.
*   **Word completion** — partial → full word in 750ms median (`hw` → `how are you`).
*   **Local-first** — when prism-coder:7b is running on the device, autocorrect runs offline with zero network.

---

## 🍽️ Food Ordering & Real-World Scenarios
Pre-built sentence chains for common situations — restaurants, doctor visits, school transitions.
*   **Quick-order tiles** — "I want pizza", "with cheese", "no onions" — chained in 3 taps.
*   **Allergy alerts** — child can self-advocate ("I am allergic to peanuts") with a single tap.
*   **Caregiver-customizable menus** per restaurant chain (McDonalds, Subway, Olive Garden, etc.).

<details>
<summary>View Interface / Diagram</summary>

![Food ordering scenario](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/prism_aac_food.png)
*Food ordering — real-world scenario tiles for restaurants, school, doctor visits.*

</details>

---

## 🧮 Math Panel (Panther Math Paper-style)
Graph-paper canvas with KaTeX rendering. Designed for school-age users who need to do math without speech.
*   **Drawing surface** — pen + eraser, snapping grid, geometric figures (circle, triangle, parallelogram).
*   **KaTeX equation editor** — write `\frac{x^2}{y}` and have it rendered + spoken aloud.
*   **AI tutor (paid)** — speaks answers, explains step by step. Backed by Claude Sonnet 4 with tier-aware Gemini-3 fallback.
*   **Save & share** — exports to caregiver notes for homework review.

<details>
<summary>View Interface / Diagram</summary>

![Math panel with graph paper canvas](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/prism_aac_math.png)
*Math panel — graph paper, KaTeX equations, optional AI tutor.*

</details>

---

## 🎮 Therapeutic Games (9, evidence-based)
Built to teach communication, NOT for screen-time entertainment.
*   **Bubble Pop** — single-cause-effect for early causality learners.
*   **Color Hunt / Match It / Category Sort** — receptive language + categorization.
*   **My Story** — generative narrative building with picture sequences.
*   **Yes/No / Finish It / Emotion Match / What Comes Next** — comprehension + theory of mind.
*   **Free tier**: 3 games. **Paid tier**: all 9 + caregiver-tuned difficulty.

---

## 👋 Hands-Free with Gesture Recognition
For users who can't reliably tap a touchscreen.
*   **Head-pose tracking** + dwell-click via FaceLandmarker (MediaPipe Tasks). Local, browser-only — no video uploaded.
*   **Hand-pose tracking** for users with limited fine motor control — pinch, point, swipe.
*   **Per-user gesture profiles** — calibrate once, the app remembers.
*   **Configurable dwell time** — 200ms (fast) to 2000ms (cautious).

---

## 🗓️ Visual Schedule & Reward Shop
Picture-based daily routines that reduce transition anxiety.
*   **Time-blocked tiles** — "8am Breakfast", "9am School", "12pm Lunch", with pictograms and a check-off ritual.
*   **Reward shop (paid)** — children earn tokens for completed tasks, redeem for caregiver-approved rewards (extra game time, choice of dinner, etc.). Trauma-informed: opt-in, no punishment mechanic.

---

## 🩺 Clinical-Grade Defaults
Designed with BCBAs and SLPs.
*   **Verbal operant tracking** — matches BACB Task List 5th Edition (mand, tact, intraverbal, echoic).
*   **Caregiver notes sync** (paid) — ABC-format notes travel encrypted between home, school, and clinic via the Synalux portal.
*   **AAC access never restricted as a consequence** — hard-coded into the app design. A child must always have their voice.
*   **Trauma-informed defaults** — no punishment mechanics, reward shop is opt-in, all "negative feedback" UX flows have been removed.

<details>
<summary>View Interface / Diagram</summary>

![Settings — voice, language, accessibility](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/prism_aac_settings.png)
*Settings — voice, language, accessibility, gesture calibration.*

</details>

---

## 📴 Works Offline
The AAC primitive is the user's voice. It cannot depend on a network.

| Feature | Offline-capable | How |
|---|---|---|
| Keyboard input | ✅ | Pure UI |
| Pictogram tiles + categories | ✅ | Bundled assets, IndexedDB persist |
| Local word prediction | ✅ | `engine/predictionEngine.ts` (n-gram + user history) |
| Translation (14 locales) | ✅ | Bundled `offlineDictionary.ts` (4000+ word pairs) |
| Whisper transcription | ✅ | WASM in-browser model |
| Neural TTS (Tier 1.5: Kokoro-82M) | ✅ en/es/fr/pt/ja/zh | Bundled neural model |
| OS Web Speech API premium voices | ✅ | Browser-native |
| WASM espeak-ng (last resort) | ✅ | Bundled fallback |
| Categories/phrases/notes | ✅ | Zustand + IndexedDB |
| Emergency alerts (10-min queue TTL) | ✅ | Local queue, retry on reconnect |
| Sync to Synalux cloud | ❌ online-only | Background, non-blocking |
| AI chat assistant | ❌ online-only | Claude Sonnet 4 via portal |
| Cloud autocorrect (Gemini Flash-Lite) | ⚠️ degrades to local | 5s timeout → local prediction engine |

When the network goes, the device still talks.

---

## 🎙️ Voice (TTS) Architecture — 4-Tier Fallback Chain

| Tier | Engine | Quality | Offline | Notes |
|---|---|---|---|---|
| 1 | Inworld TTS-2 | Best (paid all langs; free for ro/uk/ru/de/ko/ar — Synalux absorbs cost) | — | Default for paid tier |
| 1.5 | Kokoro-82M neural | Very good | ✅ en/es/fr/pt/ja/zh | Bundled WASM |
| 2 | OS Web Speech API premium voices | Good | ✅ | Browser-native |
| 3 | WASM espeak-ng | Acceptable | ✅ | Last resort |

Voice picker (paid): all 60+ Inworld voices, including child voices, accents, and voice cloning ("speak in MY voice — I trained it last week").

---

## 🏗️ Architecture (server-side via Synalux portal)

| Path | Function | Model |
|---|---|---|
| `/api/v1/text/correct` | Autocorrect + word completion | **Gemini 2.5 Flash-Lite** (multilingual bench-validated; 752ms avg; 4.3× cheaper than 2.5 Flash) |
| `/api/v1/prism-aac/predict` | 5-word continuation prediction | **Gemini 2.5 Flash-Lite** (free tier); Claude Haiku/Sonnet (paid) |
| `/api/v1/prism-aac/chat` | AAC AI assistant | Local prism-coder:7b (simple) → 14b (medium, paid) → **Claude Sonnet 4** (complex paid). Fallback: Gemini 3 Flash/Pro Preview by tier. |
| `/api/v1/prism-aac/tts` | Text-to-speech | Inworld TTS-2 + Azure Neural fallback |
| `/api/v1/translate` | Sentence translation | Gemini 2.5 Flash + offline dictionary fallback |
| `/api/v1/transcribe` | Voice → text | Whisper (WASM, in-browser primary) |

**Stack**: Next.js 15 (App Router), Zustand state, Whisper WASM, Inworld TTS-2 + Azure Neural fallback, Kokoro-82M offline TTS, FaceLandmarker (gestures), MediaPipe Tasks (hand pose).

---

## 💳 Plans (Synalux pricing)

| | Free | Paid |
|---|---|---|
| Picture tiles + 22 categories | ✅ | ✅ |
| Type-to-speak | ✅ | ✅ |
| Default voice (Inworld) | ✅ | ✅ |
| Math panel | ✅ basic | ✅ + AI tutor |
| Schedule | ✅ | ✅ + reward shop |
| Games | 3 | All 9 |
| Voice picker (60+ Inworld voices) | — | ✅ |
| Voice cloning | — | ✅ |
| Caregiver notes sync | — | ✅ |
| Word prediction (per-user learning) | — | ✅ |
| AI chat (Claude Sonnet 4 + tier fallback) | — | ✅ |

[See full pricing →](https://synalux.ai/pricing)

---

## 🧪 Self-Host & Fork

```bash
git clone https://github.com/dcostenco/prism-aac.git
cd prism-aac
npm install
npm run dev    # http://localhost:3000
```

AGPL-3.0 — fork freely; share modifications. Synalux operates the canonical hosted version. See [prism-aac/CONTRIBUTING.md](https://github.com/dcostenco/prism-aac/blob/main/CONTRIBUTING.md), [ACCESSIBILITY.md](https://github.com/dcostenco/prism-aac/blob/main/ACCESSIBILITY.md), [SECURITY.md](https://github.com/dcostenco/prism-aac/blob/main/SECURITY.md).
