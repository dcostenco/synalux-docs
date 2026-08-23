# Applied Behavior Analysis (ABA)

Synalux brings session work, data collection, assessments, goals, behavior plans, progress graphs, clinical notes, staff oversight, authorizations, and billing into one role-controlled workspace.

This guide describes the controls available in the current customer application. Your organization decides which workflows, assessment content, billing rules, and roles to use.

## Start with the daily workflow

For a typical clinical session:

1. Open **Sessions** and select or create the patient session.
2. Use the session workspace to record skill trials, behavior counts, duration, ABC observations, or task-analysis steps.
3. If the visit requires electronic verification, collect the required location, PIN, or caregiver signature before completing it.
4. Open **Notes** to create the session note, link relevant goals, and submit it for review when ready.
5. Review progress in **Graphs** and update goals or curriculum targets only after clinical review.

Available controls depend on the user’s role and workspace configuration.

## Sessions and data collection

The session workspace is designed for touch entry on desktop, tablet, and phone. It includes:

- skill-trial recording with response and prompt information;
- behavior frequency counters;
- duration timers;
- ABC entries for antecedent, behavior, and consequence;
- task-analysis steps;
- session summary and completion controls.

The separate **Data Collection** page can record discrete, duration, interval, and task-analysis data against the selected patient and target.

### Electronic visit verification

When electronic visit verification is enabled for the workflow, the completion form can collect:

- browser-provided GPS location;
- a caregiver or parent signature;
- a verification PIN;
- completion metadata and timestamps.

The browser must have location permission for GPS capture. Synalux records the values supplied through the form; your organization remains responsible for deciding which verification fields and payer rules apply.

## Assessments

Open **Assessments** to start, resume, review, or complete an assessment session.

The current assessment workflow supports:

- workspace-configured and custom assessment templates;
- per-item scoring grouped by domain;
- barriers, readiness, and narrative notes when those sections are part of the template;
- historical assessment sessions;
- report generation from the recorded assessment;
- starting an assessment with a prior completion date when appropriate.

Workspace administrators can create a custom template with a name, type, description, milestone count, domains, and items. Items can also be imported from a CSV file using the columns `domain,code,label,description`.

> Import only material your organization is licensed or otherwise authorized to use. Synalux does not grant rights to third-party assessment instruments.

The **Adaptive Assessment Log** stores scores and notes from externally administered instruments. It is a record repository; it does not administer or reproduce those instruments.

## Goals

Open **Goals** to maintain reusable goal templates and patient goals.

Goal templates can include:

- title and operational description;
- domain and goal type;
- baseline and mastery criteria;
- measurement method;
- active or archived status.

Use search and filters to find a template, then assign it to a patient when it fits the treatment plan. Assigned goals can be tracked by patient, status, and current progress.

## FBA and BIP drafts

Open **FBA/BIP** to use the guided three-step workspace:

1. Record the functional behavior assessment information, target behavior, baseline details, and ABC observations.
2. Draft the behavior intervention plan, including hypothesized function, prevention strategies, replacement behavior, teaching and consequence strategies, caregiver involvement, and safety information.
3. Review the combined draft and save it.

The builder supports documentation and clinical review; it does not replace an individualized assessment or professional judgment. An authorized clinician should review the plan before implementation.

## Curriculum and targets

Open **Curriculum** to organize domains, subdomains, and targets. You can:

- add domains, subdomains, and targets;
- set target status, mastery threshold, prompt level, and optional stimulus or distractor image links;
- search and filter targets;
- edit target status and criteria;
- print the current curriculum view.

The page can display a stored mastery prediction when prediction data already exists for a target. Its insights panel also highlights conditions such as near-mastery, slow progress, or a mastered target based on recorded values. Treat these displays as decision support, not as an automatic clinical decision or a newly generated treatment recommendation.

## Graphs

Open **Graphs**, choose a patient and target, and review the recorded data over time. The current graph workspace provides:

