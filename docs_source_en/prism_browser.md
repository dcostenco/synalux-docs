# Prism Browser — Privacy-First Clinical Browser with AAC Accessibility

Prism Browser is an Electron-based web browser built as a **HIPAA-compliant clinical appliance** with full **AAC (Augmentative and Alternative Communication)** support. It enables users who control their computer via head tracking, switch scanning, or voice commands to browse the web independently.

> **9/10 security audit score** across 10 adversarial review rounds. All phases complete.

---

## Key Features

| Category | Features |
|----------|----------|
| **AAC Input** | Head tracking (MediaPipe), switch scanning, voice commands, gesture detection (8 types), dwell click |
| **Browsing** | Tabs, bookmarks, history, downloads, context menu, find-in-page, reader mode |
| **Clinical** | PHI sanitization (NER + regex), HIPAA session timeout, audit logging, clinical context sidebar |
| **Portal** | Synalux Mail, Calendar, Drive, Chat — dedicated sidebar with keyboard shortcuts |
| **Security** | Sandbox + CSP, default-deny permissions, encrypted storage, HMAC audit chain |

---

## AAC Accessibility

### Head Tracking

Control the cursor with head movement using your computer's camera:

- **MediaPipe FaceDetector** — GPU-accelerated face detection at 24fps
- **Kalman smoothing** — confidence-weighted cursor stabilization
- **Dwell click** — hold cursor on a target for configurable duration to click
- **Drift detection** — automatically pauses tracking if calibration degrades
- **Background recalibration** — learns and corrects drift over time
- **Edge scroll** — move cursor to screen edge to auto-scroll pages
- **Self-hosted models** — MediaPipe WASM + model bundled in app (no CDN, no IP leakage)

### Gesture Detection

8 gestures recognized from facial expressions and head movement:

| Gesture | Action | Detection |
|---------|--------|-----------|
| Blink (both eyes) | Click at cursor | Eye closure threshold |
| Wink left | Navigate back | Asymmetric eye closure |
| Wink right | Navigate forward | Asymmetric eye closure |
| Nod | Scroll down | Pitch oscillation history |
| Head shake | Cancel/escape | Yaw oscillation history |
| Smile | Toggle reader mode | Mouth corner threshold |
| Brow raise | Scroll up | Brow movement threshold |
| Mouth open | Stop TTS | Jaw open threshold |

- **Conversation mode (A-08)** — mouth gestures automatically suppressed while TTS is speaking
- **Configurable thresholds** — adjust sensitivity per gesture
- **500ms cooldown** — prevents accidental repeated triggers

### Switch Scanning

Navigate web pages using external switches, a keyboard, or a gamepad:

- **Two-phase scanning** — first scan groups (ARIA landmarks + spatial rows), then individual items
- **Input sources** — Space/Enter (keyboard), gamepad button, WebHID switch
- **ARIA landmark grouping** — discovers `<nav>`, `<main>`, `<aside>` as scan groups
- **Spatial clustering** — elements not in landmarks are grouped by vertical position (row-based)
- **Configurable** — scan speed (500-5000ms), loop count, group scan toggle

### Voice Commands

22 offline commands recognized via Web Speech API:

- **Navigation** — "go back", "go forward", "reload", "new tab", "close tab"
- **Scrolling** — "scroll down", "scroll up", "go to top", "go to bottom"
- **Actions** — "click", "find", "read page", "stop reading"
- **Tab management** — "next tab", "previous tab"
- **Settings** — "settings", "bookmarks", "zoom in", "zoom out"

### Bootstrap Wizard

First-run setup that works for **every input method**:

- **Head tracking** — coarse tracker starts on wizard mount; move head to dwell on tiles
- **Switch scanning** — Tab + Enter to select
- **Voice** — speak the option name
- **Mouse/touch** — click directly
- **2-second dwell targets** — 120x120px tiles for imprecise cursor control

### ZoomToClick

Precision selection for dense web content:

