# Clinical Workspace Guide

Synalux brings SOAP notes, review queues, treatment-plan records, goals, FBA/BIP drafts, and electronic-signature status into a role-controlled clinical workspace. Available pages and actions depend on the workspace configuration and the signed-in user's permissions.

Clinicians remain responsible for reviewing every record, obtaining required consent, and meeting professional, payer, and organizational requirements.

## SOAP note workspace

The SOAP workspace combines source observations with structured Subjective, Objective, Assessment, and Plan sections.

### Start a draft

1. Open the SOAP workspace and select the patient.
2. Enter observations in the source-text area or use dictation when the browser makes the listening control available.
3. Use **Fetch Session Data** when relevant session context is available.
4. Select the appropriate template.
5. Select **Generate** to create a structured draft from the supplied text and context.
6. Review and edit every section before saving or submitting it.

**Clone Previous Note** can provide a starting point when a prior note exists. Confirm that all copied details still apply; do not carry forward outdated findings or plans.

### Dictation

Select **Start Dictation** to begin and **Stop Dictation** to finish. In the current SOAP workspace, speech recognition runs through the local WASM Whisper worker shown on the screen; the audio used for this dictation path is processed in the active browser. Confirm recording consent before dictating. Browser, microphone, worker, and model availability can vary, so use typed entry if dictation does not start or reports an error.

Dictated or generated content is a draft. Verify patient identity, dates, observations, measurements, interventions, and plans before the text becomes part of the record.

<details>
<summary>View the current SOAP dictation workspace</summary>

![Synalux SOAP workspace with patient selection, source text, dictation, template, and structured note controls](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/03_voice_dictation.png)

</details>

## Clinical note review

The Notes page organizes notes by workflow status and provides the actions available to the signed-in user.

The current review path is:

`Draft → Submitted → Co-Signed → Finalized`

1. Save an incomplete note as a draft.
2. Submit it for review when the content is ready.
3. A different authorized clinician reviews and co-signs the submitted note. The author cannot co-sign their own note.
4. Finalize the co-signed note only after required corrections and signatures are complete.

Finalized notes are locked through the application workflow. Confirm the correct patient and encounter before finalizing.

<details>
<summary>View a structured SOAP note</summary>

![Synalux structured SOAP note with clinical sections and review actions](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/04_soap_note.png)

</details>

## FBA and BIP drafts

The guided FBA/BIP workspace separates the workflow into three steps:

1. **FBA:** record the target behavior, baseline information, antecedents, consequences, and assessment details.
2. **BIP:** draft the hypothesized function, prevention strategies, replacement behavior, teaching plan, response strategies, caregiver involvement, and safety information.
3. **Review:** review the combined content and select **Save BIP as Draft**.

Saving creates a draft for review; it does not approve the plan. An authorized clinician must individualize and review the plan before implementation.

<details>
<summary>View the current FBA/BIP builder</summary>

![Synalux FBA and BIP builder with guided assessment, intervention, and review steps](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/06_bip_builder.png)

</details>

## Treatment plans and goals

The Clinical workspace's **Treatment Plans** area lists plan documents and associated goals available to the current workspace. From there, authorized users can open goal records or start the FBA/BIP builder.

Review plan dates, status, goals, and supporting documentation before using a plan in care. A visible draft or generated document is not evidence of clinical approval.

## Electronic signatures

When electronic signatures are enabled and configured for the workspace, the E-Signature center shows document requests and their current status. The exact sending controls depend on the connected signature service and the user's permissions.

Before sending a request:

1. Confirm the document and patient or client context.
2. Verify every signer and email address.
3. Review the document and signing order.
4. Send the request using the controls available in the E-Signature center.
5. Return to the center to confirm its status and associate the completed document with the intended record according to your organization's process.

Do not assume that saving a treatment plan automatically sends a signature request.

<details>
<summary>View the current E-Signature center</summary>

![Synalux E-Signature center with document-request status and actions](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/09_esignature.png)

</details>

## Safe use checklist

- Confirm the active patient or client before entering or copying content.
- Review dictated, cloned, or generated text before saving it.
- Keep notes in draft status until they are complete.
- Use the review and co-sign workflow required by your organization.
- Verify signature-request recipients before sending.
- Treat generated drafts as decision support, not as an automatic clinical conclusion.
- Report missing permissions or unavailable configured services to a workspace administrator.

Related guides: [Clinical Notes and Documentation](./clinical_notes_documentation.md) · [Applied Behavior Analysis](./applied_behavior_analysis_aba.md) · [Security and Compliance](./security_compliance.md)
