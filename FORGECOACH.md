# ForgeCoach

**Military-grade AI fitness coaching for iPhone, iPad, and Apple Watch.**

Track recovery, predict fatigue, generate periodized programs, and get coached in real time — in 23 languages. Fully offline with on-device AI (Pro+).

<p align="center">
  <a href="https://apps.apple.com/app/forgecoach/id123456789"><img src="https://img.shields.io/badge/App_Store-Download-0D96F6?style=for-the-badge&logo=apple" alt="App Store"></a>
  <a href="https://forgecoach.app/subscribe"><img src="https://img.shields.io/badge/Pricing-Free_·_Pro_·_Elite-43e97b?style=for-the-badge" alt="Pricing"></a>
  <img src="https://img.shields.io/badge/iOS_17+-watchOS_10+-764ba2?style=for-the-badge" alt="iOS 17+ watchOS 10+">
  <img src="https://img.shields.io/badge/Tests-904_passing-brightgreen?style=for-the-badge" alt="Tests">
</p>

🌐 **Translations:** [Español](docs/i18n/forgecoach_es.md) · [Français](docs/i18n/forgecoach_fr.md) · [Português](docs/i18n/forgecoach_pt.md) · [Română](docs/i18n/forgecoach_ro.md) · [Українська](docs/i18n/forgecoach_uk.md) · [Русский](docs/i18n/forgecoach_ru.md) · [Deutsch](docs/i18n/forgecoach_de.md) · [日本語](docs/i18n/forgecoach_ja.md) · [한국어](docs/i18n/forgecoach_ko.md) · [中文](docs/i18n/forgecoach_zh.md) · [العربية](docs/i18n/forgecoach_ar.md)

---

## 🔋 Body Battery

Your single readiness score — a composite of overnight HRV, resting heart-rate trend, sleep quality, and 7-day cumulative training load.

- **Score 0–100** — ≥ 75 Fresh (green), 50–74 Moderate (yellow), 25–49 Fatigued (orange), < 25 Spent (red)
- **Passive HealthKit sync** — reads overnight HRV captured by Apple Watch; no manual input
- **ATR Engine** — Adaptive Training Readiness synthesizes 7+ biometric signals into a single readiness index, balancing acute (3-day) vs chronic (28-day) load
- **Weekly baseline recalibration** — scores normalize over time so a well-trained athlete and a beginner both read correctly

<p align="center">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png" width="280" alt="Body Battery Dashboard">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png" width="180" alt="Watch Dashboard">
</p>
<p align="center"><em>Body Battery dashboard — readiness score, weekly trend, and quick-action shortcuts. Watch companion shows the ring at a glance.</em></p>

---

## 💪 Muscle Recovery Map

Per-muscle fatigue tracking across 14 anatomical regions on a parametric body-canvas rendered in SwiftUI.

- **14 muscle groups** — Chest, Anterior/Lateral/Posterior Deltoid, Biceps, Triceps, Traps, Lats, Core, Lower Back, Glutes, Quads, Hamstrings, Calves
- **Decay model** — each muscle recovers from 100% → 0% over 48–96 h post-workout based on exercise volume and RPE; recovery follows a sigmoid curve
- **Front/back toggle** — tap to flip the silhouette; iOS uses a segmented picker, watchOS shows both as swipeable tabs
- **Color coding** — ≥ 75% green · 50–75% yellow · 25–50% orange · < 25% red
- **Workout highlights** — today's program target muscles pulse orange on the canvas

<p align="center">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png" width="280" alt="Muscle Recovery Map">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_02_bodymap.png" width="180" alt="Watch Body Map">
</p>
<p align="center"><em>Muscle recovery map — 14 regions color-coded by load. The pulsing overlay shows today's target muscles.</em></p>

---

## 📋 Training Programs

Six science-backed periodization templates covering every major training goal, plus AI-generated custom blocks.

