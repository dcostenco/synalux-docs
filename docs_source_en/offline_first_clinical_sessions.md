# 📴 Offline-First Clinical Workflow

Synalux v11.1 Elite is built for the real world. Whether you're in a rural clinic with spotty Wi-Fi or a hospital basement with zero signal, our offline-first engine ensures your data is saved instantly and synced securely the moment you're back online.

---

## ⚡ Zero-Data-Loss Drafting
Type with confidence knowing every keystroke is protected.
*   **Local Persistence:** Clinical notes are saved to your device's secure local storage as you type.
*   **Crash Recovery:** If your browser or tablet crashes, your draft is waiting for you exactly where you left off.
*   **Real-Time Status:** A subtle indicator in the sidebar shows your current sync status and the number of pending items.

![Offline Sync Status Interface](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/generated/offline_sync_ui.png)

---

## 🕒 Precision Billing (Client-Side Timestamps)
Capture accurate session durations for 100% billing compliance.
*   **Real Start/End Times:** We record timestamps from your device, not when the server receives the data.
*   **Clinical Overtime:** The calendar is a guide, not a switch. Sessions stay active until you explicitly sign off.
*   **Sync Transparency:** Admins see both the clinical event time and the server sync time in the audit log.

![Clinical Session Lifecycle Tracking](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/04_soap_note.png)

---

## 🛡️ Emergency Session Auto-Quarantine (ESAQ)
Maintain HIPAA compliance even during an unexpected timeout or battery failure.
*   **Asymmetric Vaulting:** If your device idles out while offline, your drafts are instantly encrypted using a server-only public key.
*   **Zero-Plaintext:** Sensitive PHI is purged from your browser's readable memory, leaving only an encrypted "emergency vault" blob.
*   **Recovery Sync:** Log back in on any device to securely restore and complete your quarantined sessions.

---

## 🎙️ Audio-Aware Idling
Stay logged in during long patient conversations without touching your device.
*   **Mic Detection:** If WASM Whisper is active and listening, the system prevents idle timeouts entirely.
*   **Hands-Free Liberty:** Focus 100% on the patient—your session won't time out as long as the conversation continues.

![Ambient Voice Dictation Interface](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/03_voice_dictation.png)

---

## 🔄 Idempotent Background Sync
*   **Smart Reconciliation:** Our sync engine prevents duplicate records even if you switch devices mid-session.
*   **Conflict Resolution:** If a note is edited on two devices, Synalux helps you choose the correct version.
*   **Time Drift Logic:** Automated detection and correction of device clock inaccuracies for audit integrity.

---

## 🔐 Security & Audit
*   **RSA-2048 Encryption:** Offline data is secured with industry-standard asymmetric encryption.
*   **Immutable Logs:** Every 🟢 Online and 🔴 Offline event is tracked with its original device ID.
*   **Role-Based Gating:** Access to offline drafts is restricted to the original author and authorized clinical directors.

![Security & Compliance Audit](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/generated/security_audit_logs_ui.png)