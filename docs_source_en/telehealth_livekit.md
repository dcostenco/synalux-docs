# 🎥 Telehealth (LiveKit)

**1080p video on weak Wi-Fi. No patient downloads.** Picture-in-picture so the clinician can chart while talking. Built on LiveKit's selective-forwarding-unit (SFU) infrastructure — Synalux runs the rooms, you run the care.

---

## 🔌 Bandwidth-Adaptive Video (LiveKit SFU)
Synalux uses LiveKit's open-source SFU rather than an MCU mesh, so:
*   **Per-participant bitrate adaptation** — each viewer receives a stream sized to their downlink. Patient on hotel Wi-Fi sees 480p; clinician on fiber sees 1080p simulcast.
*   **No transcoding load** on the server — CPU stays low even with 8-person multi-clinician case conferences.
*   **TURN fallback** — if direct P2P fails (NAT / corporate firewall), the SFU relays via TURN.
*   **Track-level pause** — bandwidth saver pauses outbound video when minimized to PiP.

---

## 🩺 Clinician-First UX
*   **No patient downloads** — runs in-browser via WebRTC. Patient gets a one-tap join link via the [Mail](mail.md) or [SMS](sms.md) module.
*   **Picture-in-Picture (PiP)** — minimize video, keep charting. Drag PiP anywhere on screen.
*   **In-call clinical notes** — live SOAP draft via [Voice Dictation](mobile_ai.md) running alongside the video stream.
*   **Patient chat sidebar** — text chat in-call for quiet check-ins (lab values, dosing) without interrupting speech.

---

## 🎬 Recording (consented, encrypted)
*   **Per-call consent gate** — visible on-screen confirmation before recording starts.
*   **Storage** — recordings written to the [Drive module](drive.md) with the same RLS isolation as other clinical files.
*   **Retention** — workspace-configurable; default 30 days.

---

## 🔄 Conferencing Routing (in-event creator)
The [Calendar module](calendar.md) creator picks the right conferencing provider based on tier + workspace defaults:

| Conferencing | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| Synalux LiveKit Telehealth | — | ✅ | ✅ | ✅ |
| Google Meet | ✅ | ✅ | ✅ | ✅ |
| Microsoft Teams | — | ✅ | ✅ | ✅ |
| Zoom | — | — | ✅ | ✅ |

---

## 🏗️ Architecture

```
POST /api/v1/livekit/token       Mint a per-participant LiveKit JWT (workspace + role-scoped)
POST /api/v1/meetings            Create a telehealth meeting (resolves room URL + token)
GET  /api/v1/meetings/:id        Read meeting status + participant list
PATCH /api/v1/meetings/:id       Update (extend duration, add participant)
DELETE /api/v1/meetings/:id      End meeting + flush recording to Drive
POST /api/v1/calls/:id/join      Mark participant joined (audit + presence)
GET  /api/v1/video/:id/recording Recording metadata + signed playback URL
```

| Layer | Tech |
|---|---|
| Media SFU | LiveKit (self-hosted on dedicated infrastructure for HIPAA isolation) |
| Signaling | LiveKit's protobuf signaling over WSS |
| Token mint | Synalux portal — per-participant JWT with role + workspace claims |
| Recording | LiveKit egress → S3-compatible storage → Drive metadata |
| Audio enhancement | Krisp noise suppression on patient + clinician streams |

---

## ⚖️ HIPAA + Audit
*   **Per-room access logging** — every join writes to `livekit_access_log` with participant + role + timestamp + IP.
*   **TURN traffic encrypted** — DTLS-SRTP end to end; no clear-text media on the wire.
*   **Recording consent enforced** in code — backend rejects egress requests without a stored consent receipt.
*   **No third-party analytics in the call** — LiveKit pages are CSP-locked.

---

## 💳 Plans

| | Free | Standard | Advanced | Enterprise |
|---|---|---|---|---|
| Synalux Telehealth (LiveKit) | — | ✅ 1:1 calls | ✅ Group calls (8) | ✅ Group + recording |
| Google Meet integration | ✅ | ✅ | ✅ | ✅ |
| Microsoft Teams integration | — | ✅ | ✅ | ✅ |
| Zoom integration | — | — | ✅ | ✅ |
| Call recording → Drive | — | — | ✅ | ✅ |
| In-call live SOAP dictation | — | — | ✅ | ✅ |
| Multi-workspace HQ telehealth queue | — | — | — | ✅ |

[See full pricing →](https://synalux.ai/pricing)

---

## 🔄 Inter-Module Integration
*   **Calendar** — meetings auto-attached when an event is created with conferencing.
*   **Patients** — every meeting is filed against the patient chart with consent receipt.
*   **SOAP / Clinical Notes** — in-call dictation produces a draft note attached to the meeting record.
*   **Drive** — recordings land in patient-scoped folders.
*   **Mail / SMS** — join links sent via the connected channel.
