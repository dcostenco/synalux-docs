# 🧩 Applied Behavior Analysis (ABA)

The Synalux ABA module is a full-lifecycle clinical ecosystem designed for Doctors (BCBAs) and Medical Technicians (RBTs). It automates the "paperwork nightmare" of ABA therapy through intelligent data collection, automated report drafting, and seamless insurance management.

---

## 📱 Desktop & iPad-First Clinical Workflow
Whether you are at your desk or in a 1-on-1 session with a child, Synalux adapts to your device. The interface is optimized for high-speed data entry and clear visual feedback.

<details>
<summary>View Interface / Diagram</summary>

![Synalux iPad Clinical Interface](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/generated/voice_dictation_ipad_mockup.png)
*iPad-optimized interface for Natural Environment Teaching (NET) and DTT.*

</details>

---

## 🎙️ Ambient SOAP Notes (Zero-Paperwork)
Focus 100% on the patient. Synalux listens to your session and instantly drafts a professional clinical note.
*   **WASM Whisper Engine:** On-device transcription ensures HIPAA-compliant privacy.
*   **Smart Drafting:** Automatically identifies Antecedents, Behaviors, and Consequences from the conversation.
*   **One-Click Sign-off:** Review, edit, and sign your notes directly from your tablet.

<details>
<summary>View Interface / Diagram</summary>

![Clinical Voice Dictation Interface](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/03_voice_dictation.png)

</details>

---

## 🌳 Program & Target Management
Manage your entire curriculum in a single, intuitive tree view. Track mastery, stagnation, and maintenance across all programs.
*   **Program Tree:** Hierarchical view of Programs → Goals → Targets.
*   **Progress Bars:** Real-time visual indicators of target completion.
*   **Mastery Tracking:** Automatically flags targets ready for mastery (e.g., 80% over 3 sessions).

<details>
<summary>View Interface / Diagram</summary>

![Program Tree & Data Tracking](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/07_abc_data_collection.png)

</details>

---

## 🧠 Data-Driven Mastery Predictions
Stop guessing when a skill will be mastered. Synalux uses a deterministic velocity multiplier to project mastery timelines.
*   **Clinical Velocity:** Calculates growth per session (Current Score * 0.15).
*   **Timeline Badges:** Displays estimates like "~4 sessions" or "Near mastery" directly on the clinician's dashboard.

---

## 📋 Professional Assessment Suite (FBA/BIP)
Generate insurance-ready assessments in minutes, not hours.
*   **FBA Drafts:** Automate Functional Behavioral Assessments with hypothesized functions.
*   **BIP Builder:** Create Behavior Intervention Plans with antecedent modifications and crisis procedures.
*   **Progress Reports:** One-click aggregation of all session data, graphs, and mastery trends for authorization renewals.

<details>
<summary>View Interface / Diagram</summary>

![FBA & BIP Reports](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/05_fba_report.png)

</details>

---

## 📋 Adaptive Assessment Log

A **score log** for externally-administered standardized assessments (adaptive functioning, verbal-behavior, cognitive, language, behavior-rating, autism-specific, sensory). The credentialed clinician administers and scores the instrument on the publisher's official platform; Synalux stores the typed-in standard scores alongside the rest of the chart and trends them over time.

* **Instrument-agnostic by design:** one module covers every supported instrument the clinician chooses (Vineland-3, ABAS-3, VB-MAPP, ABLLS-R, AFLS, Bayley-4, BASC-3, ADOS-2, and more).
* **Not an instrument:** Synalux does not administer, score, or reproduce any standardized assessment. The schema uses generic psychometric vocabulary so it never becomes a derivative of any one instrument.
* **AI assistant integration:** when drafting medical-necessity letters, BIPs, or DDA narratives, the BCBA assistant pulls the latest typed-in scores and quotes them verbatim — it never simulates, predicts, or normatively interprets.
* **Audit:** PHI-tier triple-logging on every create / update / delete. Source-PDF attachments are encrypted at rest, served via short-TTL access URLs, audit-logged on every view, and excluded from AI training and embedding pipelines.

🔗 [Read the full Adaptive Assessment Log documentation](./adaptive_assessment_log.md)

---

## 💳 Billing & Authorization Tracking
Avoid denials with built-in insurance logic.
*   **CPT Integration:** Direct support for 97151, 97153, 97155, and 97156.
*   **Authorization Vault:** Track authorized units vs. utilized units in real-time.
*   **Eligibility Check:** Auto-verify insurance coverage before the session starts.

<details>
<summary>View Interface / Diagram</summary>

![Billing & Payments Dashboard](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/13_billing_payments.png)

</details>

---

## 👥 Role-Based Collaboration
*   **Doctors (BCBA):** Design programs, analyze graphs, and provide supervision.
*   **Medical Technicians (RBT):** Record session notes and collect real-time data.
*   **Caregivers:** View progress and sign consent forms through the Secure Patient Portal.

<details>
<summary>View Interface / Diagram</summary>

![Team Collaboration & Chat](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/10_team_chat.png)

</details>

---

## 🔐 Security & Compliance
*   **HIPAA Audit Trails:** Every access, edit, and deletion is tracked.
*   **E-Signatures:** Secure consent via BoldSign integration.
*   **Offline-First:** Data saves instantly even if the clinic Wi-Fi drops.

<details>
<summary>View Interface / Diagram</summary>

![Security Audit Logs](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/generated/security_audit_logs_ui.png)

</details>