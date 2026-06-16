# Applied Behavior Analysis (ABA) — Complete Clinical Platform

Synalux's ABA module is a full-lifecycle clinical platform for **BCBAs**, **BCaBAs**, **RBTs**, and **clinical supervisors**. Every workflow — from initial assessment to insurance billing — is integrated into a single HIPAA-compliant system with offline-first resilience.

> **Who it's for:** ABA therapy practices serving children and adults with autism spectrum disorder, developmental disabilities, and behavioral health needs.

---

## Key Capabilities

| Category | Features |
|----------|----------|
| **Data Collection** | Discrete trials, duration recording, frequency counter, interval recording, task analysis, ABC (antecedent-behavior-consequence) |
| **Assessments** | VB-MAPP, ABLLS-R, AFLS, Essentials for Living, PEAK, custom instruments — with CSV item import for licensed content |
| **Goals Library** | Evidence-based goal bank with 11 ABA domains, template creation, search/filter, assign-to-patient flow |
| **Treatment Planning** | Guided FBA→BIP wizard, mastery predictions, AI-assisted goal suggestions |
| **Graphing** | Auto-generated line charts with mastery thresholds, baseline phase detection, AI trend narratives |
| **Clinical Notes** | SOAP notes with voice dictation (on-device WASM Whisper), co-signature workflow |
| **Staff Management** | Credential tracking (BCBA/RBT/BCaBA), supervision logs, expiry alerts |
| **Insurance** | CPT code integration (97151-97158), authorization tracking, utilization monitoring |
| **Offline Mode** | Full data collection without internet; auto-sync when connectivity returns |

---

## Live Data Collection

Record session data in real-time on any device — desktop, iPad, or phone. The interface is optimized for rapid data entry during therapy sessions.

### Discrete Trial Training (DTT)

Large touch targets (+/-) for recording correct and incorrect responses. Each trial captures:
- **Response** (correct/incorrect/no response)
- **Prompt level** (Independent, Gestural, Verbal, Partial Physical, Full Physical)
- **Target** being addressed
- **Timestamp** for rate calculations

### Duration Recording

Built-in stopwatch for timing behaviors:
- Start/stop with single tap
- Automatic duration calculation
- Running total per session
- Ideal for measuring on-task behavior, tantrums, or stereotypy duration

### Frequency Counter

Count occurrences of target behaviors during observation windows:
- Real-time counter with large increment/decrement buttons
- Rate calculation (count per minute/hour)
- Session-level aggregation

### Task Analysis

Step-by-step recording for complex skill chains:
- Define steps in the chain
- Record independence level per step
- Track which steps need additional prompting
- Forward and backward chaining support

### Interval Recording

Record whether a behavior occurred during each observation interval:
- ✓ Occurred / ✗ Absent buttons for each interval
- Running percentage calculation (intervals with behavior / total intervals)
- Suitable for partial-interval recording procedures

### ABC Data Collection

Record the three-term contingency for functional analysis:
- **Antecedent** — what happened before the behavior
- **Behavior** — the observable behavior
- **Consequence** — what happened after
- Structured dropdowns with common options + free text
- Direct link to FBA hypothesis development

---

## Electronic Visit Verification (EVV)

HIPAA-compliant session verification required by many Medicaid programs:

- **GPS location capture** at session start and end
- **Parent/caregiver signature** via touch-screen signature pad
- **PIN verification** for identity confirmation
- **Session timestamps** with client-side and server-side clocks
- **Device information** logged for audit trail

---

## Assessment Suite

### Supported Instruments

