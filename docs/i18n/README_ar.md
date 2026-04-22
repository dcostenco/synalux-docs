# ✦ Synalux

**منصتك لإدارة العيادة بالذكاء الاصطناعي**

> أدِر ممارستك الطبية بالكامل من منصة واحدة — سجلات المرضى، المواعيد، الفوترة، التواصل مع الفريق والتوثيق بالذكاء الاصطناعي. متوفر بـ 12 لغة. متوافق مع HIPAA.

<p align="center">
  <a href="https://synalux.ai/app"><img src="https://img.shields.io/badge/Web_App-Try_It_Free-43e97b?style=for-the-badge" alt="Web App"></a>
  <a href="https://marketplace.visualstudio.com/items?itemName=synalux-ai.synalux"><img src="https://img.shields.io/badge/VS_Code-Developer_Tools-764ba2?style=for-the-badge" alt="VS Code"></a>
  <a href="https://synalux.ai/docs"><img src="https://img.shields.io/badge/Compliance-HIPAA_Ready-blue?style=for-the-badge" alt="HIPAA"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-BSL--1.1-yellow?style=for-the-badge" alt="License"></a>
</p>

🌐 **Language / Язык / Limba:** [English](../../README.md) · [Español](README_es.md) · [Français](README_fr.md) · [Português](README_pt.md) · [Română](README_ro.md) · [Українська](README_uk.md) · [Русский](README_ru.md) · [Deutsch](README_de.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [中文](README_zh.md) · [العربية](README_ar.md)

📌 **[← العودة إلى النسخة الإنجليزية](../../README.md)**

🎬 **فيديوهات توضيحية قريباً** — شاهد سير العمل الكامل: المرضى، المواعيد، الملاحظات، الفواتير ودردشة الفريق.

---

## 💡 لماذا Synalux؟

### للأطباء والمعالجين
* **🎙️ تحدث، لا تكتب.** أملِ ملاحظات الجلسة وسيحولها Synalux فوراً إلى ملاحظات SOAP منظمة — كل المعالجة تتم على جهازك.
* **📴 يعمل بدون إنترنت.** ابدأ وأنهِ الجلسات حتى بدون اتصال. ملاحظاتك تُحفظ محلياً وتُزامن تلقائياً عند استعادة الاتصال.
* **🛡️ ذكاء اصطناعي موثوق.** كل اقتراح من الذكاء الاصطناعي يُظهر مقارنة قبل/بعد. لا شيء يتغير في سجل المريض حتى توافق صراحةً.
* **📝 أوراق أقل.** أنشئ FBA وBIP وتقارير التقدم — ثم أرسل للتوقيع الإلكتروني بنقرة واحدة.

### لأصحاب العيادات والمديرين
* **🏥 منصة واحدة لأي تخصص.**
* **🌍 فوترة دولية.** اقبل المدفوعات بـ USD وCAD وGBP وEUR وAUD وNZD. خصومات الحجم التلقائية.
* **💳 لا تخسر إيرادات أبداً.** المدفوعات الفاشلة تُعاد تلقائياً.
* **👥 تحكم في من يرى ماذا.** 15 دوراً.

### لتقنية المعلومات والامتثال
* **📴 جلسات آمنة بدون اتصال.** الطوابع الزمنية تُسجل على جهاز الطبيب. يرى المديرون مؤشرات 🟢/🔴.
* **🔐 HIPAA مدمج.** مهلة 15 دقيقة، بدون بيانات مرضى في المتصفح، تشفير.
* **📊 89 اختباراً آلياً.**

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

## 📦 Platform Modules

Every module is multi-tenant, workspace-scoped, and HIPAA-compliant with strict role-based access.

### 🏥 Clinical Care Modules
<details>
<summary><h3>📋 الملاحظات الطبية والوثائق</h3></summary>

🔗 **[قراءة ملخصات المرضى وتوثيقها التفصيلية](../../docs_source_en/clinical_notes_documentation.md)**



| الميزة | التفاصيل |
|---------|---------|
| **ملخصات SOAP** | تلقائية من التحدث الصوتي باستخدام نماذج متخصصة حسب التخصص |
| **التحدث الصوتي** | WASM Whisper على الجهاز → لا إرسال PHI إلى السحابة |
| **4 نماذج ملاحظات** | جلسة العلاج، المراجعة، تقييم الأولية، خلاصة الإخراج |
| ** الوثائق** | النتائج الطبية، الصور، الموافقات، التقييمات، خطط العلاج — جميعًا في نطاق العمل |
| تصدير PDF | تقديم الخدمة (بدون تسرب PHI من جانب العميل) |
| التوقيع الإلكتروني | دمج BoldSign مع 7 نماذج وثيقة |
| OCR | مسح الوثائق في أكثر من 30 لغة للتحويل الرقمي للأشكال الإدخالية |

</details>

<details>
<summary><h3>📴 جلسات طبية متعددة الأغراض دون اتصال بالإنترنت</h3></summary>

🔗 **[قراءة وثائق جلسات طبية متعددة الأغراض دون اتصال بالإنترنت التفصيلية](../../docs_source_en/offline_first_clinical_sessions.md)**



| الميزة | التفاصيل |
|---------|---------|
| **التوقيتات الزمنية على الجانب العميل** | يتم التقاط أوقات البدء/النهاية للجلسة على جهاز مقدم الخدمة — تُستخدم للاستهلاك، وليس وقت استلام السرور |
| **المشطّق غير متصل** | الأحداث معلقة في localStorage عند عدم الاتصال بالإنترنت، يتم المزامنة تلقائياً عند إعادة الاتصال |
| **الاحتفاظ بالأمانة المسودة** | يتم حفظ الملاحظات الطبية تلقائيًا إلى localStorage بكل زر الضغط — تبقى على بعد من انهيار المتصفح أو فقدان الاتصال |
| **توقيع الجلسة** | يجب أن يوقع مقدم الخدمة توقيع الجلسة عند انتهاء الجلسة — يتم التوقيت الزمني كنهاية الدفع الدقيق |
| **مراجعة الإدارة** | يظهر كل حدث مؤشرًا أخضرًا / أحمرًا للانترنت مع وقت المزامنة |
| **مراقبة الاتصال** | يعرض الجانب الأيمن الحالة في الوقت الحقيقي أخضرًا / أحمرًا مع علامة التبويب لعد عدد المزامن غير المكتملة |
| **تنظيف البيانات حسب سياسة HIPAA** | يتم تنظيف جميع البيانات المحلية عند تسجيل الخروج والوقت الهامش للعدالة |
| **مزامنة متطابقة** | تُمنع حدوث الأحداث المكررة عبر UUIDs مولد بواسطة العميل |
| ** Phátشيرة الزمنية** | يسجل السرور الفرق بين أوقات الزمان على الجانب العميل والسرور للاستهلاك |
| **حياة الجلسة** | `session_start` → `session_pause` → `session_resume` → `session_end` |

**الامتثال للدفعة:**
```
يبدأ مقدم الخدمة جلسة في الساعة 2:00 مساءً (متصل بالإنترنت) → 🟢
  يفقد الاتصال في الساعة 2:30 مساءً
ينتهي مقدم الخدمة الجلسة في الساعة 3:45 مساءً (غير متصل بالإنترنت) → 🔴 client_timestamp = 3:45 مساءً
  يعيد الاتصال في الساعة 4:00 مساءً → المزامنة تلقائية
سجل السرور: client_timestamp = 3:45 مساءً، sync_timestamp = 4:00 مساءً
  ↓
تم الدفع للتأمين: الجلسة من الساعة 2:00 مساءً إلى 3:45 مساءً (دقيق)
إدارة ترى: "جلسة انتهت في الساعة 3:45 مساءً 🔴 غير متصل (مزامنة في الساعة 4:00 مساءً)"
```

</details>

<details>
<summary><h3>🧪 ماژول الطلبات والنتائج الطبية</h3></summary>

🔗 **[قراءة وثائق مفصلة حول ماژول الطلبات والنتائج الطبية](../../docs_source_en/lab_orders_results_module.md)**



| الميزة | التفاصيل |
|---------|---------|
| **طلبات البحوث** | تتبع الطلبات مع الموردين (Quest، LabCorp، داخلية)، الأولوية (عادية/عاجلة/في حالة الطوارئ) |
| **تتبع النتائج** | نتائج الاختبارات الفردية مع نطاقات المرجع والعلامات الإشارة إلى الحالات غير العادية (منخفضة/مرتفعة/خطيرة) |
| **الأقسام** | الدم، الكيمياء، الدهون، الكلى، الغدة الدرقية، فيتامينات، التورم، الدورة الدموية |
| **التحذيرات عن الحالات غير العادية** | تلخيص تلقائي للنتائج خارج النطاق (مثل TSH المتصاعد، ضعف في فيتامين D) |
| **iPLEDGE Labs** | مراقبة شهرية لـ Accutane: CBC، CMP، لوحة الدهون، LFTs مع تتبع التطور |
| **قبل الجراحات** | INR، PT، السكر، تخلص A1C للتركيبات الفاسدة والعمليات الجراحية |
| **رصد الأدوية** | فحوصات الغدة الدرقية للأدوية المثابة، لوحة الدهون المضادة للنشاط، لوحة الأساس البيولوجيا |
| ** 生命周期 الطلبات** | تم طلبها → تم جمعها → تم إرسالها → تم استلامها → في التقدم → تم النتائج → تم مراجعتها |
| **تكامل الموردين** | Quest Diagnostics، توجيه الطلبات لـ LabCorp (خطة: الاستيراد الإلكتروني للنتائج) |
| **ربط التشخيصات** | ربط كودي ICD-10 بالطلبات لإثبات الضرورية الطبية |

</details>

<details>
<summary><h3>💊 المواد والأدوية والوصفات الطبية</h3></summary>

🔗 **[قراءة وثائق الوحدة المختصرة للمواد والأدوية والوصفات الطبية](../../docs_source_en/medications_prescriptions_module.md)**



| الميزة | التفاصيل |
|---------|---------|
| **كتالوج الأدوية** | 12+ أدوية مع رموز NDC، فئات الأدوية، الجداول الزمنية، الطرق، الجرعات الشائعة |
| **الوصفات الطبية النشطة** | قائمة الأدوية لكل مريض مع الجرعات، التكرار، المدرب، الصيدلي، تتبع تعبئة |
| **فئات الأدوية** | SSRIs، استيمايلانتس، ريتينوئودز، بيوولوجيكالز، برونكوديلاتورز، NSAIDs، أكسجينات، مضادات الفيروسات، مضادات الديدان |
| **رصد iPLEDGE** | مراقبة isotretinoin Accutane مع متطلبات المختبر الشهرية |
| ** 生命周期 الحالة** | نشط → على الإيقاف → تم إلغاؤه → اكتمال → تم إلغاء |
| **تحذيرات التفاعلات** | مصفوفة تحذيرات خاصة بالأدوية (синروز السرور، QTc، تراتوجين) |
| **توجيه الصيدليات** | صيدلية معروفة لكل وصفة للتحضير الإلكتروني |

</details>

<details>
<summary><h3>📊 وحدة الإحصاءات الأساسية والقياسات</h3></summary>

🔗 **[قراءة الوثائق المفصلة لمودعة الإحصاءات الأساسية والقياسات](../../docs_source_en/vitals_measurements_module.md)**



| الميزة | التفاصيل |
|---------|---------|
| **الإحصاءات الأساسية** | ضغط الدم (الضغط العالي/الضغط المنخفض)، معدل القلب، معدل التنفس، درجة الحرارة (مع الطريقة)، تركيز الأكسجين في الدم، الوزن، الارتفاع، مؤشر الجسم السمني |
| **مقياس الألم** | مقياس رقمي للألم من 0 إلى 10 لكل زيارة |
| **نمو الأطفال** | دائرة الرأس، وزن/طول/مؤشر الجسم السمني (WHO/CDC) |
| **تقييمات القدرة البدنية للأطفال (PT)** | درجة حرية الحركة، نتائج الاختبارات الفعلية (أوستروستري، LEFS)، ملاحظات حول النشاط الكلي |
| تتبع التطور | الإحصاءات التاريخية للمرضى لتحليل التطور |
| المرتبطة بالمواعيد المجدولة | الإحصاءات مرتبطة بمواقف معينة من المواعيد المجدولة |

</details>

<details>
<summary><h3>⚠️ مايالجات وتنبيهات المرضية</h3></summary>

🔗 **[قراءة مستندات مايالجات وتنبيهات المرضية التفصيلية](../../docs_source_en/allergies_alerts_module.md)**



| الميزانية | التفاصيل |
|---------|---------|
| **أنواع مايالجات** | الدواء، الغذاء، البيئة، اللوتين، مقارنة، آخر |
| **مستويات الخطورة** | ضعيفة، متوسطة، خطيرة، مهددة بالحياة |
| تتبع التفاعلات | وثائق تفاعل محددة (الانفجار، SJS، البقع، عدم استقرار الجهاز الهضمي) |
| دعم NKDA | وثيقة صريحة "لا ماياليجات للدواء المعروفة" |
| تنبيهات طبية | علامات الخطورة الحرجة (البنتاميسين → استخدام الكلينامسيوم، السولفا → تاريخ SJS) |
| التحقق | التحقق من المقدم مع أشارات التاريخ |

</details>

<details>
<summary><h3>💉 Module التطعيمات</h3></summary>

🔗 **[قراءة وثائق المودуль التطعيمات التفصيلية](../../docs_source_en/immunizations_module.md)**



| الميزة | التفاصيل |
|---------|---------|
| **رصد التطعيمات** | كودات CVX، أرقام الجرعة، أرقام اللوت، الشركات المصنعة |
| **التطبيق** | الموقع، المسار (IM/SC/PO/IN/ID)، مقدم التطعيم |
| **امتثال لـ VIS** | تتبع تاريخ تلقي بيان المعلومات عن التطعيم |
| **تقرير السجلات** | تتبع تسجيل التسليم للسجلات المركزية للتطعيمات في الولايات المتحدة |
| **جدول CDC** | DTaP، IPV، MMR، Varicella، Hep A/B، Influenza، Tdap |
| **المصابين المناعيين** | توصيات خاصة بالتطعيمات للمرضى المرضي الجلدي |

</details>

### 🏢 Practice Operations Modules
<details>
<summary><h3>💳 وحدة الدفع والدفعات</h3></summary>

🔗 **[قراءة الوثائق التفصيلية لوحدة الدفع والدفعات](../../docs_source_en/billing_payments_module.md)**



وحدة الدفع تستخدم **Stripe Connect** لمنح كل مكتب حساب معالجة الدفع المستقل الخاص به المرتبط بمدير المكتب.

**تكوين الدفعات لكل مكتب:**
| الإعداد | التفاصيل |
|---------|---------|
| **Stripe Connect** | يتم توفير حساب Stripe Connect مستقل لكل ورقة عمل `acct_xxx` |
| **المشرف متصل** | ترتبط صاحبة حساب Stripe بمدير المكتب |
| **جدول الرسوم** | جدولًا مرنًا للرسوم لكل مكتب مع أسعار الضرائب، التأمين الصحي، الصحة الاجتماعية، والدفع الذاتي |
| **وسائل الدفع** | البطاقة الائتمانية، ACH/تحويل البنك، فاتورة، النقود — قابل للتكوين لكل مكتب |
| **التسجيلات الآلية** | تسجيل الدفعات الآلية، إرسال الفواتير، وتصنيف التقارير الشهرية |
| **تكوين الضرائب** | معدلات الضرائب المرنة لكل مكتب ومعرفة NPI/EIN للحصول على تقرير 1099 |

**دول العملات والبلدان (جديد):**

| البلد | العملة | المبسط | المتقدم | الأعمال |
|---------|----------|----------|----------|------------|
| 🇺🇸 الولايات المتحدة الأمريكية | دولار أمريكي | $19/شهرياً | $49/شهرياً | $99/شهرياً |
| 🇨🇦 كندا | دولار كاندي | C$25/شهرياً | C$65/شهرياً | C$129/شهرياً |
| 🇬🇧 المملكة المتحدة | جنيه إسترليني | £15/شهرياً | £39/شهرياً | £79/شهرياً |
| 🇩🇪فرنسا الاتحاد الأوروبي | اليورو | €18/شهرياً | €45/شهرياً | €89/شهرياً |
| 🇦🇺 أستراليا | دولار أسترالي | A$29/شهرياً | A$75/شهرياً | A$149/شهرياً |
| 🇳🇿 نيوزيلندا | دولار نيوزيلندي | NZD $32/شهرياً | NZD $82/شهرياً | NZD $159/شهرياً |

**خصومات حجم العملاء:**
| عدد العملاء | الخصم |
|---------|----------|
| 100+ | خصم 10% من سعر مقعد كل عملاء |
| 500+ | خصم 20% من سعر مقعد كل عملاء |
| 1,000+ | خصم 30% من سعر مقعد كل عملاء |
| الدفع السنوي | خصم إضافي بنسبة 20% (تطابق مع الخصومات حجم العملاء، محدود بـ 45%) |

**الحياة المدفوعة لفشل الدفع:**
```
فشل الدفع → past_due (شريط تحذير، تظل الوصول)
  → إعادة المحاولة الثانية → لا تزال past_due (تحذير فوري)
  → الطلب الثالث لم ينجح → التراجع إلى مستوى المجانية
  → تم إلغاء الاشتراك في Stripe → plan = 'مجانية' ، sub مسحوق
```

**تجاوزات إدارة المنصة:**
- يمكن لمسؤولي المنصة Synalux تعيين أي مستخدم على الاختبار غير المحدود لأي خطة
- يتمتع المستخدمون الذين تم تجاوزهم بـ **الجاذبية** للتحديثات التلقائية من Stripe
- يرى المسؤول معلومات الألوان الأخضر/الأحمر عن حالة الدفع
- سجل كامل للمراجعة: من قام بتغيير الجازب، متى وراء ذلك، وما هو السبب

**إدارة دورة الإيرادات:**
- تتبع حياة طلب التأمين الصحي (مسودة → مقدم → مقبولة → مدفوع/مرفوض → مطالبة)
- معالجة الطلب الإلكتروني للتأمين (837P)
- التحقق الفوري من الملاءمة
- ترتيب الأمانات (COB)
- تتبع شروط الاسترداد (EOB)
- إدارة المطالبات مع نماذج البريد الإلكتروني

**التقاط الضريبة الآلية:**
- تمكين Stripe Tax لكل بلد (ضريبة القيمة المضافة، ضريبة السلع والخدمات، ضريبة الهيئة العامة، ضريبة الولاية)
- يتم حساب الضريبة تلقائيًا بناءً على البلد الذي يقع فيه العملة
- متوافق مع قواعد الضريبة المتعددة المناطق في كندا (ضريبة الفيدرالية + ضريبة الولاية / الهيئة العامة)

</details>

<details>
<summary><h3>📅 التخطيط والمواعيد</h3></summary>

🔗 **[قراءة وثائق التخطيط والمواعيد المفصلة](../../docs_source_en/scheduling_appointments.md)**



| الميزة | التفاصيل |
|---------|---------|
| **حالة الموعد** | مُحَدّث → مؤكَّد → في التقدم → مكتمل (+ ملغى، لم يحضر، مجدول) |
| **طلبات لوحة المرضى** | تطلب المرضى مواعيد مع تاريخ/وقت مفضل → يقوم الموظف بإقرارها أو رفضها |
| **متعددة الأطباء** | التخطيط عبر عدة أطباء في نفس المكتب |
| **زيارة متكررة** | جلسات العلاج الأسبوعية، زيارات الشهر، تعديلات الأسنان |
| **القائمة الانتظار** | طلبات المواعيد المرتبطة بالقائمة الانتظار عند عدم توفر الفراغات |
| **التذكيرات** | تذكيرات مواعيد مُحَدّثة تلقائيًا (مخطط) |

</details>

<details>
<summary><h3>👥 إدارة الأشخاص والموظفين</h3></summary>

🔗 **[قراءة وثائق إدارة الأشخاص والموظفين المفصلة](../../docs_source_en/hr_staff_management_module.md)**



| الميزة | التفاصيل |
|---------|---------|
| **الملفات الشخصية للموظفين** | نوع العمل، تاريخ التوظيف، الأجور/سعر الساعة، المتخصصات، تتبع القسم |
| **المؤهلات** | تتبع المؤهلات والشهادات مع تنبيهات الانتهاء وتدفق العمليات لتحديث |
| **الراحة عن العمل** | الإجازات السنوية، الأمراض، CE، الحمل، التوفيق، قضية المحكمة — عمليات الموافقة |
| **التدريب** | تتبع تدريب الامتثال (HIPAA، BLS، CPR) مع مواعيد الانتهاء والحالة المكتملة |
| **التقييمات السنوية** | التقييمات السنوية/نصف سنويًا مع التقييمات، الأهداف، خطة التحسين، وتأكيد |
| **الانضمام إلى العمل** | حالة الانضمام المعلقة، خطط تحقق المؤهلات، مهام التدريب |

</details>

<details>
<summary><h3>⏱️ ورقة العمل الزمنية والرواتب</h3></summary>

🔗 **[قراءة الوثائق التفصيلية للوحدة الزمنية والرواتب](../../docs_source_en/timesheets_payroll_module.md)**



| الميزة | التفاصيل |
|---------|---------|
| **توليد تلقائي** | ورقة العمل الزمنية تولد تلقائياً من ملاحظات الجلسة الطبية الموقعة |
| **الوقت غير المدفوع** | تتبع الوقت للإدارة، السفر، التدريب، والتحضير للمستشفى |
| **تدفق الموافقات** | تقديم الموظف → مراجعة المشرف → معالجة الرواتب |
| **تصدير الرواتب** | تصدير ورقة العمل الزمنية مدمجًا بسهولة مع ADP و Gusto و Paycom |
| **امتثال القوانين واللوائح** | تحذيرات للعمل الإضافي لمدة 40 ساعة، تتبع الزروات الضرورية، إظهار التجميع للموافقة على أجازة مدفوعة (pto) |

</details>

<details>
<summary><h3>📦 إدارة المخزون</h3></summary>

🔗 **[قراءة وثائق إدارة المخزون التفصيلية](../../docs_source_en/inventory_management_module.md)**



| الميزانية | التفاصيل |
|---------|---------|
| **الأقسام** | المواد الطبية، اللقاحات، الأدوية، البلاجيك، ملابس الأمان، الجراحية، المواد المختبرية، المكتب |
| **رصد الأسهم** | الكمية المتاحة، مستوى إعادة الشراء، كمية إعادة الشراء،تكلفة الوحدة |
| **الجملة وموعد الانتهاء** | أرقام الجملة، مواعيد الانتهاء، ترتيب FIFO لللقاحات |
| **رصد الموردين** | هنري شيشين، باترسترن دنتال، نوبل بايوكار، مكسيشن، سانوفي فاستير |
| **تحذيرات الحالة** | في المخزن، كمية صغيرة، خالية من المخزن، انتهت الصلاحية، تم إيقاف البيع |
| **مواقع التخزين** | الثلاجة لللقاحات (2-8°C)، الثلاجة البلاجيكية، مصنفات العاملين، الخزانات المغلقة |
| **العناصر المتخصصة** | أثاث الأسنان ($285)، بلاجيكات الأقراص البيولوجية ($2,850)، قناعات الكريوثربي (البرد) |

</details>

<details>
<summary><h3>🧾 ماژول الفواتير المتميزة</h3></summary>

🔗 **[قراءة وثائق ماژول الفواتير المتميزة التفصيلية](../../docs_source_en/superbills_module.md)**



| الميزانية | التفاصيل |
|---------|---------|
| **وفقا للزيارة** | فاتورة واحدة لكل زيارة مع رموز التشخيص والإجراءات |
| **متعددة الرموز** | مصفوفة التشخيصات ICD-10 + مصفوفة الإجراءات CPT/CDT + المعدلات (-25، -59) |
| **تحليل التكاليف** | إجمالي الطلب، ما تم تغطينه من قبل التأمين الصحي، دفع المريض، التعديلات |
| ** жизنية الحالة** | المسودة → مراجعة → مقدم → مدفوع / رفض / طلب إعادة النظر |
| **جميع التخصصات** | زيارات الأطفال الصحية، الإطلاعات، العظام والأنسجة، العلاج النفسي، تدريب اليوغا، إجراءات الجلدية |
| **الخصومات لتأمين الرعاية الاجتماعية للمساهمين في الصحة (CMS)** | تتبع التحديثات الآتية تلقائياً لتزام CMS |

</details>



<details>
<summary><h3>📋 مódulo المهام الطبية</h3></summary>

🔗 **[قراءة وثائق المهام الطبية التفصيلية](../../docs_source_en/clinical_tasks_module.md)**



| الميزة | التفاصيل |
|---------|---------|
| **فئات المهام** | التتبع في المختبر، الموافقة السابقة، الجدولة، الوثيقة، الفواتير، الاتصال بالمرضى، إعادة تعبئة الأدوية، الإشارة |
| **مستويات الأولوية** | منخفضة، عادية، عالية، طارئة |
| **التعيين** | مكلف على موظفين معينة لديهم أموال ورصد إنجاز المهام |
| **ال Liên kết بالمرضى** | المهام مرتبطة بمرضى معينين لتنسيق الرعاية الصحية |
| **رصد حالة** | مفتوحة → في التقدم → مكتملة / تم الإلغاء / المؤجلة |
| **سجل الامتحانات** | من قبل، مكتمل بواسطة، أوقات مكتملة |

</details>

### 🤝 Patient Experience & Collaboration
<details>
<summary><h3>🏥 بوابة المرضى</h3></summary>

🔗 **[قراءة وثائق بوابة المرضى التفصيلية](../../docs_source_en/patient_portal.md)**



بوابة متكاملة للمرضى مع تحقق الهوية، الرسائل، الوثائق، المواعيد، والدفقات المالية.

| الميزة | التفاصيل |
|---------|---------|
| **التحقق من الهوية** | تسجيل الدخول باستخدام رمز الوصول (تم تشفيره باستخدام SHA-256)، تتبع الصلاحيات |
| **اللوحة الرئيسية** | ملخص صحتك مع المواعيد القادمة، الرسائل غير المقروءة، الوثائق المعلقة، المبلغ المستحق |
| **الرسائل** | المناقشات المتسلسلة مع الأطباء، علامات الطوارئ، إيصالات القراءة |
| **الوثائق** | معاينة/تحميل الوثائق الطبية، تحميل بطاقات التأمين الصحي والأشكال |
| **المواعيد** | مراجعة المواعيد القادمة وال السابقة، طلب مواعيد جديدة مع الوقت المفضل |
| **الدفقات المالية** | مراجعة المبلغ المستحق، تاريخ الدفعات المالية مع رموز CPT، دفع عبر الإنترنت باستخدام ستريت، خطط الدفع، إيصالات |
| **الأشكال** | إكمال شروط القبول، استبيانات PHQ-9/GAD-7، تحميل شروط القبول عبر الإنترنت |
| **الموافقة على الشروط والأحكام** | إدارة الموافقة الرقمية (علاج، HIPAA، الرعاية عن بعد، الأدوية، البحث) |

</details>

<details>
<summary><h3>📚 مódulo تعليم المرضى</h3></summary>

🔗 **[قراءة وثائق التعليم للمرضى بالتفصيل](../../docs_source_en/patient_education_module.md)**



| الميزة | التفاصيل |
|---------|---------|
| **كتالوج المواد** | 14 وثيقة تعليمية عبر جميع التخصصات |
| **اللغات متعددة** | المواد المتاحة باللغتين الإنجليزية والبرتغالية |
| **الأقسام** | حالة، دواء، عملية، الحياة اليومية، بعد الجراحة، تمارين المنزل، السلامة، الوقاية |
| **طرق التوزيع** | طباعة، تحميل على المنصة، البريد الإلكتروني، مقابل الشخص، النص |
| **الموافقة** | تتبع ما إذا كان المريض قد قرأ أو أقر المواد |
| **أمثلة التخصصات** | دليل EpiPen، أمان Accutane، تدريب ACL، مهام CBT، بعد الجراحة للتركيب |

</details>

<details>
<summary><h3>🔔 مódulo المذكوزات وال提醒ات</h3></summary>

🔗 **[قراءة وثائق المودعة المفصلة والمذكرات](../../docs_source_en/recalls_reminders_module.md)**



| الميزانية | التفاصيل |
|---------|---------|
| **أنواع المذكوزات** | النظافة، الفحص السنوي، متابعة، إعادة فحص laboratorio، الرسوم البيانية، الاختبارات، التطعيمات، تقييم الأدوية |
| تتبع الحالة | يجب الانتهاء → متأخر → مجدول → اكتمال → تم الإلغاء |
| محاولات الاتصال | تتبع محاولات الاتصال للذكوز المتأخرة |
| محددة للمستشفي | النظافة السنوية لليأس، فحص الجلد السنوي للجلدية، تحليل Accutane الشهري |
| تاريخ الانتهاء التلقائي | بناءً على آخر زيارة اكتملت |

</details>

<details>
<summary><h3>🔄 مايادى الارجاعات ومحادثة بين الممارسات</h3></summary>

🔗 **[قراءة مستندات مفصلة حول مايادى الارجاعات ومحادثة بين الممارسات](../../docs_source_en/referrals_cross_practice_chat_module.md)**



| الميزانية | التفاصيل |
|---------|---------|
| **متابعة الارجاع** | من/إلى مقدم الخدمة، التخصص، السبب، الرموز التشخيصية، الأولوية، تتبع الموافقة |
| ** 生命周期 الحالة** | معلقة → تم إرسالها → مقبولة → مجدولة → مكتملة / انتهت / رفض |
| **محادثة بين الممارسات** | الرسائل المشفرة حسب الامتثال HIPAA بين مديري الممارسات/مدير الفروع |
| **مشاركة المرفقات** | إرسال الصور، الأشعة السينية، المستندات، نتائج التحليل، الوصفات بين الممارسات |
| **محادثات متعددة المواضيع** | مجموعات الدردشة لكل ارجاع مع إيصال القراءة |
| **أمثلة حقيقية** | طفولة→نفسية (النهاية المزمنة)، الأمراض الجلدية→علاج العظام (الأمراض المعدية الجلدية)، علاج العظام→الأمراض الجلدية (رعاية الجروح) |
| **متابعة الموافقة** | أرقام الموافقة، تاريخ الانتهاء، علامات التحقق من متطلبات الموافقات السابقة |

</details>

<details>
<summary><h3>💬 الدردشة والاتصال بين فرق العمل</h3></summary>

🔗 **[قراءة وثائق التفاعل والاتصال بين فرق العمل بالتفصيل](../../docs_source_en/team_chat_communication.md)**
- [Collaborative Editor Suite](../../docs_source_en/collaborative_editors_module.md)




| الميزانية | التفاصيل |
|---------|---------|
| **الدردشة المشفرة من الطرف إلى الطرف** | الرسائل بين فرق العمل في الفضاءات العملية مطابقة لـ HIPAA |
| **اجتماعات الفيديو الجماعية** | الاجتماعات الفيديو عبر الإنترنت الموزعة (WebRTC) ذات الحجم المناسب للمشاركة بين 6 أشخاص (HIPAA مطابق) |
| **جدول الأعمال الآمن** | التسجيلات المؤكدة باستخدام نماذج بريد إلكتروني بدون PHI لروابط التقويم |
| **الاتصالات الصوتية والفيديو** | الاتصالات الصوتية والفيديو المحمية (للشركات فقط) |
| **مشاركة السياق الذكاء الاصطناعي** | توجيه الخطة العلاجية → "مشاركة الجلسة" → نقل إلى قنوات الفحص |
| **ال الأوامر الصوتية للتنفيذ** | الأوامر الصوتية → مكالمات الهاتف، الرسائل النصية، البريد الإلكتروني، التخطيط (الأعلى من الوظيفة) |
| **قنوات** | القنوات المبنية على الأقسام (الطبية، الفحص، الإدارة) |
| **المرفقات الملفية** | مشاركة المستندات والصور والأصول الطبية في الدردشة |

</details>

<details>
<summary><h3>📞 مجموعات التعاون الطبي</h3></summary>

| الميزة | التفاصيل |
|---------|---------|
| **لوحة القيادة المركزية** | توجيه الخرائط للبيانات الإجمالية بفعالية. مركز الأوامر يعزل المهام المفقودة بشكل طبيعي. |
| **الاستشارات الفورية (WebRTC)** | تدفق فيديو أمني P2P متقدمة باستخدام عقد TURN/STUN لTwilio، مما يتجنب المرآت الوسطى. |
| **منع الوصول بناءً على RLS** | تتبع الهوية ضمنياً تجنب تسرب البيانات عبر المواقع بين المستخدمين في الخادم بشكل طبيعي وربطه بحدود Advanced/Pro بشكل صارم. |
| **مهام طبية** | مذكرات الداخلية، الموافقات، والخطوات في الطبيعة المنفصلة لكل مساحة العمل بأمان. |

</details>

### 🔐 Enterprise Administration
    <details>
    <summary><h3>🛡️ الأمان والامتثال</h3></summary>

| الميزة | التفاصيل |
|---------|---------|
| **امتثال HIPAA** | سجل مراجعة كامل لـ HIPAA، بنية تحتية مستعدة للBAAs |
| **تحكم في الوصول القواسي** | 11 دورات معتمدة على التوقيع الرقمي مع حدود الوصول المحددة |
| **عزل البيانات** | يتم إزالة جميع السجلات حسب العيادة (`workspace_id`) لمنع التلوث المتبادل |
| **تسجيل تسجيل الدخول القابض على التلاعب** | توكنات قصيرة الأمد (انتهاء في 15 دقيقة) تضمن تسجيل الخروج من الأجهزة غير النشطة |
| **التشفير عند الراحة** | تشفير بيانات متعددة الوثائق (AES-256) لجميع المعلومات الصحية |
| **سجلات التحقق القابض على التلاعب** | سجلات غير قابلة للتغيير لجميع تعيين الأدوار، الوصول إلى الملفات، وعمليات الرسائل |
| **وضع HIPAA في حالة الإخفاق** | رفض الوصول للميكروفون إذا كان المعالجة المحلية غير متاحة (لا توجد خلفية عנן مكتومة) |
| **حد أدنى للبيانات** | لا تخزن المتصفح بيانات الأشخاص المعنيين; يتم تنقية البيانات الحساسة فورًا عند إغلاق 탭 |
</details>

<details>
<summary><h3>⚙️ إدارة المنصة وعلامة التميز البيضاء</h3></summary>

🔗 **[قراءة مستندات إدارة المنصة وعلامة التميز البيضاء المفصلة](../../docs_source_en/platform_administration_white_label.md)**



| الميزانية | التفاصيل |
|---------|---------|
| **البنية التحتية المتعددة المستنادين** | مساحات العمل منعزلة مع تخصيصات وعلامات تجارية متخصصة |
| **المواقع الوظيفية الديناميكية** | الشعار، العنوان الرئيسي، والتصميم الملون يتم استرداده بشكل ديناميكي عبر SSR |
| **توفر الوحدات** | يمكن للمسؤولين عن المنصة إضافة أو إخفاء الوحدات بناءً على التخصص الطبي |
| **تبديل ميزات الموظفين** | تجاوز الأدوار الأساسية باستخدام مصفوفات JSONB `restricted_features` التي تفرض حظرات API في وقت التشغيل |
| **بناء الشاشات** | القدرة على إعادة تسمية الزر، إخفاء أعمدة جدول البيانات، أو تجاوز النسخ المعاصرة للنسخة الأم |
| **تسجيل الاستثناءات** | جميع إجراءات المسؤولين عن المنصة مسجلة في سجلات التحقق من الامتثال لـ HIPAA |

</details>



---

## 🏥 Synalux Health: تطبيق الويب السريري

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

## 🧑‍💻 Synalux Dev: إضافة VS Code

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
<summary><h2>🛡️ الأمن المؤسسي وبنية التحتية لـ HIPAA</h2></summary>

Synalux مصمم للبيئات ذات الثقة الصفرية.

### تدفق الطلبات متعدد المستأجرين

```
┌─────────────────┐     ┌──────────────────────────────┐     ┌──────────────────────────────┐     ┌─────────────────────────────┐
│   Client        │     │   Vercel Edge (Middleware)    │     │   Next.js API Routes         │     │   Supabase PostgreSQL       │
│                 │     │                              │     │                              │     │                             │
│  Browser /      │────▶│  1. التحقق من الهوية (NextAuth)  │────▶│  3. تطبيق سياسات الوصول للأدوات |────▶│  6. سياسات RLS               │
│  VS Code        │     │  2. توقيع JWT (Ed25519)         │     │  4. خدمة التجربة الذكية       │     │     (JWT → set_config)      │
│                 │     │     (مدة صلاحية 15 دقيقة)        │     │     (ProposedChange)         │     │  7. بيانات متعددة المستأجرين | 
│                 │     │                              │     │  5. سجل مراجعة HIPAA          │     │     (عزلة workspace_id)   │
└─────────────────┘     └──────────────────────────────┘     └──────────────────────────────┘     └─────────────────────────────┘
                              Google OAuth                    سياق أدوات مقتصر              فiltres RLS بالworkspace_id
```

**رؤية أساسية:** لأن JWT تحمل طلبات `workspace_id` وسياسات RLS في Postgres تقرأها عبر `current_setting('request.jwt.claims')`، لا توجد **متغيرات جلسة من جهة الخادم** ولا **مجمعات اتصال لكل مستأجر**. هذا يجعل Synalux قابل للتوسع أفقيًا.

### سياسات الأمان

* **التحقق من الهوية (EdDSA (Ed25519)):** يتم ترديم التوكنات API الثابتة إلى حالة تحديث فقط. جميع طلبات API مصادفة عبر JWT قصيرة المدة (15 دقيقة) توقيعها باستخدام كروماتيغرافية غير متقاربة.
* **التشفير الشامل للبيانات (TDE):** يتم تشفير جميع الرسائل الفريق، المستندات المنشأة، والسجلات التاريخية في الذاكرة عند الراحة.
* **الحد الأدنى القاسية للمعلومات:** نصوص التطبيق على الويب تعيش فقط في الذاكرة المؤقتة لـ React وتم التخلص منها فور إغلاق علامة التبويب. لا يتم استخدام `localStorage` لأي بيانات حساسة (PHI).
* **تخزين الملفات موزعة بناءً على نوع MIME:** يتم قياس توصيلات الطبية بواسطة التحقق من نوع MIME الخادم المركزي القواعدية والتقديم حصرياً عبر روابط URL موقعة لمدة 15 دقيقة مع حماية IDOR.
* **سجلات مراجعة غير قابلة للتغيير:** يتم تسجيل كل تعيين دور، تنزيل ملف، وحذف رسالة دائمًا في `rbac_audit_log` للضمان من عدم الاعتبار. الصفوف في سجل المراجعة هي إضافية فقط — حتى يمكن للمدراء بقاعدة البيانات تعديل السجلات التاريخية.
* **بوابة السلامة لـ HITL:** الأدوات الخطرة (`terminal`, `git_tool`, `browser`) تتطلب الموافقة الافتراضية من المستخدم عبر مربع الحوار قبل التنفيذ - مما يمنع التهديدات غير المقصودة من خلال تضمين الأوامر.
* **وضع HIPAA القفل عند الفشل:** إذا كان LLM المحلي (Ollama) غير متاح أثناء استقبال صوت طبي، فإن النظام رفض فتح الميكروفون بدلاً من الانتهاء السكري للمعالجة في السحابة.
* شعار البيانات القديمة (سلامة المرضى): إذا لم يتم تحديث بيانات الطبية في الجلسة الحالية، يظهر شعار تحذير للمستشار، مما يمنع اتخاذ قرارات علاجية بناءً على معلومات قديمة.

### إقرار HIPAA

| متطلب HIPAA | تنفيذ Synalux |
|---|---|
| **§164.312(a)(1)** السيطرة على الوصول | سياسات RBAC JWT مع سياسات الوصول لكل أداة; RLS تفرض التفوق بين المستأجرين في طبقة قاعدة البيانات |
| **§164.312(b)** سياسات المراجعة | سجل مراجعة غير قابل للتغيير `hipaa_audit_log` + `rbac_audit_log` — يتم تسجيل كل الوصول إلى PHI مع المستخدم والإجراء والموارد والمزمن |
| **§164.312(c)(1)** الامان | خدمة التجربة الذكية (`ProposedChange`) تضمن عدم الكتابات الآلية إلى بيانات الطبية بدون توقيع من المستشار |
| **§164.312(d)** التحقق من الهوية | JWT غير متقاربة (مدة صلاحية 15 دقيقة); Google OAuth مع MFA للدورات الطبية |
| **§164.312(e)(1)** أمان النقل | يتم تطبيق TLS 1.3 على جميع النهايات; الاتصالات مع Supabase تستخدم SSL؛ لا يوجد PHI في معلم URL |
| **§164.308(a)(1)** تحليل المخاطر | مراجعة أمنية متناقضة (`REVIEW_PROMPT.md`); حواجز خرج تلقائية مع مراقبة SSE النشط |
| لا `localStorage` | جميع بيانات الطبية تعيش في الذاكرة المؤقتة لـ React (تم التخلص منها عند إغلاق علامة التبويب) أو Postgres (مرتبطة بـ RLS). لا وجود تخزين جرافيكي للمعلومات الحساسة في المتصفح |

> **غطاء BAA:** توفر كاملة HIPAA مع BAA تتطلب Vercel Enterprise + Supabase Team. راجع [البنية التحتية والخدمات السحابية](#platform-modules) للحصول على الأسعار.

</details>

---

---

## 🚀 البدء

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
