# Synalux POS

**The restaurant POS that doesn't nickel-and-dime you.**

Every feature included. No add-on fees. No hardware lock-in. No multi-year contracts.
Use your own iPad — or any device with a browser.

<p align="center">
  <img src="https://img.shields.io/badge/Free_Forever-1_terminal-43e97b?style=for-the-badge" alt="Free Forever">
  <img src="https://img.shields.io/badge/Pro-$49/mo_(14_day_trial)-764ba2?style=for-the-badge" alt="Pro $49/mo">
  <img src="https://img.shields.io/badge/25_Languages-RTL_Supported-blue?style=for-the-badge" alt="25 Languages">
</p>

🌐 **Translations:** [Español](../docs/i18n/pos_es.md) · [Français](../docs/i18n/pos_fr.md) · [Português](../docs/i18n/pos_pt.md) · [Română](../docs/i18n/pos_ro.md) · [Українська](../docs/i18n/pos_uk.md) · [Русский](../docs/i18n/pos_ru.md) · [Deutsch](../docs/i18n/pos_de.md) · [日本語](../docs/i18n/pos_ja.md) · [한국어](../docs/i18n/pos_ko.md) · [中文](../docs/i18n/pos_zh.md) · [العربية](../docs/i18n/pos_ar.md)

---

## Try the demo

