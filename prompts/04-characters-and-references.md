# Grok Imagine 1.5 Prompts for Characters & Reference-to-Video

[← Social & UGC](03-social-ugc.md) · [Main collection](../README.md) · [Next: Editing & extension →](05-editing-and-extension.md)

> **Model / provider note:** Reference, editing and extension controls are not assumed to be available on SeaImagine. Official editing and extension examples use `grok-imagine-video`, not `grok-imagine-video-1.5`. See [workflow boundaries](../docs/OFFICIAL.md).

Reference-to-video is best when each image has one job. Use clear, compatible references and explicitly map them in the prompt. Current xAI documentation allows up to seven reference images and up to three preset voices, with output capped at 720p.

## 1. Harbor Cartographer — consistent character introduction

**References:** `<IMAGE_0>` face, `<IMAGE_1>` full-body wardrobe, `<IMAGE_2>` map room · **Output:** 10s · 16:9 · 720p

```text
Create the same original adult cartographer using facial identity, skin, hair, and age from
<IMAGE_0>; body proportions, weathered teal coat, boots, and satchel from <IMAGE_1>; and the round
harbor map room, windows, chart table, and dawn lighting from <IMAGE_2>. Do not combine clothing
or architecture from the identity portrait.

Start in a medium-wide view. The cartographer crosses from the window to the chart table in four
natural steps, sets the existing satchel on a chair, and unrolls one paper chart with both hands.
Camera makes a slow half-circle to reveal their face in three-quarter profile. Sea breeze through
the open window moves hair, coat hem, and only the loose chart corners. They notice one marked
route, trace it with a finger, then look toward the harbor with a calm decision.

Audio: gulls, distant rigging, boot steps, leather satchel, paper roll, quiet room. No dialogue,
music, narration, or text.

Lock: exact face, age, hairstyle, body, coat design and color, satchel, room geometry, chart count,
and dawn light. No identity drift, wardrobe redesign, extra jewelry, extra fingers, readable map
labels, logos, crowd, camera cut, or fantasy glow.
```

## 2. Linen Set — virtual try-on walk test

**References:** `<IMAGE_0>` person, `<IMAGE_1>` front garment, `<IMAGE_2>` back garment, `<IMAGE_3>` shoes, `<IMAGE_4>` studio · **Output:** 10s · 9:16 · 720p

```text
Use the fictional adult model's identity, body, skin, hair, and height from <IMAGE_0>. Dress them
in the exact linen two-piece shown from front in <IMAGE_1> and back in <IMAGE_2>, plus the exact
unbranded shoes from <IMAGE_3>. Use only the neutral plaster studio and light direction from
<IMAGE_4>. Garment fit should respect the model's real body rather than changing their shape.

The model takes three relaxed steps toward camera, stops, turns once to show the side and back,
then returns to a three-quarter front pose. Camera stays at chest height and slowly pulls back to
keep the full body and both shoes visible. Linen folds, hem, and sleeves respond to walking and
settle with believable weight; closures and seams remain in place.

Audio: shoes on plaster, light fabric movement, studio room tone. No music or speech.

Lock: identity, body proportions, garment cut, seams, buttons, color, texture, back construction,
shoe shape, and studio. No slimming, height change, face retouch, fabric morph, missing shoe,
new accessory, logo, extreme runway pose, mirror, or camera cut.
```

## 3. Counter Demo — product placement without redesign

**References:** `<IMAGE_0>` presenter, `<IMAGE_1>` appliance front, `<IMAGE_2>` appliance sides, `<IMAGE_3>` kitchen · **Output:** 12s · 16:9 · 720p

```text
Use the fictional adult presenter from <IMAGE_0>. Place the exact original countertop appliance
from <IMAGE_1> and <IMAGE_2> in the modern kitchen from <IMAGE_3>. Preserve the product's front
panel, side vents, dimensions, color, controls, and unbranded appearance. The presenter wears the
same simple outfit as <IMAGE_0>.

0–4s: medium-wide shot. Presenter stands beside, not behind, the appliance and says, “The useful
part is how little counter space it takes.” They gesture once without covering the front panel.
4–8s: camera moves to a gentle three-quarter angle as the presenter opens the product's existing
lid and places one prepared item inside using both hands. 8–12s: they close the lid, press the
single supplied control once, and say, “Set it, then get on with breakfast.” Hold the product.

Audio: clear presenter voice, lid hinge, button click, quiet kitchen ambience. No music or beep
unless visible in the reference design. No subtitles.

Lock: presenter identity, appliance geometry and scale, control count, hinge direction, kitchen,
and item. No invented display text, product stretching, hand passing through lid, new logo,
steam before operation, extra appliance, or jump cut.
```

