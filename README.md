# ✦ Synalux

**Stop spending half your day on paperwork.**

Synalux listens to your sessions, writes the notes, files the claims, schedules the follow-ups, and chases the prior auths — so you can focus on patients.

For ABA practices, pediatrics, mental health, dentistry, physical therapy, dermatology, veterinary, and family medicine. HIPAA-compliant. 12 languages. Works offline.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Try_It-Free-43e97b?style=for-the-badge" alt="Try Free"></a>
  <a href="https://synalux.ai/pricing"><img src="https://img.shields.io/badge/Pricing-See_Plans-764ba2?style=for-the-badge" alt="Pricing"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/HIPAA-Ready-blue?style=for-the-badge" alt="HIPAA"></a>
</p>

🌐 **Translations:** [Español](docs/i18n/README_es.md) · [Français](docs/i18n/README_fr.md) · [Português](docs/i18n/README_pt.md) · [Română](docs/i18n/README_ro.md) · [Українська](docs/i18n/README_uk.md) · [Русский](docs/i18n/README_ru.md) · [Deutsch](docs/i18n/README_de.md) · [日本語](docs/i18n/README_ja.md) · [한국어](docs/i18n/README_ko.md) · [中文](docs/i18n/README_zh.md) · [العربية](docs/i18n/README_ar.md)

---

## What you get

### 🎙 Stop typing notes
Speak the session. Synalux dictates, structures into SOAP, codes, and files it. Audio never leaves your device.

### 📅 One calendar, every account
Google Calendar + Outlook in one view. Schedule with **Google Meet, Microsoft Teams, or Zoom** in one click.

### 📨 Mail without switching tabs
Gmail + Outlook + Slack + Discord + Telegram + WhatsApp + SMS — all read and replied to inside Synalux. AI-suggested quick replies.

### 💸 Get paid faster
Real-time insurance eligibility. EDI 837P claims. Stripe Connect for copays. Built-in CPT calculator catches the Medicare 8-minute rule and remainder rollover.

### 🎥 Telehealth that just works
1080p video on weak Wi-Fi. No patient downloads. Picture-in-picture so you can chart while you talk.

### 📴 Works offline
Trial data on a tablet at a remote school? Collect, save, sync when you are back.

### 🔒 Provably secure
Every PHI access is immutably logged with a tamper-evident hash chain. Local AI models mean patient data never leaves your clinic.

---

## Try it

