# Grok Imagine 1.5 提示词库 — 简体中文

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 62 条提示词，其中 8 个图文案例提供 15 种语言版本。按分类浏览，复制完整提示词。

![Grok Imagine 1.5 — 展开的提示词手册，产品鞋、电车与纸鲸连成同一场景](assets/seaimagine-grok-hero.webp)

改编自 [Flaq AI](https://github.com/flaqai/awesome-grok-imagine)，由 SeaImagine 维护，采用 [MIT](LICENSE) 许可，与 xAI 无隶属关系。概念配图不代表 Grok 实测效果。

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## 分类索引

| 创作目标 | 图文案例 |
| --- | --- |
| 产品广告 | [海蓝色磨砂玻璃瓶——控制变量比较动态效果](#case-sea-glass-bottle) · [柑橘光环——高端香水产品短片](#case-citrus-halo) |
| 电影感动作场面 | [蓝色路线——雨中市场快递员跟拍](#case-blue-route) |
| 奇幻故事 | [蜂蜜面包——微缩烘焙坊故事](#case-honey-loaf) |
| 人物对白 | [港口重逢——只表现一个情绪变化](#case-harbor-reunion) |
| 生活方式视频 | [第一口——自然的咖啡馆体验分享](#case-first-sip) |
| 旅行短片 | [晨曦盐田线——旅行纪录片](#case-salt-line) |
| 动态排版 | [海岸明信片——让设计好的图片动起来](#case-coastal-postcard) |

[图文案例](#featured-prompts) · [官方与社区作品](#learn-from-official-and-community-examples) · [参数与操作参考](#writing-guide)

**[浏览更多提示词（英语）](docs/PROMPT_INDEX.md) · 54**

| 分类 | 数量 |
| --- | --- |
| [广告与产品](prompts/01-ads-and-products.md) | 6 |
| [电影故事](prompts/02-cinematic-storytelling.md) | 6 |
| [社交与生活方式](prompts/03-social-ugc.md) | 6 |
| [人物与参考素材](prompts/04-characters-and-references.md) | 6 |
| [编辑与延长视频](prompts/05-editing-and-extension.md) | 6 |
| [解压材质与微距声音](prompts/07-satisfying-materials.md) | 6 |
| [空间与场景变换](prompts/08-spaces-and-transformations.md) | 6 |
| [微缩与超现实日常](prompts/09-miniature-and-surreal.md) | 6 |
| [时尚造型与表演](prompts/10-fashion-and-performance.md) | 6 |

<a id="visual-index"></a>

<a id="featured-prompts"></a>

## 可复制、可改写的图文提示词

8 个案例均附完整提示词与起始帧图片。图片用于展示构思，并非已核验的视频结果。

标注来源 Flaq AI 的五个案例保留原始时长和分辨率；其余三个案例按 SeaImagine 当前选项编写。在 SeaImagine 使用源库案例时，请选择 5/10/15 秒和 480p/720p，并重新安排动作时间。

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. 海蓝色磨砂玻璃瓶——控制变量比较动态效果

![海蓝色磨砂玻璃瓶——控制变量比较动态效果](assets/seaimagine-sea-glass-bottle.webp)

**图生视频参数:** 5s · 16:9 · 720p · [起始帧——打开并保存](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/zh-CN/sea-glass-bottle.txt)

```text
保留浅色石面上唯一的海蓝色磨砂玻璃瓶、圆柱形瓶盖、没有印字的空白正面、
液面高度、地平线和柔和侧光。瓶子始终不动。
在五秒内让摄影机缓慢向右平移，移动距离不超过一个瓶身宽度。
一小滴水沿瓶身正面滑下，在底部停住。背景海浪在虚焦中轻轻起伏。
反射效果始终与摄影机和光源的位置一致。
声音：只有远处海浪声；不要音乐、人声、玻璃碰撞声或夸张的水花声。
不剪切，不变焦。保留瓶身轮廓、瓶盖对齐关系、玻璃质感和物体数量。
避免生成标志、改变液面高度、扭曲边缘、物体漂浮或新增道具。
最后一秒保持画面稳定。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. 蓝色路线——雨中市场快递员跟拍

![蓝色路线——雨中市场快递员跟拍](assets/rainy-market-courier-video.webp)

**图生视频参数:** 10s · 16:9 · 1080p · [起始帧——打开并保存](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/zh-CN/blue-route.txt)

[来源：Flaq AI](docs/ATTRIBUTION.md)

```text
保留所提供图片中的快递员、钴蓝色电动摩托车、货箱、高架市场、半透明雨棚、湿钢制步道、灯光和夜间配色。制作一个贴近真实环境、连续的低机位跟拍镜头，表现可信的重量、轮胎抓地力、雨水和悬挂运动。

0–3 秒：摩托车从原有姿态平稳加速。后轮排开一层薄薄的扇形水花，悬挂经过排水接缝时压缩。摄影机在车轮高度、车辆侧后方跟拍，以相同速度移动，不剧烈晃动。

3–7 秒：快递员倾身通过一个宽阔的左弯。雨棚随风弯动，食摊冒出蒸汽，暖色实景灯在湿地反射中形成柔和光痕。两只车轮始终保持圆形并接触地面。

7–10 秒：摩托车回正，驶向市场中更明亮、开阔的区域。摄影机落后半米，显露前方路线，再保持稳定的结束画面。

声音：真实的电机啸鸣、水花声、雨打棚顶声、轻微市场人声，以及一次悬挂的低沉撞击声。不要配乐、对白、警笛或爆炸。

连续性要求：精确保留骑手服装、头盔、摩托车几何形状、货箱、蓝色车身板和市场布局。不要车辆变形、车轮扭曲、碰撞、武器、可读招牌、标志、瞬移镜头或不可能的速度突变。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. 蜂蜜面包——微缩烘焙坊故事

![蜂蜜面包——微缩烘焙坊故事](assets/pear-bakery-miniature-video.webp)

**图生视频参数:** 9s · 16:9 · 1080p · [起始帧——打开并保存](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/zh-CN/honey-loaf.txt)

[来源：Flaq AI](docs/ATTRIBUTION.md)

```text
保留梨子屋烘焙坊、三名微缩面包师、服装、面孔、蜂蜜面包、烤炉、窗户、苔藓、三叶草、月亮、具有触感的定格动画材料，以及冷暖色对比。

0–3 秒：以所提供的广角构图开场，带有细微的手作定格节奏。两名面包师一起抬起温热的蜂蜜面包，双手始终贴在木板上。一小团面粉扬起，炉火闪动，第三名面包师打开售卖窗口。

3–7 秒：两人小心地同步走四步，朝窗口前进。面包呈现可信的重量，在两人之间略微下沉。屋外，一片三叶草叶子滴下一滴露水，两只萤火虫在不同的远近位置飘过。摄影机向右缓缓绕行五度。

7–9 秒：他们把木板推上柜台，相视露出释然的微笑，炉火光线稳定下来。结尾让三个人都在画面中，面包位于中央。

声音：木地板上的细小脚步声、轻柔炉火噼啪声、木板吱呀声、微弱夜虫声，以及售卖窗口的一声小铃响。不要对白、旁白、音乐或文字。

连续性要求：保留人物数量、脸部设计、比例、服装颜色、梨子形状、室内布局和手工材质。不要多余面包师、光滑的电脑生成质感、橡胶般的肢体、悬浮道具、融化的面包、镜头切换、标志或类似知名系列的人物设计。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. 港口重逢——只表现一个情绪变化

![港口重逢——只表现一个情绪变化](assets/seaimagine-harbor-reunion.webp)

**图生视频参数:** 10s · 16:9 · 720p · [起始帧——打开并保存](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/zh-CN/harbor-reunion.txt)

```text
保留所提供图片中的两名成年人、各自的面容、藏蓝色与奶油色服装、木码头和柔和晨光。
始终让两人处于同一个中远景画面中。
0–3 秒：左侧的人注意到前来的朋友，向前迈一小步。
其肩膀放松下来；朋友回以轻轻的微笑。双手保持可见，姿态自然放松。
3–7 秒：左侧的人用自然的普通话说：“你来了。”朋友点一下头。
对白要克制，不哭泣，也不做夸张表情。
7–10 秒：两人都转头望向停泊的小船。最后一秒保持画面，方便衔接下一个镜头。
镜头：只缓慢推进一次，不切反打镜头，不剪切。
声音：近距离、清晰可辨的对白，轻柔的港口水声和远处的海鸥声；不要音乐或字幕。
保持两人身份、服装、码头结构、船只位置和晨光方向一致。
避免多出人物、戏剧化动作、面部磨皮、多余手指和镜头跳动。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. 第一口——自然的咖啡馆体验分享

<a href="assets/cozy-cafe-ugc-video.webp"><img src="assets/cozy-cafe-ugc-video.webp" width="480" alt="第一口——自然的咖啡馆体验分享"></a>

**图生视频参数:** 10s · 9:16 · 1080p · [起始帧——打开并保存](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/zh-CN/first-sip.txt)

[来源：Flaq AI](docs/ATTRIBUTION.md)

```text
把所提供的咖啡馆照片变成真实、手持拍摄的创作者体验分享。保留人物的脸、年龄、皮肤纹理、头发、苔绿色毛衣、杯子、糕点、窗户和桌面布局。

0–3 秒：镜头自然轻微晃动。她喝完一口，把陶瓷杯放低约十厘米，带着浅笑呼一口气，视线从窗外转回镜头。蒸汽向上卷起，身后玻璃上的雨痕缓慢汇合。

3–8 秒：她用自然、放松的普通话说：“口感很绵密，不会太甜——而且真的能尝到燕麦味。”语气随意，在“太甜”之后稍作停顿。口型紧贴对白，手中的杯子保持稳定。

8–10 秒：她轻轻点头表示认可，摄影机稳定下来时，她低头看向糕点。

声音：近距离手机录音的人声、安静的咖啡馆环境底音、远处牛奶蒸汽机声、轻柔雨声、陶瓷杯接触声。人声在前景，环境声保持低音量。不要背景音乐或字幕。

连续性要求：不要美化面部、换衣服、多余手指、重新设计杯子或食物、凭空出现的背景人物、标志或夸张的网红动作。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. 晨曦盐田线——旅行纪录片

![晨曦盐田线——旅行纪录片](assets/coastal-salt-train-documentary.webp)

**图生视频参数:** 12s · 16:9 · 1080p · [起始帧——打开并保存](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/zh-CN/salt-line.txt)

[来源：Flaq AI](docs/ATTRIBUTION.md)

```text
把所提供的沿海盐田场景变成尊重劳动者的观察式旅行纪录片。保留两名工人、奶油色与赭色列车、盐池、石灰岩山丘、建筑、海面、日出方向和低饱和胶片配色。

0–4 秒：固定广角画面。工人继续检查水道：一人用木制工具划过浅卤水，另一人扶稳隔板。水波随工具和晨风变化。列车在中景以平稳速度驶近。

4–9 秒：摄影机缓慢向右摇摄，跟随列车。车轮始终对齐铁轨，车厢间距和车窗排列节奏保持一致。一层薄薄海雾从列车后方飘过，阳光逐渐照亮前景盐晶。

9–12 秒：列车向海岸方向驶过，摇摄缓缓停止。一名工人站起，自然伸展身体，望向铁路线。最后两秒保持画面，留作剪辑点。

声音：轻柔电力列车嗡鸣、有节奏的车轮过接缝声、掠过浅水的微风、远处海鸥声，以及木制工具划过卤水的声音。不要旁白、音乐、人群声或戏剧化汽笛。

连续性要求：劳动动作真实、人体结构稳定、地景固定、列车设计不变，反射与水体运动符合物理规律。不要现代城市天际线、摆拍游客、新建筑、标志、可读招牌、过度饱和的明信片色彩或延时摄影天空。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. 海岸明信片——让设计好的图片动起来

<a href="assets/seaimagine-coastal-postcard.webp"><img src="assets/seaimagine-coastal-postcard.webp" width="480" alt="海岸明信片——让设计好的图片动起来"></a>

**图生视频参数:** 5s · 9:16 · 720p · [起始帧——打开并保存](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/zh-CN/coastal-postcard.txt)

```text
让这张三格海岸明信片动起来，不改变排版或边框。
完整保留所有物体和颜色。上格：杯中升起一缕细细的蒸汽。
中格：港口水面泛起轻微涟漪，阳光在水面闪动。
下格：只有画面中已有的纸张一角被微风轻轻掀起，然后落下。
每个动作都限制在各自的画格内。五秒内始终完整显示所有画格。
镜头：固定，不变焦、不摇移、不剪切，画格之间不转场。
声音：轻微水声和柔和的纸张沙沙声；不要对白、音乐、字幕或新增文字。
保留杯柄、窗框、地图标记、各格尺寸和阅读顺序。
避免画格融合、凭空生成新场景、重绘字母，或让物体跨越边框移动。
结尾时纸角落稳，原有构图保持完整。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. 柑橘光环——高端香水产品短片

![柑橘光环——高端香水产品短片](assets/citrus-fragrance-product-video.webp)

**图生视频参数:** 8s · 16:9 · 1080p · [起始帧——打开并保存](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/zh-CN/citrus-halo.txt)

[来源：Flaq AI](docs/ATTRIBUTION.md)

```text
保留所提供图片中的瓶身设计、玻璃比例、瓶盖、石灰岩台座、葡萄柚皮、暖象牙色布景和金色侧光。制作一段优雅的八秒产品短片。

0–2.5 秒：以近乎固定的微距构图开场。摄影机极缓慢地向前推进。冷凝水珠映着光，两滴水沿冰凉的玻璃自然滑下。葡萄柚皮从台座上飘起，仿佛被可控的影棚微风托起。

2.5–6 秒：果皮优雅地绕瓶身螺旋一周，不接触或遮挡瓶盖。细小的柑橘雾粒穿过逆光。折射和聚焦光斑在厚玻璃中按物理规律移动；瓶身始终完全坚硬、不变形。

6–8 秒：果皮落回原先的弧形，摄影机缓缓停下，一道明亮的镜面高光沿瓶身边缘移动一次。以干净的产品主画面结束。

声音：仅有近距离的影棚拟音——果皮条轻柔移动声、两声清脆水滴声和细微的玻璃共鸣。不要人声、音乐或文字。

连续性要求：不要改变瓶身轮廓、瓶盖切面、液面高度、台座、配色或背景拱形。不要标签、标志、多余水果、悬浮瓶子、几何形状晃动、镜头跳动或人造闪光爆发。
```

[返回分类索引](#find-the-right-prompt)

<a id="learn-from-official-and-community-examples"></a>

## 学习官方与社区作品的做法

来源帖标明了创作者和模型版本。请打开原帖观看；以下实用建议介绍创作方法，不代表我们已经复现这些视频。

### [官方 1.5 Preview 片段——Grok / Heavy Pulp](https://x.com/grok/status/2062225080843747351)

[![官方 1.5 Preview 片段——Grok / Heavy Pulp](https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg)](https://x.com/grok/status/2062225080843747351)

学习把预告片拆成多个独立短镜头来规划。请区分 Preview 预览版素材与已发布的 1.5 模型。

### [完成的短片——JSFILMZ](https://x.com/JSFILMZ0412/status/2062480692835938771)

作者称其制作了一部 2.5 分钟的短片，并讨论生成式表演的局限。先练习一段平静的交流，再用剪辑后的多个镜头组成更长的故事。

### [先规划图片，再生成动态——GENEL](https://x.com/genel_ai/status/2061382998873034825)

[![先规划图片，再生成动态——GENEL](https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg)](https://x.com/genel_ai/status/2061382998873034825)

创作者称先用 ChatGPT Images 2.0 制作拼贴图，再用 Grok Imagine Video 1.5 生成动态。我们的明信片练习固定画格边框，并且每格只安排一个动作。

### [控制变量的对比——JSFILMZ](https://x.com/JSFILMZ0412/status/2061117682515050669)

使用同一张原图和可比的参数。检查几何形状、运动和声音，不要照搬过去的排名。我们的玻璃瓶练习将这些变量分开考察。

<details>
<summary>抽样画面观察与核验限制</summary>

2026 年 9 月 24 日，我们在 X 原帖播放器中抽样查看了这些画面：官方视频约 3.6 秒处（头盔与军队）、19.8 秒处（面部特写）和 34.6 秒处（燃烧的滨水城市）；GENEL 视频约 0.05 秒处（海边栏杆）、4.9 秒处（铁路道口）和 12 秒处（逆光中的手）。可以学习官方视频如何切换景别，以及 GENEL 如何在不同镜头间保持一致的海岸光线。我们的固定画格明信片是另一种练习。此次仅抽样查看画面，未完整测试运动效果或音频。

</details>

[来源与观看记录（英语）](docs/COMMUNITY.md)

<a id="writing-guide"></a>

<a id="1-竹影茶席冷泡茶产品片"></a>

<a id="grok-imagine-15-最适合用中文还是英文提示词"></a>

<a id="grok-imagine-video-15-能力速览"></a>

<a id="使用建议"></a>

<a id="参考图越多越好吗"></a>

<a id="图生视频为什么容易变脸或改变产品"></a>

<a id="完整场景库"></a>

<a id="常见问题"></a>

<a id="怎样做超过-15-秒的故事"></a>

<a id="提示词写法"></a>

<a id="贡献与版权"></a>

## 参考资料

[写作参考](docs/guides/zh-CN.md) · [参数与操作参考](docs/workflows/zh-CN.md) · [SeaImagine](https://seaimagine.com/cn/model/grok-imagine-1-5/)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

<a id="multilingual-prompts"></a>

## 合集与来源署名

共 62 条不同的英语提示词：35 条保留自源库，27 条原创。最新 24 条根据社媒题材重新创作，尚未生成验证。翻译不计为新增场景。

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/cn/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
