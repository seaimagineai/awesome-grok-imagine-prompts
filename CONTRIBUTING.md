# Contributing

Thanks for improving SeaImagine's Grok Imagine prompt library.

1. State the use case, required input, mode, duration and intended aspect ratio.
2. Supply a complete copy-ready prompt with action, camera, audio and continuity details.
3. Label it **untested**, **author-reported** or **tested**, and record actual settings when tested. Do not imply that a concept image is a Grok output.
4. For adapted material, retain the source link, author and applicable license. Do not bulk-import material without permission or remove attribution. This repository's authorized upstream adaptation is documented in [ATTRIBUTION.md](docs/ATTRIBUTION.md).
5. Link community media to its original post. Do not apply this repository's MIT license to someone else's media.
6. For language changes, edit `templates/readmes/` and update `data/locales.json` if the site's language menu changes. Run `python3 scripts/build.py`, then `python3 scripts/validate.py`.
7. Do not invent SeaImagine API endpoints or copy xAI capabilities into a brand feature list without checking the live product.

Small improvements to prompt clarity, source accuracy, localization and reproducibility are welcome. Never include keys, private URLs or customer assets.