| Surface | URL | What |
|---|---|---|
| **Web app** | [synalux.ai/app](https://synalux.ai/app) | Full clinical UI |
| **Patient Portal** | [synalux.ai/patient-portal](https://synalux.ai/patient-portal) | Where families sign forms + pay bills |
| **Mail** | [synalux.ai/mail](https://synalux.ai/mail) | Unified mailbox |
| **Calendar** | [synalux.ai/calendar](https://synalux.ai/calendar) | Cross-provider scheduling |
| **Drive** | [synalux.ai/drive](https://synalux.ai/drive) | Practice file storage |
| **Chat** | [synalux.ai/chat](https://synalux.ai/chat) | AI assistant + messaging |

---

## Who it's for

| Specialty | What Synalux solves for you |
|---|---|
| **🧩 ABA / BCBA** | Data collection, BIP drafts, EVV, insurance auth — all automated. RBTs get a tablet-optimized field UI. |
| **🧠 Mental Health** | PHQ-9/GAD-7/Columbia SSRS built in. Safety planning, medication tracking, and HIPAA telehealth without add-ons. |
| **👶 Pediatrics** | WHO/CDC growth curves, CDC immunization alerts, Vanderbilt scoring, and parent portal — standard on every chart. |
| **🦷 Dental & Ortho** | Full-mouth tooth chart, periodontal pocket entry, DICOM viewer, implant sequencing, and Stripe payment plans. |
| **🏃 Physical Therapy** | ROM graphs, functional test scoring, HEP builder, and prior auth justification notes — automated. |
| **🔬 Dermatology** | Body map, photo series, biopsy tracking, iPLEDGE compliance, and biologics management. |
| **🐾 Veterinary** | Species-specific records, breed-aware vitals, DICOM, DEA drug log, and owner portal. |
| **🏥 Multi-specialty / Group** | One platform, separate branch workspaces, HQ-level reporting, and white-label per location. |

---

## Modules

Click any module name to expand the full description and setup guide.

---

### 🩺 Core Clinical Workflow

<details>
<summary><strong>🧩 Applied Behavior Analysis (ABA)</strong> — Eliminate ABA paperwork; data collection, BIPs, and insurance run themselves</summary>

<br>

![ABA Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/07_abc_data_collection.png)

The Synalux ABA module automates the paperwork nightmare of ABA therapy through intelligent data collection, automated report drafting, and seamless insurance management. The interface is optimized for iPad and touch devices — built for field sessions with children.

**Key features:**
- **Ambient SOAP Notes** — WASM Whisper transcribes on-device; zero cloud PHI, one-click sign-off
- **ABC Data Collection** — Touch-optimized trials (DTT/NET), frequency, duration, and latency recording
- **FBA → BIP Builder** — Guided functional behavior assessment with automated Behavior Intervention Plan drafts
- **EVV + Payroll** — Electronic Visit Verification linked directly to payroll and insurance billing
- **Progress Reports** — Auto-generated graphs and narrative summaries for insurance and families
- **RBT Role View** — Simplified interface for technicians — session data only, no admin clutter
- **Offline-first** — Collect trial data on a school tablet with no Wi-Fi; syncs on reconnect

**Quick setup:**
1. Go to **Admin → Modules** and enable **Applied Behavior Analysis**
2. Add BCBAs under **Team → Roles** (BCBA credential) and RBTs under the RBT role
3. Open any patient chart → **ABA** tab → start a session

▶️ [Watch setup video](https://youtu.be/tvA6XnglbDk) · [📖 Full documentation](https://synalux.ai/docs/applied_behavior_analysis_aba)

</details>

---

<details>
<summary><strong>📝 Clinical Notes & Documentation</strong> — Speak the session; Synalux writes the note — no typing, no cloud PHI</summary>

<br>

![Clinical Notes](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/04_soap_note.png)

Synalux transforms the clinical note from a chore into an automated byproduct of your session. WASM-powered voice dictation and specialty-specific templates deliver 100% documentation compliance with zero cloud PHI transmission.

**Key features:**
- **Voice Dictation** — Speak the session; Synalux structures it into SOAP format automatically
- **16+ Specialty Templates** — Pre-built for ABA, pediatrics, mental health, PT, dentistry, dermatology, and more
- **ICD-10 / CPT Auto-Coding** — Diagnosis and procedure codes suggested from note content
- **e-Signature** — BoldSign integration; providers sign from any device
- **Offline Drafts** — Notes saved locally during connectivity loss, synced on reconnect
- **Audit Trail** — Immutable hash-chained log of every edit and signature event

**Quick setup:**
1. Enable **Clinical Documentation** in **Admin → Modules**
2. Select your specialty template under **Settings → Note Templates**
3. Open a patient encounter → **New Note** → speak or type

▶️ [Watch setup video](https://youtu.be/f0FhfbsS1mM) · [📖 Full documentation](https://synalux.ai/docs/clinical_notes_documentation)

</details>

---

<details>
<summary><strong>📅 Scheduling & Appointments</strong> — Fill your schedule and cut no-shows — patients book and confirm themselves</summary>

<br>

![Scheduling Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/15_scheduling.png)

The Scheduling module supports the full appointment lifecycle from patient request through completion, with two-way sync to Google Calendar and Outlook.

**Key features:**
- **Full Lifecycle** — Scheduled → Confirmed → In-Progress → Completed, plus Cancelled / No-show / Rescheduled
- **Patient Self-Scheduling** — Patients request times through the Patient Portal; staff confirm or deny
- **Google Calendar + Outlook Sync** — Two-way sync; schedule with Google Meet, Teams, or Zoom in one click
- **Conflict Detection** — Prevents double-booking across providers and rooms
- **Automated Reminders** — SMS + email reminders at configurable intervals before appointments
- **Recurring Appointments** — Weekly ABA sessions, monthly check-ups, or custom cadences

**Quick setup:**
1. Enable **Scheduling** in **Admin → Modules**
2. Connect calendars under **Settings → Calendar Integrations**
3. Go to **Schedule** tab → **New Appointment** → select provider, patient, and time

▶️ [Watch setup video](https://youtu.be/YTY10Luaq8k) · [📖 Full documentation](https://synalux.ai/docs/scheduling_appointments)

</details>

---

<details>
<summary><strong>🎥 Telehealth</strong> — See patients anywhere — they click a link, no downloads, no accounts</summary>

<br>

![Telehealth Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/17_telehealth.png)

Built on LiveKit open-source SFU — bandwidth-adaptive video keeps calls connected on slow connections. Patients join from a browser link; no app or account needed.

**Key features:**
- **1080p Adaptive Video** — Automatically adjusts quality to maintain connection on slow Wi-Fi
- **No Downloads** — Patients join from a browser link — no app, no account
- **Picture-in-Picture** — Chart and document while the video call runs in a floating window
- **Group Sessions** — Multi-participant for case conferences, family sessions, team meetings
- **Screen Sharing** — Share patient education materials or clinical data during the call
- **Session Recording** — Optional encrypted recording with patient consent workflow

**Quick setup:**
1. Enable **Telehealth** in **Admin → Modules**
2. Configure LiveKit credentials under **Settings → Telehealth**
3. From any appointment → **Start Telehealth** → send the patient link via SMS or email

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/telehealth_livekit)

</details>

---

<details>
<summary><strong>📴 Offline-First Clinical Workflow</strong> — Keep working when Wi-Fi dies — notes save locally and sync when you're back</summary>

<br>

![Offline Workflow](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/36_global_dash.png)

Built for rural clinics, hospital basements, and school fieldwork — every keystroke is saved locally and synced securely the moment connectivity returns.

**Key features:**
- **Local Persistence** — Notes saved to device secure storage as you type
- **Crash Recovery** — Browser or tablet crash? Your draft is waiting exactly where you left off
- **Sync Status Indicator** — Sidebar shows current sync status and pending item count
- **Conflict Resolution** — Smart merge when the same record is edited offline on two devices
- **Local AI Models** — Voice dictation and clinical AI run entirely on-device
- **EVV Offline** — ABA session data collected offline syncs when reconnected

**Quick setup:**
Offline mode is enabled by default. No configuration required. The sync icon in the sidebar shows green (synced) or amber (pending uploads).

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/offline_first_clinical_sessions)

</details>


### 🏥 Specialty Modules

<details>
<summary><strong>🧠 Mental Health & Psychiatry</strong> — Spend the session listening — PHQ-9, safety plans, and notes handled automatically</summary>

<br>

![Mental Health Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/31_mental_health.png)

A trauma-informed, high-security environment — PHQ-9, GAD-7, Columbia Suicide Severity Rating, medication management, and HIPAA-compliant telehealth built in.

**Key features:**
- **Specialty Templates** — PHQ-9, GAD-7, Columbia SSRS, mental status exam pre-built
- **Crisis Protocols** — Built-in safety planning tools and emergency contact escalation
- **Medication Management** — Full psychiatric medication tracking with dosage history and refills
- **Secure Telehealth** — HIPAA-compliant video sessions with session notes synced automatically
- **Progress Tracking** — Symptom severity graphs over time; shareable with patients
- **Privacy Flags** — Extra-sensitive record protection with additional access controls

**Quick setup:**
1. Enable **Mental Health & Psychiatry** in **Admin → Modules → Specialties**
2. Assign providers the Mental Health role under **Team → Roles**
3. Open a patient chart → **Mental Health** tab

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/mental_health_psychiatry)

</details>

---

<details>
<summary><strong>👶 Pediatrics</strong> — Never miss a milestone or a due vaccine — growth charts and immunization alerts are automatic</summary>

<br>

![Pediatrics Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/27_pediatrics.png)

Automated WHO/CDC growth percentiles, proactive immunization alerts, ADHD Vanderbilt scoring, and a parent portal — designed for the well-child visit workflow.

**Key features:**
- **WHO/CDC Growth Curves** — Automated percentile calculation for weight, height, head circumference
- **Immunization Alerts** — Proactive notifications when vaccines are due; CDC schedule integration
- **ADHD Vanderbilt Scoring** — Parent and teacher forms with automated score calculation
- **Developmental Milestones** — Structured tracking at standard well-child visit intervals
- **Parent Portal Access** — Parents see growth charts, upcoming vaccines, and visit summaries
- **School Forms** — Generate medication authorization and health summary letters automatically

**Quick setup:**
1. Enable **Pediatrics** in **Admin → Modules → Specialties**
2. Patient age auto-triggers pediatric templates for patients under 18
3. Open a patient chart → **Pediatrics** tab → enter visit measurements

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/pediatrics)

</details>

---

<details>
<summary><strong>🦷 Dental & Orthodontics</strong> — Chart a full mouth in minutes — implant sequences and payment plans write themselves</summary>

<br>

![Dental Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/33_dental.png)

AI-assisted periodontal charting, multi-phase implant sequencing, full-mouth tooth chart, and automated Stripe payment plans for modern dental and orthodontic practices.

**Key features:**
- **Periodontal Charting** — Fast pocket depth and recession entry with automatic BPE scoring
- **Tooth Chart** — Interactive full-mouth diagram; click to annotate findings, restorations, extractions
- **Implant Sequencing** — Multi-phase treatment planning (consultation → placement → crown)
- **Orthodontic Progress** — Before/after photo documentation, bracket placement records
- **X-Ray & DICOM** — Digital radiography integration; DICOM viewer built in
- **Payment Plans** — Treatment cost breakdown with installment scheduling via Stripe

**Quick setup:**
1. Enable **Dental & Orthodontics** in **Admin → Modules → Specialties**
2. Configure fee schedule under **Settings → Billing → Dental CDT Codes**
3. Open a patient chart → **Dental** tab → start a new exam

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/dental_orthodontics)

</details>

---

<details>
<summary><strong>🏃 Physical Therapy & Sports Medicine</strong> — Prove progress to insurers — ROM graphs and functional scores generated automatically</summary>

<br>

![Physical Therapy Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/32_physical_therapy.png)

ROM tracking with trend graphs, evidence-based rehab protocols, and Home Exercise Programs delivered directly to the patient's phone.

**Key features:**
- **ROM Tracking** — Angle entry with trend graphs across visits
- **Functional Tests** — Timed Up-and-Go, BERG Balance Scale, QuickDASH automated scoring
- **HEP Builder** — Drag-and-drop home exercise programs with video instruction links sent to patient portal
- **Progress Photography** — Standardized photo series for range-of-motion comparison
- **Modality Tracking** — Log ultrasound, TENS, heat/ice, manual therapy with dosage records
- **Insurance Justification** — Auto-generate functional progress notes for prior auth renewals

**Quick setup:**
1. Enable **Physical Therapy** in **Admin → Modules → Specialties**
2. Add PT/PTA staff and assign PT roles under **Team → Roles**
3. Open a patient chart → **PT** tab → create an initial evaluation

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/physical_therapy_sports_medicine)

</details>

---

<details>
<summary><strong>🔬 Dermatology</strong> — Track every lesion precisely — photo comparisons and iPLEDGE compliance handled automatically</summary>

<br>

![Dermatology Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/34_dermatology.png)

High-resolution photo documentation, full-body lesion mapping, automated iPLEDGE tracking, and biologics management for modern dermatology practices.

**Key features:**
- **Body Map** — Pin lesions on a full anatomical diagram; track size and color changes over time
- **Photo Series** — Standardized capture with side-by-side visit comparison
- **Biopsy Tracking** — Log sites, pathology results, and follow-up actions in one workflow
- **iPLEDGE Support** — Isotretinoin enrollment tracking with monthly pregnancy test logging
- **Biologics Management** — Prior auth, infusion scheduling, REMS compliance
- **Cosmetic Procedures** — Document fillers, Botox units, and treatment areas with before/after photos

**Quick setup:**
1. Enable **Dermatology** in **Admin → Modules → Specialties**
2. Assign providers the Dermatology role under **Team → Roles**
3. Open a patient chart → **Dermatology** tab → start a new skin exam

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/dermatology)

</details>

---

<details>
<summary><strong>🐾 Veterinary Medicine</strong> — Species-specific care without specialty software — DICOM, drug logs, and wellness plans built in</summary>

<br>

![Veterinary Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/28_veterinary.png)

Species-specific body maps, breed-aware vital flags, DICOM imaging, DEA-compliant controlled drug logs, and subscription wellness plans for dogs, cats, horses, and exotics.

**Key features:**
- **Species-Specific Records** — Anatomical body maps for dogs, cats, horses; breed-aware vital flags
- **Growth Curves** — Weight and BCS (1-9) tracked against species norms
- **DICOM Viewer** — Integrated X-ray and imaging viewer attached to patient records
- **Wellness Plans** — Subscription preventive care with auto-renewals
- **Controlled Drug Log** — DEA-compliant Schedule II–V tracking with per-dose audit trail
- **Owner Portal** — Pet owners see vaccination records, upcoming appointments, and invoices

**Quick setup:**
1. Enable **Veterinary Medicine** in **Admin → Modules → Specialties**
2. Select species list under **Settings → Veterinary → Species Configuration**
3. Create a patient record → set species → open the **Vet** clinical tab

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/veterinary_medicine)

</details>


### 💳 Billing & Revenue Cycle

<details>
<summary><strong>💳 Billing & Payments</strong> — Get paid faster with fewer denials — claims, eligibility, and ERA auto-posting in one place</summary>

<br>

![Billing Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/13_billing_payments.png)

EDI 837P claim submission, real-time insurance eligibility, ERA auto-posting, Stripe Connect copay collection, and Medicare-correct CPT calculation in one engine.

**Key features:**
- **EDI 837P Claims** — Submit electronic claims directly to payers; batch submission supported
- **Real-Time Eligibility** — Verify coverage, copays, and deductibles before appointments
- **ERA / 835 Processing** — Auto-post remittance advice; flag denials for follow-up
- **Stripe Connect** — Each practice gets its own payment infrastructure; copays collected online
- **CPT Calculator** — Medicare 8-minute rule, remainder rollover, and modifier suggestions automatic
- **Multi-Country Tax** — VAT/GST/HST handling for international deployments

**Quick setup:**
1. Enable **Billing** in **Admin → Modules**
2. Connect Stripe account under **Settings → Billing → Stripe Connect**
3. Add payers under **Settings → Insurance Payers** with EDI credentials

▶️ [Watch setup video](https://youtu.be/5mKnq7UxDAw) · [📖 Full documentation](https://synalux.ai/docs/billing_payments_module)

</details>

---

<details>
<summary><strong>📋 Superbills</strong> — Stop manually coding visits — superbills write themselves from your encounter note</summary>

<br>

![Superbills](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/13_billing_payments.png)

Auto-populate ICD-10, CPT, and modifiers from the encounter note — then batch-review and distribute in one end-of-day workflow.

**Key features:**
- **Auto-Population** — ICD-10 and CPT codes pulled from the encounter note automatically
- **Specialty Templates** — Common code combinations pre-loaded per specialty
- **Per-Provider Customization** — Fee schedules and template preferences saved per provider
- **Batch Review** — End-of-day workflow to review, modify, and approve multiple superbills at once
- **Patient Distribution** — Send to patient portal or email in one click
- **Resubmission** — Edit and resubmit denied superbills with change tracking

**Quick setup:**
1. Enable **Superbills** in **Admin → Modules → Billing**
2. Configure fee schedule under **Settings → Billing → CPT Fee Schedule**
3. Complete an encounter → **Generate Superbill** appears automatically

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/superbills_module)

</details>

---

<details>
<summary><strong>🏦 Patient Insurance</strong> — Know coverage before the visit, not after — real-time eligibility and prior auth built in</summary>

<br>

![Patient Insurance](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/13_billing_payments.png)

Real-time eligibility, multi-policy management (primary/secondary/tertiary), automated prior authorization, and appeal letter generation for denials.

**Key features:**
- **Real-Time Eligibility** — Validates coverage, copays, deductibles, and remaining benefits instantly
- **Multi-Policy Support** — Primary / Secondary / Tertiary with effective dates and subscriber info
- **Prior Authorization** — Automated PA requests with status tracking; appeal letters from templates
- **Authorization Tracking** — Units authorized vs. used per authorization code
- **Denial Management** — Flag, categorize, and track claim denials with follow-up workflows
- **Coverage Alerts** — Warn staff when a patient's coverage expires or nears annual limits

**Quick setup:**
1. Enable **Patient Insurance** in **Admin → Modules**
2. Add payer contracts under **Settings → Insurance → Payer Configuration**
3. Open patient chart → **Insurance** tab → add policy → run eligibility check

▶️ [Watch setup video](https://youtu.be/aq3WJEIvO1c) · [📖 Full documentation](https://synalux.ai/docs/patient_insurance_module)

</details>

---

### 👤 Patient Management

<details>
<summary><strong>🏥 Patient Portal</strong> — Patients complete intake, sign forms, and pay bills before they arrive — no phone tag</summary>

<br>

![Patient Portal](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/14_patient_portal.png)

Mobile-optimized secure portal — intake forms, document signing, bill pay, progress reports, and secure messaging without requiring an app download.

**Key features:**
- **Online Intake Forms** — Patients complete demographics, consent, and health history before the first visit
- **Document Signing** — BoldSign e-signature for consent forms, treatment agreements, and releases
- **Appointment Requests** — Patients request times; staff confirm or suggest alternatives
- **Bill Pay** — Copays, balances, and payment plans paid online via Stripe
- **Progress Reports** — ABA graphs, therapy notes, and visit summaries accessible to families
- **Secure Messaging** — HIPAA-compliant messaging between patients and the care team

**Quick setup:**
1. Enable **Patient Portal** in **Admin → Modules**
2. Configure URL and branding under **Settings → Patient Portal → White Label**
3. From any patient record → **Invite to Portal** → patient receives a setup email

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/patient_portal)

</details>

---

<details>
<summary><strong>⚠️ Allergies & Safety Alerts</strong> — Stop adverse drug events before they start — every order checked against every allergy automatically</summary>

<br>

![Allergies Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/02_patient_dashboard.png)

Allergy data cross-referenced with every medication and procedure order in real time — adverse drug events stopped before they happen.

**Key features:**
- **Drug Interaction Checker** — Real-time alerts when a new prescription conflicts with existing meds or allergies
- **Severity Levels** — Mild / Moderate / Severe / Anaphylaxis with reaction type
- **Procedure Alerts** — Contrast dye, latex, and anesthetic allergies flagged at point of order entry
- **EHR Sync** — Allergy list syncs across all clinical modules; updated once, visible everywhere
- **Override Workflow** — Providers override with documented justification, logged to audit trail
- **Allergy History** — Full audit trail of additions, removals, and overrides

**Quick setup:**
Allergies is enabled by default. Add allergies in any patient chart → **Allergies** → **Add Allergy**. Conflict alerts appear automatically at order entry.

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/allergies_alerts_module)

