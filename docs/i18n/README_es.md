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
<summary><h3>📋 Notas Clínicas y Documentación</h3></summary>

🔗 **[Leer la Documentación Detallada de las Notas Clínicas y la Documentación](../../docs_source_en/clinical_notes_documentation.md)**



| Característica | Detalles |
|---------|---------|
| **Notas SOAP** | Generadas automáticamente a partir del dictado de voz con plantillas específicas por especialidad |
| **Dictado de Voz** | WASM Whisper en el dispositivo → transmisión cero de PHI al nube |
| **4 Plantillas de Notas** | Sesión terapéutica, nota de progreso, evaluación inicial, resumen de alta médica |
| **Documentos** | Resultados de laboratorio, imágenes, consentimientos, evaluaciones, planes de tratamiento — todos los documentos del espacio de trabajo |
| **Exportación a PDF** | Renderizado en el servidor (sin filtrado de PHI en el lado del cliente) |
| **Firmas Electrónicas** | Integración con BoldSign para 7 plantillas de documento |
| **OCR** | Escaneo de documentos en más de 30 idiomas para la digitalización de los formularios de entrada |

</details>

<details>
<summary><h3>📴 Sesiones Clínicas Primero Desconectado</h3></summary>

🔗 **[Leer la Documentación Detallada de las Sesiones Clínicas Primero Desconectado](../../docs_source_en/offline_first_clinical_sessions.md)**



| Característica | Detalles |
|---------|---------|
| **Marcas de Tiempo del Cliente** | Las horas de inicio y finalización de la sesión se capturan en el dispositivo del proveedor — se usan para facturar, no la hora de recepción del servidor |
| **Cola Desconectada** | Los eventos se ponen en cola en localStorage cuando están desconectados, se sincran automáticamente al reconectar |
| **Persistencia de borradores** | Las notas clínicas se guardan automáticamente en localStorage con cada pulsación de teclado — sobreviven a un cierre del navegador o una pérdida de conexión |
| **Desaprobación de Sesión** | El proveedor DEBE desaprobar la sesión al finalizarla — la marca de tiempo es el momento exacto de facturación |
| **Auditoría Administrativa** | Cada evento muestra un indicador verde/rojo 🟢 / 🔴 con los tiempos de sincronización |
| **Monitor de Conexión** | El panel lateral muestra en tiempo real el estado verde/rojo 🟢/🔴 con la insignia de la cuenta pendiente de sincronización |
| **Limpieza HIPAA** | Todos los datos locales se eliminan al cerrar sesión y por tiempo ocioso |
| **Sincronización Idempotente** | Se previenen eventos duplicados mediante UUIDs generados por el cliente |
| **Detección de Desfase del Tiempo** | El servidor registra el desfase entre las marcas de tiempo del cliente y el servidor para auditoría |
| **Ciclo de Vida de la Sesión** | `session_start` → `session_pause` → `session_resume` → `session_end` |

**Cumplimiento con Facturación:**
```
El proveedor inicia la sesión a las 2:00 PM (en línea) → 🟢
  La conexión se pierde a las 2:30 PM
El proveedor termina la sesión a las 3:45 PM (desconectado) → 🔴 client_timestamp = 3:45 PM
  La conexión se restaura a las 4:00 PM → sincronización automática
El servidor registra: client_timestamp = 3:45 PM, sync_timestamp = 4:00 PM
  ↓
La aseguradora factura: sesión de 2:00 PM – 3:45 PM (exacta)
El administrador ve: "Sesión terminada a las 3:45 PM 🔴 Desconectado (sincronizada a las 4:00 PM)"
```

</details>

<details>
<summary><h3>🧪 Módulo de Pedidos y Resultados de Laboratorio</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Pedidos y Resultados de Laboratorio](../../docs_source_en/lab_orders_results_module.md)**



