# ✦ Synalux

**Your AI-Powered Practice Management Platform**

> Run your entire healthcare practice from one platform — patient records, scheduling, billing, team communication, and AI-assisted documentation. Works for ABA therapy, pediatrics, mental health, dentistry, physical therapy, and dermatology. Available in 12 languages. HIPAA-compliant.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Try_It_Free-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Developer_Tools-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language / Язык / Limba:** [English](#-why-synalux) · [Español](docs/i18n/README_es.md) · [Français](docs/i18n/README_fr.md) · [Português](docs/i18n/README_pt.md) · [Română](docs/i18n/README_ro.md) · [Українська](docs/i18n/README_uk.md) · [Русский](docs/i18n/README_ru.md) · [Deutsch](docs/i18n/README_de.md) · [日本語](docs/i18n/README_ja.md) · [한국어](docs/i18n/README_ko.md) · [中文](docs/i18n/README_zh.md) · [العربية](docs/i18n/README_ar.md)

🎬 **Demo videos coming soon** — See the full workflow: patients, scheduling, notes, billing, and team chat in action.

---

## 💡 Why Synalux?

### For Clinicians
* **🎙️ Talk, don't type.** Dictate your session notes, and Synalux turns them into structured SOAP notes instantly — all processed on your device, never sent to the cloud.
* **📴 Works offline.** Start and end sessions even without internet. Your notes are saved locally and sync automatically when you're back online. Your sign-off time is always accurate for billing — even if you're in a dead zone.
* **🛡️ AI you can trust.** Every AI suggestion shows you a before/after comparison. Nothing changes in the patient record until you explicitly approve it.
* **📝 Less paperwork.** Generate FBAs, BIPs, progress reports, and discharge summaries from your session data — then send for e-signature in one click.

### For Practice Owners & Administrators
* **🏥 One platform for any specialty.** The entire system adapts to your practice type — ABA, pediatrics, mental health, dental, PT, or dermatology. Same platform, different clinical language.
* **🌍 International-ready billing.** Accept payments in USD, CAD, GBP, EUR, AUD, and NZD. Volume discounts kick in automatically at 100, 500, and 1,000+ clients. Annual billing saves 20%.
* **💳 Never lose revenue.** Failed payments are automatically retried. You see warning banners before anyone loses access. Platform admins can override any account to unlimited trial.
* **👥 Control who sees what.** 15 roles — from doctors to billing specialists to HR — each with specific permissions. Assign roles per country and per specialty.

### For IT & Compliance
* **📴 Offline-safe sessions.** Timestamps are captured on the clinician's device. When they sign off a session at 3:45 PM in a dead zone, the billing time is 3:45 PM — not when the server got it at 4:00 PM. Admins see 🟢 Online / 🔴 Offline status for every session event.
* **🔐 HIPAA built-in.** 15-minute idle timeout, no patient data in browser storage, encrypted at rest, audit logs for every action. Session drafts are automatically purged on logout.
* **📊 201 tests passing.** Pricing engine, payment flow, offline sessions, billing, database tools, and compliance scenarios — all covered by automated tests.

<details>
<summary><strong>🔧 Under the Hood (Technical Details)</strong></summary>

* **Stateless RLS:** Multi-tenant data isolation uses signed JWTs mapped to Postgres Row-Level Security — no session variables, no connection pools per tenant.
* **Persistent Memory:** Built on [Prism MCP](https://github.com/dcostenco/prism-mcp), the AI remembers context across sessions and reloads, isolated by workspace.
* **Fine-Tuned Local LLM:** An embedded offline Copilot powered by `prism-coder:7b` acts as the routing engine, trained via SFT and GRPO to natively execute MCP tools without ever exposing patient context to cloud providers.
  * *Latest MLX Benchmark Results (M4 Max):* 100% JSON schema validation accuracy against MCP specs with 33.3% initial tool logic precision, firing natively at **45.1 Tokens/second**.
* **Prompt-Level RBAC:** Tool ACLs are cryptographically signed. If a technician asks the AI to run a command they're not authorized for, the tool is stripped before the LLM sees it.
* **Payment Webhook Lifecycle:** `invoice.payment_failed` → flag as `past_due` → auto-downgrade after 3 retries → webhook guards protect platform-admin overrides from ever being reverted.
* **Offline Sync Engine:** Client-side `SessionEvent` objects with `connection_status` field, queued in localStorage, synced idempotently via UUID on reconnect.

</details>

---

## 🏥 Supported Practice Types

Synalux is a **multi-practice enterprise platform** supporting 6 medical specialties out of the box. Each practice type includes specialty-specific clinical templates, billing codes, fee schedules, and workflows.

<details>
<summary><h3>🧩 Applied Behavior Analysis (ABA)</h3></summary>

🔗 **[Read Detailed Applied Behavior Analysis (ABA) Documentation](docs_source_en/applied_behavior_analysis_aba.md)**



| Feature | Details |
|---------|---------|
| **Clinical Templates** | FBA, BIP, ABC Data Collection, Session Notes, Progress Reports, Discharge Summary |
| **Billing Codes** | 97151 (Assessment), 97153 (Protocol), 97155 (Modification), 97156 (Family Guidance), 97157 (Group) |
| **RBAC Roles** | BCBA (Full clinical), RBT (Session notes only), Office Manager |
| **Voice Dictation** | Ambient session recording → auto-structured SOAP notes |
| **E-Signatures** | BoldSign integration for parent/guardian consent |
| **Data Tracking** | Behavioral targets, skill acquisition, frequency/duration data |
| **Insurance** | Autism/ABA-specific payer rules, prior auth tracking |
| **🧠 AI Mastery Predictions** | Trend-based prediction of target mastery timelines per skill |
| **💡 AI Goal Suggestions** | Auto-recommend next targets based on mastered skills |
| **📄 AI Progress Reports** | One-click generation of insurance-ready progress reports |
| **🔍 Treatment Integrity** | Real-time DTT/NET fidelity monitoring with adherence scoring |
| **🌳 Program Tree View** | Hierarchical Program → Goal → Target tree with progress bars |

</details>

<details>
<summary><h3>👶 Pediatrics</h3></summary>

🔗 **[Read Detailed Pediatrics Documentation](docs_source_en/pediatrics.md)**



| Feature | Details |
|---------|---------|
| **Clinical Templates** | Well-child exams, sick visits, immunization tracking, developmental screening |
| **Billing Codes** | 99392–99395 (Preventive), 99213–99215 (Office visits), 90460 (Immunization) |
| **Patient Portal** | Parent/guardian access, growth charts, immunization records, appointment booking |
| **Asthma Management** | Action plans, peak flow tracking, rescue inhaler logs |
| **ADHD Workflow** | Vanderbilt scoring, medication management, school accommodation letters |
| **Insurance** | BCBS, UHC, Medicaid — auto-eligibility verification |

</details>

<details>
<summary><h3>🦷 Dental & Orthodontics</h3></summary>

🔗 **[Read Detailed Dental & Orthodontics Documentation](docs_source_en/dental_orthodontics.md)**



| Feature | Details |
|---------|---------|
| **Clinical Templates** | Comprehensive exam, perio charting, treatment planning, operative notes |
| **Billing Codes (CDT)** | D0150 (Exam), D0210 (FMX), D2740 (Crown), D3330 (RCT), D6010 (Implant), D8080 (Ortho) |
| **Treatment Sequencing** | Multi-phase treatment plans (Root canal → Crown → Follow-up) |
| **Ortho Management** | Monthly adjustments, payment plans ($194/mo × 18 months), progress tracking |
| **Implant Workflow** | Surgical planning, guided surgery, healing abutment, prosthesis phases |
| **Perio Charting** | SRP quadrant tracking, pocket depths, bone loss classification |
| **Payment Plans** | Stripe-powered installment plans with autopay for high-value procedures |
| **Insurance** | Delta Dental, MetLife, Cigna — annual max tracking, pre-determination |

</details>

<details>
<summary><h3>🧠 Mental Health & Psychiatry</h3></summary>

🔗 **[Read Detailed Mental Health & Psychiatry Documentation](docs_source_en/mental_health_psychiatry.md)**



| Feature | Details |
|---------|---------|
| **Clinical Templates** | Psychiatric eval, psychotherapy notes, CBT/CPT protocols, safety plans |
| **Billing Codes** | 90791 (Psych eval), 90834/90837 (Therapy 45/60min), 99214 (Med management) |
| **Outcome Measures** | PHQ-9, GAD-7, PTSD-5, BDI-II — auto-scored with trend tracking |
| **Medication Tracking** | Prescriptions, dose changes, side effects, drug interactions |
| **Trauma Therapy (CPT)** | 12-session protocol, stuck point logs, impact statement drafts |
| **Crisis Protocol** | Urgent message flags, safety plan templates, crisis hotline integration |
| **Telehealth** | Zoom integration, consent tracking, session recording (with consent) |
| **Insurance** | Anthem BCBS, Aetna, Cigna Behavioral — auth tracking for session limits |

</details>

<details>
<summary><h3>🏃 Physical Therapy & Sports Medicine</h3></summary>

🔗 **[Read Detailed Physical Therapy & Sports Medicine Documentation](docs_source_en/physical_therapy_sports_medicine.md)**



| Feature | Details |
|---------|---------|
| **Clinical Templates** | PT evaluation, ROM/strength assessment, functional outcome measures |
| **Billing Codes** | 97162 (PT eval), 97110 (Exercise), 97116 (Gait), 97140 (Manual), 97530 (Functional) |
| **Rehab Protocols** | ACL reconstruction, rotator cuff, chronic pain, neuro rehab — phased progression |
| **Outcome Tracking** | ROM degrees, manual muscle testing (MMT), LEFS/DASH scores |
| **Home Exercise Programs** | Auto-generated HEP with images, frequency, sets/reps |
| **Work Comp / Sports** | Return-to-play protocols, FCE documentation, work restrictions |
| **Insurance** | Medicare (therapy caps), workers' comp, auto-accident PIP — auth tracking |

</details>

<details>
<summary><h3>🔬 Dermatology</h3></summary>

🔗 **[Read Detailed Dermatology Documentation](docs_source_en/dermatology.md)**



| Feature | Details |
|---------|---------|
| **Clinical Templates** | Skin exam, biopsy reports, pathology tracking, phototherapy logs |
| **Billing Codes** | 99214 (Office visit), 11102 (Biopsy), 17000 (Cryotherapy), 96401 (Chemo SC/IM) |
| **Melanoma Screening** | Full-body mapping, dermoscopy documentation, ABCDE criteria |
| **Accutane (iPLEDGE)** | Monthly labs (CBC, LFT, lipid), pregnancy testing, iPLEDGE compliance tracking |
| **Biologics Management** | Humira/Dupixent dosing, prior auth, injection scheduling, phototherapy logs |
| **Photo Documentation** | Lesion before/after tracking, body map annotations |
| **Lab Integration** | Quest/LabCorp order routing, result auto-import |
| **Insurance** | Prior auth for biologics, step therapy documentation, appeal templates |

</details>

<details>
<summary><h3>🐾 Veterinary Medicine</h3></summary>

🔗 **[Read Detailed Veterinary Medicine Documentation](docs_source_en/veterinary_medicine.md)**

| Feature | Details |
|---------|---------|
| **Clinical Records** | Animal health records with breed, species, weight tracking, vaccination history |
| **RBAC Roles** | Veterinarian (full clinical), Vet Technician (intake, vitals, treatment) |
| **Exams & Surgical Notes** | Species-specific exam templates, surgical reports, post-op care plans |
| **Prescriptions** | Species-appropriate dosing, compounding pharmacy, controlled substance tracking |
| **Vaccination Schedules** | Core/non-core vaccine protocols, automated wellness reminders |
| **Diagnostic Imaging** | DICOM-compatible radiograph & ultrasound review with annotations |
| **Billing** | Wellness plans, procedure bundles, pet insurance claim submission |

</details>

---

## 📦 Platform Modules

Every module is multi-tenant, workspace-scoped, and HIPAA-compliant with strict row-level security.

<details>
<summary><h3>💳 Billing & Payments Module</h3></summary>

🔗 **[Read Detailed Billing & Payments Module Documentation](docs_source_en/billing_payments_module.md)**



The billing module uses **Stripe Connect** to give each practice its own independent payment processing account linked to the practice administrator.

**Per-Practice Billing Configuration:**
| Setting | Details |
|---------|---------|
| **Stripe Connect** | Each workspace has its own `acct_xxx` Stripe Connect account |
| **Admin Linked** | Stripe account ownership is linked to the workspace admin user |
| **Fee Schedules** | Per-practice fee schedules with standard, insurance, Medicare, and self-pay rates |
| **Payment Methods** | Credit card, ACH/bank transfer, check, cash — configurable per practice |
| **Auto-Posting** | Automatic payment posting, receipt sending, and monthly statement generation |
| **Tax Configuration** | Per-practice tax rates and NPI/EIN for 1099 reporting |

**Multi-Country & Multi-Currency (NEW):**

| Country | Currency | Standard | Advanced | Enterprise |
|---------|----------|----------|----------|------------|
| 🇺🇸 USA | USD | $19/mo | $49/mo | $99/mo |
| 🇨🇦 Canada | CAD | C$25/mo | C$65/mo | C$129/mo |
| 🇬🇧 UK | GBP | £15/mo | £39/mo | £79/mo |
| 🇩🇪🇫🇷 EU | EUR | €18/mo | €45/mo | €89/mo |
| 🇦🇺 Australia | AUD | A$29/mo | A$75/mo | A$149/mo |
| 🇳🇿 New Zealand | NZD | NZ$32/mo | NZ$82/mo | NZ$159/mo |

**Volume Discounts:**
| Clients | Discount |
|---------|----------|
| 100+ | 10% off per-seat price |
| 500+ | 20% off per-seat price |
| 1,000+ | 30% off per-seat price |
| Annual billing | Additional 20% off (stacks with volume, capped at 45%) |

**Payment Failure Lifecycle:**
```
Payment Failed → past_due (warning banner, keep access)
  → 2nd retry → still past_due (urgent warning)
  → 3rd retry failed → auto-downgrade to Free tier
  → Stripe subscription.deleted → plan = 'free', sub cleared
```

**Platform Admin Overrides:**
- Synalux platform admins can set any user to unlimited trial on any plan
- Override users are **immune** to Stripe webhook downgrades
- Admin sees 🟢/🔴 indicators for payment status
- Full audit trail: who set the override, when, and why

**Revenue Cycle Management:**
- Insurance claim lifecycle tracking (draft → submitted → accepted → paid/denied → appeal)
- ERA/EOB electronic remittance processing
- Denial management with appeal deadline tracking
- Prior authorization workflow
- Aging reports (30/60/90/120 day buckets)

**Patient Payments:**
- Patient portal "Pay Now" → Stripe Checkout redirect
- Partial payments and custom amounts
- Payment plans with Stripe recurring subscriptions
- Receipt generation and download
- Refund processing

**Insurance Claims:**
- Electronic claim submission (837P)
- Real-time eligibility verification
- Coordination of Benefits (COB)
- Explanation of Benefits (EOB) tracking
- Appeal management with letter templates

**Automatic Tax Collection:**
- Stripe Tax enabled per-country (VAT, GST, HST, PST)
- Tax calculated automatically based on workspace country
- Compliant with Canadian multi-province tax rules (federal GST + provincial PST/HST)

</details>

<details>
<summary><h3>🏥 Patient Portal</h3></summary>

🔗 **[Read Detailed Patient Portal Documentation](docs_source_en/patient_portal.md)**



A full-featured patient-facing portal with authentication, messaging, documents, appointments, and billing.

| Feature | Details |
|---------|---------|
| **Authentication** | Access code login (SHA-256 hashed), expiration tracking |
| **Dashboard** | Health overview with upcoming appointments, unread messages, pending documents, balance due |
| **Messaging** | Threaded conversations with providers, urgent flags, read receipts |
| **Documents** | View/download clinical documents, upload insurance cards and forms |
| **Appointments** | View upcoming/past visits, request new appointments with preferred times |
| **Billing** | View balance, billing history with CPT codes, pay online via Stripe, payment plans, receipts |
| **Forms** | Complete intake forms, PHQ-9/GAD-7 questionnaires, consent forms online |
| **Consents** | Digital consent management (treatment, HIPAA, telehealth, medication, research) |

</details>

<details>
<summary><h3>👥 HR & Staff Management Module</h3></summary>

🔗 **[Read Detailed HR & Staff Management Module Documentation](docs_source_en/hr_staff_management_module.md)**



| Feature | Details |
|---------|---------|
| **Staff Profiles** | Employment type, hire date, salary/hourly rate, specialties, department tracking |
| **Credentials** | License/certification tracking with expiration alerts and renewal workflows |
| **Time Off** | Vacation, sick, CE, maternity, bereavement, jury duty — approval workflows |
| **Training** | Compliance training tracking (HIPAA, BLS, CPR) with due dates and completion status |
| **Performance Reviews** | Annual/semi-annual reviews with ratings, goals, improvement plans, and acknowledgment |
| **Onboarding** | Pending onboarding status, credential verification pipeline, training assignments |

</details>

<details>
<summary><h3>📋 Clinical Notes & Documentation</h3></summary>

🔗 **[Read Detailed Clinical Notes & Documentation Documentation](docs_source_en/clinical_notes_documentation.md)**



| Feature | Details |
|---------|---------|
| **SOAP Notes** | AI-generated from voice dictation with specialty-specific templates |
| **Voice Dictation** | WASM Whisper on-device → zero cloud PHI transmission |
| **4 Note Templates** | Therapy Session, Progress Note, Initial Evaluation, Discharge Summary |
| **Documents** | Lab results, imaging, consents, assessments, treatment plans — all workspace-scoped |
| **PDF Export** | Server-side rendering (no client-side PHI leakage) |
| **E-Signatures** | BoldSign integration with 7 document templates |
| **OCR** | Document scanning in 30+ languages for intake form digitization |

</details>

<details>
<summary><h3>📅 Scheduling & Appointments</h3></summary>

🔗 **[Read Detailed Scheduling & Appointments Documentation](docs_source_en/scheduling_appointments.md)**



| Feature | Details |
|---------|---------|
| **Appointment States** | Scheduled → Confirmed → In-Progress → Completed (+ cancelled, no-show, rescheduled) |
| **Patient Portal Requests** | Patients request appointments with preferred date/time → staff confirms or denies |
| **Multi-Provider** | Schedule across providers within a practice |
| **Recurring Visits** | Weekly therapy sessions, monthly check-ups, ortho adjustments |
| **Waitlist** | Waitlisted appointment requests when slots are full |
| **Reminders** | Automated appointment reminders (planned) |

</details>

<details>
<summary><h3>📴 Offline-First Clinical Sessions</h3></summary>

🔗 **[Read Detailed Offline-First Clinical Sessions Documentation](docs_source_en/offline_first_clinical_sessions.md)**



| Feature | Details |
|---------|---------|
| **Client-Side Timestamps** | Session start/end times captured on the provider's device — used for billing, not server receipt time |
| **Offline Queue** | Events queued in localStorage when offline, auto-synced on reconnect |
| **Draft Persistence** | Clinical notes auto-saved to localStorage on every keystroke — survives browser crash, connection loss |
| **Session Sign-Off** | Provider MUST sign off at session end — timestamp is the billing-accurate end time |
| **Admin Audit** | Each event shows 🟢 Online / 🔴 Offline indicator with sync timestamps |
| **Connection Monitor** | Sidebar shows real-time 🟢/🔴 status with pending sync count badge |
| **HIPAA Cleanup** | All local data purged on logout and idle timeout |
| **Idempotent Sync** | Duplicate events prevented via client-generated UUIDs |
| **Time Drift Detection** | Server logs drift between client and server timestamps for audit |
| **Session Lifecycle** | `session_start` → `session_pause` → `session_resume` → `session_end` |

**Billing Compliance:**
```
Provider starts session at 2:00 PM (online) → 🟢
  Connection drops at 2:30 PM
Provider ends session at 3:45 PM (offline) → 🔴 client_timestamp = 3:45 PM
  Connection restores at 4:00 PM → auto-sync
Server records: client_timestamp = 3:45 PM, sync_timestamp = 4:00 PM
  ↓
Insurance billed: session 2:00 PM – 3:45 PM (accurate)
Admin sees: "Session ended 3:45 PM 🔴 Offline (synced 4:00 PM)"
```

</details>

<details>
<summary><h3>🧪 Lab Orders & Results Module</h3></summary>

🔗 **[Read Detailed Lab Orders & Results Module Documentation](docs_source_en/lab_orders_results_module.md)**



| Feature | Details |
|---------|---------|
| **Lab Orders** | Order tracking with vendor (Quest, LabCorp, in-house), priority (routine/urgent/stat) |
| **Result Tracking** | Individual test results with reference ranges and abnormal flags (low/high/critical) |
| **Categories** | Hematology, Chemistry, Lipid, Liver, Thyroid, Vitamin, Inflammation, Coagulation |
| **Abnormal Alerts** | Automatic flagging of out-of-range results (e.g., elevated TSH, low Vitamin D) |
| **iPLEDGE Labs** | Monthly Accutane monitoring: CBC, CMP, lipid panel, LFTs with trend tracking |
| **Pre-Surgical** | INR, PT, glucose, A1C clearance for dental implants and surgical procedures |
| **Medication Monitoring** | SSRI thyroid checks, stimulant lipid panels, biologic baseline panels |
| **Order Lifecycle** | Ordered → Collected → Sent → Received → In Progress → Resulted → Reviewed |
| **Vendor Integration** | Quest Diagnostics, LabCorp order routing (planned: electronic result import) |
| **Diagnosis Linking** | ICD-10 codes attached to orders for medical necessity documentation |

</details>

<details>
<summary><h3>💊 Medications & Prescriptions Module</h3></summary>

🔗 **[Read Detailed Medications & Prescriptions Module Documentation](docs_source_en/medications_prescriptions_module.md)**



| Feature | Details |
|---------|---------|
| **Drug Catalog** | 12+ medications with NDC codes, drug classes, schedules, routes, common doses |
| **Active Prescriptions** | Per-patient medication list with dose, frequency, prescriber, pharmacy, refill tracking |
| **Drug Classes** | SSRIs, stimulants, retinoids, biologics, bronchodilators, NSAIDs, antibiotics, anticonvulsants |
| **iPLEDGE Tracking** | Accutane isotretinoin monitoring with monthly lab requirements |
| **Status Lifecycle** | Active → On Hold → Discontinued → Completed → Cancelled |
| **Interaction Warnings** | Drug-specific warnings array (serotonin syndrome, QTc, teratogenic) |
| **Pharmacy Routing** | Named pharmacy per prescription for e-prescribe readiness |

</details>

<details>
<summary><h3>📊 Vitals & Measurements Module</h3></summary>

🔗 **[Read Detailed Vitals & Measurements Module Documentation](docs_source_en/vitals_measurements_module.md)**



| Feature | Details |
|---------|---------|
| **Standard Vitals** | BP (systolic/diastolic), HR, RR, temp (with method), SpO2, weight, height, BMI |
| **Pain Scale** | 0-10 numeric pain scale per visit |
| **Pediatric Growth** | Head circumference, weight/height/BMI percentiles (WHO/CDC) |
| **PT Assessments** | ROM degrees, functional scores (Oswestry, LEFS), quad activation notes |
| **Trend Tracking** | Historical vitals per patient for trend analysis |
| **Appointment Linked** | Vitals tied to specific appointment encounters |

</details>

<details>
<summary><h3>⚠️ Allergies & Alerts Module</h3></summary>

🔗 **[Read Detailed Allergies & Alerts Module Documentation](docs_source_en/allergies_alerts_module.md)**



| Feature | Details |
|---------|---------|
| **Allergen Types** | Drug, food, environmental, latex, contrast, other |
| **Severity Levels** | Mild, moderate, severe, life-threatening |
| **Reaction Tracking** | Specific reaction documentation (anaphylaxis, SJS, hives, GI upset) |
| **NKDA Support** | Explicit "No Known Drug Allergies" documentation |
| **Clinical Alerts** | Critical allergy flags (Penicillin → use clindamycin, Sulfa → SJS history) |
| **Verification** | Provider verification with date stamps |

</details>

<details>
<summary><h3>💉 Immunizations Module</h3></summary>

🔗 **[Read Detailed Immunizations Module Documentation](docs_source_en/immunizations_module.md)**



| Feature | Details |
|---------|---------|
| **Vaccine Tracking** | CVX codes, dose numbers, lot numbers, manufacturers |
| **Administration** | Site, route (IM/SC/PO/IN/ID), administering provider |
| **VIS Compliance** | Vaccine Information Statement date tracking |
| **Registry Reporting** | State immunization registry submission tracking |
| **CDC Schedule** | DTaP, IPV, MMR, Varicella, Hep A/B, Influenza, Tdap |
| **Immunocompromised** | Special vaccine recommendations for biologic patients |

</details>

<details>
<summary><h3>⏱️ Timesheets & Payroll Module</h3></summary>

🔗 **[Read Detailed Timesheets & Payroll Module Documentation](docs_source_en/timesheets_payroll_module.md)**



| Feature | Details |
|---------|---------|
| **Auto-Generation** | Timesheets automatically generated from signed clinical session notes |
| **Non-Billable Time** | Track admin time, drive time, training, and clinic prep |
| **Approval Workflows** | Employee submission → Supervisor review → Payroll processing |
| **Payroll Export** | Export timesheets natively integrated with ADP, Gusto, and Paycom |
| **Compliance** | 40-hour overtime warnings, mandatory break tracking, PTO accrual visibility |

</details>

<details>
<summary><h3>⚙️ Platform Administration & White-Label</h3></summary>

🔗 **[Read Detailed Platform Administration & White-Label Documentation](docs_source_en/platform_administration_white_label.md)**



| Feature | Details |
|---------|---------|
| **Multi-Tenant Architecture** | Isolated workspaces with dedicated branding and configurations |
| **Dynamic Workspaces** | Practice logo, primary address, and color theming dynamically fetched via SSR |
| **Module Availability** | Platform Admins can drag-and-drop or hide modules based on the clinic specialization |
| **Employee Feature Toggling** | Override base roles with `restricted_features` JSONB arrays enforcing API blocks at runtime |
| **Screen Builders** | Per-practice ability to rename buttons, hide datagrid columns, or override standard UI copy |
| **Break-Glass Auditing** | All platform admin actions logged to HIPAA-compliant audit trails |

</details><details>
<summary><h3>🔄 Referrals & Cross-Practice Chat Module</h3></summary>

🔗 **[Read Detailed Referrals & Cross-Practice Chat Module Documentation](docs_source_en/referrals_cross_practice_chat_module.md)**



| Feature | Details |
|---------|---------|
| **Referral Tracking** | From/to provider, specialty, reason, diagnosis codes, urgency, auth tracking |
| **Status Lifecycle** | Pending → Sent → Accepted → Scheduled → Completed / Expired / Declined |
| **Cross-Practice Chat** | HIPAA-compliant messaging between practice admins/office managers |
| **Attachment Sharing** | Send images, X-rays, documents, lab results, prescriptions between practices |
| **Threaded Conversations** | Per-referral chat threads with read receipts |
| **Real Examples** | Peds→Psychiatry (ADHD), Derm→PT (psoriatic arthritis), PT→Derm (wound care) |
| **Authorization Tracking** | Auth numbers, expiry dates, prior auth requirement flags |

</details>

<details>
<summary><h3>📋 Clinical Tasks Module</h3></summary>

🔗 **[Read Detailed Clinical Tasks Module Documentation](docs_source_en/clinical_tasks_module.md)**



| Feature | Details |
|---------|---------|
| **Task Categories** | Lab follow-up, prior auth, scheduling, documentation, billing, call patient, refill, referral |
| **Priority Levels** | Low, normal, high, urgent |
| **Assignment** | Assigned to specific staff with due dates and completion tracking |
| **Patient Linked** | Tasks tied to specific patients for care coordination |
| **Status Tracking** | Open → In Progress → Completed / Cancelled / Deferred |
| **Audit Trail** | Created by, completed by, completed at timestamps |

</details>

<details>
<summary><h3>🏥 Patient Insurance Module</h3></summary>

🔗 **[Read Detailed Patient Insurance Module Documentation](docs_source_en/patient_insurance_module.md)**



| Feature | Details |
|---------|---------|
| **Plan Details** | Payer, plan name, member ID, group number, subscriber relationship |
| **Cost Sharing** | Copay amount, coinsurance %, deductible, deductible met, out-of-pocket max |
| **Primary/Secondary** | Multi-payer support with primary/secondary designation |
| **Verification** | Verification status with verified date |
| **Medicare/Medicaid** | MBI tracking, therapy cap tracking, remaining benefit amounts |
| **All Major Payers** | BCBS, UHC, Anthem, Aetna, Delta Dental, MetLife, Cigna, Humana, Medicare |

</details>

<details>
<summary><h3>🔔 Recalls & Reminders Module</h3></summary>

🔗 **[Read Detailed Recalls & Reminders Module Documentation](docs_source_en/recalls_reminders_module.md)**



| Feature | Details |
|---------|---------|
| **Recall Types** | Hygiene, annual exam, follow-up, lab recheck, imaging, screening, vaccination, med review |
| **Status Tracking** | Due → Overdue → Scheduled → Completed → Cancelled |
| **Contact Attempts** | Track outreach attempts for overdue recalls |
| **Practice-Specific** | Dental 6-month cleanings, derm annual skin checks, Accutane monthly labs |
| **Auto-Due Dates** | Based on last completed visit |

</details>

<details>
<summary><h3>📦 Inventory Management Module</h3></summary>

🔗 **[Read Detailed Inventory Management Module Documentation](docs_source_en/inventory_management_module.md)**



| Feature | Details |
|---------|---------|
| **Categories** | Dental supplies, vaccines, medications, biologics, PPE, surgical, lab supplies, office |
| **Stock Tracking** | Quantity on hand, reorder level, reorder quantity, unit cost |
| **Lot & Expiry** | Lot numbers, expiration dates, FIFO rotation for vaccines |
| **Supplier Tracking** | Henry Schein, Patterson Dental, Nobel Biocare, McKesson, Sanofi Pasteur |
| **Status Alerts** | In stock, low stock, out of stock, expired, discontinued |
| **Storage Locations** | Vaccine fridge (2-8°C), biologic fridge, operatory cabinets, locked cabinets |
| **Specialty Items** | Implant fixtures ($285), biologic pens ($2,850), cryotherapy canisters |

</details>

<details>
<summary><h3>🧾 Superbills Module</h3></summary>

🔗 **[Read Detailed Superbills Module Documentation](docs_source_en/superbills_module.md)**



| Feature | Details |
|---------|---------|
| **Encounter-Based** | One superbill per visit with diagnosis + procedure codes |
| **Multi-Code** | ICD-10 diagnosis arrays + CPT/CDT procedure arrays + modifiers (-25, -59) |
| **Financial Breakdown** | Total charge, insurance billed, patient copay, adjustments |
| **Status Lifecycle** | Draft → Review → Submitted → Paid / Denied / Appealed |
| **All Specialties** | Well-child visits, implants, ortho, psychotherapy, PT rehab, derm procedures |
| **Medicare Write-offs** | Automatic adjustment tracking for Medicare contractual obligations |

</details>

<details>
<summary><h3>📚 Patient Education Module</h3></summary>

🔗 **[Read Detailed Patient Education Module Documentation](docs_source_en/patient_education_module.md)**



| Feature | Details |
|---------|---------|
| **Material Catalog** | 14 education documents across all specialties |
| **Multi-Language** | English + Spanish materials available |
| **Categories** | Condition, medication, procedure, lifestyle, post-op, home exercise, safety, preventive |
| **Delivery Methods** | Printed, portal upload, email, in-person, text |
| **Acknowledgment** | Track whether patient viewed/acknowledged the material |
| **Specialty Examples** | EpiPen guide, Accutane safety, ACL rehab, CBT homework, implant post-op |

</details>

<details>
<summary><h3>📊 Quality Measures Module (HEDIS/MIPS)</h3></summary>

🔗 **[Read Detailed Quality Measures Module (HEDIS/MIPS) Documentation](docs_source_en/quality_measures_module_hedismips.md)**



| Feature | Details |
|---------|---------|
| **Measure Types** | HEDIS, MIPS, CMS Star Ratings, Joint Commission, custom |
| **8 Core Measures** | Well-child visits, immunizations, depression screening, tobacco screening, antidepressant management, referral loop, BMI screening, MH follow-up |
| **Performance Tracking** | Numerator, denominator, exclusions, performance rate calculation |
| **Benchmarking** | Below / At / Above / Top Performer ratings vs national benchmarks |
| **Reporting Periods** | Annual and quarterly reporting support |
| **Practice Results** | Per-workspace compliance tracking with trend analysis |

</details>

<details>
<summary><h3>🔐 Security & Compliance</h3></summary>

🔗 **[Read Detailed Security & Compliance Documentation](docs_source_en/security_compliance.md)**



| Feature | Details |
|---------|---------|
| **HIPAA Compliance** | Full HIPAA audit trail, BAA-ready architecture |
| **RBAC** | 11 cryptographically-signed roles with tool-level ACLs |
| **Multi-Tenant Isolation** | All records scoped by `workspace_id` with row-level security |
| **EdDSA Authentication** | Ed25519 signed JWTs (15-min expiry) |
| **Encryption at Rest** | Transparent Data Encryption for all PHI |
| **Audit Logs** | Immutable `rbac_audit_log` for all role assignments, file access, and message actions |
| **HITL Safety Gate** | Dangerous tools require explicit user approval modal |
| **Fail-Closed HIPAA Mode** | Refuses mic access if local LLM unavailable (no silent cloud fallback) |
| **Data Minimization** | No `localStorage` for PHI, explicit React state nulling, `Cache-Control: no-store` |

</details>

<details>
<summary><h3>💬 Team Chat & Communication</h3></summary>

🔗 **[Read Detailed Team Chat & Communication Documentation](docs_source_en/team_chat_communication.md)**



| Feature | Details |
|---------|---------|
| **E2E Encrypted Chat** | HIPAA-compliant team messaging within workspaces |
| **AI Context Sharing** | Generate treatment plan → "Share Session" → forward to billing channel |
| **Voice-to-Action** | Voice commands → call, SMS, email, schedule (Pro+) |
| **Channels** | Department-based channels (Clinical, Billing, Admin) |
| **File Attachments** | Share documents, images, and clinical assets in chat |

</details>

---

## 🏥 Synalux Health: The Clinical Web App

*Access anywhere via iPad, Chromebook, or Desktop at [`synalux.ai/app`](https://synalux.ai/app).*

<details>
<summary><strong>The "Intake Room"</strong> — A zero-install PWA designed for ABA therapists</summary>

* **Smart Mic:** Uses the Page Visibility API + `window.onblur` to automatically pause recording if the clinician switches tabs or windows, preventing accidental ambient capture of other patients.
* **SOAP & BIP Generation:** Speak naturally. Synalux automatically categorizes your dictation into Subjective, Objective, Assessment, and Plan fields using 4 specialized templates.
* **Document Builder:** Edit the generated markdown, attach a patient intake template, and push it directly to BoldSign for parent/guardian E-Signatures in one click.
* **Server-Side PDF:** Documents are rendered server-side to prevent client-side PHI memory leakage — no `html2pdf.js` artifacts.
* **HIPAA-Hardened:** 15-minute idle timeout, no `localStorage` for PHI, explicit React state nulling on session clear, `Cache-Control: no-store` on all API responses.

**Templates:**

| Template | Use Case |
|----------|----------|
| 🧩 Therapy Session | ABA/behavioral therapy session notes |
| 📈 Progress Note | Ongoing treatment progress tracking |
| 📝 Initial Evaluation | First assessment and intake documentation |
| 🏁 Discharge Summary | Treatment completion and transition planning |

</details>

---

## 🧑‍💻 Synalux Dev: The VS Code Extension

*The ultimate memory-augmented IDE assistant.*

<details>
<summary><strong>Multi-Agent Orchestrator</strong> — Don't just chat; delegate</summary>

Describe a task (e.g., *"Add Stripe checkout and write tests"*), and Synalux will spawn a `planner` agent to break it down, a `coder` agent to write the implementation, and a `tester` agent to run Vitest in your terminal until the build passes.

* **Safe Mode Sandbox:** High-risk shell commands (`terminal`, `git_tool`, `browser`) require explicit user approval via a modal confirmation dialog before execution.
* **Dependency Audits:** Built-in tools scan your `package.json` against CVE databases automatically.
* **Prism Integration:** Synalux reads your codebase architecture and previous architectural decisions before writing a single line of code.

**17 Integrated Tools:**

| Category | Tools |
|----------|-------|
| 🖥️ Development | `terminal`, `git_tool`, `vitest`, `node_tool`, `browser` |
| 📝 Documentation | `soap_templates`, `boldsign`, `ocr`, `file_manager` |
| 🎙️ Multimodal | `voice`, `tts`, `screenshot`, `image_analyze` |
| 🔌 Integrations | `jira`, `confluence`, `slack`, `webhooks` |

</details>

---

<details>
<summary><h2>🔐 15 RBAC Roles</h2></summary>

Each role has a cryptographically signed Tool ACL and a server-injected system prompt:

| Role | Tools | Target |
|------|-------|--------|
| 🧑‍💻 `coder` | terminal, git, vitest, node, browser | Software engineers |
| 🏥 `doctor` | soap, voice, boldsign, file_manager | Physicians / BCBAs |
| 🧑‍⚕️ `medical_technician` | soap, voice, file_manager | Technicians / RBTs |
| 🏢 `office_manager` | file_manager, boldsign, slack, billing | Office Managers |
| 👨‍💼 `practice_admin` | all clinical + admin | Practice Administrators |
| 💰 `billing_specialist` | billing, claims, file_manager | Billing / Revenue Cycle |
| 👥 `hr_manager` | staff, credentials, training | HR / People Ops |
| 📋 `manager` | jira, confluence, slack, file_manager | Project Managers |
| ✍️ `writer` | file_manager, browser, screenshot | Technical Writers |
| 🔒 `security` | terminal, git, browser | Security Engineers |
| 🧪 `tester` | vitest, terminal, browser | QA Engineers |
| ⚙️ `devops` | terminal, git, webhooks | DevOps/SRE |
| 📊 `planner` | jira, confluence, webhooks | Product Managers |
| 🚫 `restricted` | *(none)* | Read-only observers |
| ⚡ `platform_admin` | **all** + plan overrides + user management | Synalux super-admins |

**Country/Province-Specific Role Activation:**
- Roles are activated per country and per medical specialty module
- Each workspace's available roles depend on its configured country and practice type
- Example: `billing_specialist` in Canada includes HST/GST tax configuration tools

</details>

---

<details>
<summary><h2>🛡️ Enterprise Security & HIPAA Architecture</h2></summary>

Synalux is engineered for zero-trust environments.

### Security Architecture — Multi-Tenant Request Flow

```
┌─────────────────┐     ┌──────────────────────────────┐     ┌──────────────────────────────┐     ┌─────────────────────────────┐
│   Client        │     │   Vercel Edge (Middleware)    │     │   Next.js API Routes         │     │   Supabase PostgreSQL       │
│                 │     │                              │     │                              │     │                             │
│  Browser /      │────▶│  1. Auth Check (NextAuth)    │────▶│  3. Tool ACL Enforcement     │────▶│  6. RLS Policies            │
│  VS Code        │     │  2. JWT Signing (Ed25519)    │     │  4. AI Sandbox               │     │     (JWT → set_config)      │
│                 │     │     (15 min TTL)             │     │     (ProposedChange)         │     │  7. Multi-Tenant Data       │
│                 │     │                              │     │  5. HIPAA Audit Log          │     │     (workspace_id isolation) │
└─────────────────┘     └──────────────────────────────┘     └──────────────────────────────┘     └─────────────────────────────┘
                              Google OAuth                    Stripped tool context                   RLS filters by workspace_id
```

**Key insight:** Because JWTs carry `workspace_id` claims and Postgres RLS policies read them via `current_setting('request.jwt.claims')`, there are **no server-side session variables** and **no per-tenant connection pools**. This is what makes Synalux horizontally scalable — a critical advantage over legacy EHRs that use connection-per-session models.

### Security Controls

* **EdDSA (Ed25519) Authentication:** Static API tokens are demoted to refresh-only status. All API requests are authenticated via short-lived (15 min) JWTs signed with asymmetric cryptography.
* **Transparent Data Encryption (TDE):** All team messages, generated documents, and session histories are encrypted at rest.
* **Strict Data Minimization:** Web App transcripts live strictly in React state memory and are garbage-collected the moment a tab is closed. `localStorage` is never used for PHI.
* **MIME-Gated File Storage:** Clinical attachments are restricted by strict server-side MIME verification and served exclusively via 15-minute signed URLs with IDOR prevention.
* **ABA Precision Protocol Guardrails:** Deeply integrated with Prism MCP, Synalux enforces behavioral adherence rules limiting AI hallucinations and strictly isolating UI elements to guarantee HIPAA compliance and prevent duplication in CRUD operations.
* **Immutable Audit Logs:** Every role assignment, file download, and message deletion is permanently recorded in the `rbac_audit_log` for compliance non-repudiation. Audit rows are append-only — even database admins cannot modify historical entries.
* **HITL Safety Gate:** Dangerous tools (`terminal`, `git_tool`, `browser`) require explicit user approval via a modal dialog before execution — preventing zero-click RCE via prompt injection.
* **Fail-Closed HIPAA Mode:** If the local LLM (Ollama) is unavailable during clinical voice intake, the system refuses to open the microphone rather than silently falling back to cloud processing.
* **StaleDataBanner (Patient Safety):** If clinical data hasn't been refreshed in the current session, a banner alerts the clinician, preventing treatment decisions based on outdated information.

### HIPAA Compliance Statement

| HIPAA Requirement | Synalux Implementation |
|---|---|
| **§164.312(a)(1)** Access Control | JWT-based RBAC with per-tool ACLs; RLS enforces tenant isolation at the database layer |
| **§164.312(b)** Audit Controls | Immutable `hipaa_audit_log` + `rbac_audit_log` + `session_events` — every PHI access, session sign-off, and plan override is recorded with user, action, resource, and timestamp |
| **§164.312(c)(1)** Integrity | AI Sandbox (`ProposedChange`) ensures no automated writes to clinical data without clinician signature. Offline session timestamps preserve billing-accurate times via client-side capture. |
| **§164.312(d)** Authentication | Ed25519 asymmetric JWTs (15 min TTL); Google OAuth with MFA for clinical roles |
| **§164.312(e)(1)** Transmission Security | TLS 1.3 enforced on all endpoints; Supabase connections use SSL; no PHI in URL parameters |
| **§164.310(d)(1)** Data Encryption | AES-256 at rest (Supabase TDE); WASM Whisper for on-device transcription (PHI never transmitted); offline drafts auto-purged on logout |
| **§164.308(a)(1)** Risk Analysis | Adversarial security reviews (`REVIEW_PROMPT.md`); automated output guardrails with rolling-window SSE scanning |
| **No LocalStorage** | All clinical data lives in React state (garbage-collected on tab close) or Postgres (RLS-protected). Session drafts in localStorage are purged on logout/idle timeout via `purgeLocalData()` |
| **Offline Safety** | Connection loss doesn't compromise data — offline queue preserves events with client timestamps, syncs on reconnect. Admin sees 🟢/🔴 indicators for audit trail. |

> **BAA Coverage:** Full HIPAA compliance with BAA requires Vercel Enterprise + Supabase Team tier. See [Infrastructure & Cloud Services](#-infrastructure--cloud-services) for pricing.

</details>

---

---

## 🚀 Getting Started

### For Healthcare & Clinics (Web App)
1. Go to [synalux.ai/app](https://synalux.ai/app).
2. Sign in with Google (MFA required for clinical roles).
3. Select **Therapy Session** from the template dropdown.
4. Type or dictate your clinical notes.
5. Click **📤 Generate SOAP Note** and review the streamed output.

### For Developers (VS Code)
1. Install the extension: `ext install synalux-ai.synalux`
2. Press `Cmd+Shift+P` → **Synalux: Sign In with Google**
3. Open the chat panel and type: `@coder Scaffold a new Next.js route for user profiles.`

### For Clinics Wanting 100% Local
```bash
# 1. Install Ollama
brew install ollama     # macOS

# 2. Pull a model
ollama pull qwen2.5-coder:14b

# 3. Enable CORS for the web app
OLLAMA_ORIGINS="https://synalux.ai" ollama serve

# 4. Open synalux.ai/app → toggle backend to "Local"
```

---

<details>
<summary><h2>☁️ Infrastructure & Cloud Services</h2></summary>

Synalux runs on a **serverless-first architecture** using 6 cloud services. No Azure, AWS, or GCP VMs are needed.

### Current Stack (All Free Tiers)

| Service | Role | Current Plan | Cost | Free Tier Limit |
|---------|------|-------------|------|-----------------|
| **Vercel** | Hosting + Edge + CDN | Pro | $20/mo | Global CDN, auto-scaling |
| **Supabase (US)** | PostgreSQL + Auth + RLS | Pro | $25/mo | West US (Oregon) — US/CA data |
| **Supabase (EU)** | PostgreSQL + Auth + RLS | Pro | $0/mo (Micro included) | Central EU (Frankfurt) — GDPR data residency |
| **Stripe** | Payments + Subscriptions | Standard | 2.9% + 30¢/txn | No monthly fee, unlimited products |
| **Google Cloud** | Gemini AI + OAuth + Transcription | Free tier | $0/mo | 15 RPM Gemini, unlimited OAuth |
| **OpenRouter** | Multi-model LLM routing | Free models | $0/mo | Unlimited `:free` model requests |
| **GitHub** | Source control + CI/CD | Free | $0/mo | Unlimited private repos, 2000 CI min/mo |

### Multi-Region Architecture (GDPR Compliant)

Synalux routes patient data to the geographically correct database based on workspace country:

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        Vercel Edge Network                              │
│              (auto-routes to nearest PoP worldwide)                     │
├─────────────────────────────────┬────────────────────────────────────────┤
│         US/CA Workspaces        │         EU/UK Workspaces               │
│                                 │                                        │
│  ┌───────────────────────────┐  │  ┌────────────────────────────────┐    │
│  │  Supabase — US (Oregon)   │  │  │  Supabase — EU (Frankfurt)     │    │
│  │  pjddaprqhwqxtcpdmprk    │  │  │  rkffbtabogjxxzxmgodv          │    │
│  │  SSL Enforced ✅           │  │  │  SSL Enforced ✅                │    │
│  │  21 migrations synced     │  │  │  21 migrations synced          │    │
│  └───────────────────────────┘  │  └────────────────────────────────┘    │
└─────────────────────────────────┴────────────────────────────────────────┘
```

**Data Residency Routing (`supabase-region.ts`):**

| Workspace Country | Database Region | Supabase Instance |
|-------------------|----------------|-------------------|
| 🇺🇸 US, 🇨🇦 CA | West US (Oregon) | `pjddaprqhwqxtcpdmprk` |
| 🇬🇧 UK, 🇩🇪 DE, 🇫🇷 FR, 🇳🇱 NL + 27 EU countries | Central EU (Frankfurt) | `rkffbtabogjxxzxmgodv` |

**Locale-Aware Clinical Dictionaries (`clinical-dictionaries.ts`):**

All clinical dropdowns auto-populate based on workspace country:

| Dictionary | US | CA | UK | EU |
|-----------|----|----|----|----|---|
| Insurance Providers | Aetna, BCBS, Medicaid... | OAP, OHIP, Sun Life... | NHS, EHCP, Bupa... | AOK, CPAM, Allianz... |
| Diagnosis Codes | ICD-10-CM | ICD-10-CA | ICD-10 + ICD-11 preview | ICD-10 + ICD-11 preview |
| Billing Codes | CPT (97151-97158) | Hourly service codes | Service descriptions | Service descriptions |
| Credentials | BCBA, RBT, NPI | BCBA, ONTABA RBA | UKBA(cert), HCPC | BCBA (legacy) |
| Issuing Authorities | BACB, State Board | BACB, ONTABA, CIHI | UK-SBA, PSA, DBS | UK-SBA, BACB |
| States/Provinces | 50 US states + DC | 13 provinces/territories | 4 UK regions | — |

### AI Models & Routing

Synalux routes AI requests through a **dual-backend architecture**:

**Cloud Backend (via OpenRouter + Gemini fallback)**
| User Plan | Default Model | Max Tokens | Daily Limit |
|-----------|---------------|-----------|-------------|
| Free | Gemma 3 12B `:free` | 2,048 | 10K tokens |
| Standard | Gemma 3 27B `:free` | 4,096 | 100K tokens |
| Pro | Gemma 4 31B `:free` | 8,192 | 500K tokens |
| Enterprise | Gemma 4 31B `:free` | 16,384 | 5M tokens |

**Selectable Models (by tier)**
| Model | Free | Standard | Pro | Enterprise |
|-------|------|----------|-----|-----------|
| Gemma 3 12B | ✅ | ✅ | ✅ | ✅ |
| Gemini 2.5 Flash | — | ✅ | ✅ | ✅ |
| Claude Sonnet 4 | — | — | ✅ | ✅ |
| GPT-4.1 | — | — | ✅ | ✅ |
| Gemini 2.5 Pro | — | — | ✅ | ✅ |
| Claude Opus 4 | — | — | — | ✅ |
| o3-pro | — | — | — | ✅ |

**Local Backend (Ollama — 100% on-device, no tier gating)**
| Model | RAM Required |
|-------|-------------|
| Qwen 2.5 Coder 14B | 18GB |
| DeepSeek R1 14B | 18GB |
| Qwen 2.5 Coder 32B | 36GB |
| DeepSeek R1 32B | 36GB |

**Google Gemini (Free Tier — Direct Fallback)**
| Feature | Limit |
|---------|-------|
| Model | `gemini-2.5-flash` |
| Rate limit | 15 requests/minute |
| Input context | 1M tokens |
| Voice transcription | Gemini-powered, free tier |

> **Why Gemini as fallback?** When OpenRouter is down or rate-limited, the chat API
> falls back to Google's Gemini API directly. This gives us a free, reliable safety net
> with tool-calling support. No API key cost — Google's free tier is generous.

### Scaling Thresholds

| Clients | Action Required | Monthly Cost |
|---------|----------------|-------------|
| **1–100** | ⚠️ Upgrade Vercel to Pro (commercial use required) | **$20** |
| **100–1,000** | Upgrade Supabase to Pro (8GB DB, daily backups) | **$45** |
| **1,000–10,000** | Add Vercel Pro + Supabase Pro + CDN for videos | **$50–100** |
| **10,000+** | Vercel Pro + Supabase Team + custom Stripe rate | **$650+** |
| **HIPAA Required** | Vercel Enterprise + Supabase Team (BAA) | **$1,100+** |

### Enterprise Tier Pricing

| Service | Enterprise Plan | Price | What You Get |
|---------|----------------|-------|-------------|
| **Vercel** | Enterprise | ~$500+/mo (custom) | BAA, SSO/SAML, SLA, dedicated support, WAF |
| **Supabase** | Team | $599/mo | BAA, SOC2, HIPAA, 100GB DB, priority support |
| **Supabase** | Enterprise | Custom | HIPAA+BAA, dedicated infra, custom SLA |
| **Stripe** | Custom | Negotiated | 2.5% + 25¢ at $50K+/mo volume |
| **OpenRouter** | Pay-per-token | ~$0.001–0.03/1K tokens | Non-free models (Claude Opus, GPT-4.1, o3) |
| **Google Cloud** | Pay-as-you-go | $0 (free tier sufficient) | Upgrade only if exceeding 15 RPM |

### Why Not Azure or AWS?

Synalux deliberately avoids Azure, AWS, and traditional IaaS:

| Concern | How Synalux Handles It | Why Not Azure/AWS |
|---------|----------------------|-------------------|
| **Hosting** | Vercel (zero-config Next.js, global CDN, auto-scaling) | Azure App Service requires manual scaling, SSL config, CI/CD setup |
| **Database** | Supabase (managed Postgres + built-in RLS + Auth + Realtime) | Azure SQL/RDS requires manual RLS policies, separate auth service |
| **AI/LLM** | OpenRouter + Gemini (multi-model routing, free tiers) | Azure OpenAI requires $200+/mo commitment, limited model selection |
| **Auth** | NextAuth + Google OAuth (zero cost, built-in) | Azure AD B2C is $0.00325/auth, complex setup |
| **Payments** | Stripe (industry standard, PCI-compliant) | No Azure/AWS equivalent |
| **CI/CD** | GitHub Actions (free for private repos) | Azure DevOps adds complexity |
| **Total ops burden** | **Zero servers to manage** | Azure/AWS = VMs, VPCs, security groups, patching |

> **Bottom line:** Azure/AWS would cost **$200–500+/mo** for equivalent infrastructure with
> significantly more operational complexity. Our serverless stack runs at **$0/mo** on free
> tiers and scales to **$45/mo** for 1,000 clients — with zero server management.

### Current Database Stats (Live)

| Metric | Value |
|--------|-------|
| Database size | 17 MB / 500 MB (3%) |
| Tables | ~30 |
| Patients | 27 |
| Appointments | 61 |
| Documents | 78 |
| Cache hit rate | 99–100% |
| WAL size | 80 MB |

</details>

---

<details>
<summary><h2>📁 Project Structure</h2></summary>

```
synalux-private/
├── portal/                   # Next.js web portal + clinical web app
│   ├── src/app/app/          # 🏥 Synalux Health (Web App)
│   │   ├── page.tsx          # SOAP Notes workspace
│   │   ├── chat/page.tsx     # AI Chat
│   │   ├── team/page.tsx     # Team Chat (Pro+)
│   │   ├── billing/page.tsx  # Clinical Billing (multi-currency)
│   │   └── layout.tsx        # App shell + sidebar + offline monitor
│   ├── src/app/admin/        # 🛡️ Admin Dashboard
│   │   ├── subscriptions/    # Subscription management (multi-currency)
│   │   └── users/            # User management + plan overrides
│   ├── src/app/patient-portal/  # 🏥 Patient Portal
│   │   └── page.tsx          # Dashboard, Documents, Appointments, Billing, Messages
│   ├── src/app/api/v1/       # REST APIs
│   │   ├── chat/route.ts     # Streaming chat (SSE)
│   │   ├── soap/route.ts     # SOAP note generation
│   │   ├── pdf/route.ts      # Server-side PDF export
│   │   ├── messages/         # Team Chat API
│   │   ├── roles/            # RBAC management
│   │   ├── billing/          # Stripe integration + multi-currency checkout
│   │   ├── sessions/         # Offline-first session sign-off API
│   │   ├── admin/            # Platform admin APIs (plan overrides)
│   │   └── webhooks/stripe/  # Stripe webhook handler (payment lifecycle)
│   ├── src/lib/              # Auth, DB, i18n, SOAP templates
│   │   ├── stripe.ts         # Stripe Connect + Multi-Currency Checkout + Portal
│   │   ├── pricing-engine.ts # Enterprise pricing: per-country, volume, annual
│   │   ├── platform-admin.ts # Platform super-admin + plan overrides
│   │   ├── session-offline.ts# Offline-first session management + draft persistence
│   │   ├── supabase-clients.ts # Service-role + RLS-enforced Supabase clients
│   │   ├── supabase-region.ts # Multi-region router (US/EU) based on workspace country
│   │   ├── clinical-dictionaries.ts # Locale-aware clinical ref data (US/CA/GB/EU)
│   │   ├── region-config.ts  # Country/province configuration + tax rules
│   │   ├── db.ts             # Supabase client + user management
│   │   └── auth-options.ts   # NextAuth + Google OAuth
│   ├── src/__tests__/        # Test suites
│   │   ├── billing.test.ts   # Pricing engine + payment flow (42 tests)
│   │   └── session-offline.test.ts # Offline sessions + compliance (32 tests)
│   └── supabase/             # Database migrations + seed data
│       ├── seed_poc_part1.sql          # Core users/workspaces
│       ├── seed_poc_part2b_*.sql       # HR tables + clinical catalogs
│       ├── seed_poc_part2c.sql         # Cross-practice links + payers
│       ├── seed_poc_part2d.sql         # Appointments (61 records)
│       ├── seed_poc_part2e.sql         # Treatment plans (16 records)
│       ├── seed_poc_part2f.sql         # HR module (staff/credentials/reviews)
│       ├── seed_poc_part2g.sql         # Billing entries, SOAP notes, documents
│       ├── seed_poc_part2h.sql         # Portal data (messages, consents, forms)
│       ├── seed_poc_part2i_*.sql       # Per-practice billing config + Stripe Connect
│       ├── seed_poc_part2q_module_tabs.sql  # 13 clinical modules (referrals, tasks, etc.)
│       └── migrations/                 # Schema migrations
│           ├── 20260417_payment_status_plan_override.sql  # Payment tracking + overrides
│           └── 20260417_session_events.sql                # Offline session events
├── synalux-vscode/           # 🧑‍💻 VS Code extension
│   ├── src/chat-panel.ts     # Agentic chat + tool execution
│   ├── src/mcp-server.ts     # Local MCP tool dispatcher
│   └── tools/                # Python tool implementations
├── README.md                 # This file
├── LICENSE                   # BSL-1.1
└── REVIEW_PROMPT.md          # Adversarial security review
```

</details>

---

<details>
<summary><h2>📊 Database Census</h2></summary>

The production database contains **1,400+ records** across 71 tables:

| Module | Table | Records |
|--------|-------|---------|
| **Infrastructure** | Workspaces | 6 |
| | Users | 19 |
| | Workspace Members | 21 |
| | Medical Fields | 37 |
| | Workspace Roles | 54 |
| | Role Field Links | 104 |
| **Auth & Security** | JWT Auth Log | 261 |
| | API Tokens | 14 |
| | Processed Webhook IDs | 11 |
| **Clinical Catalogs** | Diagnosis Codes (ICD-10) | 63 |
| | Billing Codes (CPT/CDT) | 61 |
| | Insurance Payers | 16 |
| | Medications Catalog | 12 |
| **Patient Care** | Patients | 27 |
| | Appointments | 61 |
| | Treatment Plans | 16 |
| | Session Notes | 18 |
| | Documents | 78 |
| | Patient Vitals | 10 |
| | Patient Allergies | 10 |
| | Patient Medications | 10 |
| | Immunizations | 10 |
| | Clinical Tasks | 10 |
| **Billing & Revenue** | Billing Entries | 34 |
| | Fee Schedules | 26 |
| | Patient Payments | 15 |
| | Payment Plans | 3 |
| | Insurance Claims | 7 |
| | Workspace Billing Configs | 6 |
| | Patient Insurance | 15 |
| **HR Module** | Staff Profiles | 16 |
| | Staff Credentials | 14 |
| | Staff Time Off | 10 |
| | Staff Training | 13 |
| | Performance Reviews | 6 |
| **Patient Portal** | Portal Messages | 18 |
| | Patient Consents | 21 |
| | Patient Forms | 14 |
| | Appointment Requests | 10 |
| | Portal Access Codes | 9 |
| **Lab Module** | Lab Orders | 9 |
| | Lab Results | 29 |
| **Referral System** | Referrals | 5 |
| | Referral Chat Threads | 3 |
| | Referral Chat Messages | 15 |
| | Patient Recalls | 11 |

</details>

---

<details>
<summary><strong>🌐 Supported Languages</strong></summary>

The portal, documentation, and AI interface are available in 12 languages:

| Language | Code | Status |
|----------|------|--------|
| 🇺🇸 English | `en` | ✅ Full |
| 🇪🇸 Español | `es` | ✅ Full |
| 🇫🇷 Français | `fr` | ✅ Full |
| 🇵🇹 Português | `pt` | ✅ Full |
| 🇷🇴 Română | `ro` | ✅ Full |
| 🇺🇦 Українська | `uk` | ✅ Full |
| 🇷🇺 Русский | `ru` | ✅ Full |
| 🇩🇪 Deutsch | `de` | ✅ Full |
| 🇯🇵 日本語 | `ja` | ✅ Full |
| 🇰🇷 한국어 | `ko` | ✅ Full |
| 🇨🇳 中文 | `zh` | ✅ Full |
| 🇸🇦 العربية | `ar` | ✅ Full (RTL) |

</details>

---

<p align="center">
  <br>
  <b>© 2024–2026 Dmitri Costenco.</b><br>
  Licensed under the <a href="LICENSE">Business Source License 1.1 (BSL-1.1)</a>.<br>
  <a href="https://synalux.ai/docs/disclaimer">Legal & Medical Disclaimer</a>
</p>
