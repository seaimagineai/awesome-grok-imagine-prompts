# Create a short video with SeaImagine

[← Prompt library](../README.md) · [简体中文](#中文操作说明)

[SeaImagine Grok Imagine 1.5](https://seaimagine.com/model/grok-imagine-1-5/) is the brand's browser entry for this collection. Start with a product still, portrait, illustration or opening frame you can use, then describe the motion. You do not need an API key for the workflow described here.

## Actual controls, checked September 24, 2026

![SeaImagine interface with bottle prompt and settings](../assets/seaimagine-interface.jpg)

The screenshot is a real browser capture: the bottle prompt is entered, with **720p / 5s / 16:9** selected. **Start Frame is empty**; upload the image before generating. No generation was submitted. The displayed credit amount is a point-in-time quote, not a fixed price.

| Control | Observed choices | How to use it |
| --- | --- | --- |
| Video / Image | Video selected | Choose Video for these exercises. |
| Start Frame | Image upload on the left | Save a case image and upload it here. |
| Prompt | Counter allows 2,000 characters | Paste one complete localized case; all new cases fit. |
| Model | Grok Imagine 1.5 | Confirm this selection before submitting. |
| Resolution | 480p, 720p | The new cases use 720p; 1080p is not offered in the inspected interface. |
| Duration | 5s, 10s, 15s | Original illustrated cases: 10s; bottle: 5s. |
| Ratio | 2:3, 3:2, 1:1, 9:16, 16:9, 4:3, 3:4 | Original illustrated cases: 16:9. |
| Generate | Setting-dependent credits | Check the amount and account requirements before submitting. |

1. Open [the bottle exercise](../README.md#seaimagine-sea-glass-bottle), save its image and copy its complete prompt.
2. Select **Video**, upload the image with **Start Frame**, paste the prompt and confirm the model.
3. Select **720p**, **5s**, **16:9** below the prompt. Review the credit quote beside **Generate**.
4. Submit when ready. Inspect the resulting bottle shape, cap, droplet, reflections and final frame before downloading. These are instructions for the reader; this repository has not tested generation.
5. Change only one instruction per retry and save the actual settings with the result.

### Adapting the source archive

The inherited recipes preserve their original creative intent, including 6/8/9/12-second timings and 1080p suggestions. These are not SeaImagine UI settings. Select 5, 10 or 15 seconds and rewrite the timing ranges so every action fits; choose 720p for the inspected interface. References, editing and extension are separate workflows whose availability must be checked with the chosen provider.

## Related SeaImagine tools

| Need | Brand entry | Suggested use |
| --- | --- | --- |
| Animate a prepared first frame | [Grok Imagine 1.5](https://seaimagine.com/model/grok-imagine-1-5/) | Use the motion-first recipes in this library. |
| Create a first frame from an idea | [Text to Image](https://seaimagine.com/text-to-image/) | Establish subject, lighting and composition before animation. |
| Refine an existing still | [Image to Image](https://seaimagine.com/image-to-image/) | Correct the source image before asking the video model to move it. |
| Compare another animation route | [Image to Video](https://seaimagine.com/image-to-video/) | Use the same source and short brief for a fair comparison. |
| Work with an explicit audio track | [Lip Sync Video Generator](https://seaimagine.com/lip-sync-video-generator/) | A separate tool; do not assume it is a switch inside Grok 1.5. |

These public routes were checked on September 24, 2026. This is a practical recommendation based on accessible product pages, not a promise of permanent uptime, free unlimited use, or a successful paid generation. Check [pricing](https://seaimagine.com/pricing/) and live settings when you create. We found no basis for carrying over Flaq AI's API endpoints into SeaImagine documentation.

## 中文操作说明

先打开 [SeaImagine 中文 Grok Imagine 1.5 页面](https://seaimagine.com/cn/model/grok-imagine-1-5/)，上传首帧，再复制适合的提示词。把人物、服装、产品外形和光线改成你自己的图片内容，每次只安排一个主要动作和一种运镜。

已核对的界面提供 480p／720p，时长为 5／10／15 秒。瓶子案例选 720p、5 秒、16:9；其余五个原创图文案例选 10 秒、16:9。截图只填写了提示词并选择参数，首帧尚未上传，也未提交生成。旧配方中的 8 秒或 1080p 不能照搬：请选择现有参数，并重新安排动作时间。费用以提交时页面显示为准。生成后检查脸、手、物体数量、接触位置、反光、声音和最后一帧；有问题时只调整一个因素，方便判断哪种写法有效。需要先制作首帧，可用官网的文字生图或图片编辑工具。

本库保留官方参考图、编辑与延长教程，但不代表 SeaImagine 的 1.5 页面已提供这些功能。官网可访问也不等于已完成付费生成或长期稳定性测试。