</details>

---

<details>
<summary><strong>💉 Immunizations</strong> — Never miss a due vaccine — CDC schedule alerts and state registry reporting automated</summary>

<br>

![Immunizations Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/24_immunizations.png)

CVX-coded vaccine tracking with CDC schedule alerts, VIS delivery to patient portal, and bi-directional state immunization registry integration.

**Key features:**
- **CVX Code Support** — Every vaccine identified by CDC standard vaccine code
- **Dose Tracking** — Lot number, manufacturer, dose number, site, route, and administering provider
- **CDC Schedule Alerts** — Proactive reminders when doses are due based on patient age and history
- **VIS Delivery** — Vaccine Information Statements sent to patient portal with acknowledgment tracking
- **Immunization Registry** — State IIS integration (IZ Gateway) for bi-directional reporting
- **Catch-Up Schedules** — Automatic catch-up schedule for patients behind on vaccines

**Quick setup:**
1. Enable **Immunizations** in **Admin → Modules**
2. Configure state IIS credentials under **Settings → Immunizations → Registry**
3. Open patient chart → **Immunizations** tab → record administered vaccine

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/immunizations_module)

</details>

---

<details>
<summary><strong>📚 Patient Education</strong> — Prescribe education that patients actually read — track who opened what, in their language</summary>

