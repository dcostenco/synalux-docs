# App Store Metadata — Synalux Apps

Single source of truth for App Store Connect listings. Update here first, then paste into App Store Connect.

---

## PrismCoach

### Name
```
PrismCoach
```

### Subtitle (≤ 30 characters)
```
AI Strength Coach · On-Device
```

### Promotional Text (≤ 170 characters — updateable without a new build)
```
Now with Watch AI Coach — ask your coach from your wrist. Prism 1.7B + SmolLM2-360M run fully on-device, no cloud required. Body Battery · Muscle Recovery · Programs.
```

### Description (≤ 4,000 characters)
```
PrismCoach is an AI-powered strength and conditioning coach for iPhone, iPad, and Apple Watch — with all AI running on-device via Metal. No cloud. No subscription required for on-device coaching. No data ever leaves your device.

── ON-DEVICE AI CASCADE ──

PrismCoach runs two local AI models and selects the best one based on available RAM — automatically, every 2 seconds:

• Prism Coder 1.7B (≥1,600 MB free RAM) — fine-tuned strength & conditioning model, 4,096-token context, full Metal GPU offload. Responds in ~300–500 ms.
• SmolLM2-360M (450–799 MB free RAM) — 185 MB footprint, safe on any A14+ device. Fills the gap so coaching is never lost.
• Cloud AI (800–1,599 MB) — Synalux server when the 1.7B won't fit but RAM is too high for SmolLM.
• Core-only mode (<450 MB) — workouts and tracking always work, AI degrades gracefully.

── WATCH AI COACH ──

Ask your AI coach from your wrist. Apple Watch relays your query to the paired iPhone over WatchConnectivity, runs the full on-device cascade, and streams the reply back — no subscription needed. Six tabs on Apple Watch: Dashboard · Muscle Map · Workout · AI Coach · CNS Tap Test · Settings.

── BODY BATTERY ──

Your single readiness score — a composite of overnight HRV, resting heart-rate trend, sleep quality, and 7-day cumulative training load. Score 0–100. Fresh (≥75) · Moderate (50–74) · Fatigued (25–49) · Spent (<25).

── MUSCLE RECOVERY MAP ──

14 anatomical muscle groups tracked on a parametric body canvas. Each muscle decays from 100% → 0% over 48–96 hours based on exercise volume and RPE. Today's target muscles pulse on the canvas.

── TRAINING PROGRAMS ──

Six science-backed periodization templates: PPL, 5/3/1 Wendler, GZCLP, PHUL, Full Body, Deload. Elite subscribers get AI-generated custom multi-week programs built by Prism 8B or Claude Sonnet.

── NUTRITION ENGINE ──

NLP meal logging — describe your meal in plain language, get macros. Protein, carbs, fat, fiber, hydration. Daily targets calculated from bodyweight, goal, and training load.

── TRAINING INTELLIGENCE ──

• ACWR Injury Risk — Acute:Chronic Workload Ratio flags overtraining before injuries happen (Gabbett, 2016)
• Volume Landmarks — MEV / MAV / MRV per muscle, from Renaissance Periodization research
• HR-Adaptive Rest Timer — rest ends when your heart rate actually recovers, not when a timer hits
• Velocity-Based Training — Apple Watch accelerometer estimates bar velocity per rep; flags neuromuscular fatigue at >20% velocity loss
• Sleep-Training Readiness Loop — synthesizes HRV + sleep + Body Battery into one training recommendation

── VOICE CONTROL ──

50+ hands-free commands: log sets, skip rest, ask the AI, navigate tabs — all without touching the screen. On-device speech recognition, no cloud.

── AUTONOMOUS COACH ──

Guided workouts by voice. The coach calls out warm-up cues, monitors bar velocity, adjusts rest time based on heart rate, and gives a full workout summary at the end. No screen required.

── APPLE WATCH ──

6 tabs. Body Battery ring · Muscle map · Live workout logging with rest timer · AI Coach relay · CNS Tap Test · Settings. WatchConnectivity syncs in real time.

── CNS TAP TEST ──

10-second rapid-tap readiness test. Compares today's taps/sec against your personal 14-day baseline. Flags neuromuscular fatigue before you start training.

── VISION AI ──

Equipment scanner (one-time onboarding): point your camera at your gym — Claude Vision maps it to Full Gym / Home Gym / Dumbbells Only / Bodyweight. Every AI prompt is injected with your equipment tier afterward.

Live AR body-pose overlay: 18 joints tracked on-device via Apple Vision, fatigue dots anchor to your actual body in the camera feed.

── PRIVACY ──

All biometric data stays on-device. No analytics SDK. No crash reporting. HealthKit read-only (except workout writes). Pro AI never contacts any server. FemmeEngine cycle data is CoreData-only, never synced.

── LANGUAGES ──

23 languages including Spanish, French, Portuguese, German, Japanese, Korean, Mandarin, Arabic.

─────────────────
Free · Pro ($8.99/mo · $69.99/yr) · Elite ($17.99/mo · $129.99/yr)
```

### Keywords (≤ 100 characters)
```
strength coach,workout,HRV,recovery,AI,on-device,Apple Watch,muscle,body battery,periodization,gym
```

### What's New (version notes)
```
Watch AI Coach — ask your coach from your wrist. Your Apple Watch relays queries to the iPhone, runs Prism 1.7B or SmolLM2-360M on-device, and streams the reply back in seconds.

SmolLM2-360M miniAI tier — when free RAM is 450–799 MB, a 185 MB on-device model activates so coaching never fails on older or loaded devices.

6 Watch tabs: Dashboard · Muscle Map · Workout · AI Coach · CNS Tap Test · Settings.
```