- When 3+ interactive elements cluster within 100px of cursor, a **3x magnified lens** appears
- **300ms settle period** — cursor must stabilize before dwell starts (magnification amplifies tremor)
- Select the intended element within the lens via dwell click

### Break Reminder

Configurable rest timer for head tracking users:

- Default: 20-minute intervals
- Full-screen pause prompt with oversized "Resume" button (dwell-compatible)
- Tracking paused during break (not the page)

---

## Content Bridge Architecture

The browser's chrome UI and browsed web pages run in **separate processes** (WebContentsView). AAC features interact with web content via a secure Content Bridge:

```
Chrome Renderer (AAC)          Browsed Tab (sandboxed)
┌──────────────────┐          ┌──────────────────┐
│ Head Tracker      │  ──────► │ Content Bridge    │
│ Dwell Click       │ IPC      │  - hitTest(x,y)   │
│ Switch Scanner    │ ◄────── │  - dispatchClick  │
│ Gesture Detector  │          │  - scanGroups     │
│ Voice Commands    │          │  - scrollBy       │
└──────────────────┘          └──────────────────┘
```

- **Isolated-world preload** — content script invisible to page JavaScript
- **Same-origin iframes** — bridge traverses into iframes and open shadow DOM
- **Sender validation** — AAC responses verified against active tab/portal webContents

---

## Privacy & Security

### Permissions

**Default-deny** on all sessions (browsing, portal, chrome):
- Camera: granted only for synalux.ai origin (head tracking)
- All other permissions (geolocation, USB, HID, serial): denied by default

### Content Security Policy

Production CSP: `script-src 'self'`, `object-src 'none'`, `base-uri 'self'` — no `unsafe-eval` or `unsafe-inline` in scripts.

### PHI Sanitization

Two-layer PHI scrubbing on all search queries before they leave the browser:

**Layer 1 (Regex):** SSN, phone, email, DOB, address, ZIP, MRN, NPI, TitleCase names

**Layer 2 (NER):** ICD-10 codes, NDC drug codes, medication names (30 common prefixes), age patterns — all gated on medical-context detection to prevent false positives

### Session Lock (HIPAA Automatic Logoff)

- **15-minute inactivity timeout** — triggers automatic lock
- **View detachment** — all tab and portal WebContentsViews hidden + throttled (no JS/websocket/media during lock)
- **PIN-based unlock** — forced PIN setup on first use, 5-attempt brute-force lockout with 30s cooldown
- **Encrypted PIN storage** — via Electron safeStorage (OS keychain)
- **powerMonitor integration** — locks on system suspend/lock-screen

### Audit Logging

Append-only JSONL log with **HMAC chain** (per-install key in OS keychain):

- **40+ event types**: session start/lock/unlock, navigation, search, PHI redaction, bookmark/clip CRUD, portal open/close, reader mode, downloads, permissions, clinical context, therapy timer, sync, AI summary
- **Who/what/when/where** per 164.312(b)
- **Tamper-evident** — each entry chains to the previous via HMAC-SHA256; `audit:verify` IPC validates the chain
- **Cross-day chaining** — head hash persisted in safeStorage

### Encrypted Storage

All persistent data (bookmarks, history, settings, annotations, caregiver config) encrypted via Electron `safeStorage`:
- **Fail-closed** — refuses to persist when encryption unavailable (no plaintext fallback)

---

## Portal Integration

Synalux portal services as first-class sidebar modules:

| Module | Shortcut | Description |
|--------|----------|-------------|
| Dashboard | Cmd+Shift+H | Practice overview |
| Mail | Cmd+Shift+M | Clinical email |
| Calendar | Cmd+Shift+C | Scheduling |
| Drive | Cmd+Shift+D | Document storage |
| Chat | Cmd+Shift+A | Team messaging |

- **Portal session partition** — isolated cookies/storage from browsing
- **AAC-navigable** — head tracking and switch scanning work on portal modules
- **Navigation lock** — portal views restricted to synalux.ai origin

