# Applied Behavior Analysis (ABA)

<a name="clinical-templates"></a>
## Clinical Templates

The Synalux ABA module provides a comprehensive suite of clinical templates to support various stages of therapy and assessment. These include Functional Behavioral Assessments (FBA), Behavior Intervention Plans (BIP), Antecedent-Behavior-Consequence (ABC) Data Collection, detailed Session Notes, Progress Reports, and Discharge Summaries. Each template is designed to streamline the documentation process, ensuring that all necessary information is captured accurately and efficiently.

<a name="billing-codes"></a>
## Billing Codes

Accurate billing is crucial for ABA therapy providers. The Synalux platform supports the use of relevant CPT codes such as 97151 (Assessment), 97152 (Supporting Assessment), 97153 (Protocol Development), 97154 (Group Treatment), 97155 (Modification of Protocol), 97156 (Family/Guardian Training and Support), 97157 (Group/Family Counseling/Support), 97158 (Group Adaptive Behavior Treatment), 0362T, and 0373T. These codes are integrated directly into the platform, facilitating easy and accurate billing processes.

<a name="rbac-roles"></a>
## RBAC Roles

The Role-Based Access Control (RBAC) system within Synalux ensures that each team member has access only to the information they need. The roles include Board Certified Behavior Analysts (BCBA) with full clinical access, Registered Behavior Technicians (RBT) who can enter session notes, and Office Managers who manage administrative tasks. This segregation of duties enhances security and efficiency.

<a name="voice-dictation"></a>
## Voice Dictation

Synalux incorporates advanced voice dictation technology that allows therapists to record sessions in an ambient environment. These recordings are then automatically transcribed into structured SOAP (Subjective, Objective, Assessment, Plan) notes, significantly reducing the time spent on manual documentation.

<a name="e-signatures"></a>
## E-Signatures

Parent/guardian consent for ABA therapy can now be handled electronically through Synalux's integration with BoldSign. This feature not only simplifies the process but also ensures that all consents are stored securely and are easily accessible whenever required.

<a name="data-tracking"></a>
## Data Tracking

Comprehensive data tracking is at the heart of effective ABA therapy. The platform allows therapists to monitor behavioral targets, skill acquisition, frequency, and duration data in real-time. This detailed tracking enables continuous improvement in treatment plans and patient outcomes.

<a name="insurance"></a>
## Insurance

Navigating insurance requirements for ABA services can be complex. Synalux simplifies this by providing autism/ABA-specific payer rules and prior authorization tracking. These features help ensure that providers are reimbursed promptly and accurately, reducing administrative overhead.

<a name="data-driven-mastery-predictions"></a>
## 🧠 Data-Driven Mastery Predictions

The Synalux platform leverages a deterministic, data-driven projection model to predict timelines for target mastery based on current trends in patient progress. Instead of a generic LLM, it uses a clinical velocity multiplier to provide transparent, mathematically sound estimates:

1. **Data Extraction:** The engine extracts the raw numerical values from the patient's current progress and the final mastery criteria (e.g., current = 50%, target = 80%).
2. **Velocity Calculation:** The timeline is calculated by determining the remaining progress (`target - current`) and dividing it by an estimated growth velocity per session. The algorithm uses a linear projection based on **15% of the current score** acting as the expected growth per session.
3. **Timeline Generation:** The exact formula used is `sessionsEstimate = Math.ceil(remaining / Math.max(1, current * 0.15))`.
4. **Clinical Display:** If the patient still has remaining progress, the UI displays a badge like **"~4 sessions"**. If the calculation determines the remaining amount is negligible, it flags the skill as **"Near mastery"**.

This predictive analytics feature empowers therapists to set realistic goals and adjust treatment plans proactively.

<a name="smart-treatment-recommendations"></a>
## 💡 Smart Treatment Recommendations

Building on the mastery predictions, Synalux’s AI provides automatic recommendations for the next targets based on skills that have already been mastered by the patient. By analyzing the `status === 'mastered'` targets within the current Program Tree, the platform queries its built-in curriculum database to suggest the next logical progression of learning objectives (e.g., progressing from "Echoics" to "Manding"). This ensures a structured clinical continuum, enhancing the effectiveness of the therapy plan.

<a name="automated-progress-reports"></a>
## 📄 Automated Progress Reports

Generating progress reports is streamlined with one-click functionality in Synalux. The platform aggregates the mastery predictions, goal suggestions, and session data across the reporting period. These reports are tailored to meet insurance requirements (such as summarizing phase-change lines and frequency trends) and provide clear, concise summaries of patient progress, ensuring compliance and rapid authorization renewals with third-party payers.

<a name="treatment-integrity"></a>
## 🔍 Treatment Integrity

Synalux includes real-time monitoring for Discrete Trial Training (DTT) and Natural Environment Teaching (NET) fidelity, complete with adherence scoring. This feature ensures that treatment is delivered consistently according to established protocols, maintaining the integrity of the ABA therapy.

<a name="program-tree-view"></a>
## 🌳 Program Tree View

The hierarchical Program → Goal → Target tree view provides a clear visual representation of the therapy structure, including progress bars for each target. This intuitive interface helps therapists and administrators to easily track patient progress and make informed decisions about treatment adjustments.