## 4. Two Voices, One Repair — synchronized dialogue scene

**References:** `<IMAGE_0>` technician A, `<IMAGE_1>` technician B, `<IMAGE_2>` workshop, `<AUDIO_0>` voice A, `<AUDIO_1>` voice B · **Output:** 12s · 16:9 · 720p

```text
Use technician A's identity and navy coveralls from <IMAGE_0>, speaking with <AUDIO_0>. Use
technician B's identity and rust-colored coveralls from <IMAGE_1>, speaking with <AUDIO_1>. Place
them at the workbench from <IMAGE_2>. Preserve the small radio, open tool roll, lamp, and window.

Single two-shot with a slow push-in. A holds the radio chassis steady while B fits one existing
connector. A asks, “Did the signal hold this time?” B watches the meter, pauses for one beat, then
answers, “Long enough to hear the weather station.” A smiles slightly: “Then we try the roof.”
B closes the tool roll and nods. Maintain correct eye lines, alternating mouth movement, and hands
in contact with the same objects. No overlapping dialogue.

Audio: use the assigned voices, workshop room tone, connector click, faint radio static, canvas
tool roll. Dialogue is foreground; no music or subtitles.

Lock: both identities and voices, coverall colors, height relationship, radio, tools, workshop,
speaker order, and dialogue wording. No voice swap, face blend, duplicated tools, extra hands,
lip movement on the silent person, readable brands, or cut.
```

## 5. Sunday Table — consistent three-person ensemble

**References:** `<IMAGE_0>` person A, `<IMAGE_1>` person B, `<IMAGE_2>` person C, `<IMAGE_3>` dining room, `<IMAGE_4>` cake · **Output:** 10s · 16:9 · 720p

```text
Create three fictional adults with separate, unchanged identities: person A from <IMAGE_0>, person
B from <IMAGE_1>, and person C from <IMAGE_2>. Use the dining room from <IMAGE_3> and the exact
homemade cake from <IMAGE_4>. Seat A left, B center, C right. Keep each reference person's own
hair, age, skin, and clothing; do not average or swap features.

Start on a medium-wide table view. B carries the cake with both hands, sets it at center, and sits.
A lights one candle while C shields the flame from a small open-window breeze. They exchange a
brief look, then all three lean toward the cake and laugh at the candle relighting after a failed
blow. Camera remains at table height with a tiny natural push-in. Hands never overlap impossibly.

Audio: plate contact, match strike, breeze, quiet room, one shared natural laugh. No song,
dialogue, music, or captions.

Lock: three distinct identities, seat positions, clothes, cake design, one candle, table setting,
room, and daylight. No face blending, fourth person, duplicated cake, age change, hand fusion,
floating flame, brand, text, or cut.
```

## 6. Parcel Finch — reusable brand mascot motion

**References:** `<IMAGE_0>` mascot front, `<IMAGE_1>` mascot side, `<IMAGE_2>` parcel prop, `<IMAGE_3>` color board · **Output:** 7s · 1:1 · 720p

```text
Create the exact original parcel-finch mascot from front view <IMAGE_0> and side construction
<IMAGE_1>. Use the exact small parcel from <IMAGE_2> and only the palette and flat-paper texture
from <IMAGE_3>. Plain warm off-white set, soft shadow, centered square composition. Preserve the
mascot as a tactile layered-paper puppet, not a realistic bird or glossy 3D character.

The mascot enters from the left in four small hops, parcel held securely under one wing. Layered
paper feathers flex slightly on landing. It places the parcel at center, taps the top twice with
its beak, then looks directly at camera and gives one quick wing salute. Camera remains locked.
End with the character and parcel fully visible and motionless.

Audio: four paper foot taps, light parcel contact, two cardboard beak taps, short friendly
two-note whistle. No speech, music bed, or text.

Lock: silhouette, eye size, beak, wing layers, leg count, colors, paper texture, parcel proportions,
and scale. No logo, label, extra wings, realistic feathers, color drift, parcel opening, props,
background scene, watermark, or looped duplicate character.
```

## Reference planning checklist

| Reference | Best content | Avoid |
| --- | --- | --- |
| Identity | neutral, well-lit face, natural expression | filters, occlusion, extreme angle |
| Body / wardrobe | full body, front and back when needed | conflicting garments or proportions |
| Product | front plus side/three-quarter construction | multiple revisions in one request |
| Location | clean wide view with usable layout | crowds and unreadable visual clutter |
| Voice | one clearly assigned voice per speaker | ambiguous speaker order |

Do not spend all seven image slots by default. Fewer, clearer references usually produce a more coherent brief than many redundant views.
