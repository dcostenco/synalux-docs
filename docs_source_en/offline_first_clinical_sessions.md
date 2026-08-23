# 📴 Offline Clinical Workflows

Supported Synalux clinical workflows can queue selected activity on the active device when the browser reports that it is offline, then attempt synchronization after the connection returns. Offline behavior is workflow- and configuration-specific: test the exact devices and tasks your organization plans to use before relying on them.

## Connection and queue status

The application’s connection indicator distinguishes online, offline, and queued states where offline support is active. Do not sign out, clear browser data, remove the device profile, or assume another device has the queued work until synchronization is confirmed.

## Session event timing

Supported session events retain client event time and connection status so authorized staff can distinguish when activity occurred from when an offline event synchronized. Review those records before using them for billing or payroll.

<details>
<summary>View the current clinical note workspace</summary>

![Current Synalux clinical note workspace](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/04_soap_note.png)

</details>

---

## Dictation while connectivity is limited

The current SOAP workspace uses its local WASM Whisper worker for speech recognition, so audio for that dictation path is processed in the active browser. Confirm recording consent and review the resulting text. Browser, microphone, worker, and model availability still affect whether dictation can start, and a first load may need assets that are not already available on the device. Use typed entry if dictation is unavailable. A working dictation control also does not prove that the related note save or attachment can complete while offline.

<details>
<summary>View the SOAP dictation workspace</summary>

![Ambient Voice Dictation Interface](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/03_voice_dictation.png)

</details>

---

## Reconnect checklist

1. Keep the application open and restore the expected network connection.
2. Wait for the connection indicator to return online and the queued count to clear.
3. Open the intended patient and confirm that the record reflects the queued work.
4. If synchronization reports an error or the record is incomplete, stop duplicate entry and contact your administrator.

## Audit review

Authorized administrators can review the recorded events available in the audit log. Offline support does not remove the organization’s responsibility to protect the device, control access, verify synchronization, and maintain downtime procedures.

<details>
<summary>View the audit log</summary>

![Current Synalux audit log](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/38_compliance_audit.png)

</details>