---

## Prism AAC

### Name
```
Prism AAC
```

### Subtitle (≤ 30 characters)
```
Offline AAC · On-Device AI
```

### Promotional Text (≤ 170 characters — updateable without a new build)
```
Speak with confidence — no internet needed. On-device AI in 20 languages. 1,261 pre-translated phrases. Apple Watch emergency phrases. Works on airplanes, in hospitals.
```

### Description (≤ 4,000 characters)
```
Prism AAC is an augmentative and alternative communication (AAC) app for people who are nonverbal or have limited speech — with all AI running on-device. No cloud required for phrase generation, prediction, or translation. No data ever leaves your device.

── ON-DEVICE AI ──

Prism AAC automatically selects the best local model based on your device:

• iPad Pro 16 GB — Prism 14B model (97.1% routing accuracy)
• iPhone / iPad Air — Prism 8B model (98.0% routing accuracy)
• Any other device — Prism 1.7B model (96.1% routing accuracy)
• SmolLM2-360M — activates on low-RAM devices so phrase generation never stops

All models run via Metal GPU acceleration. Instant responses, fully private.

── OFFLINE PHRASE DICTIONARY ──

1,261 core AAC phrases pre-translated into 20 languages — built into the app. Tap a phrase, hear it spoken in the local language. Works on airplanes, in hospitals, anywhere — no Wi-Fi, no cell signal needed.

20 languages: Arabic · Chinese · Dutch · French · German · Hebrew · Hindi · Indonesian · Italian · Japanese · Korean · Filipino · Polish · Portuguese · Romanian · Russian · Turkish · Ukrainian · Vietnamese · English.

── APPLE WATCH ──

Emergency phrases and all 20 language translations work completely offline on Apple Watch. Critical AAC phrases with built-in text-to-speech. Apple Watch Ultra: standalone offline AAC companion.

── PICTURE COMMUNICATION ──

Phrase tiles with picture symbols — all 1,503 icons download in the background on first launch and display offline. Compatible with PECS-style communication boards.

── KEYBOARD MODES ──

Standard mode with categorized phrase tiles. MAX KB mode fills the screen with the keyboard for faster free-form typing. Your preferred mode is remembered.

── TEXT-TO-SPEECH ──

Natural-sounding speech in 20 languages. High-quality on-device TTS with multiple voice options and adjustable rate. Works fully offline.

── AI PHRASE GENERATION ──

The on-device AI generates contextually relevant phrases based on situation, environment, and communication history — without sending data to any server.

── PRIVACY ──

All AI inference is on-device. No phrase data, voice data, or communication history is ever sent to any server. Designed for children, nonverbal adults, and medical environments where privacy is non-negotiable.

── WHO IT'S FOR ──

• Autism spectrum disorder (ASD)
• Cerebral palsy
• ALS / motor neuron disease
• Stroke / aphasia
• Apraxia of speech
• Traumatic brain injury (TBI)
• Anyone who needs a voice when theirs isn't available

── LANGUAGES ──

App UI: English. Phrase output and TTS: 20 languages (see above).

─────────────────
Free · Pro subscription available for advanced AI features.
```

### Keywords (≤ 100 characters)
```
AAC,augmentative,nonverbal,speech,autism,ALS,aphasia,offline,picture,communication,assistive,text to speech
```

### What's New (version 1.4.0)
```
On-device AI — no internet needed for phrase generation, prediction, or translation. Three model tiers select automatically: 14B (iPad Pro 16GB), 8B (iPhone/iPad Air), 1.7B (all others).

Offline phrase dictionary: 1,261 phrases × 20 languages built into the app.

Apple Watch: emergency phrases and all 20 language translations work completely offline.

MAX KB mode: full-screen keyboard for faster typing. Tap ⬇ to restore phrase tiles.
```

---

## Smart App Banner Setup

Add to your website `<head>` to show a native install banner in Safari:

### PrismCoach
```html
<meta name="apple-itunes-app" content="app-id=PRISMCOACH_APP_ID, app-argument=prismcoach://open">
```

### Prism AAC
```html
<meta name="apple-itunes-app" content="app-id=PRISMAAC_APP_ID, app-argument=prismaac://open">
```

Replace `PRISMCOACH_APP_ID` and `PRISMAAC_APP_ID` with the numeric App Store IDs from App Store Connect.

---

## App Store Marketing Checklist

- [ ] Upload screenshots: iPhone 6.9", iPhone 6.3", iPad 13" (required sizes)
- [ ] Upload App Preview video (optional but improves conversion 35%)
- [ ] Set promotional text in App Store Connect (can be updated without a build)
- [ ] Add Smart App Banner meta tag to prismcoach.app and prismaac.app websites
- [ ] Submit for App Store featuring: appstoreconnect.apple.com → Promote → Get Featured
- [ ] Enable "Works with Apple Health" badge on product page
- [ ] Set up pre-order if launching to new regions
- [ ] Generate App Store badges from Apple Marketing Tools for use in social posts
- [ ] Create custom product pages (App Store Connect) for different audiences:
    - PrismCoach: "powerlifting" page, "recovery" page, "Apple Watch" page
    - Prism AAC: "autism" page, "ALS" page, "medical" page
