# Grok Imagine 1.5 提示詞庫 — 繁體中文

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 65 段提示詞，其中 11 個圖文範例提供 15 種語言版本。依分類瀏覽，複製完整提示詞。

![Grok Imagine 1.5 — 展開的提示詞手冊，產品鞋、電車與紙鯨連成同一場景](assets/seaimagine-grok-hero.webp)

改編自 [Flaq AI](https://github.com/flaqai/awesome-grok-imagine)，由 SeaImagine 維護，採用 [MIT](LICENSE) 授權，與 xAI 無隸屬關係。概念配圖不代表 Grok 實測效果。

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## 分類索引

[瀏覽更多提示詞（英文） · 65](docs/PROMPT_INDEX.md)

| 分類 | 包含場景 | 適用模式 | 案例 |
| --- | --- | --- | --- |
| [產品與廣告 · 8](docs/PROMPT_INDEX.md#01-ads-and-products) | 保養品微距 / 咖啡 / 珠寶 / 應用程式廣告 | 文字生成影片 / 圖片生成影片 / 參考圖生成影片 | [海玻璃瓶——控制變因比較動態效果](#case-sea-glass-bottle) · [柑橘光環——精品香水產品短片](#case-citrus-halo) |
| [電影敘事 · 7](docs/PROMPT_INDEX.md#02-cinematic-storytelling) | 動作 / 愛情 / 懸疑 / 科幻 / 動畫 | 文字生成影片 / 圖片生成影片 / 影片延伸 | [藍色路線——雨中市場快遞員跟拍](#case-blue-route) |
| [社群與生活 · 8](docs/PROMPT_INDEX.md#03-social-ugc) | 體驗分享 / 美食 / 健身 / 訪談 | 文字生成影片 / 圖片生成影片 / 參考圖生成影片 | [第一口——自然的咖啡館體驗分享](#case-first-sip) · [晨曦鹽田線——旅行紀錄片](#case-salt-line) |
| [人物與對白 · 7](docs/PROMPT_INDEX.md#04-characters-and-references) | 人物 / 服裝 / 對白 / 群像 | 參考圖生成影片 / 圖片生成影片 | [最後一枚齒輪——鐘錶修復師的默契](#case-clockwork-dialogue) |
| [視覺變換與延伸 · 7](docs/PROMPT_INDEX.md#05-editing-and-extension) | 天氣替換 / 清理 / 風格轉換 / 延伸 | 影片編輯 / 影片延伸 / 圖片生成影片 | [雨入長廊——連續發生的天氣變化](#case-rainlit-arcade) |
| [療癒材質與聲音 · 7](docs/PROMPT_INDEX.md#07-satisfying-materials) | 壓沙 / 銅箔 / 水珠 / 拓印 | 文字生成影片 / 圖片生成影片 | [琥珀果園——一片通透的切面](#case-amber-orchard) |
| [空間與建築 · 7](docs/PROMPT_INDEX.md#08-spaces-and-transformations) | 家具展開 / 庭院 / 房屋剖面 | 文字生成影片 / 圖片生成影片 | [展開的中庭——機械溫室揭幕](#case-unfolding-atrium) |
| [微縮與超現實 · 7](docs/PROMPT_INDEX.md#09-miniature-and-surreal) | 茶杯渡輪 / 抽屜雨景 / 紙月亮 | 文字生成影片 / 圖片生成影片 | [蜂蜜麵包——微縮烘焙坊故事](#case-honey-loaf) |
| [時尚與表演 · 7](docs/PROMPT_INDEX.md#10-fashion-and-performance) | 裙襬 / 披風 / 衣領投影 / 舞步 | 文字生成影片 / 圖片生成影片 | [鈷藍迴旋——高階時裝的一週轉身](#case-cobalt-orbit) |

[圖文範例](#featured-prompts) · [SeaImagine 創作入口](#create-with-seaimagine)

<a id="visual-index"></a>

<a id="featured-prompts"></a>

## 可複製、可改寫的圖文提示詞

11 個範例均附完整提示詞與參考圖片。圖片用於展示構想，並非已核驗的影片結果。

標註來源 Flaq AI 的五個範例保留原始長度與解析度；其餘六個範例依 SeaImagine 目前的選項編寫。在 SeaImagine 使用原始範例時，請選擇 5/10/15 秒與 480p/720p，並重新安排動作時間。

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

<a id="case-clockwork-dialogue"></a>

<a id="seaimagine-clockwork-dialogue"></a>

### 4. 最後一枚齒輪——鐘錶修復師的默契

![最後一枚齒輪——鐘錶修復師的默契](assets/clockwork-dialogue.png)

**圖片轉影片設定:** 10s · 16:9 · 720p · [起始影格——開啟並儲存](assets/clockwork-dialogue.png) · [TXT](prompts/text/zh-TW/clockwork-dialogue.txt)

```text
將參考圖製作成一段剋制的十秒電影場景。兩位成年修復師、敞開的黃銅天文鐘、唯一的散放齒輪和月光下的天文臺須保持可辨認的一致性。穿藏藍工作服的短髮女性始終在畫面左側，系赭色圍裙的灰髮男性始終在右側。隔著工作臺，以腰部以上的雙人中景取景。

0–3秒：保持雙人構圖，鏡頭幾乎不可察覺地前推。女性端詳鐘錶，用中文輕聲問：“它能走準嗎？”男性注視鐘內機構。只有女性說話，口型與臺詞對應。鐘錶從一開始就在緩慢、輕聲滴答。

3–7秒：男性雙手放鬆、保持不動，專注聽了一拍鐘聲，然後用中文回答：“現在能了。”這句臺詞只有他的嘴唇移動。他不碰散放的齒輪；齒輪始終靜止，鍾內可見的擒縱機構保持穩定擺動。

7–10秒：她的視線從鐘錶轉向他，露出一絲釋然的微笑。他回望她。結束於兩人共同的停頓，鐘聲在中間響起，冷月光勾勒肩部輪廓。

聲音：貼近、乾淨的對白；全程保持空曠房間裡均勻、輕細的滴答聲。無配樂、無搶話、無齒輪移動聲。

散放齒輪始終與鐘錶分離，無人安裝或轉動它。保持手部結構、鍾內零件、服裝、視線和左右位置一致。滴答聲從開始就存在，不由任何手勢觸發；不增加工具、齒輪、字幕、鏡頭切換或誇張手勢。
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

<a id="case-rainlit-arcade"></a>

<a id="seaimagine-rainlit-arcade"></a>

### 7. 雨入長廊——連續發生的天氣變化

![雨入長廊——連續發生的天氣變化](assets/rainlit-arcade.png)

**圖片轉影片設定:** 10s · 16:9 · 720p · [起始影格——開啟並儲存](assets/rainlit-arcade.png) · [TXT](prompts/text/zh-TW/rainlit-arcade.txt)

```text
以所給空無一人的裝飾藝術風格拱廊為精確首幀，製作十秒天氣變化鏡頭。保持深綠色瓷磚、黃銅飾邊、水磨石地面、連續拱門和左牆暖燈不變。遠處臨街開口保持暮色藍調。室內拋光石材地面起初全部乾燥，保留原有柔和反射；鏡頭從拱廊內朝向出口。

0–3秒：固定建築構圖，不搖攝、不變焦。遠處門檻外，一陣風將街上的雨斜吹而過。零星雨滴最先越過入口，僅將門檻旁的水磨石打溼變深。前景完全乾燥。

3–7秒：風勢加強，細雨沿同一方向吹入拱廊更深處。不規則的溼潤邊緣從遠端向中部推進；後落下的雨滴清楚地連入已有溼斑。溼潤區域形成淺小水窪。保留原有柔和反射；溼潤部分的左牆燈光倒影被雨滴打散成顫動的暖色光帶。

7–10秒：最後一陣雨霧掃到靠近中部的地面，逐漸停下。最近的一條前景地面保持乾燥。雨勢減弱，淺水窪中重疊的漣漪逐漸消退，暖色倒影趨於平靜。保留藍色出口前毫無變化的拱門。

聲音：先是室外雨聲，再有越來越近的雨滴敲石聲、一陣低沉風聲和輕柔的拱廊迴響。無雷聲、音樂或人聲。

水分進入的路徑必須連續可見：不能整片地面突然發亮，也不能在溼潤邊緣前方憑空出現水窪。積水保持淺薄，燈光穩定，鏡頭水平，建築線條不變形。不出現人，不新增植物、新招牌、閃電、洪水、切鏡或表面改造。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-amber-orchard"></a>

<a id="seaimagine-amber-orchard"></a>

### 8. 琥珀果園——一片通透的切面

![琥珀果園——一片通透的切面](assets/amber-orchard.png)

**圖片轉影片設定:** 10s · 16:9 · 720p · [起始影格——開啟並儲存](assets/amber-orchard.png) · [TXT](prompts/text/zh-TW/amber-orchard.txt)

```text
將所給參考圖製作成十秒超現實材質特寫。保持黑色石盤上的透明琥珀玻璃梨、內部細小氣泡和金色細絲。唯一一把窄刀從畫面右側伸入，刀尖按參考圖接觸梨的右側。不出現人臉或手。梨是一件堅硬但可以整齊切開的幻想玻璃物體：不可能的材質是刻意設定，但形體結構須連貫。

0–3秒：以固定的四分之三角度微距構圖開始，完整保留梨和石盤。暖側光照亮內部懸著的細絲。刀刃先從現有接觸點退開，抬至右側切面上方，再對準一條豎直切線，只切下一片薄薄的外側果肉，果梗留在較大的主體上。

3–7秒：一刀連續向下切。刀刃穿過右側，直至剛剛碰到石盤。唯一的平整切面隨刀刃推進，僅分離一片。梨的主體始終直立。薄片輕輕向右外側傾倒，露出光滑琥珀色切面，隨後靠在石盤上，不碎裂。

7–10秒：刀刃豎直抬起離開梨並停住。鏡頭只輕微前移，展示相互吻合的兩個切面。結束時，梨的主體、一片分離薄片和刀都須在畫面中清晰可辨。

聲音：切割時細微的晶體摩擦聲；薄片觸石時一聲清亮輕響，接著短促的自然餘音。無音樂或說話聲。

氣泡和細絲固定在各自的固體部分內。保持透明度、切口之外的梨形輪廓和石盤位置。不得再次下刀、複製薄片、產生碎屑、液體填充、熔化、新細絲、漂浮碎片或切換鏡頭。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-unfolding-atrium"></a>

<a id="seaimagine-unfolding-atrium"></a>

### 9. 展開的中庭——機械溫室揭幕

![展開的中庭——機械溫室揭幕](assets/unfolding-atrium.png)

**圖片轉影片設定:** 10s · 16:9 · 720p · [起始影格——開啟並儲存](assets/unfolding-atrium.png) · [TXT](prompts/text/zh-TW/unfolding-atrium.txt)

```text
將所給胡桃木與黃銅建築模型製作成十秒精密機械展示。灰色石質展臺、微型樓梯和茂密蕨類保持不變。弧形玻璃屋頂恰由兩個弧形半片構成，鉸接於中央屋脊上固定的鉸軸。兩扇起初均關閉，室內從一開始就可透過玻璃看見。

0–3秒：以近距離四分之三角度展示完整模型。暖光掠過胡桃木紋和小巧黃銅鉸鏈筒。鏡頭開始緩慢、連續上升，輕柔俯看中庭。屋頂先保持關閉一拍，然後兩側外緣屋簷開始抬起，屋脊不分離。

3–7秒：兩扇玻璃繞各自固定的屋脊鉸鏈，以相同的穩定速度向上旋轉。外緣屋簷抬起，露出下方種滿植物的中庭。展現受控的機械開啟，每扇都保持原有弧度和剛性黃銅邊框。鏡頭繼續上升，剛好露出樓梯井；整個展臺始終在畫面內。

7–10秒：兩扇緩緩抵達相同的開啟角度，無回彈地停下。停留展示敞開屋頂框住的蕨類冠層與微型樓梯。一小片柔和日光照進室內更深處，植物自身不動。結束時敞開的結構清晰可讀。

聲音：與屋頂運動同步的低柔齒輪聲；兩聲幾乎同時響起的限位輕響；隨後歸於安靜室內底噪。無音樂或人聲。

嚴格保持兩扇屋頂、屋脊上的固定鉸鏈軸和同一室內佈局。沒有東西生長、從空處展開或改變比例。不得出現滑動屋面、脫落玻璃、彎曲金屬、新房間、開啟的展臺、人或鏡頭切換。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-cobalt-orbit"></a>

<a id="seaimagine-cobalt-orbit"></a>

### 10. 鈷藍迴旋——高階時裝的一週轉身

![鈷藍迴旋——高階時裝的一週轉身](assets/cobalt-orbit.png)

**圖片轉影片設定:** 10s · 16:9 · 720p · [起始影格——開啟並儲存](assets/cobalt-orbit.png) · [TXT](prompts/text/zh-TW/cobalt-orbit.txt)

```text
將所給虛構成年時裝模特製作成十秒全身高階時裝肖像。保留黑色短髮、銅質圓片耳環和雕塑感鈷藍褶襉長裙。保留空曠的圓形混凝土房間、頂上天窗和乾淨地面。她起初面向鏡頭，雙腳落地，雙臂放鬆。取景從頭到地面，為裙襬預留充足空間。

0–3秒：鏡頭完全固定。正面短暫停留後，她以俯視方向的順時針緩緩轉身，用小幅、受控的步伐原地移動。肩膀自然引導動作，厚重的褶襉裙稍後跟隨。至第三秒形成清晰的四分之一圈側身。

3–7秒：沿同一方向，以從容的走秀節奏繼續轉身。約第五秒經過清晰背面，第七秒轉到另一側面。她始終居於相同地面位置的中央。布料繞腿移動，褶襉輕微開合；裙邊擦過地面，不抬起成水平圓盤。耳環只略微擺動。

7–10秒：至第九秒恰好完成一次360度轉身，再次面向鏡頭。腳步先停，裙襬最後的小幅擺動隨後停止。餘下一秒保持正面姿勢，以沉靜表情看向鏡頭。

聲音：混凝土地面上的輕腳步聲、剋制的布料窸窣聲和低柔室內底噪。無音樂、對白或掌聲。

保持同一人物身份、原有服裝結構和衣物下連貫可信的身體。頭、手和裙邊始終在畫面內。天窗光線方向和背景固定。不得繞人物運鏡、多轉一圈、切鏡、改變布料顏色、讓裙邊騰空、增加配飾或使身體彈性變形。
```

[返回分類索引](#find-the-right-prompt)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 11. 柑橘光環——精品香水產品短片

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

<a href="https://seaimagine.com/tw/model/grok-imagine-1-5/"><img src="assets/seaimagine-logo.png" width="64" height="64" alt="SeaImagine"></a>

從玻璃瓶的通透質感，到鐘錶師對話的細微表情，再到禮服旋轉時的褶襉變化：選一張參考圖和對應提示詞，在 SeaImagine 的 Grok Imagine 1.5 頁面繼續創作。

[瓶身質感](#case-sea-glass-bottle) · [鐘錶師對白](#case-clockwork-dialogue) · [禮服旋轉](#case-cobalt-orbit)

[![產品、材質、建築與時裝，在同一個流動的創作空間相遇。SeaImagine 原創品牌概念圖。](assets/seaimagine-creative-atrium.png)](https://seaimagine.com/tw/model/grok-imagine-1-5/)

產品、材質、建築與時裝，在同一個流動的創作空間相遇。SeaImagine 原創品牌概念圖。

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

共 65 條不同的英語提示詞：35 條保留自來源庫，30 條原創。翻譯不計為新增場景；原創提示詞尚未生成驗證。

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/tw/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
