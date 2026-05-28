# Synalux POS

**The restaurant POS that doesn't nickel-and-dime you.**

Every feature included. No add-on fees. No hardware lock-in. No multi-year contracts.
Use your own iPad — or any device with a browser.

<p align="center">
  <a href="https://synalux.ai/pos"><img src="https://img.shields.io/badge/Try_It-Free_Forever-43e97b?style=for-the-badge" alt="Try Free"></a>
  <a href="https://synalux.ai/pos/pricing"><img src="https://img.shields.io/badge/Pro-$49/mo_(14_day_trial)-764ba2?style=for-the-badge" alt="Pricing"></a>
  <a href="https://synalux.ai/pos/demo"><img src="https://img.shields.io/badge/Live_Demo-blue?style=for-the-badge" alt="Demo"></a>
</p>

---

## At a glance

| Register | Tables | KDS | Payment |
|:--------:|:------:|:---:|:-------:|
| ![Register](../images/pos/ipad_01_register.svg) | ![Tables](../images/pos/ipad_02_tables.svg) | ![KDS](../images/pos/ipad_03_kds.svg) | ![Payment](../images/pos/ipad_05_payment.svg) |

| Reports | Online Ordering | Customer Display | Manager Mobile |
|:-------:|:---------------:|:----------------:|:--------------:|
| ![Reports](../images/pos/ipad_reports.svg) | ![Online](../images/pos/online_01_menu.svg) | ![Display](../images/pos/ipad_customer_display.svg) | ![Mobile](../images/pos/iphone_01_dashboard.svg) |

---

## Why switch?

Your current POS costs too much. Toast charges $400–600/mo for a full setup. Square hits $250–350/mo. Clover locks you into 3-year contracts with $2,000+ hardware.

**Synalux: Free forever for 1 terminal. $49/mo Pro with 14-day free trial. Your own iPad. Cancel anytime.**

---

## Features

### Register

![Register](../images/pos/ipad_01_register.svg)

3-panel layout: categories on the left, product grid in the center, order ticket on the right. Tap items to add. Modifiers pop up when required. Seat assignment, course firing, barcode scanning, open-price entry, weight-based pricing — all built in.

<details>
<summary><strong>Setup guide + details</strong></summary>

**How to set up:**
1. Go to **Settings > Menu Builder** to add categories and items
2. Set prices, KDS stations, and modifier groups per item
3. Items appear on the register automatically
4. Assign barcodes in the menu builder for scan-to-add support

**Features:**
- 4 order types: Dine-in, Takeout, Delivery, Bar Tab — switchable before sending to kitchen
- Seat number assignment (S1–S8) for split-by-seat payments
- Age verification prompt for alcohol items
- Open-price items with floor/ceiling limits
- Weight-based items with scale input and price-per-unit calculation
- Barcode scanner support (USB HID keyboard input — any scanner works)
- Discounts selectable from the order panel (RBAC-gated)
- Auto-gratuity for large parties (configurable threshold + rate)
- Tax-exempt toggle per order

</details>

---

### Tables & Floor Plan

![Tables](../images/pos/ipad_02_tables.svg)

Visual floor plan with positioned table widgets. Color-coded by status. Click a table to start or view its order.

<details>
<summary><strong>Setup guide + details</strong></summary>

**How to set up:**
1. Go to **Settings > Floor Plan**
2. Click **+ Add Table** — set name, section, capacity, shape
3. Create sections (Main, Patio, Bar) for quick filtering

**Features:**
- Table merge, split-back, transfer, reopen closed check
- QR table ordering: copy QR link per table, print as table tent
- Real-time status updates via Supabase Realtime

![Table Merge](../images/pos/ipad_table_merge.svg)
![Seat Management](../images/pos/ipad_seat_management.svg)

</details>

---

### Kitchen Display (KDS)

![KDS](../images/pos/ipad_03_kds.svg)

4-column ticket board. Color-coded timing. Bump, recall, void. All-day count shows total pending per item.

<details>
<summary><strong>Setup guide + details</strong></summary>

**How to set up:**
1. Open `/pos/kds` on any tablet or TV
2. Filter by station (Grill, Fry, Prep, Expo, Bar, Cold)
3. Configure routing rules in **Settings > Printers & KDS**

**Features:**
- Tickets color-coded by order type: blue (dine-in), orange (takeout), purple (delivery)
- All-day count: toggle to see total pending per item
- Void button removes ticket and marks items voided
- Bump bar support (USB HID physical buttons)

</details>

---

### Payment

![Payment](../images/pos/ipad_05_payment.svg)

6 payment methods. Tip selection. Cash discount. Split check. Post-payment tip via QR.

<details>
<summary><strong>Setup guide + details</strong></summary>

**How to set up:**
1. **Card**: Add `STRIPE_SECRET_KEY` in Vercel settings. Pair Stripe Reader M2 ($59).
2. **Gift cards**: Issue from the Gift Cards page.
3. **House accounts**: Create in House Accounts page.

