# ✦ Synalux

**Ваша ИИ-платформа для управления медицинской практикой**

> Управляйте всей вашей медицинской практикой с одной платформы — медкарты, расписание, выставление счетов, командная коммуникация и ИИ-документация. Доступна на 12 языках. Соответствует HIPAA.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Try_It_Free-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Developer_Tools-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language / Язык / Limba:** [English](../../README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← Вернуться к английской версии](../../README.md)**

🎬 **Демо-видео скоро** — Полный рабочий процесс: пациенты, запись, заметки, выставление счетов и командный чат.

---

## 💡 Почему Synalux?

### Для Клиницистов
* **🎙️ Говорите, а не печатайте.** Диктуйте заметки сеансов, и Synalux мгновенно превращает их в структурированные SOAP-заметки — всё обрабатывается на вашем устройстве.
* **📴 Работает офлайн.** Начинайте и завершайте сеансы даже без интернета. Ваши заметки сохраняются локально и синхронизируются автоматически.
* **🛡️ ИИ, которому можно доверять.** Каждое предложение ИИ показывает сравнение до/после. Ничего не меняется без вашего подтверждения.
* **📝 Меньше бумаг.** Генерируйте FBA, BIP, отчёты — и отправляйте на электронную подпись одним кликом.

### Для Владельцев и Администраторов
* **🏥 Одна платформа для любой специальности.**
* **🌍 Международный биллинг.** Принимайте платежи в USD, CAD, GBP, EUR, AUD и NZD. Скидки за объём.
* **💳 Никогда не теряйте доход.** Неудачные платежи автоматически повторяются.
* **👥 Контролируйте кто что видит.** 15 ролей.

### Для ИТ и Соответствия
* **📴 Безопасные офлайн-сеансы.** Метки времени фиксируются на устройстве клинициста. Админы видят 🟢/🔴 индикаторы.
* **🔐 HIPAA встроен.** Таймаут 15 мин, без данных пациента в браузере, шифрование.
* **📊 89 автоматизированных тестов.**

---


## <a name="platform-modules"></a>📦 Модули платформы

Каждый модуль поддерживает многопользовательскую среду, изолирован по рабочим пространствам и соответствует требованиям HIPAA со строгим контролем доступа.

### 🏥 Клинические модули
<details>
<summary><h3>📋 Клинические записи и документация</h3></summary>

🔗 **[Подробное описание: Клинические записи и документация](../../docs_source_en/clinical_notes_documentation.md)**



| Функция | Подробности |
|---------|---------|
| **SOAP Notes** | Автоматически сгенерированы из голосовой речи с использованием специализированных шаблонов |
| **Голосовая речь** | WASM Whisper на устройстве → нулевое передача PHI в облако |
| **4 Шаблона записей** | Сессия терапии, Прогресс-нота, Начальная оценка, Заключительный справочник |
| **Документы** | Лабораторные результаты, Изображения, Согласия, Оценки, Планы лечения — все в области рабочего пространства |
| **Экспорт PDF** | Серверная рендеринг (нет утечки PHI на стороне клиента) |
| **Электронные подписи** | Интеграция с BoldSign и 7 шаблонами документов |
| **Оптическая распознавание символов (OCR)** | Сканирование документов на 30+ языках для цифровизации анкет |

</details>

<details>
<summary><h3>📴 Сеансы клиники в автономном режиме</h3></summary>

🔗 **[Подробное описание: Сеансы клиники в автономном режиме документация](../../docs_source_en/offline_first_clinical_sessions.md)**



| Функция | Подробности |
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
<summary><h3>🧪 Модуль Лабораторных Назначений и Результатов</h3></summary>

🔗 **[Подробное описание: Модуль Лабораторных Назначений и Результатов](../../docs_source_en/lab_orders_results_module.md)**