- a line chart of recorded values;
- a configurable mastery reference criterion;
- deterministic trend and aim lines;
- a trend summary based on the selected data;
- a mastery-rule result when enough points exist.

Trend summaries and mastery results are calculated from the displayed data. Review the underlying points and clinical context before changing a program.

## Clinical notes

Open **Notes** to create and manage SOAP-style session notes.

### Create and submit a note

1. Select **New SOAP Note**.
2. Choose the patient and, when useful, a configured note template.
3. Enter the session date, duration, note type, and Subjective, Objective, Assessment, and Plan sections.
4. Optionally link treatment-plan goals.
5. Save the note as a draft.
6. Open the draft and select **Submit for review** when it is ready.

The review workflow is:

`Draft → Submitted → Co-Signed → Finalized`

A note author cannot co-sign their own submitted note. A different authorized clinician must co-sign it before it can be finalized. Finalization locks the note through the application workflow.

### Dictation and assisted drafting

The SOAP workspace also offers live dictation when the browser and configured speech service support it. Staff can type or dictate raw observations, load selected-patient context, and request a structured draft. The result remains editable and must be reviewed for accuracy before it is used or signed.

Do not assume every browser supports the same speech path. If the listening control reports a warning or does not start, type the observations and contact your workspace administrator.

## Staff, credentials, training, and supervision

Open **Staff** to review the staff directory and switch among **Credentials**, **Training**, and **Supervision**.

### Credentials

Authorized users can add or edit a credential with its type, number, issuing authority, expiration date, and staff member. The credentials view shows expired credentials and credentials expiring within 30 days, with additional countdown states for later expiration dates.

### Training

The Training tab lists assigned training records and can filter overdue items. Training assignment and configuration may be managed elsewhere by your organization; the current Staff tab is primarily a tracker.

### Supervision

Authorized users can log or edit a supervision session with the supervisee, date, duration, supervision type, topics, and feedback. Pending records can be reviewed and approved in the Supervision tab.

## Authorizations and billing

Use **Authorizations** to maintain authorization periods, approved units or hours, utilization, renewal status, and exported records. Confirm payer-specific units, dates, and service rules before relying on remaining-balance displays.

Use **Billing** for the configured claim, eligibility, payment, and reporting workflows available to your workspace. Billing codes, modifiers, clearinghouse connectivity, and submission controls depend on organization and payer configuration. A code appearing in the system does not by itself establish coverage or reimbursement.

## Offline collection and synchronization

Supported clinical mutations can be queued when the browser loses connectivity and retried after connection returns. The local queue is encrypted, bounded, and time-limited.

For field use:

1. Sign in and open the patient and session while connected whenever possible.
2. Watch the application’s offline and queue status.
3. Continue only while the application confirms that entries are being queued.
4. Reconnect before the queue reaches its limit.
5. Wait for synchronization to finish, then reopen the session and verify the expected records before submission or billing.

Do not clear browser storage, sign out, or change devices while unsynchronized work remains. Offline availability can vary by action; a visible page alone does not prove that a particular save was queued.

## Roles, privacy, and clinical responsibility

- Access is controlled by workspace membership and assigned permissions.
- Patient and clinical records remain scoped to the active workspace and authorized users.
- Audit and application records support review, but customers must configure access, retention, consent, and payer procedures for their organization.
- Automated summaries, stored predictions, and assisted drafts require professional review.
- Synalux does not replace clinical judgment, credentialing requirements, payer policy, or applicable law.

## Getting started

1. Ask a workspace administrator to invite staff and assign appropriate roles.
2. Add or verify patients, coverage, diagnoses, and required consents.
3. Configure the assessment, goal, curriculum, note, authorization, and billing records your organization uses.
4. Run a supervised test session before field use.
5. Confirm data collection, EVV, note review, graphing, and billing handoffs with your organization’s policies.
6. For offline work, test disconnection and successful resynchronization with non-production training data first.

For help, contact [support@synalux.ai](mailto:support@synalux.ai).
