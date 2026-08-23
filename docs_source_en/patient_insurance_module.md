# Patient Insurance

Patient insurance information is split between the patient chart, Billing, and Authorizations so each task remains focused.

## Policy records

Open a patient chart and select **Insurance** to add and review policy details. A policy can include:

- Payer and plan name
- Member and group IDs
- Copay
- Subscriber name and relationship
- Effective and termination dates
- Notes

The first policy recorded for a patient becomes the primary policy in the current workflow. The chart displays the primary payer and policy details for quick reference.

## Eligibility check

Eligibility is a staff-initiated action:

1. Open **Billing**.
2. Select **Eligibility Check**.
3. Choose the patient and payer.
4. Run the check.

When a clearinghouse is configured, the result can show active/inactive coverage, payer, group, member ID, and copay information returned by that connection. If no clearinghouse is configured, Synalux reports that the check is unavailable rather than treating stored policy data as verified coverage.

## Claims and authorizations

Use **Billing** to review claims, denials, payments, and configured electronic claim submission. Use **Authorizations** to create and manage authorization numbers, service types, approved units, date ranges, utilization, renewals, and CSV export.

The current customer screens do not automatically resubmit denied claims or generate payer appeal letters from the patient Insurance tab.