| Функция | Подробности |
|---------|---------|
| **Лабораторные Назначения** | Отслеживание заказов с поставщиками (Quest, LabCorp, внутренние), приоритет (регулярный/срочный/статус) |
| **Отслеживание Результатов** | Индивидуальные результаты тестов с диапазонами норм и флагами аномалий (низкий/высокий/критический) |
| **Категории** | Хематология, Химия, Жир, Кожные заболевания, Гормоны щелочной железы, Витамин, Инфлюенция, Коагуляция |
| **Аномальные Предупреждения** | Автоматическое выделение результатов за пределами диапазона (например, повышенный ТШС, низкий витамин D) |
| **iPLEDGE Labs** | Месячное мониторинг Accutane: CBC, CMP, панель жировых кислот, LFT с отслеживанием тренда |
| **Пре-хирургическое** | INR, PT, глюкоза, очистка A1C для зубных имплантатов и хирургических процедур |
| **Мониторинг Лекарств** | Проверки щелочной железы при SSRIs, панели жировых кислот стимуляторов, базовые панели биологий |
| **Цикл Заказа** | Заказано → Собрано → Отправлено → Получено → В процессе → Результаты получены → Проверено |
| **Интеграция с поставщиками** | Quest Diagnostics, маршрутизация заказов LabCorp (план: электронный импорт результатов) |
| **Связь с диагнозом** | Коды ICD-10 прикреплены к заказам для документации медицинской необходимости |

</details>

<details>
<summary><h3>💊 Медикаменты и рецепты Module</h3></summary>

🔗 **[Подробное описание: Медикаменты и рецепты Module документация](../../docs_source_en/medications_prescriptions_module.md)**



| Функция | Подробности |
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
<summary><h3>📊 Жизненные показатели и измерения Module</h3></summary>

🔗 **[Подробное описание: Жизненные показатели и измерения Module документация](../../docs_source_en/vitals_measurements_module.md)**



| Функция | Подробности |
|---------|---------|
| **Standard Vitals** | BP (systolic/diastolic), HR, RR, temp (with method), SpO2, weight, height, BMI |
| **Pain Scale** | 0-10 numeric pain scale per visit |
| **Pediatric Growth** | Head circumference, weight/height/BMI percentiles (WHO/CDC) |
| **PT Assessments** | ROM degrees, functional scores (Oswestry, LEFS), quad activation notes |
| **Trend Tracking** | Historical vitals per patient for trend analysis |
| **Appointment Linked** | Vitals tied to specific appointment encounters |

</details>

<details>
<summary><h3>⚠️ Аллергии и предупреждения Module</h3></summary>

🔗 **[Подробное описание: Аллергии и предупреждения Module документация](../../docs_source_en/allergies_alerts_module.md)**



| Функция | Подробности |
|---------|---------|
| **Allergen Types** | Drug, food, environmental, latex, contrast, other |
| **Severity Levels** | Mild, moderate, severe, life-threatening |
| **Reaction Tracking** | Specific reaction documentation (anaphylaxis, SJS, hives, GI upset) |
| **NKDA Support** | Explicit "No Known Drug Allergies" documentation |
| **Clinical Alerts** | Critical allergy flags (Penicillin → use clindamycin, Sulfa → SJS history) |
| **Verification** | Provider verification with date stamps |

</details>

<details>
<summary><h3>💉 Модуль Прививки и вакцинации</h3></summary>

🔗 **[Подробное описание: Прививки и вакцинация Module документация](../../docs_source_en/immunizations_module.md)**



| Функция | Подробности |
|---------|---------|
| **Отслеживание прививок** | Коды CVX, номера доз, номера партий, производители |
| **Администрирование** | Место (IM/SC/PO/IN/ID), путь (инъекция, подкожный ввод, внутрь рта, внутрь глаза, внутрь носа), провайдер, осуществляющий прививку |
| **Соответствие требованиям VIS** | Отслеживание даты подписания Информационной визы по прививкам |
| **Отчетность в реестре иммунизации** | Отслеживание подачи данных в государственный реестр иммунизации |
| **Государственный календарь прививок** | DTaP, IPV, MMR, Varicella, Hep A/B, Influenza, Tdap |
| **Пациенты с ухудшенной иммунной системой** | Особые рекомендации по прививкам для биологических пациентов |