| Program | Structure | Goal |
|---|---|---|
| PPL (Push/Pull/Legs) | 6-day upper/lower split | Hypertrophy + strength |
| 5/3/1 Wendler | 4-day barbell + accessories | Powerlifting strength |
| GZCLP | 3-day tiered system | Linear beginner progression |
| PHUL (Power Hypertrophy) | 4-day classic split | Balanced hypertrophy |
| Full Body | 3-day compound emphasis | General fitness |
| Deload / Maintenance | 1-day active recovery | Regeneration |

- **AI-generated programs** (Elite) — describe your goal and constraints; ForgeCoach generates a custom multi-week block using Prism 8B or Claude Sonnet
- **JSON Program Generator** — programs are typed Swift models; the engine generates a full 8-week program in < 500 ms on-device
- **Watch sync** — active program is cached on Apple Watch for offline training (< 100 KB payload)

<p align="center">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png" width="280" alt="Training Programs">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_03_workout.png" width="180" alt="Watch Workout">
</p>
<p align="center"><em>Training programs — six periodization templates, plus AI-custom programs for Elite. Watch shows live set logging with rest timer.</em></p>

---

## 🍎 Nutrition Engine

NLP-driven meal logging — describe the food in plain language, get the macros.

- **NLP meal entry** — type or dictate "2 eggs, buttered toast, black coffee" and the engine parses food entities, quantities, and units using regex + Claude Haiku
- **Macro targets** — calculated from bodyweight, goal (deficit / surplus / maintenance), and activity level; adjusted daily by training load
- **Calorie tracking** — running daily total with breakdown (protein / carbs / fat / fiber / water)
- **Nutrient density score** — flags micronutrient gaps based on logged foods
- **Hydration reminders** — adaptive push notifications based on estimated sweat rate during exercise

<p align="center">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png" width="280" alt="Nutrition Engine">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_04_nutrition.png" width="380" alt="Nutrition Engine iPad">
</p>
<p align="center"><em>Nutrition tracker — NLP meal logging, daily macro targets, and hydration tracking.</em></p>

---

## 🤖 AI Coach (Cascade)

Conversational coaching that knows your recovery state, last session, and program context.

| Tier | Route | Latency | Privacy |
|---|---|---|---|
| Free | No AI — static templates only | — | — |
| Pro | Prism 1.7B on-device (Metal) | ~500 ms | 100% local — no network |
| Elite | Prism 1.7B → 8B → Claude Sonnet | ~500 ms / ~1.5 s / ~3 s | Anon context to Prism server; Claude for complex queries |

- **Context window** — ForgeMemoryStore injects last 3 sessions, active program week, current muscle loads, and Body Battery score into every prompt
- **Voice output** — AI responses spoken via ForgeTTSEngine: Synalux cloud TTS (MP3, 24 kHz) with AVSpeechSynthesizer offline fallback; 6 coaching tones: Friendly, Calm, Enthusiastic, Precise, Empathetic, Hopeful
- **Proactive coaching** — ProactiveCoachEngine surfaces unsolicited insights ("Your HRV dropped 15% — consider reducing intensity today") based on 7 trigger types
- **Velocity-based feedback** — wrist-mounted bar velocity estimation via CoreMotion flags neuromuscular fatigue when bar speed drops > 15%

<p align="center">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_05_aicoach.png" width="280" alt="AI Coach iPhone">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png" width="380" alt="AI Coach iPad">
</p>
<p align="center"><em>AI Coach — contextual conversational coaching with voice output and proactive insights. iPad shows the full chat UI.</em></p>

---

## ⌚ Apple Watch

Full companion app — not just notifications. Independent wrist-side session tracking.

- **5 watch tabs** — Dashboard (Body Battery), Muscle Map, Workout Log, CNS Tap Test, Settings
- **Workout session** — log sets (exercise, weight, reps, RPE) directly from your wrist; 90-second rest timer with haptic countdown
- **CNS Tap Test** — 10-second rapid-tap test before training; measures taps/sec and flags neuromuscular fatigue below personal baseline
- **Haptic Pacer** — rhythmic haptics during AMRAP/EMOM circuits
- **Auto Set Detection** — accelerometer + gyroscope recognize set start/end and classify exercise type
- **Phone sync** — WatchConnectivity bridge pushes muscle batteries, body battery, and feature flags bidirectionally in real time

