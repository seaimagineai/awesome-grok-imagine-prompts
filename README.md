# Grok Imagine 1.5 Prompt Library

> 65 prompts, including 11 illustrated cases available in 15 languages. Browse by category and copy complete prompts.

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Prompts](https://img.shields.io/badge/English_recipes-65-7c3aed)](#prompt-library)
[![Languages](https://img.shields.io/badge/languages-15-0ea5e9)](#multilingual-prompts)

![Grok Imagine 1.5 — Open prompt notebook with a product shoe, tram and paper whale in one continuous scene](assets/seaimagine-grok-hero.webp)

Adapted from [Flaq AI](https://github.com/flaqai/awesome-grok-imagine), maintained by SeaImagine. Independent of xAI; concept images are not verified Grok outputs. [Attribution](docs/ATTRIBUTION.md) · [MIT](LICENSE).

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## Category index

[Browse more prompts (English) · 65](docs/PROMPT_INDEX.md)

| Category | Scenes | Modes | Examples |
| --- | --- | --- | --- |
| [Products & advertising · 8](docs/PROMPT_INDEX.md#01-ads-and-products) | Skincare close-ups / coffee / jewelry / app ads | Text to video / Image to video / Reference to video | [Sea-glass bottle — a controlled motion comparison](#case-sea-glass-bottle) · [Citrus Halo — premium fragrance product film](#case-citrus-halo) |
| [Cinematic storytelling · 7](docs/PROMPT_INDEX.md#02-cinematic-storytelling) | Action / romance / suspense / science fiction / animation | Text to video / Image to video / Video extension | [Blue Route — rain-market courier tracking shot](#case-blue-route) |
| [Social & everyday life · 8](docs/PROMPT_INDEX.md#03-social-ugc) | Personal reviews / food / fitness / interviews | Text to video / Image to video / Reference to video | [First Sip — authentic café UGC review](#case-first-sip) · [Salt Line at Dawn — travel documentary](#case-salt-line) |
| [Characters & dialogue · 7](docs/PROMPT_INDEX.md#04-characters-and-references) | Characters / clothing / dialogue / ensemble scenes | Reference to video / Image to video | [The Last Tooth — a clockmaker duet](#case-clockwork-dialogue) |
| [Visual transformations & continuation · 7](docs/PROMPT_INDEX.md#05-editing-and-extension) | Weather changes / cleanup / restyling / continuation | Video editing / Video extension / Image to video | [Rain Reaches the Arcade — a continuous weather transformation](#case-rainlit-arcade) |
| [Satisfying materials & sounds · 7](docs/PROMPT_INDEX.md#07-satisfying-materials) | Sand pressing / copper foil / water droplets / marbling | Text to video / Image to video | [Amber Orchard — one translucent slice](#case-amber-orchard) |
| [Spaces & architecture · 7](docs/PROMPT_INDEX.md#08-spaces-and-transformations) | Unfolding furniture / courtyards / house cutaways | Text to video / Image to video | [Unfolding Atrium — a mechanical greenhouse reveal](#case-unfolding-atrium) |
| [Miniature & surreal worlds · 7](docs/PROMPT_INDEX.md#09-miniature-and-surreal) | Teacup ferries / rainy drawers / paper moons | Text to video / Image to video | [The Honey Loaf — miniature bakery story](#case-honey-loaf) |
| [Fashion & performance · 7](docs/PROMPT_INDEX.md#10-fashion-and-performance) | Flowing skirts / capes / collar projections / dance steps | Text to video / Image to video | [Cobalt Orbit — a full-turn fashion study](#case-cobalt-orbit) |

[Illustrated examples](#featured-prompts) · [Create with SeaImagine](#create-with-seaimagine)

<a id="visual-index"></a>

<a id="featured-prompts"></a>

## Illustrated prompts to copy and adapt

11 cases with full prompts and starting-frame images. Images illustrate concepts; they are not verified video outputs.

The five cases labeled Source: Flaq AI preserve their original duration and resolution; the other six use current SeaImagine options. To use a source case on SeaImagine, choose 5/10/15 seconds and 480p/720p and rewrite its timed actions.

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. Sea-glass bottle — a controlled motion comparison

![Sea-glass bottle — a controlled motion comparison](assets/seaimagine-sea-glass-bottle.webp)

**Image-to-video settings:** 5s · 16:9 · 720p · [Starting frame — open and save](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/en-US/sea-glass-bottle.txt)

```text
Preserve the single frosted sea-glass bottle on the pale stone surface, its cylindrical cap,
empty unprinted front, water level, horizon and soft side lighting. The bottle never moves.
Over five seconds, make a slow camera slide to the right, no more than one bottle-width.
One small water droplet travels down the front and stops at the base. Background ocean waves
move softly out of focus. Keep reflections consistent with the camera and the light source.
Audio: distant surf only; no music, voice, glass impact or exaggerated splash.
No cuts or zoom. Preserve the bottle silhouette, cap alignment, glass texture and object count.
Avoid logo generation, changing liquid level, bending edges, floating objects or new props.
Hold a stable frame for the final second.
```

[Back to category index](#find-the-right-prompt)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. Blue Route — rain-market courier tracking shot

![Blue Route — rain-market courier tracking shot](assets/rainy-market-courier-video.webp)

**Image-to-video settings:** 10s · 16:9 · 1080p · [Starting frame — open and save](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/en-US/blue-route.txt)

[Source: Flaq AI](docs/ATTRIBUTION.md)

```text
Preserve the supplied courier, cobalt electric motorcycle, cargo box, elevated market,
translucent awnings, wet steel walkway, lighting, and night palette. Create one grounded,
continuous low tracking shot with convincing mass, tire grip, rain, and suspension.

0–3s: the motorcycle accelerates smoothly from the existing pose. The rear tire displaces a
thin fan of water; suspension compresses over a drainage seam. Camera tracks beside and just
behind the bike at wheel height, matching speed without shaking violently.

3–7s: the courier leans through one broad left curve. Awnings flex in the wind, steam rolls
from the food stalls, and warm practical lights streak softly in the wet reflections. Keep
both wheels round and in contact with the ground.

7–10s: the bike straightens and moves toward a brighter open section of the market. The
camera falls back half a meter, revealing the route ahead, then holds a stable ending frame.

Audio: realistic electric motor whine, water spray, rain on awnings, subtle market voices,
one suspension thump. No score, dialogue, sirens, or explosions.

Continuity lock: exact rider outfit, helmet, motorcycle geometry, cargo box, blue panels,
and market layout. No vehicle morphing, wheel deformation, collisions, weapons, readable
signs, logos, teleporting camera, or impossible speed ramp.
```

[Back to category index](#find-the-right-prompt)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. The Honey Loaf — miniature bakery story

![The Honey Loaf — miniature bakery story](assets/pear-bakery-miniature-video.webp)

**Image-to-video settings:** 9s · 16:9 · 1080p · [Starting frame — open and save](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/en-US/honey-loaf.txt)

[Source: Flaq AI](docs/ATTRIBUTION.md)

```text
Keep the pear-house bakery, three miniature bakers, costumes, faces, honey loaf, oven,
window, moss, clover, moon, tactile stop-motion materials, and warm-cool color contrast.

0–3s: begin on the supplied wide composition with subtle handmade stop-motion cadence. Two
bakers lift the warm honey loaf together; their hands stay attached to the wooden board. A
small flour puff rises, oven fire flickers, and the third baker opens the service window.

3–7s: the pair take four careful synchronized steps toward the window. The loaf has believable
weight, dipping slightly between them. Outside, one clover leaf releases a dew drop and two
fireflies drift past at different depths. Camera makes a gentle five-degree arc to the right.

7–9s: they slide the board onto the counter, exchange relieved smiles, and the oven glow
settles. End with all three characters visible and the loaf centered.

Audio: tiny foot taps on wood, soft oven crackle, board creak, faint night insects, one small
bell at the service window. No dialogue, narration, music, or text.

Continuity lock: preserve character count, facial design, scale, wardrobe colors, pear shape,
room layout, and handcrafted texture. No extra bakers, glossy CGI, rubber limbs, floating
props, melting loaf, camera cuts, logos, or franchise-like character design.
```

[Back to category index](#find-the-right-prompt)

<a id="case-clockwork-dialogue"></a>

<a id="seaimagine-clockwork-dialogue"></a>

### 4. The Last Tooth — a clockmaker duet

![The Last Tooth — a clockmaker duet](assets/clockwork-dialogue.png)

**Image-to-video settings:** 10s · 16:9 · 720p · [Starting frame — open and save](assets/clockwork-dialogue.png) · [TXT](prompts/text/en-US/clockwork-dialogue.txt)

```text
Animate this reference as a restrained ten-second film scene. Keep both adult restorers, the open brass astronomical clock, the single loose gear and the moonlit observatory exactly recognizable. The short-haired woman in navy workwear remains screen left; the gray-haired man in an ochre apron remains screen right. Frame both from the waist up across the workbench.

0–3s: hold the two-shot with a barely perceptible forward push. The woman studies the clock, then asks quietly in English, “Will it keep time?” The man watches the clock mechanism. Only she speaks; her lips follow the words. The clock already ticks slowly, its visible escapement rocking steadily.

3–7s: the man listens closely to the ticking, keeping his hands relaxed and still. The loose gear stays motionless on the tabletop; nobody touches it. After a short listening pause he answers in English, “It will now.” His lips alone move for this line. The clock and escapement maintain the same unhurried rhythm.

7–10s: she looks from the clock to him and releases a small, relieved smile. He returns her glance. Finish on their shared pause, with the clock ticking between them and cool moonlight outlining their shoulders.

Audio: close, dry dialogue and a delicate slow clock tick present from the first frame in the hollow room. No music, overlapping speech or gear-movement sound.

Keep the loose gear separate and stationary throughout; nobody installs it. Preserve hand anatomy, clock internals, wardrobe, eye lines and left/right positions. Do not start the clock with a gesture. No extra tools, extra gears, subtitles, camera cuts or exaggerated gestures.
```

[Back to category index](#find-the-right-prompt)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. First Sip — authentic café UGC review

<a href="assets/cozy-cafe-ugc-video.webp"><img src="assets/cozy-cafe-ugc-video.webp" width="480" alt="First Sip — authentic café UGC review"></a>

**Image-to-video settings:** 10s · 9:16 · 1080p · [Starting frame — open and save](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/en-US/first-sip.txt)

[Source: Flaq AI](docs/ATTRIBUTION.md)

```text
Animate the supplied café photo as an honest handheld creator review. Preserve the person's
face, age, skin texture, hair, moss-green sweater, cup, pastry, window, and table layout.

0–3s: gentle natural handheld drift. She finishes a sip, lowers the ceramic cup about ten
centimeters, exhales through a small smile, and looks from the window back to the camera.
Steam curls upward and rain trails slowly merge on the glass behind her.

3–8s: she says, in a relaxed conversational voice, “Creamy, not too sweet — and you can
actually taste the oats.” Keep the delivery casual, with one tiny pause after “sweet.” Match
lip movement closely and keep the cup steady in her hand.

8–10s: she gives a small approving nod and glances down at the pastry as the camera settles.

Audio: close smartphone voice, quiet café room tone, distant milk steamer, soft rain, ceramic
cup contact. Voice is foreground; ambience stays low. No background music and no subtitles.

Continuity lock: no face beautification, no wardrobe change, no extra fingers, no cup or food
redesign, no background people appearing, no logos, and no exaggerated influencer gestures.
```

[Back to category index](#find-the-right-prompt)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. Salt Line at Dawn — travel documentary

![Salt Line at Dawn — travel documentary](assets/coastal-salt-train-documentary.webp)

**Image-to-video settings:** 12s · 16:9 · 1080p · [Starting frame — open and save](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/en-US/salt-line.txt)

[Source: Flaq AI](docs/ATTRIBUTION.md)

```text
Animate the supplied coastal salt-pond scene as a respectful observational travel documentary.
Preserve the two workers, cream-and-ochre train, salt beds, limestone hills, buildings, sea,
sunrise direction, and muted film palette.

0–4s: locked wide frame. The workers continue inspecting the channel: one guides a wooden
tool through the shallow brine while the other steadies the divider. Water ripples respond to
the tool and morning breeze. The train approaches at a measured speed in the midground.

4–9s: camera pans slowly right to follow the train. Wheels stay aligned to the rails; carriage
spacing and window rhythm remain consistent. A light veil of sea haze drifts behind it while
sunlight gradually catches the salt crystals in the foreground.

9–12s: the train passes toward the coast and the pan eases to a stop. One worker stands,
stretches naturally, and looks toward the line. Hold the final two seconds for an edit point.

Audio: soft electric rail hum, rhythmic wheel joints, breeze across shallow water, distant
gulls, wooden tool moving through brine. No narration, music, crowd, or dramatic horn.

Continuity lock: realistic labor, stable anatomy, fixed landscape, unchanged train design,
plausible reflections and water physics. No modern skyline, tourist staging, new buildings,
logos, readable signs, oversaturated postcard color, or time-lapse sky.
```

[Back to category index](#find-the-right-prompt)

<a id="case-rainlit-arcade"></a>

<a id="seaimagine-rainlit-arcade"></a>

### 7. Rain Reaches the Arcade — a continuous weather transformation

![Rain Reaches the Arcade — a continuous weather transformation](assets/rainlit-arcade.png)

**Image-to-video settings:** 10s · 16:9 · 720p · [Starting frame — open and save](assets/rainlit-arcade.png) · [TXT](prompts/text/en-US/rainlit-arcade.txt)

```text
Use the supplied empty Art Deco arcade as the exact first frame of a ten-second weather study. Preserve the deep-green tiles, brass trim, terrazzo floor, repeating arches and warm lamps along the left wall. The distant street opening stays blue with dusk. All interior flooring starts dry; the camera faces the opening from inside the arcade.

0–3s: a locked architectural composition with no pan or zoom. Beyond the far threshold, a gust drives rain diagonally across the street. The first scattered drops cross the opening and darken only the terrazzo immediately beside the threshold. The foreground remains completely dry.

3–7s: the gust strengthens, carrying fine rain farther along the same direction into the arcade. An irregular wet front advances from the far end toward the middle; successive drops visibly join existing patches. Small shallow puddles form in the wetted area. Preserve the existing soft reflections on the polished dry floor; in wetted areas, rain breaks them into rippling warm streaks.

7–10s: a final sweep of spray reaches the near-middle floor and slows. Keep the closest strip of foreground dry. Rain slackens; overlapping rings diminish in the shallow puddles while the warm reflections settle. Hold the unchanged arches against the blue opening.

Audio: exterior rain first, then increasingly close taps on stone, one low gust, and a soft arcade echo. No thunder, music or voices.

Maintain a continuous, visible path of arriving moisture: no instant whole-floor gloss or puddles ahead of the wet front. Keep water shallow, lamps steady, the camera level and all architectural lines rigid. No people, new plants, new signage, lightning flashes, flooding, camera cuts or remodeled surfaces.
```

[Back to category index](#find-the-right-prompt)

<a id="case-amber-orchard"></a>

<a id="seaimagine-amber-orchard"></a>

### 8. Amber Orchard — one translucent slice

![Amber Orchard — one translucent slice](assets/amber-orchard.png)

**Image-to-video settings:** 10s · 16:9 · 720p · [Starting frame — open and save](assets/amber-orchard.png) · [TXT](prompts/text/en-US/amber-orchard.txt)

```text
Create a ten-second surreal material close-up from the supplied reference. Preserve the transparent amber glass pear on its black stone plate, its tiny trapped bubbles and fine gold fibers. A single narrow knife enters from screen right, its tip already touching the pear’s right flank. No face or hand enters the frame. Treat the pear as a rigid, cleanly sliceable fantasy glass object: the impossible material is intentional, but its geometry must remain coherent.

0–3s: begin in a locked three-quarter macro view, keeping the entire pear and plate visible. Warm side light reveals the fibers. First withdraw the knife from its existing contact point, lift it above the right flank, then align it for one vertical cut that will remove a thin outer cheek, leaving the stem attached to the larger body.

3–7s: make one uninterrupted downward stroke. The blade passes through the right flank until its edge just meets the plate. A single clean cut plane progresses with the blade; only one slice separates. The main pear stays upright. The slice tips gently outward to the right, exposing its smooth amber cross-section, and comes to rest against the plate without shattering.

7–10s: lift the blade straight upward clear of the fruit and hold it still. Ease the camera forward only slightly to show the matching cut faces. End with the large pear body, one detached slice and the knife all readable in the frame.

Audio: a fine crystalline scrape during the cut, one bright chink as the slice meets stone, then a short natural ring. No music or speech.

Keep the bubbles and fibers fixed within their respective solid pieces. Preserve material transparency, pear silhouette outside the cut and the plate's position. No second stroke, duplicate slices, chips, liquid filling, melting, new fibers, floating fragments or camera cuts.
```

[Back to category index](#find-the-right-prompt)

<a id="case-unfolding-atrium"></a>

<a id="seaimagine-unfolding-atrium"></a>

### 9. Unfolding Atrium — a mechanical greenhouse reveal

![Unfolding Atrium — a mechanical greenhouse reveal](assets/unfolding-atrium.png)

**Image-to-video settings:** 10s · 16:9 · 720p · [Starting frame — open and save](assets/unfolding-atrium.png) · [TXT](prompts/text/en-US/unfolding-atrium.txt)

```text
Animate the supplied walnut-and-brass architectural model as a ten-second precision mechanism reveal. Keep the gray stone display plinth, miniature stairs and dense fern planting unchanged. The curved glass roof consists of exactly two curved roof halves, hinged along fixed axes at the central ridge. Both leaves start closed; the interior is already visible through the glass.

0–3s: establish the whole model in a close three-quarter view. Warm light grazes the walnut grain and small brass hinge barrels. The camera begins a slow, continuous upward move, looking gently down into the atrium. The roof stays closed for the first beat, then the outer eave edges begin to lift; the central ridge remains fixed.

3–7s: both roof halves rotate upward at the same measured speed about their fixed ridge hinges. Their outer eave edges rise to reveal the planted atrium; the central ridge does not separate. Show a controlled mechanical opening, retaining each half’s curvature and rigid brass frame. The camera rises just enough to reveal the stairwell; keep the entire plinth in frame.

7–10s: the leaves ease to matching open angles and stop without bouncing. Hold on the fern canopy and miniature stairs framed by the open roof. A soft patch of daylight reaches farther into the interior; the plants themselves stay still. End with the open structure clearly readable.

Audio: a subdued gear whirr synchronized with the roof motion, two nearly simultaneous end-stop clicks, then quiet room tone. No music or voice.

Keep exactly two rigid roof halves, fixed hinge axes at the ridge and the same interior layout. Nothing grows, unfolds from empty space or changes scale. No sliding roof panels, detached glass, bending metal, extra rooms, opening plinth, people or camera cuts.
```

[Back to category index](#find-the-right-prompt)

<a id="case-cobalt-orbit"></a>

<a id="seaimagine-cobalt-orbit"></a>

### 10. Cobalt Orbit — a full-turn fashion study

![Cobalt Orbit — a full-turn fashion study](assets/cobalt-orbit.png)

**Image-to-video settings:** 10s · 16:9 · 720p · [Starting frame — open and save](assets/cobalt-orbit.png) · [TXT](prompts/text/en-US/cobalt-orbit.txt)

```text
Animate the supplied fictional adult fashion model in a ten-second full-body couture portrait. Preserve her short black hair, copper disc earrings and sculptural cobalt-blue pleated gown. Keep the bare circular concrete room, overhead skylight and clean floor. She starts facing the camera with both feet planted and arms relaxed. Frame her from head to floor with generous room for the skirt.

0–3s: hold the camera completely still. After a brief front-facing pause, she begins a slow clockwise turn as seen from above, taking small controlled steps in place. Her shoulders lead naturally; the heavy pleated skirt follows with a slight delay. By three seconds she is in a clear quarter-turn profile.

3–7s: continue in the same direction at a calm runway pace. Pass through a readable back view near five seconds and the opposite profile near seven. Keep her centered on the same floor position. The pleats open and close subtly as fabric moves around her legs; the hem brushes the floor without lifting into a horizontal disk. Earrings swing only a little.

7–10s: complete exactly one 360-degree turn by nine seconds, arriving face-on again. Her feet settle, followed by the last small movement of the skirt. Hold the final frontal pose for the remaining second; she meets the lens with a composed expression.

Audio: soft footsteps on concrete, restrained fabric rustle and low room ambience. No music, dialogue or applause.

Maintain one identity, the original dress construction and a plausible continuous body beneath the garment. Keep head, hands and hem visible throughout. Skylight direction and background remain fixed. No camera orbit, extra rotation, cut, fabric color change, airborne hem, new accessories or elastic body distortion.
```

[Back to category index](#find-the-right-prompt)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 11. Citrus Halo — premium fragrance product film

![Citrus Halo — premium fragrance product film](assets/citrus-fragrance-product-video.webp)

**Image-to-video settings:** 8s · 16:9 · 1080p · [Starting frame — open and save](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/en-US/citrus-halo.txt)

[Source: Flaq AI](docs/ATTRIBUTION.md)

```text
Preserve the supplied bottle design, glass proportions, cap, limestone pedestal, grapefruit
peel, warm ivory set, and golden side light. Create an elegant eight-second product film.

0–2.5s: begin with a nearly locked macro composition. The camera makes a very slow dolly-in.
Condensation beads catch the light; two droplets slide naturally down the cold glass. The
grapefruit peel lifts from the pedestal as if carried by a controlled studio breeze.

2.5–6s: the peel completes one graceful spiral around the bottle without touching or
occluding the cap. Tiny citrus mist particles cross the backlight. Refraction and caustics
move physically through the thick glass; the bottle itself remains completely rigid.

6–8s: the peel settles into the original curve, the camera eases to a stop, and one bright
specular highlight travels once along the bottle edge. End on a clean hero frame.

Audio: intimate studio Foley only — a soft peel ribbon movement, two crisp water drops,
and a delicate glass resonance. No voice, no music, no text.

Continuity lock: do not alter the bottle silhouette, cap facets, liquid level, pedestal,
palette, or background arch. No label, logo, extra fruit, floating bottle, geometry wobble,
camera jump, or artificial sparkle explosion.
```

[Back to category index](#find-the-right-prompt)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

## Take your chosen shot to SeaImagine

Bring the glass-bottle shot, clockmakers’ quiet exchange or cobalt gown turn to Grok Imagine 1.5 on SeaImagine with its starting image and complete prompt. Explore glass and light, timing between two speakers, or the way fabric follows a turn.

[Glass and light](#case-sea-glass-bottle) · [A clockmaker dialogue](#case-clockwork-dialogue) · [A couture turn](#case-cobalt-orbit)

[![SeaImagine · Grok Imagine 1.5](assets/seaimagine-interface.jpg)](https://seaimagine.com/model/grok-imagine-1-5/)

Actual interface: the glass-bottle prompt is entered at 720p · 5s · 16:9. The start image has not been uploaded; no video has been generated.

**[Create this shot with SeaImagine](https://seaimagine.com/model/grok-imagine-1-5/)**

<a id="learn-from-official-and-community-examples"></a>

<a id="writing-guide"></a>

<a id="a-compact-reusable-template"></a>

<a id="api-quick-start"></a>

<a id="can-grok-imagine-prompts-be-written-in-languages-other-than-english"></a>

<a id="contributing"></a>

<a id="does-grok-imagine-video-15-support-1080p"></a>

<a id="frequently-asked-questions"></a>

<a id="grok-imagine-video-15-capabilities"></a>

<a id="how-do-i-keep-a-character-consistent"></a>

<a id="how-long-can-a-grok-imagine-15-video-be"></a>

<a id="license"></a>

<a id="official-resources"></a>

<a id="quality-checklist"></a>

<a id="should-i-include-a-negative-prompt"></a>

<a id="the-prompt-formula"></a>

<a id="what-is-the-best-grok-imagine-15-prompt-structure"></a>

## Reference material

[Writing reference](docs/guides/en-US.md) · [Settings and operation reference](docs/workflows/en-US.md) · [SeaImagine](https://seaimagine.com/model/grok-imagine-1-5/)

[Sources](docs/COMMUNITY.md) · [X / YouTube](docs/SOCIAL_INSPIRATION.md)

<a id="multilingual-prompts"></a>

## Collection and attribution

65 distinct English prompts: 35 inherited and 30 original. Original prompts are newly written and not generation-tested. Translations are not additional scenarios.

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