</details>

### 🏢 Модули управления практикой
<details>
<summary><h3>💳 Счета и платежи Module</h3></summary>

🔗 **[Подробное описание: Счета и платежи Module документация](../../docs_source_en/billing_payments_module.md)**



The billing module uses **Stripe Connect** to give each practice its own independent payment processing account linked to the practice administrator.

**Per-Practice Billing Configuration:**
| Setting | Подробности |
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
<summary><h3>📅 Планирование и записи</h3></summary>

🔗 **[Подробное описание: Планирование и записи документация](../../docs_source_en/scheduling_appointments.md)**



| Функция | Подробности |
|---------|---------|
| **Appointment States** | Scheduled → Confirmed → In-Progress → Completed (+ cancelled, no-show, rescheduled) |
| **Портал для пациентов Requests** | Patients request appointments with preferred date/time → staff confirms or denies |
| **Multi-Provider** | Schedule across providers within a practice |
| **Recurring Visits** | Weekly therapy sessions, monthly check-ups, ortho adjustments |
| **Waitlist** | Waitlisted appointment requests when slots are full |
| **Reminders** | Automated appointment reminders (planned) |

</details>

<details>
<summary><h3>👥 Управление персоналом (HR) Module</h3></summary>

🔗 **[Подробное описание: Управление персоналом (HR) Module документация](../../docs_source_en/hr_staff_management_module.md)**



| Функция | Подробности |
|---------|---------|
| **Staff Profiles** | Employment type, hire date, salary/hourly rate, specialties, department tracking |
| **Credentials** | License/certification tracking with expiration alerts and renewal workflows |
| **Time Off** | Vacation, sick, CE, maternity, bereavement, jury duty — approval workflows |
| **Training** | Compliance training tracking (HIPAA, BLS, CPR) with due dates and completion status |
| **Performance Reviews** | Annual/semi-annual reviews with ratings, goals, improvement plans, and acknowledgment |
| **Onboarding** | Pending onboarding status, credential verification pipeline, training assignments |

</details>

<details>
<summary><h3>⏱️ Табели и расчет заработной платы Module</h3></summary>

🔗 **[Подробное описание: Табели и расчет заработной платы Module документация](../../docs_source_en/timesheets_payroll_module.md)**



| Функция | Подробности |
|---------|---------|
| **Auto-Generation** | Timesheets automatically generated from signed clinical session notes |
| **Non-Billable Time** | Track admin time, drive time, training, and clinic prep |
| **Approval Workflows** | Employee submission → Supervisor review → Payroll processing |
| **Payroll Export** | Export timesheets natively integrated with ADP, Gusto, and Paycom |
| **Compliance** | 40-hour overtime warnings, mandatory break tracking, PTO accrual visibility |

</details>

<details>
<summary><h3>📦 Управление запасами Module</h3></summary>

🔗 **[Подробное описание: Управление запасами Module документация](../../docs_source_en/inventory_management_module.md)**



| Функция | Подробности |
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
<summary><h3>🧾 Сводные счета (Superbills) Module</h3></summary>

🔗 **[Подробное описание: Сводные счета (Superbills) Module документация](../../docs_source_en/superbills_module.md)**



| Функция | Подробности |
|---------|---------|
| **Encounter-Based** | One superbill per visit with diagnosis + procedure codes |
| **Multi-Code** | ICD-10 diagnosis arrays + CPT/CDT procedure arrays + modifiers (-25, -59) |
| **Financial Breakdown** | Total charge, insurance billed, patient copay, adjustments |
| **Status Lifecycle** | Draft → Review → Submitted → Paid / Denied / Appealed |
| **All Specialties** | Well-child visits, implants, ortho, psychotherapy, PT rehab, derm procedures |
| **Medicare Write-offs** | Automatic adjustment tracking for Medicare contractual obligations |

