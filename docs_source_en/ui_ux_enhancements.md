# UI/UX Enhancements: Synalux Omni-Search

Synalux is built to significantly reduce "click fatigue" typical in other EHRs (e.g. SimplePractice, CentralReach) by offering deep navigation shortcuts and a global command palette.

## Omni-Search (CMD+K) Command Palette

The global **Command Palette** drastically streamlines user navigation inside the practice portal.
Instead of navigating deep into the sidebar for routine operations:

1. Press `Cmd + K` on Mac or `Ctrl + K` on Windows.
2. The global search overlay intercepts the screen.
3. Type the command or area (e.g. `Billing`, `Patients`).
4. Instant routing without extra mouse clicks.

<details>
<summary>Technical Implementation</summary>

Mounted natively in `RootLayout`, intercepting keydown event listeners globally. 

```tsx
import CommandPalette from '@/components/ui/CommandPalette';
// Embedded in RootLayout Providers
<CommandPalette />
```

Test covered automatically via Playwright mapping (`tests/ui/deep-ui.spec.ts`). Testing ensures the `Escape` key effectively triggers the overlay dropdown dismount to preserve accessibility standards.
</details>

## Smart "First Available" Booking Widget

Designed to eliminate friction for patients trying to book quick appointments. It masks complex scheduling matrices under an intuitive "First Available" list. Located natively in the scheduling flow (`components/ui/SmartBookingWidget.tsx`).

## Floating AI Assistant

Provides clinicians with an omni-present contextual side-panel (`components/ui/FloatingAIAssistant.tsx`). Instead of clicking back and forth between tabs to draft notes, the Assistant is pre-loaded with the active patient's context to draft SOAP notes and summarize histories dynamically.
