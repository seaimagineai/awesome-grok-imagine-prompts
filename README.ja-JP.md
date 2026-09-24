# Grok Imagine 1.5 プロンプト集 — 日本語

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 38 本のプロンプトを収録。そのうち画像付きの 8 作例は 15 言語で掲載しています。カテゴリ別に探して、プロンプト全文をコピーできます。

![Grok Imagine 1.5 — 開いたプロンプト手帳から、靴・路面電車・紙のクジラが一つの世界へ広がる](assets/seaimagine-grok-hero.webp)

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) をもとに再編集し、SeaImagine が管理しています。[MIT](LICENSE) ライセンスで公開しており、xAI とは独立したプロジェクトです。コンセプト画像は Grok で実測した出力を示すものではありません。

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## カテゴリ索引

| 作りたいもの | 画像付き作例 |
| --- | --- |
| 商品広告 | [シーグラスのボトル — 条件をそろえて動きを比較する](#case-sea-glass-bottle) · [シトラス・ヘイロー — 高級香水の商品映像](#case-citrus-halo) |
| 映画のようなアクション | [ブルールート — 雨の市場を走る配達員の追跡ショット](#case-blue-route) |
| ファンタジー | [ハニーローフ — ミニチュアのパン屋の物語](#case-honey-loaf) |
| 人物の会話 | [港での再会 — 一つの感情の変化を描く](#case-harbor-reunion) |
| ライフスタイル動画 | [最初のひと口 — 自然なカフェ体験レビュー](#case-first-sip) |
| 旅行映像 | [夜明けの塩田線 — 旅行ドキュメンタリー](#case-salt-line) |
| 動くレイアウト | [海辺のポストカード — 構成を決めた画像を動かす](#case-coastal-postcard) |

[画像付きの例](#featured-prompts) · [公式とコミュニティの作品](#learn-from-official-and-community-examples) · [設定と操作の参考資料](#writing-guide)

<a id="visual-index"></a>

### 画像付き作例一覧

8 件の作例にプロンプト全文と開始フレーム画像を掲載。画像は構想を示すもので、検証済みの動画出力ではありません。

出典が Flaq AI と表示された5つの例は、元の長さと解像度を保存しています。残る3つは SeaImagine の現在の選択肢に合わせて書いています。元の例を SeaImagine で使う場合は 5/10/15 秒と 480p/720p を選び、動作の時間配分を組み直してください。

| | |
| --- | --- |
| <a href="#case-sea-glass-bottle"><img src="assets/seaimagine-sea-glass-bottle.webp" height="180" alt="シーグラスのボトル — 条件をそろえて動きを比較する"></a><br>[1. シーグラスのボトル — 条件をそろえて動きを比較する](#case-sea-glass-bottle)<br>5s · 16:9 · 720p | <a href="#case-blue-route"><img src="assets/rainy-market-courier-video.webp" height="180" alt="ブルールート — 雨の市場を走る配達員の追跡ショット"></a><br>[2. ブルールート — 雨の市場を走る配達員の追跡ショット](#case-blue-route)<br>10s · 16:9 · 1080p |
| <a href="#case-honey-loaf"><img src="assets/pear-bakery-miniature-video.webp" height="180" alt="ハニーローフ — ミニチュアのパン屋の物語"></a><br>[3. ハニーローフ — ミニチュアのパン屋の物語](#case-honey-loaf)<br>9s · 16:9 · 1080p | <a href="#case-harbor-reunion"><img src="assets/seaimagine-harbor-reunion.webp" height="180" alt="港での再会 — 一つの感情の変化を描く"></a><br>[4. 港での再会 — 一つの感情の変化を描く](#case-harbor-reunion)<br>10s · 16:9 · 720p |
| <a href="#case-first-sip"><img src="assets/cozy-cafe-ugc-video.webp" height="180" alt="最初のひと口 — 自然なカフェ体験レビュー"></a><br>[5. 最初のひと口 — 自然なカフェ体験レビュー](#case-first-sip)<br>10s · 9:16 · 1080p | <a href="#case-salt-line"><img src="assets/coastal-salt-train-documentary.webp" height="180" alt="夜明けの塩田線 — 旅行ドキュメンタリー"></a><br>[6. 夜明けの塩田線 — 旅行ドキュメンタリー](#case-salt-line)<br>12s · 16:9 · 1080p |
| <a href="#case-coastal-postcard"><img src="assets/seaimagine-coastal-postcard.webp" height="180" alt="海辺のポストカード — 構成を決めた画像を動かす"></a><br>[7. 海辺のポストカード — 構成を決めた画像を動かす](#case-coastal-postcard)<br>5s · 9:16 · 720p | <a href="#case-citrus-halo"><img src="assets/citrus-fragrance-product-video.webp" height="180" alt="シトラス・ヘイロー — 高級香水の商品映像"></a><br>[8. シトラス・ヘイロー — 高級香水の商品映像](#case-citrus-halo)<br>8s · 16:9 · 1080p |

**ほかのプロンプトを見る（英語） · 30**

| カテゴリ | 作例索引 |
| --- | --- |
| [広告と商品 · 6](prompts/01-ads-and-products.md) | [1. Dew Drop Laboratory — skincare serum macro](prompts/01-ads-and-products.md#1-dew-drop-laboratory--skincare-serum-macro) · [2. Cold Brew Eclipse — coffee launch film](prompts/01-ads-and-products.md#2-cold-brew-eclipse--coffee-launch-film) · [3. Street-to-Studio — performance shoe demonstration](prompts/01-ads-and-products.md#3-street-to-studio--performance-shoe-demonstration) · [4. Doorstep Dinner — food delivery social ad](prompts/01-ads-and-products.md#4-doorstep-dinner--food-delivery-social-ad) · [5. Silver Current — artisan jewelry reveal](prompts/01-ads-and-products.md#5-silver-current--artisan-jewelry-reveal) · [6. One Tap Away — clean mobile app promo](prompts/01-ads-and-products.md#6-one-tap-away--clean-mobile-app-promo) |
| [映画のような物語 · 6](prompts/02-cinematic-storytelling.md) | [1. Last Tram Note — restrained urban romance](prompts/02-cinematic-storytelling.md#1-last-tram-note--restrained-urban-romance) · [2. Room 407 — quiet hotel mystery](prompts/02-cinematic-storytelling.md#2-room-407--quiet-hotel-mystery) · [3. Glasshouse Pursuit — grounded parkour action](prompts/02-cinematic-storytelling.md#3-glasshouse-pursuit--grounded-parkour-action) · [4. Tidekeeper — coastal fantasy ritual](prompts/02-cinematic-storytelling.md#4-tidekeeper--coastal-fantasy-ritual) · [5. Paper Moon Delivery — hand-drawn animation](prompts/02-cinematic-storytelling.md#5-paper-moon-delivery--hand-drawn-animation) · [6. Europa Signal — hard-science discovery](prompts/02-cinematic-storytelling.md#6-europa-signal--hard-science-discovery) |
| [SNS とライフスタイル · 6](prompts/03-social-ugc.md) | [1. Shelf Test — honest skincare mini-review](prompts/03-social-ugc.md#1-shelf-test--honest-skincare-mini-review) · [2. Twelve-Minute Noodles — one-pan recipe reel](prompts/03-social-ugc.md#2-twelve-minute-noodles--one-pan-recipe-reel) · [3. First Set — realistic morning fitness log](prompts/03-social-ugc.md#3-first-set--realistic-morning-fitness-log) · [4. One Question, One Corner — street interview](prompts/03-social-ugc.md#4-one-question-one-corner--street-interview) · [5. Clay Cup Morning — tactile pottery ASMR](prompts/03-social-ugc.md#5-clay-cup-morning--tactile-pottery-asmr) · [6. Umbrella Reset — seamless pet comedy loop](prompts/03-social-ugc.md#6-umbrella-reset--seamless-pet-comedy-loop) |
| [人物と参照素材 · 6](prompts/04-characters-and-references.md) | [1. Harbor Cartographer — consistent character introduction](prompts/04-characters-and-references.md#1-harbor-cartographer--consistent-character-introduction) · [2. Linen Set — virtual try-on walk test](prompts/04-characters-and-references.md#2-linen-set--virtual-try-on-walk-test) · [3. Counter Demo — product placement without redesign](prompts/04-characters-and-references.md#3-counter-demo--product-placement-without-redesign) · [4. Two Voices, One Repair — synchronized dialogue scene](prompts/04-characters-and-references.md#4-two-voices-one-repair--synchronized-dialogue-scene) · [5. Sunday Table — consistent three-person ensemble](prompts/04-characters-and-references.md#5-sunday-table--consistent-three-person-ensemble) · [6. Parcel Finch — reusable brand mascot motion](prompts/04-characters-and-references.md#6-parcel-finch--reusable-brand-mascot-motion) |
| [編集と延長 · 6](prompts/05-editing-and-extension.md) | [1. Blue Hour Conversion — day-to-night architectural edit](prompts/05-editing-and-extension.md#1-blue-hour-conversion--day-to-night-architectural-edit) · [2. First Snow — controlled weather replacement](prompts/05-editing-and-extension.md#2-first-snow--controlled-weather-replacement) · [3. Clean Plate — remove one distracting object](prompts/05-editing-and-extension.md#3-clean-plate--remove-one-distracting-object) · [4. Practical Miniature — change rendering style, keep motion](prompts/05-editing-and-extension.md#4-practical-miniature--change-rendering-style-keep-motion) · [5. Beyond the Gate — continue a travel shot](prompts/05-editing-and-extension.md#5-beyond-the-gate--continue-a-travel-shot) · [6. Turntable Loop — repair a product animation into a seamless cycle](prompts/05-editing-and-extension.md#6-turntable-loop--repair-a-product-animation-into-a-seamless-cycle) |

<a id="featured-prompts"></a>

## コピーしてアレンジできる画像付きプロンプト

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. シーグラスのボトル — 条件をそろえて動きを比較する

**画像から動画を生成する設定:** 5s · 16:9 · 720p · [開始フレーム — 開いて保存](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/ja-JP/sea-glass-bottle.txt)

```text
淡い色の石の上にある1本のすりガラス状のシーグラスボトル、円筒形のキャップ、
印刷のない無地の正面、液面の高さ、水平線、柔らかな側光を保つ。ボトルは動かさない。
5秒間でカメラをゆっくり右へスライドさせる。移動幅はボトル1本分の幅以内にする。
小さな水滴が1滴、正面を伝って下がり、底で止まる。背景の海の波はぼけたまま穏やかに動く。
反射はカメラと光源の位置に整合させる。
音声：遠くの波音のみ。音楽、声、ガラスの衝突音、誇張した水しぶきの音は入れない。
カットやズームは不要。ボトルの輪郭、キャップの位置関係、ガラスの質感、物体の数を保つ。
ロゴの生成、液面の変化、縁のゆがみ、物体の浮遊、小道具の追加を避ける。
最後の1秒は安定した画を保つ。
```

[カテゴリ索引に戻る](#find-the-right-prompt) · [画像付き作例一覧](#visual-index)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. ブルールート — 雨の市場を走る配達員の追跡ショット

**画像から動画を生成する設定:** 10s · 16:9 · 1080p · [開始フレーム — 開いて保存](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/ja-JP/blue-route.txt)

[出典：Flaq AI](docs/ATTRIBUTION.md)

```text
入力画像の配達員、コバルトブルーの電動バイク、荷箱、高架の市場、半透明の日よけ、ぬれた鉄製通路、照明、夜の配色を保つ。重量、タイヤのグリップ、雨、サスペンションに説得力のある、現実的で連続した低い位置からの追跡ショットを作る。

0–3 秒：バイクは元の姿勢から滑らかに加速する。後輪が薄い扇形の水しぶきを上げ、排水用の継ぎ目を越えるとサスペンションが沈む。カメラは車輪の高さでバイクの横やや後ろを同じ速度で追い、激しく揺れない。

3–7 秒：配達員が体を傾け、大きな左カーブを通る。日よけが風でたわみ、屋台から湯気が流れ、暖色の現場照明がぬれた面の反射に柔らかな光の筋を作る。両輪を丸いまま地面に接触させ続ける。

7–10 秒：バイクが直立に戻り、市場の明るく開けた場所へ進む。カメラは半メートル後退し、前方のルートを見せてから、安定した終わりの画を保つ。

音声：リアルな電動モーターの高い駆動音、水しぶき、日よけを打つ雨、控えめな市場の人声、サスペンションが一度ドンと鳴る音。劇伴、台詞、サイレン、爆発は不要。

連続性の固定：ライダーの服、ヘルメット、バイクの形状、荷箱、青いパネル、市場の配置を正確に保つ。車両の変形、車輪のゆがみ、衝突、武器、読める看板、ロゴ、瞬間移動するカメラ、不可能な速度変化を入れない。
```

[カテゴリ索引に戻る](#find-the-right-prompt) · [画像付き作例一覧](#visual-index)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. ハニーローフ — ミニチュアのパン屋の物語

**画像から動画を生成する設定:** 9s · 16:9 · 1080p · [開始フレーム — 開いて保存](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/ja-JP/honey-loaf.txt)

[出典：Flaq AI](docs/ATTRIBUTION.md)

```text
梨の家のパン屋、3人の小さなパン職人、衣装、顔、ハニーローフ、オーブン、窓、苔、クローバー、月、手触りを感じるストップモーション素材、暖色と寒色の対比を保つ。

0–3 秒：入力画像のワイド構図から、わずかな手作りストップモーションのリズムで始める。2人の職人が温かいハニーローフを一緒に持ち上げ、手は木の板に接したままにする。小さな粉煙が立ち、オーブンの火が揺れ、3人目が販売窓を開ける。

3–7 秒：2人は窓に向かって慎重に歩調を合わせて4歩進む。パンには本物らしい重みがあり、2人の間で少し下がる。外ではクローバーの葉1枚から露が1滴落ち、2匹のホタルが異なる奥行きで漂う。カメラは右へ穏やかに5度回り込む。

7–9 秒：2人は板をカウンターへ滑らせ、ほっとした笑みを交わす。オーブンの光が落ち着く。3人全員が見え、パンが中央にある画で終える。

音声：木の上の小さな足音、柔らかな炉のパチパチ音、板のきしみ、かすかな夜の虫、販売窓の小さなベル1回。台詞、ナレーション、音楽、文字は不要。

連続性の固定：人数、顔のデザイン、縮尺、服の色、梨の形、室内配置、手作りの質感を保つ。職人の追加、光沢のあるCG、ゴムのような手足、浮く小道具、溶けるパン、カット、ロゴ、既存シリーズを思わせるキャラクターデザインを入れない。
```

[カテゴリ索引に戻る](#find-the-right-prompt) · [画像付き作例一覧](#visual-index)

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. 港での再会 — 一つの感情の変化を描く

**画像から動画を生成する設定:** 10s · 16:9 · 720p · [開始フレーム — 開いて保存](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/ja-JP/harbor-reunion.txt)

```text
入力画像にある大人2人、それぞれの顔、紺色とクリーム色の服、木の桟橋、柔らかな朝の光を保つ。
2人を同じミディアムワイドの構図に収め続ける。
0–3 秒：左の人物が到着した友人に気づき、小さく一歩前に出る。
肩の力が抜け、友人は静かな笑みを返す。手は見える状態で、自然に力を抜いている。
3–7 秒：左の人物が自然な日本語で「来てくれたんだね」と言う。友人は一度うなずく。
台詞は控えめに話し、泣いたり大げさな表情をしたりしない。
7–10 秒：2人が係留された船に目を向ける。次のショットにつなげられるよう、最後の1秒は画を保つ。
カメラ：ゆっくり1回だけ寄る。切り返しもカットも入れない。
音声：近くではっきり聞こえる声、穏やかな港の水音、遠くのカモメ。音楽と字幕は入れない。
2人の人物同一性、服装、桟橋の形、船の位置、朝の光の方向を固定する。
人物の追加、大げさな身振り、顔の過度な美肌処理、指の増加、カメラの急な跳びを避ける。
```

[カテゴリ索引に戻る](#find-the-right-prompt) · [画像付き作例一覧](#visual-index)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. 最初のひと口 — 自然なカフェ体験レビュー

**画像から動画を生成する設定:** 10s · 9:16 · 1080p · [開始フレーム — 開いて保存](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/ja-JP/first-sip.txt)

[出典：Flaq AI](docs/ATTRIBUTION.md)

```text
入力されたカフェ写真を、誠実な手持ち撮影の体験レビューとして動かす。人物の顔、年齢、肌の質感、髪、モスグリーンのセーター、カップ、焼き菓子、窓、テーブル配置を保つ。

0–3 秒：自然で穏やかな手持ちの揺れ。彼女はひと口飲み終え、陶器のカップを約10センチ下げ、軽く微笑んで息を吐き、窓からカメラへ視線を戻す。湯気が上がり、背後の窓ガラスの雨筋がゆっくり合流する。

3–8 秒：リラックスした自然な日本語で「クリーミーで、甘すぎない。ちゃんとオーツの味もする」と話す。気取らない口調で、「甘すぎない」の後にごく短い間を置く。口の動きを台詞に正確に合わせ、手に持つカップは安定させる。

8–10 秒：彼女は満足そうに小さくうなずき、カメラが落ち着くと焼き菓子に目を落とす。

音声：スマートフォンで近くから録った声、静かなカフェの環境音、遠くのミルクスチーマー、柔らかな雨音、陶器のカップが触れる音。声を手前に出し、環境音は低くする。BGM と字幕は不要。

連続性の固定：顔の美化、着替え、指の増加、カップや食べ物の再設計、背景人物の出現、ロゴ、大げさなインフルエンサー風の身振りを入れない。
```

[カテゴリ索引に戻る](#find-the-right-prompt) · [画像付き作例一覧](#visual-index)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. 夜明けの塩田線 — 旅行ドキュメンタリー

**画像から動画を生成する設定:** 12s · 16:9 · 1080p · [開始フレーム — 開いて保存](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/ja-JP/salt-line.txt)

[出典：Flaq AI](docs/ATTRIBUTION.md)

```text
入力された海辺の塩田を、働く人への敬意を持つ観察型の旅行ドキュメンタリーとして動かす。2人の作業員、クリーム色と黄土色の列車、塩田、石灰岩の丘、建物、海、日の出の方向、落ち着いたフィルムの配色を保つ。

0–4 秒：固定のワイド画面。作業員が水路の点検を続ける。1人は浅い濃い塩水の中で木製道具を動かし、もう1人は仕切りを支える。水面の波紋は道具と朝の風に反応する。中景の列車が落ち着いた速度で近づく。

4–9 秒：列車を追ってカメラをゆっくり右にパンする。車輪をレールに合わせ、車両間隔と窓の並びのリズムを一定に保つ。薄い海霧が後ろを漂い、手前の塩の結晶を日光が徐々に照らす。

9–12 秒：列車が海岸へ通り過ぎ、パンはゆっくり止まる。1人の作業員が立ち、自然に伸びをして線路へ目を向ける。編集点にできるよう最後の2秒は画を保つ。

音声：穏やかな電車の駆動音、規則的な車輪の継ぎ目音、浅い水面を渡る風、遠くのカモメ、濃い塩水の中を動く木製道具。ナレーション、音楽、群衆、劇的な警笛は不要。

連続性の固定：現実的な作業、安定した人体構造、固定された風景、変わらない列車デザイン、自然な反射と水の物理挙動。現代的な街のスカイライン、観光客の演出、新しい建物、ロゴ、読める看板、過度に鮮やかな絵はがき色、タイムラプスの空を入れない。
```

[カテゴリ索引に戻る](#find-the-right-prompt) · [画像付き作例一覧](#visual-index)

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. 海辺のポストカード — 構成を決めた画像を動かす

**画像から動画を生成する設定:** 5s · 9:16 · 720p · [開始フレーム — 開いて保存](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/ja-JP/coastal-postcard.txt)

```text
3コマの海辺のポストカードを、レイアウトや枠線を変えずに動かす。
すべての物体と色を忠実に保つ。上のコマでは、カップから細い湯気が一筋立ち上る。
中央のコマでは、港の水面が穏やかに揺れ、日光がきらめく。
下のコマでは、元からある紙の角だけがそよ風でわずかに持ち上がり、元に戻る。
各動作はそれぞれのコマの中だけに収める。5秒間、すべてのコマを常に表示する。
カメラ：固定。ズーム、パン、カット、コマ間のトランジションは入れない。
音声：静かな水音と紙のかすかな擦れる音。台詞、音楽、字幕、文字の追加は不要。
カップの持ち手、窓枠、地図の記号、コマの寸法、読む順序を保つ。
コマの融合、新しい場面の生成、文字の描き直し、枠を越えた物体の移動を避ける。
最後は紙の角が落ち着き、元の構図を保った状態で終える。
```

[カテゴリ索引に戻る](#find-the-right-prompt) · [画像付き作例一覧](#visual-index)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. シトラス・ヘイロー — 高級香水の商品映像

**画像から動画を生成する設定:** 8s · 16:9 · 1080p · [開始フレーム — 開いて保存](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/ja-JP/citrus-halo.txt)

[出典：Flaq AI](docs/ATTRIBUTION.md)

```text
入力画像のボトルのデザイン、ガラスの比率、キャップ、石灰岩の台座、グレープフルーツの皮、暖かなアイボリーのセット、金色の側光を保つ。優雅な8秒の商品映像を作る。

0–2.5 秒：ほぼ固定のマクロ構図から始める。カメラはごくゆっくりドリーインする。結露の粒が光を受け、2滴の水滴が冷たいガラスを自然に滑り落ちる。グレープフルーツの皮が、制御されたスタジオのそよ風に運ばれるように台座から浮き上がる。

2.5–6 秒：皮がボトルの周りを優雅ならせんで一周する。キャップに触れたり隠したりしない。細かな柑橘のミストが逆光を横切る。厚いガラスの中で屈折と集光模様が物理法則に従って動く。ボトル自体は完全に硬いまま変形しない。

6–8 秒：皮が元の曲線に戻り、カメラは滑らかに止まる。明るい鏡面ハイライトがボトルの縁を一度だけ移動する。すっきりとした商品メインカットで終える。

音声：近距離のスタジオ効果音のみ。帯状の皮が柔らかく動く音、明瞭な水滴音2回、繊細なガラスの共鳴。声、音楽、文字は不要。

連続性の固定：ボトルの輪郭、キャップの面、液面、台座、配色、背景のアーチを変えない。ラベル、ロゴ、余分な果物、浮くボトル、形状の揺らぎ、カメラの跳び、人工的なきらめきの爆発を入れない。
```

[カテゴリ索引に戻る](#find-the-right-prompt) · [画像付き作例一覧](#visual-index)

<a id="learn-from-official-and-community-examples"></a>

## 公式とコミュニティの作品から学ぶ

出典の投稿には制作者とモデルのバージョンが示されています。動画は元の投稿を開いて視聴してください。以下のメモは制作方法を説明するもので、動画を再現できたという報告ではありません。

### [公式 1.5 Preview の映像 — Grok / Heavy Pulp](https://x.com/grok/status/2062225080843747351)

[![公式 1.5 Preview の映像 — Grok / Heavy Pulp](https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg)](https://x.com/grok/status/2062225080843747351)

予告編を個別の短いショットに分けて計画する方法を学びます。Preview 版の映像と、正式に公開された 1.5 モデルは区別してください。

### [完成した短編 — JSFILMZ](https://x.com/JSFILMZ0412/status/2062480692835938771)

作者は 2.5 分の作品を制作したと報告し、生成された演技の限界について述べています。まず静かなやり取りを一つ練習し、編集した複数のショットから長い物語を作りましょう。

### [動画化の前に画像を設計する — GENEL](https://x.com/genel_ai/status/2061382998873034825)

[![動画化の前に画像を設計する — GENEL](https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg)](https://x.com/genel_ai/status/2061382998873034825)

制作者は ChatGPT Images 2.0 でコラージュを作り、Grok Imagine Video 1.5 で動かしたと説明しています。このポストカード練習ではコマの枠を固定し、各コマの動きを一つに絞っています。

### [条件をそろえた比較 — JSFILMZ](https://x.com/JSFILMZ0412/status/2061117682515050669)

同じ元画像と比較可能な設定を使います。過去の順位をそのまま採用するのではなく、形状、動き、音声を確認してください。ボトルの練習では、これらの変数を分けて確認します。

<details>
<summary>フレームの観察と検証の範囲</summary>

2026 年 9 月 24 日、X の元投稿のプレーヤーで一部のフレームを確認しました。公式動画では約 3.6 秒（兜と軍勢）、19.8 秒（顔のクローズアップ）、34.6 秒（燃える水辺の都市）、GENEL の動画では約 0.05 秒（海辺の手すり）、4.9 秒（踏切）、12 秒（逆光の手）です。公式動画のショットサイズの切り替えや、GENEL の異なるショットに共通する海辺の光の使い方を参考にできます。固定されたコマを使う本ポストカード例は、これとは別の練習です。確認したのは一部のフレームであり、動きや音声を通して検証したものではありません。

</details>

[出典と視聴に関する記録（英語）](docs/COMMUNITY.md)

<a id="writing-guide"></a>

<a id="1-湯気の喫茶店ドリップバッグ商品ショット"></a>

<a id="15秒を超える物語は"></a>

<a id="よくある質問"></a>

<a id="キャラクターを安定させるには"></a>

<a id="コントリビューション"></a>

<a id="全プロンプトカテゴリ"></a>

<a id="基本テンプレート"></a>

<a id="日本語の台詞はどう指定しますか"></a>

<a id="日本語オリジナルプロンプト"></a>

## 参考資料

[プロンプト作成の参考資料](docs/guides/ja-JP.md) · [設定と操作の参考資料](docs/workflows/ja-JP.md) · [SeaImagine](https://seaimagine.com/ja/model/grok-imagine-1-5/)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

<a id="multilingual-prompts"></a>

## 収録内容と出典

英語のプロンプト例は計 38 種類です。元コレクションから引き継いだ 35 種類と、新しい練習例 3 種類で構成されています。翻訳は別のシナリオとして数えません。

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/ja/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