</details>



<details>
<summary><h3>📋 Клинические задачи Module</h3></summary>

🔗 **[Подробное описание: Клинические задачи Module документация](../../docs_source_en/clinical_tasks_module.md)**



| Функция | Подробности |
|---------|---------|
| **Task Categories** | Lab follow-up, prior auth, scheduling, documentation, billing, call patient, refill, referral |
| **Priority Levels** | Low, normal, high, urgent |
| **Assignment** | Assigned to specific staff with due dates and completion tracking |
| **Patient Linked** | Tasks tied to specific patients for care coordination |
| **Status Tracking** | Open → In Progress → Completed / Cancelled / Deferred |
| **Audit Trail** | Created by, completed by, completed at timestamps |

</details>

### 🤝 Опыт пациентов и сотрудничество
<details>
<summary><h3>🏥 Портал для пациентов</h3></summary>

🔗 **[Подробное описание: Портал для пациентов документация](../../docs_source_en/patient_portal.md)**



A full-featured patient-facing portal with authentication, messaging, documents, appointments, and billing.

| Функция | Подробности |
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
<summary><h3>📚 Обучение пациентов Module</h3></summary>

🔗 **[Подробное описание: Обучение пациентов Module документация](../../docs_source_en/patient_education_module.md)**



| Функция | Подробности |
|---------|---------|
| **Material Catalog** | 14 education documents across all specialties |
| **Multi-Language** | English + Spanish materials available |
| **Categories** | Condition, medication, procedure, lifestyle, post-op, home exercise, safety, preventive |
| **Delivery Methods** | Printed, portal upload, email, in-person, text |
| **Acknowledgment** | Track whether patient viewed/acknowledged the material |
| **Specialty Examples** | EpiPen guide, Accutane safety, ACL rehab, CBT homework, implant post-op |

</details>

<details>
<summary><h3>🔔 Вызовы и напоминания Module</h3></summary>

🔗 **[Подробное описание: Вызовы и напоминания Module документация](../../docs_source_en/recalls_reminders_module.md)**



| Функция | Подробности |
|---------|---------|
| **Recall Types** | Hygiene, annual exam, follow-up, lab recheck, imaging, screening, vaccination, med review |
| **Status Tracking** | Due → Overdue → Scheduled → Completed → Cancelled |
| **Contact Attempts** | Track outreach attempts for overdue recalls |
| **Practice-Specific** | Dental 6-month cleanings, derm annual skin checks, Accutane monthly labs |
| **Auto-Due Dates** | Based on last completed visit |

</details>

<details>
<summary><h3>🔄 Направления и межклинический чат Module</h3></summary>

🔗 **[Подробное описание: Направления и межклинический чат Module документация](../../docs_source_en/referrals_cross_practice_chat_module.md)**



| Функция | Подробности |
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
<summary><h3>💬 Командный чат и коммуникация</h3></summary>

🔗 **[Подробное описание: Командный чат и коммуникация документация](../../docs_source_en/team_chat_communication.md)**
- [Collaborative Editor Suite](../../docs_source_en/collaborative_editors_module.md)




| Функция | Подробности |
|---------|---------|
| **Сквозное шифрование** | Обмен сообщениями команды, соответствующий HIPAA |
| **Group Video Meetings** | Scalable 6-peer mesh WebRTC HIPAA-compliant telehealth & team standups |
| **Secure Scheduling** | Authenticated RSVPs utilizing zero-PHI email layouts for calendar links |
| **Голосовые и видеозвонки** | Защищенные голосовые и видео конференци (Только для тарифа Enterprise) |
| **Обмен контекстом ИИ** | Создать план лечения → "Поделиться" → переслать в отдел биллинга |
| **Голосовые команды** | Голосовые команды → звонок, SMS, эл. почта, расписание (Pro+) |
| **Каналы** | Каналы по отделам (Клинический, Биллинг, Админ) |
| **Файловые вложения** | Делитесь документами, изображениями и клиническими данными в чате |

