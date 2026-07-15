# PrismCoach

**AI-powered strength and recovery coach.** iPhone, iPad, and Apple Watch. Tracks recovery, predicts fatigue, generates training programs, and coaches you in real time — in 23 languages. Core features work fully offline; AI coaching uses on-device inference with optional cloud escalation for complex queries.

> PrismCoach is not medical advice. Consult a physician before starting any exercise program. AI-generated recommendations may be inaccurate and should not replace professional guidance.

---

## Body Battery

Your primary readiness score — a composite of overnight HRV, resting heart rate trend, sleep quality, and training load accumulated over the past 7 days.

*   **Scoring** — 0–100. ≥ 75 = Fresh (green), 50–74 = Moderate (yellow), 25–49 = Fatigued (orange), < 25 = Depleted (red).
*   **HealthKit integration** — reads passive overnight HRV captured by Apple Watch. No manual input required. When HealthKit data is unavailable, the dashboard displays "No Data" instead of a score.
*   **Baseline recalibration** — body battery recomputes its rolling baseline weekly so a well-trained athlete and a beginner see correctly normalised scores.
*   **ATR Engine** — Adaptive Training Readiness synthesises 7+ biometric signals into a single readiness index. Accounts for acute (last 3 days) vs. chronic (28-day) load ratio.

<details>
<summary>View Screenshot — Dashboard</summary>

![PrismCoach Dashboard — Body Battery](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png)
*Body Battery dashboard — composite readiness score, weekly trend, and quick-action shortcuts.*

</details>

---

## Muscle Recovery Map

Per-muscle fatigue tracking across 14 anatomical regions (left/right tracked independently) using a parametric body-map canvas rendered in SwiftUI and an interactive 3D SceneKit avatar.

*   **14 anatomical regions** — Chest, Anterior/Lateral/Posterior Delts, Biceps, Triceps, Traps, Lats, Core, Lower Back, Glutes, Quads, Hamstrings, Calves (plus Forearms, Shins, Feet, Neck). Left and right sides tracked independently.
*   **Charge model** — each muscle decays from 100% to 0% over 48–96 hours post-workout depending on exercise volume and RPE. Recovery follows a sigmoidal curve (not linear).
*   **3D avatar** — interactive SceneKit model (USDZ) with tap-to-select muscles, front/back rotation, and training mode selection (Heavy/Light/Limited).
*   **Color coding** — ≥ 75% green, 50–75% yellow, 25–50% orange, < 25% red.
*   **Injury registry** — mark muscles as "Limited / Pain" to exclude them from AI-generated programs.

<details>
<summary>View Screenshot — Muscle Map</summary>

![PrismCoach Muscle Recovery Map](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png)
*Muscle recovery map — 14 regions, colour-coded by charge. Pulsing overlay shows today's target muscles.*

</details>

---

## Training Programs

12 science-based periodisation templates covering all major training goals. 3 free (Starting Strength, StrongLifts 5x5, Bodyweight Basics); 9 require Pro.

| Program | Structure | Goal |
|---|---|---|
| Starting Strength | 3-day A/B barbell | Beginner linear progression |
| StrongLifts 5x5 | 3-day A/B barbell | Beginner strength |
| GZCLP | 4-day tier system (T1/T2/T3) | Beginner linear progression |
| 5/3/1 Boring But Big | 4-day barbell + accessory | Powerlifting strength |
| PHUL | 4-day upper/lower power+hypertrophy | Balanced strength & size |
| Reddit PPL | 6-day push/pull/legs | Hypertrophy + strength |
| Bodyweight Basics | 3-day no-equipment | Home/travel fitness |
| Upper/Lower Split | 4-day classic split | Balanced hypertrophy |
| nSuns 5/3/1 LP | 5-day high-volume | Intermediate strength |
| Arnold Split | 6-day classic bodybuilding | Hypertrophy |
| Power Building | 4-day powerlifting+hypertrophy | Strength & size |
| Full Body 3x/Week | 3-day compound-focused | General fitness |

*   **AI-generated programs** (Pro) — describe your goal and constraints; PrismCoach generates a fully custom program using the on-device AI or cloud cascade.
*   **Watch sync** — active program caches to Apple Watch for offline reference.

<details>
<summary>View Screenshot — Programs</summary>

![PrismCoach Programs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png)
*Training programs — 12 periodisation templates with AI-generated custom programs for Pro.*

</details>

---

## Nutrition Engine

Meal logger with macro tracking and calorie targets.