| Característica | Detalles |
|---------|---------|
| **Pedidos de Laboratorio** | Seguimiento de pedidos con proveedores (Quest, LabCorp, en-situ), prioridad (ordinario/urgente/emergencia) |
| **Seguimiento de Resultados** | Individuales resultados de pruebas con rangos referenciales y banderas de anomalía (bajo/alto/crítico) |
| **Categorías** | Hematología, Química, Lipídicos, Fígado, Tiroides, Vitamina, Inflamación, Coagulación |
| **Alertas por Anomalía** | Marcado automático de resultados fuera del rango (por ejemplo, TSH elevada, vitamina D baja) |
| **iPLEDGE Labs** | Monitoreo mensual de Accutane: CBC, CMP, panel lipídico, LFTs con seguimiento de tendencia |
| **Prequirúrgicas** | INR, PT, glucosa, aclaración A1C para implantes dentales y procedimientos quirúrgicos |
| **Monitoreo de Medicamentos** | Verificación del tiroides por SSRIs, paneles lipídicos estímulantes, paneles de base biológica |
| **Ciclo de Vida del Pedido** | Pedido → Recogido → Enviado → Recibido → En Proceso → Resultado → Revisado |
| **Integración con Proveedores** | Quest Diagnostics, enrutamiento de pedidos LabCorp (planeado: importación automática de resultados electrónicos) |
| **Enlace a la Diagnóstica** | Códigos ICD-10 adjuntos a los pedidos para documentación de necesidad médica |

</details>

<details>
<summary><h3>💊 Módulo de Medicamentos y Prescripciones</h3></summary>

🔗 **[Leer la documentación detallada del Módulo de Medicamentos y Prescripciones](../../docs_source_en/medications_prescriptions_module.md)**



| Función | Detalles |
|---------|---------|
| **Catálogo de Medicamentos** | 12+ medicamentos con códigos NDC, clases de medicamento, horarios, rutas, dosis comunes |
| **Prescripciones Activas** | Lista de medicamentos por paciente con dosis, frecuencia, prescriptor, farmacia, seguimiento de reemplazos |
| **Clases de Medicamentos** | SSRIs, estimulantes, retinoides, biológicos, broncodilatadores, NSAIDs, antibióticos, anticonvulsivos |
| **Seguimiento iPLEDGE** | Monitoreo de isotretinoin con Accutane requerimientos de laboratorio mensuales |
| **Ciclo de Estado** | Activo → En espera → Discontinuado → Completado → Cancelado |
| **Advertencias por Interacción** | Matriz de advertencias específicas por medicamento (síndrome del serotonina, QTc, teratogénico) |
| **Enrutamiento Farmacéutico** | Farmacia nombrada por prescripción para la preparación de e-prescripciones |

</details>

<details>
<summary><h3>📊 Módulo de Vitalidad y Medidas</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Vitalidad y Medidas](../../docs_source_en/vitals_measurements_module.md)**



| Característica | Detalles |
|---------|---------|
| **Vitalidades Estándar** | BP (sistólica/diastólica), HR, RR, temp (con método), SpO2, peso, altura, BMI |
| **Escala de Dolor** | Escala numérica de dolor del 0 al 10 por visita |
| **Crecimiento Infantil** | Circunferencia craneal, percentiles de peso/altura/BMI (WHO/CDC) |
| **Evaluaciones PT** | Grados de ROM, puntuaciones funcionales (Oswestry, LEFS), notas sobre la activación cuádriceps |
| **Seguimiento de Tendencias** | Vitales históricos por paciente para análisis de tendencias |
| **Enlace a Citas** | Vitalidades vinculadas a las citas específicas |

</details>

<details>
<summary><h3>⚠️ Módulo de Alergias y Alertas</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Alergias y Alertas](../../docs_source_en/allergies_alerts_module.md)**



| Característica | Detalles |
|---------|---------|
| **Tipos de Alergeno** | Medicamento, alimento, ambiental, látex, contraste, otro |
| **Niveles de Gravedad** | Sutil, moderado, severo, amenazante con la vida |
| **Seguimiento de Reacciones** | Documentación específica de reacción (anafilaxis, SJS, urticaria, upset gastrointestinal) |
| **Soporte NKDA** | Documentación explícita "No alergias conocidas a medicamentos" |
| **Alertas Clínicas** | Marcadores críticos de alergia (Penicilina → usar clindamicina, Sulfonamida → historia de SJS) |
| **Verificación** | Verificación del proveedor con marcas de fecha |

</details>

