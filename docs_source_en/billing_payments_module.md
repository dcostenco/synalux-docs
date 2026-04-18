# Billing & Payments Module

The Synalux platform's Billing & Payments Module leverages Stripe Connect to provide each practice with an independent payment processing account managed by the workspace administrator. This ensures secure and efficient financial management tailored to each practice's specific needs.

## Per-Practice Billing Configuration

### Stripe Connect
Each workspace is equipped with its own dedicated Stripe Connect account (`acct_xxx`), ensuring seamless and isolated payment processing for every practice.

### Admin Linked
The Stripe account ownership is directly linked to the designated workspace administrator, facilitating easy management and control over financial transactions.

### Fee Schedules
Practices can define custom fee schedules that include standard rates, insurance billing, Medicare payments, and self-pay arrangements, allowing flexible pricing strategies.

### Payment Methods
A variety of payment methods are supported, including credit cards, ACH/bank transfers, checks, and cash. Practices have the flexibility to configure these options according to their requirements.

### Auto-Posting
The module automates payment posting, receipt generation, and monthly statement creation, streamlining financial management processes and saving time for administrators.

### Tax Configuration
Practices can set up per-practice tax rates along with necessary identifiers like NPI/EIN for accurate 1099 reporting, ensuring compliance with tax regulations.

## Multi-Country & Multi-Currency

The Billing & Payments Module supports multiple countries and currencies, offering tiered pricing to accommodate different business sizes and needs:

| Country     | Currency   | Standard | Advanced | Enterprise |
|-------------|------------|----------|----------|------------|
| 🇺🇸 USA      | USD        | $19/mo   | $49/mo   | $99/mo     |
| 🇨🇦 Canada   | CAD        | C$25/mo  | C$65/mo  | C$129/mo   |
| 🇬🇧 UK       | GBP        | £15/mo   | £39/mo   | £79/mo     |
| 🇩🇪🇫🇷 EU     | EUR        | €18/mo   | €45/mo   | €89/mo     |
| 🇦🇺 Australia| AUD        | A$29/mo  | A$75/mo  | A$149/mo   |
| 🇳🇿 New Zealand| NZD      | NZ$32/mo | NZ$82/mo | NZ$159/mo  |

## Volume Discounts

To incentivize growth, Synalux offers volume discounts based on the number of clients:

- **100+ Clients:** 10% off per-seat price
- **500+ Clients:** 20% off per-seat price
- **1,000+ Clients:** 30% off per-seat price

Additionally, practices that opt for annual billing receive an extra 20% discount, stacking with volume discounts but capped at a maximum of 45%.

## Payment Failure Lifecycle

The payment failure lifecycle is designed to maintain service continuity while ensuring financial health:

- **Payment Failed:** Triggers `past_due` status with a warning banner.
- **2nd Retry Failure:** Urgent warning displayed.
- **3rd Retry Failure:** Automatic downgrade to the Free tier.
- **Stripe Subscription Deleted:** Plan set to 'free', and subscription cleared.

## Platform Admin Overrides

Synalux platform administrators have powerful tools at their disposal:

- Set any user to an unlimited trial on any plan.
- Override users are immune to Stripe webhook downgrades.
- Administrators view 🟢/🔴 indicators for payment status.
- Comprehensive audit trails document who set overrides, when, and why.

## Revenue Cycle Management

Efficiently manage the revenue cycle with features that track:

- Insurance claim lifecycle from draft to acceptance or denial.
- ERA/EOB electronic remittance processing.
- Denial management with deadline tracking.
- Prior authorization workflow.
- Aging reports categorized into 30/60/90/120-day buckets.

## Patient Payments

Facilitate patient payments through:

- A "Pay Now" option in the patient portal that redirects to Stripe Checkout.
- Acceptance of partial and custom payment amounts.
- Setup of payment plans using Stripe recurring subscriptions.
- Generation and download of receipts.
- Processing of refunds efficiently.

## Insurance Claims

Streamline insurance claim processes with:

- Electronic submission of claims (837P).
- Real-time eligibility verification.
- Coordination of Benefits (COB) handling.
- Tracking of Explanation of Benefits (EOB).
- Management of appeals using customizable letter templates.

## Automatic Tax Collection

Ensure compliance with automatic tax calculations enabled per-country for VAT, GST, HST, and PST. The system adheres to Canadian multi-province tax rules, applying federal GST along with provincial PST/HST as necessary.