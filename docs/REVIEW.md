# Source comparison and review record

Review date: September 24, 2026. Scope: repository content, source attribution, language navigation and public product routes.

## Initial release: independent reader review

- Baseline review: keep full image-plus-prompt examples, preserve source recipes and attribution, separate provider controls from official model capabilities.
- Round 1: accepted corrections to the English recipe count, Japanese/Spanish review dates and contribution policy. Accepted improvements to cover compression, community section placement and Chinese phrasing.
- Round 2: corrected three localized contribution-policy paragraphs and their templates. Reviewer rechecked those corrections and found no remaining blocking issue.

- Follow-up round after the main editor's independent check: the inherited issue form still prohibited all adaptations. It was aligned with the contribution guide, adding provenance, permission, verification status and actual model/provider fields. The reviewer approved the follow-up; a final field-position wording correction was also applied.

## Initial release: main editor's independent final check

After the review loop, checked the source and final repository directly: all five featured prompt blocks, thirty category recipes and five inherited images remain available. The Chinese wording correction is intentional. Checked the fifteen language routes and five related product routes: all returned HTTP 200 and matching page titles. The route snapshot is in [website-checks.json](../data/website-checks.json).

`python3 scripts/validate.py` passes. A second generation of the language pages produces identical files. Git whitespace checks pass. GitHub's Markdown renderer accepts the homepage and emits all intended image elements; the published GitHub page was then checked in a browser: all eleven image elements loaded, including badges, the cover, five featured images and two source thumbnails. Copy controls and full prompt text were present.

These checks do not establish paid generation success, video playback quality, translation equivalence across model outputs, or long-term product uptime. The initial browser attempt exposed X text and counts but no playback. A later review successfully loaded original video players; the current frame-sampling evidence supersedes that initial playback limitation. See [community evidence](COMMUNITY.md).

## Illustrated multilingual expansion

The follow-up source comparison identified four gaps: brand-specific visual cases, depth beyond language landing links, actual interface instructions, and direct viewing notes for community examples.

- Round 1: added three original illustrated exercises to every homepage; the reviewer requested direct navigation to the new workflow, local archive-parameter warnings, and an explicit empty-start-frame screenshot caption. All were accepted and applied in all 15 languages.
- Round 2: the reviewer found that standalone category and localized prompt files could bypass homepage warnings. Added nearby parameter notes to all five categories and the Chinese/Japanese/Spanish extended files, without rewriting their prompt bodies. Clarified the three new versus five inherited images.
- Final reviewer pass: checked the generated pages, global-language additions, image attribution and viewing limits; no remaining blocking finding. The validator passed independently.
- Main editor's independent comparison: source README text blocks, all 30 category prompt bodies and all five inherited asset files were preserved. The 15 homepages now carry 45 complete localized versions of the three new exercises; the unique English scenario count remains 38. Repeated generation was byte-for-byte stable. Local Markdown/HTML links, anchors, asset hashes and prompt synchronization passed. GitHub Markdown rendering produced the expected 15 image elements on the English homepage.

The screenshot documents 480p/720p and 5/10/15-second controls with no submitted generation. Original X players loaded during the follow-up; the official and GENEL observations are sampled frames, not full motion or audio tests. These checks do not establish successful paid generation or long-term uptime.