<details>
<summary><h3>💉 Módulo de Vacunas</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Vacunas](../../docs_source_en/immunizations_module.md)**



| Característica | Detalles |
|---------|---------|
| **Seguimiento de Vacunas** | Códigos CVX, números de dosis, números de lote, fabricantes |
| **Administración** | Sitio, vía (IM/SC/PO/IN/ID), proveedor administrante |
| **Cumplimiento con el VIS** | Seguimiento de la fecha del Informe de Vacuna |
| **Informes al Registro Estatal** | Seguimiento de la entrega al registro estatal de vacunas |
| **Calendario CDC** | DTaP, IPV, MMR, Varicella, Hep A/B, Influenza, Tdap |
| **Immunocomprometidos** | Recomendaciones especiales de vacunas para pacientes biológicos |

</details>

### 🏢 Practice Operations Modules
<details>
<summary><h3>💳 Modulo de Facturación y Pagos</h3></summary>

🔗 **[Leer la documentación detallada del módulo de facturación y pagos](../../docs_source_en/billing_payments_module.md)**



El módulo de facturación usa **Stripe Connect** para otorgar a cada práctica su propia cuenta bancaria independiente de pago vinculada al administrador de la práctica.

**Configuración de Facturación por Práctica:**
| Configuración | Detalles |
|---------|---------|
| **Stripe Connect** | Cada espacio de trabajo tiene su propia cuenta `acct_xxx` de Stripe Connect |
| **Admin Vinculado** | La propiedad de la cuenta de Stripe está vinculada al usuario administrador del espacio de trabajo |
| **Horarios de Tarifas** | Horarios de tarifas por práctica con tasas estándar, de seguro, de Medicare y de pago propio |
| **Métodos de Pago** | Tarjeta de crédito, ACH/traslado bancario, cheque, efectivo — configurable por práctica |
| **Publicación Automática** | Publicación automática de pagos, envío de recibos y generación de estados mensuales |
| **Configuración Fiscal** | Tasas fiscales por práctica y NPI/EIN para el informe 1099 |

**Múltiples Países y Monedas (NUEVO):**

| País | Moneda | Estándar | Avanzado | Empresarial |
|---------|----------|----------|----------|------------|
| 🇺🇸 USA | USD | $19/mo | $49/mo | $99/mo |
| 🇨🇦 Canada | CAD | C$25/mo | C$65/mo | C$129/mo |
| 🇬🇧 UK | GBP | £15/mo | £39/mo | £79/mo |
| 🇩🇪🇫🇷 EU | EUR | €18/mo | €45/mo | €89/mo |
| 🇦🇺 Australia | AUD | A$29/mo | A$75/mo | A$149/mo |
| 🇳🇿 New Zealand | NZD | NZ$32/mo | NZ$82/mo | NZ$159/mo |

**Descuentos por volumen:**
| Clientes | Descuento |
|---------|----------|
| 100+ | 10% de descuento por precio por licencia |
| 500+ | 20% de descuento por precio por licencia |
| 1,000+ | 30% de descuento por precio por licencia |
| Facturación anual | Descuento adicional del 20% (se acumula con los descuentos por volumen, limitado al 45%) |

**Ciclo de vida de la falla en el pago:**
```
Pago Fallido → past_due (bandera de advertencia, mantener el acceso)
  → intento de pago 2º → aún past_due (advertencia urgente)
  → intento de pago 3º fallido → desgradación automática al nivel gratuito
  → Stripe subscription.deleted → plan = 'free', sub limpiado
```

**Sobrescrituras por Administrador de Plataforma:**
- Los administradores de la plataforma Synalux pueden establecer a cualquier usuario en pruebas ilimitadas en cualquier plan
- Los usuarios sobrescritos son **inmutables** ante las actualizaciones de descarga de webhook de Stripe
- El administrador ve indicadores verde/rojo para el estado del pago
- Rastreo completo: quién estableció la sobrescritura, cuándo y por qué

**Gestión del ciclo de facturación:**
- Seguimiento del ciclo de vida de las solicitudes de cobertura médica (borrador → enviado → aceptado → pagado/rechazado → recurso)
- Procesamiento electrónico de remittencias (ERA/EOB)
- Gestión de rechazos con seguimiento de plazos para los recursos
- Flujo de trabajo de autorización previa
- Informes de envejecimiento (intervalos de 30/60/90/120 días)