| Instrument | Scoring | Domains |
|-----------|---------|---------|
| **VB-MAPP** (Verbal Behavior Milestones Assessment) | 0, 0.5, 1 | Mand, Tact, Listener Responding, Visual Perceptual Skills, Play, Social, Echoic, Spontaneous Vocal, Intraverbal, Group & Classroom, Linguistics, Reading, Writing, Math |
| **ABLLS-R** (Assessment of Basic Language and Learning Skills) | 0-4 | Basic Learner Skills, Academic Skills, Self-Help Skills, Motor Skills |
| **AFLS** (Assessment of Functional Living Skills) | 0-2 | Basic Living Skills, Home Skills, Community Participation, School Skills, Vocational Skills |
| **Essentials for Living** | 0-1 | 8 domains covering essential functional skills |
| **PEAK** (Promoting Emergence of Advanced Knowledge) | 0-2 | Direct Training, Generalization, Equivalence, Transformation |
| **Custom** | 0-3 | User-defined domains and milestones |

### Assessment Features

- **Real instrument items** — import actual milestone descriptions from your licensed copy via CSV upload (format: `domain,code,label,description`)
- **Domain-based scoring grid** — per-item scores with descriptions, tooltips, and color-coded progress
- **Historical tracking** — compare scores across assessment periods; record completed assessments retroactively
- **Multiple assessment sessions** per patient per instrument
- **Barrier analysis & recommendations** — structured clinical notes per assessment
- **AI-assisted interpretation** — trend analysis across assessment periods
- **Legacy fallback** — auto-generated item labels for templates without imported items

### Adaptive Assessment Log

A score repository for externally-administered standardized assessments:
- **Instrument-agnostic** — stores scores from Vineland-3, ABAS-3, Bayley-4, BASC-3, ADOS-2, and any future instrument
- **Not an instrument** — Synalux does not administer, score, or reproduce any standardized assessment
- **AI integration** — BCBA assistant pulls scores verbatim for medical-necessity letters and BIP drafts
- **Audit trail** — PHI-tier triple-logging on every CRUD operation

---

## Goals Library

A reusable, searchable goal bank for building evidence-based treatment plans.

### Goal Templates

Create and maintain a workspace-wide library of clinical goals:
- **11 ABA domains** — Behavior Reduction, Skill Acquisition, Communication, Social Skills, Daily Living, Academic, Motor, Play & Leisure, Self-Management, Safety, Other
- **Structured definitions** — title, operational description, baseline criteria, mastery criteria, measurement method
- **Goal types** — Short-Term, Long-Term, Maintenance
- **8 measurement methods** — Percent Correct, Frequency Count, Duration, Rate, Latency, Interval Recording, Task Analysis, Discrete Trial
- **Search and filter** — find goals by domain, keyword, or type

### Assign to Patient

Clone a template goal into an active patient goal:
1. Select a goal template from the library
2. Choose the patient
3. Optionally link to a treatment plan
4. Goal is created as `active` with the template's criteria pre-populated

### Active Goals View

Track all patient-assigned goals across the practice:
- Patient name, domain, current progress, status
- Filter by domain or search by goal title
- Status tracking: Active → In Progress → Met → Maintenance → Discontinued

---

## FBA → BIP Builder

A guided 3-step wizard for creating Functional Behavior Assessments and Behavior Intervention Plans.

### Step 1: FBA (Functional Behavior Assessment)

- **Target behavior definitions** — operational definition, examples, non-examples, baseline frequency, severity
- **A-B-C observations** — structured Antecedent-Behavior-Consequence data entry with setting and time
- **Assessment summary** — current functioning level, relevant diagnoses, prior interventions
- **Behavioral history** — onset, previous BIPs, treatment response

### Step 2: BIP (Behavior Intervention Plan)

For each target behavior:
- **Hypothesized function** — Attention, Escape/Avoidance, Access to Tangible, Automatic/Sensory
- **Antecedent / prevention strategies** — environmental modifications, visual schedules, pre-teaching, choice-making
- **Replacement behavior (FCT)** — select from the Goals Library or enter custom replacement
- **Teaching procedure** — DTT, NET, prompting hierarchy, reinforcement schedule
- **Consequence strategies** — DRA, DRO, NCR, extinction (if safe)
- **Crisis / safety protocol** — de-escalation steps, supervisor contact, emergency procedures

Plus:
- **Caregiver involvement** — parent training goals, home program, communication protocol
- **Global crisis plan** — emergency contacts, de-escalation protocol
- **Review date** scheduling

