# Grok Imagine 1.5 Multilingual Prompt Directory

[← Back to the main collection](../README.md)

All 15 language homepages now include the same three complete illustrated SeaImagine exercises, five steps tied to the actual browser interface, and four explanations of official or community work. Each exercise has a downloadable starting image, a full prompt, matching settings and a review checklist. Dialogue is localized into the reader’s language. The images are AI-generated starting frames, not verified Grok video results; the exercises remain untested.

The language set matches the fifteen language links observed on the [SeaImagine model page](https://seaimagine.com/model/grok-imagine-1-5/) on September 24, 2026. Exact routes are recorded in [locales.json](../data/locales.json). The interface screenshot was checked on the same date and uses English labels; every language guide explains the controls locally.

## Language directory

Every landing page below contains **3 illustrated exercises + 5 interface steps + 4 source explanations**. The last column describes additional material retained from the source collection; it does not replace the three complete homepage exercises.

| Language | Landing page | Additional source material |
| --- | --- | --- |
| English | [README](../README.md) | 35 inherited recipes: 5 illustrated homepage cases and 30 category recipes |
| 简体中文 | [中文说明](../README.zh-CN.md) | [4 extended localized recipes](../i18n/prompts.zh-CN.md) |
| 繁體中文 | [繁體中文說明](../README.zh-TW.md) | Earlier shared workshop test scene |
| 日本語 | [日本語ガイド](../README.ja-JP.md) | [4 extended localized recipes](../i18n/prompts.ja-JP.md) |
| 한국어 | [한국어 안내](../README.ko-KR.md) | Earlier shared workshop test scene |
| Español | [Guía en español](../README.es-ES.md) | [4 extended localized recipes](../i18n/prompts.es-ES.md) |
| Français | [Guide français](../README.fr-FR.md) | Earlier shared workshop test scene |
| Deutsch | [Deutsche Anleitung](../README.de-DE.md) | Earlier shared workshop test scene |
| Português (Brasil) | [Guia em português](../README.pt-BR.md) | Earlier shared workshop test scene |
| Italiano | [Guida italiana](../README.it-IT.md) | Earlier shared workshop test scene |
| Русский | [Русское руководство](../README.ru-RU.md) | Earlier shared workshop test scene |
| العربية | [الدليل العربي](../README.ar.md) | Earlier shared workshop test scene |
| Bahasa Indonesia | [Panduan Indonesia](../README.id-ID.md) | Earlier shared workshop test scene |
| ไทย | [คู่มือภาษาไทย](../README.th-TH.md) | Earlier shared workshop test scene |
| Tiếng Việt | [Hướng dẫn tiếng Việt](../README.vi-VN.md) | Earlier shared workshop test scene |

## What is fully localized, and what remains an archive?

The three shared SeaImagine exercises are a 10-second harbor reunion, a 5-second coastal postcard and a 5-second sea-glass bottle shot. All use 720p. Their complete instructions, dialogue where present, and review notes are available in every homepage language. All five browser steps and all four community explanations are also translated. The four source explanations do not imply that the original videos have been fully viewed or independently reproduced; see the [viewing evidence](COMMUNITY.md).

The English collection still contains **38 distinct recipes: 35 inherited recipes plus the 3 new exercises**. Translation does not increase that scenario count. The additional 35 English recipes and extended English documents have not all been translated into all 15 languages. Chinese, Japanese and Spanish retain their four longer localized recipes. The other eleven non-English pages retain the earlier ceramic-lamp workshop test scene as archive material, below the new shared exercises.

That earlier workshop scene specifies eight seconds and includes a controlled hand action, slow camera movement, preserved artisan and workshop, localized dialogue, ambient sound and continuity restrictions. It remains useful as a creative brief, but eight seconds is not an offered duration in the browser interface checked for this update. Choose an available duration and rewrite its time ranges before using it; do not assume every setting in an archived recipe is available.

No page claims that different languages produce identical results. Compare instruction following, dialogue, lip synchronization, sound mix and semantic drift using actual outputs rather than translation completeness alone.

## Maintaining the localized homepages

Edit the complete English master in [en-US.json](../data/homepage-locales/en-US.json), then update all fourteen other files in `data/homepage-locales/`. Keep the three case identifiers, image paths, settings and source URLs aligned. Preserve every production constraint while making dialogue natural in each language. The English prompt bodies must also match [the exercise document](../prompts/06-community-exercises.md).

Run `python3 scripts/build.py` to regenerate the homepages, then `python3 scripts/validate.py`. The validator checks locale structure, prompt length, fixed references, images, all five steps, source links, English prompt synchronization and generated-file freshness. These checks establish content consistency, not native-speaker fluency or video quality.

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

- [ ] The page contains all three complete illustrated prompts, all five browser steps and all four community explanations.
- [ ] Every prompt fits the current 2,000-character input limit.
- [ ] Case identifiers, images, settings, source URLs and English master synchronization pass validation.
- [ ] Dialogue fits within the specified duration.
- [ ] Model names, reference tags, URLs, and code identifiers are not translated.
- [ ] Rights and safety meaning remains unchanged.
- [ ] A proficient reviewer checked fluency and regional appropriateness.
- [ ] Local links and Markdown headings work.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for originality and media-rights requirements.
