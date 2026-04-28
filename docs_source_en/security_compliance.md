# 🛡️ Security, Privacy & HIPAA Compliance

Synalux v11.1 Elite is built on a "Security-First" architecture. We don't just check boxes; we harden every layer of the clinical workflow to ensure that patient data is the most protected asset in your practice.

---

## 🔒 HIPAA Technical Safeguards
Exceed the federal standards for data protection.
*   **Encryption at Rest:** All clinical data and media are secured with AES-256-GCM encryption.
*   **Encryption in Transit:** Every connection is protected by TLS 1.3 with high-strength cipher suites.
*   **Zero-Knowledge Options:** For psychiatry and sensitive therapy, notes are encrypted with keys that only the provider can access.

<details>
<summary>View Interface / Diagram</summary>

![Security Architecture & Audit](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/38_compliance_audit.png)

</details>

---

## 🕵️ Immutable Clinical Audit Trails
Absolute accountability for every action taken on the platform.
*   **7-Year Retention:** We maintain a permanent, unalterable log of every PHI access, edit, and deletion.
*   **Contextual Logging:** Know exactly who looked at a chart, from which IP address, and for how long.
*   **Administrative Oversight:** HQ admins can review organization-wide security posture in real-time.

<details>
<summary>View Interface / Diagram</summary>

![Security Audit Logs UI](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/generated/security_audit_logs_ui.png)

</details>

---

## 🛡️ Role-Based Access Control (RBAC)
Enforce the "Principle of Least Privilege" with granular precision.
*   **Clinical vs. Admin:** Ensure front-desk staff can see schedules but never clinical SOAP notes.
*   **Employee Overrides:** Overrule base roles to restrict specific high-risk features (e.g., "Export to Excel").
*   **Branch Isolation:** Providers in one branch cannot access records in another unless explicitly authorized.

<details>
<summary>View Interface / Diagram</summary>

![RBAC Role Management](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/11_rbt_role_view.png)

</details>

---

## 📴 Offline-First Privacy (ESAQ)
Security that follows you into the field.
*   **Emergency Vaulting:** If a device is lost or stolen while offline, the data is cryptographically sealed and plaintext PHI is purged.
*   **No Cloud AI Leaks:** Our WASM-powered voice dictation processes all audio locally. Your clinical conversations are never sent to external AI servers.

---

## 🤝 Business Associate Agreement (BAA)
We stand behind our security.
*   **Enterprise Coverage:** We provide signed BAAs for all Enterprise tier customers.
*   **Subprocessor Transparency:** Full disclosure of our secure cloud infrastructure partners (Supabase/AWS/Vercel).
*   **Compliance Support:** Our team assists you during insurance audits or HIPAA inspections.

---

## ⚡ Break-Glass Emergency Protocol
*   **One-Click Access:** Authorized staff can override restrictions in true clinical emergencies.
*   **Immediate Notification:** Security officers are alerted the moment a "Break-Glass" event occurs.
*   **Mandatory Justification:** The system requires a clinical rationale to be entered before access is granted.

---

## 🔐 Platform Hardening
*   **Automatic Timeouts:** Sessions expire after 15 minutes of inactivity (protected by Audio-Aware idling).
*   **SHA-256 Hashing:** Passwords and access codes are never stored in plaintext.
*   **Regular Pentesting:** We conduct frequent security audits to identify and patch vulnerabilities proactively.
