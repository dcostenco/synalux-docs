# ✦ Synalux

**Tu Plataforma de Gestión de Consultorio con IA**

> Gestiona toda tu práctica de salud desde una sola plataforma — historias clínicas, citas, facturación, comunicación de equipo y documentación asistida por IA. Funciona para terapia ABA, pediatría, salud mental, odontología, fisioterapia y dermatología. Disponible en 12 idiomas. Compatible con HIPAA.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Try_It_Free-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Developer_Tools-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language / Язык / Limba:** [English](../../README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← Volver a la versión en inglés](../../README.md)**

🎬 **Próximamente videos de demostración** — Vea el flujo completo: pacientes, citas, notas, facturación y chat de equipo en acción.

---

## 💡 ¿Por qué Synalux?

### Para Clínicos
* **🎙️ Habla, no escribas.** Dicta tus notas de sesión y Synalux las convierte en notas SOAP estructuradas al instante — todo procesado en tu dispositivo, nunca enviado a la nube.
* **📴 Funciona sin conexión.** Inicia y termina sesiones incluso sin internet. Tus notas se guardan localmente y se sincronizan automáticamente cuando vuelves a estar en línea. Tu hora de cierre siempre es precisa para la facturación.
* **🛡️ IA en la que puedes confiar.** Cada sugerencia de IA te muestra una comparación antes/después. Nada cambia en el expediente del paciente hasta que tú lo apruebas explícitamente.
* **📝 Menos papeleo.** Genera FBAs, BIPs, informes de progreso y resúmenes de alta a partir de los datos de tu sesión — luego envía para firma electrónica con un clic.

### Para Propietarios y Administradores de Consultorios
* **🏥 Una plataforma para cualquier especialidad.** Todo el sistema se adapta a tu tipo de práctica — ABA, pediatría, salud mental, dental, fisioterapia o dermatología.
* **🌍 Facturación internacional.** Acepta pagos en USD, CAD, GBP, EUR, AUD y NZD. Los descuentos por volumen se activan automáticamente a partir de 100, 500 y 1.000+ clientes. La facturación anual ahorra un 20%.
* **💳 Nunca pierdas ingresos.** Los pagos fallidos se reintentan automáticamente. Ves alertas antes de que nadie pierda acceso. Los administradores pueden activar periodo de prueba ilimitado.
* **👥 Controla quién ve qué.** 15 roles — desde médicos hasta especialistas en facturación y RRHH — cada uno con permisos específicos.

### Para TI y Cumplimiento
* **📴 Sesiones seguras offline.** Las marcas de tiempo se capturan en el dispositivo del clínico. Cuando cierran sesión a las 3:45 PM sin señal, el tiempo de facturación es 3:45 PM. Los administradores ven indicadores 🟢/🔴 para cada evento.
* **🔐 HIPAA integrado.** Cierre por inactividad de 15 minutos, sin datos de pacientes en el navegador, cifrado en reposo, registros de auditoría para cada acción.
* **📊 89 pruebas automatizadas.** Motor de precios, flujo de pago, sesiones offline y escenarios de cumplimiento — todos cubiertos.

---


## 📦 Platform Modules

Every module is multi-tenant, workspace-scoped, and HIPAA-compliant with strict role-based access.

### 🏥 Clinical Care Modules
<details>
<summary><h3>📋 Clinical Notes & Documentation</h3></summary>

🔗 **[Read Detailed Clinical Notes & Documentation Documentation](docs_source_en/clinical_notes_documentation.md)**



| Feature | Details |
|---------|---------|
| **SOAP Notes** | Auto-generated from voice dictation with specialty-specific templates |
| **Voice Dictation** | WASM Whisper on-device → zero cloud PHI transmission |
| **4 Note Templates** | Therapy Session, Progress Note, Initial Evaluation, Discharge Summary |
| **Documents** | Lab results, imaging, consents, assessments, treatment plans — all workspace-scoped |
| **PDF Export** | Server-side rendering (no client-side PHI leakage) |
| **E-Signatures** | BoldSign integration with 7 document templates |
| **OCR** | Document scanning in 30+ languages for intake form digitization |

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

### 🏢 Practice Operations Modules
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

### 🤝 Patient Experience & Collaboration
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
<summary><h3>💬 Team Chat & Communication</h3></summary>

🔗 **[Read Detailed Team Chat & Communication Documentation](docs_source_en/team_chat_communication.md)**