</details>

<details>
<summary><h3>📞 Collaboration Practice Suite</h3></summary>

| Функция | Подробности |
|---------|---------|
| **Centralized Dashboard** | Router mapping aggregate metrics efficiently. Command center isolating missed tasks natively. |
| **Video Consults (WebRTC)** | Advanced secure P2P video streaming using Twilio TURN/STUN nodes avoiding middleboxes. |
| **RLS Gating** | Implicit identity tracking eliminating server-side cross-tenant data leaks natively mapping strictly to Advanced/Pro limits. |
| **Клинические задачи** | Internal clinic reminders, approvals, and queueing isolated per workspace securely. |

</details>

### 🔐 Корпоративное администрирование
    <details>
    <summary><h3>🛡️ Безопасность и соответствие</h3></summary>

| Функция | Подробности |
|---------|---------|
| **Соответствие с HIPAA** | Полный аудиторский след с журналом BAA, архитектура готовая к BAA |
| **Строгий контроль доступа** | 11 ролей, цифровски подписанной с конкретными ограничениями доступа |
| **Изоляция данных** | Все записи изолированы по клинике (`workspace_id`) для предотвращения кросс-контamination |
| **Криптографический вход** | Короткие-lived токены (срок действия 15 минут) обеспечивают выход устаревших устройств |
| **Шифрование в покое** | Шифрование прозрачных данных (AES-256) для всех медицинских данных |
| **Неприкосновенные журналы аудита** | Независимые журналы для всех назначений ролей, доступа к файлам и действий с сообщениями |
| **Режим HIPAA Fail-Closed** | Отказывает в доступе микрофону при недоступности местной обработки (нет тихого облачного отката) |
| **Минимизация данных** | Нет кэширования браузера для PHI; конфиденциальная информация удаляется немедленно при закрытии вкладки |
</details>

<details>
<summary><h3>⚙️ Platform Administration & White-Label</h3></summary>

🔗 **[Подробное описание: Platform Administration & White-Label документация](../../docs_source_en/platform_administration_white_label.md)**



| Функция | Подробности |
|---------|---------|
| **Multi-Tenant Architecture** | Isolated workspaces with dedicated branding and configurations |
| **Dynamic Workspaces** | Practice logo, primary address, and color theming dynamically fetched via SSR |
| **Module Availability** | Platform Admins can drag-and-drop or hide modules based on the clinic specialization |
| **Employee Функция Toggling** | Override base roles with `restricted_features` JSONB arrays enforcing API blocks at runtime |
| **Screen Builders** | Per-practice ability to rename buttons, hide datagrid columns, or override standard UI copy |
| **Break-Glass Auditing** | All platform admin actions logged to HIPAA-compliant audit trails |

</details>



---


### 📸 Product Tour

| 📊 1. Patient Dashboard | 🧠 2. AI Clinical SOAP Notes | 💬 3. Secure Team Chat |
|:---:|:---:|:---:|
| <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/02_patient_dashboard.png" width="100%" alt="Patient Dashboard"> | <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/04_soap_note.png" width="100%" alt="AI SOAP Notes"> | <img src="https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/10_team_chat.png" width="100%" alt="Secure Team Chat"> |

| 💉 4. Immunizations | 📦 5. Inventory Management | 🧪 6. Lab Orders & Results |
|:---:|:---:|:---:|
| <img src="../demo/24_immunizations.png" width="100%" alt="Immunizations Module"> | <img src="../demo/25_inventory.png" width="100%" alt="Inventory Management"> | <img src="../demo/26_lab_orders.png" width="100%" alt="Lab Orders & Results"> |

| 👶 7. Pediatrics | 🐾 8. Veterinary Medicine | ❤️ 9. Vitals & Measurements |
|:---:|:---:|:---:|
| <img src="../demo/27_pediatrics.png" width="100%" alt="Pediatrics Module"> | <img src="../demo/28_veterinary.png" width="100%" alt="Veterinary Medicine"> | <img src="../demo/29_vitals.png" width="100%" alt="Vitals & Measurements"> |