### Step 3: Review & Save

- Full BIP summary with all sections displayed
- **BCBA disclaimer** — "Clinical support draft; must be reviewed and individualized by a credentialed BCBA before implementation per local policy and applicable laws."
- Saves as `treatment_plans` with `plan_type = 'bip'` and `status = 'draft'`
- Draft BIPs appear in the patient's Treatment Plans tab with "(Draft)" label

---

## Curriculum & Target Bank

Manage your entire ABA curriculum in a hierarchical tree view:

```
Program
  └── Domain
       └── Target
            ├── Mastery Threshold (default 80%)
            ├── Current Performance
            ├── Prompt Level History
            └── AI Mastery Prediction
```

### Features

- **Program → Domain → Target** hierarchy
- **Real-time progress bars** showing completion toward mastery
- **Mastery tracking** — flags targets meeting criteria (e.g., 80% across 3 consecutive sessions)
- **AI-powered mastery predictions** — projects sessions-to-mastery based on clinical velocity
- **Smart goal suggestions** — recommends next targets based on assessment data and curriculum sequence
- **Behavioral pattern analysis** — identifies stagnation and suggests intervention modifications

---

## Graphing & Data Visualization

Auto-generated graphs from collected session data:

### Graph Types
- **Line charts** — data points with session dates on x-axis, percentage/frequency on y-axis
- **Mastery reference lines** — horizontal line at mastery threshold (configurable per target)
- **Baseline phase detection** — automatically identifies baseline vs. intervention data points

### AI Trend Analysis

Each graph includes a natural-language narrative:
- **Trend direction** — accelerating, decelerating, or stable
- **Performance summary** — current level relative to mastery
- **Mastery recommendation** — suggests when to probe for mastery or modify intervention

---

## Clinical Notes (SOAP)

### Voice Dictation

Focus on the patient while Synalux captures your clinical observations:
- **WASM Whisper engine** — on-device speech recognition (no audio leaves the device)
- **Real-time transcription** — see your words appear as you speak
- **HIPAA-compliant** — processing happens locally, not in the cloud

### AI-Assisted Note Generation

- **Smart drafting** — generates SOAP format from session observations
- **Template selection** — therapy session, progress note, supervision note
- **Clinical vocabulary** — trained on ABA terminology

### Note Workflow

```
Draft → Submitted → Co-Signed → Finalized
```

- **Co-signature support** — supervising BCBA can review and co-sign RBT notes
- **CRDT persistence** — real-time collaboration without data loss
- **Audit trail** — every edit tracked with timestamp and author

---

## Staff & Supervision Management

### Credential Tracking

Monitor certification status for your entire clinical team:

| Credential | Tracked Fields |
|-----------|---------------|
| BCBA | Certification #, expiry, CEU status |
| BCBA-D | Doctoral-level board certification |
| BCaBA | Assistant analyst certification |
| RBT | Technician certification, renewal date |
| LABA | Licensed Applied Behavior Analyst (state-specific) |
| QBA | Qualified Behavior Analyst |

- **Expiry alerts** — automated notifications before credential expiration
- **Training tracker** — log completed CEUs and training hours
- **State license integration** — tracks state-specific licensing requirements

### Supervision Logging

Record supervision sessions per BACB requirements:
- **Supervision types**: Direct, Indirect, Group, Individual, Competency Assessment
- **Duration tracking** — minutes per session
- **Topics covered** — free text + structured topic categories
- **BCBA ↔ RBT pairing** — track who supervises whom

---

## Insurance & Authorization Management

### CPT Code Integration

Direct support for ABA-specific billing codes:

| Code | Description |
|------|-------------|
| 97151 | Behavior identification assessment |
| 97152 | Behavior identification supporting assessment |
| 97153 | Adaptive behavior treatment by protocol |
| 97154 | Group adaptive behavior treatment |
| 97155 | Adaptive behavior treatment with protocol modification |
| 97156 | Family adaptive behavior treatment guidance |
| 97157 | Multiple-family group adaptive behavior treatment |
| 97158 | Group adaptive behavior treatment by protocol modification |

