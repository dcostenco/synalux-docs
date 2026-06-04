# Synalux POS

**Full-featured restaurant POS — runs on any device with a browser.**

Every feature included. No hardware lock-in. No multi-year contracts.
Use your own iPad — or any device with a browser.

<p align="center">
  <img src="https://img.shields.io/badge/25_Languages-RTL_Supported-blue?style=for-the-badge" alt="25 Languages">
</p>

🌐 **Translations:** [Español](../docs/i18n/pos_es.md) · [Français](../docs/i18n/pos_fr.md) · [Português](../docs/i18n/pos_pt.md) · [Română](../docs/i18n/pos_ro.md) · [Українська](../docs/i18n/pos_uk.md) · [Русский](../docs/i18n/pos_ru.md) · [Deutsch](../docs/i18n/pos_de.md) · [日本語](../docs/i18n/pos_ja.md) · [한국어](../docs/i18n/pos_ko.md) · [中文](../docs/i18n/pos_zh.md) · [العربية](../docs/i18n/pos_ar.md)

---

## Table of Contents

- [Try the demo](#try-the-demo)
- [Features](#features)
  - [Staff Login](#staff-login)
  - [Register](#register)
  - [Tables & Floor Plan](#tables--floor-plan)
  - [Kitchen Display (KDS)](#kitchen-display-kds)
  - [Payment](#payment)
  - [Staff & Labor](#staff--labor)
  - [Online Ordering & QR Table](#online-ordering--qr-table)
  - [Delivery Management](#delivery-management)
  - [AI Chat Assistant](#ai-chat-assistant)
  - [Pizza Builder & Modifiers](#pizza-builder--modifiers)
  - [Customer Display](#customer-display)
  - [Reports](#reports)
  - [Inventory & Recipes](#inventory--recipes)
  - [Gift Cards & Loyalty](#gift-cards--loyalty)
  - [Compliance](#compliance)
  - [End of Day](#end-of-day)
  - [Reservations](#reservations)
  - [Catering](#catering)
  - [Drive-Thru](#drive-thru)
  - [Handheld Server](#handheld-server)
  - [Refunds](#refunds)
  - [Multi-Location & Franchise](#multi-location--franchise)
  - [Accounting & Ledger](#accounting--ledger)
  - [Coursing](#coursing)
  - [Order Throttling](#order-throttling)
  - [HR & Timesheets](#hr--timesheets)
  - [More](#more)
- [25 Languages](#25-languages)
- [Developer Guide](#developer-integration-setup-guide)

---

## Try the demo

Open [synalux-pos.vercel.app/auth](https://synalux-pos.vercel.app/auth) and log in with the demo credentials below.

| | |
|---|---|
| **Login** | `demo@synalux.ai` |
| **Password** | `demo1234` |
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

## Features

### Staff Login

PIN login with clock-in, 7-level role-based access, and automatic screen routing per role.

![PIN Login](../images/pos/ipad_00_pin_entry.png)

<details>
<summary><strong>Setup</strong></summary>

1. Add staff in **Settings > Staff Management** — name, PIN, role
2. Assign roles: cashier, host, server, bartender, supervisor, manager, admin
3. Multi-role staff see a role picker; single-role staff go straight to their screen

![Role Selection](../images/pos/ipad_00b_role_select.png)

</details>

---

### Register

Ring orders in seconds. Categories, product grid, and order ticket — all on one screen.

![Register](../images/pos/ipad_01_register.png)

<details>
<summary><strong>Setup</strong></summary>

1. **Settings > Menu Builder** — add categories and items
2. Set prices, modifiers, KDS stations, and barcodes per item
3. Items appear on the register automatically

![Menu Builder](../images/pos/settings_menu_builder.png)
![Barcode Scan](../images/pos/ipad_barcode_scan.svg)
![Allergen Filter](../images/pos/ipad_allergen_filter.svg)
![Discounts](../images/pos/settings_discounts.png)
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

![Tables](../images/pos/ipad_02_tables.png)

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

![KDS](../images/pos/ipad_03_kds.png)

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/kds` on any tablet or TV
2. Filter by station: Grill, Fry, Prep, Expo, Bar, Cold
3. Configure routing rules in **Settings > Printers & KDS**

![Printer Routing](../images/pos/settings_printer_routing.svg)

</details>

---

### Payment

Card, cash, gift card, mobile pay, house account, EBT, bar tabs, Tap-to-Pay on iPhone, and cash discount/dual pricing. Split check, tips, and post-payment tip via QR.

![Payment](../images/pos/ipad_05_payment.png)

<details>
<summary><strong>Setup</strong></summary>

1. **Card** — add Stripe keys in **Settings > Integrations**. Pair a Stripe Reader M2
2. **Tap-to-Pay on iPhone** — enable in Stripe Dashboard, then tap "📱 Tap to Pay" on the payment screen. Uses your iPhone as a contactless card reader — no additional hardware
3. **Cash discount / Dual pricing** — configure the cash discount percentage in **Settings > Venue > Cash Discount**. Customers see both card and cash prices at checkout (e.g. Card: $100 | Cash: $96.50)
4. **Bar tabs** — tap "🍺 Start Tab" at payment to pre-authorize a card and hold the check open. Open tabs show in the register sidebar with a one-tap "Close" button to capture the final amount
5. **Gift cards** — issue from the Gift Cards page
6. **House accounts** — create in **Settings > House Accounts**, then charge at payment
7. **EBT/SNAP** — add Forage API key in Settings > Integrations. Eligible items are automatically calculated
8. **Split check** — split by even, custom amount, or per-seat. Each split can pay by different method (card/cash)

![Split Check](../images/pos/ipad_split_check.svg)
![Bar Tab](../images/pos/ipad_bar_tab.png)
![Tap-to-Pay](../images/pos/ipad_tap_to_pay.png)
![Cash Discount](../images/pos/ipad_cash_discount.png)
![Post-Payment Tip](../images/pos/ipad_post_payment_tip.svg)
![EBT/SNAP Payment](../images/pos/ipad_ebt_payment.svg)
![House Accounts](../images/pos/settings_house_accounts.svg)
![Cash Discount Settings](../images/pos/settings_cash_discount.png)
![Receipts](../images/pos/settings_receipts.svg)
![Chargebacks](../images/pos/settings_chargebacks.svg)
![Cash Rounding](../images/pos/settings_rounding.svg)
![Wallet Pay](../images/pos/ipad_wallet_pay.svg)

</details>

---

### Staff & Labor

Scheduling, break tracking, overtime alerts, tip pooling (3 modes), and payroll with FLSA compliance.

![Employees](../images/pos/settings_employees.png)

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

Customers browse your menu, order, and pay — no app needed. Pickup and delivery channels. QR codes per table go straight to KDS. Scheduled orders, loyalty points, promo codes, AI chat assistant, and order tracking.

![Online](../images/pos/online_01_menu.png)

<details>
<summary><strong>Setup</strong></summary>

1. **Enable** — turn on online ordering in **Settings > Online Ordering**
2. **Business hours** — set per-day open/close times. Orders are blocked outside hours
3. **Channels** — enable Pickup and/or Delivery independently with separate min-order amounts and prep times
4. **Delivery zones** — define radius zones with per-zone fees and minimums. Set venue lat/lng coordinates
5. **Closed dates** — add holidays when the venue is closed
6. **Share your link** — customers order at `https://your-slug.synalux.ai` or your custom domain
7. **QR table ordering** — print QR tents from **Settings > Floor Plan**. Customer scans, orders, and the ticket goes straight to KDS
8. **Scheduled orders** — customers pick a future date/time at checkout. Orders appear on KDS at the scheduled time
9. **Promo codes** — one-time-use codes validated server-side. Duplicates are rejected
10. **AI chat** — customer-facing AI understands your full menu including modifiers and pizza builder. Supports 14 languages with voice input/output

![QR Ordering](../images/pos/ipad_qr_ordering.svg)
![Scheduled Orders](../images/pos/ipad_scheduled_orders.png)
![AI Chat (Customer)](../images/pos/ipad_ai_chat_oo.png)
![Order Tracking](../images/pos/ipad_order_tracking.png)
![Online Ordering Settings](../images/pos/settings_online_ordering.png)

</details>

---

### Delivery Management

In-house drivers, 3PD delegation (DoorDash Drive, Uber Direct), or hybrid mode. Route optimization, driver GPS tracking, auto-dispatch, and menu sync to 3PD platforms.

![Delivery](../images/pos/ipad_delivery_management.png)

<details>
<summary><strong>Setup</strong></summary>

1. **Choose mode** in **Settings > Delivery**: 3PD Only, In-House, or Hybrid (try in-house first, fall back to 3PD)
2. **3PD providers** — add DoorDash Drive or Uber Direct API credentials. The system creates deliveries via the provider API and tracks status
3. **In-house drivers** — add drivers with name, phone, vehicle type (car/bike/scooter/walk), and max concurrent orders
4. **Menu sync** — tap "Sync to DoorDash" / "Sync to Uber Eats" to upload your menu. Enable auto-sync to push changes automatically when you edit menu items
5. **Driver mobile page** — drivers open `/pos/delivery/driver` on their phone. They see assigned orders, tap to navigate, mark picked up / delivered / failed, and auto-report GPS every 30s
6. **Route optimization** — batch dispatch clusters nearby deliveries and assigns the optimal driver using proximity scoring
7. **Order status sync** — when KDS bumps an order to "ready", the system notifies the 3PD provider and triggers auto-dispatch for in-house drivers

![Driver Mobile](../images/pos/ipad_delivery_driver.svg)
![Delivery Settings](../images/pos/settings_delivery.png)

</details>

---

### AI Chat Assistant

Context-aware AI assistant on every POS page (15 surfaces) and on the online ordering page for customers. Voice input, 14 languages, quick prompts, and Prism memory for learning patterns.

![AI Chat (POS)](../images/pos/ipad_ai_chat_pos.png)

<details>
<summary><strong>How it works</strong></summary>

**POS Staff Chat** — appears on every page, auto-loads live data for that screen:
- **Register** — "What's the most popular item today?", "Find order with 3 cokes", "Customer last name Garcia"
- **KDS** — "What's the oldest ticket?", "Any allergens on ticket 4?", "Grill count?"
- **Tables** — "Any 4-tops available?", "How long has table 12 been seated?"
- **Inventory** — "What's low on stock?", "How many cases of Bud Light?"
- **Reports** — "Compare lunch vs dinner sales", "Top 5 items this week", "Labor % today?"
- **EOD** — "Start closing", "What's the tip pool?", "Any cash variance?"
- **Delivery** — "Where is driver Maria?", "How many pending deliveries?"
- **+ 8 more surfaces** (Staff, Reservations, Catering, Loyalty, Gift Cards, Disputes, Scheduling, Table Ops)

**OO Customer Chat** — customers ask "Make me a half pepperoni half mushroom pizza" and the AI builds the order with correct modifiers and pricing:
- Voice input (microphone) + voice output (speaker) with adjustable speed/pitch/gender
- 14 languages with locale picker
- Returning customer greeting via cookie
- Tool calls: add_to_cart, remove_from_cart, filter_menu, suggest_combo

![AI Chat (Customer)](../images/pos/ipad_ai_chat_oo.png)

</details>

---

### Pizza Builder & Modifiers

Visual half/half pizza builder with per-topping placement and intensity. Standard modifiers with qty, nested groups, forced/optional, and max-quantity limits.

![Pizza Builder](../images/pos/ipad_pizza_builder.png)

<details>
<summary><strong>Setup</strong></summary>

1. **Standard modifiers** — create modifier groups in **Settings > Menu Builder**. Set min/max selections, price deltas, and max quantity per option
2. **Pizza builder** — set a modifier group's display mode to "🍕 Pizza Builder" in the menu builder. This triggers the visual half/half UI instead of checkboxes
3. **Placement** — customers choose Whole, Left Half, or Right Half for each topping. Half placement = 50% of the topping price
4. **Intensity** — None (not selected), Light (75% price), Regular (100%), Extra (150% price)
5. **3PD compatibility** — pizza toppings sync to DoorDash/UberEats as standard modifiers (placement/intensity are stripped since 3PD doesn't support halves). This is logged as an incompatibility
6. **AI chat** — "Make me a half pepperoni half mushroom pizza" works without the visual builder. The AI maps to the correct modifiers and prices

![Modifier Sheet](../images/pos/ipad_modifier_sheet.png)

</details>

---

### Customer Display

Second screen facing the customer with live order, running total, and idle promos.

![Customer Display](../images/pos/ipad_customer_display.png)

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/display` on a second iPad or monitor facing the customer
2. The display auto-syncs with the active register order in real time
3. Configure idle promo images in **Settings > Venue**

</details>

---

### Reports

Sales, PMIX, menu engineering, speed of service, server leaderboard, payments, voids, and labor. CSV export on every report.

![Reports](../images/pos/ipad_reports.png)

<details>
<summary><strong>Setup</strong></summary>

1. Access from the **Reports** page — all reports are auto-generated from order data
2. **Sales** — hourly heatmap, daily/weekly/monthly totals
3. **PMIX** — product mix by category, item, and modifier
4. **Menu engineering** — Star/Dog/Puzzle/Workhorse quadrant analysis
5. **Speed of service** — per-station ticket times at `/pos/reports/speed`
6. **Server leaderboard** — staff performance ranking at `/pos/reports/leaderboard`
7. **CSV export** — every report has a one-click CSV download

![Menu Engineering](../images/pos/settings_menu_engineering.svg)
![Advanced Reports](../images/pos/settings_reports_advanced.svg)
![Revenue Centers](../images/pos/settings_revenue_centers.svg)

</details>

---

### Inventory & Recipes

Stock tracking, low-stock alerts, vendor management, and recipe builder with food cost %.

![Inventory](../images/pos/settings_inventory.png)

<details>
<summary><strong>Setup</strong></summary>

- Add items with SKU, qty, unit, cost, and reorder threshold
- Link recipes to menu items — food cost % auto-calculates

![Recipes](../images/pos/settings_recipes.png)
![Vendors](../images/pos/settings_vendors.svg)

</details>

---

### Gift Cards & Loyalty

Issue gift cards ($25–$250). Loyalty with points, auto-tier (Bronze/Silver/Gold), and referrals.

![Gift Cards](../images/pos/settings_gift_cards.png)

<details>
<summary><strong>Setup</strong></summary>

![Loyalty](../images/pos/settings_loyalty.png)
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
![Taxes](../images/pos/settings_taxes.png)
![Privacy (CCPA/GDPR)](../images/pos/settings_privacy.svg)

</details>

---

### End of Day

Count cash, distribute tip pool, export GL journal, print Z-Report, close register.

![EOD](../images/pos/ipad_eod.png)

<details>
<summary><strong>Setup</strong></summary>

![Cash Management](../images/pos/settings_cash_management.svg)

</details>

---

### Reservations

Timeline view with party size, table assignment, and webhook integration for Google Reserve, OpenTable, and Yelp.

![Reservations](../images/pos/ipad_reservations.png)

<details>
<summary><strong>Setup</strong></summary>

1. Open the **Reservations** page to see the timeline view
2. Add reservations manually with party size, date/time, and table assignment
3. **Webhook integration** — configure webhooks in **Settings > Integrations** for Google Reserve, OpenTable, or Yelp. Incoming reservations auto-create in the system
4. Waitlist mode available for walk-ins

</details>

---

### Catering

Large-order entry with Banquet Event Orders, delivery scheduling, and deposit tracking.

![Catering](../images/pos/ipad_catering.png)

<details>
<summary><strong>Setup</strong></summary>

1. Open the **Catering** page to create catering events
2. Build a Banquet Event Order (BEO) with menu items, headcount, and timeline
3. Set delivery date/time and assign a driver or 3PD provider
4. Track deposits (partial payments) against the event total

</details>

---

### Drive-Thru

Lane management with color-coded timing and auto-advance to the next station.

![Drive-Thru](../images/pos/ipad_drive_thru.png)

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/drive-thru` on a dedicated screen per lane
2. Orders flow through stations: Order → Prep → Window
3. Color-coded timing (green < 3 min, yellow < 5 min, red > 5 min)
4. Auto-advance when KDS bumps the ticket

</details>

---

### Handheld Server

Tableside ordering on any iPhone. Same menu, same modifiers, same KDS routing.

![Handheld](../images/pos/ipad_handheld_ordering.png)

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/handheld` on any iPhone or small tablet
2. Server logs in with their PIN — same role-based access as the register
3. Tap a table → add items → send to KDS. Full modifier support including pizza builder

</details>

---

### Refunds

Partial or full refund with reason codes. Reopen closed checks for corrections.

![Refund](../images/pos/ipad_refund.png)
![Reopen Check](../images/pos/ipad_reopen_check.svg)

<details>
<summary><strong>Setup</strong></summary>

1. Open the **Refunds** page or tap "Refund" on any completed order
2. Choose partial (specific items) or full refund
3. Select a reason code (wrong item, quality, customer request, etc.)
4. Stripe refund is processed automatically. Cash refunds are recorded for drawer reconciliation
5. **Reopen check** — managers can reopen a closed order for corrections, then re-close

</details>

---

### Multi-Location & Franchise

Per-venue KPIs, consolidated P&L, config push, and franchise reporting.

![Multi-Location](../images/pos/settings_multi_location.png)
![Franchise](../images/pos/settings_franchise.svg)

<details>
<summary><strong>Setup</strong></summary>

1. Create additional venues under the same workspace in **Settings > Multi-Location**
2. Push menu, tax, and discount configs from a template venue to all locations
3. View consolidated P&L, sales, and labor reports across all venues
4. Franchise reporting with per-location royalty calculations

</details>

---

### Accounting & Ledger

Journal entries, general ledger, and banking integration. QuickBooks and Xero auto-sync at EOD.

![Accounting](../images/pos/ipad_accounting.png)

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/accounting` for the main accounting dashboard
2. `/pos/accounting/ledger` for journal entries and GL
3. `/pos/accounting/banking` for bank feed integration
4. Configure QuickBooks or Xero sync in **Settings > Integrations** — GL journal auto-exports at end of day

</details>

---

### Coursing

Multi-course meal sequencing with per-item course assignment and fire-on-demand.

![Coursing](../images/pos/ipad_coursing.png)

<details>
<summary><strong>Setup</strong></summary>

1. Assign course numbers (1–6) to each item in the order ticket
2. Course 0 = fire immediately. Courses 1–6 fire in sequence when the server taps "Fire Next Course"
3. KDS shows course badges on each ticket item

</details>

---

### Order Throttling

Rate-limit incoming online orders during peak times to prevent kitchen overwhelm.

![Throttling](../images/pos/ipad_throttling.png)

<details>
<summary><strong>Setup</strong></summary>

1. Configure throttle limits in **Settings > Online Ordering**
2. Set max orders per 15-minute window
3. When the limit is reached, new customers see "We're busy — try again in a few minutes"

</details>

---

### HR & Timesheets

Leave management, timesheet review, and employee document tracking.

![HR](../images/pos/ipad_hr_timesheets.png)

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/hr` for timesheet review and leave management
2. Staff submit time-off requests; managers approve/deny
3. Timesheets auto-populate from clock-in/out records
4. Export to payroll (Gusto/ADP) from the Payroll page

</details>

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

![Offline](../images/pos/ipad_offline_mode.png)

</details>

<details>
<summary><strong>Integrations</strong></summary>

Stripe, DoorDash Drive, Uber Direct, Uber Eats, Grubhub, QuickBooks, Xero, Gusto, ADP, OpenTable, Google Reserve, Yelp, Twilio, SendGrid, Forage (EBT), Ollama (local AI).

![Integrations](../images/pos/settings_integrations.png)

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

![Marketing](../images/pos/settings_marketing.png)

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

## 25 languages

English, Spanish, French, Chinese, Arabic, Romanian, Portuguese, German, Italian, Japanese, Korean, Vietnamese, Russian, Ukrainian, Polish, Turkish, Dutch, Swedish, Hebrew, Thai, Hindi, Indonesian, Malay, Filipino, Greek. RTL supported.

---

<details>
<summary><strong>Developer: Integration Setup Guide</strong></summary>

Every integration activates by adding credentials in **Settings > Integrations**. No code changes needed.

| Integration | Env var | What activates |
|---|---|---|
| **Stripe** (card payments) | `STRIPE_SECRET_KEY` | Card tap/chip/swipe, Tap-to-Pay on iPhone, online payments |
| **DoorDash Drive** (delivery dispatch) | `DOORDASH_DEVELOPER_ID`, `DOORDASH_KEY_ID`, `DOORDASH_SIGNING_SECRET` | 3PD delivery delegation, menu sync |
| **Uber Direct** (delivery dispatch) | `UBER_CLIENT_ID`, `UBER_CLIENT_SECRET` | 3PD delivery delegation, menu sync |
| **DoorDash / Uber Eats / Grubhub** (marketplace) | Webhook URL | Inbound 3PD orders on KDS with purple badge |
| **SendGrid** (email) | `SENDGRID_API_KEY` | Email receipts, order confirmations |
| **Twilio** (SMS) | `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` | SMS receipts, order-ready notifications |
| **Google Reserve / OpenTable / Yelp** | Webhook URL | Auto-created reservations |
| **QuickBooks / Xero** | `QUICKBOOKS_ACCESS_TOKEN` or `XERO_ACCESS_TOKEN` | EOD GL journal auto-sync |
| **Forage** (EBT/SNAP) | `FORAGE_API_KEY` | EBT payment, eligible item flagging |
| **Dwolla / Stripe Treasury** | `DWOLLA_API_KEY` or `STRIPE_TREASURY_KEY` | ACH payroll direct deposit |
| **Ollama** (local AI) | `NEXT_PUBLIC_LOCAL_LLM_URL` | Natural language order parsing (local, no cloud) |
| **Prism MCP** (AI memory) | `PRISM_MCP_URL` | Per-staff and per-customer AI memory and context |
| **Apple / Google Wallet** | Pass Type ID + signing cert | Loyalty "Add to Wallet" |
| **Zebra / Brother** (labels) | Printer IP in Settings | ZPL price/SKU/prep labels |

**Required env vars:** `NEXT_PUBLIC_POS_SUPABASE_URL`, `NEXT_PUBLIC_POS_SUPABASE_ANON_KEY`, `POS_SUPABASE_SERVICE_ROLE_KEY`

</details>

<details>
<summary><strong>Developer: E2E Workflow & Role Testing</strong></summary>

![E2E Workflow](../images/pos/ipad_00_e2e_workflow.svg)
![Combined Role Tests](../images/pos/ipad_00c_combined_roles.svg)

</details>

---

## License

BUSL-1.1 — see [`LICENSE`](../LICENSE).
