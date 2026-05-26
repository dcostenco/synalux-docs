# 🏋️ PrismCoach

**Coach fitness IA de niveau militaire.** Application iPhone · iPad · Apple Watch. Suit la récupération, prédit la fatigue, génère des programmes d'entraînement et vous accompagne en temps réel — dans 23 langues. Fonctionne entièrement hors ligne avec un modèle IA embarqué (Pro+). Dépôt autonome : [`forge-watch`](https://github.com/dcostenco/forge-watch).

---

## 🔋 Batterie Corporelle

Votre score de disponibilité principal — une combinaison de la HRV nocturne, de la tendance de la fréquence cardiaque au repos, de la qualité du sommeil et de la charge d'entraînement accumulée sur les 7 derniers jours.

*   **Notation** — 0–100. ≥ 75 = Frais (vert), 50–74 = Modéré (jaune), 25–49 = Fatigué (orange), < 25 = Épuisé (rouge).
*   **Intégration HealthKit** — lit la HRV nocturne passive capturée par l'Apple Watch. Aucune saisie manuelle requise.
*   **Recalibrage de référence** — la batterie corporelle recalcule sa ligne de base mobile chaque semaine, de sorte qu'un athlète entraîné et un débutant voient des scores correctement normalisés.
*   **Moteur ATR** — la Disponibilité d'Entraînement Adaptative synthétise plus de 7 signaux biométriques en un seul indice de disponibilité. Tient compte du rapport entre la charge aiguë (3 derniers jours) et chronique (28 jours).

<details>
<summary>Voir la Capture d'Écran — Tableau de Bord</summary>

![PrismCoach Dashboard — Body Battery](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_01_dashboard.png)
*Tableau de bord Batterie Corporelle — score de disponibilité composite, tendance hebdomadaire et raccourcis d'action rapide.*

</details>

---

## 💪 Carte de Récupération Musculaire

Suivi de la fatigue par muscle dans 14 régions anatomiques à l'aide d'un canvas de carte corporelle paramétrique rendu en SwiftUI.

*   **14 groupes musculaires** — Pectoraux, Deltoïdes Antérieur/Latéral/Postérieur, Biceps, Triceps, Trapèzes, Dorsaux, Sangle abdominale, Bas du dos, Fessiers, Quadriceps, Ischio-jambiers, Mollets.
*   **Modèle de charge** — chaque muscle décroît de 100 % à 0 % en 48 à 96 heures après l'entraînement selon le volume d'exercice et le RPE. La récupération suit une courbe sigmoïde (non linéaire).
*   **Bascule avant/arrière** — appuyez pour retourner la silhouette. iOS utilise un sélecteur segmenté ; watchOS affiche les deux vues sous forme d'onglets à glisser.
*   **Code couleur** — ≥ 75 % vert, 50–75 % jaune, 25–50 % orange, < 25 % rouge.
*   **Temps forts de l'entraînement** — les muscles ciblés par le programme du jour clignotent en orange sur le canvas.

<details>
<summary>Voir la Capture d'Écran — Carte Musculaire</summary>

![PrismCoach Muscle Recovery Map](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_02_muscles.png)
*Carte de récupération musculaire — 14 régions codées par couleur selon la charge. La superposition clignotante indique les muscles cibles du jour.*

</details>

---

## 📋 Programmes d'Entraînement

Six modèles de périodisation basés sur la science couvrant tous les principaux objectifs d'entraînement.

| Programme | Structure | Objectif |
|---|---|---|
| PPL (Puissance/Poussé/Tiré/Jambes) | Fractionnement haut/bas sur 6 jours | Hypertrophie + force |
| 5/3/1 Wendler | Barre + accessoires sur 4 jours | Force en powerlifting |
| GZCLP | Système à niveaux sur 3 jours | Progression linéaire débutant |
| Haut/Bas | Fractionnement classique sur 4 jours | Hypertrophie équilibrée |
| Corps Entier | Accent sur les composés sur 3 jours | Remise en forme générale |
| Décharge / Maintien | Récupération active sur 1 jour | Régénération |