<br>

![Patient Education](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/08_progress_reports.png)

Providers prescribe education materials during encounters — patients see them in the portal, and providers track whether they have been read.

**Key features:**
- **Content Library** — Organized by condition, procedure, and specialty; text, images, and video
- **Prescribable Materials** — Assign during encounters; materials appear immediately in Patient Portal
- **Read Tracking** — Know which patients have viewed their assigned materials
- **16-Language Support** — Automatic language selection based on patient language preference
- **Custom Content** — Upload practice-specific education materials
- **Caregiver Delivery** — Send to parent/guardian portal for pediatric patients

**Quick setup:**
1. Enable **Patient Education** in **Admin → Modules**
2. Browse the library at **Settings → Education → Content Library**
3. During any encounter → **Assign Education** → select materials → patient sees them in portal

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/patient_education_module)

</details>


### 🩺 Clinical Management

<details>
<summary><strong>💊 Medications & Prescriptions</strong> — Prescribe in seconds, stay DEA-compliant — 12,000 drugs, EPCS, and refill requests built in</summary>

<br>

![Medications Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/21_pharmacy.png)

12,000+ drug catalog with NDC codes, active prescription tracking, DEA-compliant controlled substance logs, and SureScripts electronic prescribing.

**Key features:**
- **Drug Catalog** — 12,000+ medications with NDC codes, classifications, schedules, and common doses
- **Active Prescriptions** — Per-patient view with dosage, frequency, prescribing provider, pharmacy, and refills
- **Controlled Substance Log** — DEA-compliant Schedule II–V tracking with per-dose audit trail
- **Refill Management** — Refill requests from patient portal; provider approves in one click
- **Pharmacy Integration** — Electronic prescriptions via SureScripts (EPCS for controlled substances)
- **Drug Classes** — SSRIs, stimulants, retinoids, biologics, bronchodilators, NSAIDs, antibiotics