<p align="center">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png" width="180" alt="Watch Dashboard">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_02_bodymap.png" width="180" alt="Watch Body Map">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_03_workout.png" width="180" alt="Watch Workout">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_04_cns.png" width="180" alt="Watch CNS Test">
</p>
<p align="center"><em>Apple Watch companion — Body Battery ring, muscle map, live workout logging, and CNS tap test.</em></p>

---

## 🧬 FemmeEngine

Cycle-phase metric adjustments for female athletes (optional, never synced off-device).

- **4 phases** — Menstrual, Follicular, Ovulatory, Luteal
- **Training adjustments** — volume, intensity targets, and RPE recommendations shift per phase based on published research on hormonal effects on strength and recovery
- **Body Battery correction** — basal body temperature and HRV baselines are phase-adjusted to avoid mid-cycle false fatigue signals
- **Privacy** — cycle data stays in CoreData only; no sync, no cloud

---

## 🌍 23 Languages

Coaching and UI available in English, Spanish, French, Portuguese, German, Italian, Dutch, Polish, Russian, Ukrainian, Romanian, Czech, Hungarian, Swedish, Norwegian, Finnish, Japanese, Korean, Mandarin, Arabic, Hindi, Turkish, Hebrew.

<p align="center">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_06_settings.png" width="280" alt="Settings">
  <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_05_settings.png" width="180" alt="Watch Settings">
</p>
<p align="center"><em>Settings — language picker, subscription tier, AI routing, TTS voice selection, and FemmeEngine toggle.</em></p>

---

## 💳 Plans

| Feature | Free | Pro | Elite |
|---|---|---|---|
| Body Battery + HRV dashboard | ✅ | ✅ | ✅ |
| Muscle recovery map | ✅ | ✅ | ✅ |
| Workout log (60-day history) | ✅ | ✅ | ✅ |
| Unlimited workout history | — | ✅ | ✅ |
| All 6 training templates | — | ✅ | ✅ |
| Full nutrition engine + food database | — | ✅ | ✅ |
| Body visualizer (front/back canvas) | — | ✅ | ✅ |
| Apple Watch companion app | — | ✅ | ✅ |
| FemmeEngine (cycle tracking) | — | ✅ | ✅ |
| AI Coach — Prism 1.7B on-device | — | ✅ | ✅ |
| AI Coach — Prism 8B server | — | — | ✅ |
| AI Coach — Claude Sonnet cascade | — | — | ✅ |
| AI-generated custom programs | — | — | ✅ |
| **Monthly** | Free | $8.99/mo | $17.99/mo |
| **Annual** | Free | $69.99/yr | $129.99/yr |

Subscribe at [forgecoach.app/subscribe](https://forgecoach.app/subscribe) — web payment via Stripe. No in-app purchase required.

---

## 🔬 Science

- Mifflin-St Jeor BMR (JADA, 1990)
- ACSM activity multipliers (Resource Manual, 8th ed.)
- NSCA protein targets: 1.5–2.2 g/kg BW by goal (NSCA Essentials, 4th ed.)
- Menstrual cycle recovery modifiers: McNulty et al., 2020 (*Sports Medicine*)
- CNS tap-test readiness: Saldanha et al., 2019 (*JSCR*)
- Sleep stage analysis: Apple HealthKit HKCategoryTypeIdentifierSleepAnalysis

---

## 🔒 Privacy

All biometric data stays on-device. No analytics SDK. No third-party crash reporting.

- **HealthKit** — read-only except workout session writes; described in App Store privacy label
- **AI prompts (Pro)** — never sends data to any server
- **AI prompts (Elite)** — sends anonymized training context to Prism inference server (no PII, no HealthKit data)
- **Subscription check** — email sent over HTTPS to `api.forgecoach.app`; stored in Keychain with 24-hour TTL and 48-hour grace window
- **Cycle data** — FemmeEngine data is CoreData-only, never synced

---

*© Synalux · All rights reserved*
