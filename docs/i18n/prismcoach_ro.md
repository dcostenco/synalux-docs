# 🏋️ PrismCoach

**Antrenor de fitness AI de nivel militar.** Aplicație iPhone · iPad · Apple Watch. Urmărește recuperarea, prezice oboseala, generează programe de antrenament și te antrenează în timp real — în 23 de limbi. Funcționează complet offline cu un model AI pe dispozitiv (Pro+). Depozit independent: [`forge-watch`](https://github.com/dcostenco/forge-watch).

---

## 🔋 Bateria Corpului

Scorul tău principal de pregătire — o combinație a HRV nocturn, a tendinței frecvenței cardiace de repaus, a calității somnului și a sarcinii de antrenament acumulate în ultimele 7 zile.

*   **Punctaj** — 0–100. ≥ 75 = Proaspăt (verde), 50–74 = Moderat (galben), 25–49 = Obosit (portocaliu), < 25 = Epuizat (roșu).
*   **Integrare HealthKit** — citește HRV-ul nocturn pasiv capturat de Apple Watch. Nu este necesară introducerea manuală.
*   **Recalibrare de bază** — bateria corpului recalculează săptămânal linia de bază mobilă, astfel încât un atlet bine antrenat și un începător să vadă scoruri corect normalizate.
*   **Motorul ATR** — Adaptive Training Readiness sintetizează 7+ semnale biometrice într-un singur indice de pregătire. Ține cont de raportul dintre sarcina acută (ultimele 3 zile) și cea cronică (28 de zile).

<details>
<summary>Vezi Captură de Ecran — Tablou de Bord</summary>

![PrismCoach Dashboard — Body Battery](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png)
*Tabloul de bord al Bateriei Corpului — scor compus de pregătire, tendință săptămânală și scurtături de acțiune rapidă.*

</details>

---

## 💪 Harta de Recuperare Musculară

Urmărirea oboselii per mușchi în 14 regiuni anatomice folosind un canvas de hartă corporală parametrică redat în SwiftUI.

*   **14 grupe musculare** — Piept, Deltoizi Anteriori/Laterali/Posteriori, Bicepși, Tricepși, Trapezi, Dorsali, Core, Zona lombară, Fesieri, Cvadricepși, Ischiogambieri, Gambe.
*   **Model de încărcare** — fiecare mușchi scade de la 100% la 0% în 48–96 de ore după antrenament, în funcție de volumul exercițiului și RPE. Recuperarea urmează o curbă sigmoidă (nu liniară).
*   **Comutator față/spate** — apasă pentru a răsturna silueta. iOS folosește un selector segmentat; watchOS afișează ambele vizualizări ca file cu glisare.
*   **Codificare prin culori** — ≥ 75% verde, 50–75% galben, 25–50% portocaliu, < 25% roșu.
*   **Evidențieri de antrenament** — mușchii vizați de programul de azi pulsează în portocaliu pe canvas.

<details>
<summary>Vezi Captură de Ecran — Harta Musculară</summary>

![PrismCoach Muscle Recovery Map](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png)
*Harta de recuperare musculară — 14 regiuni codificate prin culori în funcție de încărcare. Suprapunerea pulsantă arată mușchii vizați azi.*

</details>

---

## 📋 Programe de Antrenament

Șase șabloane de periodizare bazate pe știință, acoperind toate obiectivele principale de antrenament.

| Program | Structură | Obiectiv |
|---|---|---|
| PPL (Putere/Împingere/Tragere/Picioare) | Împărțire superioară/inferioară pe 6 zile | Hipertrofie + forță |
| 5/3/1 Wendler | Bara + accesorii pe 4 zile | Forță powerlifting |
| GZCLP | Sistem de niveluri pe 3 zile | Progresia liniară a începătorilor |
| Superior/Inferior | Împărțire clasică pe 4 zile | Hipertrofie echilibrată |
| Corp Întreg | Focus pe compuse pe 3 zile | Fitness general |
| Descărcare / Menținere | Recuperare activă o zi | Regenerare |

*   **Programe generate de AI** (Elite) — descrie-ți obiectivul și constrângerile; PrismCoach generează un bloc personalizat de mai multe săptămâni folosind Prism 8B sau Claude Sonnet.
*   **Generator de Programe JSON** — programele sunt reprezentate ca modele Swift tipizate; motorul poate genera un program complet de 8 săptămâni în < 500 ms pe dispozitiv.
*   **Sincronizare Watch** — programul activ se stochează în cache pe Apple Watch pentru antrenament offline (sarcină utilă < 100 KB).

<details>
<summary>Vezi Captură de Ecran — Programe</summary>

![PrismCoach Programs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png)
*Programe de antrenament — șase șabloane de periodizare cu programe personalizate generate de AI pentru Elite.*

</details>

---

## 🍎 Motorul de Nutriție

Jurnal de mese susținut de NLP — descrie mâncarea în limbaj natural, obține macronutrienții.

*   **Înregistrarea meselor prin NLP** — tastează sau dictează "2 ouă, pâine prăjită cu unt, cafea neagră" și motorul analizează entitățile alimentare, cantitățile și unitățile folosind regex + Claude Haiku.
*   **Obiective de macronutrienți** — calculate din greutatea corporală, obiectiv (deficit/surplus/menținere) și nivelul de activitate. Ajustate zilnic pe baza sarcinii de antrenament.
*   **Urmărire calorică** — total zilnic cumulat cu detaliere (proteine / carbohidrați / grăsimi / fibre / apă).
*   **Scor de densitate nutritivă** — semnalează deficiențele de micronutrienți pe baza alimentelor înregistrate.
*   **Memento-uri de hidratare** — notificări push adaptive bazate pe estimarea ratei de transpirație în timpul antrenamentului.

<details>
<summary>Vezi Captură de Ecran — Nutriție</summary>

![PrismCoach Nutrition](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png)
*Tracker de nutriție — înregistrarea meselor prin NLP, obiective zilnice de macronutrienți și urmărirea hidratării.*

</details>

---

## 🤖 Antrenorul AI

Antrenament conversațional care îți cunoaște starea de recuperare, ultima sesiune și contextul programului.

*   **Nivel Gratuit** — fără AI (doar șabloane de programe statice).
*   **Pro — Prism 1.7B pe dispozitiv** — rulează prin llama.cpp cu accelerare Metal. Zero rețea, complet privat. Când RAM-ul liber este ≥ 1.600 MB, folosește Prism Coder 1.7B (pe dispozitiv, Metal); când RAM-ul liber este de 450–799 MB, folosește SmolLM2-360M (185 MB, pe dispozitiv); antrenamentul nu eșuează niciodată, se degradează doar grațios. Răspunde la întrebările despre antrenamentul tău, sugerează corecții de formă, ajustează volumul de azi pe baza pregătirii.
*   **Elite — cascadă Prism 1.7B → 8B → Claude Sonnet** — mai întâi pe dispozitiv; escaladează la serverul de inferență Prism (8B) pentru întrebări complexe; revine la Claude Sonnet pentru antrenament nuanțat.
*   **Fereastra de context** — ForgeMemoryStore injectează ultimele 3 sesiuni, săptămâna activă a programului, încărcăturile musculare actuale și scorul bateriei corpului în fiecare prompt.
*   **Ieșire vocală** — răspunsurile AI sunt citite prin ForgeTTSEngine: Synalux cloud TTS (MP3, 24 kHz) cu AVSpeechSynthesizer ca alternativă offline. Șase tonuri de antrenament: Prietenos, Calm, Entuziasmat, Precis, Empatic, Plin de Speranță.
*   **Antrenament proactiv** — ProactiveCoachEngine oferă informații nesolicitate (ex.: „HRV-ul tău a scăzut cu 15% — ia în considerare reducerea intensității azi") bazate pe 7 tipuri de declanșatoare.

<details>
<summary>Vezi Captură de Ecran — Antrenorul AI</summary>

![PrismCoach AI Coach](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png)
*Antrenorul AI — antrenor conversațional conștient de context cu ieșire vocală și perspective proactive.*

</details>

---

## ⌚ Aplicația Apple Watch

Aplicație însoțitoare completă — nu doar notificări. Urmărirea independentă a sesiunilor de pe încheietură.

*   **6 file Watch** — Tablou de Bord (Bateria Corpului), Harta Musculară, Jurnal de Antrenament, Watch AI Coach, Test de Tap al Sistemului Nervos Central, Setări.
*   **Watch AI Coach** — IA conversațională completă pe încheietură: interogările sunt transmise spre iPhone-ul asociat prin WatchConnectivity; iPhone-ul rulează cascada pe dispozitiv 1.7B → 360M → cloud și trimite răspunsul înapoi; trece la o stare clară „iPhone inaccesibil" când conexiunea eșuează.
*   **Sesiune de antrenament** — înregistrează seriile (exercițiu, greutate, repetări, RPE) direct de pe încheietură. Cronometru de odihnă de 90 de secunde cu numărătoare inversă haptică.
*   **Testul de Tap al Sistemului Nervos Central** — test de tap rapid de 10 secunde înainte de antrenament. Măsoară tapuri/sec; semnalează oboseala neuromusculară dacă este sub linia de bază personală.
*   **Metronom Haptic** — haptice ritmice în timpul circuitelor AMRAP/EMOM.
*   **Sincronizare telefon** — puntea WatchConnectivity trimite bateriile, bateria corpului și marcajele de funcții bidirecțional în timp real.
*   **Detectare Automată a Seriilor** — accelerometrul + giroscopul recunosc începutul/sfârșitul seriei și clasifică tipul de exercițiu. Dezactivează pentru a economisi bateria ceasului.
*   **Antrenament Bazat pe Viteză** — estimarea vitezei barei montate pe încheietură folosind CoreMotion. Semnalează oboseala neuromusculară când viteza barei scade cu > 15%.

<details>
<summary>Vezi Captură de Ecran — Tabloul de Bord Watch</summary>

![PrismCoach Apple Watch](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png)
*Însoțitor Apple Watch — tabloul de bord rapid al Bateriei Corpului cu inelul de recuperare.*

</details>

---

## 🧬 Motorul Femme

Ajustări ale parametrilor în funcție de faza ciclului pentru sportivele de sex feminin (opțional).

*   **4 faze** — Menstruală, Foliculară, Ovulatorie, Luteală.
*   **Ajustări de antrenament** — volumul, țintele de intensitate și recomandările RPE variază pe faze pe baza cercetărilor publicate privind efectele hormonale asupra forței și recuperării.
*   **Corecția bateriei corpului** — liniile de bază ale temperaturii corporale bazale și ale variabilității frecvenței cardiace sunt ajustate pe faze pentru a preveni marcajele false de oboseală la mijlocul ciclului.
*   **Confidențialitate** — datele ciclului nu părăsesc niciodată dispozitivul (CoreData, fără sincronizare).

---

## 🧠 Somn și HRV

Știința recuperării nocturne rulând în tăcere în fundal.

*   **Captarea HRV** — interogări pasive HealthKit pentru mostre HRV nocturne. Nu este necesară măsurarea activă.
*   **Analiza fazelor somnului** — citește datele fazelor de somn ale Apple (treaz/de bază/adânc/REM) pentru a evalua calitatea somnului.
*   **Bucla de antrenament** — SleepTrainingLoop corelează sarcina din ziua precedentă cu HRV-ul din dimineața următoare pentru a construi în timp un model personal de stres–recuperare.
*   **Linia de bază a bateriei corpului** — mediana HRV pe 28 de zile utilizată ca referință personală; abaterile determină scorul bateriei.

---

## 🔊 Voce și TTS

Antrenament AI vorbit în limba ta.

*   **Synalux TTS** — sinteză MP3 în cloud la 24 kHz/96 kbps mono prin portalul Synalux. 6 tonuri de antrenament.
*   **Alternativă offline** — AVSpeechSynthesizer cu selectarea automată a celei mai înalte calități vocale disponibile (premium ≥ îmbunătățit ≥ implicit). Funcționează în toate cele 23 de limbi acceptate.
*   **Atenuarea muzicii** — ForgeTTSEngine atenuează automat Apple Music / Spotify în timpul discursului de antrenament și restabilește volumul după.
*   **Inferența automată a tonului** — conținutul mesajului este scanat pentru cuvinte cheie emoționale (PR, oboseală, accidentare, revenire etc.) și tonul adecvat este selectat automat.
*   **Comenzi vocale** — VoiceCommandEngine gestionează înregistrarea seriilor fără mâini libere ("înregistrează 100 kg 5 repetări RPE 8") și navigarea ("arată-mi harta musculară") prin framework-ul Speech.

---

## 🌍 Limbi

23 de limbi acceptate prin stiva vocală Apple + Synalux TTS.

*   **Coduri de limbă BCP-47** — preferința de limbă per utilizator stocată în LanguageStore; folosită pentru selecția vocii TTS și localizarea promptului de sistem al antrenorului AI.
*   **Antrenament AI** — prompturile sunt scrise în limba selectată de utilizator. Modelele Claude și Prism gestionează toate cele 23 de limbi.
*   **23 de limbi** — Engleză, Spaniolă, Franceză, Portugheză, Germană, Italiană, Olandeză, Poloneză, Rusă, Ucraineană, Română, Cehă, Maghiară, Suedeză, Norvegiană, Finlandeză, Japoneză, Coreeană, Mandarină, Arabă, Hindi, Turcă, Ebraică.

---

## 🏗️ Arhitectură

*   **PrismCoachCore** — pachet Swift partajat (SPM) conținând toate motoarele, modelele și logica de afaceri. Utilizat de aplicația iOS, aplicația Mac Catalyst și extensia watchOS.
*   **llama.cpp (Metal)** — inferență pe dispozitiv pentru modelul Prism 1.7B GGUF printr-un pachet SPM local (`_llama_cpp_local`). Doar iOS/macOS; exclus din watchOS la compilare.
*   **Puntea WatchConnectivity** — `WatchBridge` sincronizează bateriile musculare, bateria corpului și marcajele de funcții bidirecțional între iPhone și Watch în timp real.
*   **Sincronizare CloudKit** — `CloudKitSyncEngine` replicase istoricul antrenamentelor și profilul utilizatorului pe dispozitive folosind tokenuri de modificare CKRecord cu rezolvarea conflictelor.
*   **HealthKit** — citește HRV, fazele somnului, FC de repaus, energia activă și mostrele de antrenament. Scrie rezumatele sesiunilor de antrenament.
*   **Siri Intents** — `LogWorkoutIntent`, `GetBodyBatteryIntent`, `StartRestTimerIntent` pentru integrarea Comenzi Rapide.

---

## 🔒 Confidențialitate

*   **Local în primul rând** — toate datele biometrice rămân pe dispozitiv. Fără SDK de analiză. Fără raportare de erori terță parte.
*   **HealthKit** — acces doar pentru citire cu excepția scrierilor sesiunilor de antrenament. Descris în eticheta de confidențialitate din App Store.
*   **Prompturi AI** — nivelul Pro nu trimite niciodată date la niciun server. Nivelul Elite trimite context de antrenament anonimizat la serverul de inferență Prism (fără PII, fără date HealthKit).
*   **Verificarea abonamentului** — e-mail trimis prin HTTPS la `api.prismcoach.app/subscription/check`. E-mailul stocat în Keychain cu TTL de 24 de ore și fereastră de grație de 48 de ore.
*   **Date de ciclu** — datele Motorului Femme sunt doar CoreData, niciodată sincronizate.

---

## 💳 Planuri

| Funcționalitate | Gratuit | Pro | Elite |
|---|---|---|---|
| Tabloul de bord Bateria Corpului + HRV | ✅ | ✅ | ✅ |
| Harta de recuperare musculară | ✅ | ✅ | ✅ |
| Jurnal de antrenament (istoric 60 de zile) | ✅ | ✅ | ✅ |
| Istoric nelimitat de antrenamente | — | ✅ | ✅ |
| Toate cele 6 șabloane de antrenament | — | ✅ | ✅ |
| Motor de nutriție complet + bază de date alimente | — | ✅ | ✅ |
| Vizualizator corporal (canvas față/spate) | — | ✅ | ✅ |
| Aplicație însoțitoare Apple Watch | — | ✅ | ✅ |
| Motorul Femme (urmărirea ciclului) | — | ✅ | ✅ |
| Antrenor AI — Prism 1.7B pe dispozitiv | — | ✅ | ✅ |
| SmolLM2-360M pe dispozitiv (rezervă RAM scăzut) | — | ✅ | ✅ |
| Watch AI Coach (releu) | — | ✅ | ✅ |
| Antrenor AI — server Prism 8B | — | — | ✅ |
| Antrenor AI — cascadă Claude Sonnet | — | — | ✅ |
| Programe personalizate generate de AI | — | — | ✅ |
| **Lunar** | Gratuit | $8,99/lună | $17,99/lună |
| **Anual** | Gratuit | $69,99/an | $129,99/an |

Abonează-te la [prismcoach.app/subscribe](https://prismcoach.app/subscribe) — checkout web susținut de Stripe. Nu este necesară achiziția din aplicație.

---

## 🧪 Teste

904 teste automate care acoperă toate motoarele de bază — ATR, Bateria Corpului, Bateria Musculară, rutarea AI, Nutriție, Somn, Sistemul Nervos Central, Siri Intents, Abonament, CloudKit, VBT, comenzi vocale și altele.

```
watchOS build:    ✅ BUILD SUCCEEDED
iOS tests (904):  ✅ 904/904 passed, 0 failures
```