**Pagos a pacientes:**
- Portal del paciente "Pagar Ahora" → redirección a Stripe Checkout
- Pagos parciales y cantidades personalizadas
- Planes de pago con suscripciones recurrentes de Stripe
- Generación y descarga de recibos
- Procesamiento de reembolsos

**Reclamaciones de seguro:**
- Presentación electrónica de reclamaciones (837P)
- Verificación en tiempo real de la elegibilidad
- Coordinación de beneficios (COB)
- Seguimiento de los recursos de cobertura (EOB)
- Gestión de recurso con plantillas de carta

**Recopilación automática de impuestos:**
- Stripe Tax habilitado por país (IVA, GST, HST, PST)
- Cálculo automático del impuesto basado en el país del espacio de trabajo
- Cumple con las reglas fiscales canadienses multi-provincial (GST federal + provincial PST/HST)

</details>

<details>
<summary><h3>📅 Agenda y Citas</h3></summary>

🔗 **[Leer la Documentación Detallada de Agenda y Citas](../../docs_source_en/scheduling_appointments.md)**



| Funcionalidad | Detalles |
|---------|---------|
| **Estados de las Citas** | Programado → Confirmado → En Progreso → Completado (+ cancelado, ausente, reprogramado) |
| **Solicitudes del Portal del Paciente** | Los pacientes solicitan citas con la fecha y hora preferida → el personal confirma o niega |
| **Múltiples Proveedores** | Programar a través de varios proveedores dentro de una práctica |
| **Visitas Recurrentes** | Sesiones terapéuticas semanales, consultas mensuales, ajustes ortodóxicos |
| **Lista de Espera** | Solicitudes de citas en la lista de espera cuando no hay cupos disponibles |
| **Recordatorios Automáticos** | Recordatorios automáticos de citas (programados) |

</details>

<details>
<summary><h3>👥 Módulo de Gestión de Recursos Humanos y Personal</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Gestión de Recursos Humanos y Personal](../../docs_source_en/hr_staff_management_module.md)**



| Característica | Detalles |
|---------|---------|
| **Perfiles de Personal** | Tipo de empleo, fecha de contratación, salario/tasa horaria, especialidades, seguimiento del departamento |
| **Credenciales** | Seguimiento de licencias/certificaciones con alertas de vencimiento y flujos de renovación |
| **Tiempo Libre** | Vacaciones, enfermedades, CE, maternidad, luto, jurado — flujos de aprobación |
| **Formación** | Seguimiento de formación de cumplimiento (HIPAA, BLS, CPR) con fechas límite y estado de finalización |
| **Evaluaciones de Desempeño** | Revisión anual/semestral con calificaciones, metas, planes de mejora y reconocimiento |
| **Admisión** | Estado pendiente de admisión, flujo de verificación de credenciales, asignaciones de formación |

</details>

<details>
<summary><h3>⏱️ Modulo de Hojas de Tiempo y Nómina</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Hojas de Tiempo y Nómina](../../docs_source_en/timesheets_payroll_module.md)**



| Característica | Detalles |
|---------|---------|
| **Generación Automática** | Las hojas de tiempo se generan automáticamente a partir de las notas clínicas firmadas |
| **Tiempo No Facturable** | Rastrea el tiempo administrativo, el tiempo de conducción, la formación y la preparación del clínico |
| **Flujos de Aprobación** | Presentación por parte del empleado → Revisión por supervisor → Procesamiento de nómina |
| **Exportación de Nómina** | Exporta las hojas de tiempo integradas nativamente con ADP, Gusto y Paycom |
| **Cumplimiento** | Advertencias por horas extras de 40 horas, seguimiento obligatorio de descansos, visibilidad del ahorro de vacaciones |

</details>

<details>
<summary><h3>📦 Módulo de Gestión del Inventario</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Gestión del Inventario](../../docs_source_en/inventory_management_module.md)**