*   **Meal logging** — type or dictate meals in plain language. The offline NLP parser extracts food entities, quantities, and units using regex and a built-in food database. No cloud AI required.
*   **Macro targets** — calculated from body weight, goal (cut/bulk/maintain), and activity level using the Mifflin-St Jeor equation. Adjusts daily based on training load.
*   **Caloric tracking** — running daily total with breakdown (protein / carbs / fat).
*   **Food database** — search a built-in database of common foods with nutritional data.

<details>
<summary>View Screenshot — Nutrition</summary>

![PrismCoach Nutrition](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png)
*Nutrition tracker — meal logging, daily macro targets, and calorie tracking.*

</details>

---

## AI Coach

Conversational coaching that knows your recovery state, last session, and program context.

*   **Free tier** — 3 AI messages per day.
*   **Pro — on-device AI** — Qwen 3.5-4B runs via llama.cpp with Metal acceleration on 6 GB+ devices. Falls back to 1.7B on lower-memory devices. Zero network, fully private for on-device queries.
*   **Pro — cloud cascade** — for complex queries, the app escalates to Prism 4B inference server, then Claude Sonnet as fallback. Cloud queries send anonymised training context (no PII, no raw HealthKit data).
*   **Context window** — injects current muscle charges, body battery score, active program, and injury registry into every prompt.
*   **Voice output** — AI replies spoken via text-to-speech with sentence-level highlighting. Music volume ducks automatically during speech.
*   **Voice input** — push-to-talk and hands-free set logging via Speech framework.

> AI Coach is not a certified personal trainer or medical professional. Recommendations are generated by AI models and may be inaccurate. Always verify advice with a qualified professional, especially regarding injuries or medical conditions.

<details>
<summary>View Screenshot — AI Coach</summary>

![PrismCoach AI Coach](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png)
*AI Coach — context-aware conversational coach with voice output.*

</details>

---

## Camera Features (Pro)

*   **Body Scan** — provide one clear, full-body photo (choose from your library or take a new one facing the camera). Apple's Vision framework runs on the still image to detect body pose (skeleton joint positions), overlays the detected skeleton so you can confirm the fit, and measures shoulder/hip proportions to scale the 3D avatar to your body shape. Includes lens-distortion compensation for close-range captures. Runs entirely on-device — the photo is never uploaded.
*   **Equipment Recognition** — capture a photo of your gym setup; the image is sent to a cloud AI vision model for classification into equipment tiers (full gym / home gym / dumbbells / bodyweight). Requires network connection.

> Note: Equipment recognition sends the captured photo to a cloud API for analysis. No biometric or health data is included in this request.

---

## Apple Watch App

Full companion app — not just notifications. Independent session tracking on wrist.

*   **6 Watch tabs** — Dashboard (Body Battery), Muscle Map, Workout Logger, AI Coach, CNS Tap Test, Settings.
*   **Workout session** — log sets (exercise, weight, reps, RPE) directly from wrist. HR-adaptive rest timer adjusts rest duration based on current vs. resting heart rate. Full HKWorkoutSession + HKLiveWorkoutBuilder integration.
*   **CNS Tap Test** — 10-second pre-workout fast-tap test. Measures taps/sec; flags neuromuscular fatigue if below personal baseline. 7-day sparkline trend.
*   **AI Coach on Watch** — queries relay to iPhone via WatchConnectivity. Falls back to direct cloud or on-device SmolLM2-360M (CPU-only) when iPhone is unreachable.
*   **Watch complications** — Body Battery score available in circular, rectangular, inline, and corner complication families.
*   **Phone sync** — WatchConnectivity bridge pushes muscle batteries, body battery, streaks, and injury registry bidirectionally.

<details>
<summary>View Screenshot — Watch Dashboard</summary>

![PrismCoach Apple Watch](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png)
*Apple Watch companion — Body Battery glanceable dashboard with recovery ring.*

</details>

---

## Femme Engine

Cycle-phase-aware metric adjustments for female athletes (opt-in, Pro).

*   **4 phases** — Menstrual, Follicular, Ovulatory, Luteal.
*   **Training adjustments** — recovery rate multipliers (0.80x–1.15x) and HR zone offsets shift per phase based on published research on hormonal effects on strength and recovery.
*   **Body battery correction** — heart rate variability baselines are adjusted by phase to prevent false fatigue flags mid-cycle.
*   **Privacy** — cycle data stored locally only.

---

## Sleep & HRV

Overnight recovery science running silently in the background.

*   **HRV capture** — passive HealthKit queries for overnight HRV samples. No active measurement required.
*   **Sleep stage analysis** — reads Apple's sleep stage data (awake/core/deep/REM) to score sleep quality.
*   **Body battery baseline** — rolling 28-day median HRV used as personal reference; deviations drive the battery score.