**Quick setup:**
1. Enable **Medications** in **Admin → Modules**
2. Connect pharmacy network under **Settings → Medications → SureScripts**
3. Open patient chart → **Medications** tab → **New Prescription**

▶️ [Watch setup video](https://youtu.be/rEHa6zj5kwA) · [📖 Full documentation](https://synalux.ai/docs/medications_prescriptions_module)

</details>

---

<details>
<summary><strong>📊 Vitals & Measurements</strong> — Catch deteriorating patients early — vitals trend automatically, abnormals alert instantly</summary>

<br>

![Vitals Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/29_vitals.png)

Capture all standard vitals with automatic trend analysis and out-of-range alerts. Pediatric age-adjusted norms built in; Bluetooth device import supported.

**Key features:**
- **Standard Vitals** — Blood pressure, heart rate, respiratory rate, temperature, SpO2, weight, height, BMI
- **Pain Scale** — 0–10 numeric scale documented per visit with trend graph
- **Trend Analysis** — Visual graphs across visits; deteriorating trends flagged automatically
- **Abnormal Alerts** — Out-of-range values flagged with severity (low / high / critical)
- **Pediatric Norms** — Age-adjusted reference ranges for pediatric patients
- **Device Integration** — Import from Bluetooth blood pressure cuffs, scales, and pulse oximeters

**Quick setup:**
1. Enable **Vitals** in **Admin → Modules** (on by default for most specialties)
2. Configure reference ranges per specialty under **Settings → Vitals → Reference Ranges**
3. Open any patient encounter → **Vitals** section → enter measurements

▶️ [Watch setup video](https://youtu.be/mHFCvre3v5I) · [📖 Full documentation](https://synalux.ai/docs/vitals_measurements_module)

</details>

---

<details>
<summary><strong>🧪 Lab Orders & Results</strong> — Order labs and get results back — Quest, LabCorp, and in-house with critical value paging</summary>

<br>

![Lab Orders Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/26_lab_orders.png)

Order entry with vendor tracking through result receipt with automatic abnormal flagging and critical value alerts via bi-directional HL7 v2.x interface.

**Key features:**
- **Order Management** — Vendor tracking (Quest, LabCorp, in-house), priority levels (routine / urgent / stat)
- **Individual Results** — Reference ranges with automatic abnormal flags (low / high / critical)
- **Panel Results** — CBC, CMP, lipid panels with component-level visualization
- **Critical Alerts** — Automatic notification to ordering provider for critical values
- **Trending** — Side-by-side comparison of repeat labs over time
- **HL7 Integration** — Bi-directional HL7 v2.x interface for lab system integration

**Quick setup:**
1. Enable **Lab Orders** in **Admin → Modules**
2. Configure lab interfaces under **Settings → Labs → Lab Partners**
3. Open patient encounter → **Orders** tab → **New Lab Order**

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/lab_orders_results_module)

</details>

---

<details>
<summary><strong>✅ Clinical Tasks</strong> — Nothing falls through the cracks — abnormal results and expiring auths auto-create tasks</summary>

<br>

![Clinical Tasks](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/36_global_dash.png)

Priority-based task management with automatic task creation from clinical events — abnormal lab results, expiring authorizations, or upcoming recalls trigger tasks automatically.

**Key features:**
- **Task Management** — Priority levels, due dates, category tags, delegation between providers and staff
- **Event-Triggered Tasks** — Abnormal lab result → follow-up task created automatically
- **Shared Task Lists** — Real-time status with comments and attachments for collaborative resolution
- **Notification Alerts** — SMS + in-app notifications for new assignments and approaching deadlines
- **Audit History** — Full record of every task action with timestamp and user
- **Dashboard View** — Provider-specific queue with overdue highlighting

**Quick setup:**
Tasks is enabled by default. Access via **Tasks** in the left sidebar. Configure auto-triggers under **Settings → Tasks → Automation Rules**.

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/clinical_tasks_module)