**Payment methods:**
- **Card** — Stripe Terminal (NFC/chip/swipe)
- **Cash** — tender amounts, change calculation, CAD penny rounding
- **Gift Card** — enter code, validate, deduct
- **House Account** — select account, charge to balance
- **Split Check** — even (2–12 ways) or custom amounts
- **Bar Tab** — pre-auth hold, add items, close later

**After payment:** Print, email (SendGrid), SMS (Twilio), or skip receipt. Post-payment tip page via QR.

![Split Check](../images/pos/ipad_split_check.svg)
![Post-Payment Tip](../images/pos/ipad_post_payment_tip.svg)

</details>

---

### Reports

![Reports](../images/pos/ipad_reports.svg)

8 report tabs. CSV export on every report.

<details>
<summary><strong>Details</strong></summary>

1. **Sales** — net/gross, discounts, hourly heatmap
2. **PMIX** — product mix: qty, revenue, % of sales
3. **Menu Engineering** — Star/Dog/Puzzle/Workhorse quadrant
4. **Speed of Service** — avg kitchen time per station
5. **Server Performance** — leaderboard with tips + avg ticket
6. **Payments** — cash/card/gift mix
7. **Voids/Comps** — voided and comped items
8. **Labor** — hours, shifts, overtime

Training orders excluded automatically.

![Menu Engineering](../images/pos/settings_menu_engineering.svg)

</details>

---

### Staff & Labor

![Employees](../images/pos/settings_employees.svg)

PIN auth. 7-level RBAC. Clock in/out. Break tracking. Scheduling with predictive alerts. Tip pooling. Payroll.

<details>
<summary><strong>Setup guide + details</strong></summary>

**How to set up:**
1. **Settings > Staff Management** — add employees with name, PIN, role
2. Roles: cashier, host, server, bartender, supervisor, manager, admin

**Features:**
- Break tracking (meal 30m unpaid, rest 10m paid — CA §226.7)
- Scheduling with overtime/clopening/minor labor alerts
- Tip pooling (3 modes: by hours, percentage, points)
- Payroll: regular/OT hours, tip credit (FLSA §3m), IRS Form 8027, CSV export

![Scheduling](../images/pos/settings_scheduling.svg)
![Tip Pooling](../images/pos/settings_tip_pooling.svg)
![Payroll](../images/pos/settings_payroll.svg)

</details>

---

### Online Ordering & QR Table

![Online](../images/pos/online_01_menu.svg)

Customer-facing menu. No app install. Orders go to KDS.

<details>
<summary><strong>Setup guide</strong></summary>

- **Online ordering**: Share `/pos/order` link. Customers browse, add to cart, checkout.
- **QR table ordering**: Copy QR link from Settings > Floor Plan per table. Print as table tent. Guest scans → orders → KDS.

![QR Ordering](../images/pos/ipad_qr_ordering.svg)

</details>

---

### Inventory & Recipes

![Inventory](../images/pos/settings_inventory.svg)

Stock tracking, cost per unit, stocktake mode, low-stock alerts, vendor management, recipe builder with food cost %.

<details>
<summary><strong>Setup guide + details</strong></summary>

- Add items: name, SKU, qty, unit, threshold, cost
- **Stocktake mode**: enter actual counts, bulk save
- **Recipes**: select menu item → add ingredients from inventory → food cost % auto-calculates
- **Vendors**: name, contact, payment terms (Net 30, COD, etc.)

![Recipes](../images/pos/settings_recipes.svg)
![Vendors](../images/pos/settings_vendors.svg)

</details>

---

### Gift Cards & Loyalty

![Gift Cards](../images/pos/settings_gift_cards.svg)

Issue/reload/deactivate gift cards. Loyalty with points, tiers, referrals.

<details>
<summary><strong>Details</strong></summary>

- **Gift cards**: Issue ($25–$250), auto-generated 16-char code, redeem at payment
- **Loyalty**: Enroll, check-in (+10 pts), auto-tier (Bronze/Silver/Gold), add/redeem points
- **Referrals**: 100 pts to referrer, 50 pts to new member

![Loyalty](../images/pos/settings_loyalty.svg)
![Loyalty Check-in](../images/pos/ipad_loyalty_checkin.svg)

</details>

---

### Compliance

![RBS Compliance](../images/pos/settings_rbs_compliance.svg)

Age verification, alcohol incidents, RBS tracking, audit trail, tax-exempt, CCPA/GDPR, IRS 8027.

<details>
<summary><strong>Details</strong></summary>

- Alcohol items trigger age verification modal
- RBS cert tracking with 30-day expiry alerts
- Incident logging (refusal, ID check, cutoff)
- Tax-exempt toggle per order
- CCPA/GDPR data deletion API
- Full audit trail

![Age Verification](../images/pos/ipad_age_verification.svg)
![Tax Exempt](../images/pos/settings_tax_exempt.svg)

</details>

---

### End of Day

![EOD](../images/pos/ipad_eod.svg)

