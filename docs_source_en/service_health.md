# Service Health

Synalux runs platform-side health checks for core records, connected accounts, voice services, and other shared dependencies. These checks help the Synalux operations team detect service failures and investigate degraded behavior.

## What customers see

Each customer-facing workflow must report its own failure instead of implying that an action succeeded. For example, a failed connection, calendar update, message, payment, or voice request should remain visible as an error or unavailable state in that workflow.

## What to do when a feature is unavailable

1. Keep any unsaved work visible and note the action that failed.
2. Retry once after confirming the device is online.
3. For a connected service, open **Settings > Integrations** and review its connection state.
4. If the issue continues, contact Synalux support with the affected workspace, feature, approximate time, and visible error message. Do not send passwords, access tokens, payment data, or patient information in a general support message.

## Current visibility

The customer portal does not currently include a full service-health dashboard or public status page. Platform monitoring and administrator notifications do not prove that a specific customer action completed; verify the result in the workflow where the action was performed.
