# Offline-First Clinical Sessions

The Offline-First Clinical Sessions module is designed to ensure continuity and accuracy in clinical workflows, even when internet connectivity is inconsistent. This module captures essential data locally on the provider's device and syncs it with the server once a connection is re-established. Below are detailed descriptions of each feature:

## Client-Side Timestamps
Session start and end times are captured on the provider's device using client-side timestamps. These timestamps are critical for billing purposes, as they reflect the actual start and end times of the clinical session rather than the time at which data was received by the server.

## Offline Queue
When a connection to the server is lost, events are automatically queued in the browser's localStorage. As soon as connectivity is restored, these queued events are synced with the server, ensuring that no data is lost during offline periods.

## Draft Persistence
Clinical notes are automatically saved to localStorage every time a keystroke is made. This feature ensures that all work is preserved even if the provider experiences a browser crash or connection loss, maintaining the integrity of the clinical documentation process.

## Session Sign-Off
Providers are required to sign off at the end of each session. The timestamp recorded during this sign-off action serves as the accurate billing endpoint for the session, ensuring compliance with billing standards.

### Decoupling Calendar from Session State (Clinical Overtime)
To handle real-world clinical unpredictability (e.g., crisis intervention causing a 45-minute session to run 90 minutes), the system treats the calendar strictly as a guideline, not a kill-switch. There is **no forced sync or sign-off tied to the scheduled end time**. The clinical session state (`in_progress`) remains active indefinitely until the provider explicitly clicks "End Session" or the absolute inactivity timeout triggers. The billing module later compares the scheduled time vs. the actual time and automatically suggests appropriate extended CPT modifiers (e.g., prolonged service codes) during Superbill generation.

## Admin Audit
Each event in a clinical session is marked with an indicator showing whether it occurred online (🟢) or offline (🔴). Additionally, timestamps for both client-side events and server syncs are logged, providing administrators with detailed audit trails for review.

## Connection Monitor
A real-time connection status monitor is displayed in the sidebar. It shows a 🟢/🔴 status indicating whether the device is currently connected to the server and includes a badge that displays the count of pending sync items.

## HIPAA Cleanup & Emergency Session Auto-Quarantine (ESAQ)
To resolve the conflict between HIPAA's strict "no plaintext PHI on unattended device" rule (§164.312(a)(2)(iv)) and the need to prevent data loss during an emergency (e.g., laptop battery dies, browser idles out), Synalux employs an **Asymmetric Emergency Vault** mechanism.

Upon logout or after a 15-minute idle timeout, all local data is securely processed before purging:

1. **Online Timeout (Quarantine State):** If the device is online when the timeout fires, it executes a beacon payload to a secure endpoint containing the unsynced drafts, tagged with the `last_active_timestamp`. The server saves this session with a `QUARANTINED` status. The Admin can then log in, review the Draft, confirm the actual end-time with the provider based on the last known activity, and manually sign off to release it for billing.
2. **Offline Timeout (Asymmetric Emergency Vault):** If the device is offline, the app uses the native WebCrypto API to encrypt the existing offline queue entirely using a Server Public Key loaded during initial login (RSA-OAEP). The encrypted blob is stored as an `emergency_vault` in localStorage, and all readable PHI texts are immediately purged. This cryptographically seals the data from any malicious local actor.
3. **Recovery Sync:** When the provider regains connectivity and logs back in, the app syncs the encrypted blob to the server, where it is decrypted using the Server Private Key and transitioned into the `QUARANTINED` state for Admin review.

### Audio-Aware Idling (False Inactivity Safeguard)
In therapy or psychiatric evaluations, a provider might actively converse with a patient for 30 minutes without touching the keyboard. To prevent false idle timeouts, Synalux features Audio-Aware Idling. If the microphone is active and capturing audio (e.g., via WASM Whisper dictation), continuous audio input counts as continuous user activity, preventing the 15-minute timeout entirely. If the mic is off, an audible chime and modal appear at the 14-minute mark to warn the provider.

## Idempotent Sync
To prevent duplicate entries during the sync process, each event is assigned a unique client-generated UUID (Universally Unique Identifier). This mechanism ensures that only new or modified data is synced with the server, maintaining data integrity and preventing redundancy.

## Time Drift Detection
The system logs any discrepancies between client-side timestamps and server timestamps. These logs are used for audit purposes to detect and address any time drift issues that may affect the accuracy of clinical session records.

## Session Lifecycle
The lifecycle of a clinical session is represented by a series of states: `session_start`, `session_pause`, `session_resume`, and `session_end`. This structured approach helps in accurately tracking the progression of sessions, from initiation to completion.

**Billing Compliance Example:**
```
Provider starts session at 2:00 PM (online) → 🟢
Connection drops at 2:30 PM
Provider ends session at 3:45 PM (offline) → 🔴 client_timestamp = 3:45 PM
Connection restores at 4:00 PM → auto-sync
Server records: client_timestamp = 3:45 PM, sync_timestamp = 4:00 PM
↓
Insurance billed: session 2:00 PM – 3:45 PM (accurate)
Admin sees: "Session ended 3:45 PM 🔴 Offline (synced 4:00 PM)"