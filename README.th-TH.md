# คลังพรอมป์ต์ Grok Imagine 1.5 — ภาษาไทย

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> พรอมป์ต์ 38 แบบ โดยมี 8 ตัวอย่างพร้อมภาพใน 15 ภาษา เลือกดูตามหมวดหมู่และคัดลอกพรอมป์ต์ฉบับเต็ม

![Grok Imagine 1.5 — สมุดพรอมป์ต์ที่เปิดออก มีรองเท้า รถราง และวาฬกระดาษอยู่ในฉากเดียวกัน](assets/seaimagine-grok-hero.webp)

ดัดแปลงจาก [Flaq AI](https://github.com/flaqai/awesome-grok-imagine) ดูแลโดย SeaImagine ภายใต้สัญญาอนุญาต [MIT](LICENSE) และเป็นโครงการอิสระจาก xAI ภาพแนวคิดไม่ได้แสดงผลการทดสอบจริงด้วย Grok

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## ดัชนีหมวดหมู่

| สิ่งที่อยากสร้าง | ตัวอย่างพร้อมภาพ |
| --- | --- |
| โฆษณาสินค้า | [ขวดแก้วทะเลขัดฝ้า — เปรียบเทียบการเคลื่อนไหวโดยควบคุมตัวแปร](#case-sea-glass-bottle) · [รัศมีซิตรัส — หนังสินค้าน้ำหอมระดับพรีเมียม](#case-citrus-halo) |
| ฉากแอ็กชันแบบภาพยนตร์ | [เส้นทางสีน้ำเงิน — ช็อตติดตามคนส่งของในตลาดกลางฝน](#case-blue-route) |
| เรื่องแฟนตาซี | [ขนมปังน้ำผึ้ง — เรื่องราวร้านขนมปังจิ๋ว](#case-honey-loaf) |
| บทสนทนาของตัวละคร | [พบกันอีกครั้งที่ท่าเรือ — ถ่ายทอดการเปลี่ยนอารมณ์เพียงจังหวะเดียว](#case-harbor-reunion) |
| วิดีโอไลฟ์สไตล์ | [จิบแรก — รีวิวคาเฟ่อย่างเป็นธรรมชาติ](#case-first-sip) |
| หนังท่องเที่ยว | [รางเกลือยามรุ่งอรุณ — สารคดีท่องเที่ยว](#case-salt-line) |
| เลย์เอาต์เคลื่อนไหว | [โปสการ์ดชายฝั่ง — ทำให้ภาพที่วางองค์ประกอบแล้วเคลื่อนไหว](#case-coastal-postcard) |

[ตัวอย่างพร้อมภาพ](#featured-prompts) · [ผลงานทางการและชุมชน](#learn-from-official-and-community-examples) · [ข้อมูลอ้างอิงการตั้งค่าและการใช้งาน](#writing-guide)

<a id="visual-index"></a>

### ภาพรวมตัวอย่างพร้อมภาพ

8 ตัวอย่างพร้อมพรอมป์ต์ฉบับเต็มและภาพเฟรมเริ่มต้น ภาพใช้แสดงแนวคิด ไม่ใช่ผลลัพธ์วิดีโอที่ผ่านการตรวจสอบแล้ว

ตัวอย่างห้าแบบที่ระบุแหล่งที่มาเป็น Flaq AI คงความยาวและความละเอียดเดิมไว้ ส่วนอีกสามแบบเขียนตามตัวเลือกปัจจุบันของ SeaImagine เมื่อนำตัวอย่างต้นฉบับมาใช้ใน SeaImagine ให้เลือก 5/10/15 วินาที และ 480p/720p แล้วจัดช่วงเวลาของการกระทำใหม่

| | |
| --- | --- |
| <a href="#case-sea-glass-bottle"><img src="assets/seaimagine-sea-glass-bottle.webp" height="180" alt="ขวดแก้วทะเลขัดฝ้า — เปรียบเทียบการเคลื่อนไหวโดยควบคุมตัวแปร"></a><br>[1. ขวดแก้วทะเลขัดฝ้า — เปรียบเทียบการเคลื่อนไหวโดยควบคุมตัวแปร](#case-sea-glass-bottle)<br>5s · 16:9 · 720p | <a href="#case-blue-route"><img src="assets/rainy-market-courier-video.webp" height="180" alt="เส้นทางสีน้ำเงิน — ช็อตติดตามคนส่งของในตลาดกลางฝน"></a><br>[2. เส้นทางสีน้ำเงิน — ช็อตติดตามคนส่งของในตลาดกลางฝน](#case-blue-route)<br>10s · 16:9 · 1080p |
| <a href="#case-honey-loaf"><img src="assets/pear-bakery-miniature-video.webp" height="180" alt="ขนมปังน้ำผึ้ง — เรื่องราวร้านขนมปังจิ๋ว"></a><br>[3. ขนมปังน้ำผึ้ง — เรื่องราวร้านขนมปังจิ๋ว](#case-honey-loaf)<br>9s · 16:9 · 1080p | <a href="#case-harbor-reunion"><img src="assets/seaimagine-harbor-reunion.webp" height="180" alt="พบกันอีกครั้งที่ท่าเรือ — ถ่ายทอดการเปลี่ยนอารมณ์เพียงจังหวะเดียว"></a><br>[4. พบกันอีกครั้งที่ท่าเรือ — ถ่ายทอดการเปลี่ยนอารมณ์เพียงจังหวะเดียว](#case-harbor-reunion)<br>10s · 16:9 · 720p |
| <a href="#case-first-sip"><img src="assets/cozy-cafe-ugc-video.webp" height="180" alt="จิบแรก — รีวิวคาเฟ่อย่างเป็นธรรมชาติ"></a><br>[5. จิบแรก — รีวิวคาเฟ่อย่างเป็นธรรมชาติ](#case-first-sip)<br>10s · 9:16 · 1080p | <a href="#case-salt-line"><img src="assets/coastal-salt-train-documentary.webp" height="180" alt="รางเกลือยามรุ่งอรุณ — สารคดีท่องเที่ยว"></a><br>[6. รางเกลือยามรุ่งอรุณ — สารคดีท่องเที่ยว](#case-salt-line)<br>12s · 16:9 · 1080p |
| <a href="#case-coastal-postcard"><img src="assets/seaimagine-coastal-postcard.webp" height="180" alt="โปสการ์ดชายฝั่ง — ทำให้ภาพที่วางองค์ประกอบแล้วเคลื่อนไหว"></a><br>[7. โปสการ์ดชายฝั่ง — ทำให้ภาพที่วางองค์ประกอบแล้วเคลื่อนไหว](#case-coastal-postcard)<br>5s · 9:16 · 720p | <a href="#case-citrus-halo"><img src="assets/citrus-fragrance-product-video.webp" height="180" alt="รัศมีซิตรัส — หนังสินค้าน้ำหอมระดับพรีเมียม"></a><br>[8. รัศมีซิตรัส — หนังสินค้าน้ำหอมระดับพรีเมียม](#case-citrus-halo)<br>8s · 16:9 · 1080p |

**ดูพรอมป์ต์เพิ่มเติม (ภาษาอังกฤษ) · 30**

| หมวดหมู่ | ดัชนีตัวอย่าง |
| --- | --- |
| [โฆษณาและสินค้า · 6](prompts/01-ads-and-products.md) | [1. Dew Drop Laboratory — skincare serum macro](prompts/01-ads-and-products.md#1-dew-drop-laboratory--skincare-serum-macro) · [2. Cold Brew Eclipse — coffee launch film](prompts/01-ads-and-products.md#2-cold-brew-eclipse--coffee-launch-film) · [3. Street-to-Studio — performance shoe demonstration](prompts/01-ads-and-products.md#3-street-to-studio--performance-shoe-demonstration) · [4. Doorstep Dinner — food delivery social ad](prompts/01-ads-and-products.md#4-doorstep-dinner--food-delivery-social-ad) · [5. Silver Current — artisan jewelry reveal](prompts/01-ads-and-products.md#5-silver-current--artisan-jewelry-reveal) · [6. One Tap Away — clean mobile app promo](prompts/01-ads-and-products.md#6-one-tap-away--clean-mobile-app-promo) |
| [เรื่องราวแบบภาพยนตร์ · 6](prompts/02-cinematic-storytelling.md) | [1. Last Tram Note — restrained urban romance](prompts/02-cinematic-storytelling.md#1-last-tram-note--restrained-urban-romance) · [2. Room 407 — quiet hotel mystery](prompts/02-cinematic-storytelling.md#2-room-407--quiet-hotel-mystery) · [3. Glasshouse Pursuit — grounded parkour action](prompts/02-cinematic-storytelling.md#3-glasshouse-pursuit--grounded-parkour-action) · [4. Tidekeeper — coastal fantasy ritual](prompts/02-cinematic-storytelling.md#4-tidekeeper--coastal-fantasy-ritual) · [5. Paper Moon Delivery — hand-drawn animation](prompts/02-cinematic-storytelling.md#5-paper-moon-delivery--hand-drawn-animation) · [6. Europa Signal — hard-science discovery](prompts/02-cinematic-storytelling.md#6-europa-signal--hard-science-discovery) |
| [โซเชียลและไลฟ์สไตล์ · 6](prompts/03-social-ugc.md) | [1. Shelf Test — honest skincare mini-review](prompts/03-social-ugc.md#1-shelf-test--honest-skincare-mini-review) · [2. Twelve-Minute Noodles — one-pan recipe reel](prompts/03-social-ugc.md#2-twelve-minute-noodles--one-pan-recipe-reel) · [3. First Set — realistic morning fitness log](prompts/03-social-ugc.md#3-first-set--realistic-morning-fitness-log) · [4. One Question, One Corner — street interview](prompts/03-social-ugc.md#4-one-question-one-corner--street-interview) · [5. Clay Cup Morning — tactile pottery ASMR](prompts/03-social-ugc.md#5-clay-cup-morning--tactile-pottery-asmr) · [6. Umbrella Reset — seamless pet comedy loop](prompts/03-social-ugc.md#6-umbrella-reset--seamless-pet-comedy-loop) |
| [ตัวละครและภาพอ้างอิง · 6](prompts/04-characters-and-references.md) | [1. Harbor Cartographer — consistent character introduction](prompts/04-characters-and-references.md#1-harbor-cartographer--consistent-character-introduction) · [2. Linen Set — virtual try-on walk test](prompts/04-characters-and-references.md#2-linen-set--virtual-try-on-walk-test) · [3. Counter Demo — product placement without redesign](prompts/04-characters-and-references.md#3-counter-demo--product-placement-without-redesign) · [4. Two Voices, One Repair — synchronized dialogue scene](prompts/04-characters-and-references.md#4-two-voices-one-repair--synchronized-dialogue-scene) · [5. Sunday Table — consistent three-person ensemble](prompts/04-characters-and-references.md#5-sunday-table--consistent-three-person-ensemble) · [6. Parcel Finch — reusable brand mascot motion](prompts/04-characters-and-references.md#6-parcel-finch--reusable-brand-mascot-motion) |
| [การแก้ไขและต่อความยาว · 6](prompts/05-editing-and-extension.md) | [1. Blue Hour Conversion — day-to-night architectural edit](prompts/05-editing-and-extension.md#1-blue-hour-conversion--day-to-night-architectural-edit) · [2. First Snow — controlled weather replacement](prompts/05-editing-and-extension.md#2-first-snow--controlled-weather-replacement) · [3. Clean Plate — remove one distracting object](prompts/05-editing-and-extension.md#3-clean-plate--remove-one-distracting-object) · [4. Practical Miniature — change rendering style, keep motion](prompts/05-editing-and-extension.md#4-practical-miniature--change-rendering-style-keep-motion) · [5. Beyond the Gate — continue a travel shot](prompts/05-editing-and-extension.md#5-beyond-the-gate--continue-a-travel-shot) · [6. Turntable Loop — repair a product animation into a seamless cycle](prompts/05-editing-and-extension.md#6-turntable-loop--repair-a-product-animation-into-a-seamless-cycle) |

<a id="featured-prompts"></a>

## พรอมป์ต์พร้อมภาพที่คัดลอกและปรับใช้ได้

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. ขวดแก้วทะเลขัดฝ้า — เปรียบเทียบการเคลื่อนไหวโดยควบคุมตัวแปร

**การตั้งค่าภาพเป็นวิดีโอ:** 5s · 16:9 · 720p · [เฟรมเริ่มต้น — เปิดและบันทึก](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/th-TH/sea-glass-bottle.txt)

```text
คงขวดแก้วทะเลผิวฝ้าเพียงขวดเดียวบนพื้นหินสีอ่อน ฝาทรงกระบอก
ด้านหน้าที่ว่างเปล่าไม่มีลายพิมพ์ ระดับของเหลว เส้นขอบฟ้า และแสงด้านข้างที่นุ่มนวล ขวดต้องไม่เคลื่อนที่เลย
ตลอดห้าวินาที ให้กล้องเลื่อนไปทางขวาช้า ๆ เป็นระยะไม่เกินความกว้างหนึ่งขวด
หยดน้ำเล็ก ๆ หนึ่งหยดไหลลงตามด้านหน้าขวดและหยุดที่ฐาน คลื่นทะเลในพื้นหลังเคลื่อนไหวเบา ๆ โดยยังเบลอนอกระยะโฟกัส
ให้แสงสะท้อนสอดคล้องกับตำแหน่งกล้องและแหล่งกำเนิดแสง
เสียง: มีเพียงเสียงคลื่นจากระยะไกล ไม่มีดนตรี เสียงคน เสียงแก้วกระแทก หรือเสียงน้ำกระเซ็นเกินจริง
ไม่ตัดภาพหรือซูม คงรูปร่างขวด แนวฝาขวด เนื้อผิวแก้ว และจำนวนวัตถุ
หลีกเลี่ยงการสร้างโลโก้ การเปลี่ยนระดับของเหลว ขอบบิดงอ วัตถุลอย หรืออุปกรณ์ประกอบฉากใหม่
ค้างภาพให้นิ่งในวินาทีสุดท้าย
```

[กลับไปยังดัชนีหมวดหมู่](#find-the-right-prompt) · [ภาพรวมตัวอย่างพร้อมภาพ](#visual-index)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. เส้นทางสีน้ำเงิน — ช็อตติดตามคนส่งของในตลาดกลางฝน

**การตั้งค่าภาพเป็นวิดีโอ:** 10s · 16:9 · 1080p · [เฟรมเริ่มต้น — เปิดและบันทึก](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/th-TH/blue-route.txt)

[ที่มา: Flaq AI](docs/ATTRIBUTION.md)

```text
คงคนส่งของ มอเตอร์ไซค์ไฟฟ้าสีน้ำเงินโคบอลต์ กล่องสินค้า ตลาดยกระดับ กันสาดโปร่งแสง ทางเดินเหล็กเปียก แสง และชุดสีกลางคืนจากภาพ สร้างช็อตติดตามมุมต่ำต่อเนื่องหนึ่งช็อตที่สมจริง ทั้งมวลน้ำหนัก การยึดเกาะของยาง ฝน และระบบกันสะเทือน

0–3 วินาที: มอเตอร์ไซค์เร่งอย่างราบรื่นจากท่าเดิม ยางหลังปัดน้ำเป็นรูปพัดบาง ๆ ระบบกันสะเทือนยุบเมื่อผ่านรอยต่อระบายน้ำ กล้องติดตามที่ระดับล้ออยู่ข้างรถค่อนไปด้านหลังเล็กน้อย เคลื่อนด้วยความเร็วเท่ากันโดยไม่สั่นรุนแรง

3–7 วินาที: คนส่งของเอนตัวผ่านโค้งซ้ายกว้างหนึ่งโค้ง กันสาดโค้งตามลม ไอน้ำลอยจากร้านอาหาร และแสงอุ่นจากโคมในฉากยืดเป็นเส้นนุ่มในเงาสะท้อนบนพื้นเปียก ล้อทั้งสองยังกลมและสัมผัสพื้น

7–10 วินาที: รถตั้งตรงแล้วมุ่งสู่ส่วนตลาดที่สว่างและเปิดโล่งกว่า กล้องตามห่างออกไปครึ่งเมตร เผยเส้นทางข้างหน้า แล้วค้างภาพจบให้นิ่ง

เสียง: เสียงมอเตอร์ไฟฟ้าสูงอย่างสมจริง น้ำกระเซ็น ฝนตกบนกันสาด เสียงคนในตลาดเบา ๆ และเสียงกระแทกระบบกันสะเทือนหนึ่งครั้ง ไม่มีดนตรี บทพูด ไซเรน หรือระเบิด

คงความต่อเนื่อง: ชุดผู้ขับ หมวกกันน็อก รูปทรงรถ กล่องสินค้า แผงสีน้ำเงิน และผังตลาดต้องเหมือนเดิมทุกประการ ไม่มีรถแปลงร่าง ล้อผิดรูป การชน อาวุธ ป้ายอ่านได้ โลโก้ กล้องวาร์ป หรือการเปลี่ยนความเร็วที่เป็นไปไม่ได้
```

[กลับไปยังดัชนีหมวดหมู่](#find-the-right-prompt) · [ภาพรวมตัวอย่างพร้อมภาพ](#visual-index)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. ขนมปังน้ำผึ้ง — เรื่องราวร้านขนมปังจิ๋ว

**การตั้งค่าภาพเป็นวิดีโอ:** 9s · 16:9 · 1080p · [เฟรมเริ่มต้น — เปิดและบันทึก](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/th-TH/honey-loaf.txt)

[ที่มา: Flaq AI](docs/ATTRIBUTION.md)

```text
คงร้านขนมปังในบ้านทรงลูกแพร์ คนทำขนมปังจิ๋วสามคน ชุด ใบหน้า ขนมปังน้ำผึ้ง เตาอบ หน้าต่าง มอส โคลเวอร์ ดวงจันทร์ วัสดุสต็อปโมชันที่ให้ความรู้สึกจับต้องได้ และความต่างของสีอุ่นกับสีเย็น

0–3 วินาที: เริ่มด้วยองค์ประกอบกว้างตามภาพ มีจังหวะสต็อปโมชันทำมือเล็กน้อย คนทำขนมปังสองคนยกขนมปังน้ำผึ้งอุ่นขึ้นพร้อมกัน มือยังติดอยู่กับแผ่นไม้ แป้งฟุ้งเล็กน้อย ไฟเตาอบไหว และคนที่สามเปิดหน้าต่างขายของ

3–7 วินาที: ทั้งคู่เดินอย่างระมัดระวังพร้อมกันสี่ก้าวไปที่หน้าต่าง ขนมปังมีน้ำหนักน่าเชื่อและหย่อนลงเล็กน้อยระหว่างทั้งสอง ด้านนอกใบโคลเวอร์หนึ่งใบปล่อยน้ำค้างหนึ่งหยด และหิ่งห้อยสองตัวลอยผ่านที่ระยะลึกต่างกัน กล้องเคลื่อนเป็นส่วนโค้งเบา ๆ ไปทางขวาห้าองศา

7–9 วินาที: ทั้งคู่เลื่อนแผ่นไม้ขึ้นบนเคาน์เตอร์ ยิ้มให้กันอย่างโล่งใจ และแสงเตาอบสงบลง จบโดยเห็นครบทั้งสามคนและขนมปังอยู่ตรงกลาง

เสียง: เสียงเท้าเล็ก ๆ แตะไม้ ไฟเตาอบแตกเบา ๆ ไม้ลั่น แมลงกลางคืนแผ่ว ๆ และระฆังเล็กที่หน้าต่างขายของหนึ่งครั้ง ไม่มีบทพูด คำบรรยายเสียง ดนตรี หรือข้อความ

คงความต่อเนื่อง: รักษาจำนวนตัวละคร แบบใบหน้า สัดส่วน สีชุด รูปทรงลูกแพร์ ผังห้อง และผิวสัมผัสงานทำมือ ไม่มีคนทำขนมปังเพิ่ม ภาพคอมพิวเตอร์มันวาว แขนขาเหมือนยาง อุปกรณ์ลอย ขนมปังละลาย การตัดภาพ โลโก้ หรือตัวละครที่ดูเหมือนจากแฟรนไชส์ดัง
```

[กลับไปยังดัชนีหมวดหมู่](#find-the-right-prompt) · [ภาพรวมตัวอย่างพร้อมภาพ](#visual-index)

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. พบกันอีกครั้งที่ท่าเรือ — ถ่ายทอดการเปลี่ยนอารมณ์เพียงจังหวะเดียว

**การตั้งค่าภาพเป็นวิดีโอ:** 10s · 16:9 · 720p · [เฟรมเริ่มต้น — เปิดและบันทึก](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/th-TH/harbor-reunion.txt)

```text
คงผู้ใหญ่สองคน ใบหน้าของแต่ละคน เสื้อผ้าสีน้ำเงินกรมท่าและสีครีม ท่าเรือไม้ และแสงเช้าอ่อน ๆ จากภาพที่ให้มา
ให้ทั้งสองคนอยู่ในองค์ประกอบภาพระยะปานกลางค่อนข้างกว้างเดียวกันตลอด
0–3 วินาที: คนทางซ้ายสังเกตเห็นเพื่อนที่มาถึงและก้าวไปข้างหน้าเล็กน้อยหนึ่งก้าว
ไหล่ของเขาผ่อนคลายลง เพื่อนตอบด้วยรอยยิ้มบาง ๆ ให้มือยังมองเห็นและอยู่ในท่าผ่อนคลาย
3–7 วินาที: คนทางซ้ายพูดด้วยภาษาไทยอย่างเป็นธรรมชาติว่า “มาแล้วเหรอ” เพื่อนพยักหน้าหนึ่งครั้ง
พูดอย่างเรียบง่าย ไม่ร้องไห้และไม่แสดงสีหน้าเกินจริง
7–10 วินาที: ทั้งคู่มองไปที่เรือที่จอดเทียบท่า ค้างภาพในวินาทีสุดท้ายเพื่อเชื่อมต่อกับช็อตถัดไป
กล้อง: เคลื่อนเข้าอย่างนุ่มนวลเพียงครั้งเดียว ไม่มีช็อตย้อนมุมและไม่มีการตัดภาพ
เสียง: บทพูดระยะใกล้ที่ฟังชัด เสียงน้ำในท่าเรือเบา ๆ และเสียงนกนางนวลไกล ๆ ไม่มีดนตรีหรือคำบรรยาย
คงอัตลักษณ์ของทั้งสองคน เสื้อผ้า รูปทรงท่าเรือ ตำแหน่งเรือ และทิศทางแสงเช้าให้เหมือนเดิม
หลีกเลี่ยงคนเพิ่มเติม ท่าทางเกินจริง การเกลี่ยผิวหน้า นิ้วเกิน และกล้องกระโดดเปลี่ยนตำแหน่ง
```

[กลับไปยังดัชนีหมวดหมู่](#find-the-right-prompt) · [ภาพรวมตัวอย่างพร้อมภาพ](#visual-index)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. จิบแรก — รีวิวคาเฟ่อย่างเป็นธรรมชาติ

**การตั้งค่าภาพเป็นวิดีโอ:** 10s · 9:16 · 1080p · [เฟรมเริ่มต้น — เปิดและบันทึก](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/th-TH/first-sip.txt)

[ที่มา: Flaq AI](docs/ATTRIBUTION.md)

```text
ทำให้ภาพคาเฟ่ที่ให้มาเคลื่อนไหวเป็นรีวิวจากครีเอเตอร์อย่างจริงใจด้วยกล้องถือมือ คงใบหน้า อายุ รายละเอียดผิว ผม เสื้อสเวตเตอร์สีเขียวมอส ถ้วย ขนม หน้าต่าง และการจัดโต๊ะ

0–3 วินาที: กล้องถือมือไหวเบา ๆ อย่างเป็นธรรมชาติ เธอจิบเสร็จ ลดถ้วยเซรามิกลงประมาณสิบเซนติเมตร ผ่อนลมหายใจพร้อมยิ้มเล็กน้อย แล้วเปลี่ยนสายตาจากหน้าต่างกลับมาที่กล้อง ไอน้ำม้วนขึ้นและทางน้ำฝนบนกระจกด้านหลังค่อย ๆ ไหลรวมกัน

3–8 วินาที: เธอพูดภาษาไทยอย่างผ่อนคลายเป็นธรรมชาติว่า “นุ่มละมุน ไม่หวานเกินไป แล้วก็ได้รสข้าวโอ๊ตจริง ๆ” ให้เหมือนคุยกันปกติ หยุดสั้น ๆ หลัง “หวานเกินไป” ขยับปากให้ตรงบทพูดและถือถ้วยให้นิ่ง

8–10 วินาที: เธอพยักหน้าเล็กน้อยอย่างพอใจ แล้วเหลือบมองขนมขณะที่กล้องนิ่งลง

เสียง: เสียงพูดใกล้ไมค์โทรศัพท์ บรรยากาศคาเฟ่เงียบ ๆ เครื่องสตีมนมไกล ๆ ฝนเบา ๆ และเสียงถ้วยเซรามิกสัมผัสพื้นผิว ให้เสียงพูดเด่นอยู่ด้านหน้าและเสียงแวดล้อมเบา ไม่มีดนตรีประกอบหรือคำบรรยาย

คงความต่อเนื่อง: ไม่แต่งใบหน้าให้สวยขึ้น ไม่เปลี่ยนเสื้อผ้า ไม่มีนิ้วเกิน ไม่ออกแบบถ้วยหรืออาหารใหม่ ไม่มีคนปรากฏเพิ่มในพื้นหลัง ไม่มีโลโก้หรือท่าทางอินฟลูเอนเซอร์ที่เกินจริง
```

[กลับไปยังดัชนีหมวดหมู่](#find-the-right-prompt) · [ภาพรวมตัวอย่างพร้อมภาพ](#visual-index)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. รางเกลือยามรุ่งอรุณ — สารคดีท่องเที่ยว

**การตั้งค่าภาพเป็นวิดีโอ:** 12s · 16:9 · 1080p · [เฟรมเริ่มต้น — เปิดและบันทึก](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/th-TH/salt-line.txt)

[ที่มา: Flaq AI](docs/ATTRIBUTION.md)

```text
ทำให้ฉากนาเกลือชายฝั่งที่ให้มาเคลื่อนไหวเป็นสารคดีท่องเที่ยวแบบสังเกตการณ์ที่ให้เกียรติคนทำงาน คงคนงานสองคน รถไฟสีครีมกับสีเหลืองดิน แปลงเกลือ เนินหินปูน อาคาร ทะเล ทิศทางพระอาทิตย์ขึ้น และชุดสีฟิล์มหม่น

0–4 วินาที: ภาพกว้างอยู่กับที่ คนงานตรวจร่องน้ำต่อ คนหนึ่งลากเครื่องมือไม้ผ่านน้ำเกลือตื้น ส่วนอีกคนประคองแผ่นกั้น ระลอกน้ำตอบสนองต่อเครื่องมือและลมเช้า รถไฟเข้ามาด้วยความเร็วพอดีในระยะกลาง

4–9 วินาที: กล้องแพนขวาช้า ๆ ตามรถไฟ ล้อยังตรงราง ระยะห่างตู้และจังหวะเรียงหน้าต่างคงเดิม หมอกทะเลบาง ๆ ลอยอยู่ด้านหลัง ขณะแสงแดดค่อย ๆ จับผลึกเกลือด้านหน้า

9–12 วินาที: รถไฟผ่านไปทางชายฝั่งและกล้องค่อย ๆ หยุดแพน คนงานหนึ่งคนยืนขึ้น ยืดตัวอย่างธรรมชาติ แล้วมองไปทางราง ค้างสองวินาทีสุดท้ายไว้เป็นจุดตัดต่อ

เสียง: เสียงครางเบาของรถไฟไฟฟ้า เสียงล้อผ่านรอยต่อเป็นจังหวะ ลมเหนือผิวน้ำตื้น นกนางนวลไกล ๆ และเครื่องมือไม้เคลื่อนในน้ำเกลือ ไม่มีคำบรรยายเสียง ดนตรี ฝูงชน หรือแตรที่เร้าอารมณ์

คงความต่อเนื่อง: การทำงานสมจริง สรีระคงที่ ภูมิทัศน์ไม่เปลี่ยน แบบรถไฟเดิม แสงสะท้อนและฟิสิกส์ของน้ำสมเหตุสมผล ไม่มีเส้นขอบฟ้าเมืองสมัยใหม่ นักท่องเที่ยวจัดฉาก อาคารใหม่ โลโก้ ป้ายอ่านได้ สีโปสการ์ดอิ่มเกินไป หรือท้องฟ้าแบบไทม์แลปส์
```

[กลับไปยังดัชนีหมวดหมู่](#find-the-right-prompt) · [ภาพรวมตัวอย่างพร้อมภาพ](#visual-index)

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. โปสการ์ดชายฝั่ง — ทำให้ภาพที่วางองค์ประกอบแล้วเคลื่อนไหว

**การตั้งค่าภาพเป็นวิดีโอ:** 5s · 9:16 · 720p · [เฟรมเริ่มต้น — เปิดและบันทึก](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/th-TH/coastal-postcard.txt)

```text
ทำให้โปสการ์ดชายฝั่งสามช่องนี้เคลื่อนไหวโดยไม่เปลี่ยนการจัดวางหรือเส้นขอบ
คงวัตถุและสีทั้งหมดให้เหมือนเดิมทุกประการ ช่องบนมีไอร้อนเส้นบางหนึ่งสายลอยขึ้นจากถ้วย
ช่องกลางมีน้ำในท่าเรือกระเพื่อมเบา ๆ และแสงแดดสะท้อนระยิบระยับบนผิวน้ำ
ช่องล่างมีเพียงมุมกระดาษที่มีอยู่เดิมยกขึ้นเล็กน้อยตามลมอ่อนแล้วตกลง
จำกัดการเคลื่อนไหวแต่ละอย่างให้อยู่ภายในช่องของตัวเอง แสดงทุกช่องตลอดทั้งห้าวินาที
กล้อง: อยู่กับที่ ไม่ซูม ไม่แพน ไม่ตัดภาพ และไม่มีการเปลี่ยนฉากระหว่างช่อง
เสียง: เสียงน้ำสงบและเสียงกระดาษเสียดสีเบา ๆ ไม่มีบทพูด ดนตรี คำบรรยาย หรือข้อความเพิ่มเติม
คงหูถ้วย กรอบหน้าต่าง เครื่องหมายบนแผนที่ ขนาดช่อง และลำดับการอ่าน
หลีกเลี่ยงการรวมช่อง การสร้างฉากใหม่ การวาดตัวอักษรใหม่ หรือการเคลื่อนวัตถุข้ามเส้นขอบ
จบด้วยมุมกระดาษที่วางนิ่งและองค์ประกอบเดิมที่ยังสมบูรณ์
```

[กลับไปยังดัชนีหมวดหมู่](#find-the-right-prompt) · [ภาพรวมตัวอย่างพร้อมภาพ](#visual-index)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. รัศมีซิตรัส — หนังสินค้าน้ำหอมระดับพรีเมียม

**การตั้งค่าภาพเป็นวิดีโอ:** 8s · 16:9 · 1080p · [เฟรมเริ่มต้น — เปิดและบันทึก](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/th-TH/citrus-halo.txt)

[ที่มา: Flaq AI](docs/ATTRIBUTION.md)

```text
คงแบบขวด สัดส่วนแก้ว ฝา ฐานหินปูน เปลือกเกรปฟรุต ฉากสีงาช้างอบอุ่น และแสงด้านข้างสีทองจากภาพที่ให้มา สร้างหนังสินค้าแปดวินาทีที่ดูสง่างาม

0–2.5 วินาที: เริ่มด้วยองค์ประกอบมาโครที่แทบอยู่นิ่ง กล้องเคลื่อนเข้าอย่างช้ามาก หยดไอน้ำควบแน่นรับแสง น้ำสองหยดไหลลงบนแก้วเย็นอย่างเป็นธรรมชาติ เปลือกเกรปฟรุตยกตัวจากฐานราวกับถูกพัดด้วยลมอ่อนในสตูดิโอที่ควบคุมได้

2.5–6 วินาที: เปลือกหมุนเป็นเกลียวอย่างสง่างามรอบขวดหนึ่งรอบ โดยไม่แตะหรือบังฝา ละอองซิตรัสเล็ก ๆ ลอยผ่านแสงย้อน การหักเหและลวดลายแสงรวมเคลื่อนผ่านแก้วหนาอย่างถูกหลักฟิสิกส์ ตัวขวดยังคงแข็งและไม่เปลี่ยนรูปเลย

6–8 วินาที: เปลือกกลับลงมาเป็นเส้นโค้งเดิม กล้องค่อย ๆ หยุด และไฮไลต์สะท้อนสว่างหนึ่งเส้นเคลื่อนผ่านขอบขวดเพียงครั้งเดียว จบด้วยภาพสินค้าหลักที่สะอาดตา

เสียง: ใช้เพียงเสียงประกอบในสตูดิโอระยะใกล้ ได้แก่ เสียงแถบเปลือกเคลื่อนเบา ๆ เสียงหยดน้ำใสสองครั้ง และเสียงกังวานแก้วบางเบา ไม่มีเสียงพูด ดนตรี หรือข้อความ

คงความต่อเนื่อง: ไม่เปลี่ยนรูปทรงขวด เหลี่ยมฝา ระดับของเหลว ฐาน ชุดสี หรือซุ้มโค้งด้านหลัง ไม่มีฉลาก โลโก้ ผลไม้เพิ่ม ขวดลอย รูปทรงสั่น กล้องกระโดด หรือประกายเทียมที่ระเบิดออกมา
```

[กลับไปยังดัชนีหมวดหมู่](#find-the-right-prompt) · [ภาพรวมตัวอย่างพร้อมภาพ](#visual-index)

<a id="learn-from-official-and-community-examples"></a>

## เรียนรู้จากผลงานทางการและชุมชน

โพสต์ต้นทางระบุผู้สร้างและรุ่นของโมเดล เปิดโพสต์ต้นฉบับเพื่อรับชม คำแนะนำด้านล่างอธิบายวิธีสร้างงาน ไม่ได้หมายความว่าเราได้สร้างวิดีโอเหล่านั้นซ้ำสำเร็จแล้ว

### [ชุดคลิปทางการ 1.5 Preview — Grok / Heavy Pulp](https://x.com/grok/status/2062225080843747351)

[![ชุดคลิปทางการ 1.5 Preview — Grok / Heavy Pulp](https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg)](https://x.com/grok/status/2062225080843747351)

เรียนรู้การวางแผนตัวอย่างหนังโดยแยกเป็นช็อตสั้น ๆ หลายช็อต แยกให้ชัดระหว่างภาพจากรุ่น Preview กับโมเดล 1.5 ที่เปิดตัวแล้ว

### [หนังสั้นที่เสร็จแล้ว — JSFILMZ](https://x.com/JSFILMZ0412/status/2062480692835938771)

ผู้สร้างระบุว่าได้ทำหนังยาว 2.5 นาที และพูดถึงข้อจำกัดของการแสดงที่สร้างด้วยโมเดล เริ่มฝึกจากบทสนทนาสงบ ๆ หนึ่งช่วงก่อน แล้วค่อยนำช็อตมาตัดต่อเป็นเรื่องที่ยาวขึ้น

### [วางแผนภาพก่อนสร้างการเคลื่อนไหว — GENEL](https://x.com/genel_ai/status/2061382998873034825)

[![วางแผนภาพก่อนสร้างการเคลื่อนไหว — GENEL](https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg)](https://x.com/genel_ai/status/2061382998873034825)

ผู้สร้างระบุว่าใช้ ChatGPT Images 2.0 ทำภาพคอลลาจ แล้วใช้ Grok Imagine Video 1.5 ทำให้เคลื่อนไหว แบบฝึกโปสการ์ดของเราคงเส้นขอบช่องให้อยู่กับที่และกำหนดเพียงหนึ่งการเคลื่อนไหวต่อช่อง

### [การเปรียบเทียบแบบควบคุมตัวแปร — JSFILMZ](https://x.com/JSFILMZ0412/status/2061117682515050669)

ใช้ภาพต้นทางเดียวกันและการตั้งค่าที่เปรียบเทียบกันได้ ตรวจสอบรูปทรง การเคลื่อนไหว และเสียง แทนการยึดอันดับในอดีต แบบฝึกขวดของเราแยกตัวแปรเหล่านี้เพื่อให้ตรวจสอบได้

<details>
<summary>ข้อสังเกตจากเฟรมและขอบเขตการตรวจสอบ</summary>

เมื่อวันที่ 24 กันยายน 2026 เราสุ่มดูเฟรมผ่านเครื่องเล่นในโพสต์ X ต้นฉบับ โดยคลิปทางการดูที่ประมาณ 3.6 วินาที (หมวกเกราะและกองทัพ), 19.8 วินาที (ภาพใบหน้าระยะใกล้) และ 34.6 วินาที (เมืองริมน้ำที่กำลังลุกไหม้) ส่วนคลิป GENEL ดูที่ประมาณ 0.05 วินาที (ราวกั้นริมทะเล), 4.9 วินาที (ทางข้ามทางรถไฟ) และ 12 วินาที (มือในแสงย้อน) ลองศึกษาการเปลี่ยนขนาดภาพของช็อตในคลิปทางการ และการรักษาแสงชายฝั่งให้สอดคล้องกันระหว่างช็อตต่าง ๆ ของ GENEL โปสการ์ดแบบตรึงช่องของเราเป็นแบบฝึกหัดอีกประเภทหนึ่ง การตรวจสอบครั้งนี้เป็นเพียงการสุ่มดูเฟรม ไม่ใช่การทดสอบการเคลื่อนไหวหรือเสียงตลอดทั้งคลิป

</details>

[แหล่งที่มาและบันทึกการรับชม (ภาษาอังกฤษ)](docs/COMMUNITY.md)

<a id="writing-guide"></a>

<a id="คลงพรอมตฉบบเตม"></a>

<a id="ฉากทดสอบหลายภาษา-เวรกชอปโคมไฟเซรามก"></a>

<a id="หลกการใชงานอยางยอ"></a>

## เอกสารอ้างอิง

[ข้อมูลอ้างอิงการเขียน](docs/guides/th-TH.md) · [ข้อมูลอ้างอิงการตั้งค่าและการใช้งาน](docs/workflows/th-TH.md) · [SeaImagine](https://seaimagine.com/th/model/grok-imagine-1-5/)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

<a id="multilingual-prompts"></a>

## คอลเลกชันและการระบุที่มา

มีพรอมป์ต์ภาษาอังกฤษที่แตกต่างกันทั้งหมด 38 แบบ ได้แก่ 35 แบบจากคอลเลกชันเดิม และแบบฝึกหัดใหม่ 3 แบบนี้ ฉบับแปลไม่นับเป็นสถานการณ์ใหม่

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/th/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