Plus telehealth variants (modifier 95) for all codes.

### Authorization Tracking

- **Units vs. hours toggle** — track authorized amounts in either format
- **Utilization monitoring** — real-time view of used vs. remaining authorizations
- **Expiration alerts** — notifications before authorization periods end
- **CSV export** — for insurance submission and internal reporting

---

## AI Clinical Copilot

An AI assistant trained on ABA clinical workflows:

- **Treatment plan assistance** — suggests evidence-based interventions based on assessment data
- **Note drafting** — generates clinical language from session observations
- **Clinical questions** — answers questions about ABA methodology, BACB ethics, and best practices
- **Privacy-first** — runs on local Ollama instance with DLP redaction; patient data processed with HIPAA safeguards

---

## Connectivity & Data Safety

Synalux requires an internet connection for clinical data capture. When offline:

- **Visible status** — a red "Offline — saves disabled" badge appears immediately
- **Data preserved in-session** — entered trials and notes remain in the active form until you reconnect and save
- **Session save protection** — if an end-of-session save fails, the app shows a retry dialog and preserves all session state (no silent data loss)
- **No client-side PHI storage** — clinical data is never written to browser storage (localStorage or IndexedDB)
- **PHI purge on boot** — any legacy device data from prior versions is automatically cleared on app load
- **SOAP notes** — voice dictation works offline (WASM Whisper runs on-device); generated notes save when reconnected

---

## Multi-Locale Support

ABA services are delivered worldwide. Synalux adapts to your region:

| Region | Insurance | Credentials | Diagnosis Codes |
|--------|-----------|-------------|-----------------|
| **United States** | US commercial + Medicaid | BACB (BCBA, RBT) | ICD-10-CM |
| **Canada** | Provincial (Ontario, BC, Alberta) | BACB + provincial | ICD-10-CA |
| **United Kingdom** | NHS + private | HCPC, DBS | ICD-10 |
| **European Union** | National systems (DE, FR, NL) | Country-specific | ICD-10 |

---

## Security & Compliance

- **HIPAA audit trails** — every data access, edit, and deletion logged with user identity
- **Workspace isolation** — multi-tenant architecture prevents cross-practice data leakage
- **Role-based access** — BCBAs see all patients; RBTs see only assigned patients
- **E-signatures** — secure consent via integrated signature workflow
- **Encryption at rest** — all clinical data encrypted via platform-level safeStorage
- **SOC 2 controls** — rate limiting, SSRF protection, input validation on all clinical endpoints

---

## Getting Started

1. **Create a workspace** at [synalux.ai](https://synalux.ai)
2. **Add your team** — invite BCBAs, RBTs, and administrative staff
3. **Set up patients** — enter demographics, insurance, and diagnosis codes
4. **Create curriculum** — build your program tree with targets and mastery criteria
5. **Start collecting data** — use any device for real-time session data entry
6. **Review and graph** — analyze progress with auto-generated charts
7. **Generate notes** — use voice dictation for zero-paperwork documentation
8. **Bill insurance** — track authorizations and submit claims with CPT codes

---

## Roadmap

Recently shipped:

- [x] FBA/BIP structured builder workflow (3-step wizard)
- [x] Goals template library (browse, search, assign from evidence-based bank)
- [x] Real assessment instrument support (CSV item import)
- [x] Interval recording UI (occurred/absent with running percentage)
- [x] Task analysis recording in post-hoc data collection

In active development:

- [ ] Phase change lines and celeration/aim lines on graphs
- [ ] Insurance-ready progress report generator with embedded graphs
- [ ] Parent/caregiver portal for progress viewing
- [ ] Encrypted offline data collection with auto-sync
- [ ] BACB fieldwork hours tracking (restricted/unrestricted split)
- [ ] Supervision contract management

---

*For questions or feature requests, contact [support@synalux.ai](mailto:support@synalux.ai) or visit [synalux.ai/docs](https://synalux.ai/docs).*
