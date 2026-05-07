# 🧮 CPT Calculator (Medicare-Correct)

Built-in CPT code calculator that catches the **Medicare 8-minute rule** + **remainder rollover** most practices miss. Real underbilling fix shipped 2026 — this is one of the highest-impact billing tools in the platform.

---

## ⚠️ Why It Matters
Most practice-management tools implement the 8-minute rule but miss the remainder-rollover rule that Medicare specifically requires. Result: practices systematically under-code time-based services, leaving real revenue on the table.

Synalux's CPT calculator implements both:
*   **8-minute rule** — minimum 8 minutes of one-on-one time per billable unit of time-based codes (97530, 97110, 97140, etc.).
*   **Remainder rollover** — when the total minutes spans multiple service types, leftover minutes from one service can roll over to fill the 8-minute floor of another. Most software doesn't compute this.

---

## 🧪 Worked Example
Session has:
*   23 minutes of therapeutic exercise (97110)
*   12 minutes of manual therapy (97140)
*   3 minutes of neuromuscular re-education (97112)

Naive calculation: 97110=2 units, 97140=1 unit, 97112=0 units → **3 units billed**.

Synalux's correct calculation: rollover the 3-min orphan to a service that qualifies → **3 units, with the third unit allocated to the highest-RVU service** (97110). Same total but billed correctly per Medicare guidance.

For a practice doing 1000 sessions/month, this fix typically recovers 4-8% of billable time = **5-figure annual revenue restoration**.

---

## 🏗️ Architecture
*   `services/cpt-calculator.ts` — pure function; no I/O.
*   `POST /api/v1/billing/cpt-calculate` — server endpoint that takes session minutes + service breakdown, returns the unit allocation with explanation.
*   Drives the SOAP note's billing block + the [Billing & Insurance](billing_payments_module.md) charge entry.

---

## ⚖️ Compliance
*   Audit log captures every calculation with input + output + timestamp — defensible if questioned by an audit.
*   Configuration locked to Medicare's published rules; can't be overridden per-workspace (intentional — wrong overrides cause fraud risk).

---

## 💳 Plans
Available on **Standard+**.

[See full pricing →](https://synalux.ai/pricing)
