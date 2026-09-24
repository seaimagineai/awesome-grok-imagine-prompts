# Multilingual prompt directory

[← Main collection](../README.md)

All **15 homepages contain eight complete illustrated cases**, presented in the same topic order: product, action, fantasy, dialogue, lifestyle, travel, animated layout and a second product treatment. The homepage provides nine category links, a complete 62-prompt index, and eight large starting images directly beside their complete local-language prompts and TXT exports. The separate preview grid has been removed. Featured cases belong to the same nine categories as the extended recipes; the complete index shows mode, duration, ratio, resolution and TXT links. Browser instructions live in separate localized reference pages.

The images are concept starting frames, not verified Grok video results. Translation completeness does not establish generation quality or equivalent results across languages.

The language set matches the fifteen links observed on the [SeaImagine model page](https://seaimagine.com/model/grok-imagine-1-5/) on September 24, 2026. Exact routes are in [locales.json](../data/locales.json). The interface screenshot uses English labels; fifteen linked workflow references explain its controls in their own language.

## Language directory

Every homepage contains **one unified 9-category table + a complete 62-prompt index + 8 illustrated cases with TXT exports + an illustrated SeaImagine section**. The guides preserve the earlier writing advice and additional local exercises.

| Language | Eight-case homepage | Further reading |
| --- | --- | --- |
| English | [English](../README.md) | [Writing guide](guides/en-US.md) |
| 简体中文 | [简体中文](../README.zh-CN.md) | [Writing guide](guides/zh-CN.md) · [4 extended recipes](../i18n/prompts.zh-CN.md) |
| 繁體中文 | [繁體中文](../README.zh-TW.md) | [Writing guide](guides/zh-TW.md) |
| 日本語 | [日本語](../README.ja-JP.md) | [Writing guide](guides/ja-JP.md) · [4 extended recipes](../i18n/prompts.ja-JP.md) |
| 한국어 | [한국어](../README.ko-KR.md) | [Writing guide](guides/ko-KR.md) |
| Español | [Español](../README.es-ES.md) | [Writing guide](guides/es-ES.md) · [4 extended recipes](../i18n/prompts.es-ES.md) |
| Français | [Français](../README.fr-FR.md) | [Writing guide](guides/fr-FR.md) |
| Deutsch | [Deutsch](../README.de-DE.md) | [Writing guide](guides/de-DE.md) |
| Português | [Português](../README.pt-BR.md) | [Writing guide](guides/pt-BR.md) |
| Italiano | [Italiano](../README.it-IT.md) | [Writing guide](guides/it-IT.md) |
| Русский | [Русский](../README.ru-RU.md) | [Writing guide](guides/ru-RU.md) |
| العربية | [العربية](../README.ar.md) | [Writing guide](guides/ar.md) |
| Bahasa Indonesia | [Bahasa Indonesia](../README.id-ID.md) | [Writing guide](guides/id-ID.md) |
| ไทย | [ไทย](../README.th-TH.md) | [Writing guide](guides/th-TH.md) |
| Tiếng Việt | [Tiếng Việt](../README.vi-VN.md) | [Writing guide](guides/vi-VN.md) |

## Scope and count

The English collection contains **62 distinct recipes: 35 inherited recipes plus 27 original briefs**. The five inherited featured cases are now fully translated in `data/featured-locales/`, alongside three shared exercises in `data/homepage-locales/`. These 120 displayed language versions represent eight shared scenes, not 120 different scenarios.

The three new exercises use 720p and durations of 10/5/5 seconds. The five inherited cases retain their original source settings; each has a source label; actual browser controls are documented in the linked workflow reference. Choose 5/10/15 seconds and 480p/720p on the inspected SeaImagine interface, and adapt timed actions accordingly.

The 54 category recipes (30 inherited plus 24 new originals) and advanced English documentation remain in English. All fifteen homepage category labels and recipe counts are localized. The 24 newest text-to-video prompts are untested original briefs based on documented social themes; see [research and attribution](SOCIAL_INSPIRATION.md). Chinese, Japanese and Spanish retain four extended localized recipes. The other eleven non-English guides preserve their ceramic-lamp workshop example. No original prompt body was shortened to reduce homepage length. Archived eight-second briefs must be adapted to an available browser duration.

Community video recommendations have been removed from the homepages. Sources remain in [the evidence reference](COMMUNITY.md). The SeaImagine section pairs a real interface screenshot with links to the bottle, dialogue and postcard cases; the screenshot is not a generated result.

## Maintenance

Maintain the three new exercises in [homepage-locales/en-US.json](../data/homepage-locales/en-US.json) and the five source cases plus navigation in [featured-locales/en-US.json](../data/featured-locales/en-US.json). Update all fourteen translations in the corresponding directories. Keep case IDs, images, settings, URLs and legacy anchors stable.

The five original English prompt bodies are checked against [source hashes](../data/source-featured-provenance.json). The three new English prompts also match [the exercise document](../prompts/06-community-exercises.md). Writing guides live in `docs/guides/`; their mappings and compatibility anchors are in [guide-index.json](../data/guide-index.json).

Plain-text exports in `prompts/text/` and the fifteen references in `docs/workflows/` are generated from the same canonical prompts and interface descriptions. Category pages retain full prompt blocks with per-page indexes and TXT links.

Run `python3 scripts/build.py`, then `python3 scripts/validate.py`. Validation checks all eight complete prompts, local links, image pairings, source settings, early navigation, section order, old anchors and generated-file freshness. These checks do not replace language or video review.

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

- [ ] The page contains eight complete illustrated prompts, one unified category table, and the localized SeaImagine image and call to action. Workflow instructions and community sources remain linked as references.
- [ ] Every prompt fits the current 2,000-character input limit.
- [ ] Case identifiers, images, settings, source URLs and English master synchronization pass validation.
- [ ] Dialogue fits within the specified duration.
- [ ] Model names, reference tags, URLs, and code identifiers are not translated.
- [ ] Rights and safety meaning remains unchanged.
- [ ] A proficient reviewer checked fluency and regional appropriateness.
- [ ] Local links and Markdown headings work.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for originality and media-rights requirements.