*   **Programmes générés par IA** (Elite) — décrivez votre objectif et vos contraintes ; PrismCoach génère un bloc personnalisé sur plusieurs semaines avec Prism 8B ou Claude Sonnet.
*   **Générateur de Programmes JSON** — les programmes sont représentés sous forme de modèles Swift typés ; le moteur peut générer un programme complet de 8 semaines en < 500 ms sur l'appareil.
*   **Synchronisation Watch** — le programme actif est mis en cache sur l'Apple Watch pour un coaching hors ligne (charge utile < 100 Ko).

<details>
<summary>Voir la Capture d'Écran — Programmes</summary>

![PrismCoach Programs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_03_programs.png)
*Programmes d'entraînement — six modèles de périodisation avec des programmes personnalisés générés par IA pour Elite.*

</details>

---

## 🍎 Moteur Nutritionnel

Journal de repas alimenté par NLP — décrivez la nourriture en langage naturel, obtenez les macros.

*   **Journalisation des repas par NLP** — tapez ou dictez « 2 œufs, toast avec beurre, café noir » et le moteur analyse les entités alimentaires, les quantités et les unités à l'aide de regex + Claude Haiku.
*   **Objectifs macros** — calculés à partir du poids corporel, de l'objectif (sèche/prise de masse/maintien) et du niveau d'activité. Ajustés quotidiennement selon la charge d'entraînement.
*   **Suivi calorique** — total journalier cumulé avec décomposition (protéines / glucides / lipides / fibres / eau).
*   **Score de densité nutritionnelle** — signale les carences en micronutriments selon les aliments consignés.
*   **Rappels d'hydratation** — notifications push adaptatives basées sur l'estimation du taux de transpiration pendant l'entraînement.

<details>
<summary>Voir la Capture d'Écran — Nutrition</summary>

![PrismCoach Nutrition](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/iphone_pro_04_nutrition.png)
*Suivi nutritionnel — journalisation NLP des repas, objectifs macros quotidiens et suivi de l'hydratation.*

</details>

---

## 🤖 Coach IA

Coaching conversationnel qui connaît votre état de récupération, votre dernière séance et le contexte de votre programme.

*   **Niveau Gratuit** — pas d'IA (modèles de programmes statiques uniquement).
*   **Pro — Prism 1.7B embarqué** — fonctionne via llama.cpp avec accélération Metal. Zéro réseau, entièrement privé. Répond aux questions sur votre entraînement, suggère des corrections de forme, ajuste le volume du jour selon la disponibilité.
*   **Elite — cascade Prism 1.7B → 8B → Claude Sonnet** — embarqué en premier ; escalade vers le serveur d'inférence Prism (8B) pour les questions complexes ; bascule sur Claude Sonnet pour un coaching nuancé.
*   **Fenêtre de contexte** — ForgeMemoryStore injecte les 3 dernières séances, la semaine active du programme, les charges musculaires actuelles et le score de batterie corporelle dans chaque prompt.
*   **Sortie vocale** — les réponses de l'IA sont vocalisées via ForgeTTSEngine : Synalux cloud TTS (MP3, 24 kHz) avec repli AVSpeechSynthesizer hors ligne. Six tons de coaching : Amical, Calme, Enthousiaste, Précis, Empathique, Plein d'Espoir.
*   **Coaching proactif** — ProactiveCoachEngine remonte des informations non sollicitées (ex. : « Votre HRV a chuté de 15 % — envisagez de réduire l'intensité aujourd'hui ») basées sur 7 types de déclencheurs.

<details>
<summary>Voir la Capture d'Écran — Coach IA</summary>

![PrismCoach AI Coach](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/ipad_05_aicoach.png)
*Coach IA — coach conversationnel contextuel avec sortie vocale et informations proactives.*

</details>

---

## ⌚ Application Apple Watch

Application compagnon complète — pas seulement des notifications. Suivi de session indépendant au poignet.

