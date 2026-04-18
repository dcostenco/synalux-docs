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

## Admin Audit
Each event in a clinical session is marked with an indicator showing whether it occurred online (🟢) or offline (🔴). Additionally, timestamps for both client-side events and server syncs are logged, providing administrators with detailed audit trails for review.

## Connection Monitor
A real-time connection status monitor is displayed in the sidebar. It shows a 🟢/🔴 status indicating whether the device is currently connected to the server and includes a badge that displays the count of pending sync items.

## HIPAA Cleanup
Upon logout or after an idle timeout, all local data stored in localStorage is securely purged. This ensures compliance with HIPAA regulations by preventing unauthorized access to sensitive patient information when devices are left unattended or when users log out.

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