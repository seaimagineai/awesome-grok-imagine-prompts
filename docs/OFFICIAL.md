# Official Grok Imagine 1.5 examples and model boundaries

[← Prompt library](../README.md)

Checked September 24, 2026 against the following first-party sources. Official demonstrations describe xAI's products; they do not establish which controls SeaImagine exposes.

- [Video 1.5 release and Odyssey behind the scenes](https://x.ai/news/grok-imagine-video-1-5): credited to David Thompson / Heavy Pulp. Open the article for the official motion, audio and filmmaking examples.
- [Official X Preview launch video](https://x.com/grok/status/2062225080843747351): historical Preview release, not a SeaImagine sample.
- [Image-to-video documentation](https://docs.x.ai/developers/model-capabilities/video/image-to-video): includes a Milky Way source-image exercise using `grok-imagine-video-1.5`.
- [Imagine overview](https://docs.x.ai/developers/model-capabilities/imagine): includes a waterfall source-image example using `grok-imagine-video-1.5`.

[![Official waterfall input image](https://docs.x.ai/assets/api-examples/video/waterfall-still.png)](https://docs.x.ai/developers/model-capabilities/imagine)

*Official documentation input image; click for the source and example code. This is an input still, not a generated video result.*

## Before choosing a recipe

| Workflow | Documented model / constraint | Practical consequence |
| --- | --- | --- |
| Text or image to video | `grok-imagine-video-1.5`; 1–15 seconds; up to 1080p | Choose duration and resolution in the actual provider controls. Prompt text alone does not set API parameters. |
| References and preset voices | See the [reference guide](https://docs.x.ai/developers/model-capabilities/video/reference-to-video) | Advanced reference controls are not assumed to exist on SeaImagine's 1.5 page. |
| Video editing | The [editing guide](https://docs.x.ai/developers/model-capabilities/video/editing) uses `grok-imagine-video`; input up to 8.7 seconds | Recipes in the editing collection are companion workflows. Check that your chosen provider supports that separate model. |
| Extension | The [extension guide](https://docs.x.ai/developers/model-capabilities/video/extension) uses `grok-imagine-video`; adds 2–10 seconds to a 2–15 second input | This is not a claim that the 1.5 page has an extension button. |

For current parameters, follow [video generation documentation](https://docs.x.ai/developers/model-capabilities/video/generation). The API example in the main README requires an xAI account and key. We did not execute paid requests during documentation review.
