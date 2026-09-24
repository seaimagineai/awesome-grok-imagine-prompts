# Grok Imagine 1.5 Prompts for Video Editing, Extension & Transformations

[← Characters & references](04-characters-and-references.md) · [Main collection](../README.md)

> **Model / provider note:** Reference, editing and extension controls are not assumed to be available on SeaImagine. Official editing and extension examples use `grok-imagine-video`, not `grok-imagine-video-1.5`. See [workflow boundaries](../docs/OFFICIAL.md).

Editing prompts should read like change orders: name the exact modification first, then repeat everything that must remain unchanged. Current xAI documentation says edited video keeps the source duration and aspect ratio, with output capped at 720p; check the docs before production.

## 1. Blue Hour Conversion — day-to-night architectural edit

**Mode:** video edit · **Output:** source duration and ratio · up to 720p

```text
Change only the time of day and related illumination. Transform the existing late-afternoon
exterior into realistic blue hour approximately twenty minutes after sunset.

Preserve every building, window, door, tree, path, parked bicycle, person, action, camera move,
timing, framing, lens behavior, and surface material. Gradually cool the sky to deep cobalt while
retaining a faint warm horizon. Turn on only the practical lights already visible in windows and
under eaves; each light casts restrained, physically consistent warmth on nearby surfaces. Make
existing street lamps illuminate in sequence as the camera passes. Adjust shadows, reflections,
exposure, and white balance consistently across every frame. People and bicycle continue their
original movement without any speed or identity change.

Audio: preserve the source audio exactly. Do not add crickets, music, or electrical switch sounds.

Do not add or remove architecture, windows, signage, vehicles, people, clouds, or lamps. No
flickering exposure, new neon, fantasy glow, star time-lapse, wet ground, readable text mutation,
camera stabilization change, or altered duration.
```

## 2. First Snow — controlled weather replacement

**Mode:** video edit · **Output:** source duration and ratio · up to 720p

```text
Change only weather, seasonal surface details, and the light they physically affect. Convert the
existing quiet autumn courtyard into the first gentle snowfall of early winter.

Preserve all people, faces, clothes, actions, timing, camera path, buildings, benches, trees,
ground geometry, and composition. Replace falling leaves with sparse snowflakes traveling in the
same wind direction at varied depths. Add a thin, uneven dusting of fresh snow only on upward-facing
surfaces; paths remain mostly visible and slightly damp. Bare branches keep their exact structure.
Cool the daylight subtly and soften contrast while retaining believable skin color. Footsteps and
wheel contact respond to damp ground without changing movement.

Audio: keep original voices and foreground sounds. Replace leaf rustle with soft snowfall ambience
and dampened courtyard room tone; do not add music.

No blizzard, deep snow, wardrobe change, breath clouds unless temperature supports them, frozen
fountain, new footprints ahead of people, extra branches, identity drift, camera change, or text.
```

## 3. Clean Plate — remove one distracting object

**Mode:** video edit · **Output:** source duration and ratio · up to 720p

```text
Remove only the bright red plastic condiment bottle at the back-left edge of the restaurant table.
Reconstruct the wooden tabletop, wall edge, and soft shadow behind it using surrounding texture,
perspective, grain, and lighting. The repaired area must remain stable as the camera moves and as
foreground hands briefly pass in front of it.

Keep every other plate, glass, utensil, napkin, food item, person, face, hand action, reflection,
camera move, focus pull, exposure, color grade, audio event, and clip timing exactly unchanged.
Do not shift objects to fill the space. Preserve the original shallow depth of field and motion
blur in the reconstructed area.

Audio: preserve the complete source track without modification.

No table redesign, cloned wood pattern, pulsing patch, missing plate, changed food, hand distortion,
new object, crop, zoom, stabilization, relighting, skin retouch, logo removal elsewhere, or duration
change. The requested bottle is the only element that should disappear.
```

## 4. Practical Miniature — change rendering style, keep motion

**Mode:** video edit · **Output:** source duration and ratio · up to 720p

```text
Restyle the existing original 3D fantasy village clip as a physically built tabletop miniature
photographed with a real macro lens. Preserve the village layout, camera path, character positions,
actions, timing, weather, color relationships, and narrative beat exactly.

Translate materials consistently: buildings become carved basswood and painted card; roof tiles
become individually cut paper; trees become wire-and-flock models; water becomes layered clear
resin with subtle surface ripple; characters become articulated felt-and-clay puppets. Add gentle
handmade imperfections, shallow macro depth of field appropriate to the camera distance, soft studio
light spill, and plausible miniature-scale shadows. Motion retains the source choreography with a
subtle stop-motion cadence, but no frames or actions are removed.

Audio: preserve dialogue and sound timing. Replace only material Foley where needed — wood, paper,
felt, and resin — at natural volume. Preserve the original music if present.

No new buildings, characters, props, logos, text, camera angles, color-theme change, glossy toy
plastic, franchise imitation, object morphing, or altered duration.
```

## 5. Beyond the Gate — continue a travel shot

**Mode:** video extension · **Output:** continue 8s from the source final frame

```text
Continue immediately from the existing final frame with no cut. Preserve the hiker's identity,
red windbreaker, backpack straps, walking pace, direction of travel, body position, trail, wooden
gate, mountain layers, morning light, cloud direction, camera height, lens, grade, and source audio
character.

The hiker finishes pushing the gate open, walks through, then closes it gently behind them. Camera
continues the same slow following movement at the same distance. As the trail curves right, reveal
a narrow alpine lake already implied by the valley geography; it appears gradually through the
opening, not by a sudden wide reveal. Wind moves grass, jacket, and lake ripples in the same
direction. The hiker pauses at the curve, shifts backpack weight once, and looks toward the lake.
Hold the final second on a stable over-the-shoulder composition for another possible extension.

Audio: continue existing footsteps and wind seamlessly; add gate hinge, latch contact, distant
water birds, and subtle fabric movement. No music swell or narration.

No wardrobe change, new gear, identity drift, trail teleport, gate redesign, impossible lake,
weather jump, new person, drone move, camera cut, time-lapse, text, or logo.
```

## 6. Turntable Loop — repair a product animation into a seamless cycle

**Mode:** video edit · **Output:** source duration and ratio · up to 720p

```text
Keep the original unbranded desk speaker, turntable, background, surface, lighting, camera position,
materials, color, and audio style. Modify only the object's rotational timing and the final-to-first
transition so the clip becomes a seamless loop.

The speaker completes exactly one constant-speed 360-degree rotation around its vertical center.
It never translates, tilts, scales, flexes, or changes design. Highlights and shadow move smoothly
and physically with the rotation, returning to their exact opening state on the last frame. Keep
all buttons, grille holes, feet, seams, and reflections coherent across the hidden side. Remove any
speed ramp, hesitation, reverse motion, exposure pulse, or final-frame freeze from the source.
Background and camera stay perfectly locked. Match the last frame to the first in object angle,
light, shadow, focus, and grain.

Audio: create a continuous quiet room tone and low turntable motor that crosses the loop point
without a click, volume jump, or fade. No music or voice.

No label, logo, geometry invention, mirrored controls, floating object, camera orbit, background
movement, shadow discontinuity, new reflection, or duration change.
```

## Edit and extension checklist

- Start with “Change only…” or “Continue directly…” so scope is unambiguous.
- Repeat the source invariants: identity, geometry, timing, camera, grade, and audio.
- For removal, describe what should exist behind the removed object.
- For style transfer, map old materials to new materials one by one.
- For extension, preserve direction of travel, wind, gaze, lighting, and camera velocity.
- End extensions on a stable frame if the sequence may continue again.