</details>

---

<details>
<summary><strong>📬 Recalls & Reminders</strong> — Bring patients back before they forget — recall campaigns run themselves on your schedule</summary>

<br>

![Recalls Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/15_scheduling.png)

Configure recall intervals per visit type — the system generates recall lists and sends multi-channel outreach to bring patients back at the right time.

**Key features:**
- **Configurable Intervals** — Set 6-month dental, annual physical, or custom recall cadences per visit type
- **Recall Lists** — Auto-generated when patients are due; filterable by provider and date range
- **Multi-Channel Outreach** — SMS, email, and in-app notification with delivery status tracking
- **Batch Campaigns** — Seasonal campaigns (flu shots, school physicals) with merge-field personalization
- **Response Tracking** — See who opened, clicked, and scheduled from each campaign
- **Opt-Out Management** — Patient communication preferences respected per channel

**Quick setup:**
1. Enable **Recalls** in **Admin → Modules**
2. Configure intervals under **Settings → Recalls → Visit Type Rules**
3. Go to **Recalls** dashboard → review due list → send batch campaign

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/recalls_reminders_module)

</details>

---

<details>
<summary><strong>🔗 Referrals & Cross-Practice Chat</strong> — Know where every referral stands — from sent to scheduled, with automatic status updates</summary>

<br>

![Referrals Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/22_collaboration_suite.png)

Full referral lifecycle tracking with secure inter-practice messaging and fax integration — Pending through Completed or Declined, with automatic status notifications.

**Key features:**
- **Referral Tracking** — Referring/receiving provider, specialty, diagnosis codes, urgency, auth status
- **Full Lifecycle** — Pending → Sent → Accepted → Scheduled → Completed / Expired / Declined
- **Secure Messaging** — HIPAA-compliant messages between practices with document attachments
- **Fax Integration** — Send referral packets via SRFax/Phaxio without leaving Synalux
- **Status Notifications** — Referring practice notified when referral is accepted or scheduled
- **Referral Analytics** — Track volume, response times, and conversion rates by provider

**Quick setup:**
1. Enable **Referrals** in **Admin → Modules**
2. Add network contacts under **Settings → Referral Network**
3. Open patient chart → **Referrals** tab → **New Referral**

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/referrals_cross_practice_chat_module)

</details>

---

### ⚙️ Operations & Administration

<details>
<summary><strong>👥 HR & Staff Management</strong> — Stop chasing license renewals — credential expiration alerts fire automatically</summary>

<br>

![HR Management Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/16_hr_management.png)

Full HR administration — credential expiration alerts, time-off management, KPI-weighted performance reviews, and onboarding checklists with e-signature.