| 🤖 10. Intelligent Clinical Assistant |
|:---:|
| <img src="../demo/30_intelligent_assistant.png" width="50%" alt="Intelligent Clinical Assistant"> |

| 🌍 11. Глобальная панель управления | 💱 12. Элитные финансы (Консолидация) | 🛡️ 13. Аудит соответствия |
|:---:|:---:|:---:|
| <img src="../demo/36_global_dash.png" width="100%" alt="Global Dash"> | <img src="../demo/37_cross_border_finance.png" width="100%" alt="Elite Finance"> | <img src="../demo/38_compliance_audit.png" width="100%" alt="Compliance Audit"> |

| 📍 14. Управление филиалами |
|:---:|
| <img src="../demo/39_branch_isolation.png" width="50%" alt="Branch Manager"> |

## 🏥 Synalux Health: Клиническое веб-приложение

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

## 🧑‍💻 Synalux Dev: Расширение VS Code

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
<summary><h2>🛡️ Экспертиза безопасности и архитектура HIPAA</h2></summary>

Synalux проектирован для сред без доверия.

### Архитектура безопасности — Поток мультитенантных запросов

```
┌─────────────────┐     ┌──────────────────────────────┐     ┌──────────────────────────────┐     ┌─────────────────────────────┐
│   Клиент        │     │   Vercel Edge (Middleware)    │     │   Next.js API Routes         │     │   Supabase PostgreSQL       │
│                 │     │                              │     │                              │     │                             │
│  Браузер /      │────▶│  1. Проверка аутентификации (NextAuth)    │────▶│  3. Ограничение доступа к инструментам (ACL)     │────▶│  6. Политики RLS            │
│  VS Code        │     │  2. Подпись JWT (Ed25519)    │     │  4. AI Sandbox               │     │     (JWT → set_config)      │
│                 │     │     (срок действия 15 минут)             │     │     (ProposedChange)         │     │  7. Многотенантные данные       │
│                 │     │                              │     │  5. Журнал аудита HIPAA          │     │     (изоляция workspace_id) │
└─────────────────┘     └──────────────────────────────┘     └──────────────────────────────┘     └─────────────────────────────┘
                              Google OAuth                    Отредактированный контекст инструмента                   Фильтры RLS по workspace_id
```

**Ключевой вывод:** JWT несут claims `workspace_id`, а политики RLS Postgres читают их через `current_setting('request.jwt.claims')`, поэтому нет **серверных переменных сессии** и **пулов соединений на тенант**. Это делает Synalux горизонтально масштабируемым.

### Контроль безопасности

* **Аутентификация EdDSA (Ed25519):** Статические API-токены демoted to refresh-only status. Все запросы к API аутентифицируются через короткие-lived (15 минут) JWTs, подписанные с использованием асимметричной криптографии.
* **Прозрачная шифрование данных (TDE):** Все сообщения командной работы, документы и история сессий шифруются при хранении.
* **Строгое минимизация данных:** Транскрипты веб-приложения существуют только в памяти React state и удаляются при закрытии вкладки. `localStorage` никогда не используется для PHI.
* **Хранение файлов с ограничением MIME:** Клинические вложения ограничены строгой проверкой MIME на сервере и предоставляются исключительно через 15-минутные подписанную URL с предотвращением IDOR.
* **Непрерывный журнал аудита:** Все назначения ролей, скачивания файлов и удаление сообщений записываются в `rbac_audit_log` для обеспечения непререкаемости соответствия. Записи журнала аудита добавляются только в конец — даже администраторы базы данных не могут изменять исторические записи.
* **Шлюз безопасности HITL:** Дамагинги (`terminal`, `git_tool`, `browser`) требуют явного одобрения пользователя через модальное диалоговое окно перед выполнением — предотвращая нажатие кнопки для удаленного кода с использованием подделки запросов.
* **Fail-Closed режим HIPAA:** Если локальный LLM (Ollama) недоступен во время приема голосовых данных, система отклоняет доступ к микрофону вместо того, чтобы тихо переключаться на обработку в облаке.
* **Баннер с устаревшими данными (безопасность пациентов):** Если клинические данные не были обновлены в текущей сессии, баннер предупреждает врача, что предотвращает принятие решений о лечении на основе устаревших данных.