| Característica | Detalles |
|---------|---------|
| **Categorías** | Suministros dentales, vacunas, medicamentos, biológicos, PPE, quirúrgico, suministros de laboratorio, oficina |
| **Rastreo del Stock** | Cantidad en stock, nivel de reorden, cantidad para reordenar, costo unitario |
| **Lote y Caducidad** | Números de lote, fechas de vencimiento, rotación FIFO para vacunas |
| **Seguimiento de Proveedores** | Henry Schein, Patterson Dental, Nobel Biocare, McKesson, Sanofi Pasteur |
| **Alertas de Estado** | En stock, bajo stock, agotado, caducado, discontinuado |
| **Ubicaciones de Almacenamiento** | Refrigerador de vacunas (2-8°C), refrigerador biológico, armarios quirúrgicos, cajones cerrados |
| **Objetos Especiales** | Fijas implantes ($285), lápices biológicos ($2,850), canastillas de cryoterapia |

</details>

<details>
<summary><h3>🧾 Módulo de Facturas Superiores</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Facturas Superiores](../../docs_source_en/superbills_module.md)**



| Característica | Detalles |
|---------|---------|
| **Por Encuentro** | Una factura superior por visita con diagnóstico y códigos de procedimiento |
| **Código Multicodificación** | Arreglos de diagnóstico ICD-10 + arreglos de procedimientos CPT/CDT + modificadores (-25, -59) |
| **Desglose Financiero** | Cargo total, cobertura por seguro, copago del paciente, ajustes |
| **Ciclo de Estado** | Borrador → Revisión → Presentado → Pagado / Denegado / Apeal |
| **Todas las Especialidades** | Visitas pediátricas, implantes, ortopedia, terapia psicológica, rehabilitación PT, procedimientos dermatológicos |
| **Descuentos por Seguro de Seguros Sociales** | Rastreo automático de ajustes para los deberes contractuales del seguro de seguros sociales |

</details>



<details>
<summary><h3>📋 Módulo de Tareas Clínicas</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Tareas Clínicas](../../docs_source_en/clinical_tasks_module.md)**



| Característica | Detalles |
|---------|---------|
| **Categorías de Tareas** | Seguimiento laboral, autorización previa, programación, documentación, facturación, llamada al paciente, reemplazo, referencias |
| **Niveles de Prioridad** | Baja, normal, alta, urgente |
| **Asignación** | Asignado a personal específico con fechas límite y seguimiento de finalización |
| **Enlace al Paciente** | Tareas vinculadas a pacientes específicos para la coordinación del cuidado |
| **Seguimiento del Estado** | Abierto → En Progreso → Completado / Cancelado / Pausado |
| **Rastro Auditivo** | Creado por, completado por, timestamps de finalización |

</details>

### 🤝 Patient Experience & Collaboration
<details>
<summary><h3>Puerto Hospitalario</h3></summary>

🔗 **[Leer la documentación detallada del Puerto Hospitalario](../../docs_source_en/patient_portal.md)**



Un portal completo y funcional para pacientes con autenticación, mensajes, documentos, citas y facturación.

| Feature | Details |
|---------|---------|
| **Autenticación** | Inicio de sesión por código (cifrado SHA-256), seguimiento de expiraciones |
| **Panel de Control** | Visión general de la salud con citas programadas próximas, mensajes no leídos, documentos pendientes, saldo adeudado |
| **Mensajes** | Conversaciones en hilos con proveedores, indicadores urgentes, recibos de lectura |
| **Documentos** | Ver/bajar documentos clínicos, cargar tarjetas de seguro y formularios |
| **Citas** | Ver citas futuras/pasadas, solicitar nuevas citas con tiempos preferidos |
| **Facturación** | Ver saldo, historial de facturación con códigos CPT, pagar en línea a través de Stripe, planes de pago, recibos |
| **Formularios** | Completar formularios de admisión, cuestionarios PHQ-9/GAD-7, formularios de consentimiento en línea |
| **Consentimientos** | Gestión digital de los consentimientos (tratamiento, HIPAA, telemedicina, medicamentos, investigación) |

</details>

<details>
<summary><h3>📚 Módulo de Educación al Paciente</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Educación al Paciente](../../docs_source_en/patient_education_module.md)**