**Key features:**
- **Staff Profiles** — Employment type, hire date, salary/hourly rate, specialties, and department
- **Credential Tracking** — Licenses and certifications with expiration dates and automated renewal alerts
- **Time Off Management** — PTO requests, approvals, and balance tracking by staff member
- **Performance Reviews** — KPI-weighted reviews with customizable metrics per role
- **Onboarding Checklists** — New hire task lists with document collection and e-signature
- **Role-Based Access** — Granular permission assignment per staff role across all modules

**Quick setup:**
1. Enable **HR & Staff Management** in **Admin → Modules**
2. Add staff under **Team → Staff** with roles and department
3. Upload licenses under each staff profile → **Credentials** tab

▶️ [Watch setup video](https://youtu.be/GMcj1rZGAtY) · [📖 Full documentation](https://synalux.ai/docs/hr_staff_management_module)

</details>

---

<details>
<summary><strong>⏱️ Timesheets & Payroll</strong> — Payroll runs itself — timesheets generate from signed session notes, no manual entry</summary>

<br>

![Timesheets Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/16_hr_management.png)

Timesheets build themselves as session notes are signed — eliminating manual entry errors. Medicaid EVV-compliant with QuickBooks and ADP export.

**Key features:**
- **Auto-Generated Timesheets** — Signing a session note creates the timesheet entry automatically
- **EVV Compliance** — Electronic Visit Verification timestamps meet Medicaid requirements
- **Approval Workflow** — Staff submit → supervisor reviews → payroll exports with one click
- **Payroll Export** — QuickBooks, ADP, and CSV export formats
- **Overtime Tracking** — FLSA overtime rules enforced; alerts when staff approach weekly limits
- **Manual Adjustments** — Supervisors adjust entries with documented justification

**Quick setup:**
1. Enable **Timesheets** in **Admin → Modules**
2. Configure pay periods under **Settings → Payroll → Pay Period**
3. Timesheets populate automatically from signed session notes; review at **Payroll → Timesheets**

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/timesheets_payroll_module)

</details>

---

<details>
<summary><strong>📦 Inventory Management</strong> — Never run out of supplies — auto reorder kicks in before stock hits zero</summary>

<br>

![Inventory Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/25_inventory.png)

Enterprise-grade inventory to prevent stock-outs and track high-value assets across all storage locations — dental implants, biologics, vaccines, and office supplies.

**Key features:**
- **SKU Tracking** — Full visibility across all storage locations; QR code scanning supported
- **Reorder Points** — Automatic purchase order drafts when stock falls below minimums
- **Physical Count** — Scheduled audit workflows with variance reporting
- **Vaccine Cold Chain** — Temperature log integration for cold storage compliance
- **Fixed Asset Depreciation** — Straight-line and declining balance depreciation schedules
- **Supplier Management** — Purchase orders, receiving confirmations, and invoice matching

**Quick setup:**
1. Enable **Inventory** in **Admin → Modules**
2. Add suppliers under **Inventory → Suppliers**
3. Add items under **Inventory → Items** with SKU, location, and reorder point

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/inventory_management_module)

</details>

---

<details>
<summary><strong>📊 Quality Measures (HEDIS/MIPS)</strong> — Hit your HEDIS and MIPS targets — care gaps caught at the point of encounter</summary>

<br>

![Quality Measures Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/35_hedis_dashboard.png)

Automated HEDIS and MIPS quality measure tracking with real-time dashboards, point-of-care alerts, and CMS-ready attestation reports with historical trending.

**Key features:**
- **Automated Tracking** — Real-time dashboards with care gap identification
- **Point-of-Care Alerts** — Notify providers when a quality measure opportunity exists during an encounter
- **CMS Reports** — Ready-to-submit reports with attestation support and historical trending
- **Payer-Specific Measures** — Configure measure sets per payer contract and reporting period
- **Staff Scorecards** — Individual provider performance vs. panel average
- **Care Gap Lists** — Exportable lists of patients needing interventions per measure

**Quick setup:**
1. Enable **Quality Measures** in **Admin → Modules**
2. Configure measure set under **Settings → Quality → Measure Set**
3. Dashboard auto-populates from existing clinical data; review gaps at **Quality → Dashboard**

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/quality_measures_module_hedismips)

</details>

---

<details>
<summary><strong>⚙️ Platform Administration & White Label</strong> — Run 10 locations like one — push config to every branch in a single click</summary>

<br>

![Platform Admin](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/20_platform_admin.png)

Command and control for practice owners and enterprise administrators — manage multiple branches, customize brand identity, and push configuration to all locations from one dashboard.

**Key features:**
- **Multi-Branch Management** — Separate workspaces per location with HQ-level oversight
- **White Label** — Custom logo, colors, and domain per branch; patients see your brand
- **Global Config Push** — Deploy forms, KPI templates, and GL chart of accounts from HQ to all branches
- **Granular Permissions** — Role-based access with per-module, per-action assignment
- **Branch Isolation** — Data and user access strictly isolated between branches
- **Audit Dashboard** — Cross-branch compliance and activity reporting in one view

**Quick setup:**
1. Platform Administration is available on **Enterprise plan** — contact [sales@synalux.ai](mailto:sales@synalux.ai)
2. Create branches under **Admin → Branches → New Branch**
3. Configure branding per branch under **Admin → Branches → [Branch] → White Label**

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/platform_administration_white_label)

</details>

---

### 🔒 Security & Compliance

<details>
<summary><strong>🛡️ Security, Privacy & HIPAA Compliance</strong> — HIPAA-ready out of the box — local AI means patient data never reaches a cloud vendor</summary>