### Соответствие требованиям HIPAA

| Требование HIPAA | Реализация Synalux |
|---|---|
| **§164.312(a)(1)** Управление доступом | RBAC на основе JWT с ограничениями ACL по инструментам; RLS обеспечивает изоляцию тенантов на уровне базы данных |
| **§164.312(b)** Журнал аудита | Непрерывный `hipaa_audit_log` + `rbac_audit_log` — каждый доступ к PHI записывается с именем пользователя, действием, ресурсом и временем戳 |
| **§164.312(c)(1)** Целостность | AI Sandbox (`ProposedChange`) гарантирует, что нет автоматических изменений в клинических данных без подписи врача |
| **§164.312(d)** Аутентификация | JWT асимметричной криптографии (срок действия 15 минут); Google OAuth с MFA для медицинских ролей |
| **§164.312(e)(1)** Безопасность передачи данных | TLS 1.3 на всех концах; подключения Supabase используют SSL; нет PHI в параметрах URL |
| **§164.308(a)(1)** Анализ рисков | Адversarial security reviews (`REVIEW_PROMPT.md`); автоматические контрольные линии с использованием сканирования SSE с окном прокрутки |
| Нет `localStorage` | Все клинические данные существуют в React state (удаляются при закрытии вкладки) или Postgres (защищены RLS). Нет хранения PHI в браузере |

> **Область применения BAA:** Полная соответствия HIPAA с использованием BAA требует Vercel Enterprise и уровня команды Supabase. Подробнее см. [Инфраструктура и облачные услуги](#platform-modules) для цен.

</details>

---

---

## 🚀 Начало работы

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
<a name="platform-modules"></a>
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

### 🧠 Model Routing & Tier Architecture

The server automatically routes each request to the best model for the user's subscription tier. All Synalux products (Portal, PrismAAC, Prism Coder) use the same `/api/v1/chat` endpoint.

- **Free:** Gemini 2.5 Flash
- **Standard:** Claude Sonnet 4 (fallback: Gemini 2.5 Flash)
- **Advanced:** Claude Sonnet 4 (fallback: Gemini 2.5 Flash)
- **Enterprise:** Claude Opus 4 (fallback: Gemini 2.5 Flash)

<details>
<summary>Click to view full details</summary>

| Tier | Default Model | Fallback | Max Tokens | Daily Limit |
|------|--------------|----------|------------|-------------|
| **Free** | Gemini 2.5 Flash | — | 4,096 | 100 |
| **Standard** | Claude Sonnet 4 | Gemini 2.5 Flash | 8,192 | 2,000 |
| **Advanced** | Claude Sonnet 4 | Gemini 2.5 Flash | 16,384 | 5,000 |
| **Enterprise** | Claude Opus 4 | Gemini 2.5 Flash | 32,768 | Unlimited |

**Products using this routing:**
- ✅ **Synalux Portal** — web app chat, FloatChat, SOAP dictation
- ✅ **PrismAAC** — AI Chat for AAC users, caregiver note parsing (`source: prism-aac`)
- ✅ **Prism Coder IDE** — coding assistant
- ✅ **VS Code Extension** — inline coding

**Offline fallback:** All products fall back to `prism-coder:7b` via local Ollama when the API is unreachable.

**Server-side enforcement:** Even if a client sends a model ID, the server validates it against `TIER_ALLOWED_MODELS`. A free-tier user requesting `claude-sonnet-4` will be silently downgraded to their tier default.
</details>

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

The portal, documentation, and AI interface are available in 16 languages:

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