| Característica | Detalles |
|---------|---------|
| **Catálogo de Material** | 14 documentos educativos a lo largo de todas las especialidades |
| **Múltiples Idiomas** | Documentos en inglés y español disponibles |
| **Categorías** | Condición, medicación, procedimiento, estilo de vida, pos-operatorio, ejercicio doméstico, seguridad, prevención |
| **Métodos de Entrega** | Impreso, carga por portal, correo electrónico, presencial, texto |
| **Aceptación** | Rastrear si el paciente vio/aceptó el material |
| **Ejemplos Específicos de Especialidades** | Guía EpiPen, seguridad Accutane, rehabilitación ACL, tarea homework CBT, pos-operatorio implante |

</details>

<details>
<summary><h3>🔔 Módulo de Avisos y Recordatorios</h3></summary>

🔗 **[Leer la documentación detallada del Módulo de Avisos y Recordatorios](../../docs_source_en/recalls_reminders_module.md)**



| Funcionalidad | Detalles |
|---------|---------|
| **Tipos de Aviso** | Higiene, examen anual, seguimiento, rechazo de laboratorio, imagenología, escaneo, vacunación, revisión médica |
| **Seguimiento del Estado** | Pendiente → Vencido → Programado → Completado → Cancelado |
| **Intentos de Contacto** | Rastrear los esfuerzos de contacto para los avisos vencidos |
| **Específico por Práctica** | Limpieza bucal cada 6 meses, chequeos anuales de piel dermatológica, laboratorios mensuales de Accutane |
| **Fechas Vencidas Automáticas** | Basadas en la última visita completada |

</details>

<details>
<summary><h3>🔄 Módulo de Citas y Chat Interconsultorio</h3></summary>

🔗 **[Leer la Documentación Detallada del Módulo de Citas y Chat Interconsultorio](../../docs_source_en/referrals_cross_practice_chat_module.md)**



| Característica | Detalles |
|---------|---------|
| **Seguimiento de Citas** | Proveedor, especialidad, motivo, códigos de diagnóstico, urgencia, seguimiento de autorización |
| **Ciclo de Estado** | Pendiente → Enviado → Aceptado → Programado → Completado / Expirado / Rechazado |
| **Chat Interconsultorio** | Mensajería HIPAA-compliant entre administradores de consultorios/gerentes de oficina |
| **Compartir Archivos** | Envío de imágenes, radiografías, documentos, resultados de laboratorio, recetas entre consultorios |
| **Conversaciones Threaded** | Hilos de chat por cita con recibos de lectura |
| **Ejemplos Reales** | Peds→Psiciatría (ADHD), Derm→PT (artritis psoriática), PT→Derm (cuidado de heridas) |
| **Seguimiento de Autorización** | Números de autorización, fechas de expiración, indicadores de requisito previo de autorización |

</details>

<details>
<summary><h3>💬 Comunicación y Chat de Equipo</h3></summary>

🔗 **[Leer la Documentación Detallada sobre Comunicación y Chat de Equipo](../../docs_source_en/team_chat_communication.md)**
- [Collaborative Editor Suite](../../docs_source_en/collaborative_editors_module.md)




| Función | Detalles |
|---------|---------|
| **Chat Cifrado por Fin a Fin** | Mensajería de equipo HIPAA-compliant dentro de los espacios de trabajo |
| **Reuniones de Video Grupal** | Reuniones WebRTC de 6 participantes escalables y telemedicina & reuniones de equipo HIPAA-compliant |
| **Agendamiento Seguro** | RSVP autenticados utilizando plantillas de correo electrónico sin PHI para enlaces del calendario |
| **Llamadas y Videoconferencias por Voz y Video** | Conferencias de voz y video seguras (solo para Empresas) |
| **Compartir Contexto con IA** | Generar Plan de Tratamiento → "Compartir Sesión" → reenviar a la canal de facturación |
| **Comando por Voz** | Comandos de voz → llamada, SMS, correo electrónico, agendar (Pro+) |
| **Canales** | Canales basados en departamentos (Clínico, Facturación, Administrativo) |
| **Archivos Adjuntos** | Compartir documentos, imágenes y activos clínicos en el chat |

</details>

<details>
<summary><h3>📞 Suite de Práctica de Colaboración</h3></summary>

