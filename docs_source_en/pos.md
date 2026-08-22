# Synalux POS

**Restaurant POS for browser-based register, kitchen, payment, and venue operations.**

Synalux POS connects front-of-house, kitchen, ordering, payment, and back-office workflows in one browser-based system for compatible tablets and computers. Configure the experience by venue, revenue center, station, staff role, and screen layout.

<p align="center">
  <img src="https://img.shields.io/badge/26_Languages-RTL_Supported-blue?style=for-the-badge" alt="26 Languages">
</p>

🌐 **Interface languages:** Synalux POS includes 26 interface locales, including Bulgarian and right-to-left Arabic and Hebrew. See [26 languages](#26-languages).

## Register at a glance

The Register keeps the menu, order ticket, totals, and service actions together so staff can build and route an order without leaving the screen. Its presentation adapts to the available width instead of squeezing the desktop workspace onto a smaller device.

**Desktop register — 1920 × 1080**

<img src="../images/pos/production-demo-2026-08/prod-20260822-register-desktop.png" alt="Desktop Synalux POS Register with the full order panel on the left, five menu columns, the menu and open-orders panel on the right, and persistent actions across the bottom">

On a wide desktop, the check stays open on the left while the menu and open-order switcher remain visible on the right.

**Tablet register — 820 × 1180**

<p align="center">
  <img src="../images/pos/production-demo-2026-08/prod-20260822-register-tablet.png" width="640" alt="Tablet Synalux POS Register with five proportionate menu columns and a View Order action above the bottom navigation">
</p>

**Phone check view — 390 × 844**

<p align="center">
  <img src="../images/pos/production-demo-2026-08/prod-20260822-register-phone-order.png" width="390" alt="Phone Synalux POS order view with Back to Menu, Cheesecake line item, tax, total, Send to Kitchen, and Pay actions">
</p>

On tablet and phone layouts, **View Order** opens the check without compressing the menu into the desktop panel arrangement. The phone example shows the resulting order view with the item, tax, total, send, and payment path visible.

- Ring configured dine-in, takeout, delivery, drive-thru, bar-tab, and catering orders.
- Search the menu, select modifiers, add open-price items, and apply permitted comps or discounts.
- Keep the customer reference, line items, tax, total, and order state visible while building the check.
- Send items to the kitchen and continue through the payment workflow.

See the [detailed Register workflow](#register) for setup, menu tools, order controls, and service behavior.

## Why Synalux POS

- **One connected service flow:** Follow an order from Register through tables and seats, KDS and expo, and payment in the Synalux POS workspace.
- **Venue-specific control:** Configure revenue centers, stations, price levels, staff roles, and screen layouts around each service model.
- **Multiple ordering channels:** Manage in-venue, online, QR-table, delivery, phone, WhatsApp, catering, drive-thru, and handheld workflows from the same venue data.
- **Operational depth:** Bring labor, inventory, loyalty, house accounts, reporting, accounting, and end-of-day controls into the POS workspace.
- **International interface:** Use 26 interface locales, including right-to-left Arabic and Hebrew.

---

## Try the demo

**For customers (no login needed):**

| | |
|---|---|
| **Order Online (US)** | [pos.synalux.ai/pos/order](https://pos.synalux.ai/pos/order?v=00000000-0000-0000-0000-000000000100) |
| **Order Online (EU)** | [pos-eu.synalux.ai/pos/order](https://pos-eu.synalux.ai/pos/order?v=b6000000-0000-0000-0000-000000000002) |
| **Order by Phone (AI)** | Call **+1 (256) 787-0815** — say "switch to Spanish" or speak one of the supported voice languages for automatic detection |
| **Order via WhatsApp** | [<img src="https://img.shields.io/badge/WhatsApp-25D366?logo=whatsapp&logoColor=white&style=flat" alt="WhatsApp">](https://wa.me/14155238886?text=join%20bat-come) — tap to join, then text your order |

**For staff — POS login:**

| Region | URL | Credentials |
|---|---|---|
| **US** | [pos.synalux.ai/auth](https://pos.synalux.ai/auth) | `demo@synalux.ai` / `demo1234` |
| **EU** | [pos-eu.synalux.ai/auth](https://pos-eu.synalux.ai/auth) | `demobg@synalux.ai` / `demo1234` |

Then enter a staff PIN:

| Role | Name | PIN | Screens |
|---|---|---|---|
| **Cashier** | Cashier | `5555` | Register, Payment |
| **Host** | Host | `4444` | Tables, Waitlist, Reservations |
| **Server** | Server 1 | `1111` | Register, Tables, Payment, Handheld |
| **Server** | Server 2 | `2222` | Register, Tables, Payment, Handheld |
| **Bartender** | Bartender | `3333` | Bar Register, Payment, Age Verification |
| **Supervisor** | Supervisor | `9012` | Register, Tables, Reports, Voids, Discounts, KDS |
| **Manager** | Manager | `5678` | All screens + EOD + Staff |
| **Admin** | Admin | `1234` | All screens + Settings |

The public demo is pre-populated. The repository seed command is a maintainer tool for controlled demo environments; staff using the public demo do not need to run it. The credentials and PINs above are intentionally public demo access; create unique accounts, PINs, and role assignments for a production venue.

> **Screenshot policy:** The responsive Register screenshots above were captured from the US production demo on **August 22, 2026**. Other production-demo screenshots identify their capture date in the filename or caption. A screen is shown as current evidence only when it contains meaningful configured data and no visible error state; older workflow illustrations are being refreshed section by section.

---

## Customer setup and go-live path

Use this sequence for a new venue. Each step links to the detailed feature documentation and setup controls later in this guide.

1. **Sign in and confirm the venue.** Use the account and region supplied by Synalux or your venue administrator. Confirm the venue name, region, currency, and time zone before entering prices or tax rules.
2. **Configure venue basics.** In **Settings > Venue Settings**, review order types, table behavior, revenue centers, price levels, gratuity, cash handling, and the payment processor used by the venue.
3. **Create tax zones and revenue centers.** Confirm rates and taxable item types with the venue's accountant or tax adviser. Create separate revenue centers only for meaningful service differences such as dining room, bar, patio, counter, takeout, or delivery.
4. **Build the menu.** In **Settings > Menu Builder**, create categories, items, modifier sets, combos, availability schedules, kitchen routes, tax behavior, receipt names, allergens, and consistently framed item images.
5. **Add staff and permissions.** Create a unique PIN or supported credential for each employee, assign the least-privileged role needed, and test at least one account for every role used by the venue.
6. **Create and assign stations.** Configure each terminal's operational purpose, default revenue center, allowed roles, menu, and printer routing. Use device assignment when possible; use IP assignment only for managed networks that require it.
7. **Configure printers and kitchen routing.** Add receipt, kitchen, label, and KDS destinations. Test dine-in, takeout, modifier, void, refire, and multi-course examples used by the venue, and confirm each item arrives once at the correct destination.
8. **Configure payments, tips, gratuity, rounding, and receipts.** Review each enabled tender separately, including tip timing, cash-overpayment behavior, currency rounding, optional additional tip, auto-gratuity, receipt delivery, refund permissions, and processor-specific hardware.
9. **Choose screen layouts.** In **Settings > Screen Builder**, start from the closest service profile, then configure Register actions for dine-in, bar tab, quick service, takeout, and delivery. Keep frequent actions persistent, move secondary actions to **Actions**, and preserve at least one reachable payment path.
10. **Configure ordering channels.** Enable only the online, QR-table, phone, WhatsApp, delivery, catering, drive-thru, or handheld workflows the venue will operate. Verify hours, fulfillment rules, taxes, menu availability, and customer notifications for each enabled channel.
11. **Run a go-live rehearsal.** Test the complete path for every service mode: staff sign-in, order entry, modifiers, seats or customer reference, kitchen routing, payment, receipt, refund/void permissions, reporting, and end-of-day. A saved setting alone does not prove that a processor, printer, message, or third-party integration completed its external action.

Useful starting points: [Settings map](#settings-map), [Register](#register), [Tables](#tables--floor-plan), [KDS](#kitchen-display-kds), [Payment](#payment), [Screen Builder](#screen-builder), [Printers](#printers--cash-drawer), and [Security](#security--pci-compliance).

---

## Table of Contents

- **Start and configure:** [Customer setup and go-live path](#customer-setup-and-go-live-path), [Settings map](#settings-map), [staff authentication](#staff-login--authentication), [revenue centers](#revenue-centers), [stations](#per-station-configuration), [price levels](#price-levels), and [Screen Builder](#screen-builder).
- **Serve guests:** [Register](#register), [tables and floor plan](#tables--floor-plan), [seat management](#seat-management), [KDS](#kitchen-display-kds), [expo](#expo--order-management), and [payment](#payment).
- **Accept orders:** [Online and QR table](#online-ordering--qr-table), [delivery](#delivery-management), [AI chat](#ai-chat-assistant), [voice](#ai-voice-ordering-phone), [WhatsApp](#whatsapp-ordering), [catering](#catering), [drive-thru](#drive-thru), and [handheld](#handheld-server).
- **Operate the venue:** [Staff and labor](#staff--labor), [reports](#reports), [inventory](#inventory--recipe-costing), [gift cards and loyalty](#gift-cards--loyalty), [house accounts](#house-accounts), [compliance](#compliance), [end of day](#end-of-day), and [reservations](#reservations--waitlist).
- **Manage at scale:** [Refunds](#refunds), [multi-location](#multi-location--franchise), [accounting](#accounting--ledger), [coursing](#coursing--course-firing), [order throttling](#order-throttling), [HR and timesheets](#hr--timesheets), and [Back Office](#back-office-suite).
- **Platform and setup:** [Offline mode](#offline-mode-pwa), [integrations](#integrations), [printers and drawers](#printers--cash-drawer), [security](#security--pci-compliance), [26 languages](#26-languages), and the [developer guide](#developer-integration-setup-guide).

---

## Settings map

Open **Settings** from the top bar to reach the 16 linked administration areas. The landing page also shows the recent settings audit trail, including who changed a setting and when.

<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-hub.png" alt="Production demo Settings hub with linked administration areas and a populated recent audit trail">

| Settings area | Route | What it controls |
|---|---|---|
| Menu Builder | `/pos/settings/menu` | Categories, items, modifier sets, shared modifiers, combos, pricing, availability, KDS routing, barcodes, EBT flags, allergens, recipes, price levels, and CSV import/export |
| Staff Management | `/pos/settings/staff` | Staff records, roles, PINs, cards, QR badges, and passkeys |
| Role Permissions | `/pos/settings/roles` | Permission matrix for the seven staff roles |
| Tax Zones | `/pos/settings/tax` | Sales tax, VAT/GST jurisdictions, rates, and taxable item types |
| Discounts | `/pos/settings/discounts` | Percentage, fixed, BOGO, group, coupon, eligibility, stacking, and usage rules |
| Floor Plan | `/pos/settings/tables` | Rooms, tables, capacity, position, dimensions, rotation, and QR table codes |
| Printers & KDS | `/pos/settings/printers` | Receipt/kitchen/label printers, drawers, stations, and category routing |
| Screen Builder | `/pos/settings/screen-builder` | Venue layout profiles, 12 POS screens, register behavior, receipts, and responsive presentation variants |
| Stations | `/pos/settings/stations` | Terminal identity, device assignment, menus, printers, revenue centers, and role access |
| Venue Settings | `/pos/settings/venue` | Venue identity/time zone, processor, table occupancy, revenue centers, price levels, auto-gratuity, cash discount, over-payment behavior, blind drawer, sales tax on discounts, meal rules, and order types |
| Integrations | `/pos/settings/integrations` | Payment, ordering, accounting, calendar, drive, mail, messaging, and voice providers |
| Online Ordering | `/pos/settings/online-ordering` | Hours, pickup/delivery channels, minimums, prep times, zones, and closed dates |
| Void Reasons | `/pos/settings/void-reasons` | Active order/item void reasons and translations |
| Comp Reasons | `/pos/settings/comp-reasons` | Active item-comp reasons and translations |
| Account | `/pos/settings/account` | Account data export and deletion controls |
| Touch Diagnostic | `/pos/settings/touch-diagnostic` | Touchscreen detection and input diagnostics |

**Delivery Management** is also available directly at `/pos/settings/delivery`. It controls 3PD, in-house, and hybrid delivery modes plus provider selection and menu sync, but it is not currently a card on the Settings landing page.

---

## Features

<a name="staff-login--authentication"></a>

### Staff Login & Authentication

PIN login with clock-in, 7-level role-based access, and automatic screen routing per role. Four authentication methods — PIN is default, biometric and card are progressive enhancements.

<img src="../images/pos/ipad_pin_overlay.png" alt="PIN Numpad — Employee Login">
<img src="../images/pos/ipad_00_pin_entry.png" alt="Owner Sign In (email/password)">

<details>
<summary><strong>Authentication Methods</strong></summary>

| Method | How it works | Setup |
|---|---|---|
| **PIN** | 4-digit numeric code per staff member | Default — created on staff setup |
| **WebAuthn Passkeys** | Touch ID, Face ID, Windows Hello, hardware security keys | Settings > Staff > Register Passkey |
| **Swipe Card** | Magnetic stripe / RFID employee badges | Settings > Staff > Assign Card |
| **Manual Card Entry** | Keyed card-not-present transactions (admin override required) | Admin PIN + confirmation dialog |

WebAuthn passkeys use the Web Authentication API — credentials are device-bound and never leave the staff member's device. Multiple passkeys can be registered per staff member (e.g., both iPad Touch ID and phone Face ID). Falls back to PIN if biometric fails.

</details>

**Account sign-in and staff PIN are separate authorization layers.** Email/password signs the device into a venue account. A PIN then selects the on-duty staff identity for shared-terminal workflows. When someone opens Settings or another account-managed route, the POS verifies the signed-in account's venue membership and switches to that account's linked, active staff record; it never carries a cashier or server PIN identity into management as authority. If the account has no accessible venue or linked active staff record, management access stops with an account-access error.

**Sign Out is a staff handoff, not a venue-account logout.** It clears the active staff identity and returns the terminal to the PIN pad while retaining the venue account session, so the next employee can enter their own PIN without re-entering the venue email and password.

<details>
<summary><strong>Roles & Routing</strong></summary>

1. Add staff in **Settings > Staff Management** — name, PIN, role
2. Assign roles: cashier, host, server, bartender, supervisor, manager, admin
3. Multi-role staff see a role picker; single-role staff go straight to their screen

| Role | Landing Page | What you see |
|---|---|---|
| Admin | Settings | Settings + All screens |
| Manager | Register | All screens + EOD |
| Supervisor | Register | Register, Tables, KDS, EOD |
| Server | Register | Register + Tables + Handheld |
| Bartender | Register | Bar Register + Age Verification |
| Host | Tables | Tables + Reservations |
| Cashier | Register | Register only |

These rows are the standard terminal-role baseline, not an immutable list. **Settings > Role Permissions** can add or remove terminal routes for each venue, Revenue Center configuration can choose the post-login landing screen, and a station's **Allowed Roles** can restrict who may use that terminal. None of those terminal settings bypasses the separate account-membership check for Settings and other management routes.

<img src="../images/pos/ipad_00b_role_select.png" alt="Role Selection">
<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-staff.png" alt="Production demo Staff Management with populated employee records and credential controls">

</details>

---

### Revenue Centers

Revenue Centers control which menu categories appear, which KDS stations receive items, which discounts are eligible, and which price level applies — per service area.

<img src="../images/pos/ipad_settings_venue_rc.png" alt="Venue Settings — Revenue Centers">
<img src="../images/pos/ipad_settings_venue_rc_scroll.png" alt="Revenue Center Configuration">

<details>
<summary><strong>Setup</strong></summary>

1. Define RCs in **Settings > Venue Settings** (e.g., Main Dining, Bar, Patio, Takeout)
2. Configure per-RC in **Settings > Venue Settings > Revenue Centers**:
   - **Menu Categories** — which categories show when this RC is active
   - **KDS Routes** — remap station routing (e.g., Bar RC sends all items to bar station)
   - **Eligible Discounts** — restrict which discounts work in this RC
   - **Price Level** — default pricing for orders in this RC
   - **🏁 Landing Screen** — where staff land right after picking this RC: Floor Plan (pick a table first), Bar Tabs, Register, or Delivery Board. Table-service RCs typically land on the Floor Plan so servers choose their table before the order opens. Staff only land where their role has access.
3. Staff select their RC at login and are taken straight to that RC's workflow screen. Orders are automatically scoped.

</details>

---

### Per-Station Configuration

Named terminal configurations with independent menus, printers, and access controls. The bar terminal sees only drink categories, the hostess station sees only table service. **📍 Assign** — one tap per iPad binds the terminal to its station **by device**, and it auto-selects that station on every login and reload. The binding survives Wi-Fi changes, router reboots, and new DHCP leases — no station picker, no network configuration.

<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-stations.png" alt="Production demo Station Configuration with five named terminals and device assignment controls">

The active station shows next to the staff name in the top bar (e.g. **Alex M. · BAR POS**), so staff always know which terminal identity they're ringing on.

<details>
<summary><strong>Setup</strong></summary>

1. Go to **Settings > Stations > Add Station**
2. Set **Name** ("Bar POS", "Hostess", "Drive-Thru 1")
3. Assign **Menu Categories** — only these categories appear on this terminal
4. Assign **Printers** — this station sends tickets to specific printers
5. Set **Default Revenue Center** — auto-selects RC when staff logs in
6. Set **Allowed Roles** — restrict which staff roles can use this station
7. Set **Allowed Revenue Centers** — restrict which RCs are available

**One-tap device assignment:**

1. Walk to the bar iPad → open **Settings > Stations**
2. Tap **📍 Assign** on "Bar POS" → this iPad is now bound to that station, marked with a **📍 This device** badge (stations bound to other terminals show **🔒 Other device**)
3. On every future login, this iPad auto-selects Bar POS — no station picker, no manual steps
4. Repeat for each device: dining iPad → "All Access", takeout iPad → "Takeout"
5. **📍 Unassign** releases the binding; if a device has no assignment, the station picker appears at login

**First-login claim:** on an unassigned terminal, the station picker after PIN entry claims the chosen station for that device — same effect as Assign in Settings. Stations already claimed by another terminal show "In Use"; managers can override to move a station to a new device.

<img src="../images/pos/station_picker_claim.png" alt="Station Picker — claiming a station on first login, with In Use lock and manager override">

**IP Auto-Assign (legacy fallback):** the section at the bottom maps device IPs to stations for terminals that were never device-assigned. Prefer 📍 Assign — IP matching depends on the network exposing a stable local IP, which modern browsers increasingly hide. Existing rules keep working; `*` acts as a default for unmatched devices and IP prefixes (e.g. `192.168.1.`) match whole subnets.

</details>

---

### Price Levels

Up to 14 price levels per item with automatic day/time scheduling. Happy hour, employee, VIP pricing — all server-side.

<img src="../images/pos/settings_price_levels.png" alt="Price Level Settings">

<details>
<summary><strong>Setup</strong></summary>

1. Define levels in **Settings > Venue Settings > Price Levels** with name + multiplier
2. Set **Schedule** for auto-switching: `{days: ["mon","tue","wed","thu","fri"], start: "16:00", end: "18:00"}`
3. **Overnight windows** work: `{start: "22:00", end: "02:00"}`
4. Per-item overrides in **Menu Builder > Item > Price Levels** (exact price per level)
5. **Price cascade:** Station price level → RC price level → Schedule → Base price
6. Manual override requires `change_price_level` role (manager+)

</details>

---

### Register

Ring orders in seconds. Categories, product grid, and order ticket — all on one screen. Cart auto-scrolls as items are added. Open Price button creates custom-priced items with a description field. Send to Kitchen button reappears after adding new items to a submitted order.

**Customer Name / Order Reference** — every order has a Customer Name field in the order panel. Type a guest name for takeout tickets, bar tabs, or dine-in. The name prints on receipts and appears on KDS tickets.

<img src="../images/pos/ipad_customer_name.png" alt="Customer Name on Takeout Order">

**Item Search** — tap the search icon on the register to search the full menu in real time (2-character minimum). Finds items across all categories instantly — no scrolling needed.

<img src="../images/pos/ipad_item_search.png" alt="Item Search">

**Custom order types** — choose which order types appear on the register (dine-in, takeout, delivery, drive-thru, bar tab, catering) and give them custom labels (e.g. show *drive-thru* as "Curbside") in **Settings > Venue > Order Types**.

<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-venue.png" alt="Production demo Venue Settings with configured dine-in, takeout, delivery, and bar-tab order types">

**Comp an item** — comp a line item with a configurable reason. Manage the reason list in **Settings > Comp Reasons**; when comping, staff pick a reason (or free-text) so comps are itemized by cause in the Comps report.

<p>
  <img src="../images/pos/production-demo-2026-08/prod-20260810-settings-void-reasons.png" alt="Production demo Void Reasons with ten active translated reasons" width="49%">
  <img src="../images/pos/production-demo-2026-08/prod-20260810-settings-comp-reasons.png" alt="Production demo Comp Reasons with seven active translated reasons" width="49%">
</p>

<details>
<summary><strong>Setup</strong></summary>

1. **Settings > Menu Builder** — add categories and items with **Item Type** (Food/Alcohol/Beverage/Merchandise), **EBT/SNAP eligibility**, and **KDS Station** (Grill/Fry/Prep/Expo/Bar/Cold/Pass) dropdowns
2. Set prices, modifiers, KDS stations, and barcodes per item
3. **Per-item price level overrides** — set custom prices for Employee, Happy Hour, VIP levels in the item edit form. **Happy-hour pricing applies to online and phone orders too** — the customer is charged the same happy-hour price they see
4. **Combos** — build meal deals in the Combos tab. A component can be a specific item **or a category slot** ("any item from Sides"), each with its own **quantity** (e.g. Burger + any Side ×2 + any Drink for $10). Combo savings apply on the register and on online/phone/AI orders alike
5. Items appear on the register automatically

<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-menu.png" alt="Production demo Menu Builder with 39 configured items, categories, modifiers, combos, and CSV controls">
<img src="../images/pos/ipad_barcode_scan.png" alt="Barcode Scan">
<img src="../images/pos/ipad_allergen_filter.png" alt="Allergen Filter">
<img src="../images/pos/settings_auto_gratuity.png" alt="Auto Gratuity">
<img src="../images/pos/settings_combos.png" alt="Combos">
<img src="../images/pos/settings_discounts.png" alt="Discounts">
<img src="../images/pos/settings_menu_scheduling.png" alt="Menu Scheduling">
<img src="../images/pos/settings_nutritional.png" alt="Nutritional Info">
<img src="../images/pos/settings_price_levels.png" alt="Price Levels">

</details>

<details>
<summary><strong>Import & export your menu (CSV)</strong></summary>

**Settings > Menu Builder** has **Export CSV** and **Import CSV** buttons. The quickest way to start is to export first — the file you get back is exactly the format import expects, so you can edit it in Excel or Google Sheets and import it again.

The first row must be a header row. Column order does not matter and header names are not case-sensitive. **`name` and `price` are required**; every other column is optional and may be left out entirely.

| Column | Required | What to put in it |
|--------|----------|-------------------|
| `name` | **Yes** | Item name, up to 200 characters |
| `price` | **Yes** | Price in dollars, e.g. `14.50` |
| `category` | No | Name of an existing category, e.g. `Appetizers` |
| `type` | No | `food`, `beverage`, `alcohol`, or `merchandise`. Defaults to `food` |
| `barcode` | No | Barcode for scanning at the register |
| `available` | No | `no` marks the item unavailable. Anything else means available |
| `calories` | No | Whole number |
| `allergens` | No | Separate multiple allergens with **semicolons**: `nuts;dairy` |

Example:

```csv
name,price,category,type,available,allergens
Caesar Salad,8.00,Appetizers,food,yes,dairy;gluten
House Red,11.50,Drinks,alcohol,yes,
Cheesecake,7.00,Desserts,food,no,dairy;eggs;gluten
```

What to expect on import:

- **Import only adds new items — it never changes existing ones.** If an item with the same name already exists in the same category, that row is skipped and the item is left exactly as it is. Editing a price in the CSV and re-importing will **not** update the item; change prices in the Menu Builder instead. The upside is that re-running the same file is always safe and never creates duplicates
- **Categories are matched, never created.** A category name that does not already exist is reported back in the summary and the item is imported without a category. Create your categories first
- **Bad rows are skipped, not fatal.** A row missing a name or with an unreadable price is counted and reported; the rest of the file still imports
- After importing, the summary tells you how many items were imported, skipped as duplicates, skipped as invalid, and how many category names went unmatched
- Up to **5,000 rows** per file
- Newly imported items without photos can be filled in from the Menu Images manager — see [AI Dish Image Generation](#ai-dish-image-generation)

Values containing a comma, quote, or line break should be wrapped in double quotes, the same as any spreadsheet export.

</details>

---

<a name="tables--floor-plan"></a>

### Tables & Floor Plan

Visual floor plan with color-coded table status, multiple rooms, and resizable/rotatable tables. Table state syncs across every terminal in real time — no manual refresh.

<img src="../images/pos/production-demo-2026-08/prod-20260810-tables.png" alt="Production demo Floor Plan with 28 tables and active long-wait checks">

<details>
<summary><strong>Setup</strong></summary>

1. **Settings > Floor Plan** — add tables with name, section, capacity, shape, **size (width/height), and rotation**. Drag to position, resize, and rotate each table to match the real room
2. **Multiple rooms** — group tables by section (Main, Patio, Bar) into separate rooms; a room switcher draws one room at a time in both the designer and the live floor view
3. **Change Table** — move an order to a different table from the order panel. Pick the new table from the floor plan
4. **Move seats between orders** — transfer individual seat groups from one table's order to another
5. Merge, split-back, transfer, or reopen closed checks from the table detail panel
6. **Occupy-on-add** — adding items to a table opens its check immediately, so the table shows **occupied on every terminal** in real time, before "Send to Kitchen." Toggle in **Settings > Venue > Table Occupancy** (on by default); turn it off to only occupy the table once the order is fired
7. **Live status** — available / occupied / long-wait syncs across all terminals instantly, with no manual refresh
8. **Mark Clean** — after a table is vacated, tap **Mark Clean** to flip it back to available (records a bussed timestamp so a fired order is never mistaken for a new one)

<img src="../images/pos/settings_occupy_on_add.png" alt="Occupy table when items are added">
<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-floor-plan.png" alt="Production demo Floor Plan settings with populated table capacities and layout controls">
<img src="../images/pos/ipad_table_merge.png" alt="Table Merge">
<img src="../images/pos/production-demo-2026-08/prod-20260810-table-operations.png" alt="Production demo Table Operations with seven active table orders">

</details>

---

### Seat Management

Assign items to individual seats for split checks and per-guest delivery. Seat tabs on the register let servers ring items per guest. Split a single item across all seated guests — price is distributed evenly.

<img src="../images/pos/ipad_seat_management.png" alt="Seat Management">

<details>
<summary><strong>Setup</strong></summary>

1. Tap **Seat 1 / Seat 2 / + Seat** tabs on the register to assign items to specific guests
2. Tap the **⋯** menu on any line item, then **Move to Seat**, to assign or change which guest it belongs to (the item shows a colored seat chip)
3. **Split item across guests** — open a line item's **⋯** menu → **Move to Seat**, then tap "Split across all (N)." The item is cloned into one line per seat with the price distributed evenly (remainder goes to seat 1). Modifier prices are also split
4. Split check by seat — each guest gets their own bill with only their items
5. Seat assignment works alongside courses — assign items to Seat 1/2/3 and Course 1/2/3 independently

</details>

---

### Kitchen Display (KDS)

Ticket board with color-coded timing (green → yellow → orange → red). Bump, recall, void. All-day count per item. 8 station types: Kitchen, Grill, Fry, Prep, Expo, Bar, Cold, Pass.

<img src="../images/pos/production-demo-2026-08/prod-20260810-kds.png" alt="Production demo KDS with two active kitchen tickets and station filters">

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/kds` on any tablet or TV
2. Filter by station: ALL, Grill, Fry, Prep, Expo, Bar, Cold, Pass
3. Configure routing rules in **Settings > Printers & KDS**
4. **Timed Course Fire** — set `prep_time_minutes` per menu item. Items split by course; later courses auto-fire offset by the longest prep time so everything finishes together
5. **Modifier Steering** — modifiers can redirect items to additional stations. Set "Steer to Station" on any modifier option in Menu Builder. Steering is additive: item goes to default AND modifier station
6. **Voids reflect on fired tickets** — voiding an item after it's fired marks it struck-through with a **VOID** badge on the kitchen ticket, so the line the kitchen already sees is cancelled instead of leaving a phantom item to be made

</details>

---

<a name="expo--order-management"></a>

### Expo & Order Management

The KDS is only one part of the live order workflow:

- **Expo** (`/pos/expo`) collects completed kitchen work for final handoff and lets staff mark ready orders complete.
- **Orders** (`/pos/orders`) is the searchable order ledger for open and completed checks, totals, staff, and tender context.
- **Table Operations** (`/pos/table-ops`) centralizes active table checks for transfers, merges, split-backs, and reopen workflows.
- **Scheduled Orders** (`/pos/scheduled`) lists future orders when the venue has scheduled demand. An empty scheduled-order queue is intentionally not illustrated.

<img src="../images/pos/production-demo-2026-08/prod-20260810-expo.png" alt="Production demo Expo board with five ready orders">
<img src="../images/pos/production-demo-2026-08/prod-20260810-orders.png" alt="Production demo Orders ledger with eight populated order rows and totals">
<img src="../images/pos/production-demo-2026-08/prod-20260810-table-operations.png" alt="Production demo Table Operations showing seven active orders on tables">

---

### Timed Course Fire

Automatic kitchen ticket timing — items in a course fire based on prep time so everything lands on the expo at the same time. Course numbers are assigned at the register; KDS hides future-course tickets until their fire time.

<img src="../images/pos/production-demo-2026-08/prod-20260810-kds.png" alt="Production demo KDS where fired course tickets appear for kitchen action">

<details>
<summary><strong>How it works</strong></summary>

1. Set **prep_time_minutes** on each menu item in **Settings > Menu Builder**
2. Assign **Course 1 / 2 / 3** to items in the cart during order entry
3. Course 1 fires immediately. Course 2 fires after Course 1's longest prep time elapses
4. Within a course, faster items are delayed — a 5-min soup waits 13 minutes so it finishes with the 18-min steak
5. KDS hides future-dated tickets until their fire time passes
6. Online, voice, and WhatsApp orders receive **estimated_ready_at** computed from the longest prep item

</details>

---

### Modifier-Based KDS Steering

Modifiers can redirect parent items to additional kitchen stations (additive routing). Example: a "Grilled Shrimp" modifier on a burger sends the burger to both Prep AND Grill stations.

<img src="../images/pos/settings_modifier_steering.png" alt="Modifier KDS Steering — Grilled Shrimp routes to Grill, Side Salad routes to Cold">

<details>
<summary><strong>Setup</strong></summary>

1. Open **Settings > Menu Builder > Modifiers tab**
2. Click **Edit** on any modifier option to open the inline edit form
3. Set **KDS Steer** dropdown on any modifier option (e.g., "Grilled Shrimp" → Grill)
3. Toggle **Follow Item** to control whether modifier text appears on the steered ticket
4. Steering is **additive** — the item goes to its default station AND the modifier's station
5. Multiple modifiers can steer to different stations — dedup prevents duplicates

</details>

---

### Payment

Card, cash, gift card, mobile pay, house account, bar tabs, and cash discount/dual pricing. EBT/SNAP and Tap-to-Pay on iPhone are in implementation. Split check, tips, and post-payment tip via QR.

<img src="../images/pos/ipad_05_payment.png" alt="Payment">

<details>
<summary><strong>Setup</strong></summary>

1. **Card** — configure Stripe server-side, select Stripe as the venue processor, set the Terminal Location, then pair a supported reader from **Settings > Integrations**
2. **Tap-to-Pay on iPhone** — requires the Synalux POS iPhone app, Stripe as the venue processor, a supported signed build/device, a Stripe Terminal Location, and Stripe Tap to Pay availability. When the native capability check passes, tap **Tap to Pay on iPhone** on the payment screen; otherwise that tender stays hidden rather than presenting an unusable button
3. **Cash discount / Dual pricing** — configure the cash discount percentage in **Settings > Venue > Cash Discount**. Customers see both card and cash prices at checkout (e.g. Card: $100 | Cash: $96.50)
4. **Bar tabs** — tap "🍺 Start Tab" at payment to pre-authorize a card and hold the check open. Open tabs show in the register sidebar with a one-tap "Close" button to capture the final amount
5. **Gift cards** — issue from the Gift Cards page
6. **House accounts** — create the customer account on **House Accounts**, then choose **House Account** at payment or record standalone account activity. See [House Accounts](#house-accounts)
7. **EBT/SNAP** — *in implementation*. Per-item eligibility already works: mark each menu item **EBT-eligible / not eligible / auto** in Menu Builder (auto infers from item type — food/beverage eligible, alcohol excluded), and the register exempts eligible items from tax at tender. Authorization is not yet wired to a processor, so the EBT tender cannot complete a payment — contact support before promising EBT to a venue
8. **Split check** — four modes: even split, by seat, by item, and by custom amount. Each split can pay by a different method (card/cash/gift card). Unsplit (merge) an open split back into one check from the order panel
9. **Over-payment handling** — when a customer pays cash above the amount owed, choose how the excess is handled in **Settings > Venue > Over-payment handling**: *Give change* (cash back, recorded for end-of-day drawer reconciliation — the default), *Add to tip*, or *Ask cashier each time*. The amount applied to the bill is always exactly what's owed

<img src="../images/pos/settings_overpayment.png" alt="Over-payment Handling">
<img src="../images/pos/ipad_split_check.png" alt="Split Check">
<img src="../images/pos/ipad_bar_tab.png" alt="Bar Tab">
<img src="../images/pos/ipad_tap_to_pay.png" alt="Tap-to-Pay">
<img src="../images/pos/ipad_cash_discount.png" alt="Cash Discount">
<img src="../images/pos/ipad_post_payment_tip.png" alt="Post-Payment Tip">
<img src="../images/pos/ipad_ebt_payment.png" alt="EBT/SNAP Payment">
<img src="../images/pos/ipad_wallet_pay.png" alt="Apple Pay / Google Pay">
<img src="../images/pos/settings_house_accounts.png" alt="House Accounts">
<img src="../images/pos/settings_receipts.png" alt="Receipts">
<img src="../images/pos/production-demo-2026-08/prod-20260810-disputes.png" alt="Production demo Disputes and Chargebacks list with three populated cases">
<img src="../images/pos/settings_chargebacks.png" alt="Chargeback Settings">

</details>

<details>
<summary><strong>Payment review, receipts, disputes, and refunds</strong></summary>

These pages serve different jobs:

| Page | Route | Purpose |
|---|---|---|
| Payment Review | `/pos/payments` | Exception queue for payments that need staff review; it is not the complete payment history and can legitimately be empty |
| Receipts | `/pos/receipts` | Find an order, select it, then preview, print, email, or text its receipt |
| Disputes | `/pos/disputes` | Chargeback/dispute cases, evidence, amount, status, and due dates |
| Refunds | `/pos/refunds` | Search completed sales and process or review partial/full refunds |

Empty review queues and the pre-selection Receipts state are intentionally not used as screenshots.

</details>

---

<a name="staff--labor"></a>

### Staff & Labor

Scheduling, break punches, meal-penalty enforcement, overtime alerts, tip pooling (3 modes), and payroll with FLSA compliance.

<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-staff.png" alt="Production demo Staff Management with 14 configured staff records">
<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-roles.png" alt="Production demo Role Permissions matrix with configured access controls">

<details>
<summary><strong>Setup</strong></summary>

1. **Settings > Staff Management** — add employees with name, PIN, role
2. Configure pay periods, break rules, and overtime thresholds
3. Tip pool mode: by hours, percentage, or points
4. **Break punches** — staff Start/End a meal or rest break from the timeclock. Ending a break resumes the same shift (no clock-out/clock-in), and the break minutes are recorded on the shift
5. **Meal penalty** — set the rules in **Settings > Venue > Meal Penalty & Break Rules** (threshold, minimum meal length, premium minutes, and a **grace period**). When someone works past the threshold with no qualifying meal break, a premium is owed; it rolls into the labor report's gross pay. The grace period is slack past the threshold before any penalty applies

</details>

---

<a name="online-ordering--qr-table"></a>

### Online Ordering & QR Table

Customers browse your menu, order, and pay — no app needed. Pickup and delivery channels. QR codes per table go straight to KDS. Scheduled orders, loyalty points, promo codes, AI chat assistant, and order tracking.

<img src="../images/pos/online_01_menu.png" alt="Online">

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

<img src="../images/pos/ipad_qr_ordering.png" alt="QR Ordering">
<img src="../images/pos/ipad_order_tracking.png" alt="Order Tracking">
<img src="../images/pos/ipad_ai_chat_oo.png" alt="AI Chat (Customer)">
<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-online-ordering.png" alt="Production demo Online Ordering settings with configured business hours and order channels">

</details>

---

### Delivery Management

In-house drivers, 3PD delegation (DoorDash Drive, Uber Direct), or hybrid mode. Route optimization, driver GPS tracking, auto-dispatch, and menu sync to 3PD platforms. This section intentionally omits a screenshot while the demo has no configured provider or active delivery data; empty demo controls are not representative of the workflow.

<details>
<summary><strong>Setup</strong></summary>

1. **Choose mode** in **Settings > Delivery**: 3PD Only, In-House, or Hybrid (try in-house first, fall back to 3PD)
2. **3PD providers** — add DoorDash Drive or Uber Direct API credentials. The system creates deliveries via the provider API and tracks status
3. **In-house drivers** — add drivers with name, phone, vehicle type (car/bike/scooter/walk), and max concurrent orders
4. **Menu sync** — tap "Sync to DoorDash" / "Sync to Uber Eats" to upload your menu. Enable auto-sync to push changes automatically when you edit menu items
5. **Driver mobile page** — drivers open `/pos/delivery/driver` on their phone. They see assigned orders, tap to navigate, mark picked up / delivered / failed, and auto-report GPS every 30s
6. **Route optimization** — batch dispatch clusters nearby deliveries and assigns the optimal driver using proximity scoring
7. **Order status sync** — when KDS bumps an order to "ready", the system notifies the 3PD provider and triggers auto-dispatch for in-house drivers

The driver page is documented without a screenshot when the demo has no assigned deliveries; an empty driver queue is not representative of the workflow.

</details>

---

### AI Chat Assistant

Context-aware AI assistant across staff POS workflows and the online-ordering experience. It uses the current route to load relevant page context, supports voice input, quick prompts, and Prism memory, and can take **real actions** where that screen exposes a tool. Actions are **module-isolated** (a tool runs only in its own workflow) and **role-gated** (only staff with the required permission can run it). Dedicated display surfaces and screens without an action tool remain read-only or omit the launcher.

<img src="../images/pos/ipad_ai_chat_pos.png" alt="AI Chat (POS)">

<details>
<summary><strong>How it works</strong></summary>

**POS Staff Chat** — appears on every page, auto-loads live data for that screen, and beyond answering questions can **perform the action for you** (it confirms first, then calls a real, audited, tenant-scoped tool):
- **Register / Handheld / Drive-Thru / Tabs** — add item, apply discount, void item, split check, send payment link, open drawer; "Find order with 3 cokes"
- **KDS / Coursing / Expo** — bump or recall tickets, check allergens; "What's the oldest ticket?"
- **Tables / Table Ops** — availability, merge / split / transfer, reopen check
- **Reservations** — book a reservation, add a walk-in to the waitlist, seat / cancel / mark no-show
- **Loyalty** — look up a member, enroll a new member
- **Gift Cards** — check balance, reload, redeem against an order
- **Staff** — clock a staff member out
- **Messaging** — post to a staff channel; **Calendar** — schedule an event
- **Reports / Dashboards** — sales summary (revenue, orders, average ticket, tax, tips, discounts)
- **Payroll / HR / Multi-Location** — aggregate labor-hours and labor-cost summary
- **Accounting** — chart-of-accounts summary; **Allergens** — allergen-coverage audit; **Compliance** — RBS certs, incidents, data-deletion deadlines; **Documents** — search the file drive; **Marketing** — campaign performance; **Feedback** — NPS + ratings; **House Accounts / Vendors / Payments / Refunds / Scheduled orders** — read-only summaries
- **Screen Builder** — toggle receipt display options

Money- and compliance-sensitive actions (payroll ACH, tax changes, journal postings, loyalty point grants, issuing refunds, sending marketing) are deliberately **read-only in chat** — the assistant surfaces the data and points you to the on-screen control to execute them.

**OO Customer Chat** — customers ask "Make me a half pepperoni half mushroom pizza" and the AI builds the order with correct modifiers and pricing:
- Voice input (microphone) + voice output (speaker) with adjustable speed/pitch/gender
- 14 languages with locale picker
- Returning customer greeting via cookie
- Tool calls: add_to_cart, remove_from_cart, filter_menu, suggest_combo

</details>

---

### AI Voice Ordering (Phone)

Customers call your venue's phone number and place orders through natural AI conversation. The current voice stack uses Deepgram Nova-3 multilingual speech recognition, ElevenLabs Flash v2.5 speech synthesis, Gemini 3.6 Flash ordering logic, and Twilio ConversationRelay. Returning customer recognition, phonetic correction, and automatic SMS confirmation are built into the workflow.

The production demo's integration card is not shown while its payment processor reports a disconnected state; enabling Voice Ordering alone does not prove the complete order-to-payment path is connected.

<details>
<summary><strong>Setup & Configuration</strong></summary>

1. **Enable** in Settings > Integrations > Voice Ordering
2. Set your **Twilio phone number** in Settings > Venue
3. Configure the **Twilio console** — Phone Number > Voice > Webhook POST > `https://your-domain.com/api/v1/pos/webhooks/voice`

**Customizable settings:**

| Setting | Description |
|---------|-------------|
| Custom Greeting | Opening message with `{venue}` and `{name}` placeholders |
| AI Persona | Tone and style — "friendly server", "professional concierge", etc. |
| Today's Specials | AI proactively suggests these when asked "what's good?" |
| Supported Languages | 26 configured conversation languages with multilingual detection and explicit "switch to" commands (see below) |
| Fallback Number | Transfer to human after repeated AI failures |

</details>

<details>
<summary><strong>How a call works</strong></summary>

1. Customer calls venue phone number
2. AI greets in English — if the customer speaks a different supported language (e.g., Spanish, Russian), the AI phonetically detects the language and **automatically switches** the conversation flow before the first item is ordered.
3. Twilio ConversationRelay streams speech and responses over the secure voice relay connection.
4. Returning customers auto-recognized by phone — AI greets by name, knows past orders.
5. The Verifier intercepts background noise, wind, or filler words ("uh", "um"), ensuring the AI only processes clean intent.
6. Gemini 3.6 Flash processes the transcribed order context and returns the next response or cart action.
7. AI adds items immediately, confirms with price: "Added a Classic Burger for twelve dollars. What else?"
8. Phonetic correction: garbled phone audio auto-matched to menu items
9. "Change burger to family pack" → removes old + adds new in one turn
10. "Repeat my order" → AI reads back all items with prices
11. "That's all" → asks for customer name → reads back order with total
12. "Yes" → order created → KDS kitchen ticket → SMS confirmation
13. Session saved to database for analytics

**Customer commands:**

| Say | What happens |
|-----|-------------|
| Any menu item name | Added immediately with price confirmation |
| "Change X to Y" | Removes X, adds Y |
| "Remove the fries" | Item removed |
| "What do you have?" | Top items listed |
| "Repeat my order" | Current order read back with prices |
| "My usual" | Adds items from last order (returning customers) |
| "Put me on the waitlist" | Asks for party size and adds customer to venue waitlist |
| "How long is the wait?" | Reads back current waitlist estimate |
| "That's all" / "Done" | Starts confirmation flow |
| "Yes" / "Confirm" | Places order |
| "No" / "Wait" | Returns to ordering |

**Language support:**

| Language | Auto-detect | Via "switch to" | Notes |
|----------|:-:|:-:|-------|
| English | Yes | Yes | Default |
| Spanish | Yes | Yes | |
| French | Yes | Yes | |
| German | Yes | Yes | |
| Italian | Yes | Yes | |
| Portuguese | Yes | Yes | |
| Russian | Yes | Yes | |
| Chinese (Mandarin) | Yes | Yes | |
| Japanese | Yes | Yes | |
| Korean | Yes | Yes | |
| Hindi | Yes | Yes | |
| Dutch | Yes | Yes | |
| Romanian | Yes | Yes | Phonetic auto-detection |
| Ukrainian | Yes | Yes | Phonetic auto-detection |
| Arabic | Yes | Yes | Phonetic auto-detection |
| Vietnamese | Yes | Yes | Phonetic auto-detection |
| Bulgarian | Yes | Yes | |
| Czech | Yes | Yes | |
| Danish | Yes | Yes | |
| Finnish | Yes | Yes | |
| Hungarian | Yes | Yes | |
| Indonesian | Yes | Yes | |
| Polish | Yes | Yes | |
| Swedish | Yes | Yes | |
| Tamil | Yes | Yes | |
| Turkish | Yes | Yes | |

**Auto-detect**: just speak — AI detects the language automatically (Deepgram Nova-3 multi-language)
**Via "switch to"**: say "switch to Romanian" in English first, then continue in that language

**Online ordering** is also available at the same time:

<img src="../images/pos/voice_ordering_oo_menu.png" alt="Online Ordering Menu">

</details>

<details>
<summary><strong>Voice Stack Architecture</strong></summary>

| Layer | Technology | Behavior |
|-------|-----------|---------|
| **Speech-to-Text** | Deepgram Nova-3 multilingual through ConversationRelay | Streaming |
| **AI/LLM** | Gemini 3.6 Flash | Streaming turn processing |
| **Text-to-Speech** | ElevenLabs Flash v2.5 through ConversationRelay | Streaming |
| **Transport** | Twilio ConversationRelay over a secure WebSocket | Bidirectional |
| **Noise Filtering** | Relay input verifier for empty, repeated, filler-only, and malformed speech | Before model invocation |
| **Server** | POS voice webhook and relay-chat routes | Venue-scoped |
| **Phonetic Correction** | Menu-aware Gemini parsing | During the ordering turn |
| **Customer Memory** | Supabase past-order and loyalty context | Loaded per session |

**Fallback:** If the AI encounters a severe failure or consecutive low-confidence inputs, it gracefully transfers to a human line.

</details>


---

### WhatsApp Ordering

Same AI engine as voice ordering, over WhatsApp — unified in a shared ordering module (`chat-ordering`) with identical state machine, cart handling, and order placement. Text or voice message in **any language** — AI auto-detects. Cart with emoji formatting, order confirmation with ETA. No app download needed.

<img src="../images/pos/whatsapp_ordering.png" alt="WhatsApp Ordering">

<details>
<summary><strong>How it works</strong></summary>

1. Customer texts or sends a voice message to the venue on WhatsApp
2. AI responds with Gemini 3.6 Flash — the same menu and ordering logic used by the voice workflow
3. **Any language** — text in English, Russian, Spanish, Chinese, or record a voice message in any of 30+ languages (auto-detected via Deepgram)
4. Add items naturally: "I want a burger and fries" or "я хочу бургер и картошку"
4. Cart displayed after each message:
   ```
   🛒 Your cart:
     1x Classic Burger
     1x Fries

   Say "done" when ready to order.
   ```
5. "done" → asks for name → confirms order → "YES" → order placed
6. Confirmation with order number, total, and estimated pickup time
7. Payment link sent via Stripe Checkout
8. SMS confirmation via Twilio Messaging Service (A2P 10DLC compliant)
9. Email receipt via Resend (when customer email is on file)
10. Returning customers recognized by phone — favorites and past orders recalled

**Commands:**

| Text | What happens |
|------|-------------|
| Any menu item | Added to cart with price |
| "Change X to Y" | Swap items |
| "Remove fries" | Item removed |
| "My usual" | Last order re-added |
| "Done" | Starts confirmation |
| "YES" | Places order → KDS ticket |
| Voice message (mic button) | Transcribed via Deepgram, processed as text |

**Language support:**

| Input | Languages |
|-------|-----------|
| **Text messages** | 100+ (any language Gemini understands) |
| **Voice messages** | 30+ (auto-detected via Deepgram Nova-2) |
| **AI responses** | Same language as customer input |

**Venue resolution:** The inbound Twilio `To` number must match a venue's `whatsapp_number` or `phone_number`. If no match, the system fails closed — no country-based guessing or fallback to arbitrary venues.

**Setup:**
1. Register a WhatsApp Business number in Twilio Console
2. Set webhook: `https://your-domain.com/api/v1/pos/webhooks/whatsapp` (POST)
3. In POS Settings → Integrations, enter the WhatsApp number for the venue
4. Customers text the number — no app install, no signup

</details>

---

### AI Dish Image Generation

Menu items automatically get AI-generated dish photos — no professional photography needed. A photo is generated once per dish and cached, so the same item is never billed twice. Items show an emoji placeholder until a photo exists, and photos you upload yourself always take priority.

<details>
<summary><strong>Setup</strong></summary>

1. Open **Settings > Menu Builder**. A new item generates its photo in the background — the item is sellable immediately and the picture catches up
2. **Generate one** — an item without a photo shows a **Generate image** button in its editor
3. **Generate all missing** — the Menu Images manager generates every item that lacks a photo in one batch, showing the item count and estimated cost for approval before anything runs
4. **Upload your own** at any time to override a generated photo. Uploads are never overwritten by generation, and clearing generated images leaves your uploads untouched
5. Each venue has a **monthly image budget**. When it is reached, generation stops rather than continuing to spend, and says so instead of failing quietly

</details>

<details>
<summary><strong>If an item is missing its photo</strong></summary>

Occasionally a photo cannot be produced at the moment an item is created. The item is still saved and sellable — only the picture is missing.

Opening **Settings > Menu Builder** retries recently added items automatically, so in most cases the photo appears on your next visit to that page with no action needed. To fix one immediately, use **Generate image** in the item's editor, or **Generate all missing** in the Menu Images manager.

</details>

---

<a name="pizza-builder--modifiers"></a>

### Pizza Builder & Modifiers

Visual half/half pizza builder with per-topping placement and intensity. Standard modifiers with qty, nested groups, forced/optional, and max-quantity limits.

<img src="../images/pos/ipad_pizza_builder.png" alt="Pizza Builder">

<details>
<summary><strong>Setup</strong></summary>

1. **Modifier sets** — create sets in **Settings > Menu Builder > Modifier Sets**. Set min/max selections, price deltas, and max quantity per option. Use **Items** on a set to tick every menu item that should offer it, instead of opening each item one at a time
2. **Shared modifiers** — the **Modifiers** tab is your venue's list of modifiers, each one defined once and reused. "Ranch" is a single modifier that can belong to several sets and carry a different price in each, so renaming it or 86'ing it takes effect everywhere at once. Open a set and choose **Edit** to pick modifiers for it from that shared list, set each one's price for this set, and drag them into the order staff will see
3. **Pizza builder** — set a modifier group's display mode to "🍕 Pizza Builder" in the menu builder. This triggers the visual half/half UI instead of checkboxes
4. **Placement** — customers choose Whole, Left Half, or Right Half for each topping. Half placement = 50% of the topping price
5. **Intensity** — None (not selected), Light (75% price), Regular (100%), Extra (150% price)
6. **3PD compatibility** — pizza toppings sync to DoorDash/UberEats as standard modifiers (placement/intensity are stripped since 3PD doesn't support halves). This is logged as an incompatibility
7. **AI chat** — "Make me a half pepperoni half mushroom pizza" works without the visual builder. The AI maps to the correct modifiers and prices

<img src="../images/pos/ipad_modifier_sheet.png" alt="Modifier Sheet">

</details>

---

### Customer Display

Second screen facing the customer with live order, running total, and idle promos.

<img src="../images/pos/production-demo-2026-08/prod-20260810-customer-display.png" alt="Production demo Customer Display with two items and a populated total">

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/display` on a second iPad or monitor facing the customer
2. The display auto-syncs with the active register order in real time
3. Configure idle promo images in **Settings > Venue**

</details>

---

### Reports

Sales, PMIX, category sales, per-tax/jurisdiction, menu engineering, speed of service, server leaderboard, payments, voids, and comps. CSV export on every report.

<img src="../images/pos/production-demo-2026-08/prod-20260810-reports.png" alt="Production demo Reports dashboard showing a populated weekly sales period">

<details>
<summary><strong>Setup</strong></summary>

1. Access from the **Reports** page — all reports are auto-generated from order data
2. **Sales** — hourly heatmap, daily/weekly/monthly totals
3. **PMIX** — product mix by category, item, and modifier
4. **Category sales** — sales rolled up by menu category (major group), with each category's share of net sales
5. **Tax** — a per-jurisdiction breakdown (taxable sales + tax collected per tax zone) that reconciles against the recorded tax
6. **Comps** — comped items itemized, broken down by (configurable) comp reason, with totals and CSV
7. **Menu engineering** — Star/Dog/Puzzle/Workhorse quadrant analysis
8. **Speed of service** — per-station ticket times at `/pos/reports/speed`
9. **Server leaderboard** — staff performance ranking at `/pos/reports/leaderboard`
10. **Audit** — actor, action, entity, timestamp, and details at `/pos/reports/audit`
11. **Labor** — hours, break minutes, overtime, and meal-penalty premium folded into gross pay
12. **CSV export** — every report has a one-click CSV download

<img src="../images/pos/settings_menu_engineering.png" alt="Menu Engineering">
<img src="../images/pos/production-demo-2026-08/prod-20260810-report-speed.png" alt="Production demo Speed of Service report with populated station metrics">
<img src="../images/pos/production-demo-2026-08/prod-20260810-report-audit.png" alt="Production demo Audit report with populated activity rows">
<img src="../images/pos/settings_revenue_centers.png" alt="Revenue Centers">

</details>

---

<a name="inventory--recipe-costing"></a>

### Inventory & Recipe Costing

Stock tracking with optimistic-lock deductions, low-stock alerts, vendor management, recipe builder with ingredient cost + profit margin %, plus reorder suggestions and purchase orders with receiving.

<img src="../images/pos/production-demo-2026-08/prod-20260810-inventory.png" alt="Production demo Inventory with five populated SKU records and stock values">

<details>
<summary><strong>Setup</strong></summary>

1. Add inventory items with SKU, qty, unit, cost per unit, and **low stock threshold** (the reorder point)
2. Link **recipes** to menu items — ingredient cost + margin % auto-calculates
3. On order completion, inventory **auto-deducts** per recipe (optimistic lock with retry)
4. **Stock count** with audit trail — records who counted, old vs new quantity
5. Low-stock items trigger **real-time alerts** at shift clock-in
6. **Reorder suggestions** — items at or below their reorder point are surfaced with a suggested order quantity (up to par) and estimated cost, grouped by vendor
7. **Purchase orders** — raise a PO to a supplier straight from the suggestions (one PO per vendor); **receive** it to add the ordered quantities back into stock. Receiving is idempotent so a PO can't be received twice

<img src="../images/pos/production-demo-2026-08/prod-20260810-vendors.png" alt="Production demo Vendors with three configured supplier records">

Recipe configuration is described without a production screenshot when the demo has no recipe records.

</details>

---

<a name="gift-cards--loyalty"></a>

### Gift Cards & Loyalty

Issue gift cards ($25–$250) with auto-numbering and multi-location redemption. Loyalty with points, auto-tier, referrals, and **automatic award coupon generation** when customers cross point thresholds.

<img src="../images/pos/production-demo-2026-08/prod-20260810-gift-cards.png" alt="Production demo Gift Cards with two active cards and a combined balance">

<details>
<summary><strong>Setup</strong></summary>

1. **Gift cards** — issue from the Gift Cards page. Auto-numbered. Customers redeem at payment
2. **Multi-location** — set `workspace_id` on gift cards/house accounts for cross-venue redemption
3. **Loyalty** — enable in **Settings > Loyalty**. Customers earn points per dollar spent
4. Auto-tier upgrades: Bronze → Silver → Gold based on cumulative spend
5. **Award auto-generation** — configure point thresholds in venue features. When a customer crosses a threshold, a coupon is automatically issued with the source discount's value (single-use, optimistic-lock dedup)
6. Referral rewards: existing customers share a link, both get bonus points

The Loyalty workspace is documented without a screenshot when the production demo has no enrolled members.

</details>

---

### House Accounts

House Accounts is the customer A/R workspace for companies, schools, municipalities, regular guests, and other customers that buy now and settle later. It includes credit limits, an immutable activity ledger, customer deposits, statements, delivery history, public balance access, and payment collection.

<img src="../images/pos/production-demo-2026-08/prod-20260810-house-accounts.png" alt="Production demo House Accounts with three customers and populated receivable balances">

<p>
  <img src="../images/pos/house-accounts-v2/accounts-list.png" alt="House Accounts list with outstanding balances, credits, active accounts, and over-limit summary" width="49%">
  <img src="../images/pos/house-accounts-v2/account-detail.png" alt="House Account detail with balance, available credit, contact information, and account actions" width="49%">
</p>

<details open>
<summary><strong>Manager setup</strong></summary>

1. Confirm the venue has an active **Enterprise** subscription or trial.
2. Open **House Accounts** from the POS navigation and select **New Account**.
3. Enter the account name. Add a contact name, email, mobile number, and billing address when statements or payment links will be delivered.
4. Set the credit limit if your role permits financial overrides. Otherwise the venue default applies.
5. Open the account, select **Settings**, and optionally configure:
   - statement frequency: **7, 14, or 30 days**
   - next statement date
   - email and/or SMS automatic delivery
   - an automatic discount
6. Use **Freeze** instead of deleting an account. Frozen accounts keep their complete ledger and statement history and cannot accept new charges or payments until reactivated.

Managers and supervisors can manage accounts. Credit-limit changes require the same elevated permission used for payment refunds.

</details>

<details>
<summary><strong>Charge an account</strong></summary>

- **From a sale:** on the payment screen choose **House Account**, select the customer, review available credit, and confirm. The server rejects charges that exceed the account limit.
- **Standalone charge:** open the account and select **Add Charge** for activity that is not tied to a POS order. Enter the amount and a useful note.
- **Automatic discount:** when configured in the account Settings tab, the discount is applied to eligible orders before the charge reaches the account.

Order-backed charges are posted to the general ledger by the normal end-of-day journal. Standalone account activity posts immediately, so the same receivable is never posted twice.

</details>

<details>
<summary><strong>Receive a payment or customer deposit</strong></summary>

Open the account and select **Receive Payment**, then choose the tender that was actually used:

| Tender | Workflow |
|---|---|
| **Cash** | An open cash drawer is required. The collection is included in drawer reconciliation. |
| **Check** | Record the payment and put the check number in the note. It does not change cash-drawer totals. |
| **Card terminal** | Complete the payment on the venue's configured Stripe or Dejavoo terminal first. Then record it against the account and enter the processor transaction or receipt reference. The configured processor is linked to the ledger entry automatically. |
| **Other** | Use for a verified external payment method and describe the source/reference in the note. |

If the payment exceeds the current amount due, the POS shows the resulting credit and requires confirmation before holding it as a **customer deposit**. Credits are available for future charges and are shown separately from A/R.

<img src="../images/pos/house-accounts-v2/activity-ledger.png" alt="House Account activity ledger showing charges, payments, tender references, amounts, and running balances">

</details>

<details>
<summary><strong>Create and send statements</strong></summary>

1. Open the account and select **Statements**.
2. Choose the period end. The period start is derived from the canonical ledger or the preceding statement so activity cannot be skipped.
3. Select **Generate**, then **View**, **Print**, or **Send**.
4. Email and SMS attempts appear in delivery history. A failed channel is visible on both the account list and account detail page.
5. To correct a statement, select **Void**, enter a reason, and optionally regenerate the same period. Issued history is never deleted.

Automatic statements run daily and process accounts whose configured next-send date is due. The scheduled job skips empty periods and advances the next statement date safely.

<img src="../images/pos/house-accounts-v2/statement.png" alt="House Account statement with opening balance, itemized activity, amounts, and running balance">

</details>

<details>
<summary><strong>Customer balance and hosted payment links</strong></summary>

Every account can expose a tokenized customer page with the current balance and statement history. Regenerate the public token from the account Settings tab if a link was shared with the wrong recipient.

- **Stripe:** hosted balance-payment links are available when Stripe is the venue processor and the Stripe secret/webhook are configured. Only one active fixed-amount link is allowed, it expires after 24 hours, and a balance change invalidates the old link.
- **Dejavoo:** terminal payments can be recorded against the account. House Account hosted checkout is mock-only in local/non-production testing until the full create/capture/expire lifecycle is configured and verified.

<p>
  <img src="../images/pos/house-accounts-v2/customer-balance.png" alt="Tokenized customer House Account balance page with secure payment action" width="66%">
  <img src="../images/pos/house-accounts-v2/mobile-frozen.png" alt="Frozen House Account on a mobile viewport with balance and preserved history" width="30%">
</p>

</details>

<details>
<summary><strong>Developer and deployment setup</strong></summary>

1. Apply the POS and shared-accounting migrations using the repository's combined migration runner:

   ```bash
   cd synalux-pos
   ./scripts/push-manual.sh --apply
   ```

   Do not use `supabase db push` while POS and Portal share the same Supabase projects and migration histories.

2. Configure the normal POS database credentials plus:

   ```env
   # Public URL used in statement and customer links
   SYNALUX_POS_URL=https://pos.your-domain.example

   # Portal delivery bridge for statement/payment-link email and SMS
   SYNALUX_PORTAL_URL=https://your-portal-domain.example
   SYNALUX_SERVICE_KEY=replace-with-a-shared-service-secret

   # Authorizes /api/cron/send-ha-statements
   CRON_SECRET=replace-with-a-random-secret

   # Stripe hosted balance checkout
   STRIPE_SECRET_KEY=sk_live_or_test
   STRIPE_WEBHOOK_SECRET=whsec_replace
   ```

3. Configure the Stripe webhook on the POS custom domain at `/api/v1/pos/webhooks/stripe`. The House Account balance is updated only after the signed processor completion event is reconciled.
4. The included Vercel schedule calls `/api/cron/send-ha-statements` daily at **13:00 UTC**. Non-Vercel deployments must invoke the same route with `Authorization: Bearer $CRON_SECRET`.
5. For local Dejavoo workflow tests only, set `DEJAVOO_HA_MOCK_MODE=true` with `NODE_ENV` not equal to `production`. Production rejects the mock return and FEED completion paths; do not enable this variable in production.

</details>

#### Accounting behavior

House Accounts uses debit/credit control accounts rather than a second, isolated accounting system:

- a positive amount owed is **House Accounts Receivable**
- an overpayment or prepaid credit is **Customer Deposits**
- standalone charges and collections post immediately
- order-backed charges remain part of the existing end-of-day sales journal
- payments reduce A/R first; any excess credits Customer Deposits
- later charges consume Customer Deposits before increasing A/R

The posting path is idempotent and failed accounting posts are retained for retry instead of silently dropping the subledger event.

---

### Discount Engine

Auto-apply discounts, group discounts ("every 4th pizza free"), stacking rules, purchase minimums, and usage limits — all server-side enforced.

<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-discounts.png" alt="Production demo Discount Settings with three configured discount rules">

<details>
<summary><strong>Setup</strong></summary>

1. **Auto-apply** — toggle on any discount. Applied automatically when conditions met (no coupon code needed)
2. **Group discounts** — set `every_nth` (e.g., 4) and `discount_type` (free or % off). Applies to the lowest-priced qualifying item
3. **Stacking** — toggle `is_exclusive` to prevent combining with other discounts
4. **Purchase minimum** — set `min_purchase_cents`. Discount only applies above this subtotal
5. **Max uses** — set `max_uses` for limited promotions. Enforced atomically via Postgres function (concurrent requests: exactly one succeeds)
6. **Modifier targeting** — require specific modifier selections (e.g., "large pizza with exactly 2 toppings")
7. **Revenue Center restrictions** — limit discounts to specific RCs
8. **Target price** — set a specific final price for promotional items
9. **Coupon codes** — give a discount a `coupon_code` and it's hidden from the open discount list; the cashier applies it by typing or **scanning the code** in the register's coupon field. Invalid, expired, and not-yet-active codes are rejected with inline feedback

| Type | Example | How it works |
|------|---------|-------------|
| Percent | 10% off | `value: 1000` (basis points) |
| Amount | $5 off | `value: 500` (cents) |
| BOGO | Buy 1 get 1 | `discount_type: bogo` |
| Target price | Item for $5 | `discount_type: target_price, value: 500` |
| Group | Every 4th free | `group_discount_config: {every_nth: 4, discount_type: "free"}` |

</details>

---

### Real-Time Alerts

Automated alerts for low stock, overtime, and order delays. Auto-scan at every shift clock-in. Role-filtered — managers see everything, servers see their own.

<img src="../images/pos/ipad_alerts_reports.png" alt="Reports with Alerts">

<details>
<summary><strong>Setup</strong></summary>

1. **Low stock** — set `low_stock_threshold` on inventory items. Alert fires at threshold (warning) and at zero (critical)
2. **Overtime** — warning at 8 hours on clock, critical at 10 hours
3. **Order delay** — warning at 25 minutes ticket age, critical at 40 minutes
4. Alerts auto-scan at every **staff clock-in** — no manual trigger needed
5. **Dedup** — duplicate alerts prevented. Same condition only generates one unread alert
6. View alerts in the Reports dashboard (60-second auto-refresh)

</details>

---

### Compliance

Age verification, RBS cert tracking, tax-exempt orders, per-item taxability, CCPA/GDPR, and full audit trail.

The production demo Compliance page is currently omitted from screenshots because it does not render successfully. The configuration paths below remain the source-backed workflow; this is not a visual acceptance claim for that page.

<details>
<summary><strong>Tax Configuration</strong></summary>

**Order-level tax exempt** — toggle an entire order as non-taxable from the order panel.

**Per-item taxability** — each menu item has an **Item Type** (Food, Alcohol, Beverage, Merchandise). Tax zones define which item types they apply to. Set an item's type to one not included in any active tax zone and it is effectively non-taxable. Configure item types in **Settings > Menu Builder** and tax zones in **Settings > Tax**.

<img src="../images/pos/settings_tax_exempt.png" alt="Tax Exempt">
<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-tax.png" alt="Production demo Tax Settings with two populated jurisdiction and rate records">

</details>

<details>
<summary><strong>Age Verification & Compliance</strong></summary>

Age checks are enforced for alcohol items; privacy controls cover CCPA/GDPR data requests; and RBS certificates are tracked by staff member. These controls are not shown as production-demo screenshots until the Compliance page renders successfully.

</details>

---

### End of Day

Count cash (with optional blind close), distribute tip pool, export GL journal, print Z-Report, close register.

An end-of-day screenshot is shown only after the demo has a recorded batch close; the current empty batch state is intentionally not pictured.

<details>
<summary><strong>Setup</strong></summary>

1. Enter the closing count by denomination — the counted total, expected amount, and over/short are shown as you count
2. **Blind drawer count** — enable **Blind Close** in **Settings > Venue** to hide the expected amount and over/short while counting, so the count is unbiased. A manager can reveal the figures after the count is entered; the variance is still recorded
3. **Tip pool** distribution, **GL journal** export, and **Z-Report** print
4. Closing the register records the over/short for reconciliation

</details>

---

<a name="reservations--waitlist"></a>

### Reservations & Waitlist

Full reservation + waitlist management. Timeline view with party size, table assignment, auto-position waitlist with ETA, and webhook integration.

<img src="../images/pos/production-demo-2026-08/prod-20260810-reservations.png" alt="Production demo Reservations and Waitlist with three reservations and populated waitlist records">

<details>
<summary><strong>Setup</strong></summary>

1. Open the **Reservations** page — toggle between Reservations and Waitlist tabs
2. **Create reservation** — guest name, phone, email, party size, date/time, table assignment
3. **Add to waitlist** — auto-positions with estimated wait time (15 min × position)
4. **Seat** a party — assign table, records seated_at timestamp
5. **Cancel / No-show** — tracked with timestamps for reporting
6. **Webhook integration** — configure in **Settings > Integrations** for Google Reserve, OpenTable, or Yelp
7. Auto-refresh: reservations every 30s, waitlist every 15s

</details>

---

### Catering

Large-order entry with Banquet Event Orders, delivery scheduling, and deposit tracking.

<img src="../images/pos/production-demo-2026-08/prod-20260810-catering.png" alt="Production demo Catering workspace with three completed events and order totals">

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

The production demo currently has no active drive-thru tickets, so this workflow is documented without an empty lane-board screenshot.

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

<img src="../images/pos/ipad_handheld_ordering.png" alt="Handheld">

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/handheld` on any iPhone or small tablet
2. Server logs in with their PIN — same role-based access as the register
3. Tap a table → add items → send to KDS. Full modifier support including pizza builder

</details>

---

### Refunds

Partial or full refund with reason codes for Stripe and Dejavoo payments. Tip-aware refund ceiling prevents over-refund on tip-adjusted captures. Gift card and house account balances auto-restored on refund.

<img src="../images/pos/production-demo-2026-08/prod-20260810-refunds.png" alt="Production demo Refunds workspace with populated completed-payment rows">

<details>
<summary><strong>Setup</strong></summary>

1. Open the **Refunds** page or tap "Refund" on any completed order
2. Choose partial (specific items) or full refund
3. Select a reason code (wrong item, quality, customer request, etc.)
4. Refund is processed via the venue's payment processor (Stripe or Dejavoo SPIn). Cash refunds are recorded for drawer reconciliation
5. **Reopen check** — managers can reopen a closed order for corrections, then re-close

<img src="../images/pos/ipad_reopen_check.png" alt="Reopen Check">

</details>

---

<a name="multi-location--franchise"></a>

### Multi-Location & Franchise

Per-venue KPIs, consolidated P&L, config push, and franchise reporting. Month-to-date comparison across all locations with revenue, COGS, labor, and net profit side-by-side.

<img src="../images/pos/production-demo-2026-08/prod-20260810-multi-location.png" alt="Production demo Multi-Location dashboard with populated revenue and order KPIs">

<details>
<summary><strong>Setup</strong></summary>

1. Create additional venues under the same workspace in **Settings > Multi-Location**
2. Push menu, tax, and discount configs from a template venue to all locations
3. View consolidated P&L, sales, and labor reports across all venues
4. Franchise reporting with per-location royalty calculations
5. **Month-to-date comparison** — revenue, COGS, labor, net profit per venue side-by-side
6. **CSV export** — download consolidated P&L for accountant handoff

</details>

---

<a name="accounting--ledger"></a>

### Accounting & Ledger

Journal entries, general ledger, and banking integration. QuickBooks and Xero auto-sync at EOD.

<img src="../images/pos/production-demo-2026-08/prod-20260810-general-ledger.png" alt="Production demo General Ledger with ten populated journal rows">

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/accounting` for the main accounting dashboard
2. `/pos/accounting/ledger` for journal entries and GL
3. `/pos/accounting/banking` for bank feed integration
4. Configure QuickBooks or Xero sync in **Settings > Integrations** — GL journal auto-exports at end of day

Banking is documented without a screenshot until a bank connection is present; the disconnected setup state is not used as an example.

</details>

---

<a name="coursing--course-firing"></a>

### Coursing & Course Firing

Multi-course meal sequencing with per-item course assignment and fire-on-demand. Assign course numbers to menu items and fire them sequentially from the register.

<img src="../images/pos/production-demo-2026-08/prod-20260810-coursing.png" alt="Production demo Coursing workspace with populated course groups and fire controls">

<details>
<summary><strong>Setup</strong></summary>

1. Assign course numbers (1–6) to each item in the order ticket using the Course dropdown
2. Course 0 = fire immediately. Courses 1–6 fire in sequence when the server taps **"Fire Next Course"**
3. KDS shows course badges on each ticket item with color-coded timing
4. Seat assignment works alongside courses — assign items to Seat 1/2/3 and Course 1/2/3 independently
5. Kitchen holds later courses until earlier ones are bumped — perfect for appetizer → entree → dessert flow

</details>

---

### Order Throttling

Rate-limit incoming online orders during peak times to prevent kitchen overwhelm.

The production demo currently has no queued throttled orders, so the zero-queue state is not shown as a product screenshot.

<details>
<summary><strong>Setup</strong></summary>

1. Configure throttle limits in **Settings > Online Ordering**
2. Set max orders per 15-minute window
3. When the limit is reached, new customers see "We're busy — try again in a few minutes"

</details>

---

<a name="hr--timesheets"></a>

### HR & Timesheets

Leave management, timesheet review, payroll draft with FLSA overtime split, and per-server KPIs. Pulls directly from clock-in/out data — all staff appear automatically including PIN-only staff.

HR, timesheet, and payroll pages are documented without demo screenshots until the selected pay period contains populated shift and payroll records.

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/hr` for the HR command center
2. **Timesheets tab** — clock-in/clock-out data grouped by staff member for the selected week. Week picker defaults to current Mon–Sun
3. **Payroll Draft tab** — calculates gross pay: regular hours (up to 40h) + overtime (above 40h at 1.5×). Export CSV for Gusto/ADP
4. **KPIs tab** — per-server metrics: sales/hour, avg check, tip %, 7-day sparkline trend
5. Staff submit time-off requests; managers approve/deny
6. **IRS Form 8027** — Settings > Compliance > Form 8027. Auto-calculates gross receipts, charge tips, and 8% allocation for tipped establishments

</details>

---

### Back Office Suite

Complete back-office suite built into the POS — no separate software needed. Every module is wired to POS data so EOD, timesheets, payroll, and vendor communications flow automatically.

The `/pos/backoffice/*` paths are the canonical routes and keep the back-office sidebar visible. Legacy standalone paths such as `/pos/documents`, `/pos/mail`, `/pos/calendar`, `/pos/dashboards`, `/pos/forms`, and `/pos/payroll` redirect into that shell.

| Module | What it does | Route |
|---|---|---|
| **Accounting & GL** | Double-entry ledger, journal entries, P&L, balance sheet. EOD auto-posts to GL | `/pos/accounting` |
| **Bank Feed** | Connect bank via Plaid/Salt Edge. Auto-match transactions. Reconciliation | `/pos/accounting/banking` |
| **Payroll** | Pay-period review, payroll drafts, history, and exports | `/pos/backoffice/payroll` |
| **Documents** | Connected cloud file storage, folders, uploads, and sharing | `/pos/backoffice/documents` |
| **Mail** | Connected mailbox, compose/reply, templates, and vendor auto-tagging | `/pos/backoffice/mail` |
| **Calendar** | Connected calendar events, reservations, catering, and staff meetings | `/pos/backoffice/calendar` |
| **Back Office Messaging** | Venue-scoped channels and real-time staff communication | `/pos/backoffice/messaging` |
| **Staff Messages** | Standalone staff messaging workspace outside the back-office shell | `/pos/messages` |
| **AI Assistant** | Context-aware AI with live POS data | `/pos/assistant` |
| **Operational Forms** | 12 ready-to-print/download restaurant forms | `/pos/backoffice/forms` |
| **Custom Form Builder** | API-backed templates and submissions with 10 field types | `/pos/form-builder` |
| **Dashboards** | Drag-and-drop widget builder with auto-refresh | `/pos/backoffice/dashboards` |

<details>
<summary><strong>Documents</strong></summary>

Documents uses the portal-connected cloud drive. Connect the appropriate provider/account before expecting files; without that authorization the page presents a connection requirement rather than a local standalone drive.

</details>

<details>
<summary><strong>Mail</strong></summary>

Full inbox for your restaurant — connected to Gmail or Outlook. Compose, reply, templates (vendor orders, catering quotes, EOD summary). Vendor emails auto-tagged with vendor name badge when sender matches your vendor records.

Mail is provider-backed and requires portal authentication plus a connected mailbox. It does not fall back to a separate local inbox.

</details>

<details>
<summary><strong>Calendar</strong></summary>

Connected calendar events, reservations, catering events, staff meetings, and delivery schedules appear in one view. A provider connection is required; the production demo connection prompt is not used as a feature screenshot.

</details>

<details>
<summary><strong>Staff Messaging</strong></summary>

Slack-like internal messaging — no Slack account needed. 6 pre-configured channels:

| Channel | Purpose |
|---|---|
| **All Staff** | Broadcast to everyone |
| **Front of House** | Servers, hosts, bartenders |
| **Back of House** | Kitchen, prep, expo |
| **Managers** | Managers and admin only |
| **Daily Specials** | Push 86'd items, daily features |
| **Lost & Found** | Customer lost items |

Messages use Supabase Realtime — delivery in < 200ms on the same LAN. Direct messages supported. Messages are venue-scoped: staff at different venues cannot see each other's channels.

</details>

<details>
<summary><strong>Dashboards</strong></summary>

Drag-and-drop widget builder with metric cards, charts, and tables. Preset templates for Owner, Manager, and Kitchen views. Auto-refresh every 30 seconds.

The dashboard builder is documented without a screenshot when the venue has no saved dashboard widgets.

</details>

<details>
<summary><strong>Operational Forms vs. Custom Form Builder</strong></summary>

These are separate workflows:

- `/pos/backoffice/forms` contains the 12 built-in restaurant forms. Staff choose a form and print or download a prefilled document; it is not an empty template library.
- `/pos/form-builder` creates custom API-backed templates, collects submissions, and provides searchable history. It supports 10 field types: Text, Email, Telephone, Number, Date, Select, Radio, Textarea, Checkbox, and Signature.

Use Operational Forms for standard restaurant paperwork and Custom Form Builder when the venue needs its own data-entry schema.

</details>

---

### Screen Builder

Configure every POS screen from a single settings page — button layout, split modes and limits, tip controls, hold timing, login methods, kiosk lock, receipt format, grid columns, display toggles, item sizing, and responsive presentation. Configuration is stored in named venue layout profiles rather than only in the current browser.

**Navigate to:** Settings > Screen Builder

<img src="../images/pos/production-demo-2026-08/prod-20260810-settings-screen-builder.png" alt="Production demo Screen Builder showing its active venue profile and 12 configurable screen tabs">

<details>
<summary><strong>Profiles, persistence, and runtime precedence</strong></summary>

- Create, save, and activate named layout profiles for the venue. Saving writes the profile through the POS settings API and updates the venue's active profile.
- Each screen consumes the active stored layout at runtime; Screen Builder is not a documentation-only preview.
- Register settings layer from **Base venue profile → Revenue Center profile → Station override**. The most specific configured value wins and an unset value inherits from the previous layer.
- The matching Phone, Landscape, Tablet, or Short-height variant is then used for responsive presentation fields.
- Upgrades preserve the historic behavior of two formerly display-only controls: profiles that have never explicitly set them continue to show **Custom Tip** and keep **Receipt Logo** off. The first explicit toggle in Screen Builder activates that control; the authorized Screen Builder receipt action can also activate **Receipt Logo**. After **Save changes**, the saved on/off value is enforced at runtime. This avoids silently changing a live terminal during an upgrade.

</details>

<details>
<summary><strong>12 Configurable Screens</strong></summary>

| Screen | Key Settings |
|--------|-------------|
| **Register** | Two button zones (drag-and-drop), check panel width, item display size, product grid columns, tile style and imagery, toolbar style, quick pay toggles, receipt settings |
| **KDS** | Columns, gap spacing, ticket card size, all-day counts, age alert thresholds, per-station colors |
| **Tables** | Columns, table button size, elapsed timer, revenue display, heat map |
| **Customer Display** | Show modifiers, unit price, font size, idle content (promos/logo/specials/blank), tax breakdown |
| **Menu Board** | Columns, font size, show prices, show images |
| **Drive-Thru** | Columns, card size, vehicle description, elapsed timer, timer warning and danger thresholds |
| **Bar Tabs** | Columns, card size, show total, automatic tab naming |
| **EOD** | Tip pool section, cash denominations, denomination columns |
| **Reports** | Chart height, labor section, end-of-day by terminal, card brand breakdown, receipt preview |
| **Orders** | Which columns appear, summary bar, default tab, page size |
| **Online Ordering** | Grid columns, tile imagery and density, search, assistant placement |
| **Appearance** | Default theme, accent colour, font scale, theme toggle, compact mode, high contrast |

</details>

<details>
<summary><strong>Device layouts — why a setting can look different on the floor</strong></summary>

Each screen has a **Base** layout plus four optional responsive variants: **Phone**, **Landscape**, **Tablet**, and **Short height**. A terminal automatically uses whichever one matches its screen size, falling back to Base when you have not customised that size.

This is what lets a phone show three product columns while a wide terminal shows six, without maintaining two separate menus. Device layouts change presentation only — never payments, permissions, or any operational rule.

That presentation-only restriction applies to the responsive variants, not the Base layout profile. Base and profile configuration also contains operational controls such as maximum tip percentage, allowed/default split modes, hold auto-send timing, receipt content, login-method visibility, and kiosk auto-lock.

**Short height** is worth knowing about: it is chosen by window *height*, not width. A laptop browser window with tabs and a bookmarks bar can be short enough to qualify even though it is very wide, so it can pick up the Short height layout rather than Base.

Because of that, the layout you are editing is not always the layout in front of you. The device tab that matches your current screen is marked **THIS DEVICE**, and if you are editing a different one, a note appears telling you which layout your screen is actually rendering, with a one-tap button to jump to it. If you change a setting and the screen does not change, check that banner first — you are almost certainly editing a different device size.

</details>

<details>
<summary><strong>Register Layout Builder</strong></summary>

The register screen has two configurable button zones:

- **Quick Pay Zone** — one-tap Cash and Credit buttons in the check panel footer. Enable one, both, or neither
- **Action Bar Zone** — Split, Transfer, Merge, Move, Discount, Hold, No Sale, Void Order, Payments — drag to reorder, toggle on/off, resize each (S/M/L)

**Check Panel Width:**

| Setting | Width on a large screen | Best for |
|---------|------------------------|----------|
| **Narrow** | ~340px | Maximum menu grid space |
| **Standard** | ~420px | Balanced — recommended |
| **Wide** | ~480px | Check-centric workflow, large item names |

All three narrow to around 300px on smaller screens so the menu grid stays usable — the setting controls how much room the check takes once there is room to give.

**Item Display Size:**

| Setting | Text size | Best for |
|---------|-----------|----------|
| **Compact** | Small (14px) | High item count, experienced staff |
| **Comfortable** | Medium (16px) | General use — recommended |
| **Spacious** | Large (18px) | Readability, accessibility, training |

**Operational controls that are easy to miss:**

- **Login Methods** — show or hide PIN, swipe-card, and QR login choices on the shared-terminal gate
- **Split Check** — enable Even, By Seat, By Item, and By Amount; choose the default tab; set 2–20 maximum splits; use the full-screen split board; allow fractional item splits; and show shared-item badges
- **Tip** — edit the suggested percentages, show or hide Custom Tip, and set the 10–50% maximum tip limit used for card authorization and checkout validation
- **Hold** — edit hold-time presets, show future date/time, show the hold badge, and choose whether held checks auto-send when due
- **Notifications** — show order-ready, table, stock, and clock events; enable sound; and cap the retained notification list

</details>

<details>
<summary><strong>Receipt & Bill</strong></summary>

Configure receipt output from **Settings > Screen Builder > Register > Receipt & Bill**.

**Paper Width** — controls thermal column count, PDF page width, and browser print max-width simultaneously:

| Width | Thermal cols | PDF width | Common hardware |
|-------|:---:|:---:|-----------------|
| **80mm** (default) | 42 | 80mm | Epson TM-T88, Star TSP143/TSP654, most desktop receipt printers |
| **58mm** | 30 | 58mm | Mobile printers (Star SM-S, Epson TM-P), small café countertops |
| **76mm** | 40 | 76mm | Impact/dot-matrix kitchen printers (Star SP700), wide legacy units |

80mm is the most common. Choose 58mm for mobile/handheld setups. 76mm is typically only used with older impact printers.

Toggle 14 receipt sections on/off:

| Section | Default |
|---------|:-------:|
| Header (venue name) | On |
| Address | On |
| Logo | Off |
| Items | On |
| Modifiers | On |
| Qty & unit price | On |
| Tax breakdown | On |
| Suggested gratuity | On |
| Tip line | On |
| Signature line | On |
| QR code | On |
| Barcode | Off |
| CC details | On |
| Footer message | On |

The **Logo** switch applies to all three receipt surfaces: the on-screen/browser receipt, generated PDF, and thermal ESC/POS output (a monochrome raster is used for thermal printers). When QR is enabled, choose **Tip link**, **Order details**, **Feedback**, or **Custom URL**. When Barcode is enabled, choose **Order ID**, **Order Number**, or **Payment ID**. The footer text is editable independently of the footer on/off switch.

</details>

---

### QR Code Login

Staff can scan a QR badge to log in — no PIN needed. Badges are HMAC-signed, venue-scoped, and revocable per employee. Print badges from **Settings > Staff Management** and assign to any staff member. Lost badges can be revoked instantly without affecting other credentials.

![Register with QR Login](assets/pos/01-register-categories.png)

---

### Hold/Send Kitchen Timing

Set a hold timer (5-60 minutes) on an order before sending to kitchen. Kitchen tickets auto-fire when the timer expires — server-authoritative, not client-poll. Servers use this for appetizer-first timing, bar-tab food holds, or coordinating with a reservation arrival.

![Hold/Send Timer](assets/pos/05-hold-send-timer.png)

---

### Split Check with Fractional Splits

Split a single item across multiple checks (1/2, 1/3, 1/4). Share badges show which items are shared across guests. Penny-conserving math ensures totals always balance — remainder cents go to the first split. Works alongside seat management and coursing.

![Split Check](assets/pos/06-split-check-modal.png)

---

### Notification Bell

Real-time alerts for new online orders, order-ready bumps, table timer alerts, and low stock warnings. Configurable per notification type with sound alerts. Bell icon in the top bar shows unread count — tap to expand the notification drawer without leaving the current screen.

---

### Bar Tab Name Capture

When a card is swiped for a bar tab, the cardholder name is automatically captured and used as the tab name. No manual typing needed. Configure automatic naming and the as-returned, Last/First, or First Last format in **Settings > Screen Builder > Bar Tabs**.

![Bar Tabs](assets/pos/19-bar-tabs.png)

---

### Training Mode

Isolated sandbox. Orders excluded from reports. Staff can practice without affecting live data.

<img src="../images/pos/settings_training_mode.png" alt="Training">

<details>
<summary><strong>Setup</strong></summary>

1. Enable training mode in **Settings > Venue** — toggle "Training Mode"
2. All orders created while training mode is active are tagged `[TRAINING]`
3. Training orders are excluded from sales reports, EOD, and payroll calculations
4. Disable training mode when done — real orders resume immediately

</details>

---

### Offline Mode (PWA)

Your restaurant never stops — even when the internet does. Synalux POS is a full Progressive Web App (PWA) that keeps running when your network drops. Staff can continue taking orders, accepting cash payments, clocking in and out, and browsing the menu without interruption. Everything is saved locally on the device and automatically syncs back to the cloud the moment connectivity returns — no manual steps, no lost orders.

When the network goes down, a red **"Offline"** badge appears in the top-right corner of the screen (visible in the screenshot below). The full menu stays available from cache, and the register works normally. When the connection comes back, the badge disappears and all queued data syncs silently in the background.

<img src="../images/pos/ipad_offline_mode.png" alt="Synalux POS Register in Offline Mode — red Offline badge visible in top-right corner, menu fully loaded from cache">

**What works offline:**

| Capability | How it works |
|---|---|
| **Orders** | Queue locally with idempotency keys — auto-sync on reconnect |
| **Cash payments** | Fully offline — queued and synced when network returns |
| **Staff clock in/out** | Shifts queue locally, synced to the server on reconnect |
| **Menu browsing** | Cached locally (24h TTL) so staff can ring items without network |
| **EOD summary** | Cached when online (4h TTL), shown from cache when offline with "cached as of" timestamp |
| **Reports** | Orders and payments cached — Sales, PMIX, Server, and Payment reports available offline |
| **PDF receipts** | Client-side PDF generation — no network needed |
| **Page rendering** | Service Worker precaches Register, KDS, Tables, and EOD pages so the app shell loads instantly |
| **Split checks** | Splits saved locally with client-side conservation check — applied when order syncs |

**What requires network (queued or degraded offline):**

| Capability | Offline behavior |
|---|---|
| **Card payments** | Payment record is queued locally — the actual charge (Stripe/Dejavoo) is processed when the connection returns |
| **Bar tab pre-authorization** | Queued as "authorized" — the hold is created on reconnect |
| **Real-time KDS updates** | Supabase Realtime subscription pauses — KDS falls back to polling when connection resumes |
| **Receipt email / SMS** | Requires Resend / Twilio API — PDF receipts still work offline (client-side generation) |

#### Sync Architecture

The offline sync engine handles the full lifecycle of queued orders and payments, with idempotency guarantees that prevent duplicate charges even across browser tabs, page reloads, and network retries.

**Phase 1 — Terminal goes offline:**

```
Staff places order ──► queueOfflineOrder()
                              |
                              v
                      +----------------+
                      | localStorage   |  idempotency keys
                      | offline_queue  |  + 48h TTL timestamps
                      +-------+--------+
                              |
Staff takes payment ──► queueOfflinePayment()
                              |  (carries orderIdempotencyKey
                              |   for order correlation)
                              v
                      +----------------+
                      | localStorage   |  payment linked to
                      | offline_queue  |  order via idem. key
                      +----------------+
```

**Phase 2 — Terminal reconnects:**

```
syncOfflineQueue() ──► processQueue(syncItem)
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
        Orders sync     Payments sync    Sweep route
        (first, by      (after orders)   (pending_offline
         insertion                        -> processor)
         order)
              |               |               |
              v               v               v
        +-----------+   +-----------+   +---------------+
        | Claim     |   | Resolve   |   | Forward to    |
        | table     |   | via claim |   | Stripe /      |
        | prevents  |   | table     |   | Dejavoo       |
        | duplicates|   | offline-N |   | Record losses |
        | (23505 =  |   | -> real   |   | in pos_       |
        | noop)     |   | UUID      |   | offline_losses|
        +-----------+   +-----------+   +---------------+
              |
              v
        +-------------------+
        | Emit synced event |---> Cart store remaps activeOrderId
        | + persist remap   |    (offline-N -> real UUID)
        | to localStorage   |---> Cross-tab: any tab can resolve
        +-------------------+
```

#### Idempotency — No Duplicate Charges

Every money-moving operation is replay-safe:

| Layer | Protection |
|-------|-----------|
| **Order creation** | Unpartitioned `pos_order_idempotency` claim table with `PRIMARY KEY (venue_id, idempotency_key)`. Two tabs replaying the same order both hit the claim — the second gets the existing order back, not a duplicate. |
| **Payment creation** | Every `pos_payments` insert carries an `idempotency_key` (caller-supplied or server-minted). `UNIQUE(venue_id, idempotency_key)` prevents duplicates. |
| **Card terminal** | CAS status transition (`authorized` → `capturing` → `captured`) — only one caller can claim the payment. Retries see "already captured" and get the success response. |
| **House account** | Charge route deduplicates via `pos_house_account_charges` table with `UNIQUE(venue_id, idempotency_key)`. Retry returns the original debit result. |
| **Gift card** | Balance deduction uses CAS (`WHERE balance_cents = {expected}`). A retry after successful deduction fails the CAS and returns 409. |
| **Processor calls** | Stripe has built-in idempotency. Dejavoo SPIn uses PNRef/invoice-based dedup. |

#### Multi-Tab Safety

Multiple browser tabs can be open on the same POS simultaneously. The sync engine handles this:

- **Queue reads from localStorage before every mutation** — tab B can't resurrect items tab A already synced
- **Queue item IDs use `crypto.randomUUID()`** — no sequential counter collisions across tabs
- **Order remap persisted to localStorage** — any tab can resolve an offline order ID to the real server UUID, even if a different tab performed the sync
- **Dropped-order detection persisted** — if an order was permanently rejected (e.g., menu item deleted while offline), any tab surfaces the terminal error instead of retrying forever

#### Error Handling

| Scenario | Behavior |
|----------|----------|
| **Transient error (5xx, timeout)** | Exponential backoff retry, capped at 30 seconds |
| **Deterministic rejection (400/422)** | Item dropped immediately from queue. Staff notified via toast with the order details for re-entry. |
| **Order rejected → payments orphaned** | Dependent payments cascade-dropped in the same pass — no orphaned retry loop |
| **Queue items older than 48 hours** | Automatically dropped with a staff notification on next load or sync |
| **Corrupt localStorage** | Malformed entries isolated and logged; well-formed siblings survive |
| **Card tap during sync race** | Auto-retry on 409 `ORDER_NOT_SYNCED` (4× with 1/2/3s backoff). Staff sees "Order is still syncing" only if all retries exhaust. |

#### Payment Resolution by Tender Type

When paying an order that was created offline, each tender type resolves the offline order ID:

| Tender | How it resolves |
|--------|----------------|
| **Cash, EBT, bar tab** | `createPayment` resolves via server-side claim table lookup using `orderIdempotencyKey` |
| **Card (terminal)** | `create-intent` resolves via claim table. Auto-retries 409 if order hasn't synced yet |
| **Card (manual entry)** | Resolved at tap time via persistent remap. Blocks with "still syncing" if unresolved |
| **Gift card** | Resolved at tap time. Blocks if unresolved to prevent debiting the card against a nonexistent order |
| **House account** | Blocks when both remap and idempotency key are unavailable. Key path resolves via claim table |
| **Split (cash/card)** | Same as single tender — each split payment resolves independently |

<details>
<summary><strong>Setup</strong></summary>

1. Open the POS in Chrome or Safari and add to home screen — installs as a PWA automatically
2. When network drops, a red "Offline" badge appears in the top-right corner with queue status
3. All orders and payments (cash and card) queue locally and auto-sync when connectivity returns
4. Card charges are processed through the venue's payment processor when the connection resumes — no staff intervention needed
5. Multi-tab: open on multiple devices — sync engine handles concurrent access safely

</details>

---

### Integrations

Stripe, Dejavoo (SPIn terminal), DoorDash Drive, Uber Direct, Uber Eats, Grubhub, QuickBooks, Xero, Gusto, ADP, OpenTable, Google Reserve, Yelp, Twilio (voice + WhatsApp + SMS), Resend (email), Forage (EBT), Deepgram (speech-to-text), ElevenLabs (text-to-speech), Gemini (AI ordering), Ollama (local AI).

The Settings page is a control surface, not proof that a provider is connected. A production screenshot is included only after the relevant processor/provider reports a connected state; the demo's disconnected integration cards are intentionally not shown.

<details>
<summary><strong>Setup</strong></summary>

1. Open **Settings > Integrations** and use the provider-specific connection flow. Some providers use OAuth, some use server-managed credentials, and payment terminals also require pairing/location setup
2. **Stripe** — configure the server-side Stripe credentials and Terminal Location, then pair supported readers; Tap to Pay additionally requires the supported native iPhone app/build
3. **DoorDash / Uber** — add API credentials for delivery dispatch and menu sync
4. **Twilio / SendGrid** — add keys for SMS order-ready notifications and email receipts
5. **QuickBooks / Xero** — connect via OAuth for automatic EOD GL journal sync

</details>

---

### Operational Forms

Cash Count, Void Auth, Tax-Exempt Cert, Catering BEO, Tip Declaration, Inventory Count, Time-Off, Purchase Order, Incident Log, Daily Specials, Prep List, Server Checkout.

<img src="../images/pos/production-demo-2026-08/prod-20260810-operational-forms.png" alt="Production demo Operational Forms with all 12 built-in restaurant forms">

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/backoffice/forms` to access all 12 pre-built operational forms (`/pos/forms` redirects there)
2. Forms auto-fill venue name, date, and staff info from the current session
3. Open a form, then print or download it; use `/pos/form-builder` only for custom templates and submissions

</details>

---

### Digital Menu Board

Configure layout, sections, and pricing display. Assign to any TV or display.

<img src="../images/pos/production-demo-2026-08/prod-20260810-menu-board.png" alt="Production demo Digital Menu Board with populated categories, items, and prices">

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/board` on any TV or large display
2. Configure columns, font size, prices, and images in **Settings > Screen Builder > Menu Board**. The board groups the active Menu Builder items by category
3. Prices and availability auto-sync from the menu builder

</details>

---

### Marketing & Campaigns

Email/SMS blasts, promo codes, audience segmentation, planned send times, and send history.

Marketing is documented without a production screenshot when the demo has no campaign records.

<details>
<summary><strong>Setup</strong></summary>

1. Open the **Marketing** page to create email or SMS campaigns
2. **Audience segmentation** — target a campaign by minimum orders, minimum spend, last-visit recency, and whether the contact has an email or phone. A live summary shows who the campaign will reach
3. **Planned send** — set a planned send time on a campaign; it's shown on the campaign card so staff know when to send it
4. Create promo codes with percentage or fixed discounts
5. Requires Twilio (SMS) or SendGrid (email) credentials in **Settings > Integrations**

</details>

---

### Customer Feedback

Post-visit surveys, an at-the-terminal NPS prompt, star ratings, comment review, and response templates.

Feedback is documented without a production screenshot when the demo has no submitted responses; a zero-response dashboard is not used as an example.

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/feedback` to view submitted customer surveys and the NPS dashboard
2. **On-terminal NPS capture** — enable **Auto-Prompt** in the Feedback settings and the payment-complete screen shows a 0–10 "how likely to recommend" prompt with an optional comment. Tapping a score records it immediately (non-blocking — it never holds up the close-out)
3. QR codes on receipts link to the survey form
4. Star ratings, NPS, and comments are aggregated per server and per time period

</details>

---

<a name="printers--cash-drawer"></a>

### Printers & Cash Drawer

Thermal receipt printers, kitchen ticket printers, and cash drawers. Network (LAN), USB, and Bluetooth. Epson, Star, and generic ESC/POS. No drivers needed — the browser handles USB and Bluetooth natively.

The demo has configured printers but no explicit category routing rules, so its settings page is not used as a screenshot. With no routing rules, order items continue to route by each item's configured `kds_station`; explicit rules override that default for selected categories.

<details>
<summary><strong>Supported Hardware</strong></summary>

| Type | Protocol | Connection | Examples |
|------|----------|------------|----------|
| Generic ESC/POS | Raw TCP port 9100 | Network, USB, Bluetooth | Most thermal printers |
| Epson | ePOS (SOAP/HTTP) | Network | TM-T88, TM-T20, TM-m30 |
| Star | WebPRNT (HTTP) | Network | TSP143, TSP654, mC-Print3 |
| Zebra | ZPL (HTTP) | Network | ZD421, ZD620, GK420 |

Auto-detection: the system reads the **Model** field and routes accordingly — if it contains "star" it uses Star WebPRNT, "epson" uses Epson ePOS, anything else uses generic ESC/POS (raw TCP port 9100).

</details>

<details>
<summary><strong>Network Printer Setup (Recommended)</strong></summary>

Best for restaurants — printer connects to the same LAN as the POS terminal.

1. Assign a **static IP** to the printer (check printer's network config sheet — hold Feed button during power-on on most models)
2. Go to **Settings > Printers & KDS**
3. Click **Add Printer**
4. Enter a friendly **Name** (e.g. "Front Receipt", "Kitchen 1")
5. Enter the **Model** — include "star" or "epson" in this field for correct protocol detection
6. Select a **Station**: receipt, kitchen, bar, expo, or label
7. Select **Network (LAN)** and enter the printer's **IP address**
8. Click **Add Printer**, then **Test Print** to verify

**Network ports used:**

| Protocol | Port/Endpoint |
|----------|---------------|
| Generic ESC/POS | TCP `9100` (raw socket) |
| Epson ePOS | HTTP `POST /cgi-bin/epos/service.cgi` |
| Star WebPRNT | HTTP `POST /StarWebPRNT/SendMessage` |
| Zebra ZPL | HTTP `POST /cgi-bin/print` |

**Cloud deployment (Vercel) + local printer:** When the POS is deployed to Vercel but the printer is on a local network, the system automatically relays print jobs via Supabase Realtime broadcast. A local relay agent on the same network picks up the job and forwards to the printer — no VPN or port forwarding needed.

**Printer auto-discovery:** If a local relay is running, discovered printers appear at the top of the settings page. Click **Configure** to auto-fill name, IP, and model.

</details>

<details>
<summary><strong>Cloud Print Relay (Required for Cloud → Local Printing)</strong></summary>

If your POS is hosted in the cloud (pos.synalux.ai) and your printers are on a local network (192.168.x.x, 10.x.x.x), install the relay app on any computer at your venue.

> **iOS / iPad users:** No relay needed — the iOS app prints directly to printers on your local network via native TCP. Just add the printer in Settings > Printers & KDS and tap Test Print.

**Download and install:**

| Platform | Download | Size |
|----------|----------|------|
| **macOS** | [Download .dmg](https://github.com/dcostenco/synalux-local-relay/releases/latest) | 5 MB |
| **Windows** | [Download .msi](https://github.com/dcostenco/synalux-local-relay/releases/latest) | 4 MB |

**Setup (one time):**

1. Download and install the relay app
2. The app runs invisibly in the system tray — no window needed
3. Auto-starts on boot, auto-updates, auto-reconnects
4. Go to POS → **Settings > Printers & KDS** → click **Test Print** on any printer

No Node.js, no command line, no configuration files, no secrets to manage.

**How it works:** The POS writes print jobs to a database queue. The relay app polls the queue, picks up jobs for your venue, and forwards them to your local printers via TCP (port 9100) or HTTP (Epson ePOS / Star WebPRNT). Failed jobs retry automatically up to 3 times.

**Troubleshooting:**

| Symptom | Fix |
|---------|-----|
| Nothing prints after Test Print | Make sure the relay app is running (check system tray) |
| Relay connected but printer doesn't respond | Verify printer IP in POS settings. Run `ping <printer-ip>` from the relay computer |
| Relay app won't start | Check internet connection — the app needs access to Supabase |

</details>

<details>
<summary><strong>USB Printer Setup</strong></summary>

Uses the Web Serial API — no drivers needed. Chrome and Edge only.

1. Connect the printer via USB to the POS terminal
2. Go to **Settings > Printers & KDS** > **Add Printer**
3. Enter Name, Model, Station
4. Select **USB (Browser Native)**
5. Click **Add Printer**
6. Click **Test Print** — the browser shows a serial port picker, select your printer
7. The browser remembers the selection for future prints

**Requirements:** Chrome or Edge. HTTPS or localhost. The first print requires a user click (browser security).

</details>

<details>
<summary><strong>Bluetooth Printer Setup</strong></summary>

Uses the Web Bluetooth API. Useful for mobile POS terminals.

1. Put the printer in Bluetooth pairing mode
2. Go to **Settings > Printers & KDS** > **Add Printer**
3. Enter Name, Model, Station
4. Select **Bluetooth (Browser Native)**
5. Click **Add Printer**
6. Click **Test Print** — the browser shows a Bluetooth device picker, select your printer

**Requirements:** Chrome browser. HTTPS or localhost. Data is chunked into 512-byte segments (Bluetooth LE limitation).

</details>

<details>
<summary><strong>Cash Drawer Setup</strong></summary>

Cash drawers connect to the receipt printer via an **RJ-12 cable** (the "DK" port on the back of most thermal printers). The POS sends an ESC/POS drawer-kick command through the printer — no separate USB connection needed.

1. Plug the drawer's RJ-12 cable into the printer's **DK port** (labeled "DK" or with a drawer icon)
2. In **Settings > Printers & KDS**, ensure your receipt printer is configured with station = **receipt**
3. An **Open Cash Drawer** button appears next to Test Print — click it to kick the drawer
4. The drawer also kicks automatically after a cash payment, and on **No Sale** — the No Sale action physically opens the drawer (to make change) and records a no-sale audit event

**Troubleshooting:**

| Symptom | Fix |
|---------|-----|
| Drawer doesn't open | Check RJ-12 is in the DK port, not the phone/network port |
| Opens intermittently | Replace RJ-12 cable — these are fragile |
| Wrong drawer opens | Check DK1 vs DK2 port on the printer |
| "Open Cash Drawer" not visible | Printer must be assigned to the **receipt** station |

</details>

<details>
<summary><strong>KDS Routing (Multi-Printer)</strong></summary>

Route menu categories to specific printer stations so bar items print at the bar, food items print in the kitchen, etc.

1. In **Settings > Printers & KDS**, scroll to **KDS Routing**
2. Click **Add Route**
3. Select a **menu category** (e.g. "Appetizers", "Drinks")
4. Select a **station** (kitchen, bar, expo)
5. Set **copies** (1–3)
6. Click **Add**

When an order is sent to kitchen, items are split by category and routed to the correct station.

</details>

<details>
<summary><strong>Troubleshooting</strong></summary>

| Issue | Steps |
|-------|-------|
| Network printer not responding | 1. Ping the IP: `ping 192.168.1.100`. 2. Check port — **Mac/Linux:** `nc -zv 192.168.1.100 9100` / **Windows:** `Test-NetConnection 192.168.1.100 -Port 9100` (PowerShell). 3. Ensure port 9100 is not blocked by firewall. 4. Verify static IP (DHCP lease may have expired). |
| USB "No port selected" | Ensure Chrome/Edge, HTTPS or localhost. Try unplugging and reconnecting USB. Check `chrome://device-log`. |
| Print goes to wrong printer | Verify each printer has the correct **station** and check KDS routing rules. |

</details>

---

### Label Printer

ZPL-compatible (Zebra, Brother). Price/SKU/prep labels from any menu or inventory item.

<img src="../images/pos/settings_label_printer.png" alt="Label Printer">

<details>
<summary><strong>Setup</strong></summary>

1. Add your Zebra or Brother printer IP in **Settings > Printers**
2. Tap the label icon on any menu item or inventory item to print a ZPL label
3. Labels include item name, price, SKU, barcode, and expiry date

</details>

---

### Equipment Tracking

Device registry with serial numbers, warranty, maintenance schedule, and depreciation.

<img src="../images/pos/settings_equipment.png" alt="Equipment">

<details>
<summary><strong>Setup</strong></summary>

1. Add devices in the equipment registry with serial number, purchase date, and warranty info
2. Set maintenance schedules — the system alerts when service is due
3. Track depreciation for accounting purposes

</details>

---

### Manager Mobile

iPhone access to reports, KPIs, and quick actions — same data as the desktop, optimized for mobile.

<img src="../images/pos/iphone_02_reports.png" alt="Manager Mobile — Reports">

<details>
<summary><strong>Setup</strong></summary>

1. Open `/pos/reports` on any iPhone or mobile browser
2. Pin to home screen for quick access
3. Live KPIs: today's sales, open checks, labor %, voids, and average ticket size

<img src="../images/pos/iphone_01_dashboard.png" alt="Manager Dashboard">

</details>

---

<a name="security--pci-compliance"></a>

### Security & PCI Compliance

Synalux POS minimizes your PCI-DSS scope to the lowest possible levels:

| Scenario | PCI Level | How |
|---|---|---|
| **In-person card payments** | SAQ C / P2PE | Stripe Terminal (WisePOS E, Reader S700) — card data never touches your tablet, network, or servers |
| **Online ordering checkout** | SAQ A | Stripe Elements iframe — your server handles only `PaymentIntent` IDs, never card data |
| **Offline CC Vault (OO fallback)** | SAQ A-EP | Client-side WebCrypto RSA-OAEP encryption — server stores encrypted blob, never decrypts |

**GDPR Region Routing:** Venues in EU/EEA countries automatically use the EU database region. Region is resolved from country code at workspace creation and cached per venue. US and EU deployments share the same codebase — region routing is transparent to the frontend.

**Data privacy:** Built-in CCPA and GDPR deletion workflows. Customer data purge available in Settings. Minor labor law compliance with age-gated access controls.

---

## 26 languages

English, Spanish, French, Chinese, Arabic, Romanian, Portuguese, German, Italian, Japanese, Korean, Vietnamese, Russian, Ukrainian, Polish, Turkish, Dutch, Swedish, Hebrew, Thai, Hindi, Indonesian, Malay, Filipino, Greek, Bulgarian. Arabic and Hebrew use right-to-left layout support.

---

## Developer integration setup guide

<details>
<summary><strong>Environment and provider reference</strong></summary>

Integration setup varies by provider: OAuth connections are completed through their connect flow, server-managed services use deployment credentials, and terminal providers also require device/location setup. **Settings > Integrations** exposes the applicable workflow; a card appearing there does not by itself mean the provider is connected.

| Integration | Env var | What activates |
|---|---|---|
| **Stripe** (card payments) | `STRIPE_SECRET_KEY` | Card tap/chip/swipe, Tap-to-Pay on iPhone, online payments |
| **DoorDash Drive** (delivery dispatch) | `DOORDASH_DEVELOPER_ID`, `DOORDASH_KEY_ID`, `DOORDASH_SIGNING_SECRET` | 3PD delivery delegation, menu sync |
| **Uber Direct** (delivery dispatch) | `UBER_CLIENT_ID`, `UBER_CLIENT_SECRET` | 3PD delivery delegation, menu sync |
| **DoorDash / Uber Eats / Grubhub** (marketplace) | Webhook URL | Inbound 3PD orders on KDS with purple badge |
| **Gemini** (dish photos) | `GEMINI_API_KEY` | AI-generated menu item images. Without it, items fall back to emoji |
| **SendGrid** (email) | `SENDGRID_API_KEY` | Email receipts, order confirmations |
| **Twilio** (SMS) | `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` | SMS receipts, order-ready notifications |
| **Google Reserve / OpenTable / Yelp** | Webhook URL | Auto-created reservations |
| **QuickBooks / Xero** | `QUICKBOOKS_ACCESS_TOKEN` or `XERO_ACCESS_TOKEN` | EOD GL journal auto-sync |
| **Forage** (EBT/SNAP) | `FORAGE_API_KEY` | Eligible item flagging. EBT payment authorization is in implementation |
| **Dwolla / Stripe Treasury** | `DWOLLA_API_KEY` or `STRIPE_TREASURY_KEY` | ACH payroll direct deposit |
| **Ollama** (local AI) | `NEXT_PUBLIC_LOCAL_LLM_URL` | Natural language order parsing (local, no cloud) |
| **Prism MCP** (AI memory) | `PRISM_MCP_URL` | Per-staff and per-customer AI memory and context |
| **Apple / Google Wallet** | Pass Type ID + signing cert | Loyalty "Add to Wallet" |
| **Zebra / Brother** (labels) | Printer IP in Settings | ZPL price/SKU/prep labels |

**Required env vars:** `NEXT_PUBLIC_POS_SUPABASE_URL`, `NEXT_PUBLIC_POS_SUPABASE_ANON_KEY`, `POS_SUPABASE_SERVICE_ROLE_KEY`

</details>

---

## License

BUSL-1.1 — see [`LICENSE`](../LICENSE).
