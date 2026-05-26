# 🏋️ PrismCoach

**KI-Fitness-Coach in Militärqualität.** iPhone · iPad · Apple Watch App. Verfolgt die Erholung, sagt Ermüdung vorher, erstellt Trainingsprogramme und coacht Sie in Echtzeit — in 23 Sprachen. Funktioniert vollständig offline mit einem KI-Modell auf dem Gerät (Pro+). Eigenständiges Repository: [`forge-watch`](https://github.com/dcostenco/forge-watch).

---

## 🔋 Körperbatterie

Ihr wichtigster Bereitschaftswert — eine Kombination aus nächtlichem HRV, Ruhepuls-Trend, Schlafqualität und über die letzten 7 Tage aufgebauter Trainingsbelastung.

*   **Bewertung** — 0–100. ≥ 75 = Frisch (grün), 50–74 = Moderat (gelb), 25–49 = Erschöpft (orange), < 25 = Ausgelaugt (rot).
*   **HealthKit-Integration** — liest passiven nächtlichen HRV, der von der Apple Watch erfasst wird. Keine manuelle Eingabe erforderlich.
*   **Baseline-Neukalibrierung** — die Körperbatterie berechnet ihre gleitende Ausgangslinie wöchentlich neu, sodass ein gut trainierter Athlet und ein Anfänger korrekt normalisierte Werte sehen.
*   **ATR-Engine** — Adaptive Training Readiness synthetisiert mehr als 7 biometrische Signale zu einem einzigen Bereitschaftsindex. Berücksichtigt das Verhältnis von akuter (letzte 3 Tage) zu chronischer (28-Tage) Belastung.

<details>
<summary>Screenshot anzeigen — Dashboard</summary>

![PrismCoach Dashboard — Body Battery](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png)
*Körperbatterie-Dashboard — zusammengesetzter Bereitschaftswert, wöchentlicher Trend und Schnellzugriffs-Verknüpfungen.*

</details>

---

## 💪 Muskel-Erholungskarte

Ermüdungsverfolgung pro Muskel in 14 anatomischen Regionen mithilfe eines parametrischen Körperkarten-Canvas, der in SwiftUI gerendert wird.

*   **14 Muskelgruppen** — Brust, Vordere/Seitliche/Hintere Schultern, Bizeps, Trizeps, Trapez, Latissimus, Core, Unterer Rücken, Gesäß, Quadrizeps, Hintere Oberschenkel, Waden.
*   **Lademodell** — jeder Muskel klingt je nach Übungsvolumen und RPE innerhalb von 48–96 Stunden nach dem Training von 100 % auf 0 % ab. Die Erholung folgt einer sigmoiden Kurve (nicht linear).
*   **Vorder-/Rückseiten-Umschalter** — Tippen Sie, um die Silhouette umzudrehen. iOS verwendet einen segmentierten Picker; watchOS zeigt beide Ansichten als wischbare Tabs.
*   **Farbkodierung** — ≥ 75 % grün, 50–75 % gelb, 25–50 % orange, < 25 % rot.
*   **Trainings-Highlights** — die vom heutigen Programm angesteuerten Muskeln pulsieren orange auf dem Canvas.

<details>
<summary>Screenshot anzeigen — Muskelkarte</summary>

![PrismCoach Muscle Recovery Map](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png)
*Muskel-Erholungskarte — 14 Regionen, farblich nach Ladung kodiert. Pulsierende Überlagerung zeigt die heutigen Zielmuskeln.*

</details>

---

## 📋 Trainingsprogramme

Sechs wissenschaftsbasierte Periodisierungsvorlagen, die alle wichtigen Trainingsziele abdecken.

| Programm | Struktur | Ziel |
|---|---|---|
| PPL (Power/Push/Pull/Legs) | 6-Tage Ober-/Unterkörper-Split | Hypertrophie + Kraft |
| 5/3/1 Wendler | 4-Tage Langhantel + Zubehör | Kraftdreikampf-Kraft |
| GZCLP | 3-Tage Tier-System | Lineare Anfängerprogression |
| Ober-/Unterkörper | 4-Tage klassischer Split | Ausgewogene Hypertrophie |
| Ganzkörper | 3-Tage Verbundübungen-Fokus | Allgemeine Fitness |
| Deload / Erhaltung | 1-Tag aktive Erholung | Regeneration |

*   **KI-generierte Programme** (Elite) — beschreiben Sie Ihr Ziel und Ihre Einschränkungen; PrismCoach erstellt einen vollständig individuellen Mehrwochenblock mit Prism 8B oder Claude Sonnet.
*   **JSON-Programm-Generator** — Programme werden als typisierte Swift-Modelle dargestellt; die Engine kann ein vollständiges 8-Wochen-Programm in < 500 ms auf dem Gerät generieren.
*   **Watch-Sync** — das aktive Programm wird für Offline-Coaching auf der Apple Watch zwischengespeichert (Nutzlast < 100 KB).

<details>
<summary>Screenshot anzeigen — Programme</summary>

![PrismCoach Programs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png)
*Trainingsprogramme — sechs Periodisierungsvorlagen mit KI-generierten individuellen Programmen für Elite.*

</details>

---

## 🍎 Ernährungs-Engine

NLP-gestütztes Mahlzeitenprotokoll — beschreiben Sie Lebensmittel in natürlicher Sprache, erhalten Sie Makros.

*   **NLP-Mahlzeitenprotokoll** — tippen oder diktieren Sie „2 Eier, Toast mit Butter, schwarzer Kaffee" und die Engine analysiert Lebensmittelentitäten, Mengen und Einheiten mit Regex + Claude Haiku.
*   **Makro-Ziele** — berechnet aus Körpergewicht, Ziel (Defizit/Aufbau/Erhalt) und Aktivitätsniveau. Wird täglich basierend auf der Trainingsbelastung angepasst.
*   **Kalorientracking** — laufendes Tagessumme mit Aufschlüsselung (Proteine / Kohlenhydrate / Fett / Ballaststoffe / Wasser).
*   **Nährstoffdichte-Bewertung** — markiert Mikronährstofflücken basierend auf protokollierten Lebensmitteln.
*   **Hydrations-Erinnerungen** — adaptive Push-Benachrichtigungen basierend auf der geschätzten Schweißrate beim Training.

<details>
<summary>Screenshot anzeigen — Ernährung</summary>

![PrismCoach Nutrition](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png)
*Ernährungs-Tracker — NLP-Mahlzeitenprotokoll, tägliche Makro-Ziele und Hydrations-Tracking.*

</details>

---

## 🤖 KI-Coach

Gesprächsbasiertes Coaching, das Ihren Erholungszustand, Ihre letzte Einheit und den Programmkontext kennt.

*   **Gratis-Stufe** — keine KI (nur statische Programmvorlagen).
*   **Pro — Prism 1.7B auf dem Gerät** — läuft via llama.cpp mit Metal-Beschleunigung. Kein Netzwerk, vollständig privat. Beantwortet Fragen zu Ihrem Training, schlägt Korrekturen der Ausführungstechnik vor, passt das heutige Volumen basierend auf der Bereitschaft an.
*   **Elite — Prism 1.7B → 8B → Claude Sonnet Kaskade** — zuerst auf dem Gerät; eskaliert für komplexe Fragen zum Prism-Inferenzserver (8B); greift für nuanciertes Coaching auf Claude Sonnet zurück.
*   **Kontextfenster** — ForgeMemoryStore injiziert die letzten 3 Einheiten, die aktive Programmwoche, aktuelle Muskelladungen und den Körperbatterie-Score in jeden Prompt.
*   **Sprachausgabe** — KI-Antworten werden über ForgeTTSEngine vorgelesen: Synalux Cloud TTS (MP3, 24 kHz) mit AVSpeechSynthesizer-Offline-Fallback. Sechs Coaching-Töne: Freundlich, Ruhig, Begeistert, Präzise, Einfühlsam, Hoffnungsvoll.
*   **Proaktives Coaching** — ProactiveCoachEngine liefert unaufgeforderte Erkenntnisse (z. B. „Ihr HRV ist um 15 % gefallen — erwägen Sie heute eine Intensitätsreduktion") basierend auf 7 Auslösertypen.

<details>
<summary>Screenshot anzeigen — KI-Coach</summary>

![PrismCoach AI Coach](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png)
*KI-Coach — kontextbewusster Gesprächs-Coach mit Sprachausgabe und proaktiven Erkenntnissen.*

</details>

---

## ⌚ Apple Watch App

Vollständige Companion-App — nicht nur Benachrichtigungen. Unabhängiges Sitzungs-Tracking am Handgelenk.

*   **5 Watch-Tabs** — Dashboard (Körperbatterie), Muskelkarte, Workout-Logger, ZNS-Tap-Test, Einstellungen.
*   **Trainingseinheit** — Sätze direkt vom Handgelenk protokollieren (Übung, Gewicht, Wiederholungen, RPE). 90-Sekunden-Pausentimer mit haptischem Countdown.
*   **ZNS-Tap-Test** — 10-Sekunden-Schnelltipp-Test vor dem Training. Misst Taps/Sek.; markiert neuromuskuläre Ermüdung bei Unterschreitung der persönlichen Baseline.
*   **Haptischer Taktgeber** — rhythmische Haptik während AMRAP/EMOM-Circuits.
*   **Telefon-Sync** — WatchConnectivity-Brücke überträgt Batterien, Körperbatterie und Feature-Flags bidirektional in Echtzeit.
*   **Automatische Satzerkennung** — Beschleunigungssensor + Gyroskop erkennen Satz-Start/Ende und klassifizieren den Übungstyp. Deaktivieren zum Sparen der Watch-Batterie.
*   **Geschwindigkeitsbasiertes Training** — handgelenkmontierte Hantelgeschwindigkeitsschätzung mit CoreMotion. Markiert neuromuskuläre Ermüdung bei Geschwindigkeitsabfall > 15 %.

<details>
<summary>Screenshot anzeigen — Watch-Dashboard</summary>

![PrismCoach Apple Watch](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png)
*Apple Watch Companion — Körperbatterie-Überblicks-Dashboard mit Erholungsring.*

</details>

---

## 🧬 Femme Engine

Zyklusphasenangepasste Metrik-Anpassungen für Sportlerinnen (opt-in).

*   **4 Phasen** — Menstruell, Follikulär, Ovulatorisch, Luteal.
*   **Trainingsanpassungen** — Volumen, Intensitätsziele und RPE-Empfehlungen verschieben sich je Phase basierend auf veröffentlichter Forschung zu hormonellen Auswirkungen auf Kraft und Erholung.
*   **Körperbatterie-Korrektur** — Basaltemperatur- und HRV-Baselines werden phasenweise angepasst, um falsche Ermüdungsmeldungen in der Zyklus-Mitte zu verhindern.
*   **Datenschutz** — Zyklus-Daten verlassen das Gerät nie (CoreData, keine Synchronisierung).

---

## 🧠 Schlaf & HRV

Nächtliche Erholungswissenschaft, die still im Hintergrund läuft.

*   **HRV-Erfassung** — passive HealthKit-Abfragen für nächtliche HRV-Stichproben. Keine aktive Messung erforderlich.
*   **Schlafphasenanalyse** — liest Apples Schlafphasendaten (wach/leicht/tief/REM) zur Bewertung der Schlafqualität.
*   **Trainingsschleife** — SleepTrainingLoop korreliert die Belastung des Vortages mit dem HRV am nächsten Morgen, um über Zeit ein persönliches Stress-Erholungs-Modell aufzubauen.
*   **Körperbatterie-Baseline** — gleitender 28-Tage-Median-HRV als persönliche Referenz; Abweichungen treiben den Batterie-Score.

---

## 🔊 Sprache & TTS

KI-Coaching laut in Ihrer Sprache gesprochen.

*   **Synalux TTS** — Cloud-MP3-Synthese bei 24 kHz/96 kbps Mono über das Synalux-Portal. 6 Coaching-Töne.
*   **Offline-Fallback** — AVSpeechSynthesizer mit automatischer Auswahl der höchsten verfügbaren Stimmqualität (Premium ≥ Erweitert ≥ Standard). Funktioniert in allen 23 unterstützten Sprachen.
*   **Musik-Ducking** — ForgeTTSEngine dämpft Apple Music / Spotify automatisch während der Coaching-Sprache und stellt die Lautstärke danach wieder her.
*   **Automatische Ton-Inferenz** — der Nachrichteninhalt wird auf emotionale Schlüsselwörter (PR, Ermüdung, Verletzung, Comeback usw.) gescannt und der passende Ton automatisch ausgewählt.
*   **Sprachbefehle** — VoiceCommandEngine verwaltet freihändige Satzprotokollierung („100kg 5 Wdh RPE 8 eintragen") und Navigation („zeig meine Muskelkarte") über das Speech-Framework.

---

## 🌍 Sprachen

23 unterstützte Sprachen über Apples Sprach-Stack + Synalux TTS.

*   **BCP-47-Sprachcodes** — benutzerspezifische Sprachpräferenz im LanguageStore gespeichert; verwendet für TTS-Stimmauswahl und KI-Coach-Systemanfrage-Locale.
*   **KI-Coaching** — Prompts werden in der vom Benutzer gewählten Sprache verfasst. Claude- und Prism-Modelle verarbeiten alle 23 Sprachen.
*   **23 Sprachen** — Englisch, Spanisch, Französisch, Portugiesisch, Deutsch, Italienisch, Niederländisch, Polnisch, Russisch, Ukrainisch, Rumänisch, Tschechisch, Ungarisch, Schwedisch, Norwegisch, Finnisch, Japanisch, Koreanisch, Mandarin, Arabisch, Hindi, Türkisch, Hebräisch.

---

## 🏗️ Architektur

*   **PrismCoachCore** — gemeinsames Swift-Paket (SPM) mit allen Engines, Modellen und Geschäftslogik. Wird von der iOS-App, der Mac-Catalyst-App und der watchOS-Erweiterung verwendet.
*   **llama.cpp (Metal)** — Geräte-Inferenz für das Prism 1.7B GGUF-Modell über ein lokales SPM-Paket (`_llama_cpp_local`). Nur iOS/macOS; zur Kompilierzeit von watchOS ausgeschlossen.
*   **WatchConnectivity-Brücke** — `WatchBridge` synchronisiert Muskelbatterien, Körperbatterie und Feature-Flags bidirektional zwischen iPhone und Watch in Echtzeit.
*   **CloudKit-Sync** — `CloudKitSyncEngine` repliziert Trainingshistorie und Benutzerprofil über Geräte hinweg mit CKRecord-Change-Tokens und Konfliktauflösung.
*   **HealthKit** — liest HRV, Schlafphasen, Ruhepuls, aktive Energie und Trainingsproben. Schreibt Trainingseinheits-Zusammenfassungen.
*   **Siri Intents** — `LogWorkoutIntent`, `GetBodyBatteryIntent`, `StartRestTimerIntent` für die Kurzbefehle-Integration.

---

## 🔒 Datenschutz

*   **Local-First** — alle biometrischen Daten verbleiben auf dem Gerät. Kein Analytics-SDK. Kein Drittanbieter-Absturzbericht.
*   **HealthKit** — nur Lesezugriff außer beim Schreiben von Trainingseinheits-Zusammenfassungen. Im App-Store-Datenschutzetikett beschrieben.
*   **KI-Prompts** — Pro-Stufe sendet niemals Daten an einen Server. Elite-Stufe sendet anonymisierten Trainingskontext an den Prism-Inferenzserver (keine PII, keine HealthKit-Daten).
*   **Abonnement-Prüfung** — E-Mail per HTTPS an `api.prismcoach.app/subscription/check` gesendet. E-Mail im Keychain mit 24-Stunden-TTL und 48-Stunden-Kulanzfenster gespeichert.
*   **Zyklusdaten** — Femme-Engine-Daten sind nur CoreData, nie synchronisiert.

---

## 💳 Tarife

| Funktion | Kostenlos | Pro | Elite |
|---|---|---|---|
| Körperbatterie + HRV-Dashboard | ✅ | ✅ | ✅ |
| Muskel-Erholungskarte | ✅ | ✅ | ✅ |
| Workout-Protokoll (60-Tage-Verlauf) | ✅ | ✅ | ✅ |
| Unbegrenzter Workout-Verlauf | — | ✅ | ✅ |
| Alle 6 Trainingsvorlagen | — | ✅ | ✅ |
| Vollständige Ernährungs-Engine + Lebensmittel-DB | — | ✅ | ✅ |
| Körper-Visualisierer (Vorder-/Rückseiten-Canvas) | — | ✅ | ✅ |
| Apple Watch Companion App | — | ✅ | ✅ |
| Femme Engine (Zyklus-Tracking) | — | ✅ | ✅ |
| KI-Coach — Prism 1.7B auf dem Gerät | — | ✅ | ✅ |
| KI-Coach — Prism 8B Server | — | — | ✅ |
| KI-Coach — Claude Sonnet Kaskade | — | — | ✅ |
| KI-generierte individuelle Programme | — | — | ✅ |
| **Monatlich** | Kostenlos | 8,99 $/Monat | 17,99 $/Monat |
| **Jährlich** | Kostenlos | 69,99 $/Jahr | 129,99 $/Jahr |

Abonnieren Sie auf [prismcoach.app/subscribe](https://prismcoach.app/subscribe) — Stripe-gestützter Web-Checkout. Kein In-App-Kauf erforderlich.

---

## 🧪 Tests

904 automatisierte Tests, die alle Kernengines abdecken — ATR, Körperbatterie, Muskelbatterie, KI-Routing, Ernährung, Schlaf, ZNS, Siri Intents, Abonnement, CloudKit, VBT, Sprachbefehle und mehr.

```
watchOS build:    ✅ BUILD SUCCEEDED
iOS tests (904):  ✅ 904/904 passed, 0 failures
```