Open [synalux-pos.vercel.app/auth](https://synalux-pos.vercel.app/auth) and log in with the demo credentials below.

| | |
|---|---|
| **Login** | `demo@synalux.ai` |
| **Password** | `demo123` |
| **Venue** | Riverside Grill |

After login, enter a staff PIN to access the POS:

| Role | Name | PIN | Screens |
|---|---|---|---|
| **Cashier** | Cashier | `5555` | Register, Payment |
| **Host** | Host | `4444` | Tables, Waitlist, Reservations |
| **Server** | Server 1 | `1111` | Register, Tables, Payment, Handheld |
| **Server** | Server 2 | `2222` | Register, Tables, Payment, Handheld |
| **Bartender** | Bartender | `3333` | Bar Register, Payment, Age Verification |
| **Supervisor** | Supervisor | `6666` | Register, Tables, Reports, Voids, Discounts, KDS |
| **Manager** | Manager | `5678` | All screens + EOD + Staff |
| **Admin** | Admin | `1234` | All screens + Settings |

**All demo data resets hourly.**

---

## Why switch?

Your current POS costs too much. Toast charges $400–600/mo. Square hits $250–350/mo. Clover locks you into 3-year contracts with $2,000+ hardware.

**Synalux: Free forever for 1 terminal. $49/mo Pro with 14-day free trial. Your own iPad. Cancel anytime.**

---

## Features

### Staff Login

PIN login with clock-in, 7-level role-based access, and automatic screen routing per role.

![PIN Login](../images/pos/ipad_00_pin_entry.svg)

<details>
<summary><strong>Setup</strong></summary>

1. Add staff in **Settings > Staff Management** — name, PIN, role
2. Assign roles: cashier, host, server, bartender, supervisor, manager, admin
3. Multi-role staff see a role picker; single-role staff go straight to their screen

![Role Selection](../images/pos/ipad_00b_role_select.svg)

</details>

---

### Register

Ring orders in seconds. Categories, product grid, and order ticket — all on one screen.

![Register](../images/pos/ipad_01_register.svg)

<details>
<summary><strong>Setup</strong></summary>

1. **Settings > Menu Builder** — add categories and items
2. Set prices, modifiers, KDS stations, and barcodes per item
3. Items appear on the register automatically

![Menu Builder](../images/pos/settings_menu_builder.svg)
![Barcode Scan](../images/pos/ipad_barcode_scan.svg)
![Allergen Filter](../images/pos/ipad_allergen_filter.svg)
![Discounts](../images/pos/settings_discounts.svg)
![Auto Gratuity](../images/pos/settings_auto_gratuity.svg)
![Open Price](../images/pos/settings_open_price.svg)
![Weight Scale](../images/pos/settings_scale.svg)
![Combos](../images/pos/settings_combos.svg)
![Price Levels](../images/pos/settings_price_levels.svg)
![Nutritional Info](../images/pos/settings_nutritional.svg)
![Menu Scheduling](../images/pos/settings_menu_scheduling.svg)

</details>

---

### Tables & Floor Plan

Visual floor plan with color-coded table status. Tap a table to start or view its order.

![Tables](../images/pos/ipad_02_tables.svg)

<details>
<summary><strong>Setup</strong></summary>

1. **Settings > Floor Plan** — add tables with name, section, capacity, shape
2. Create sections (Main, Patio, Bar) for quick filtering
3. Merge, split-back, transfer, or reopen closed checks from the table detail panel

![Table Merge](../images/pos/ipad_table_merge.svg)
![Seat Management](../images/pos/ipad_seat_management.svg)
![Table Editor](../images/pos/ipad_table_editor.svg)

</details>

---

### Kitchen Display (KDS)

Ticket board with color-coded timing. Bump, recall, void. All-day count per item.

![KDS](../images/pos/ipad_03_kds.svg)

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/kds` on any tablet or TV
2. Filter by station: Grill, Fry, Prep, Expo, Bar, Cold
3. Configure routing rules in **Settings > Printers & KDS**

![Printer Routing](../images/pos/settings_printer_routing.svg)

</details>

---

### Payment

Card, cash, gift card, mobile pay, house account, EBT, and bar tabs. Split check, tips, and post-payment tip via QR.

![Payment](../images/pos/ipad_05_payment.svg)

<details>
<summary><strong>Setup</strong></summary>

1. **Card** — add Stripe keys in Settings > Integrations. Pair Reader M2 ($59).
2. **Gift cards** — issue from the Gift Cards page
3. **House accounts** — create in Settings > House Accounts

![Split Check](../images/pos/ipad_split_check.svg)
![Post-Payment Tip](../images/pos/ipad_post_payment_tip.svg)
![EBT/SNAP Payment](../images/pos/ipad_ebt_payment.svg)
![House Accounts](../images/pos/settings_house_accounts.svg)
![Receipts](../images/pos/settings_receipts.svg)
![Chargebacks](../images/pos/settings_chargebacks.svg)
![Cash Rounding](../images/pos/settings_rounding.svg)
![Wallet Pay](../images/pos/ipad_wallet_pay.svg)

</details>

---

### Customer Display

Second screen facing the customer with live order, running total, and idle promos.

![Customer Display](../images/pos/ipad_customer_display.svg)

---

### Reports

Sales, PMIX, menu engineering, speed of service, server performance, payments, voids, and labor. CSV export on every report.

![Reports](../images/pos/ipad_reports.svg)

<details>
<summary><strong>Details</strong></summary>

![Menu Engineering](../images/pos/settings_menu_engineering.svg)
![Advanced Reports](../images/pos/settings_reports_advanced.svg)
![Revenue Centers](../images/pos/settings_revenue_centers.svg)

</details>

---

### Staff & Labor

Scheduling, break tracking, overtime alerts, tip pooling (3 modes), and payroll with FLSA compliance.

![Employees](../images/pos/settings_employees.svg)

<details>
<summary><strong>Setup</strong></summary>

1. **Settings > Staff Management** — add employees with name, PIN, role
2. Configure pay periods, break rules, and overtime thresholds
3. Tip pool mode: by hours, percentage, or points

![Scheduling](../images/pos/settings_scheduling.svg)
![Break Tracking](../images/pos/settings_break_tracking.svg)
![Overtime](../images/pos/settings_overtime.svg)
![Tip Pooling](../images/pos/settings_tip_pooling.svg)
![Payroll](../images/pos/settings_payroll.svg)
![IRS Form 8027](../images/pos/settings_form_8027.svg)

</details>

---

### Online Ordering & QR Table

Customers browse your menu, order, and pay — no app needed. QR codes per table go straight to KDS.

![Online](../images/pos/online_01_menu.svg)

<details>
<summary><strong>Setup</strong></summary>

- Share your `/pos/order` link or print QR table tents from **Settings > Floor Plan**

![QR Ordering](../images/pos/ipad_qr_ordering.svg)
![Scheduled Orders](../images/pos/ipad_scheduled_orders.svg)

</details>

---

### Inventory & Recipes

Stock tracking, low-stock alerts, vendor management, and recipe builder with food cost %.

![Inventory](../images/pos/settings_inventory.svg)

<details>
<summary><strong>Setup</strong></summary>

- Add items with SKU, qty, unit, cost, and reorder threshold
- Link recipes to menu items — food cost % auto-calculates

![Recipes](../images/pos/settings_recipes.svg)
![Vendors](../images/pos/settings_vendors.svg)

</details>

---

### Gift Cards & Loyalty

Issue gift cards ($25–$250). Loyalty with points, auto-tier (Bronze/Silver/Gold), and referrals.

![Gift Cards](../images/pos/settings_gift_cards.svg)

<details>
<summary><strong>Setup</strong></summary>

![Loyalty](../images/pos/settings_loyalty.svg)
![Loyalty Check-in](../images/pos/ipad_loyalty_checkin.svg)

</details>

---

### Compliance

Age verification, RBS cert tracking, tax-exempt orders, CCPA/GDPR, and full audit trail.

![RBS Compliance](../images/pos/settings_rbs_compliance.svg)

<details>
<summary><strong>Setup</strong></summary>

![Age Verification](../images/pos/ipad_age_verification.svg)
![Tax Exempt](../images/pos/settings_tax_exempt.svg)
![Taxes](../images/pos/settings_taxes.svg)
![Privacy (CCPA/GDPR)](../images/pos/settings_privacy.svg)

</details>

---

### End of Day

Count cash, distribute tip pool, export GL journal, print Z-Report, close register.

![EOD](../images/pos/ipad_eod.svg)

<details>
<summary><strong>Setup</strong></summary>

![Cash Management](../images/pos/settings_cash_management.svg)

</details>

---

### Reservations

Timeline view with party size, table assignment, and webhook integration for Google Reserve, OpenTable, and Yelp.

![Reservations](../images/pos/ipad_reservations.svg)

---

### Catering

Large-order entry with Banquet Event Orders, delivery scheduling, and deposit tracking.

![Catering](../images/pos/ipad_catering.svg)

---

### Drive-Thru

Lane management with color-coded timing and auto-advance to the next station.

![Drive-Thru](../images/pos/ipad_drive_thru.svg)

---

### Handheld Server

Tableside ordering on any iPhone. Same menu, same modifiers, same KDS routing.

![Handheld](../images/pos/ipad_handheld_ordering.svg)

---

### Refunds

Partial or full refund with reason codes. Reopen closed checks for corrections.

![Refund](../images/pos/ipad_refund.svg)
![Reopen Check](../images/pos/ipad_reopen_check.svg)

---

### Multi-Location & Franchise

Per-venue KPIs, consolidated P&L, config push, and franchise reporting.

![Multi-Location](../images/pos/settings_multi_location.svg)
![Franchise](../images/pos/settings_franchise.svg)

---

### AI Ordering

Natural language order parsing from phone or SMS. Runs locally via Ollama — no cloud API needed.

![AI Ordering](../images/pos/ai_ordering.svg)

---

### More

<details>
<summary><strong>Training Mode</strong></summary>

Isolated sandbox. Orders excluded from reports.

![Training](../images/pos/settings_training_mode.svg)

</details>

<details>
<summary><strong>Offline Mode (PWA)</strong></summary>

Core pages precached for offline use. Orders queue locally and sync on reconnect. Card payments require network.

![Offline](../images/pos/ipad_offline_mode.svg)

</details>

<details>
<summary><strong>Integrations</strong></summary>

Stripe, DoorDash, Uber Eats, Grubhub, QuickBooks, Xero, Gusto, ADP, OpenTable, Google Reserve, Yelp, Twilio, SendGrid.

![Integrations](../images/pos/settings_integrations.svg)

</details>

<details>
<summary><strong>Operational Forms</strong></summary>

Cash Count, Void Auth, Tax-Exempt Cert, Catering BEO, Tip Declaration, Inventory Count, Time-Off, Purchase Order, Incident Log, Daily Specials, Prep List, Server Checkout.

![Forms](../images/pos/settings_forms.svg)

</details>

<details>
<summary><strong>Digital Menu Board</strong></summary>

Configure layout, sections, and pricing display. Assign to any TV or display.

![Menu Board](../images/pos/settings_menu_board.svg)

</details>

<details>
<summary><strong>Marketing & Campaigns</strong></summary>

Email/SMS blasts, promo codes, audience segments, and send history.

![Marketing](../images/pos/settings_marketing.svg)

</details>

<details>
<summary><strong>Customer Feedback</strong></summary>

Post-visit surveys, star ratings, comment review, and response templates.

![Customer Feedback](../images/pos/settings_customer_feedback.svg)

</details>

<details>
<summary><strong>Label Printer</strong></summary>

ZPL-compatible (Zebra, Brother). Price/SKU/prep labels from any menu or inventory item.

![Label Printer](../images/pos/settings_label_printer.svg)

</details>

<details>
<summary><strong>Equipment Tracking</strong></summary>

Device registry with serial numbers, warranty, maintenance schedule, and depreciation.

![Equipment](../images/pos/settings_equipment.svg)

</details>

<details>
<summary><strong>Manager Mobile</strong></summary>

iPhone dashboard with live KPIs, alerts, and quick actions.

![Manager Mobile](../images/pos/iphone_01_dashboard.svg)

</details>

<details>
<summary><strong>Synalux Advantage</strong></summary>

Referral tracking, partner benefits, and commission tiers.

![Advantage](../images/pos/settings_advantage.svg)

</details>

---

## Plans & Pricing

**Free forever** for 1 terminal. **14-day free trial** on all paid plans. Cancel anytime.

| | **Free** | **Pro** | **Business** | **Enterprise** |
|---|:---:|:---:|:---:|:---:|
| **Monthly** | **$0 forever** | **$49/mo** | **$99/mo** | **$199/location** |
| **Trial** | No card needed | **14 days free** | **14 days free** | **14 days free** |
| Terminals | 1 | Unlimited | Unlimited | Unlimited |
| Locations | 1 | 1 | 1 | Unlimited |
| Register + KDS + Reports | Yes | Yes | Yes | Yes |
| Online ordering | Yes | Yes | Yes | Yes |
| Loyalty + Marketing | — | Yes | Yes | Yes |
| Scheduling + Payroll | — | Yes | Yes | Yes |
| Reservations + Catering | — | Yes | Yes | Yes |
| Priority support | — | — | 24h SLA | 4h SLA |
| Multi-location + Franchise | — | — | — | Yes |
| API access | — | — | — | Yes |
| **Contract** | **None** | **None** | **None** | **None** |

**Processing:** 2.6% + $0.10 in-person · 2.9% + $0.30 online (via Stripe)

**Hardware — Bring Your Own Device:**

| Item | Synalux | Toast | Square | Clover |
|------|--------:|------:|-------:|-------:|
| Terminal | **$0** (any iPad) | $799–999 | $299 | $1,399–1,899 |
| Handheld | **$0** (any iPhone) | $409–627 | $399 | $499–749 |
| KDS | **$0** (any tablet/TV) | $499–699 | $300–900 | $300–900 |
| Card reader | **$59** (Stripe Reader) | $249–299 | $59 | Included |
| **Total** | **$59** | **$1,500–2,500+** | **$600–1,200** | **$2,000–4,000+** |

---

## First-year savings

| vs Competitor | Their Cost | Synalux Pro | **You Save** |
|---|---:|---:|---:|
| vs Toast | $4,800–7,200/yr + $1,500 HW | $588/yr + $59 HW | **$5,700–8,100** |
| vs Square | $3,000–4,200/yr + $600 HW | $588/yr + $59 HW | **$3,000–4,200** |
| vs Clover | $4,200–6,000/yr + $2,000 HW | $588/yr + $59 HW | **$5,600–7,700** |
| vs TouchBistro | $6,000–9,600/yr + HW | $588/yr + $59 HW | **$6,400–10,000** |
| vs Lightspeed | $5,400–7,200/yr + $800 HW | $588/yr + $59 HW | **$5,600–7,700** |

---

## 25 languages

English, Spanish, French, Chinese, Arabic, Romanian, Portuguese, German, Italian, Japanese, Korean, Vietnamese, Russian, Ukrainian, Polish, Turkish, Dutch, Swedish, Hebrew, Thai, Hindi, Indonesian, Malay, Filipino, Greek. RTL supported.

---

<details>
<summary><strong>Developer: Integration Setup Guide</strong></summary>

Every integration activates by adding credentials in **Settings > Integrations**. No code changes needed.

| Integration | Env var | What activates |
|---|---|---|
| **Stripe** (card payments) | `STRIPE_SECRET_KEY` | Card tap/chip/swipe, Tap-to-Pay, online payments |
| **SendGrid** (email receipts) | `SENDGRID_API_KEY` | Email receipt button after payment |
| **Twilio** (SMS) | `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` | SMS receipts, phone ordering |
| **DoorDash / Uber Eats / Grubhub** | Webhook URL | Delivery orders on KDS with purple badge |
| **Google Reserve / OpenTable / Yelp** | Webhook URL | Auto-created reservations |
| **QuickBooks / Xero** | `QUICKBOOKS_ACCESS_TOKEN` or `XERO_ACCESS_TOKEN` | EOD GL journal auto-sync |
| **Forage** (EBT/SNAP) | `FORAGE_API_KEY` | EBT payment, eligible item flagging |
| **Dwolla / Stripe Treasury** | `DWOLLA_API_KEY` or `STRIPE_TREASURY_KEY` | ACH payroll direct deposit |
| **Ollama** (AI ordering) | `NEXT_PUBLIC_LOCAL_LLM_URL` | Natural language order parsing |
| **Apple / Google Wallet** | Pass Type ID + signing cert | Loyalty "Add to Wallet" |
| **Zebra / Brother** (labels) | Printer IP in Settings | ZPL price/SKU/prep labels |

**Required env vars:** `NEXT_PUBLIC_POS_SUPABASE_URL`, `NEXT_PUBLIC_POS_SUPABASE_ANON_KEY`, `POS_SUPABASE_SERVICE_ROLE_KEY`

</details>

<details>
<summary><strong>Developer: E2E Workflow & Role Testing</strong></summary>

![E2E Workflow](../images/pos/ipad_00_e2e_workflow.svg)
![Combined Role Tests](../images/pos/ipad_00c_combined_roles.svg)

</details>

## Top 3 Competitors vs Synalux POS — Feature-by-Feature

Every feature, head-to-head. ✅ = included, 💰 = paid add-on, ❌ = not available, 🔒 = locked to proprietary ecosystem.

| # | Feature | **Synalux ($49/mo)** | **Toast ($69–400/mo)** | **Square ($49–250/mo)** | **Clover ($85–300/mo)** |
|---|---------|:---:|:---:|:---:|:---:|
| | **REGISTER & ORDER ENTRY** | | | | |
| 1 | 3-panel register (categories + grid + ticket) | ✅ | ✅ | ✅ | ✅ |
| 2 | Barcode scan-to-order | ✅ | ✅ | ✅ | ✅ |
| 3 | Weight-based pricing (deli/produce) | ✅ | ❌ | ❌ | ❌ |
| 4 | Open-price / market-price items | ✅ | ✅ | ✅ | ✅ |
| 5 | Combo engine (auto-detect eligible items) | ✅ | 💰 Add-on | ❌ | ❌ |
| 6 | Seat assignment + course firing | ✅ | ✅ | 💰 Premium only | 💰 App add-on |
| 7 | Void reason modal (manager required) | ✅ | ✅ | ❌ | ❌ |
| 8 | AI-generated dish images | ✅ | ❌ | ❌ | ❌ |
| 9 | Training mode (isolated sandbox) | ✅ | ✅ | ✅ | ❌ |
| 10 | Reopen closed check | ✅ | ✅ | ❌ | ❌ |
| 11 | Drive-thru + lane queue | ✅ | ✅ | ✅ | ✅ |
| | **KITCHEN DISPLAY (KDS)** | | | | |
| 12 | KDS ticket board | ✅ | ✅ | 💰 $20/mo/device | 💰 Third-party app |
| 13 | All-day count (total pending per item) | ✅ | ❌ | ❌ | ❌ |
| 14 | Bump / recall / void | ✅ | ✅ | 💰 Paid KDS | 💰 Third-party app |
| 15 | Color-coded by order type | ✅ | ✅ | ❌ | ❌ |
| 16 | Realtime ticket sync (WebSocket) | ✅ | ✅ | ✅ | ✅ |
| 17 | Auto-print kitchen tickets (ESC/POS) | ✅ | ✅ | ❌ | 💰 App add-on |
| | **TABLE MANAGEMENT** | | | | |
| 18 | Interactive floor plan editor | ✅ | ✅ | 💰 Plus+ only | 💰 App add-on |
| 19 | Table status colors (available/occupied/reserved) | ✅ | ✅ | 💰 Plus+ only | ❌ |
| 20 | Table merge / split-back / transfer | ✅ | ✅ | ❌ | ❌ |
| 21 | QR table ordering (guest scans & orders) | ✅ | 💰 Add-on | ❌ | ❌ |
| | **PAYMENTS** | | | | |
| 22 | Card (NFC / chip / swipe) | ✅ Stripe | 🔒 Toast only | 🔒 Square only | 🔒 Clover/reseller |
| 23 | Choose your own processor | ✅ | ❌ | ❌ | ❌ |
| 24 | Cash with CAD penny rounding | ✅ | ❌ | ❌ | ❌ |
| 25 | Gift card | ✅ | ✅ | ✅ | ✅ |
| 26 | House accounts + invoicing | ✅ | 💰 Add-on | ❌ | ❌ |
| 27 | Split check (even / custom / seat) | ✅ | ✅ | ✅ | ✅ |
| 28 | Bar tab (pre-auth) | ✅ | ✅ | ❌ | 💰 App add-on |
| 29 | EBT / SNAP (via Forage) | ✅ | ❌ | ❌ | ❌ |
| 30 | Post-payment tip via QR code | ✅ | ❌ | ✅ | ❌ |
| 31 | Cash discount / dual pricing | ✅ | ✅ | ❌ | 💰 App add-on |
| 32 | Chargeback evidence auto-pack | ✅ | ✅ | ✅ | ❌ |
| 33 | Tap-to-Pay on iPhone | ✅ | ✅ | ✅ | ❌ |
| | **MENU MANAGEMENT** | | | | |
| 34 | Modifier groups + forced modifiers | ✅ | ✅ | ✅ | ✅ |
| 35 | Recipe management + food cost tracking | ✅ | 💰 Add-on | ❌ | ❌ |
| 36 | Menu engineering quadrant (Star/Dog/Puzzle/Workhorse) | ✅ | ❌ | ❌ | ❌ |
| 37 | Allergen filter (customer QR scan) | ✅ | ✅ | ✅ | ❌ |
| 38 | Price levels (happy hour, lunch, etc.) | ✅ | ✅ | 💰 Plus only | 💰 App add-on |
| | **ONLINE ORDERING** | | | | |
| 39 | Branded online ordering page | ✅ | 💰 $50–75/mo | ✅ | 💰 $30–50/mo app |
| 40 | QR dine-in ordering | ✅ | 💰 Add-on | ❌ | ❌ |
| 41 | Online order throttling | ✅ | ✅ | ❌ | ❌ |
| 42 | Delivery webhook (DoorDash/Uber/Grubhub) | ✅ | ✅ | ✅ | 💰 App add-on |
| | **LOYALTY & MARKETING** | | | | |
| 43 | Points + tiers (bronze/silver/gold) | ✅ | 💰 $50–75/mo | ✅ Basic only | 💰 $10–30/mo app |
| 44 | Referral program | ✅ | 💰 Add-on | ❌ | ❌ |
| 45 | Email campaigns (SendGrid) | ✅ | 💰 $75/mo | 💰 Marketing add-on | 💰 Third-party |
| 46 | SMS campaigns (Twilio) | ✅ | 💰 $75/mo | 💰 Marketing add-on | 💰 Third-party |
| 47 | TCPA consent tracking | ✅ | ❌ | ❌ | ❌ |
| 48 | Reputation management (auto-prompt reviews) | ✅ | ❌ | ❌ | ❌ |
| | **STAFF & LABOR** | | | | |
| 49 | PIN authentication + role-based routing | ✅ 7-level RBAC | ✅ | ✅ Basic | ✅ Basic |
| 50 | Revenue Center strict filtering | ✅ | ❌ | ❌ | ❌ |
| 51 | Clock in / out | ✅ | ✅ | ✅ | ✅ |
| 52 | Break tracking (meal + rest, CA §226.7) | ✅ | ❌ | ❌ | ❌ |
| 53 | Predictive scheduling alerts (overtime, clopening, minor labor) | ✅ | ❌ | ❌ | ❌ |
| 54 | Tip pooling (FLSA-enforced, 3 modes) | ✅ | ❌ | ❌ | ❌ |
| 55 | Tip credit compliance | ✅ | ❌ | ❌ | ❌ |
| 56 | RBS certification tracking + expiry alerts | ✅ | ❌ | ❌ | ❌ |
| 57 | Payroll export (Gusto/ADP) | ✅ | 💰 $9/emp/mo | 💰 Separate product | 💰 Third-party |
| | **INVENTORY** | | | | |
| 58 | Item tracking (SKU, unit, cost, threshold) | ✅ | ✅ Basic | ✅ Plus only | ✅ Basic |
| 59 | Physical stocktake mode (bulk count) | ✅ | ❌ | ❌ | ❌ |
| 60 | Low-stock + out-of-stock alerts | ✅ | ✅ | ✅ | 💰 App add-on |
| 61 | Vendor management + payment terms | ✅ | ❌ | ❌ | ❌ |
| | **REPORTS & ANALYTICS** | | | | |
| 62 | Sales report (hourly heatmap) | ✅ | ✅ | ✅ Premium only | ✅ Basic |
| 63 | PMIX (product mix) | ✅ | ✅ | ✅ | 💰 App add-on |
| 64 | Menu engineering quadrant report | ✅ | ❌ | ❌ | ❌ |
| 65 | Speed-of-service (per-station ticket times) | ✅ | ✅ | ❌ | ❌ |
| 66 | Server performance leaderboard | ✅ | ✅ | ❌ | ❌ |
| 67 | Voids / comps report | ✅ | ✅ | ✅ | ✅ |
| 68 | Labor report | ✅ | ✅ | 💰 Separate product | ❌ |
| 69 | CSV export on every report | ✅ | ✅ | ✅ | 💰 Paid tier |
| | **COMPLIANCE & AUDIT** | | | | |
| 70 | CCPA / GDPR data deletion API | ✅ | ❌ | ❌ | ❌ |
| 71 | Age verification (alcohol, DL scan) | ✅ | ✅ | ❌ | ❌ |
| 72 | Alcohol incident logging (refusal, cutoff) | ✅ | ❌ | ❌ | ❌ |
| 73 | IRS Form 8027 tip reporting | ✅ | ✅ | ✅ | ❌ |
| 74 | Tax-exempt sales toggle | ✅ | ✅ | ✅ | ✅ |
| 75 | Full audit trail on every action | ✅ | ✅ | ❌ | ❌ |
| | **BACK OFFICE** | | | | |
| 76 | End-of-day (denomination counter, cash mgmt) | ✅ | ✅ | ✅ | ✅ |
| 77 | Tip pool distribution at EOD | ✅ | ❌ | ❌ | ❌ |
| 78 | GL journal export (QuickBooks / Xero) | ✅ | 💰 Add-on | 💰 Add-on | 💰 Third-party |
| 79 | 12 printable operational forms | ✅ | ❌ | ❌ | ❌ |
| 80 | Multi-location dashboard + consolidated P&L | ✅ Enterprise | ✅ $400+/mo/loc | ✅ Premium | 💰 Enterprise only |
| | **INTEGRATIONS** | | | | |
| 81 | Stripe Terminal | ✅ | ❌ Locked | ❌ Locked | ❌ Locked |
| 82 | OpenTable / Google Reserve / Yelp reservations | ✅ | 💰 Add-on | ❌ | ❌ |
| 83 | QuickBooks / Xero sync | ✅ | 💰 Add-on | 💰 Add-on | 💰 Third-party |
| 84 | ESC/POS receipt + kitchen printing | ✅ | ✅ | ❌ | 💰 App add-on |
| 85 | Cash drawer kick | ✅ | ✅ | ✅ | ✅ |
| 86 | Zebra label printing | ✅ | ❌ | ❌ | ❌ |
| | **TECHNOLOGY & PLATFORM** | | | | |
| 87 | Runs on any device (BYOD) | ✅ Browser-based | ❌ Toast HW only | ⚠️ Square HW + iPad | ❌ Clover HW only |
| 88 | PWA + offline mode | ✅ | ✅ Limited | ❌ | ❌ |
| 89 | 25 languages + RTL | ✅ | ⚠️ English + Spanish | ⚠️ Limited i18n | ⚠️ English only |
| 90 | Realtime sync (WebSocket) | ✅ Supabase | ✅ Proprietary | ✅ | ✅ |
| 91 | REST API access | ✅ 29 routes | ⚠️ Partner API only | ✅ Open API | ⚠️ Limited |
| 92 | Datadog RUM + Logs monitoring | ✅ | ❌ | ❌ | ❌ |
| 93 | Instant deploys (Vercel) | ✅ | ❌ Device firmware | ✅ App store | ❌ Device firmware |
| 94 | State-specific tax + labor config (64 jurisdictions) | ✅ | ⚠️ Manual setup | ⚠️ Manual setup | ⚠️ Manual setup |
| | **PRICING & CONTRACTS** | | | | |
| 95 | Monthly price (all features) | **$49** | **$200–400** | **$149–250** | **$150–300** |
| 96 | Hardware cost (2 terminals) | **$59** | **$1,500–3,000+** | **$600–1,200** | **$2,000–4,000+** |
| 97 | Contract length | **Month-to-month** | **2–3 years** | **Month-to-month** | **36–48 months** |
| 98 | Early termination fee | **$0** | **$500–2,000+** | **$0** | **$500–1,500+** |
| 99 | Per-terminal fee | **$0** (unlimited) | **Yes** | **Yes** | **Yes** |
| 100 | Year-1 total (1 loc, 2 terms) | **$647** | **$5,300–10,200+** | **$2,400–4,200+** | **$5,800–8,600+** |

### Scorecard

| | **Synalux** | **Toast** | **Square** | **Clover** |
|---|:---:|:---:|:---:|:---:|
| Features included at base price | **86 / 100** | **38 / 100** | **34 / 100** | **24 / 100** |
| Features requiring paid add-ons | **0** | **18** | **12** | **22** |
| Features unavailable at any price | **0** | **24** | **34** | **34** |
| Synalux-exclusive features | **22** | — | — | — |
| Year-1 savings vs Synalux | — | **$4,600–9,500** | **$1,700–3,500** | **$5,100–7,900** |

> **TL;DR** — Synalux includes 86 of 100 features at $49/mo with zero add-on fees. Toast includes 38 and charges $200–400/mo after add-ons. Square includes 34 and charges $149–250/mo. Clover includes 24 and charges $150–300/mo plus $2,000–4,000 in mandatory proprietary hardware. No other POS offers weight-based pricing, menu engineering, predictive scheduling, break tracking, tip credit compliance, CCPA deletion, revenue center filtering, or 12 printable operational forms at any price.

---

## License

BUSL-1.1 — see [`LICENSE`](LICENSE).