| Feature | Details |
|---------|---------|
| **E2E Encrypted Chat** | HIPAA-compliant team messaging within workspaces |
| **Group Video Meetings** | Scalable 6-peer mesh WebRTC HIPAA-compliant telehealth & team standups |
| **Secure Scheduling** | Authenticated RSVPs utilizing zero-PHI email layouts for calendar links |
| **Voice & Video Calls** | Secure voice and video conferencing (Enterprise only) |
| **AI Context Sharing** | Generate treatment plan → "Share Session" → forward to billing channel |
| **Voice-to-Action** | Voice commands → call, SMS, email, schedule (Pro+) |
| **Channels** | Department-based channels (Clinical, Billing, Admin) |
| **File Attachments** | Share documents, images, and clinical assets in chat |

</details>

<details>
<summary><h3>📞 Collaboration Practice Suite</h3></summary>

| Feature | Details |
|---------|---------|
| **Centralized Dashboard** | Router mapping aggregate metrics efficiently. Command center isolating missed tasks natively. |
| **Video Consults (WebRTC)** | Advanced secure P2P video streaming using Twilio TURN/STUN nodes avoiding middleboxes. |
| **RLS Gating** | Implicit identity tracking eliminating server-side cross-tenant data leaks natively mapping strictly to Advanced/Pro limits. |
| **Clinical Tasks** | Internal clinic reminders, approvals, and queueing isolated per workspace securely. |

</details>

### 🔐 Enterprise Administration
    <details>
    <summary><h3>🛡️ Security & Compliance</h3></summary>

| Feature | Details |
|---------|---------|
| **HIPAA Compliance** | Full HIPAA audit trail, BAA-ready architecture |
| **Strict Access Control** | 11 cryptographically-signed roles with specific access limits |
| **Data Isolation** | All records are isolated by clinic (`workspace_id`) to prevent cross-contamination |
| **Cryptographic Login** | Short-lived tokens (15-min expiry) ensure stale devices are logged out |
| **Encryption at Rest** | Transparent Data Encryption (AES-256) for all health information |
| **Tamper-Proof Audit Logs** | Immutable logs for all role assignments, file access, and message actions |
| **Fail-Closed HIPAA Mode** | Refuses microphone access if local processing is unavailable (no silent cloud fallback) |
| **Data Minimization** | No browser caching for PHI; sensitive data is wiped instantly when a tab closes |
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

</details>



---

## 🏥 Synalux Health: La aplicación web clínica

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

## 🧑‍💻 Synalux Dev: La extensión VS Code

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
<summary><h2>🔐 11 RBAC Roles</h2></summary>

Each role has a cryptographically signed Tool ACL and a server-injected system prompt:

| Role | Tools | Target |
|------|-------|--------|
| 🧑‍💻 `coder` | terminal, git, vitest, node, browser | Software engineers |
| 🏥 `bcba` | soap, voice, boldsign, file_manager | Board Certified Behavior Analysts |
| 🧑‍⚕️ `rbt` | soap, voice, file_manager | Registered Behavior Technicians |
| 🏢 `office` | file_manager, boldsign, slack | Office Managers |
| 📋 `manager` | jira, confluence, slack, file_manager | Project Managers |
| ✍️ `writer` | file_manager, browser, screenshot | Technical Writers |
| 🔒 `security` | terminal, git, browser | Security Engineers |
| 🧪 `tester` | vitest, terminal, browser | QA Engineers |
| ⚙️ `devops` | terminal, git, webhooks | DevOps/SRE |
| 📊 `planner` | jira, confluence, webhooks | Product Managers |
| 🚫 `restricted` | *(none)* | Read-only observers |

</details>

---

<details>
<summary><h2>🛡️ Enterprise Security & HIPAA Architecture</h2></summary>

Synalux is engineered for zero-trust environments.

### Arquitectura de seguridad — Flujo de solicitudes multi-tenant

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

**Perspectiva clave:** Dado que los JWT llevan claims de `workspace_id` y las políticas RLS de Postgres las leen a través de `current_setting('request.jwt.claims')`, no hay **variables de sesión del lado del servidor** ni **pools de conexión por tenant**. Esto es lo que hace a Synalux escalable horizontalmente — una ventaja crítica sobre los EHR heredados que usan modelos de conexión por sesión.

### Controles de seguridad

* **EdDSA (Ed25519) Authentication:** Static API tokens are demoted to refresh-only status. All API requests are authenticated via short-lived (15 min) JWTs signed with asymmetric cryptography.
* **Transparent Data Encryption (TDE):** All team messages, generated documents, and session histories are encrypted at rest.
* **Strict Data Minimization:** Web App transcripts live strictly in React state memory and are garbage-collected the moment a tab is closed. `localStorage` is never used for PHI.
* **MIME-Gated File Storage:** Clinical attachments are restricted by strict server-side MIME verification and served exclusively via 15-minute signed URLs with IDOR prevention.
* **Immutable Audit Logs:** Every role assignment, file download, and message deletion is permanently recorded in the `rbac_audit_log` for compliance non-repudiation. Audit rows are append-only — even database admins cannot modify historical entries.
* **HITL Safety Gate:** Dangerous tools (`terminal`, `git_tool`, `browser`) require explicit user approval via a modal dialog before execution — preventing zero-click RCE via prompt injection.
* **Fail-Closed HIPAA Mode:** If the local LLM (Ollama) is unavailable during clinical voice intake, the system refuses to open the microphone rather than silently falling back to cloud processing.
* **StaleDataBanner (Patient Safety):** If clinical data hasn't been refreshed in the current session, a banner alerts the clinician, preventing treatment decisions based on outdated information.

