# Grok Imagine 1.5 Multilingual Prompt Directory

[← Back to the main collection](../README.md)

This repository supports 15 languages with localized guidance and at least one complete, copy-ready prompt in every language. The goal is not word-for-word translation. A useful localization preserves the shot, camera, physics, continuity, and test conditions while making dialogue, phrasing, units, punctuation, and cultural context sound natural to the target audience.

The language set matches the fifteen language links observed on the [SeaImagine model page](https://seaimagine.com/model/grok-imagine-1-5/) on September 24, 2026. Exact route mappings are in [locales.json](../data/locales.json). English has the full illustrated catalog; Chinese, Japanese and Spanish have four extended localized recipes; the other eleven languages have a complete shared test scene. These are localized entry guides, not fifteen full translations of every recipe. Extended English documents are labeled when linked from localized pages.

## Language directory

| Language | Landing page | Extended prompt set | Shared test scene |
| --- | --- | --- | --- |
| English | [README](../README.md) | 38 English recipes (35 inherited + 3 new) | Source brief |
| 简体中文 | [中文说明](../README.zh-CN.md) | [4 complete recipes](../i18n/prompts.zh-CN.md) | — |
| 繁體中文 | [繁體中文說明](../README.zh-TW.md) | — | Included |
| 日本語 | [日本語ガイド](../README.ja-JP.md) | [4 complete recipes](../i18n/prompts.ja-JP.md) | — |
| 한국어 | [한국어 안내](../README.ko-KR.md) | — | Included |
| Español | [Guía en español](../README.es-ES.md) | [4 complete recipes](../i18n/prompts.es-ES.md) | — |
| Français | [Guide français](../README.fr-FR.md) | — | Included |
| Deutsch | [Deutsche Anleitung](../README.de-DE.md) | — | Included |
| Português (Brasil) | [Guia em português](../README.pt-BR.md) | — | Included |
| Italiano | [Guida italiana](../README.it-IT.md) | — | Included |
| Русский | [Русское руководство](../README.ru-RU.md) | — | Included |
| العربية | [الدليل العربي](../README.ar.md) | — | Included |
| Bahasa Indonesia | [Panduan Indonesia](../README.id-ID.md) | — | Included |
| ไทย | [คู่มือภาษาไทย](../README.th-TH.md) | — | Included |
| Tiếng Việt | [Hướng dẫn tiếng Việt](../README.vi-VN.md) | — | Included |

## Shared localization test scene

The 11 newer language pages use the same original creative brief: an eight-second image-to-video shot of a ceramic lamp workshop. Keeping the scene constant makes it easier to compare:

- preservation of the artisan, lamp, tools, workshop, composition, and light;
- one controlled hand action and one slow camera move;
- physically plausible dust, paper, clay, and light behavior;
- natural localized dialogue equivalent to “The tiny openings make the light softer”;
- workshop ambience, tool contact, voice priority, and no music;
- exclusions for identity drift, extra fingers, lamp redesign, fake text, logos, and cuts.

The pages do not claim that outputs will be identical across languages. The shared brief is a practical baseline for testing instruction following, dialogue, lip synchronization, audio mix, and semantic drift.

## Localization rules

### Preserve production intent

Do not change duration, aspect ratio, shot timing, object count, camera path, reference roles, continuity locks, or exclusions unless the localized market actually requires a production change.

### Localize dialogue, not just vocabulary

- Keep spoken dialogue in quotation marks.
- State the language and regional variety when it matters.
- Replace literal phrasing with a natural sentence of comparable speaking time.
- Preserve emotion, pause, energy, and speaker assignment.
- Do not mix translated shot direction with untranslated dialogue accidentally.

### Keep cinematography readable

Use familiar local terms for close-up, wide shot, push-in, pan, orbit, locked camera, shallow focus, backlight, room tone, and Foley. If a translated technical term is uncommon, keep the established English term in parentheses once.

### Localize responsibly

- Use local decimal, time, and quotation conventions consistently.
- Avoid stereotypes, decorative scripts used as props, and invented cultural markers.
- Do not translate a brand, product label, legal claim, or UI string unless authorized.
- Keep accessibility cues, captions, and on-screen text separate from spoken dialogue.
- Ask a native or highly proficient reviewer to check fluency and unintended meanings.

## Mixed-language production template

```text
[Shot direction language] <language used for visual and camera instructions>
[Spoken dialogue] "<exact target-language line>"
[Voice] <language + regional variety + age range + energy + pace>
[Pronunciation] <names or technical terms that need explicit guidance>
[Audio priority] dialogue foreground; ambience below; no automatic subtitle
[On-screen text] <exact approved copy, or explicitly no text>
[Continuity] preserve speaker identity, voice assignment, timing, and lip synchronization
```

## Contribution checklist for a new localization

- [ ] The page contains a complete prompt, not translated headings alone.
- [ ] Dialogue fits within the specified duration.
- [ ] Model names, reference tags, URLs, and code identifiers are not translated.
- [ ] Rights and safety meaning remains unchanged.
- [ ] A proficient reviewer checked fluency and regional appropriateness.
- [ ] Local links and Markdown headings work.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for originality and media-rights requirements.
