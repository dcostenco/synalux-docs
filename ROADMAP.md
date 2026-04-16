# 🗺️ Synalux Roadmap

> Last updated: April 16, 2026

## ✅ Completed (v3.0 — Current Release)

### Platform Core
- [x] Next.js 15 web portal with SSE streaming chat
- [x] Dual-backend AI: Cloud (OpenRouter/Gemini) + Local (Ollama)
- [x] 11 RBAC roles with cryptographic tool ACLs
- [x] 12-language internationalization (i18n)
- [x] Admin dashboard with KPI analytics
- [x] Patient portal (auth, messaging, billing, appointments)

### Clinical Modules
- [x] SOAP note generation (4 templates + voice dictation)
- [x] Patient management (27 patients, vitals, allergies, medications)
- [x] Appointment scheduling with multi-provider support
- [x] Lab orders & results with abnormal flagging
- [x] Immunization tracking (CDC schedule)
- [x] Clinical tasks with priority management
- [x] Referral system with cross-practice chat
- [x] Patient recalls & reminders
- [x] Document management with server-side PDF
- [x] Insurance tracking (15+ payers)
- [x] E-signatures via BoldSign
- [x] Superbill / CPT/CDT coding

### Business Modules
- [x] Stripe billing with subscription tiers (Free/Standard/Pro/Enterprise)
- [x] Fee schedules per practice
- [x] HR / staff management (credentials, PTO, reviews)
- [x] Inventory management
- [x] Quality measures (HEDIS/MIPS)
- [x] Patient education materials
- [x] Team chat (E2E encrypted)

### Security & Compliance
- [x] HIPAA-ready architecture (audit trails, data minimization)
- [x] EdDSA (Ed25519) JWT authentication
- [x] Row-Level Security (RLS) on all tables
- [x] Output guardrail system (prompt injection defense)
- [x] HITL safety gate for dangerous tools
- [x] Fail-closed HIPAA mode (local LLM)

### VS Code Extension (v0.12.4)
- [x] 20+ multimodal tools (voice, OCR, terminal, Git, browser)
- [x] Multi-agent orchestrator (planner → coder → tester)
- [x] Prism MCP persistent memory integration
- [x] Local workspace tools (file ops, search, commands)

---

## 🔄 In Progress (v3.1 — Target: Q2 2026)

### Platform Improvements
- [ ] Connection pooling via PgBouncer for scale
- [ ] Video CDN migration (Cloudflare R2) to reduce Vercel bandwidth
- [ ] Progressive Web App (PWA) with offline support
- [ ] Push notifications for appointment reminders

### Clinical Enhancements
- [ ] Electronic claim submission (837P) via clearinghouse integration
- [ ] Real-time insurance eligibility verification
- [ ] ERA/EOB electronic remittance auto-posting
- [ ] HL7 FHIR R4 interoperability layer

### AI Features
- [ ] Multi-turn tool execution (tool chains with 3+ steps)
- [ ] Ambient clinical documentation (continuous session recording)
- [ ] AI-powered coding suggestions (ICD-10 auto-coding from notes)
- [ ] Treatment plan optimization recommendations

---

## 📋 Planned (v4.0 — Target: Q3–Q4 2026)

### Enterprise Features
- [ ] SSO / SAML authentication
- [ ] HIPAA BAA execution (Vercel Enterprise + Supabase Team)
- [ ] Multi-organization management console
- [ ] Custom AI model fine-tuning per practice
- [ ] White-label / custom branding

### Integrations
- [ ] Zoom telehealth with auto SOAP notes
- [ ] DocuSign e-signatures (Enterprise tier)
- [ ] Slack alerts for clinical events
- [ ] Quest/LabCorp electronic lab ordering
- [ ] Pharmacy e-prescribe (EPCS-ready)

### Advanced Clinical
- [ ] Clinical decision support (CDS) alerts
- [ ] Population health dashboards
- [ ] Automated prior authorization
- [ ] Patient risk stratification
- [ ] Chronic care management (CCM) workflows

### Mobile
- [ ] Native iOS app (SwiftUI)
- [ ] Native Android app (Kotlin)
- [ ] Tablet-optimized clinical workflow

---

## 💡 Future Vision (2027+)

- [ ] FDA SaMD (Software as Medical Device) certification pathway
- [ ] Multi-language voice dictation (real-time translation)
- [ ] AI scribe with differential diagnosis suggestions
- [ ] Interoperability with major EHRs (Epic, Cerner, athenahealth)
- [ ] Wearable device integration (Apple Health, Google Fit)
- [ ] Research data platform with de-identified datasets

---

## 📬 Feature Requests

Have a feature request? Email [dmitri@synalux.ai](mailto:dmitri@synalux.ai) or open a discussion in the docs portal.

---

© 2024–2026 Dmitri Costenco. Licensed under [BSL-1.1](LICENSE).
