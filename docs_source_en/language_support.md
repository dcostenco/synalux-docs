# 🌍 Language Support

**25 UI locales · 21 TTS languages · 21 AAC offline dictionaries.** Synalux is built for multilingual practices and the families they serve. Below is the honest coverage matrix per surface.

---

## Coverage Matrix

| Language | UI translation | Premium TTS (Inworld) | Fallback TTS (Azure) | Offline TTS (Kokoro) | AAC offline dict (500 words) | Cloud autocorrect (Gemini) |
|---|---|---|---|---|---|---|
| 🇺🇸 English (US/GB/AU) | ✅ | ✅ 6 voices | — | ✅ | ✅ | ✅ |
| 🇪🇸 Spanish (ES/MX) | ✅ | ✅ Carmen / Diego | — | ✅ | ✅ | ✅ |
| 🇫🇷 French | ✅ | ✅ Camille / Lucas | — | ✅ | ✅ | ✅ |
| 🇩🇪 German | ✅ | ✅ Hans / Lena | — | — | ✅ | ✅ |
| 🇧🇷🇵🇹 Portuguese | ✅ | ✅ Luana | — | ✅ | ✅ | ✅ |
| 🇮🇹 Italian | ✅ | ✅ Giulia | — | — | ✅ | ✅ |
| 🇳🇱 Dutch | ✅ | ✅ Lotte | — | — | ✅ | ✅ |
| 🇵🇱 Polish | ✅ | ✅ Zofia | — | — | ✅ | ✅ |
| 🇯🇵 Japanese | ✅ | ✅ さくら | — | ✅ | ✅ | ✅ |
| 🇨🇳 Chinese (Mandarin) | ✅ | ✅ 美 | — | ✅ | ✅ | ✅ |
| 🇨🇳 Chinese (zh-TW) | — | — | ✅ 曉臻 | — | — | ✅ |
| 🇨🇳 Chinese (zh-HK) | — | — | ✅ 曉曼 | — | — | ✅ |
| 🇰🇷 Korean | ✅ | ✅ 지수 | — | — | ✅ | ✅ |
| 🇷🇺 Russian | ✅ | ✅ Аня | — | — | ✅ | ✅ |
| 🇷🇴 Romanian | ✅ | — (subsidized via Azure on free tier) | ✅ Alina | — | ✅ | ✅ |
| 🇺🇦 Ukrainian | ✅ | — (subsidized via Azure on free tier) | ✅ Поліна | — | ✅ | ✅ |
| 🇸🇦 Arabic (RTL) | ✅ | ✅ ليلى | — | — | ✅ | ✅ |
| 🇮🇱 Hebrew (RTL) | ✅ | ✅ נועה | — | — | ✅ | ✅ |
| 🇮🇳 Hindi | ✅ | ✅ आन्या | — | — | ✅ | ✅ |
| 🇻🇳 Vietnamese | ✅ | — | ✅ Hoài Mỹ + Nam Minh | — | ✅ | ✅ |
| 🇵🇭 Filipino (Tagalog) | ✅ | — | ✅ Blessica + Angelo | — | ✅ | ✅ |
| 🇹🇷 Turkish | ✅ | — | ✅ Emel + Ahmet | — | ✅ | ✅ |
| 🇮🇩 Indonesian | ✅ | — | ✅ Gadis + Ardi | — | ✅ | ✅ |

---

## Counts at a Glance

| Surface | Languages | Notes |
|---|---|---|
| **UI translations** | **25 locales (100% coverage each)** | en×3, es×2, pt×2 + 18 single-region locales |
| **Premium TTS (Inworld)** | 14 base languages, ~24 voices | en, es, fr, de, pt, it, nl, pl, ja, zh, ko, ru, he, ar, hi |
| **Fallback TTS (Azure)** | 8 languages, ~14 voices | ro, uk, zh-tw, zh-hk, vi, tl, tr, id |
| **Offline neural TTS (Kokoro)** | 6 languages | en, es, fr, pt, ja, zh — bundled WASM |
| **AAC offline dictionary** | 21 languages × 500 words each | Index-aligned across langs |
| **Whisper transcription** | ~99 languages | Whisper's full coverage; quality varies by language |
| **Cloud autocorrect (Gemini Flash-Lite)** | ~100+ languages | Bench-validated for en/ro/ru/es/uk/pl |

---

## How the Layered Fallback Works

If your language doesn't have premium TTS, you still get a voice. If you don't have Whisper-trained data, you still get cloud transcription. If you're offline, you still get the AAC dictionary.

```
TTS:        Inworld (Tier 1) → Kokoro WASM (Tier 1.5) → Web Speech API (Tier 2) → espeak-ng WASM (Tier 3)
Translation: Offline dictionary → Cloud Gemini Flash → original text passthrough
Autocorrect: Local prism-coder (when running) → Cloud Gemini Flash-Lite → original text passthrough
```

See [Voice TTS Architecture](voice_tts_architecture.md), [Translation](translation.md), [Transcription](transcription.md) for the full per-surface design.

---

## Subsidized Languages (Free Tier)

For users in regions where Synalux serves underserved populations, Synalux absorbs Inworld TTS-2 cost on the free tier so users get premium voices at no charge:

`ro` Romanian · `uk` Ukrainian · `ru` Russian · `de` German · `ko` Korean · `ar` Arabic

Without this subsidy, users in these regions would either pay or use Tier 1.5/2/3 fallbacks.

---

## Adding a Language

The translation pipeline is automated. To add a 26th UI locale:

1. Add the locale code to `Locale` type + `LOCALE_LABELS` in `portal/src/lib/i18n.ts`.
2. Add an empty `'<locale>': {}` entry in the `translations` map.
3. Run the bulk-translation script (one-shot, not committed) — pulls all 257 keys from `en-US`, batch-translates via Gemini Flash-Lite (~$0.005), writes back the locale block.
4. Add a voice entry to `portal/src/shared/voice-catalog.ts` (Inworld if available; else Azure fallback).
5. Run the AAC dict script for the matching prism-aac repo (translates 500 entries via Gemini, ~$0.005).
6. tsc + commit.

End-to-end: ~10 minutes per new language, ~$0.01 in API spend.

---

## Roadmap

Languages frequently requested but not yet supported:
- Greek (el), Czech (cs), Hungarian (hu), Swedish (sv), Norwegian (no), Danish (da), Finnish (fi)
- Bengali (bn), Tamil (ta), Telugu (te), Marathi (mr), Punjabi (pa) — South Asian sub-languages
- Swahili (sw), Yoruba (yo), Hausa (ha) — African languages

If you need a specific language for your practice, [contact us](https://synalux.ai/contact) — turnaround is typically 1-2 weeks for adding a new locale across all surfaces.