*   **5 onglets Watch** — Tableau de bord (Batterie Corporelle), Carte Musculaire, Journal d'Entraînement, Test de Tap SNC, Paramètres.
*   **Session d'entraînement** — enregistrez les séries (exercice, poids, répétitions, RPE) directement depuis le poignet. Minuterie de repos de 90 secondes avec compte à rebours haptique.
*   **Test de Tap SNC** — test de tap rapide de 10 secondes avant l'entraînement. Mesure les taps/sec ; signale la fatigue neuromusculaire si en dessous de la ligne de base personnelle.
*   **Métronome Haptique** — haptiques rythmiques durant les circuits AMRAP/EMOM.
*   **Synchronisation téléphone** — le pont WatchConnectivity pousse les batteries, la batterie corporelle et les indicateurs de fonctionnalité de manière bidirectionnelle en temps réel.
*   **Détection Automatique des Séries** — l'accéléromètre + gyroscope reconnaissent le début/fin de série et classifient le type d'exercice. Désactivez pour économiser la batterie de la montre.
*   **Entraînement Basé sur la Vélocité** — estimation de la vitesse de barre montée au poignet avec CoreMotion. Signale la fatigue neuromusculaire quand la vitesse de la barre chute de > 15 %.

<details>
<summary>Voir la Capture d'Écran — Tableau de Bord Watch</summary>

![PrismCoach Apple Watch](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/screenshots/watch_01_dashboard.png)
*Compagnon Apple Watch — tableau de bord Batterie Corporelle d'un coup d'œil avec anneau de récupération.*

</details>

---

## 🧬 Moteur Femme

Ajustements des métriques selon la phase du cycle pour les athlètes féminines (optionnel).

*   **4 phases** — Menstruelle, Folliculaire, Ovulatoire, Lutéale.
*   **Ajustements d'entraînement** — le volume, les objectifs d'intensité et les recommandations RPE varient selon la phase, d'après des recherches publiées sur les effets hormonaux sur la force et la récupération.
*   **Correction de la batterie corporelle** — les lignes de base de la température corporelle basale et de la variabilité de la fréquence cardiaque sont ajustées par phase pour éviter les fausses alertes de fatigue en milieu de cycle.
*   **Confidentialité** — les données du cycle ne quittent jamais l'appareil (CoreData, pas de synchronisation).

---

## 🧠 Sommeil et HRV

Science de la récupération nocturne fonctionnant silencieusement en arrière-plan.

*   **Capture HRV** — requêtes passives HealthKit pour les échantillons HRV nocturnes. Aucune mesure active requise.
*   **Analyse des phases de sommeil** — lit les données de phases de sommeil d'Apple (éveil/léger/profond/REM) pour noter la qualité du sommeil.
*   **Boucle d'entraînement** — SleepTrainingLoop corrèle la charge du jour précédent avec la HRV du lendemain matin pour construire un modèle personnel stress–récupération au fil du temps.
*   **Ligne de base de la batterie corporelle** — médiane HRV sur 28 jours utilisée comme référence personnelle ; les écarts alimentent le score de la batterie.

---

## 🔊 Voix et TTS

Coaching IA parlé dans votre langue.

*   **Synalux TTS** — synthèse MP3 cloud à 24 kHz/96 kbps mono via le portail Synalux. 6 tons de coaching.
*   **Repli hors ligne** — AVSpeechSynthesizer avec sélection automatique de la meilleure qualité de voix disponible (premium ≥ améliorée ≥ par défaut). Fonctionne dans les 23 langues prises en charge.
*   **Atténuation musicale** — ForgeTTSEngine atténue automatiquement Apple Music / Spotify pendant le discours de coaching et restaure le volume ensuite.
*   **Inférence automatique du ton** — le contenu du message est analysé pour détecter les mots-clés émotionnels (PR, fatigue, blessure, retour, etc.) et le ton approprié est sélectionné automatiquement.
*   **Commandes vocales** — VoiceCommandEngine gère la journalisation des séries en mains libres (« enregistrer 100 kg 5 répétitions RPE 8 ») et la navigation (« afficher ma carte musculaire ») via le framework Speech.

---

## 🌍 Langues

23 langues prises en charge via la pile vocale d'Apple + Synalux TTS.

*   **Codes de langue BCP-47** — préférence linguistique par utilisateur stockée dans LanguageStore ; utilisée pour la sélection de voix TTS et la locale du prompt système du coach IA.
*   **Coaching IA** — les prompts sont rédigés dans la langue choisie par l'utilisateur. Les modèles Claude et Prism gèrent les 23 langues.
*   **23 langues** — Anglais, Espagnol, Français, Portugais, Allemand, Italien, Néerlandais, Polonais, Russe, Ukrainien, Roumain, Tchèque, Hongrois, Suédois, Norvégien, Finnois, Japonais, Coréen, Mandarin, Arabe, Hindi, Turc, Hébreu.