Denomination count, cash management, tip pool, GL journal export, close register.

<details>
<summary><strong>Workflow</strong></summary>

1. Count cash by denomination
2. Record paid-in/paid-out
3. Review over/short variance
4. Distribute tip pool
5. Export GL journal (CSV for QuickBooks/Xero)
6. Print Z-Report
7. Close register

</details>

---

### More features

<details>
<summary><strong>Drive-Thru</strong></summary>

![Drive-Thru](../images/pos/ipad_drive_thru.svg)

Lane management with status advancement. Auto-refresh.

</details>

<details>
<summary><strong>Handheld Server</strong></summary>

![Handheld](../images/pos/ipad_handheld_ordering.svg)

Tableside ordering on any iPhone.

</details>

<details>
<summary><strong>Customer Display</strong></summary>

![Customer Display](../images/pos/ipad_customer_display.svg)

Live order + idle mode with promos. Any tablet/TV.

</details>

<details>
<summary><strong>Refunds</strong></summary>

![Refund](../images/pos/ipad_refund.svg)

Partial/full refund with reason codes. Reopen closed checks.

</details>

<details>
<summary><strong>Multi-Location</strong></summary>

![Multi-Location](../images/pos/settings_multi_location.svg)

Per-venue KPIs, consolidated P&L, venue switcher.

</details>

<details>
<summary><strong>Training Mode</strong></summary>

![Training](../images/pos/settings_training_mode.svg)

Isolated simulation. Orders excluded from reports.

</details>

<details>
<summary><strong>Offline Mode</strong></summary>

![Offline](../images/pos/ipad_offline_mode.svg)

Register, cash, KDS, receipts work offline. Auto-sync on reconnect.

</details>

<details>
<summary><strong>Integrations</strong></summary>

![Integrations](../images/pos/settings_integrations.svg)

Stripe, DoorDash, Uber Eats, Grubhub, QuickBooks, Xero, Gusto, ADP, OpenTable, Google Reserve, Yelp, Twilio, SendGrid.

</details>

<details>
<summary><strong>12 Operational Forms</strong></summary>

![Forms](../images/pos/settings_forms.svg)

Cash Count Sheet, Void Authorization, Tax-Exempt Certificate, Catering BEO, Server Tip Declaration, Inventory Count, Time-Off Request, Purchase Order, Incident Log, Daily Specials, Prep List, Server Checkout. Print or download.

</details>

---

## Plans & Pricing

**Free forever** for 1 terminal. **14-day free trial** on all paid plans. Billed via Stripe — cancel anytime.

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
| Multi-location + Franchise P&L | — | — | — | Yes |
| API access | — | — | — | Yes |
| **Contract** | **None** | **None** | **None** | **None** |
| **Billing** | **Free** | **Stripe** | **Stripe** | **Stripe** |

**Processing rates (via Stripe):**

| Transaction | Rate |
|-------------|------|
| In-person (tap/chip/swipe) | 2.6% + $0.10 |
| Online | 2.9% + $0.30 |
| Tap-to-Pay on iPhone | 2.6% + $0.10 |

**Hardware — Bring Your Own Device:**

| Item | Synalux | Toast | Square | Clover |
|------|--------:|------:|-------:|-------:|
| Terminal | **$0** (any iPad) | $799–999 | $299 | $1,399–1,899 |
| Handheld | **$0** (any iPhone) | $409–627 | $399 | $499–749 |
| KDS | **$0** (any tablet/TV) | $499–699 | $300–900 | $300–900 |
| Card reader | **$59** (Stripe Reader) | $249–299 | $59 | Included |
| **Total** | **$59** | **$1,500–2,500+** | **$600–1,200** | **$2,000–4,000+** |

**No contract. No early termination fee. No hidden fees. Cancel anytime from your Stripe billing portal.**

---

## First-year savings

| vs Competitor | Their Cost | Synalux Pro | **You Save** |
|---------------|-------------------------------------------:|--------:|-------------:|
| vs Toast | $4,800–7,200/yr + $1,500 HW | $588/yr + $59 HW | **$5,700–8,100** |
| vs Square | $3,000–4,200/yr + $600 HW | $588/yr + $59 HW | **$3,000–4,200** |
| vs Clover | $4,200–6,000/yr + $2,000 HW | $588/yr + $59 HW | **$5,600–7,700** |
| vs TouchBistro | $6,000–9,600/yr + HW | $588/yr + $59 HW | **$6,400–10,000** |
| vs Lightspeed | $5,400–7,200/yr + $800 HW | $588/yr + $59 HW | **$5,600–7,700** |

---

## 25 languages

English, Spanish, French, Chinese, Arabic, Romanian, Portuguese, German, Italian, Japanese, Korean, Vietnamese, Russian, Ukrainian, Polish, Turkish, Dutch, Swedish, Hebrew, Thai, Hindi, Indonesian, Malay, Filipino, Greek. RTL supported.

---

## License

BUSL-1.1 — see [`LICENSE`](LICENSE).
