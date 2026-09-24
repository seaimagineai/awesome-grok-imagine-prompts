# Grok Imagine 1.5 提示词库 — 简体中文

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 65 条提示词，其中 11 个图文案例提供 15 种语言版本。按分类浏览，复制完整提示词。

![Grok Imagine 1.5 — 展开的提示词手册，产品鞋、电车与纸鲸连成同一场景](assets/seaimagine-grok-hero.webp)

改编自 [Flaq AI](https://github.com/flaqai/awesome-grok-imagine)，由 SeaImagine 维护，采用 [MIT](LICENSE) 许可，与 xAI 无隶属关系。概念配图不代表 Grok 实测效果。

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## 分类索引

[浏览更多提示词（英语） · 65](docs/PROMPT_INDEX.md)

| 分类 | 包含场景 | 适用模式 | 案例 |
| --- | --- | --- | --- |
| [产品与广告 · 8](docs/PROMPT_INDEX.md#01-ads-and-products) | 护肤微距 / 咖啡 / 珠宝 / 应用广告 | 文生视频 / 图生视频 / 参考图生视频 | [海蓝色磨砂玻璃瓶——控制变量比较动态效果](#case-sea-glass-bottle) · [柑橘光环——高端香水产品短片](#case-citrus-halo) |
| [电影叙事 · 7](docs/PROMPT_INDEX.md#02-cinematic-storytelling) | 动作 / 爱情 / 悬疑 / 科幻 / 动画 | 文生视频 / 图生视频 / 视频续接 | [蓝色路线——雨中市场快递员跟拍](#case-blue-route) |
| [社交与生活 · 8](docs/PROMPT_INDEX.md#03-social-ugc) | 体验分享 / 美食 / 健身 / 采访 | 文生视频 / 图生视频 / 参考图生视频 | [第一口——自然的咖啡馆体验分享](#case-first-sip) · [晨曦盐田线——旅行纪录片](#case-salt-line) |
| [人物与对白 · 7](docs/PROMPT_INDEX.md#04-characters-and-references) | 人物 / 服装 / 对白 / 群像 | 参考图生视频 / 图生视频 | [最后一枚齿轮——钟表修复师的默契](#case-clockwork-dialogue) |
| [视觉变换与续接 · 7](docs/PROMPT_INDEX.md#05-editing-and-extension) | 天气替换 / 清理 / 改风格 / 续接 | 视频编辑 / 视频续接 / 图生视频 | [雨入长廊——连续发生的天气变化](#case-rainlit-arcade) |
| [解压材质与声音 · 7](docs/PROMPT_INDEX.md#07-satisfying-materials) | 压沙 / 铜箔 / 水珠 / 拓印 | 文生视频 / 图生视频 | [琥珀果园——一片通透的切面](#case-amber-orchard) |
| [空间与建筑 · 7](docs/PROMPT_INDEX.md#08-spaces-and-transformations) | 家具展开 / 庭院 / 房屋剖面 | 文生视频 / 图生视频 | [展开的中庭——机械温室揭幕](#case-unfolding-atrium) |
| [微缩与超现实 · 7](docs/PROMPT_INDEX.md#09-miniature-and-surreal) | 茶杯渡轮 / 抽屉雨景 / 纸月亮 | 文生视频 / 图生视频 | [蜂蜜面包——微缩烘焙坊故事](#case-honey-loaf) |
| [时尚与表演 · 7](docs/PROMPT_INDEX.md#10-fashion-and-performance) | 裙摆 / 披风 / 衣领投影 / 舞步 | 文生视频 / 图生视频 | [钴蓝回旋——高定礼服的一次完整转身](#case-cobalt-orbit) |

[图文案例](#featured-prompts) · [SeaImagine 创作入口](#create-with-seaimagine)

<a id="visual-index"></a>

<a id="featured-prompts"></a>

## 可复制、可改写的图文提示词

11 个案例均附完整提示词与参考图片。图片用于展示构思，并非已核验的视频结果。

标注来源 Flaq AI 的五个案例保留原始时长和分辨率；其余六个案例按 SeaImagine 当前选项编写。在 SeaImagine 使用源库案例时，请选择 5/10/15 秒和 480p/720p，并重新安排动作时间。

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

<a id="case-clockwork-dialogue"></a>

<a id="seaimagine-clockwork-dialogue"></a>

### 4. 最后一枚齿轮——钟表修复师的默契

![最后一枚齿轮——钟表修复师的默契](assets/clockwork-dialogue.png)

**图生视频参数:** 10s · 16:9 · 720p · [起始帧——打开并保存](assets/clockwork-dialogue.png) · [TXT](prompts/text/zh-CN/clockwork-dialogue.txt)

```text
将参考图制作成一段克制的十秒电影场景。两位成年修复师、敞开的黄铜天文钟、唯一的散放齿轮和月光下的天文台须保持可辨认的一致性。穿藏蓝工作服的短发女性始终在画面左侧，系赭色围裙的灰发男性始终在右侧。隔着工作台，以腰部以上的双人中景取景。

0–3秒：保持双人构图，镜头几乎不可察觉地前推。女性端详钟表，用中文轻声问：“它能走准吗？”男性注视钟内机构。只有女性说话，口型与台词对应。钟表从一开始就在缓慢、轻声滴答。

3–7秒：男性双手放松、保持不动，专注听了一拍钟声，然后用中文回答：“现在能了。”这句台词只有他的嘴唇移动。他不碰散放的齿轮；齿轮始终静止，钟内可见的擒纵机构保持稳定摆动。

7–10秒：她的视线从钟表转向他，露出一丝释然的微笑。他回望她。结束于两人共同的停顿，钟声在中间响起，冷月光勾勒肩部轮廓。

声音：贴近、干净的对白；全程保持空旷房间里均匀、轻细的滴答声。无配乐、无抢话、无齿轮移动声。

散放齿轮始终与钟表分离，无人安装或转动它。保持手部结构、钟内零件、服装、视线和左右位置一致。滴答声从开始就存在，不由任何手势触发；不增加工具、齿轮、字幕、镜头切换或夸张手势。
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

<a id="case-rainlit-arcade"></a>

<a id="seaimagine-rainlit-arcade"></a>

### 7. 雨入长廊——连续发生的天气变化

![雨入长廊——连续发生的天气变化](assets/rainlit-arcade.png)

**图生视频参数:** 10s · 16:9 · 720p · [起始帧——打开并保存](assets/rainlit-arcade.png) · [TXT](prompts/text/zh-CN/rainlit-arcade.txt)

```text
以所给空无一人的装饰艺术风格拱廊为精确首帧，制作十秒天气变化镜头。保持深绿色瓷砖、黄铜饰边、水磨石地面、连续拱门和左墙暖灯不变。远处临街开口保持暮色蓝调。室内抛光石材地面起初全部干燥，保留原有柔和反射；镜头从拱廊内朝向出口。

0–3秒：固定建筑构图，不摇摄、不变焦。远处门槛外，一阵风将街上的雨斜吹而过。零星雨滴最先越过入口，仅将门槛旁的水磨石打湿变深。前景完全干燥。

3–7秒：风势加强，细雨沿同一方向吹入拱廊更深处。不规则的湿润边缘从远端向中部推进；后落下的雨滴清楚地连入已有湿斑。湿润区域形成浅小水洼。保留原有柔和反射；湿润部分的左墙灯光倒影被雨滴打散成颤动的暖色光带。

7–10秒：最后一阵雨雾扫到靠近中部的地面，逐渐停下。最近的一条前景地面保持干燥。雨势减弱，浅水洼中重叠的涟漪逐渐消退，暖色倒影趋于平静。保留蓝色出口前毫无变化的拱门。

声音：先是室外雨声，再有越来越近的雨滴敲石声、一阵低沉风声和轻柔的拱廊回响。无雷声、音乐或人声。

水分进入的路径必须连续可见：不能整片地面突然发亮，也不能在湿润边缘前方凭空出现水洼。积水保持浅薄，灯光稳定，镜头水平，建筑线条不变形。不出现人，不新增植物、新招牌、闪电、洪水、切镜或表面改造。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-amber-orchard"></a>

<a id="seaimagine-amber-orchard"></a>

### 8. 琥珀果园——一片通透的切面

![琥珀果园——一片通透的切面](assets/amber-orchard.png)

**图生视频参数:** 10s · 16:9 · 720p · [起始帧——打开并保存](assets/amber-orchard.png) · [TXT](prompts/text/zh-CN/amber-orchard.txt)

```text
将所给参考图制作成十秒超现实材质特写。保持黑色石盘上的透明琥珀玻璃梨、内部细小气泡和金色细丝。唯一一把窄刀从画面右侧伸入，刀尖按参考图接触梨的右侧。不出现人脸或手。梨是一件坚硬但可以整齐切开的幻想玻璃物体：不可能的材质是刻意设定，但形体结构须连贯。

0–3秒：以固定的四分之三角度微距构图开始，完整保留梨和石盘。暖侧光照亮内部悬着的细丝。刀刃先从现有接触点退开，抬至右侧切面上方，再对准一条竖直切线，只切下一片薄薄的外侧果肉，果梗留在较大的主体上。

3–7秒：一刀连续向下切。刀刃穿过右侧，直至刚刚碰到石盘。唯一的平整切面随刀刃推进，仅分离一片。梨的主体始终直立。薄片轻轻向右外侧倾倒，露出光滑琥珀色切面，随后靠在石盘上，不碎裂。

7–10秒：刀刃竖直抬起离开梨并停住。镜头只轻微前移，展示相互吻合的两个切面。结束时，梨的主体、一片分离薄片和刀都须在画面中清晰可辨。

声音：切割时细微的晶体摩擦声；薄片触石时一声清亮轻响，接着短促的自然余音。无音乐或说话声。

气泡和细丝固定在各自的固体部分内。保持透明度、切口之外的梨形轮廓和石盘位置。不得再次下刀、复制薄片、产生碎屑、液体填充、熔化、新细丝、漂浮碎片或切换镜头。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-unfolding-atrium"></a>

<a id="seaimagine-unfolding-atrium"></a>

### 9. 展开的中庭——机械温室揭幕

![展开的中庭——机械温室揭幕](assets/unfolding-atrium.png)

**图生视频参数:** 10s · 16:9 · 720p · [起始帧——打开并保存](assets/unfolding-atrium.png) · [TXT](prompts/text/zh-CN/unfolding-atrium.txt)

```text
将所给胡桃木与黄铜建筑模型制作成十秒精密机械展示。灰色石质展台、微型楼梯和茂密蕨类保持不变。弧形玻璃屋顶恰由两个弧形半片构成，铰接于中央屋脊上固定的铰轴。两扇起初均关闭，室内从一开始就可透过玻璃看见。

0–3秒：以近距离四分之三角度展示完整模型。暖光掠过胡桃木纹和小巧黄铜铰链筒。镜头开始缓慢、连续上升，轻柔俯看中庭。屋顶先保持关闭一拍，然后两侧外缘屋檐开始抬起，屋脊不分离。

3–7秒：两扇玻璃绕各自固定的屋脊铰链，以相同的稳定速度向上旋转。外缘屋檐抬起，露出下方种满植物的中庭。展现受控的机械开启，每扇都保持原有弧度和刚性黄铜边框。镜头继续上升，刚好露出楼梯井；整个展台始终在画面内。

7–10秒：两扇缓缓抵达相同的开启角度，无回弹地停下。停留展示敞开屋顶框住的蕨类冠层与微型楼梯。一小片柔和日光照进室内更深处，植物自身不动。结束时敞开的结构清晰可读。

声音：与屋顶运动同步的低柔齿轮声；两声几乎同时响起的限位轻响；随后归于安静室内底噪。无音乐或人声。

严格保持两扇屋顶、屋脊上的固定铰链轴和同一室内布局。没有东西生长、从空处展开或改变比例。不得出现滑动屋面、脱落玻璃、弯曲金属、新房间、打开的展台、人或镜头切换。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-cobalt-orbit"></a>

<a id="seaimagine-cobalt-orbit"></a>

### 10. 钴蓝回旋——高定礼服的一次完整转身

![钴蓝回旋——高定礼服的一次完整转身](assets/cobalt-orbit.png)

**图生视频参数:** 10s · 16:9 · 720p · [起始帧——打开并保存](assets/cobalt-orbit.png) · [TXT](prompts/text/zh-CN/cobalt-orbit.txt)

```text
将所给虚构成年时装模特制作成十秒全身高级时装肖像。保留黑色短发、铜质圆片耳环和雕塑感钴蓝褶裥长裙。保留空旷的圆形混凝土房间、顶上天窗和干净地面。她起初面向镜头，双脚落地，双臂放松。取景从头到地面，为裙摆预留充足空间。

0–3秒：镜头完全固定。正面短暂停留后，她以俯视方向的顺时针缓缓转身，用小幅、受控的步伐原地移动。肩膀自然引导动作，厚重的褶裥裙稍后跟随。至第三秒形成清晰的四分之一圈侧身。

3–7秒：沿同一方向，以从容的走秀节奏继续转身。约第五秒经过清晰背面，第七秒转到另一侧面。她始终居于相同地面位置的中央。布料绕腿移动，褶裥轻微开合；裙边擦过地面，不抬起成水平圆盘。耳环只略微摆动。

7–10秒：至第九秒恰好完成一次360度转身，再次面向镜头。脚步先停，裙摆最后的小幅摆动随后停止。余下一秒保持正面姿势，以沉静表情看向镜头。

声音：混凝土地面上的轻脚步声、克制的布料窸窣声和低柔室内底噪。无音乐、对白或掌声。

保持同一人物身份、原有服装结构和衣物下连贯可信的身体。头、手和裙边始终在画面内。天窗光线方向和背景固定。不得绕人物运镜、多转一圈、切镜、改变布料颜色、让裙边腾空、增加配饰或使身体弹性变形。
```

[返回分类索引](#find-the-right-prompt)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 11. 柑橘光环——高端香水产品短片

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

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

## 把选中的镜头，带到 SeaImagine

<a href="https://seaimagine.com/cn/model/grok-imagine-1-5/"><img src="assets/seaimagine-logo.png" width="64" height="64" alt="SeaImagine"></a>

从玻璃瓶的通透质感，到钟表师对话的微小表情，再到礼服旋转时的褶裥变化：选一张参考图和对应提示词，在 SeaImagine 的 Grok Imagine 1.5 页面继续创作。

[瓶身质感](#case-sea-glass-bottle) · [钟表师对白](#case-clockwork-dialogue) · [礼服旋转](#case-cobalt-orbit)

[![产品、材质、建筑与时装，在同一个流动的创作空间相遇。SeaImagine 原创品牌概念图。](assets/seaimagine-creative-atrium.png)](https://seaimagine.com/cn/model/grok-imagine-1-5/)

产品、材质、建筑与时装，在同一个流动的创作空间相遇。SeaImagine 原创品牌概念图。

**[用 SeaImagine 创作这一镜](https://seaimagine.com/cn/model/grok-imagine-1-5/)**

<a id="learn-from-official-and-community-examples"></a>

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

[来源](docs/COMMUNITY.md) · [X / YouTube](docs/SOCIAL_INSPIRATION.md)

<a id="multilingual-prompts"></a>

## 合集与来源署名

共 65 条不同的英语提示词：35 条保留自源库，30 条原创。翻译不计为新增场景；原创提示词尚未生成验证。

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/cn/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