| Feature | Details |
|---------|---------|
| **Panel Centralizado** | Enrutador de mapeo de métricas agregadas de manera eficiente. Centro de comandos aislando tareas perdidas nativamente. |
| **Consultas Vídeo (WebRTC)** | Streaming P2P avanzado y seguro usando nodos TURN/STUN de Twilio evitando middleboxes. |
| **RLS Gating** | Rastreo implícito de identidad eliminando fugas de datos cruz-tennant en el servidor nativamente, mapeándolas estrictamente a los límites Avanzado/Pro. |
| **Tareas Clínicas** | Recordatorios internos de clínica, aprobaciones y encolado aislados por espacio de trabajo de manera segura. |

</details>

### 🔐 Enterprise Administration
    <details>
    <summary><h3>🛡️ Seguridad y Cumplimiento</h3></summary>

| Característica | Detalles |
|---------|---------|
| **Cumplimiento con HIPAA** | Auditoría completa de HIPAA, arquitectura lista para BAA |
| **Control de Acceso Estricto** | 11 roles firmados digitalmente con límites específicos de acceso |
| **Isolación de Datos** | Todas las registros están aisladas por clínica (`workspace_id`) para prevenir contaminación cruzada |
| **Inicio de sesión Criptográfico** | Tokens cortos de vida (expiración de 15 minutos) garantizan que los dispositivos obsoletos se desconecten |
| **Cifrado en Reposo** | Cifrado Transparente de Datos (AES-256) para toda la información sanitaria |
| **Registros de Auditoría Inmutables** | Registros inmutables para todas las asignaciones de roles, acceso a archivos y acciones de mensajes |
| **Modo de HIPAA Fallido-Cerrado** | Rechaza el acceso al microfonos si el procesamiento local no está disponible (sin retroalimentación silenciosa en la nube) |
| **Minimización de Datos** | Sin almacenamiento en caché del navegador para PHI; los datos sensibles se eliminan inmediatamente cuando una pestaña se cierra |
</details>

<details>
<summary><h3>⚙️ Administración de Plataforma y Branding Personalizado</h3></summary>

🔗 **[Leer la Documentación Detallada de Administración de Plataforma y Branding Personalizado](../../docs_source_en/platform_administration_white_label.md)**



| Funcionalidad | Detalles |
|---------|---------|
| **Arquitectura Multitenant** | Espacios de trabajo aislados con branding y configuraciones dedicadas |
| **Espacios de Trabajo Dinámicos** | Logo de la práctica, dirección principal y tematización dinámica obtenida mediante SSR |
| **Disponibilidad de Módulos** | Los administradores pueden arrastrar y soltar o ocultar módulos según la especialización clínica |
| **Alternancia de Funcionalidades para Empleados** | Sobrescribir roles básicos con matrices JSONB `restricted_features` que imponen bloqueos de API en tiempo real |
| **Construyedores de Pantallas** | Posibilidad por práctica de renombrar botones, ocultar columnas de la tabla de datos o sobrescribir el texto estándar de la interfaz de usuario |
| **Auditoría de Break-Glass** | Todas las acciones de administrador de plataforma registradas en rastros de auditoría cumplidos con HIPAA |

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
<summary><h2>🛡️ Seguridad Empresarial y Arquitectura de HIPAA</h2></summary>

Synalux está diseñado para entornos de cero confianza.

### Arquitectura de seguridad — Flujo de solicitudes multi-tenant

```
┌─────────────────┐     ┌──────────────────────────────┐     ┌──────────────────────────────┐     ┌─────────────────────────────┐
│   Cliente       │     │   Vercel Edge (Middleware)    │     │   Rutas API de Next.js         │     │   Supabase PostgreSQL       │
│                 │     │                              │     │                              │     │                             │
│  Navegador /    │────▶│  1. Verificación de autenticación (NextAuth)    │────▶│  3. Control de acceso a herramientas (ACL)     │────▶│  6. Políticas RLS            │
│  VS Code        │     │  2. Firma JWT (Ed25519)    │     │  4. Sandbox de IA               │     │     (JWT → set_config)      │
│                 │     │     (15 min TTL)             │     │     (Propuesta de cambio)         │     │  7. Datos multitenant       │
│                 │     │                              │     │  5. Registro de auditoría HIPAA          │     │     (isolación por workspace_id) │
└─────────────────┘     └──────────────────────────────┘     └──────────────────────────────┘     └─────────────────────────────┘
                              Google OAuth                    Contexto de herramienta eliminado                   Filtros RLS por workspace_id
```