---

## Clinical Features

### Reader Mode

Extract clean article text from any web page:
- **Readability.js** extraction with **DOMPurify** sanitization
- **Adjustable font size** (12-28pt)
- **TTS read-aloud** via Web Speech API
- **Portal-origin blocked** — prevents PHI extraction from clinical pages
- **Cmd+Shift+R** toggle

### AI Page Summary

"Summarize this" sends **PHI-sanitized** page text to portal AI:
- Text sanitized through PHI scrubber before egress
- **Fail-closed** — aborts if sanitizer errors (no unsanitized egress)
- 3-5 bullet point summary
- Cmd+Shift+P

### Clinical Context Sidebar

View active patient data alongside web browsing:
- Patient name, ID, DOB, diagnoses, medications, notes
- Fetched from portal API with authentication
- Audit logged on open/close
- Cmd+Shift+X

### Therapy Timer

Session timer for clinical appointments:
- Start/stop/resume/reset with notes field
- Auto-logs duration to audit trail
- Cmd+Shift+T

### PHI-Safe Printing

Print pages with PHI redacted:
- Sanitizes **rendered text** (innerText, not HTML source) — catches PHI fragmented across tags
- Prints plain text paragraphs (no scripts/active content)
- HTML-escaped before interpolation
- Audit logged with redaction count
- Cmd+P

---

## Additional Features

### Phishing Protection
Safe Browsing proxied through Synalux portal — blocks known phishing sites with a warning page.

### Private Browsing
Non-persistent session partition with no cache and default-deny permissions.

### Translation Mode
Portal-routed translation with LRU cache (500 entries), 25 built-in languages.

### 3-Tier TTS
Azure Neural TTS → Web Speech API → espeak-ng WASM fallback.

### Web Clipper
Highlight text → save with notes, color, and URL. Encrypted storage, 1000 entry cap.

### Cross-Device Sync
Server-encrypted bookmark/settings sync via portal API. Per-device ID, merge with dedup.

### Per-Side Fatigue Tracking
Left/right independent accuracy tracking for users with cerebral palsy or stroke — alerts when one side's performance degrades.

### Caregiver Mode
Content filters (domain blocklist), time limits (persisted daily usage), allowed hours, PIN-protected settings.

### DNS-over-HTTPS
Prevents DNS query snooping on clinical searches via Cloudflare + Google DoH servers.

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Cmd+T | New tab |
| Cmd+W | Close tab |
| Cmd+1-9 | Switch to tab N |
| Cmd+Shift+]/[ | Next/previous tab |
| Cmd+L | Focus address bar |
| Cmd+F | Find in page |
| Cmd+, | Settings |
| Cmd+Shift+R | Reader mode |
| Cmd+Shift+S | Switch scanning |
| Cmd+Shift+P | Summarize page |
| Cmd+Shift+X | Clinical context |
| Cmd+Shift+T | Therapy timer |
| Cmd+Shift+K | AAC keyboard |
| Cmd+/ | AI chat |
| Cmd+P | PHI-safe print |

---

## Technical Architecture

- **Electron 42.4** with WebContentsView per tab (not deprecated BrowserView)
- **React 19** chrome UI with Zustand state management
- **Two session partitions** — `persist:browsing` (shielded) + `persist:portal` (authenticated)
- **Sandbox: true** on chrome window + all tab/portal views
- **Register/attach/detach lifecycle** — no listener leaks on macOS close→reopen
- **141 unit tests** across 11 test suites

---

## System Requirements

- **macOS** 12+ (Apple Silicon + Intel universal)
- **Windows** 10+ (x64)
- **Linux** (AppImage, x64)
- Camera required for head tracking
- Internet required for portal features, AI summary, and sync

---

*For questions or feature requests, contact [support@synalux.ai](mailto:support@synalux.ai) or visit [synalux.ai/docs](https://synalux.ai/docs).*