<br>

![Security Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/38_compliance_audit.png)

Security-first architecture — every PHI access immutably logged with a tamper-evident hash chain. Local AI models eliminate the single largest HIPAA compliance gap in AI-powered clinical tools.

**Key features:**
- **Immutable Audit Log** — Every PHI access logged with tamper-evident hash chain; exported on demand
- **AES-256-GCM Encryption** — OAuth tokens, session keys, and stored PHI encrypted at rest
- **Local AI = Zero PHI Exposure** — Clinical AI inference runs on-device; patient data never sent to cloud vendors
- **MFA** — TOTP authenticator app, passkeys, and SMS second factor
- **Break-Glass Override** — Emergency access with immediate audit notification to compliance officer
- **HIPAA BAA** — Available on Standard and above; Business Associate Agreement countersigned on request

| Risk | Cloud AI | Synalux local-first |
|------|----------|-------------------|
| Patient data in LLM prompts | ✅ Sent to vendor | **❌ Never leaves clinic** |
| HIPAA BAA required | Yes (every model vendor) | **Not needed for on-prem** |
| Inference cost | $2–15/clinician/day | **$0 (local GPU/Mac)** |

**Quick setup:**
1. Enable MFA under **Admin → Security → Multi-Factor Authentication** — enforce for all staff
2. Review the audit log under **Admin → Security → Audit Trail**
3. Download the HIPAA compliance report under **Admin → Security → Compliance → HIPAA Report**

▶️ [Watch setup video](https://youtu.be/VToBmciKlwU) · [📖 Full documentation](https://synalux.ai/docs/security_compliance)

</details>

---

### 💬 Communication

<details>
<summary><strong>💬 Team Chat & Clinical Communication</strong> — Coordinate care without leaving the EHR — HIPAA chat, video huddles, and Slack all in one place</summary>

<br>

![Team Chat Module](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/10_team_chat.png)

A high-security collaboration hub — coordinate care in real-time, run HD video team meetings, and read all external channels (Slack, WhatsApp, Telegram, SMS) without leaving Synalux.

**Key features:**
- **HIPAA-Compliant Channels** — Direct and group messaging; all messages encrypted and audit-logged
- **HD Video Scrums** — Built-in video conferencing for team huddles and case conferences
- **Clinical Asset Sharing** — Share patient records and documents with granular access controls
- **@Mentions & Notifications** — Tag colleagues; delivery via in-app, SMS, and email
- **Unified Inbox** — Slack, Discord, Teams, WhatsApp, Telegram all readable from one inbox
- **Message Search** — Full-text search across all channels with permission-gated results

**Quick setup:**
1. Enable **Team Chat** in **Admin → Modules**
2. Create channels under **Chat → New Channel** — organize by team, specialty, or patient case
3. Invite staff; they receive a notification to join

📹 Setup video — coming soon · [📖 Full documentation](https://synalux.ai/docs/team_chat_communication)

</details>

---

## Plans

| | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| AI assistant | ✅ Gemini 2.5 Flash | ✅ Claude Sonnet 4 | ✅ Claude Sonnet 4 | ✅ Claude Sonnet 4 |
| Mail / Calendar / Drive | ✅ | ✅ | ✅ | ✅ |
| Telehealth | — | ✅ | ✅ + Zoom | ✅ + Zoom |
| Voice (Inworld TTS-2) | ✅ default voice | ✅ all voices | ✅ + clinical dictation | ✅ + voice cloning |
| BoldSign e-Signature | — | — | ✅ 7 templates | ✅ unlimited |
| Banking & GL | — | — | ✅ | ✅ |
| Multi-workspace HQ | — | — | — | ✅ |

Tier-aware fallback: Standard → Gemini 2.5 Flash · Advanced/Enterprise → Gemini 2.5 Pro.

[See full pricing →](https://synalux.ai/pricing)

---

## Self-hosted AI (Enterprise)

Run Prism models on your own hardware — zero cloud cost, full data sovereignty.

```bash
ollama pull dcostenco/prism-coder:1b7   # 1.1 GB  · ~1.6s · any device
ollama pull dcostenco/prism-coder:8b    # 4.7 GB  · ~0.8s · iPhone/iPad 8GB
ollama pull dcostenco/prism-coder:14b   # 8.4 GB  · ~1.1s · Mac M2+ / iPad Pro 16GB
ollama pull dcostenco/prism-coder:32b   # 16 GB   · ~0.8s · Mac M2 Ultra+
```

Set `LOCAL_LLM_URL=http://localhost:11434` in portal config.

| Model | Accuracy | Latency | Tier |
|---|---|---|---|
| **14B→32B cascade** | **100.0%** | ~1.1s | Desktop primary |
| **prism-coder:8b** v36 | **100.0%** | 0.8s | Mobile tier 2 |
| **prism-coder:1b7** v42 | **100.0%** | 1.6s | On-device tier 3 |
| Sonnet 4 (cloud) | 99% | 3.2s | Cloud fallback |

[Cascade eval →](https://github.com/dcostenco/prism-coder/tree/main/tests/benchmarks/cascade-14b-32b-opus) · [Ollama install](https://ollama.com/install)

---

## Status

- **Production**: synalux.ai (latest: v14.0.0)
- **v14 highlights**: 23 Coming Soon features implemented; military-grade security audit — 0 CRITICAL findings across 18 new API routes

---

## License
BUSL-1.1 — see [LICENSE](https://github.com/dcostenco/synalux-docs/blob/main/LICENSE).
