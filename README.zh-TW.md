# Grok Imagine 1.5 提示詞庫 — 繁體中文

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 38 段可複製的英文提示詞，涵蓋產品廣告、人物短片、奇幻故事等；提供 15 種語言的入門範例與操作指南。

![Grok Imagine 1.5 — 展開的提示詞手冊，產品鞋、電車與紙鯨連成同一場景](assets/seaimagine-grok-hero.webp)

改編自 [Flaq AI](https://github.com/flaqai/awesome-grok-imagine)，由 SeaImagine 維護，採用 [MIT](LICENSE) 授權，與 xAI 無隸屬關係。概念配圖不代表 Grok 實測效果。

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## 你想創作什麼？

| 創作目標 | 從圖文範例開始 |
| --- | --- |
| 產品廣告 | [海玻璃瓶——控制變因比較動態效果](#case-sea-glass-bottle) · [柑橘光環——精品香水產品短片](#case-citrus-halo) |
| 電影感動作場面 | [藍色路線——雨中市場快遞員跟拍](#case-blue-route) |
| 奇幻故事 | [蜂蜜麵包——微縮烘焙坊故事](#case-honey-loaf) |
| 人物對白 | [港口重逢——只呈現一個情緒轉折](#case-harbor-reunion) |
| 生活風格影片 | [第一口——自然的咖啡館體驗分享](#case-first-sip) |
| 旅行短片 | [晨曦鹽田線——旅行紀錄片](#case-salt-line) |
| 動態版面 | [海岸明信片——讓規劃好的圖片動起來](#case-coastal-postcard) |

**瀏覽更多提示詞（英文）:** [廣告與產品](prompts/01-ads-and-products.md) · [電影故事](prompts/02-cinematic-storytelling.md) · [社群與生活風格](prompts/03-social-ugc.md) · [人物與參考素材](prompts/04-characters-and-references.md) · [編輯與延長影片](prompts/05-editing-and-extension.md)

[圖文範例](#featured-prompts) · [網頁操作步驟](#seaimagine-browser-workflow) · [官方與社群作品](#learn-from-official-and-community-examples) · [撰寫指南](#writing-guide)

<a id="featured-prompts"></a>

## 可複製、可改寫的圖文提示詞

從下方選一個主題，儲存起始圖片，再複製完整提示詞。先安排一個動作與一種運鏡；圖片用於呈現構想，並非已驗證的影片成果。

標註來源 Flaq AI 的五個範例保留原始長度與解析度；其餘三個範例依 SeaImagine 目前的選項編寫。在 SeaImagine 使用原始範例時，請選擇 5/10/15 秒與 480p/720p，並重新安排動作時間。

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. 海玻璃瓶——控制變因比較動態效果

![海玻璃瓶——控制變因比較動態效果](assets/seaimagine-sea-glass-bottle.webp)

[起始影格——開啟並儲存](assets/seaimagine-sea-glass-bottle.webp)

**圖片轉影片設定:** 5s · 16:9 · 720p

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

**檢查重點:** 記錄實際使用的模型、長度、解析度、嘗試次數及日期。比較瓶身形狀、水滴移動的連貫性、反射及攝影機運動。一次成功不能證明穩定性。

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. 藍色路線——雨中市場快遞員跟拍

![藍色路線——雨中市場快遞員跟拍](assets/rainy-market-courier-video.webp)

[起始影格——開啟並儲存](assets/rainy-market-courier-video.webp)

**圖片轉影片設定:** 10s · 16:9 · 1080p

[來源：Flaq AI](docs/ATTRIBUTION.md) · [網頁操作步驟](#seaimagine-browser-workflow)

```text
保留提供的圖片中的快遞員、鈷藍色電動機車、貨箱、高架市場、半透明雨棚、濕鋼製步道、燈光與夜間配色。製作一個貼近真實環境、連續的低機位跟拍鏡頭，呈現可信的重量、輪胎抓地力、雨水與懸吊運動。

0–3 秒：機車從原有姿態平穩加速。後輪排開一層薄薄的扇形水花，懸吊經過排水接縫時壓縮。攝影機在車輪高度、車輛側後方跟拍，以相同速度移動，不劇烈晃動。

3–7 秒：快遞員傾身通過一個寬闊的左彎。雨棚隨風彎動，食攤冒出蒸氣，暖色現場燈具在濕地反射中形成柔和光痕。兩只車輪始終保持圓形並接觸地面。

7–10 秒：機車回正，駛向市場中更明亮、開闊的區域。攝影機落後半公尺，顯露前方路線，再保持穩定的結束畫面。

聲音：真實的馬達高頻運轉聲、水花聲、雨打棚頂聲、輕微市場人聲，以及一次懸吊的低沉撞擊聲。不要配樂、對白、警笛或爆炸。

連續性要求：精確保留騎士服裝、頭盔、機車幾何形狀、貨箱、藍色車殼與市場配置。不要車輛變形、車輪扭曲、碰撞、武器、可讀招牌、標誌、瞬移鏡頭或不可能的速度突變。
```

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. 蜂蜜麵包——微縮烘焙坊故事

![蜂蜜麵包——微縮烘焙坊故事](assets/pear-bakery-miniature-video.webp)

[起始影格——開啟並儲存](assets/pear-bakery-miniature-video.webp)

**圖片轉影片設定:** 9s · 16:9 · 1080p

[來源：Flaq AI](docs/ATTRIBUTION.md) · [網頁操作步驟](#seaimagine-browser-workflow)

```text
保留梨子屋烘焙坊、三名微縮麵包師、服裝、臉孔、蜂蜜麵包、烤爐、窗戶、苔蘚、三葉草、月亮、具有觸感的停格動畫材料，以及冷暖色對比。

0–3 秒：以提供的廣角構圖開場，帶有細微的手作停格節奏。兩名麵包師一起抬起溫熱的蜂蜜麵包，雙手始終貼在木板上。一小團麵粉揚起，爐火閃動，第三名麵包師打開販售窗口。

3–7 秒：兩人小心地同步走四步，朝窗口前進。麵包呈現可信的重量，在兩人之間略微下沉。屋外，一片三葉草葉子滴下一滴露水，兩隻螢火蟲在不同的遠近位置飄過。攝影機向右緩緩繞行五度。

7–9 秒：他們把木板推上櫃台，相視露出釋然的微笑，爐火光線穩定下來。結尾讓三個人都在畫面中，麵包位於中央。

聲音：木地板上的細小腳步聲、輕柔爐火劈啪聲、木板吱呀聲、微弱夜蟲聲，以及販售窗口的一聲小鈴響。不要對白、旁白、音樂或文字。

連續性要求：保留人物數量、臉部設計、比例、服裝顏色、梨子形狀、室內配置與手工材質。不要多餘麵包師、光滑的電腦生成質感、橡膠般的肢體、懸浮道具、融化的麵包、鏡頭切換、標誌或類似知名系列的人物設計。
```

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. 港口重逢——只呈現一個情緒轉折

![港口重逢——只呈現一個情緒轉折](assets/seaimagine-harbor-reunion.webp)

[起始影格——開啟並儲存](assets/seaimagine-harbor-reunion.webp)

**圖片轉影片設定:** 10s · 16:9 · 720p

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

**檢查重點:** 不靠大幅度表情變化，情緒是否仍然清楚？如果對白顯得倉促，先刪去向前踏步的動作，再考慮延長時間。製作長片時，另外撰寫下一個鏡頭。

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. 第一口——自然的咖啡館體驗分享

<a href="assets/cozy-cafe-ugc-video.webp"><img src="assets/cozy-cafe-ugc-video.webp" width="420" alt="第一口——自然的咖啡館體驗分享"></a>

[起始影格——開啟並儲存](assets/cozy-cafe-ugc-video.webp)

**圖片轉影片設定:** 10s · 9:16 · 1080p

[來源：Flaq AI](docs/ATTRIBUTION.md) · [網頁操作步驟](#seaimagine-browser-workflow)

```text
把提供的咖啡館照片變成真實、手持拍攝的創作者體驗分享。保留人物的臉、年齡、皮膚紋理、頭髮、苔綠色毛衣、杯子、糕點、窗戶與桌面配置。

0–3 秒：鏡頭自然輕微晃動。她喝完一口，把陶瓷杯放低約十公分，帶著淺笑呼一口氣，視線從窗外轉回鏡頭。蒸氣向上捲起，身後玻璃上的雨痕緩慢匯合。

3–8 秒：她用自然、放鬆的國語說：「口感很滑順，不會太甜——而且真的喝得到燕麥味。」語氣隨意，在「太甜」之後稍作停頓。嘴型緊貼對白，手中的杯子保持穩定。

8–10 秒：她輕輕點頭表示認可，攝影機穩定下來時，她低頭看向糕點。

聲音：近距離手機錄音的人聲、安靜的咖啡館環境底音、遠處牛奶蒸氣機聲、輕柔雨聲、陶瓷杯接觸聲。人聲在前景，環境聲保持低音量。不要背景音樂或字幕。

連續性要求：不要美化臉部、換衣服、多餘手指、重新設計杯子或食物、憑空出現的背景人物、標誌或誇張的網紅動作。
```

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. 晨曦鹽田線——旅行紀錄片

![晨曦鹽田線——旅行紀錄片](assets/coastal-salt-train-documentary.webp)

[起始影格——開啟並儲存](assets/coastal-salt-train-documentary.webp)

**圖片轉影片設定:** 12s · 16:9 · 1080p

[來源：Flaq AI](docs/ATTRIBUTION.md) · [網頁操作步驟](#seaimagine-browser-workflow)

```text
把提供的沿海鹽田場景變成尊重勞動者的觀察式旅行紀錄片。保留兩名工人、奶油色與赭色列車、鹽池、石灰岩山丘、建築、海面、日出方向與低飽和底片配色。

0–4 秒：固定廣角畫面。工人繼續檢查水道：一人用木製工具劃過淺鹵水，另一人扶穩隔板。水波隨工具與晨風變化。列車在中景以平穩速度駛近。

4–9 秒：攝影機緩慢向右搖攝，跟隨列車。車輪始終對齊鐵軌，車廂間距與車窗排列節奏保持一致。一層薄薄海霧從列車後方飄過，陽光逐漸照亮前景鹽晶。

9–12 秒：列車向海岸方向駛過，搖攝緩緩停止。一名工人站起，自然伸展身體，望向鐵路線。最後兩秒保持畫面，留作剪接點。

聲音：輕柔電力列車嗡鳴、有節奏的車輪過接縫聲、掠過淺水的微風、遠處海鷗聲，以及木製工具劃過鹵水的聲音。不要旁白、音樂、人群聲或戲劇化汽笛。

連續性要求：勞動動作真實、人體結構穩定、地景固定、列車設計不變，反射與水體運動符合物理規律。不要現代城市天際線、擺拍遊客、新建築、標誌、可讀招牌、過度飽和的明信片色彩或縮時攝影天空。
```

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. 海岸明信片——讓規劃好的圖片動起來

<a href="assets/seaimagine-coastal-postcard.webp"><img src="assets/seaimagine-coastal-postcard.webp" width="420" alt="海岸明信片——讓規劃好的圖片動起來"></a>

[起始影格——開啟並儲存](assets/seaimagine-coastal-postcard.webp)

**圖片轉影片設定:** 5s · 9:16 · 720p

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

**檢查重點:** 如果畫格邊框融化或場景混在一起，將每一格單獨裁切並生成影片，再用剪輯軟體組合。

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. 柑橘光環——精品香水產品短片

![柑橘光環——精品香水產品短片](assets/citrus-fragrance-product-video.webp)

[起始影格——開啟並儲存](assets/citrus-fragrance-product-video.webp)

**圖片轉影片設定:** 8s · 16:9 · 1080p

[來源：Flaq AI](docs/ATTRIBUTION.md) · [網頁操作步驟](#seaimagine-browser-workflow)

```text
保留提供的圖片中的瓶身設計、玻璃比例、瓶蓋、石灰岩台座、葡萄柚皮、暖象牙色布景與金色側光。製作一段優雅的八秒產品短片。

0–2.5 秒：以近乎固定的微距構圖開場。攝影機極緩慢地向前推進。凝結水珠映著光，兩滴水沿冰涼的玻璃自然滑下。葡萄柚皮從台座上飄起，彷彿被可控制的攝影棚微風托起。

2.5–6 秒：果皮優雅地繞瓶身螺旋一周，不接觸或遮擋瓶蓋。細小的柑橘霧粒穿過逆光。折射與聚焦光斑在厚玻璃中依物理規律移動；瓶身始終完全堅硬、不變形。

6–8 秒：果皮落回原先的弧形，攝影機緩緩停下，一道明亮的鏡面高光沿瓶身邊緣移動一次。以乾淨的產品主畫面結束。

聲音：僅有近距離的攝影棚擬音——果皮條輕柔移動聲、兩聲清脆水滴聲與細微玻璃共鳴。不要人聲、音樂或文字。

連續性要求：不要改變瓶身輪廓、瓶蓋切面、液面高度、台座、配色或背景拱形。不要標籤、標誌、多餘水果、懸浮瓶子、幾何形狀晃動、鏡頭跳動或人造閃光爆發。
```

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

## 依 SeaImagine 的實際介面操作

[SeaImagine · Grok Imagine 1.5](https://seaimagine.com/tw/model/grok-imagine-1-5/)

截圖為 2026 年 9 月 24 日核對的英文介面。各語言介面的文字可能不同；以下透過位置與步驟說明各項控制項。 截圖中已填入玻璃瓶提示詞並選取 720p / 5s / 16:9；Start Frame（起始影格）仍是空的。生成前請先上傳起始圖片。此次未提交任務。

![依 SeaImagine 的實際介面操作](assets/seaimagine-interface.jpg)

1. 開啟連結中的模型頁。選擇 Video（影片），並在模型選單確認 Grok Imagine 1.5。
2. 使用左側的 Start Frame（起始影格）上傳下載的圖片。將完整提示詞貼到大文字框；目前字數計數器允許 2,000 個字元。
3. 在提示詞下方選擇解析度（480p 或 720p）、長度（5s、10s 或 15s）及畫面比例。玻璃瓶範例請選擇 720p、5s、16:9。
4. 查看 Generate（生成）旁的點數，消耗點數會隨設定而變動。點選 Generate 會提交真實任務，可能需要登入或點數。截圖並非已完成的生成成果。
5. 預覽成果，逐項檢查上述容易出錯之處，滿意後再下載。如果原有提示詞要求 6/8/9/12 秒或 1080p，請選擇介面支援的長度並改寫時間區段；解析度使用 720p，不要假設支援 1080p。

<a id="learn-from-official-and-community-examples"></a>

## 學習官方與社群作品的做法

來源貼文標示了創作者與模型版本。請開啟原始貼文觀看；以下實用建議介紹創作方法，不表示我們已經重現這些影片。

### [官方 1.5 Preview 片段——Grok / Heavy Pulp](https://x.com/grok/status/2062225080843747351)

[![官方 1.5 Preview 片段——Grok / Heavy Pulp](https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg)](https://x.com/grok/status/2062225080843747351)

學習將預告片拆成多個獨立短鏡頭來規劃。請區分 Preview 預覽版素材與已發布的 1.5 模型。

### [完成的短片——JSFILMZ](https://x.com/JSFILMZ0412/status/2062480692835938771)

作者表示製作了一部 2.5 分鐘的短片，並討論生成式表演的限制。先練習一段平靜的交流，再透過剪輯多個鏡頭組成更長的故事。

### [先規劃圖片，再製作動態——GENEL](https://x.com/genel_ai/status/2061382998873034825)

[![先規劃圖片，再製作動態——GENEL](https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg)](https://x.com/genel_ai/status/2061382998873034825)

創作者表示先用 ChatGPT Images 2.0 製作拼貼圖，再用 Grok Imagine Video 1.5 生成動態。我們的明信片練習固定畫格邊框，並且每格只安排一個動作。

### [控制變因的比較——JSFILMZ](https://x.com/JSFILMZ0412/status/2061117682515050669)

使用同一張原始圖片及可比較的設定。檢查幾何形狀、運動與聲音，不要直接沿用過去的排名。我們的玻璃瓶練習將這些變因分開檢查。

<details>
<summary>抽樣畫面觀察與驗證限制</summary>

2026 年 9 月 24 日，我們在 X 原始貼文的播放器中抽樣查看了這些畫面：官方影片約 3.6 秒處（頭盔與軍隊）、19.8 秒處（臉部特寫）及 34.6 秒處（燃燒的濱水城市）；GENEL 影片約 0.05 秒處（海邊欄杆）、4.9 秒處（鐵路平交道）及 12 秒處（逆光中的手）。可以學習官方影片如何切換景別，以及 GENEL 如何在不同鏡頭之間維持一致的海岸光線。我們的固定畫格明信片是另一種練習。此次僅抽樣查看畫面，未完整測試動態效果或音訊。

</details>

[來源與觀看紀錄（英文）](docs/COMMUNITY.md)

<a id="writing-guide"></a>

<a id="共用多語言測試陶燈工坊"></a>

<a id="完整資料庫"></a>

<a id="快速使用原則"></a>

## 更多繁體中文內容：撰寫指南與補充練習

[撰寫指南](docs/guides/zh-TW.md)

<a id="multilingual-prompts"></a>

## 合集與來源署名

共 38 段不同的英文提示詞：35 段來自原始資料庫，另外加上這 3 個新練習。翻譯版本不算新增情境。

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/tw/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