**Perspectiva clave:** Dado que los JWT llevan claims de `workspace_id` y las políticas RLS de Postgres las leen a través de `current_setting('request.jwt.claims')`, no hay **variables de sesión del lado del servidor** ni **pools de conexión por tenant**. Esto es lo que hace a Synalux escalable horizontalmente — una ventaja crítica sobre los EHR heredados que usan modelos de conexión por sesión.

### Controles de seguridad

* **Autenticación con EdDSA (Ed25519):** Los tokens de API estáticos se demuestran como solo para refrescar. Todas las solicitudes de API se autentican mediante JWT cortos de vida (15 min) firmados con criptografía asimétrica.
* **Cifrado de datos transparente (TDE):** Todos los mensajes del equipo, documentos generados y historiales de sesiones están cifrados en reposo.
* **Minimización estricta de datos:** Las transcripciones de la aplicación web viven estrictamente en la memoria de React state y se recolectan automáticamente cuando se cierra una pestaña. `localStorage` nunca se usa para el PHI.
* **Almacenamiento seguro de archivos con MIME:** Los anexos clínicos están restringidos por una verificación MIME estricta del lado del servidor y se sirven exclusivamente a través de URLs firmadas de 15 minutos con protección contra IDOR.
* **Registros de auditoría inmutables:** Cada asignación de rol, descarga de archivo y eliminación de mensaje se registra permanentemente en `rbac_audit_log` para cumplir la no-repudiation. Las filas de auditoría son append-only — incluso los administradores de base de datos no pueden modificar entradas históricas.
* **Puerta de seguridad HITL:** Herramientas peligrosas (`terminal`, `git_tool`, `browser`) requieren aprobación explícita del usuario mediante un cuadro de diálogo modal antes de la ejecución — preveniendo el RCE por inyección de prompt sin hacer clic.
* **Modo de seguridad HIPAA falla cerrado:** Si el LLM local (Ollama) no está disponible durante la entrada de voz clínica, el sistema rechaza abrir el microfonos en lugar de caer silenciosamente a procesamiento en la nube.
* **Banner de datos obsoletos (Seguridad del paciente):** Si los datos clínicos no se refrescan en la sesión actual, un banner alerta al clínico, preveniendo decisiones de tratamiento basadas en información desactualizada.

### Declaración de cumplimiento con HIPAA

| Requisito de HIPAA | Implementación de Synalux |
|---|---|
| **§164.312(a)(1)** Control de acceso | RBAC basado en JWT con ACL por herramienta; RLS impone la aislamiento del tenant en el nivel de la base de datos |
| **§164.312(b)** Controles de auditoría | `hipaa_audit_log` inmutable + `rbac_audit_log` — cada acceso al PHI se registra con usuario, acción, recurso y marca temporal |
| **§164.312(c)(1)** Integridad | Sandbox de IA (`Propuesta de cambio`) garantiza que no haya escrituras automatizadas en los datos clínicos sin la firma del clínico |
| **§164.312(d)** Autenticación | JWT asimétricos (15 min TTL); Google OAuth con MFA para roles clínicos |
| **§164.312(e)(1)** Seguridad de transmisión | TLS 1.3 forzado en todos los puntos finales; las conexiones a Supabase usan SSL; no hay PHI en los parámetros de URL |
| **§164.308(a)(1)** Análisis de riesgos | Revisión de seguridad adversaria (`REVIEW_PROMPT.md`); barreras de salida automatizadas con escaneo SSE de ventana deslizante |
| **Sin almacenamiento local** | Todos los datos clínicos viven en React state (recolectados automáticamente al cerrar una pestaña) o Postgres (protegidos por RLS). No se persiste el PHI en el navegador |

> **Cobertura de BAA:** La cumplimiento completa con HIPAA requiere Vercel Enterprise + Supabase Team tier. Consulte [Infraestructura y servicios de nube](#platform-modules) para los precios.

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
