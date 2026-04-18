# Mobile AI Assistant & UI Optimization

The Synalux portal features a global AI Assistant and mobile-first input optimizations designed for speed and offline-resilience during clinical encounters.

## Global AI Chat Assistant
The AI Chat is anchored via a Floating Action Button (FAB) across the entire platform. 
1. **Model Routing**: By default, Paid Tiers (Advanced & Enterprise) are routed to `gemini-3.1-pro-preview` for deep clinical reasoning. Free user tier requests fall back to `gemini-2.5-flash`.
2. **Conversation History**: Chat sessions retain history directly in the DOM state using caching, ensuring that context is not lost if the user minimizes the chat modal to retrieve patient data on the page.
3. **Safe Area Insets**: The UI automatically accounts for the `env(safe-area-inset-bottom)` on iOS and Android devices, guaranteeing that the inputs never overlap with the OS home indicator.

## Native Predictive Text
All Synalux inputs are augmented with native OS-level predictive text algorithms instead of custom JS DOM-injections.
- Uses `spellCheck={true}` and `autoCorrect="on"`.
- This ensures maximum privacy (HIPAA compliance), as keystroke heuristics remain strictly on the user's hardware device rather than being piped to a 3rd party AI ghost-text server.
