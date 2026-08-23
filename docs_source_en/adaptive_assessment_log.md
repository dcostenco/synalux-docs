# Adaptive Assessment Log

The Adaptive Assessment Log records results from standardized assessments that a qualified clinician administered and scored outside Synalux. It is a documentation form, not an assessment instrument or scoring service.

Use it to keep the assessment label, administration details, summary scores, and clinician narrative with the rest of the client's documentation.

## What the current form supports

The default form includes:

- Client ID
- Clinician-entered instrument label and form or version
- Administration date and examiner
- Respondent name and relationship, when applicable
- Administration language
- Composite label, standard score, confidence interval, and percentile rank
- Domain scores
- Additional subdomain and pairwise-comparison fields when they are available in the workspace
- Clinician narrative
- A field labeled **Source PDF**

A workspace may show a published custom version of the form, so labels and available fields can differ from the default shown here. The current **Admin > Form Builder** opens a blank form canvas; it does not load this default form for direct editing. Confirm the replacement workflow with the workspace administrator before publishing a custom version.

## Assessment-content boundary

Synalux stores only the information the clinician is authorized to enter. It does not:

- administer or score a standardized assessment;
- provide publisher items, prompts, scoring rules, norms, or cutoff tables;
- replace a publisher's official assessment platform;
- infer missing scores or simulate an administration; or
- reproduce proprietary report content.

Clinicians remain responsible for meeting each publisher's qualification, licensing, administration, scoring, and documentation requirements.

### Examples of records clinicians can label

The form is instrument-neutral. A clinician may enter the name of an assessment they administered externally, including assessments in areas such as adaptive functioning, language, behavior rating, skill acquisition, cognitive or developmental evaluation, sensory processing, or autism evaluation.

Instrument names entered by a clinician remain the property of their respective publishers. Synalux is not affiliated with or endorsed by those publishers.

## Enter a record

1. Administer and score the assessment through the publisher's approved process.
2. Open **Adaptive Assessment Log** and select **New Record**.
3. Enter the client, assessment label, administration details, and the scores you are authorized to document.
4. Add a clinician narrative when needed.
5. Review required fields and select **Submit Form**.
6. Confirm the success message before leaving the page.

Required fields in the default form are Client ID, instrument label, administration date, and examiner. Synalux displays a validation message when a required field is blank.

## Score entry

The default form provides individual composite fields plus text areas for structured score details:

- **Domain Scores (JSON array)**
- **Subdomain Scores (JSON array)**, when available
- **Pairwise Difference Comparisons (JSON array)**, when available

Enter only values copied from an authorized report. The current entry screen does not calculate scores or interpret normative meaning.

## Source PDF field

The current screen displays **Source PDF** as a text field; it is not a working file picker. Do not enter a local file path, public link, access token, or report contents in that field. Store assessment reports using your organization's approved document workflow until a managed attachment control is available in this form.

## Current screen boundaries

The current Adaptive Assessment Log screen supports form entry and submission. It does not currently show a record list, longitudinal trend chart, attachment viewer, or export controls. Use the success message as confirmation that the form submission completed.

## Screenshot

The screenshot shows the current default form. A published workspace-specific version may contain different labels or fields.

<details>
<summary>View the Adaptive Assessment Log form</summary>

![Adaptive Assessment Log new-record form showing client, administration, and composite-score fields](https://raw.githubusercontent.com/dcostenco/synalux-docs/main/docs/demo/40_adaptive_assessment_log_new_record.png)

</details>

## Assistant use

If assessment information is included in an assistant prompt, treat the response as a draft for clinician review. The assistant must not generate assessment items, scoring rules, norms, or fabricated results. Verify every score, date, instrument label, and interpretation against the authorized source before using the draft in a clinical record.

## Privacy and access

Enter only the minimum necessary information and follow your organization's privacy, access, and record-handling policies. Do not place licensed test items or other proprietary assessment content in score or narrative fields.

Related guides: [Applied Behavior Analysis](./applied_behavior_analysis_aba.md) · [Clinical Notes](./clinical_notes_documentation.md) · [Security and Compliance](./security_compliance.md)
