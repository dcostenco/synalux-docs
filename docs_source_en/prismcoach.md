# 🏋️ PrismCoach

**Military-grade AI fitness coach.** iPhone · iPad · Apple Watch app. Tracks recovery, predicts fatigue, generates training programs, and coaches you in real-time — in 23 languages. Works fully offline with an on-device AI model (Pro+). Standalone repo: [`forge-watch`](https://github.com/dcostenco/forge-watch).

---

## 🔋 Body Battery

Your primary readiness score — a composite of overnight HRV, resting heart rate trend, sleep quality, and training load accumulated over the past 7 days.

*   **Scoring** — 0–100. ≥ 75 = Fresh (green), 50–74 = Moderate (yellow), 25–49 = Fatigued (orange), < 25 = Depleted (red).
*   **HealthKit integration** — reads passive overnight HRV captured by Apple Watch. No manual input required.
*   **Baseline recalibration** — body battery recomputes its rolling baseline weekly so a well-trained athlete and a beginner see correctly normalised scores.
*   **ATR Engine** — Adaptive Training Readiness synthesises 7+ biometric signals into a single readiness index. Accounts for acute (last 3 days) vs. chronic (28-day) load ratio.

<details>
<summary>View Screenshot — Dashboard</summary>

![PrismCoach Dashboard — Body Battery](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png)
*Body Battery dashboard — composite readiness score, weekly trend, and quick-action shortcuts.*

</details>

---

## 💪 Muscle Recovery Map

Per-muscle fatigue tracking across 14 anatomical regions using a parametric body-map canvas rendered in SwiftUI.

*   **14 muscle groups** — Chest, Anterior/Lateral/Posterior Delts, Biceps, Triceps, Traps, Lats, Core, Lower Back, Glutes, Quads, Hamstrings, Calves.
*   **Charge model** — each muscle decays from 100% to 0% over 48–96 hours post-workout depending on exercise volume and RPE. Recovery follows a sigmoidal curve (not linear).
*   **Front / Back toggle** — tap to flip the silhouette. iOS uses a segmented picker; watchOS shows both views as swipe tabs.
*   **Color coding** — ≥ 75% green, 50–75% yellow, 25–50% orange, < 25% red.
*   **Training highlights** — muscles targeted by today's program pulse orange on the canvas.

<details>
<summary>View Screenshot — Muscle Map</summary>

![PrismCoach Muscle Recovery Map](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png)
*Muscle recovery map — 14 regions, colour-coded by charge. Pulsing overlay shows today's target muscles.*

</details>

---

## 📋 Training Programs

Six science-based periodisation templates covering all major training goals.

| Program | Structure | Goal |
|---|---|---|
| PPL (Power/Push/Pull/Legs) | 6-day upper/lower split | Hypertrophy + strength |
| 5/3/1 Wendler | 4-day barbell + accessory | Powerlifting strength |
| GZCLP | 3-day tier system | Beginner linear progression |
| Upper/Lower | 4-day classic split | Balanced hypertrophy |
| Full Body | 3-day compound-focused | General fitness |
| Deload / Maintenance | 1-day active recovery | Regeneration |

*   **AI-generated programs** (Elite) — describe your goal and constraints; PrismCoach generates a fully custom multi-week block using Prism 8B or Claude Sonnet.
*   **JSON Program Generator** — programs are represented as typed Swift models; the engine can generate a full 8-week program in < 500 ms on-device.
*   **Watch sync** — active program caches to Apple Watch for offline coaching (< 100 KB payload).

<details>
<summary>View Screenshot — Programs</summary>

![PrismCoach Programs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png)
*Training programs — six periodisation templates with AI-generated custom programs for Elite.*

</details>

---

## 🍎 Nutrition Engine

NLP-powered meal logger — describe food in plain language, get macros.

*   **NLP meal logging** — type or dictate "2 eggs, toast with butter, black coffee" and the engine parses food entities, quantities, and units using regex + Claude Haiku.
*   **Macro targets** — calculated from body weight, goal (cut/bulk/maintain), and activity level. Adjusts daily based on training load.
*   **Caloric tracking** — running daily total with breakdown (protein / carbs / fat / fibre / water).
*   **Nutrient density scoring** — flags micronutrient gaps based on logged foods.
*   **Hydration reminders** — adaptive push notifications based on workout sweat rate estimate.

<details>
<summary>View Screenshot — Nutrition</summary>

![PrismCoach Nutrition](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png)
*Nutrition tracker — NLP meal logging, daily macro targets, and hydration tracking.*

</details>

---

## 🤖 AI Coach

Conversational coaching that knows your recovery state, last session, and program context.

*   **Free tier** — no AI (static program templates only).
*   **Pro — Prism 1.7B on-device** — runs via llama.cpp with Metal acceleration. Zero network, fully private. Answers questions about your training, suggests form corrections, adjusts today's volume based on readiness.
*   **Elite — Prism 1.7B → 8B → Claude Sonnet cascade** — on-device first; escalates to Prism inference server (8B) for complex questions; falls back to Claude Sonnet for nuanced coaching.
*   **Context window** — ForgeMemoryStore injects last 3 sessions, active program week, current muscle charges, and body battery score into every prompt.
*   **Voice output** — AI replies are spoken via ForgeTTSEngine: Synalux cloud TTS (MP3, 24 kHz) with AVSpeechSynthesizer offline fallback. Six coaching tones: Friendly, Calm, Excited, Precise, Empathetic, Hopeful.
*   **Proactive coaching** — ProactiveCoachEngine surfaces unprompted insights (e.g. "Your HRV dropped 15% — consider reducing intensity today") based on 7 trigger types.

<details>
<summary>View Screenshot — AI Coach</summary>

![PrismCoach AI Coach](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png)
*AI Coach — context-aware conversational coach with voice output and proactive insights.*

</details>

---

## ⌚ Apple Watch App

Full companion app — not just notifications. Independent session tracking on wrist.

*   **5 Watch tabs** — Dashboard (Body Battery), Muscle Map, Workout Logger, CNS Tap Test, Settings.
*   **Workout session** — log sets (exercise, weight, reps, RPE) directly from wrist. 90-second rest timer with haptic countdown.
*   **CNS Tap Test** — 10-second pre-workout fast-tap test. Measures taps/sec; flags neuromuscular fatigue if below personal baseline.
*   **Haptic Pace-Keeper** — rhythmic haptics during AMRAP/EMOM circuits.
*   **Phone sync** — WatchConnectivity bridge pushes batteries, body battery, and feature flags bidirectionally in real time.
*   **Auto-Set Detection** — accelerometer + gyroscope recognise set start/stop and classify exercise type. Disable to save watch battery.
*   **Velocity-Based Training** — wrist-mounted bar velocity estimation using CoreMotion. Flags neuromuscular fatigue when bar speed drops > 15%.

<details>
<summary>View Screenshot — Watch Dashboard</summary>

![PrismCoach Apple Watch](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png)
*Apple Watch companion — Body Battery glanceable dashboard with recovery ring.*

</details>

---

## 🧬 Femme Engine

Cycle-phase-aware metric adjustments for female athletes (opt-in).

*   **4 phases** — Menstrual, Follicular, Ovulatory, Luteal.
*   **Training adjustments** — volume, intensity targets, and RPE recommendations shift per phase based on published research on hormonal effects on strength and recovery.
*   **Body battery correction** — basal body temperature and heart rate variability baselines are adjusted by phase to prevent false fatigue flags mid-cycle.
*   **Privacy** — cycle data never leaves the device (CoreData, no sync).

---

## 🧠 Sleep & HRV

Overnight recovery science running silently in the background.

*   **HRV capture** — passive HealthKit queries for overnight HRV samples. No active measurement required.
*   **Sleep stage analysis** — reads Apple's sleep stage data (awake/core/deep/REM) to score sleep quality.
*   **Training loop** — SleepTrainingLoop correlates prior day's load with next-morning HRV to build a personal stress–recovery model over time.
*   **Body battery baseline** — rolling 28-day median HRV used as personal reference; deviations drive the battery score.

---

## 🔊 Voice & TTS

AI coaching spoken aloud in your language.

*   **Synalux TTS** — cloud MP3 synthesis at 24 kHz/96 kbps mono via Synalux portal. 6 coaching tones.
*   **Offline fallback** — AVSpeechSynthesizer with auto-selection of highest available voice quality (premium ≥ enhanced ≥ default). Works in all 23 supported languages.
*   **Music ducking** — ForgeTTSEngine automatically ducks Apple Music / Spotify during coaching speech and restores volume after.
*   **Auto-tone inference** — message content is scanned for emotional keywords (PR, fatigue, injury, comeback, etc.) and the appropriate tone is selected automatically.
*   **Voice commands** — VoiceCommandEngine handles hands-free set logging ("log 100kg 5 reps RPE 8") and navigation ("show my muscle map") via Speech framework.

---

## 🌍 Languages

23 supported languages via Apple's speech stack + Synalux TTS.

*   **BCP-47 language codes** — per-user language preference stored in LanguageStore; used for TTS voice selection and AI coach system prompt locale.
*   **AI coaching** — prompts are written in the user's selected language. Claude and Prism models handle all 23 languages.
*   **23 languages** — English, Spanish, French, Portuguese, German, Italian, Dutch, Polish, Russian, Ukrainian, Romanian, Czech, Hungarian, Swedish, Norwegian, Finnish, Japanese, Korean, Mandarin, Arabic, Hindi, Turkish, Hebrew.

---

## 🏗️ Architecture

*   **PrismCoachCore** — shared Swift Package (SPM) containing all engines, models, and business logic. Consumed by the iOS app, Mac Catalyst app, and watchOS extension.
*   **llama.cpp (Metal)** — on-device inference for Prism 1.7B GGUF model via a local SPM package (`_llama_cpp_local`). iOS/macOS only; excluded from watchOS at compile time.
*   **WatchConnectivity bridge** — `WatchBridge` syncs muscle batteries, body battery, and feature flags bidirectionally between iPhone and Watch in real time.
*   **CloudKit sync** — `CloudKitSyncEngine` replicates workout history and user profile across devices using CKRecord change tokens with conflict resolution.
*   **HealthKit** — reads HRV, sleep stages, resting HR, active energy, and workout samples. Writes workout session summaries.
*   **Siri Intents** — `LogWorkoutIntent`, `GetBodyBatteryIntent`, `StartRestTimerIntent` for Shortcuts integration.

---

## 🔒 Privacy

*   **Local-first** — all biometric data stays on-device. No analytics SDK. No third-party crash reporting.
*   **HealthKit** — read-only access except workout session writes. Described in App Store privacy label.
*   **AI prompts** — Coach tier never sends data to any server. Athlete tier sends anonymised training context to Prism inference server (no PII, no HealthKit data).
*   **Subscription check** — email posted via HTTPS to `api.prismcoach.app/subscription/check`. Email stored in Keychain with 24-hour TTL and 48-hour grace window.
*   **Cycle data** — Femme Engine data is CoreData-only, never synced.

---

## 💳 Plans

| Feature | Free | Coach | Athlete |
|---|---|---|---|
| Body Battery + HRV dashboard | ✅ | ✅ | ✅ |
| Muscle recovery map | ✅ | ✅ | ✅ |
| Workout logging (60-day history) | ✅ | ✅ | ✅ |
| Unlimited workout history | — | ✅ | ✅ |
| All 6 training templates | — | ✅ | ✅ |
| Full nutrition engine + food DB | — | ✅ | ✅ |
| Body visualizer (front/back canvas) | — | ✅ | ✅ |
| Apple Watch companion app | — | ✅ | ✅ |
| Femme Engine (cycle tracking) | — | ✅ | ✅ |
| AI Coach — Prism 1.7B on-device | — | ✅ | ✅ |
| AI Coach — Prism 8B server | — | — | ✅ |
| AI Coach — Claude Sonnet cascade | — | — | ✅ |
| AI-generated custom programs | — | — | ✅ |
| **Monthly** | Free | $8.99/mo | $17.99/mo |
| **Annual** | Free | $69.99/yr | $129.99/yr |

Subscribe at [prismcoach.app/subscribe](https://prismcoach.app/subscribe) — Stripe-backed web checkout. No in-app purchase required.

---

## 🧪 Tests

904 automated tests covering all core engines — ATR, Body Battery, Muscle Battery, AI routing, Nutrition, Sleep, CNS, Siri Intents, Subscription, CloudKit, VBT, Voice commands, and more.

```
watchOS build:    ✅ BUILD SUCCEEDED
iOS tests (904):  ✅ 904/904 passed, 0 failures
```
