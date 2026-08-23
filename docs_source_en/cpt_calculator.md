# Timed-service unit checks

Synalux uses timed-service calculations during the Billing claim-scrub workflow. The check helps staff compare documented treatment minutes with billed units before submission; it does not replace payer guidance or professional billing review.

## Run the check

1. Open **Billing** and locate the claim or billing entries to review.
2. Confirm the service code, documented duration, billed units, diagnosis, provider NPI, and authorization information.
3. Choose **Scrub now**.
4. Review every error and warning. Correct the underlying record and run the scrub again.
5. Submit only after the responsible clinician or biller confirms that the claim matches the documentation and payer rules.

The scrub can flag conditions such as:

- missing service or CPT code;
- fewer than eight documented minutes for a timed unit;
- billed units above the amount supported by the recorded minutes;
- possible underbilling when the recorded minutes support more units;
- missing diagnosis or provider NPI;
- expired, low, or exceeded authorization units.

## Example

Twenty total timed minutes support one unit under the calculator’s current eight-minute-rule boundaries. A claim that bills three timed units for those 20 minutes is flagged for correction.

When several timed services contribute to a session, do not calculate each short remainder in isolation. Confirm the combined-time and allocation rules required by the payer before changing the claim.

## Responsibility and limits

Payer rules, coding guidance, contracts, and documentation requirements can change. A clean scrub means the entered data passed the product’s current checks; it is not a coverage determination, legal opinion, reimbursement guarantee, or promise of additional revenue. Keep the clinical record and claim consistent, and escalate uncertain coding decisions to a qualified biller or payer.
