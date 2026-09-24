# Grok Imagine 1.5 提示詞庫 — 繁體中文

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 62 段提示詞，其中 8 個圖文範例提供 15 種語言版本。依分類瀏覽，複製完整提示詞。

![Grok Imagine 1.5 — 展開的提示詞手冊，產品鞋、電車與紙鯨連成同一場景](assets/seaimagine-grok-hero.webp)

改編自 [Flaq AI](https://github.com/flaqai/awesome-grok-imagine)，由 SeaImagine 維護，採用 [MIT](LICENSE) 授權，與 xAI 無隸屬關係。概念配圖不代表 Grok 實測效果。

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## 分類索引

[瀏覽更多提示詞（英文） · 62](docs/PROMPT_INDEX.md)

| 分類 | 包含場景 | 適用模式 | 案例 |
| --- | --- | --- | --- |
| [產品與廣告 · 8](docs/PROMPT_INDEX.md#01-ads-and-products) | 保養品微距 / 咖啡 / 珠寶 / 應用程式廣告 | 文字生成影片 / 圖片生成影片 / 參考圖生成影片 | [海玻璃瓶——控制變因比較動態效果](#case-sea-glass-bottle) · [柑橘光環——精品香水產品短片](#case-citrus-halo) |
| [電影敘事 · 8](docs/PROMPT_INDEX.md#02-cinematic-storytelling) | 動作 / 愛情 / 懸疑 / 科幻 / 動畫 | 文字生成影片 / 圖片生成影片 / 影片延伸 | [藍色路線——雨中市場快遞員跟拍](#case-blue-route) · [海岸明信片——讓規劃好的圖片動起來](#case-coastal-postcard) |
| [社群與生活 · 8](docs/PROMPT_INDEX.md#03-social-ugc) | 體驗分享 / 美食 / 健身 / 訪談 | 文字生成影片 / 圖片生成影片 / 參考圖生成影片 | [第一口——自然的咖啡館體驗分享](#case-first-sip) · [晨曦鹽田線——旅行紀錄片](#case-salt-line) |
| [人物與對白 · 7](docs/PROMPT_INDEX.md#04-characters-and-references) | 人物 / 服裝 / 對白 / 群像 | 參考圖生成影片 / 圖片生成影片 | [港口重逢——只呈現一個情緒轉折](#case-harbor-reunion) |
| [視覺變換與延伸 · 6](docs/PROMPT_INDEX.md#05-editing-and-extension) | 天氣替換 / 清理 / 風格轉換 / 延伸 | 影片編輯 / 影片延伸 | — |
| [療癒材質與聲音 · 6](docs/PROMPT_INDEX.md#07-satisfying-materials) | 壓沙 / 銅箔 / 水珠 / 拓印 | 文字生成影片 | — |
| [空間與建築 · 6](docs/PROMPT_INDEX.md#08-spaces-and-transformations) | 家具展開 / 庭院 / 房屋剖面 | 文字生成影片 | — |
| [微縮與超現實 · 7](docs/PROMPT_INDEX.md#09-miniature-and-surreal) | 茶杯渡輪 / 抽屜雨景 / 紙月亮 | 文字生成影片 / 圖片生成影片 | [蜂蜜麵包——微縮烘焙坊故事](#case-honey-loaf) |
| [時尚與表演 · 6](docs/PROMPT_INDEX.md#10-fashion-and-performance) | 裙襬 / 披風 / 衣領投影 / 舞步 | 文字生成影片 | — |

[圖文範例](#featured-prompts) · [SeaImagine 創作入口](#create-with-seaimagine)

<a id="visual-index"></a>

<a id="featured-prompts"></a>

## 可複製、可改寫的圖文提示詞

8 個範例均附完整提示詞與起始影格圖片。圖片用於呈現構想，並非已驗證的影片成果。

標註來源 Flaq AI 的五個範例保留原始長度與解析度；其餘三個範例依 SeaImagine 目前的選項編寫。在 SeaImagine 使用原始範例時，請選擇 5/10/15 秒與 480p/720p，並重新安排動作時間。

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. 海玻璃瓶——控制變因比較動態效果

![海玻璃瓶——控制變因比較動態效果](assets/seaimagine-sea-glass-bottle.webp)

**圖片轉影片設定:** 5s · 16:9 · 720p · [起始影格——開啟並儲存](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/zh-TW/sea-glass-bottle.txt)

```text
保留淺色石面上唯一的霧面海玻璃瓶、圓柱形瓶蓋、沒有印字的空白正面、
液面高度、地平線及柔和側光。瓶子始終不動。
在五秒內讓攝影機緩慢向右平移，移動距離不超過一個瓶身寬度。
一小滴水沿瓶身正面滑下，在底部停住。背景海浪在失焦中輕輕起伏。
反射效果始終與攝影機及光源的位置一致。
聲音：只有遠處海浪聲；不要音樂、人聲、玻璃碰撞聲或誇張的水花聲。
不剪接，不變焦。保留瓶身輪廓、瓶蓋對齊關係、玻璃質感及物件數量。
避免生成標誌、改變液面高度、扭曲邊緣、物件漂浮或新增道具。
最後一秒保持畫面穩定。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. 藍色路線——雨中市場快遞員跟拍

![藍色路線——雨中市場快遞員跟拍](assets/rainy-market-courier-video.webp)

**圖片轉影片設定:** 10s · 16:9 · 1080p · [起始影格——開啟並儲存](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/zh-TW/blue-route.txt)

[來源：Flaq AI](docs/ATTRIBUTION.md)

```text
保留提供的圖片中的快遞員、鈷藍色電動機車、貨箱、高架市場、半透明雨棚、濕鋼製步道、燈光與夜間配色。製作一個貼近真實環境、連續的低機位跟拍鏡頭，呈現可信的重量、輪胎抓地力、雨水與懸吊運動。

0–3 秒：機車從原有姿態平穩加速。後輪排開一層薄薄的扇形水花，懸吊經過排水接縫時壓縮。攝影機在車輪高度、車輛側後方跟拍，以相同速度移動，不劇烈晃動。

3–7 秒：快遞員傾身通過一個寬闊的左彎。雨棚隨風彎動，食攤冒出蒸氣，暖色現場燈具在濕地反射中形成柔和光痕。兩只車輪始終保持圓形並接觸地面。

7–10 秒：機車回正，駛向市場中更明亮、開闊的區域。攝影機落後半公尺，顯露前方路線，再保持穩定的結束畫面。

聲音：真實的馬達高頻運轉聲、水花聲、雨打棚頂聲、輕微市場人聲，以及一次懸吊的低沉撞擊聲。不要配樂、對白、警笛或爆炸。

連續性要求：精確保留騎士服裝、頭盔、機車幾何形狀、貨箱、藍色車殼與市場配置。不要車輛變形、車輪扭曲、碰撞、武器、可讀招牌、標誌、瞬移鏡頭或不可能的速度突變。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. 蜂蜜麵包——微縮烘焙坊故事

![蜂蜜麵包——微縮烘焙坊故事](assets/pear-bakery-miniature-video.webp)

**圖片轉影片設定:** 9s · 16:9 · 1080p · [起始影格——開啟並儲存](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/zh-TW/honey-loaf.txt)

[來源：Flaq AI](docs/ATTRIBUTION.md)

```text
保留梨子屋烘焙坊、三名微縮麵包師、服裝、臉孔、蜂蜜麵包、烤爐、窗戶、苔蘚、三葉草、月亮、具有觸感的停格動畫材料，以及冷暖色對比。

0–3 秒：以提供的廣角構圖開場，帶有細微的手作停格節奏。兩名麵包師一起抬起溫熱的蜂蜜麵包，雙手始終貼在木板上。一小團麵粉揚起，爐火閃動，第三名麵包師打開販售窗口。

3–7 秒：兩人小心地同步走四步，朝窗口前進。麵包呈現可信的重量，在兩人之間略微下沉。屋外，一片三葉草葉子滴下一滴露水，兩隻螢火蟲在不同的遠近位置飄過。攝影機向右緩緩繞行五度。

7–9 秒：他們把木板推上櫃台，相視露出釋然的微笑，爐火光線穩定下來。結尾讓三個人都在畫面中，麵包位於中央。

聲音：木地板上的細小腳步聲、輕柔爐火劈啪聲、木板吱呀聲、微弱夜蟲聲，以及販售窗口的一聲小鈴響。不要對白、旁白、音樂或文字。

連續性要求：保留人物數量、臉部設計、比例、服裝顏色、梨子形狀、室內配置與手工材質。不要多餘麵包師、光滑的電腦生成質感、橡膠般的肢體、懸浮道具、融化的麵包、鏡頭切換、標誌或類似知名系列的人物設計。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. 港口重逢——只呈現一個情緒轉折

![港口重逢——只呈現一個情緒轉折](assets/seaimagine-harbor-reunion.webp)

**圖片轉影片設定:** 10s · 16:9 · 720p · [起始影格——開啟並儲存](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/zh-TW/harbor-reunion.txt)

```text
保留提供的圖片中的兩名成年人、各自的臉孔、深藍色與奶油色服裝、木碼頭及柔和晨光。
始終讓兩人出現在同一個中遠景構圖中。
0–3 秒：左側的人注意到前來的朋友，向前踏一小步。
其肩膀放鬆下來；朋友回以淡淡的微笑。雙手保持可見，姿勢自然放鬆。
3–7 秒：左側的人以自然的國語說：「你來了。」朋友點一次頭。
對白要含蓄，不哭泣，也不做誇張表情。
7–10 秒：兩人都轉頭望向停泊的小船。最後一秒保持畫面，方便銜接下一個鏡頭。
鏡頭：僅緩慢推進一次，不切反打鏡頭，不剪接。
聲音：近距離、清晰可辨的對白，輕柔的港口水聲及遠處海鷗聲；不要音樂或字幕。
保持兩人身分、服裝、碼頭結構、船隻位置及晨光方向一致。
避免多出人物、戲劇化動作、臉部磨皮、多餘手指及鏡頭跳動。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. 第一口——自然的咖啡館體驗分享

<a href="assets/cozy-cafe-ugc-video.webp"><img src="assets/cozy-cafe-ugc-video.webp" width="480" alt="第一口——自然的咖啡館體驗分享"></a>

**圖片轉影片設定:** 10s · 9:16 · 1080p · [起始影格——開啟並儲存](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/zh-TW/first-sip.txt)

[來源：Flaq AI](docs/ATTRIBUTION.md)

```text
把提供的咖啡館照片變成真實、手持拍攝的創作者體驗分享。保留人物的臉、年齡、皮膚紋理、頭髮、苔綠色毛衣、杯子、糕點、窗戶與桌面配置。

0–3 秒：鏡頭自然輕微晃動。她喝完一口，把陶瓷杯放低約十公分，帶著淺笑呼一口氣，視線從窗外轉回鏡頭。蒸氣向上捲起，身後玻璃上的雨痕緩慢匯合。

3–8 秒：她用自然、放鬆的國語說：「口感很滑順，不會太甜——而且真的喝得到燕麥味。」語氣隨意，在「太甜」之後稍作停頓。嘴型緊貼對白，手中的杯子保持穩定。

8–10 秒：她輕輕點頭表示認可，攝影機穩定下來時，她低頭看向糕點。

聲音：近距離手機錄音的人聲、安靜的咖啡館環境底音、遠處牛奶蒸氣機聲、輕柔雨聲、陶瓷杯接觸聲。人聲在前景，環境聲保持低音量。不要背景音樂或字幕。

連續性要求：不要美化臉部、換衣服、多餘手指、重新設計杯子或食物、憑空出現的背景人物、標誌或誇張的網紅動作。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. 晨曦鹽田線——旅行紀錄片

![晨曦鹽田線——旅行紀錄片](assets/coastal-salt-train-documentary.webp)

**圖片轉影片設定:** 12s · 16:9 · 1080p · [起始影格——開啟並儲存](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/zh-TW/salt-line.txt)

[來源：Flaq AI](docs/ATTRIBUTION.md)

```text
把提供的沿海鹽田場景變成尊重勞動者的觀察式旅行紀錄片。保留兩名工人、奶油色與赭色列車、鹽池、石灰岩山丘、建築、海面、日出方向與低飽和底片配色。

0–4 秒：固定廣角畫面。工人繼續檢查水道：一人用木製工具劃過淺鹵水，另一人扶穩隔板。水波隨工具與晨風變化。列車在中景以平穩速度駛近。

4–9 秒：攝影機緩慢向右搖攝，跟隨列車。車輪始終對齊鐵軌，車廂間距與車窗排列節奏保持一致。一層薄薄海霧從列車後方飄過，陽光逐漸照亮前景鹽晶。

9–12 秒：列車向海岸方向駛過，搖攝緩緩停止。一名工人站起，自然伸展身體，望向鐵路線。最後兩秒保持畫面，留作剪接點。

聲音：輕柔電力列車嗡鳴、有節奏的車輪過接縫聲、掠過淺水的微風、遠處海鷗聲，以及木製工具劃過鹵水的聲音。不要旁白、音樂、人群聲或戲劇化汽笛。

連續性要求：勞動動作真實、人體結構穩定、地景固定、列車設計不變，反射與水體運動符合物理規律。不要現代城市天際線、擺拍遊客、新建築、標誌、可讀招牌、過度飽和的明信片色彩或縮時攝影天空。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. 海岸明信片——讓規劃好的圖片動起來

<a href="assets/seaimagine-coastal-postcard.webp"><img src="assets/seaimagine-coastal-postcard.webp" width="480" alt="海岸明信片——讓規劃好的圖片動起來"></a>

**圖片轉影片設定:** 5s · 9:16 · 720p · [起始影格——開啟並儲存](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/zh-TW/coastal-postcard.txt)

```text
讓這張三格海岸明信片動起來，不改變版面或邊框。
完整保留所有物件與色彩。上格：杯中升起一縷細細的蒸氣。
中格：港口水面泛起輕微漣漪，陽光在水面閃動。
下格：只有畫面中既有紙張的一角被微風輕輕掀起，然後落下。
每個動作都限制在各自的畫格內。五秒內始終完整顯示所有畫格。
鏡頭：固定，不變焦、不搖移、不剪接，畫格之間不轉場。
聲音：輕微水聲及柔和的紙張沙沙聲；不要對白、音樂、字幕或新增文字。
保留杯柄、窗框、地圖標記、各格尺寸及閱讀順序。
避免畫格融合、憑空產生新場景、重畫字母，或讓物件跨越邊框移動。
結尾時紙角落穩，原有構圖保持完整。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. 柑橘光環——精品香水產品短片

![柑橘光環——精品香水產品短片](assets/citrus-fragrance-product-video.webp)

**圖片轉影片設定:** 8s · 16:9 · 1080p · [起始影格——開啟並儲存](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/zh-TW/citrus-halo.txt)

[來源：Flaq AI](docs/ATTRIBUTION.md)

```text
保留提供的圖片中的瓶身設計、玻璃比例、瓶蓋、石灰岩台座、葡萄柚皮、暖象牙色布景與金色側光。製作一段優雅的八秒產品短片。

0–2.5 秒：以近乎固定的微距構圖開場。攝影機極緩慢地向前推進。凝結水珠映著光，兩滴水沿冰涼的玻璃自然滑下。葡萄柚皮從台座上飄起，彷彿被可控制的攝影棚微風托起。

2.5–6 秒：果皮優雅地繞瓶身螺旋一周，不接觸或遮擋瓶蓋。細小的柑橘霧粒穿過逆光。折射與聚焦光斑在厚玻璃中依物理規律移動；瓶身始終完全堅硬、不變形。

6–8 秒：果皮落回原先的弧形，攝影機緩緩停下，一道明亮的鏡面高光沿瓶身邊緣移動一次。以乾淨的產品主畫面結束。

聲音：僅有近距離的攝影棚擬音——果皮條輕柔移動聲、兩聲清脆水滴聲與細微玻璃共鳴。不要人聲、音樂或文字。

連續性要求：不要改變瓶身輪廓、瓶蓋切面、液面高度、台座、配色或背景拱形。不要標籤、標誌、多餘水果、懸浮瓶子、幾何形狀晃動、鏡頭跳動或人造閃光爆發。
```

[返回分類索引](#find-the-right-prompt)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

## 把選中的鏡頭，帶到 SeaImagine

從前面的玻璃瓶產品短片、港口對白或動態明信片選一個，帶上對應圖片與完整提示詞，在 SeaImagine 的 Grok Imagine 1.5 頁面繼續創作。產品短片看材質，人物短片看表演，排版動畫看構圖。

[產品質感](#case-sea-glass-bottle) · [人物對白](#case-harbor-reunion) · [排版動畫](#case-coastal-postcard)

[![SeaImagine · Grok Imagine 1.5](assets/seaimagine-interface.jpg)](https://seaimagine.com/tw/model/grok-imagine-1-5/)

實際介面：已填入玻璃瓶提示詞，720p · 5s · 16:9；起始圖片尚待上傳，尚未生成。

**[用 SeaImagine 創作這個鏡頭](https://seaimagine.com/tw/model/grok-imagine-1-5/)**

<a id="learn-from-official-and-community-examples"></a>

<a id="writing-guide"></a>

<a id="共用多語言測試陶燈工坊"></a>

<a id="完整資料庫"></a>

<a id="快速使用原則"></a>

## 參考資料

[撰寫參考](docs/guides/zh-TW.md) · [參數與操作參考](docs/workflows/zh-TW.md) · [SeaImagine](https://seaimagine.com/tw/model/grok-imagine-1-5/)

[來源](docs/COMMUNITY.md) · [X / YouTube](docs/SOCIAL_INSPIRATION.md)

<a id="multilingual-prompts"></a>

## 合集與來源署名

共 62 條不同的英語提示詞：35 條保留自來源庫，27 條原創。最新 24 條根據社群媒體題材重新創作，尚未生成驗證。翻譯不計為新增場景。

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/tw/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