---

## 🏗️ Architecture

*   **PrismCoachCore** — package Swift partagé (SPM) contenant tous les moteurs, modèles et logique métier. Consommé par l'app iOS, l'app Mac Catalyst et l'extension watchOS.
*   **llama.cpp (Metal)** — inférence sur l'appareil pour le modèle Prism 1.7B GGUF via un package SPM local (`_llama_cpp_local`). iOS/macOS uniquement ; exclu de watchOS à la compilation.
*   **Pont WatchConnectivity** — `WatchBridge` synchronise les batteries musculaires, la batterie corporelle et les indicateurs de fonctionnalité de manière bidirectionnelle entre l'iPhone et la Watch en temps réel.
*   **Synchronisation CloudKit** — `CloudKitSyncEngine` réplique l'historique des entraînements et le profil utilisateur sur les appareils en utilisant des tokens de changement CKRecord avec résolution des conflits.
*   **HealthKit** — lit la HRV, les phases de sommeil, la FC au repos, l'énergie active et les échantillons d'entraînement. Écrit les résumés de sessions d'entraînement.
*   **Siri Intents** — `LogWorkoutIntent`, `GetBodyBatteryIntent`, `StartRestTimerIntent` pour l'intégration avec Raccourcis.

---

## 🔒 Confidentialité

*   **Local d'abord** — toutes les données biométriques restent sur l'appareil. Pas de SDK d'analyse. Pas de rapport de crash tiers.
*   **HealthKit** — accès en lecture seule sauf pour l'écriture des sessions d'entraînement. Décrit dans l'étiquette de confidentialité de l'App Store.
*   **Prompts IA** — le niveau Pro n'envoie jamais de données à aucun serveur. Le niveau Elite envoie un contexte d'entraînement anonymisé au serveur d'inférence Prism (pas de PII, pas de données HealthKit).
*   **Vérification d'abonnement** — e-mail envoyé via HTTPS à `api.prismcoach.app/subscription/check`. E-mail stocké dans Keychain avec TTL de 24 heures et fenêtre de grâce de 48 heures.
*   **Données de cycle** — les données du Moteur Femme sont uniquement CoreData, jamais synchronisées.

---

## 💳 Abonnements

| Fonctionnalité | Gratuit | Pro | Elite |
|---|---|---|---|
| Tableau de bord Batterie Corporelle + HRV | ✅ | ✅ | ✅ |
| Carte de récupération musculaire | ✅ | ✅ | ✅ |
| Journal d'entraînement (historique 60 jours) | ✅ | ✅ | ✅ |
| Historique d'entraînement illimité | — | ✅ | ✅ |
| Les 6 modèles d'entraînement | — | ✅ | ✅ |
| Moteur nutritionnel complet + base alimentaire | — | ✅ | ✅ |
| Visualiseur corporel (canvas avant/arrière) | — | ✅ | ✅ |
| Application compagnon Apple Watch | — | ✅ | ✅ |
| Moteur Femme (suivi du cycle) | — | ✅ | ✅ |
| Coach IA — Prism 1.7B embarqué | — | ✅ | ✅ |
| Coach IA — serveur Prism 8B | — | — | ✅ |
| Coach IA — cascade Claude Sonnet | — | — | ✅ |
| Programmes personnalisés générés par IA | — | — | ✅ |
| **Mensuel** | Gratuit | 8,99 $/mois | 17,99 $/mois |
| **Annuel** | Gratuit | 69,99 $/an | 129,99 $/an |

Abonnez-vous sur [prismcoach.app/subscribe](https://prismcoach.app/subscribe) — paiement web via Stripe. Aucun achat intégré requis.

---

## 🧪 Tests

904 tests automatisés couvrant tous les moteurs principaux — ATR, Batterie Corporelle, Batterie Musculaire, routage IA, Nutrition, Sommeil, SNC, Siri Intents, Abonnement, CloudKit, VBT, commandes vocales et plus.

```
watchOS build:    ✅ BUILD SUCCEEDED
iOS tests (904):  ✅ 904/904 passed, 0 failures
```
