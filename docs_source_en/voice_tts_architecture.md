# Voice and Text-to-Speech

Synalux products that expose a **Speak** action can request a voice appropriate for the selected language. The voices shown depend on the active product, language, device, and workspace configuration.

## Voice selection

When a product includes a voice selector, choose from the voices it displays for the current language. The server validates the selected voice and routes the request to its configured speech provider.

## Fallback behavior

Synalux can try the alternate configured cloud provider when the preferred provider fails. If neither provider is available, the product receives an error or degraded response and may offer its own device-speech fallback. Available fallback behavior therefore depends on the product, device, browser, language, and configured providers.

Do not assume that every Synalux screen speaks, that every language has the same voices, or that speech remains available offline. Test the exact product, language, device, and network conditions used by the customer.

## Current voice-cloning boundary

The current customer portal does not provide a voice-cloning enrollment or voice-library management screen. Do not upload a voice sample or promise a cloned voice unless Synalux has supplied an approved enrollment workflow and the person whose voice is used has provided the required consent.

## Privacy and clinical use

Text sent to a cloud speech provider leaves the device for audio generation. Follow your organization's privacy policy and avoid sending more sensitive information than the speaking task requires. Text-to-speech is an accessibility and communication aid; it does not validate clinical content.
