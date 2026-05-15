# Mobile AI Assistant & UI Optimization

The Synalux portal features a global AI Assistant and mobile-first input optimizations designed for speed and offline-resilience during clinical encounters.

## Global AI Chat Assistant
The AI Chat is anchored via a Floating Action Button (FAB) across the entire platform.
1. **Model Routing**: Cloud tiers route through OpenRouter:
   - **Free** — Claude Haiku 3.5 (fast, cost-effective)
   - **Standard / Advanced** — Claude Sonnet 4 (primary), Claude Haiku 3.5 (fallback)
   - **Enterprise** — Claude Sonnet 4 (primary), Claude Opus 4 selectable
   - **Gemini models** (Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3 Flash/Pro Preview) available via direct Google API on Advanced+ tiers
   - **Local** — `prism-coder:14b` via Ollama (free, offline, all tiers)
2. **Conversation History**: Chat sessions retain history directly in the DOM state using caching, ensuring that context is not lost if the user minimizes the chat modal to retrieve patient data on the page.
3. **Safe Area Insets**: The UI automatically accounts for the `env(safe-area-inset-bottom)` on iOS and Android devices, guaranteeing that the inputs never overlap with the OS home indicator.

## Native Predictive Text
All Synalux inputs are augmented with native OS-level predictive text algorithms instead of custom JS DOM-injections.
- Uses `spellCheck={true}` and `autoCorrect="on"`.
- This ensures maximum privacy (HIPAA compliance), as keystroke heuristics remain strictly on the user's hardware device rather than being piped to a 3rd party AI ghost-text server.