---

## Voice & TTS

AI coaching spoken aloud in your language.

*   **Text-to-speech** — AVSpeechSynthesizer with auto-selection of highest available voice quality (premium ≥ enhanced ≥ default). Sentence-level highlighting during playback.
*   **Music ducking** — TTS engine automatically ducks Apple Music / Spotify during coaching speech and restores volume after.
*   **Auto-tone inference** — message content is scanned for emotional keywords and the appropriate tone is selected automatically.
*   **Voice input** — push-to-talk set logging and AI chat via Speech framework.

---

## Languages

23 supported languages via Apple's speech stack and text-to-speech.

*   **BCP-47 language codes** — per-user language preference stored in LanguageStore; used for TTS voice selection and AI coach system prompt locale.
*   **23 languages** — English, Spanish, French, Portuguese, German, Italian, Dutch, Polish, Russian, Ukrainian, Romanian, Japanese, Korean, Chinese (Simplified), Chinese (Traditional), Cantonese, Arabic, Hindi, Hebrew, Vietnamese, Filipino, Turkish, Indonesian.

---

## Music Integration

Workout-phase-aware music with BPM sync.

*   **Apple Music & Spotify** — connects to your music library.
*   **Phase-adaptive BPM** — configurable BPM ranges per workout phase (warmup/working/rest/cooldown). Music automatically transitions between phases.
*   **Coaching duck** — music volume drops during AI speech and TTS, then restores.
*   **BPM settings** — per-phase BPM sliders, linked playlists, auto-transition toggle.

---

## Engagement

*   **Workout streaks** — consecutive training day tracking with rest-day grace (1 per week). At-risk warnings. Bounce animation on increment.
*   **Weekly adherence** — circular progress ring showing workouts completed vs. target training days.
*   **Share card** — branded post-workout image with exercise count, sets, duration, streak badge, and trained muscle silhouette. Share via iOS share sheet.
*   **Notifications** — streak-at-risk (next day 6pm), recovery-ready (most fatigued muscle's projected recovery), inactivity win-back (3-day repeating). All local.

---

## Privacy

*   **On-device first** — core features (tracking, programs, body battery) work fully offline with no network.
*   **AI routing** — on-device AI (Qwen 3.5-4B / 1.7B) processes queries locally. For complex queries, Pro users' context is sent to Prism inference server or Claude Sonnet via encrypted HTTPS. Only anonymised training context is sent — no PII, no raw HealthKit samples.
*   **Equipment recognition** — camera photos are sent to a cloud vision API for equipment classification. No biometric data is included.
*   **HealthKit** — read-only access except workout session writes. Described in App Store privacy label.
*   **CloudKit** — workout history and profile sync across user's own devices via iCloud.
*   **Cycle data** — Femme Engine data stored locally only, never synced.
*   **No analytics SDK** — no third-party crash reporting. Datadog logging for aggregate app-level events only (tab views, launch count).

---

## Plans

Billing is 100% Apple In-App Purchase (StoreKit 2). Local currency handled automatically by Apple's price tier system.

| Feature | Free | Pro |
|---|---|---|
| Body Battery + HRV dashboard | ✅ | ✅ |
| Muscle recovery map | ✅ | ✅ |
| 3 training templates | ✅ | ✅ |
| 3 AI messages / day | ✅ | ✅ |
| All 12 training templates | — | ✅ |
| Unlimited AI coaching | — | ✅ |
| Full nutrition engine | — | ✅ |
| Camera body scan & equipment recognition | — | ✅ |
| Femme Engine (cycle tracking) | — | ✅ |
| Apple Watch companion | — | ✅ |
| Unlimited workout history | — | ✅ |
| 3D body visualizer | — | ✅ |
| **Monthly** | Free | $9.99/mo |
| **Annual** | Free | $59.99/yr (1-week free trial) |

Product IDs: `ai.synalux.prismcoach.pro.monthly`, `ai.synalux.prismcoach.pro.annual`

---

## Tests

~1,484 automated tests (1,356 unit + 128 UI) covering core engines — ATR, Body Battery, Muscle Battery, AI routing, Nutrition, Sleep, CNS, Subscription, CloudKit, VBT, Voice commands, and more.

<details>
<summary>Technical Documentation / Specifications</summary>

```
watchOS build:    ✅ BUILD SUCCEEDED
iOS tests:        ✅ ~1,484 tests
```

</details>

---

## Sources

PrismCoach's training algorithms are informed by peer-reviewed research. In-app Sources tab lists 13 citations from Sports Medicine, JSCR, Frontiers in Physiology, and other journals with verifiable PubMed links.
