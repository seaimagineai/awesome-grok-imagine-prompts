# مكتبة نصوص توجيه Grok Imagine 1.5 — العربية

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 38 نص توجيه، منها 8 أمثلة مصوّرة متاحة بـ15 لغة. تصفّح حسب الفئة وانسخ نصوص التوجيه كاملة.

![Grok Imagine 1.5 — دفتر أوصاف مفتوح يضم حذاءً وترامًا وحوتًا ورقيًا في مشهد واحد متصل](assets/seaimagine-grok-hero.webp)

مقتبسة من [Flaq AI](https://github.com/flaqai/awesome-grok-imagine)، وتتولى SeaImagine صيانتها. الترخيص: [MIT](LICENSE). المشروع مستقل عن xAI. الصور التصورية ليست نتائج موثّقة من Grok.

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## فهرس الفئات

| الهدف | أمثلة مصوّرة |
| --- | --- |
| إعلانات المنتجات | [زجاجة من زجاج البحر: مقارنة حركات مضبوطة](#case-sea-glass-bottle) · [هالة الحمضيات: فيلم لمنتج عطر فاخر](#case-citrus-halo) |
| مشاهد حركة سينمائية | [المسار الأزرق: تتبّع مندوب توصيل في سوق ممطر](#case-blue-route) |
| قصص خيالية | [رغيف العسل: حكاية مخبز مصغّر](#case-honey-loaf) |
| حوار الشخصيات | [لقاء في الميناء: لحظة عاطفية واحدة](#case-harbor-reunion) |
| فيديوهات الحياة اليومية | [الرشفة الأولى: مراجعة طبيعية لصانعة محتوى في مقهى](#case-first-sip) |
| أفلام السفر | [خط الملح عند الفجر: فيلم وثائقي عن السفر](#case-salt-line) |
| تصاميم متحركة | [بطاقة ساحلية: حرّك صورة مخططة مسبقًا](#case-coastal-postcard) |

[أمثلة مصوّرة](#featured-prompts) · [أعمال رسمية ومن المجتمع](#learn-from-official-and-community-examples) · [مرجع الإعدادات والتشغيل](#writing-guide)

<a id="visual-index"></a>

### نظرة سريعة على الأمثلة المصوّرة

8 أمثلة مع نصوص التوجيه الكاملة وصور الإطار الأول. الصور تعرض الأفكار وليست نتائج فيديو موثّقة.

تحتفظ الأمثلة الخمسة الموسومة بعبارة «المصدر: Flaq AI» بمدتها ودقتها الأصليتين؛ وتستخدم الأمثلة الثلاثة الأخرى خيارات SeaImagine الحالية. لاستخدام مثال من المصدر في SeaImagine، اختر 5/10/15 ثانية و480p/720p، وأعد كتابة توقيت أفعاله ليتناسب مع المدة المختارة.

| | |
| --- | --- |
| <a href="#case-sea-glass-bottle"><img src="assets/seaimagine-sea-glass-bottle.webp" height="180" alt="زجاجة من زجاج البحر: مقارنة حركات مضبوطة"></a><br>[1. زجاجة من زجاج البحر: مقارنة حركات مضبوطة](#case-sea-glass-bottle)<br>5s · 16:9 · 720p | <a href="#case-blue-route"><img src="assets/rainy-market-courier-video.webp" height="180" alt="المسار الأزرق: تتبّع مندوب توصيل في سوق ممطر"></a><br>[2. المسار الأزرق: تتبّع مندوب توصيل في سوق ممطر](#case-blue-route)<br>10s · 16:9 · 1080p |
| <a href="#case-honey-loaf"><img src="assets/pear-bakery-miniature-video.webp" height="180" alt="رغيف العسل: حكاية مخبز مصغّر"></a><br>[3. رغيف العسل: حكاية مخبز مصغّر](#case-honey-loaf)<br>9s · 16:9 · 1080p | <a href="#case-harbor-reunion"><img src="assets/seaimagine-harbor-reunion.webp" height="180" alt="لقاء في الميناء: لحظة عاطفية واحدة"></a><br>[4. لقاء في الميناء: لحظة عاطفية واحدة](#case-harbor-reunion)<br>10s · 16:9 · 720p |
| <a href="#case-first-sip"><img src="assets/cozy-cafe-ugc-video.webp" height="180" alt="الرشفة الأولى: مراجعة طبيعية لصانعة محتوى في مقهى"></a><br>[5. الرشفة الأولى: مراجعة طبيعية لصانعة محتوى في مقهى](#case-first-sip)<br>10s · 9:16 · 1080p | <a href="#case-salt-line"><img src="assets/coastal-salt-train-documentary.webp" height="180" alt="خط الملح عند الفجر: فيلم وثائقي عن السفر"></a><br>[6. خط الملح عند الفجر: فيلم وثائقي عن السفر](#case-salt-line)<br>12s · 16:9 · 1080p |
| <a href="#case-coastal-postcard"><img src="assets/seaimagine-coastal-postcard.webp" height="180" alt="بطاقة ساحلية: حرّك صورة مخططة مسبقًا"></a><br>[7. بطاقة ساحلية: حرّك صورة مخططة مسبقًا](#case-coastal-postcard)<br>5s · 9:16 · 720p | <a href="#case-citrus-halo"><img src="assets/citrus-fragrance-product-video.webp" height="180" alt="هالة الحمضيات: فيلم لمنتج عطر فاخر"></a><br>[8. هالة الحمضيات: فيلم لمنتج عطر فاخر](#case-citrus-halo)<br>8s · 16:9 · 1080p |

**تصفّح المزيد من نصوص التوجيه (بالإنجليزية) · 30**

| الفئة | فهرس الأمثلة |
| --- | --- |
| [إعلانات ومنتجات · 6](prompts/01-ads-and-products.md) | [1. Dew Drop Laboratory — skincare serum macro](prompts/01-ads-and-products.md#1-dew-drop-laboratory--skincare-serum-macro) · [2. Cold Brew Eclipse — coffee launch film](prompts/01-ads-and-products.md#2-cold-brew-eclipse--coffee-launch-film) · [3. Street-to-Studio — performance shoe demonstration](prompts/01-ads-and-products.md#3-street-to-studio--performance-shoe-demonstration) · [4. Doorstep Dinner — food delivery social ad](prompts/01-ads-and-products.md#4-doorstep-dinner--food-delivery-social-ad) · [5. Silver Current — artisan jewelry reveal](prompts/01-ads-and-products.md#5-silver-current--artisan-jewelry-reveal) · [6. One Tap Away — clean mobile app promo](prompts/01-ads-and-products.md#6-one-tap-away--clean-mobile-app-promo) |
| [قصص سينمائية · 6](prompts/02-cinematic-storytelling.md) | [1. Last Tram Note — restrained urban romance](prompts/02-cinematic-storytelling.md#1-last-tram-note--restrained-urban-romance) · [2. Room 407 — quiet hotel mystery](prompts/02-cinematic-storytelling.md#2-room-407--quiet-hotel-mystery) · [3. Glasshouse Pursuit — grounded parkour action](prompts/02-cinematic-storytelling.md#3-glasshouse-pursuit--grounded-parkour-action) · [4. Tidekeeper — coastal fantasy ritual](prompts/02-cinematic-storytelling.md#4-tidekeeper--coastal-fantasy-ritual) · [5. Paper Moon Delivery — hand-drawn animation](prompts/02-cinematic-storytelling.md#5-paper-moon-delivery--hand-drawn-animation) · [6. Europa Signal — hard-science discovery](prompts/02-cinematic-storytelling.md#6-europa-signal--hard-science-discovery) |
| [التواصل الاجتماعي والحياة اليومية · 6](prompts/03-social-ugc.md) | [1. Shelf Test — honest skincare mini-review](prompts/03-social-ugc.md#1-shelf-test--honest-skincare-mini-review) · [2. Twelve-Minute Noodles — one-pan recipe reel](prompts/03-social-ugc.md#2-twelve-minute-noodles--one-pan-recipe-reel) · [3. First Set — realistic morning fitness log](prompts/03-social-ugc.md#3-first-set--realistic-morning-fitness-log) · [4. One Question, One Corner — street interview](prompts/03-social-ugc.md#4-one-question-one-corner--street-interview) · [5. Clay Cup Morning — tactile pottery ASMR](prompts/03-social-ugc.md#5-clay-cup-morning--tactile-pottery-asmr) · [6. Umbrella Reset — seamless pet comedy loop](prompts/03-social-ugc.md#6-umbrella-reset--seamless-pet-comedy-loop) |
| [شخصيات وصور مرجعية · 6](prompts/04-characters-and-references.md) | [1. Harbor Cartographer — consistent character introduction](prompts/04-characters-and-references.md#1-harbor-cartographer--consistent-character-introduction) · [2. Linen Set — virtual try-on walk test](prompts/04-characters-and-references.md#2-linen-set--virtual-try-on-walk-test) · [3. Counter Demo — product placement without redesign](prompts/04-characters-and-references.md#3-counter-demo--product-placement-without-redesign) · [4. Two Voices, One Repair — synchronized dialogue scene](prompts/04-characters-and-references.md#4-two-voices-one-repair--synchronized-dialogue-scene) · [5. Sunday Table — consistent three-person ensemble](prompts/04-characters-and-references.md#5-sunday-table--consistent-three-person-ensemble) · [6. Parcel Finch — reusable brand mascot motion](prompts/04-characters-and-references.md#6-parcel-finch--reusable-brand-mascot-motion) |
| [التحرير والتمديد · 6](prompts/05-editing-and-extension.md) | [1. Blue Hour Conversion — day-to-night architectural edit](prompts/05-editing-and-extension.md#1-blue-hour-conversion--day-to-night-architectural-edit) · [2. First Snow — controlled weather replacement](prompts/05-editing-and-extension.md#2-first-snow--controlled-weather-replacement) · [3. Clean Plate — remove one distracting object](prompts/05-editing-and-extension.md#3-clean-plate--remove-one-distracting-object) · [4. Practical Miniature — change rendering style, keep motion](prompts/05-editing-and-extension.md#4-practical-miniature--change-rendering-style-keep-motion) · [5. Beyond the Gate — continue a travel shot](prompts/05-editing-and-extension.md#5-beyond-the-gate--continue-a-travel-shot) · [6. Turntable Loop — repair a product animation into a seamless cycle](prompts/05-editing-and-extension.md#6-turntable-loop--repair-a-product-animation-into-a-seamless-cycle) |

<a id="featured-prompts"></a>

## نصوص توجيه مصوّرة للنسخ والتعديل

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. زجاجة من زجاج البحر: مقارنة حركات مضبوطة

**إعدادات تحويل الصورة إلى فيديو:** 5s · 16:9 · 720p · [إطار البداية: افتح الصورة واحفظها](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/ar/sea-glass-bottle.txt)

```text
حافظ على الزجاجة الوحيدة من زجاج البحر المصنفر فوق السطح الحجري الفاتح، وغطائها الأسطواني، وواجهتها الخالية من الطباعة، ومستوى الماء، والأفق، والإضاءة الجانبية الناعمة. لا تتحرك الزجاجة مطلقًا.
خلال خمس ثوانٍ، حرّك الكاميرا ببطء نحو اليمين لمسافة لا تتجاوز عرض زجاجة واحدة.
تنزلق قطرة ماء صغيرة على الواجهة وتتوقف عند القاعدة. تتحرك أمواج البحر الضبابية في الخلفية برفق. اجعل الانعكاسات متسقة مع الكاميرا ومصدر الضوء.
الصوت: أمواج بعيدة فقط؛ بلا موسيقى أو صوت بشري أو اصطدام زجاج أو رذاذ مبالغ فيه.
بلا قطع أو تقريب. حافظ على شكل الزجاجة ومحاذاة الغطاء وملمس الزجاج وعدد العناصر.
تجنّب توليد شعارات أو تغيير مستوى السائل أو ثني الحواف أو جعل العناصر تطفو أو إضافة إكسسوارات جديدة.
ثبّت الإطار خلال الثانية الأخيرة.
```

[العودة إلى فهرس الفئات](#find-the-right-prompt) · [نظرة سريعة على الأمثلة المصوّرة](#visual-index)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. المسار الأزرق: تتبّع مندوب توصيل في سوق ممطر

**إعدادات تحويل الصورة إلى فيديو:** 10s · 16:9 · 1080p · [إطار البداية: افتح الصورة واحفظها](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/ar/blue-route.txt)

[المصدر: Flaq AI](docs/ATTRIBUTION.md)

```text
حافظ على مندوب التوصيل والدراجة الكهربائية الزرقاء الكوبالتية وصندوق الحمولة والسوق المرتفع والمظلات شبه الشفافة والممر الفولاذي المبتل والإضاءة ولوحة الألوان الليلية في الصورة. أنشئ لقطة تتبّع واحدة منخفضة ومتصلة وواقعية، بكتلة وتماسك إطارات ومطر وتعليق مقنعة.

0–3s: تتسارع الدراجة بسلاسة من وضعها الحالي. يدفع الإطار الخلفي مروحة رقيقة من الماء، وينضغط نظام التعليق فوق فاصل تصريف. تتبع الكاميرا الدراجة من جانبها وخلفها قليلًا عند مستوى العجلات، بالسرعة نفسها ودون اهتزاز عنيف.

3–7s: يميل المندوب في منعطف يساري واسع واحد. تنثني المظلات مع الريح، ويتصاعد البخار من أكشاك الطعام، وتترك المصابيح الدافئة داخل المشهد خطوطًا ناعمة في الانعكاسات المبتلة. أبقِ العجلتين دائريتين وملامستين للأرض.

7–10s: تستقيم الدراجة وتتجه نحو جزء مفتوح وأكثر إضاءة من السوق. تتراجع الكاميرا نصف متر لتكشف الطريق أمامها، ثم تثبّت إطار النهاية.

الصوت: أزيز واقعي لمحرك كهربائي، ورذاذ ماء، ومطر على المظلات، وأصوات سوق خافتة، وطرقة واحدة للتعليق. بلا موسيقى تصويرية أو حوار أو صفارات إنذار أو انفجارات.

ثبات المشهد: حافظ بدقة على زي الراكب وخوذته وهندسة الدراجة وصندوق الحمولة والألواح الزرقاء وتخطيط السوق. بلا تحوّل للمركبة أو تشوّه للعجلات أو تصادم أو أسلحة أو لافتات مقروءة أو شعارات أو انتقال آني للكاميرا أو تغيّر مستحيل في السرعة.
```

[العودة إلى فهرس الفئات](#find-the-right-prompt) · [نظرة سريعة على الأمثلة المصوّرة](#visual-index)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. رغيف العسل: حكاية مخبز مصغّر

**إعدادات تحويل الصورة إلى فيديو:** 9s · 16:9 · 1080p · [إطار البداية: افتح الصورة واحفظها](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/ar/honey-loaf.txt)

[المصدر: Flaq AI](docs/ATTRIBUTION.md)

```text
حافظ على المخبز في بيت على شكل كمثرى، والخبازين الثلاثة المصغّرين، والأزياء والوجوه ورغيف العسل والفرن والنافذة والطحلب والبرسيم والقمر والخامات الملموسة لتحريك الدمى إطارًا بإطار والتباين بين الألوان الدافئة والباردة.

0–3s: ابدأ بالتكوين الواسع المرفق بإيقاع يدوي خفيف لتحريك الدمى إطارًا بإطار. يرفع خبازان رغيف العسل الدافئ معًا؛ وتظل أيديهما ملامسة للوح الخشبي. ترتفع نفخة طحين صغيرة، وتتراقص نار الفرن، ويفتح الخباز الثالث نافذة الخدمة.

3–7s: يخطو الاثنان أربع خطوات حذرة ومتزامنة نحو النافذة. للرغيف وزن مقنع، فينخفض قليلًا بينهما. في الخارج تسقط قطرة ندى من ورقة برسيم، وتمر يراعتان على عمقين مختلفين. تتحرك الكاميرا في قوس لطيف قدره خمس درجات نحو اليمين.

7–9s: يدفعان اللوح إلى سطح البيع، ويتبادلان ابتسامتي ارتياح، ويستقر وهج الفرن. اختم والخبازون الثلاثة ظاهرون والرغيف في المنتصف.

الصوت: خطوات صغيرة على الخشب، وطقطقة فرن هادئة، وصرير اللوح، وحشرات ليلية خافتة، وجرس صغير واحد عند نافذة الخدمة. بلا حوار أو تعليق صوتي أو موسيقى أو نص.

ثبات المشهد: حافظ على عدد الشخصيات وتصميم الوجوه والمقياس وألوان الملابس وشكل الكمثرى وترتيب الغرفة والملمس اليدوي. بلا خبازين إضافيين أو رسوم حاسوبية لامعة أو أطراف مطاطية أو أدوات عائمة أو رغيف يذوب أو قطع كاميرا أو شعارات أو شخصيات تشبه شخصيات سلاسل معروفة.
```

[العودة إلى فهرس الفئات](#find-the-right-prompt) · [نظرة سريعة على الأمثلة المصوّرة](#visual-index)

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. لقاء في الميناء: لحظة عاطفية واحدة

**إعدادات تحويل الصورة إلى فيديو:** 10s · 16:9 · 720p · [إطار البداية: افتح الصورة واحفظها](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/ar/harbor-reunion.txt)

```text
حافظ على الشخصين البالغين ووجهيهما والملابس الكحلية والكريمية والرصيف الخشبي وضوء الصباح الناعم في الصورة المرفقة. أبقِ الشخصين في التكوين نفسه ضمن لقطة متوسطة واسعة.
0–3 ثوانٍ: يلاحظ الشخص على اليسار صديقه القادم ويخطو خطوة صغيرة. يرتخي كتفاه، ويردّ الصديق بابتسامة هادئة. أبقِ الأيدي ظاهرة ومرتخية.
3–7 ثوانٍ: يقول الشخص على اليسار بعربية طبيعية: «ها أنت ذا». يومئ الصديق برأسه مرة واحدة. اجعل العبارة هادئة، بلا بكاء أو تعابير وجه مبالغ فيها.
7–10 ثوانٍ: ينظر الاثنان نحو القارب الراسي. ثبّت اللقطة في الثانية الأخيرة لتمهيد القطع إلى اللقطة التالية.
الكاميرا: اقتراب لطيف واحد، بلا لقطة عكسية أو قطع.
الصوت: كلام قريب وواضح، وصوت ماء الميناء الهادئ ونورس بعيد؛ بلا موسيقى أو ترجمة مكتوبة.
ثبّت هويتي الشخصين والملابس وهندسة الرصيف وموضع القارب واتجاه ضوء الصباح.
تجنّب أشخاصًا إضافيين، وإيماءات درامية، وتنعيم الوجوه، وأصابع إضافية، وقفزات الكاميرا.
```

[العودة إلى فهرس الفئات](#find-the-right-prompt) · [نظرة سريعة على الأمثلة المصوّرة](#visual-index)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. الرشفة الأولى: مراجعة طبيعية لصانعة محتوى في مقهى

**إعدادات تحويل الصورة إلى فيديو:** 10s · 9:16 · 1080p · [إطار البداية: افتح الصورة واحفظها](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/ar/first-sip.txt)

[المصدر: Flaq AI](docs/ATTRIBUTION.md)

```text
حرّك صورة المقهى المرفقة على هيئة مراجعة صادقة لصانعة محتوى مصوّرة بكاميرا محمولة باليد. حافظ على وجهها وعمرها وملمس بشرتها وشعرها وسترتها الخضراء الطحلبية والكوب والمعجنات والنافذة وترتيب الطاولة.

0–3s: حركة يدويّة لطيفة وطبيعية للكاميرا. تنهي رشفة، وتخفض الكوب الخزفي نحو عشرة سنتيمترات، وتزفر مع ابتسامة صغيرة، وتنقل نظرها من النافذة إلى الكاميرا. يتصاعد البخار ملتفًا، وتندمج مسارات المطر ببطء على الزجاج خلفها.

3–8s: تقول بعربية طبيعية وبنبرة حوارية مسترخية: «كريمي، وحلاوته خفيفة… وطعم الشوفان واضح فعلًا». اجعل الأداء عفويًا مع وقفة قصيرة بعد «خفيفة». طابق حركة الشفاه بدقة، وأبقِ الكوب ثابتًا في يدها.

8–10s: تومئ إيماءة إعجاب صغيرة وتنظر إلى المعجنات بينما تستقر الكاميرا.

الصوت: صوت قريب كما يسجله هاتف، وأجواء مقهى هادئة، وجهاز تبخير حليب بعيد، ومطر ناعم، وتلامس كوب خزفي. الكلام في المقدمة والأجواء منخفضة. بلا موسيقى خلفية أو ترجمة مكتوبة.

ثبات المشهد: بلا تجميل للوجه أو تغيير للملابس أو أصابع إضافية أو إعادة تصميم للكوب أو الطعام أو ظهور أشخاص في الخلفية أو شعارات أو إيماءات مبالغ فيها لصانعة المحتوى.
```

[العودة إلى فهرس الفئات](#find-the-right-prompt) · [نظرة سريعة على الأمثلة المصوّرة](#visual-index)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. خط الملح عند الفجر: فيلم وثائقي عن السفر

**إعدادات تحويل الصورة إلى فيديو:** 12s · 16:9 · 1080p · [إطار البداية: افتح الصورة واحفظها](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/ar/salt-line.txt)

[المصدر: Flaq AI](docs/ATTRIBUTION.md)

```text
حرّك مشهد أحواض الملح الساحلية المرفق كفيلم سفر وثائقي يرصد المكان باحترام. حافظ على العاملين والقطار بلونَي الكريم والمغرة وأحواض الملح والتلال الجيرية والمباني والبحر واتجاه الشروق ولوحة الألوان السينمائية الهادئة.

0–4s: لقطة واسعة ثابتة. يواصل العاملان فحص القناة: يحرّك أحدهما أداة خشبية في الماء الملحي الضحل، بينما يثبّت الآخر الحاجز. تستجيب تموجات الماء للأداة ونسيم الصباح. يقترب القطار بسرعة معتدلة في المستوى المتوسط.

4–9s: تتحرك الكاميرا أفقيًا ببطء نحو اليمين لتتبع القطار. تبقى العجلات محاذية للقضبان، والمسافات بين العربات وإيقاع النوافذ ثابتة. ينساب حجاب خفيف من ضباب البحر خلفه بينما تصل أشعة الشمس تدريجيًا إلى بلورات الملح في المقدمة.

9–12s: يتابع القطار نحو الساحل، وتتوقف حركة الكاميرا برفق. يقف أحد العاملين ويتمدد طبيعيًا وينظر نحو الخط. ثبّت الثانيتين الأخيرتين لتوفير نقطة مناسبة للمونتاج.

الصوت: همهمة كهربائية خفيفة للقطار، وإيقاع العجلات عند الفواصل، ونسيم فوق الماء الضحل، ونوارس بعيدة، وأداة خشبية تتحرك في الماء الملحي. بلا تعليق صوتي أو موسيقى أو حشود أو بوق درامي.

ثبات المشهد: عمل واقعي، وتشريح مستقر، ومنظر ثابت، وتصميم قطار دون تغيير، وانعكاسات وفيزياء ماء معقولة. بلا أفق مدينة حديثة أو استعراض سياحي مُفتعل أو مبانٍ جديدة أو شعارات أو لافتات مقروءة أو ألوان بطاقات مشبعة بإفراط أو سماء مسرّعة.
```

[العودة إلى فهرس الفئات](#find-the-right-prompt) · [نظرة سريعة على الأمثلة المصوّرة](#visual-index)

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. بطاقة ساحلية: حرّك صورة مخططة مسبقًا

**إعدادات تحويل الصورة إلى فيديو:** 5s · 9:16 · 720p · [إطار البداية: افتح الصورة واحفظها](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/ar/coastal-postcard.txt)

```text
حرّك هذه البطاقة الساحلية المؤلفة من ثلاث لوحات دون تغيير ترتيبها أو حدودها. حافظ بدقة على جميع العناصر والألوان. في اللوحة العليا، يتصاعد خيط رفيع ملتف من البخار من الكوب.
في اللوحة الوسطى، يتموّج ماء الميناء برفق ويلمع ضوء الشمس على سطحه.
في اللوحة السفلى، يرتفع قليلًا طرف الورقة الموجود أصلًا ثم يستقر مع نسمة خفيفة؛ ولا يتحرك غيره.
أبقِ كل حركة داخل لوحتها. تظل جميع اللوحات ظاهرة طوال الثواني الخمس.
الكاميرا: ثابتة، بلا تقريب أو تحريك أفقي أو قطع أو انتقالات بين اللوحات.
الصوت: ماء هادئ وحفيف ورق خفيف؛ بلا حوار أو موسيقى أو عناوين توضيحية أو نص مضاف.
حافظ على مقبض الكوب وإطار النافذة وعلامات الخريطة وأبعاد اللوحات وترتيب القراءة.
تجنّب دمج اللوحات أو اختراع مشهد جديد أو إعادة رسم الحروف أو نقل العناصر عبر الحدود.
أنهِ الفيديو وطرف الورقة مستقر والتكوين الأصلي سليم.
```

[العودة إلى فهرس الفئات](#find-the-right-prompt) · [نظرة سريعة على الأمثلة المصوّرة](#visual-index)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. هالة الحمضيات: فيلم لمنتج عطر فاخر

**إعدادات تحويل الصورة إلى فيديو:** 8s · 16:9 · 1080p · [إطار البداية: افتح الصورة واحفظها](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/ar/citrus-halo.txt)

[المصدر: Flaq AI](docs/ATTRIBUTION.md)

```text
حافظ على تصميم الزجاجة المرفقة ونسب الزجاج والغطاء والقاعدة الجيرية وقشر الجريب فروت والديكور العاجي الدافئ والإضاءة الجانبية الذهبية. أنشئ فيلم منتج أنيقًا مدته ثماني ثوانٍ.

0–2.5s: ابدأ بتكوين ماكرو شبه ثابت. تتقدم الكاميرا ببطء شديد. تلتقط حبيبات التكاثف الضوء، وتنزلق قطرتان طبيعيًا على الزجاج البارد. يرتفع قشر الجريب فروت من القاعدة كأن نسيم استوديو مضبوط يحمله.

2.5–6s: يكمل القشر دورة حلزونية رشيقة واحدة حول الزجاجة دون لمس الغطاء أو حجبه. تعبر جسيمات رذاذ حمضيات دقيقة الضوء الخلفي. يتحرك الانكسار وبؤر الضوء المتجمعة حركة فيزيائية سليمة عبر الزجاج السميك، وتبقى الزجاجة نفسها صلبة تمامًا.

6–8s: يستقر القشر في انحنائه الأصلي، وتتوقف الكاميرا برفق، وتعبر لمعة انعكاسية ساطعة مرة واحدة على حافة الزجاجة. اختم بلقطة رئيسية نظيفة للمنتج.

الصوت: مؤثرات استوديو قريبة فقط — حركة ناعمة لشريط القشر، وقطرتا ماء واضحتان، ورنين زجاجي رقيق. بلا صوت بشري أو موسيقى أو نص.

ثبات المشهد: لا تغيّر شكل الزجاجة أو أوجه الغطاء أو مستوى السائل أو القاعدة أو لوحة الألوان أو القوس الخلفي. بلا ملصق أو شعار أو فاكهة إضافية أو زجاجة عائمة أو هندسة متذبذبة أو قفزة كاميرا أو انفجار لمعان مصطنع.
```

[العودة إلى فهرس الفئات](#find-the-right-prompt) · [نظرة سريعة على الأمثلة المصوّرة](#visual-index)

<a id="learn-from-official-and-community-examples"></a>

## تعلّم من الأعمال الرسمية وأعمال المجتمع

تحدّد المنشورات الأصلية اسم المبدع وإصدار النموذج. افتح الأصول لمشاهدة الفيديوهات؛ تشرح الملاحظات العملية أدناه أساليب العمل، ولا تعني أننا أعدنا إنتاج هذه الفيديوهات.

### [تسلسل رسمي من 1.5 Preview: Grok / Heavy Pulp](https://x.com/grok/status/2062225080843747351)

[![تسلسل رسمي من 1.5 Preview: Grok / Heavy Pulp](https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg)](https://x.com/grok/status/2062225080843747351)

تعلّم تخطيط إعلان تشويقي على هيئة لقطات قصيرة منفصلة. ميّز مواد Preview عن نتائج نموذج 1.5 الصادر.

### [فيلم قصير مكتمل: JSFILMZ](https://x.com/JSFILMZ0412/status/2062480692835938771)

يذكر المؤلف أنه أنشأ فيلمًا مدته 2.5 دقيقة، ويناقش حدود الأداء التمثيلي المولّد. تدرّب أولًا على تبادل هادئ للكلام، ثم ابنِ القصص الأطول من لقطات مجمّعة بالمونتاج.

### [تخطيط الصورة قبل تحريكها: GENEL](https://x.com/genel_ai/status/2061382998873034825)

[![تخطيط الصورة قبل تحريكها: GENEL](https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg)](https://x.com/genel_ai/status/2061382998873034825)

يذكر المبدع أنه صنع صورة مجمّعة باستخدام ChatGPT Images 2.0 ثم حرّكها باستخدام Grok Imagine Video 1.5. في تمرين البطاقة لدينا تبقى حدود اللوحات ثابتة، وتُخصص حركة واحدة فقط لكل لوحة.

### [مقارنة مضبوطة: JSFILMZ](https://x.com/JSFILMZ0412/status/2061117682515050669)

استخدم صورة مصدر واحدة وإعدادات قابلة للمقارنة. افحص الهندسة والحركة والصوت بدل نسخ ترتيب قديم. يعزل تمرين الزجاجة هذه المتغيرات.

<details>
<summary>ملاحظات الإطارات وحدود التحقق</summary>

في 24 سبتمبر 2026، فحصنا إطارات مختارة في مشغّلات X الأصلية: في المقطع الرسمي قرب 3.6 ثانية (خوذة وجيش)، و19.8 ثانية (لقطة مقرّبة لوجه)، و34.6 ثانية (مدينة ساحلية تحترق)؛ وفي مقطع GENEL قرب 0.05 ثانية (سياج بمحاذاة البحر)، و4.9 ثانية (معبر سكة حديد)، و12 ثانية (يد بإضاءة خلفية). ادرس تغيّر أحجام اللقطات في المقطع الرسمي واتساق الضوء الساحلي بين لقطات GENEL المنفصلة. تمرين البطاقة ذي اللوحات الثابتة لدينا مختلف. هذه إطارات مختارة، وليست اختبارات كاملة للحركة أو الصوت.

</details>

[المصادر وملاحظات المشاهدة (بالإنجليزية)](docs/COMMUNITY.md)

<a id="writing-guide"></a>

<a id="اختبار-متعدد-اللغات-ورشة-المصباح-الخزفي"></a>

<a id="المكتبة-الكاملة"></a>

<a id="قواعد-سريعة"></a>

## مواد مرجعية

[مرجع الكتابة](docs/guides/ar.md) · [مرجع الإعدادات والتشغيل](docs/workflows/ar.md) · [SeaImagine](https://seaimagine.com/ar/model/grok-imagine-1-5/)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

<a id="multilingual-prompts"></a>

## المجموعة ونسب المحتوى إلى مصدره

المجموع 38 وصفة مختلفة بالإنجليزية: 35 وصفة من المجموعة الأصلية وهذه التمارين الثلاثة الجديدة. الترجمات لا تضيف سيناريوهات جديدة.

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/ar/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
