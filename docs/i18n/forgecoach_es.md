# 🏋️ ForgeCoach

**Entrenador de fitness con IA de grado militar.** App para iPhone · iPad · Apple Watch. Hace seguimiento de la recuperación, predice la fatiga, genera programas de entrenamiento y te guía en tiempo real — en 23 idiomas. Funciona completamente sin conexión con un modelo de IA en el dispositivo (Pro+). Repositorio independiente: [`forge-watch`](https://github.com/dcostenco/forge-watch).

---

## 🔋 Batería Corporal

Tu puntuación principal de preparación — una combinación de HRV nocturno, tendencia de frecuencia cardíaca en reposo, calidad del sueño y carga de entrenamiento acumulada durante los últimos 7 días.

*   **Puntuación** — 0–100. ≥ 75 = Fresco (verde), 50–74 = Moderado (amarillo), 25–49 = Fatigado (naranja), < 25 = Agotado (rojo).
*   **Integración con HealthKit** — lee el HRV nocturno pasivo capturado por el Apple Watch. No se requiere entrada manual.
*   **Recalibración de referencia** — la batería corporal recalcula su línea base móvil semanalmente, de modo que un atleta bien entrenado y un principiante ven puntuaciones correctamente normalizadas.
*   **Motor ATR** — la Disponibilidad de Entrenamiento Adaptativa sintetiza más de 7 señales biométricas en un único índice de preparación. Tiene en cuenta la relación entre carga aguda (últimos 3 días) y crónica (28 días).

<details>
<summary>Ver Captura de Pantalla — Panel de Control</summary>

![ForgeCoach Dashboard — Body Battery](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png)
*Panel de Batería Corporal — puntuación de preparación combinada, tendencia semanal y accesos directos de acción rápida.*

</details>

---

## 💪 Mapa de Recuperación Muscular

Seguimiento de fatiga por músculo en 14 regiones anatómicas mediante un lienzo de mapa corporal paramétrico renderizado en SwiftUI.

*   **14 grupos musculares** — Pecho, Deltoides Anterior/Lateral/Posterior, Bíceps, Tríceps, Trapecios, Dorsales, Core, Zona Lumbar, Glúteos, Cuádriceps, Isquiotibiales, Gemelos.
*   **Modelo de carga** — cada músculo decae del 100% al 0% entre 48 y 96 horas después del entrenamiento según el volumen de ejercicio y el RPE. La recuperación sigue una curva sigmoide (no lineal).
*   **Alternar frente/espalda** — toca para voltear la silueta. iOS usa un selector segmentado; watchOS muestra ambas vistas como pestañas deslizables.
*   **Código de colores** — ≥ 75% verde, 50–75% amarillo, 25–50% naranja, < 25% rojo.
*   **Destacados del entrenamiento** — los músculos objetivo del programa de hoy pulsan en naranja sobre el lienzo.

<details>
<summary>Ver Captura de Pantalla — Mapa Muscular</summary>

![ForgeCoach Muscle Recovery Map](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png)
*Mapa de recuperación muscular — 14 regiones codificadas por color según la carga. La superposición pulsante muestra los músculos objetivo del día.*

</details>

---

## 📋 Programas de Entrenamiento

Seis plantillas de periodización basadas en la ciencia que cubren todos los principales objetivos de entrenamiento.

| Programa | Estructura | Objetivo |
|---|---|---|
| PPL (Poder/Empuje/Jalón/Piernas) | División superior/inferior de 6 días | Hipertrofia + fuerza |
| 5/3/1 Wendler | Barra + accesorios de 4 días | Fuerza en powerlifting |
| GZCLP | Sistema de niveles de 3 días | Progresión lineal para principiantes |
| Superior/Inferior | División clásica de 4 días | Hipertrofia equilibrada |
| Cuerpo Completo | Énfasis en compuestos de 3 días | Condición física general |
| Descarga / Mantenimiento | Recuperación activa de 1 día | Regeneración |

*   **Programas generados por IA** (Elite) — describe tu objetivo y limitaciones; ForgeCoach genera un bloque personalizado de varias semanas usando Prism 8B o Claude Sonnet.
*   **Generador de Programas JSON** — los programas se representan como modelos Swift tipados; el motor puede generar un programa completo de 8 semanas en < 500 ms en el dispositivo.
*   **Sincronización con Watch** — el programa activo se almacena en caché en el Apple Watch para entrenamiento sin conexión (carga útil < 100 KB).

<details>
<summary>Ver Captura de Pantalla — Programas</summary>

![ForgeCoach Programs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png)
*Programas de entrenamiento — seis plantillas de periodización con programas personalizados generados por IA para Elite.*

</details>

---

## 🍎 Motor de Nutrición

Registro de comidas impulsado por NLP — describe la comida en lenguaje natural, obtén los macros.

*   **Registro de comidas por NLP** — escribe o dicta "2 huevos, tostada con mantequilla, café negro" y el motor analiza entidades alimentarias, cantidades y unidades usando expresiones regulares + Claude Haiku.
*   **Objetivos de macros** — calculados a partir del peso corporal, el objetivo (déficit/superávit/mantenimiento) y el nivel de actividad. Se ajusta diariamente según la carga de entrenamiento.
*   **Seguimiento calórico** — total diario acumulado con desglose (proteínas / carbohidratos / grasas / fibra / agua).
*   **Puntuación de densidad de nutrientes** — señala las carencias de micronutrientes según los alimentos registrados.
*   **Recordatorios de hidratación** — notificaciones push adaptativas basadas en la estimación de la tasa de sudoración durante el ejercicio.

<details>
<summary>Ver Captura de Pantalla — Nutrición</summary>

![ForgeCoach Nutrition](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png)
*Seguidor de nutrición — registro de comidas por NLP, objetivos de macros diarios y seguimiento de hidratación.*

</details>

---

## 🤖 Entrenador IA

Entrenamiento conversacional que conoce tu estado de recuperación, tu última sesión y el contexto del programa.

*   **Nivel Gratuito** — sin IA (solo plantillas de programas estáticos).
*   **Pro — Prism 1.7B en el dispositivo** — funciona mediante llama.cpp con aceleración Metal. Sin conexión de red, completamente privado. Responde preguntas sobre tu entrenamiento, sugiere correcciones de técnica, ajusta el volumen del día según la preparación.
*   **Elite — cascada Prism 1.7B → 8B → Claude Sonnet** — primero en el dispositivo; escala al servidor de inferencia Prism (8B) para preguntas complejas; recurre a Claude Sonnet para un entrenamiento más matizado.
*   **Ventana de contexto** — ForgeMemoryStore inyecta las últimas 3 sesiones, la semana activa del programa, las cargas musculares actuales y la puntuación de batería corporal en cada prompt.
*   **Salida de voz** — las respuestas de la IA se verbalizan mediante ForgeTTSEngine: Synalux cloud TTS (MP3, 24 kHz) con respaldo AVSpeechSynthesizer sin conexión. Seis tonos de entrenamiento: Amigable, Tranquilo, Entusiasta, Preciso, Empático, Esperanzador.
*   **Entrenamiento proactivo** — ProactiveCoachEngine muestra información sin solicitud (p. ej., "Tu HRV bajó un 15% — considera reducir la intensidad hoy") basada en 7 tipos de activadores.

<details>
<summary>Ver Captura de Pantalla — Entrenador IA</summary>

![ForgeCoach AI Coach](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png)
*Entrenador IA — entrenador conversacional contextual con salida de voz e información proactiva.*

</details>

---

## ⌚ App para Apple Watch

App complementaria completa — no solo notificaciones. Seguimiento de sesión independiente en la muñeca.

*   **5 pestañas en el Watch** — Panel (Batería Corporal), Mapa Muscular, Registro de Entrenamiento, Test de Toque del SNC, Ajustes.
*   **Sesión de entrenamiento** — registra series (ejercicio, peso, repeticiones, RPE) directamente desde la muñeca. Temporizador de descanso de 90 segundos con cuenta regresiva háptica.
*   **Test de Toque del SNC** — test de toque rápido de 10 segundos antes del entrenamiento. Mide toques/seg; señala fatiga neuromuscular si está por debajo de la línea base personal.
*   **Marcapasos Háptico** — hápticos rítmicos durante los circuitos AMRAP/EMOM.
*   **Sincronización con el teléfono** — el puente WatchConnectivity envía baterías, batería corporal y flags de funciones de forma bidireccional en tiempo real.
*   **Detección Automática de Series** — el acelerómetro + giroscopio reconocen el inicio/final de la serie y clasifican el tipo de ejercicio. Desactívalo para ahorrar batería del reloj.
*   **Entrenamiento Basado en Velocidad** — estimación de velocidad de la barra montada en la muñeca usando CoreMotion. Señala fatiga neuromuscular cuando la velocidad de la barra cae > 15%.

<details>
<summary>Ver Captura de Pantalla — Panel del Watch</summary>

![ForgeCoach Apple Watch](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png)
*Compañero Apple Watch — panel de Batería Corporal de un vistazo con anillo de recuperación.*

</details>

---

## 🧬 Motor Femme

Ajustes de métricas según la fase del ciclo para atletas femeninas (opcional).

*   **4 fases** — Menstrual, Folicular, Ovulatoria, Lútea.
*   **Ajustes de entrenamiento** — el volumen, los objetivos de intensidad y las recomendaciones de RPE cambian por fase según investigaciones publicadas sobre los efectos hormonales en la fuerza y la recuperación.
*   **Corrección de batería corporal** — las líneas base de temperatura corporal basal y variabilidad de la frecuencia cardíaca se ajustan por fase para evitar señales de fatiga falsas a mitad del ciclo.
*   **Privacidad** — los datos del ciclo nunca salen del dispositivo (CoreData, sin sincronización).

---

## 🧠 Sueño y HRV

Ciencia de recuperación nocturna funcionando silenciosamente en segundo plano.

*   **Captura de HRV** — consultas pasivas de HealthKit para muestras de HRV nocturnas. No se requiere medición activa.
*   **Análisis de fases del sueño** — lee los datos de fases del sueño de Apple (despierto/núcleo/profundo/REM) para puntuar la calidad del sueño.
*   **Bucle de entrenamiento** — SleepTrainingLoop correlaciona la carga del día anterior con el HRV de la mañana siguiente para construir un modelo personal de estrés-recuperación a lo largo del tiempo.
*   **Línea base de batería corporal** — la mediana de HRV de 28 días como referencia personal; las desviaciones impulsan la puntuación de la batería.

---

## 🔊 Voz y TTS

Entrenamiento con IA hablado en tu idioma.

*   **Synalux TTS** — síntesis de MP3 en la nube a 24 kHz/96 kbps mono a través del portal Synalux. 6 tonos de entrenamiento.
*   **Respaldo sin conexión** — AVSpeechSynthesizer con selección automática de la mayor calidad de voz disponible (premium ≥ mejorada ≥ predeterminada). Funciona en los 23 idiomas compatibles.
*   **Atenuación de música** — ForgeTTSEngine atenúa automáticamente Apple Music / Spotify durante el habla de entrenamiento y restaura el volumen después.
*   **Inferencia automática de tono** — el contenido del mensaje se analiza en busca de palabras clave emocionales (PR, fatiga, lesión, regreso, etc.) y se selecciona automáticamente el tono apropiado.
*   **Comandos de voz** — VoiceCommandEngine gestiona el registro de series con manos libres ("registrar 100kg 5 repeticiones RPE 8") y la navegación ("mostrar mi mapa muscular") mediante el framework Speech.

---

## 🌍 Idiomas

23 idiomas compatibles a través del stack de voz de Apple + Synalux TTS.

*   **Códigos de idioma BCP-47** — preferencia de idioma por usuario almacenada en LanguageStore; usada para la selección de voz TTS y la configuración regional del prompt del sistema del entrenador IA.
*   **Entrenamiento con IA** — los prompts se redactan en el idioma seleccionado por el usuario. Los modelos Claude y Prism manejan los 23 idiomas.
*   **23 idiomas** — Inglés, Español, Francés, Portugués, Alemán, Italiano, Neerlandés, Polaco, Ruso, Ucraniano, Rumano, Checo, Húngaro, Sueco, Noruego, Finlandés, Japonés, Coreano, Mandarín, Árabe, Hindi, Turco, Hebreo.

---

## 🏗️ Arquitectura

*   **ForgeCoachCore** — paquete Swift compartido (SPM) que contiene todos los motores, modelos y lógica de negocio. Consumido por la app iOS, la app Mac Catalyst y la extensión watchOS.
*   **llama.cpp (Metal)** — inferencia en el dispositivo para el modelo Prism 1.7B GGUF mediante un paquete SPM local (`_llama_cpp_local`). Solo iOS/macOS; excluido de watchOS en tiempo de compilación.
*   **Puente WatchConnectivity** — `WatchBridge` sincroniza las baterías musculares, la batería corporal y los flags de funciones de forma bidireccional entre el iPhone y el Watch en tiempo real.
*   **Sincronización CloudKit** — `CloudKitSyncEngine` replica el historial de entrenamientos y el perfil de usuario entre dispositivos usando tokens de cambio de CKRecord con resolución de conflictos.
*   **HealthKit** — lee HRV, fases del sueño, FC en reposo, energía activa y muestras de entrenamiento. Escribe resúmenes de sesiones de entrenamiento.
*   **Siri Intents** — `LogWorkoutIntent`, `GetBodyBatteryIntent`, `StartRestTimerIntent` para integración con Atajos.

---

## 🔒 Privacidad

*   **Primero local** — todos los datos biométricos permanecen en el dispositivo. Sin SDK de analítica. Sin informes de fallos de terceros.
*   **HealthKit** — acceso de solo lectura excepto para la escritura de sesiones de entrenamiento. Descrito en la etiqueta de privacidad de la App Store.
*   **Prompts de IA** — el nivel Pro nunca envía datos a ningún servidor. El nivel Elite envía contexto de entrenamiento anonimizado al servidor de inferencia Prism (sin PII, sin datos de HealthKit).
*   **Verificación de suscripción** — correo electrónico enviado por HTTPS a `api.forgecoach.app/subscription/check`. Correo electrónico almacenado en Keychain con TTL de 24 horas y ventana de gracia de 48 horas.
*   **Datos del ciclo** — los datos del Motor Femme son solo de CoreData, nunca sincronizados.

---

## 💳 Planes

| Función | Gratuito | Pro | Elite |
|---|---|---|---|
| Panel de Batería Corporal + HRV | ✅ | ✅ | ✅ |
| Mapa de recuperación muscular | ✅ | ✅ | ✅ |
| Registro de entrenamientos (historial de 60 días) | ✅ | ✅ | ✅ |
| Historial de entrenamientos ilimitado | — | ✅ | ✅ |
| Las 6 plantillas de entrenamiento | — | ✅ | ✅ |
| Motor de nutrición completo + base de datos de alimentos | — | ✅ | ✅ |
| Visualizador corporal (lienzo frontal/posterior) | — | ✅ | ✅ |
| App complementaria Apple Watch | — | ✅ | ✅ |
| Motor Femme (seguimiento del ciclo) | — | ✅ | ✅ |
| Entrenador IA — Prism 1.7B en el dispositivo | — | ✅ | ✅ |
| Entrenador IA — servidor Prism 8B | — | — | ✅ |
| Entrenador IA — cascada Claude Sonnet | — | — | ✅ |
| Programas personalizados generados por IA | — | — | ✅ |
| **Mensual** | Gratis | $8,99/mes | $17,99/mes |
| **Anual** | Gratis | $69,99/año | $129,99/año |

Suscríbete en [forgecoach.app/subscribe](https://forgecoach.app/subscribe) — pago web con Stripe. No se requiere compra en la app.

---

## 🧪 Pruebas

904 pruebas automatizadas que cubren todos los motores principales — ATR, Batería Corporal, Batería Muscular, enrutamiento de IA, Nutrición, Sueño, SNC, Siri Intents, Suscripción, CloudKit, VBT, comandos de voz y más.

```
watchOS build:    ✅ BUILD SUCCEEDED
iOS tests (904):  ✅ 904/904 passed, 0 failures
```