### Cumplimiento HIPAA Statement

| HIPAA Requirement | Synalux Implementation |
|---|---|
| **§164.312(a)(1)** Access Control | JWT-based RBAC with per-tool ACLs; RLS enforces tenant isolation at the database layer |
| **§164.312(b)** Audit Controls | Immutable `hipaa_audit_log` + `rbac_audit_log` — every PHI access is recorded with user, action, resource, and timestamp |
| **§164.312(c)(1)** Integrity | AI Sandbox (`ProposedChange`) ensures no automated writes to clinical data without clinician signature |
| **§164.312(d)** Authentication | Ed25519 asymmetric JWTs (15 min TTL); Google OAuth with MFA for clinical roles |
| **§164.312(e)(1)** Transmission Security | TLS 1.3 enforced on all endpoints; Supabase connections use SSL; no PHI in URL parameters |
| **§164.310(d)(1)** Data Encryption | AES-256 at rest (Supabase TDE); WASM Whisper for on-device transcription (PHI never transmitted) |
| **§164.308(a)(1)** Risk Analysis | Adversarial security reviews (`REVIEW_PROMPT.md`); automated output guardrails with rolling-window SSE scanning |
| **No LocalStorage** | All clinical data lives in React state (garbage-collected on tab close) or Postgres (RLS-protected). Zero browser persistence of PHI |

> **BAA Coverage:** Full HIPAA compliance with BAA requires Vercel Enterprise + Supabase Team tier. See [Infrastructure & Cloud Services](#-infrastructure--cloud-services) for pricing.

</details>

---

---

## 🚀 Primeros pasos

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
| **Vercel** | Hosting + Edge + CDN | Hobby | $0/mo | 100GB bandwidth, 100GB-hrs serverless |
| **Supabase** | PostgreSQL + Auth + RLS | Free | $0/mo | 500MB DB, 50K MAU, 1GB storage |
| **Stripe** | Payments + Subscriptions | Standard | 2.9% + 30¢/txn | No monthly fee, unlimited products |
| **Google Cloud** | Gemini AI + OAuth + Transcription | Free tier | $0/mo | 15 RPM Gemini, unlimited OAuth |
| **OpenRouter** | Multi-model LLM routing | Free models | $0/mo | Unlimited `:free` model requests |
| **GitHub** | Source control + CI/CD | Free | $0/mo | Unlimited private repos, 2000 CI min/mo |

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
│   │   └── layout.tsx        # App shell + sidebar
│   ├── src/app/patient-portal/  # 🏥 Patient Portal
│   │   └── page.tsx          # Dashboard, Documents, Appointments, Billing, Messages
│   ├── src/app/api/v1/       # REST APIs
│   │   ├── chat/route.ts     # Streaming chat (SSE)
│   │   ├── soap/route.ts     # SOAP note generation
│   │   ├── pdf/route.ts      # Server-side PDF export
│   │   ├── messages/         # Team Chat API
│   │   ├── roles/            # RBAC management
│   │   ├── billing/          # Stripe integration + checkout
│   │   └── webhooks/stripe/  # Stripe webhook handler
│   ├── src/lib/              # Auth, DB, i18n, SOAP templates
│   │   ├── stripe.ts         # Stripe Connect + Checkout + Portal
│   │   ├── db.ts             # Supabase client + user management
│   │   └── auth-options.ts   # NextAuth + Google OAuth
│   └── supabase/             # Database migrations + seed data
│       ├── seed_poc_part1.sql          # Core users/workspaces
│       ├── seed_poc_part2b_*.sql       # HR tables + clinical catalogs
│       ├── seed_poc_part2c.sql         # Cross-practice links + payers
│       ├── seed_poc_part2d.sql         # Appointments (61 records)
│       ├── seed_poc_part2e.sql         # Treatment plans (16 records)
│       ├── seed_poc_part2f.sql         # HR module (staff/credentials/reviews)
│       ├── seed_poc_part2g.sql         # Billing entries, SOAP notes, documents
│       ├── seed_poc_part2h.sql         # Portal data (messages, consents, forms)
│       └── seed_poc_part2i_*.sql       # Per-practice billing config + Stripe Connect
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
