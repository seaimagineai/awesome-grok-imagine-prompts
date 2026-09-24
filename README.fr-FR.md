# Bibliothèque de prompts Grok Imagine 1.5 — Français

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 38 prompts, dont 8 exemples illustrés disponibles en 15 langues. Parcourez les catégories et copiez les prompts complets.

![Grok Imagine 1.5 — Carnet de prompts ouvert : une chaussure, un tramway et une baleine en papier dans un même décor](assets/seaimagine-grok-hero.webp)

Adaptée de [Flaq AI](https://github.com/flaqai/awesome-grok-imagine) et maintenue par SeaImagine. Licence [MIT](LICENSE). Ce projet est indépendant de xAI. Les images conceptuelles ne sont pas des résultats vérifiés de Grok.

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## Index des catégories

| Objectif | Exemples illustrés |
| --- | --- |
| Publicités de produits | [Bouteille en verre marin : comparer des mouvements maîtrisés](#case-sea-glass-bottle) · [Halo d’agrumes : film de parfum haut de gamme](#case-citrus-halo) |
| Action cinématographique | [Itinéraire bleu : suivi d’un livreur dans un marché pluvieux](#case-blue-route) |
| Récits fantastiques | [Le pain au miel : histoire de boulangerie miniature](#case-honey-loaf) |
| Dialogues de personnages | [Retrouvailles au port : un seul moment d’émotion](#case-harbor-reunion) |
| Vidéos du quotidien | [Première gorgée : avis authentique d’une créatrice au café](#case-first-sip) |
| Films de voyage | [La ligne du sel à l’aube : documentaire de voyage](#case-salt-line) |
| Compositions animées | [Carte postale côtière : animez une image préparée](#case-coastal-postcard) |

[Exemples illustrés](#featured-prompts) · [Travaux officiels et communautaires](#learn-from-official-and-community-examples) · [Référence des réglages et des commandes](#writing-guide)

<a id="visual-index"></a>

### Aperçu des exemples illustrés

8 exemples avec prompts complets et images de départ. Les images illustrent des concepts ; elles ne constituent pas des résultats vidéo vérifiés.

Les cinq exemples marqués « Source : Flaq AI » conservent leur durée et leur résolution d’origine ; les trois autres utilisent les options actuelles de SeaImagine. Pour utiliser un exemple source sur SeaImagine, choisissez 5/10/15 secondes et 480p/720p, puis réécrivez ses actions minutées.

| | |
| --- | --- |
| <a href="#case-sea-glass-bottle"><img src="assets/seaimagine-sea-glass-bottle.webp" height="180" alt="Bouteille en verre marin : comparer des mouvements maîtrisés"></a><br>[1. Bouteille en verre marin : comparer des mouvements maîtrisés](#case-sea-glass-bottle)<br>5s · 16:9 · 720p | <a href="#case-blue-route"><img src="assets/rainy-market-courier-video.webp" height="180" alt="Itinéraire bleu : suivi d’un livreur dans un marché pluvieux"></a><br>[2. Itinéraire bleu : suivi d’un livreur dans un marché pluvieux](#case-blue-route)<br>10s · 16:9 · 1080p |
| <a href="#case-honey-loaf"><img src="assets/pear-bakery-miniature-video.webp" height="180" alt="Le pain au miel : histoire de boulangerie miniature"></a><br>[3. Le pain au miel : histoire de boulangerie miniature](#case-honey-loaf)<br>9s · 16:9 · 1080p | <a href="#case-harbor-reunion"><img src="assets/seaimagine-harbor-reunion.webp" height="180" alt="Retrouvailles au port : un seul moment d’émotion"></a><br>[4. Retrouvailles au port : un seul moment d’émotion](#case-harbor-reunion)<br>10s · 16:9 · 720p |
| <a href="#case-first-sip"><img src="assets/cozy-cafe-ugc-video.webp" height="180" alt="Première gorgée : avis authentique d’une créatrice au café"></a><br>[5. Première gorgée : avis authentique d’une créatrice au café](#case-first-sip)<br>10s · 9:16 · 1080p | <a href="#case-salt-line"><img src="assets/coastal-salt-train-documentary.webp" height="180" alt="La ligne du sel à l’aube : documentaire de voyage"></a><br>[6. La ligne du sel à l’aube : documentaire de voyage](#case-salt-line)<br>12s · 16:9 · 1080p |
| <a href="#case-coastal-postcard"><img src="assets/seaimagine-coastal-postcard.webp" height="180" alt="Carte postale côtière : animez une image préparée"></a><br>[7. Carte postale côtière : animez une image préparée](#case-coastal-postcard)<br>5s · 9:16 · 720p | <a href="#case-citrus-halo"><img src="assets/citrus-fragrance-product-video.webp" height="180" alt="Halo d’agrumes : film de parfum haut de gamme"></a><br>[8. Halo d’agrumes : film de parfum haut de gamme](#case-citrus-halo)<br>8s · 16:9 · 1080p |

**Parcourir d’autres prompts (en anglais) · 30**

| Catégorie | Index des exemples |
| --- | --- |
| [Publicités et produits · 6](prompts/01-ads-and-products.md) | [1. Dew Drop Laboratory — skincare serum macro](prompts/01-ads-and-products.md#1-dew-drop-laboratory--skincare-serum-macro) · [2. Cold Brew Eclipse — coffee launch film](prompts/01-ads-and-products.md#2-cold-brew-eclipse--coffee-launch-film) · [3. Street-to-Studio — performance shoe demonstration](prompts/01-ads-and-products.md#3-street-to-studio--performance-shoe-demonstration) · [4. Doorstep Dinner — food delivery social ad](prompts/01-ads-and-products.md#4-doorstep-dinner--food-delivery-social-ad) · [5. Silver Current — artisan jewelry reveal](prompts/01-ads-and-products.md#5-silver-current--artisan-jewelry-reveal) · [6. One Tap Away — clean mobile app promo](prompts/01-ads-and-products.md#6-one-tap-away--clean-mobile-app-promo) |
| [Récits cinématographiques · 6](prompts/02-cinematic-storytelling.md) | [1. Last Tram Note — restrained urban romance](prompts/02-cinematic-storytelling.md#1-last-tram-note--restrained-urban-romance) · [2. Room 407 — quiet hotel mystery](prompts/02-cinematic-storytelling.md#2-room-407--quiet-hotel-mystery) · [3. Glasshouse Pursuit — grounded parkour action](prompts/02-cinematic-storytelling.md#3-glasshouse-pursuit--grounded-parkour-action) · [4. Tidekeeper — coastal fantasy ritual](prompts/02-cinematic-storytelling.md#4-tidekeeper--coastal-fantasy-ritual) · [5. Paper Moon Delivery — hand-drawn animation](prompts/02-cinematic-storytelling.md#5-paper-moon-delivery--hand-drawn-animation) · [6. Europa Signal — hard-science discovery](prompts/02-cinematic-storytelling.md#6-europa-signal--hard-science-discovery) |
| [Réseaux sociaux et quotidien · 6](prompts/03-social-ugc.md) | [1. Shelf Test — honest skincare mini-review](prompts/03-social-ugc.md#1-shelf-test--honest-skincare-mini-review) · [2. Twelve-Minute Noodles — one-pan recipe reel](prompts/03-social-ugc.md#2-twelve-minute-noodles--one-pan-recipe-reel) · [3. First Set — realistic morning fitness log](prompts/03-social-ugc.md#3-first-set--realistic-morning-fitness-log) · [4. One Question, One Corner — street interview](prompts/03-social-ugc.md#4-one-question-one-corner--street-interview) · [5. Clay Cup Morning — tactile pottery ASMR](prompts/03-social-ugc.md#5-clay-cup-morning--tactile-pottery-asmr) · [6. Umbrella Reset — seamless pet comedy loop](prompts/03-social-ugc.md#6-umbrella-reset--seamless-pet-comedy-loop) |
| [Personnages et références · 6](prompts/04-characters-and-references.md) | [1. Harbor Cartographer — consistent character introduction](prompts/04-characters-and-references.md#1-harbor-cartographer--consistent-character-introduction) · [2. Linen Set — virtual try-on walk test](prompts/04-characters-and-references.md#2-linen-set--virtual-try-on-walk-test) · [3. Counter Demo — product placement without redesign](prompts/04-characters-and-references.md#3-counter-demo--product-placement-without-redesign) · [4. Two Voices, One Repair — synchronized dialogue scene](prompts/04-characters-and-references.md#4-two-voices-one-repair--synchronized-dialogue-scene) · [5. Sunday Table — consistent three-person ensemble](prompts/04-characters-and-references.md#5-sunday-table--consistent-three-person-ensemble) · [6. Parcel Finch — reusable brand mascot motion](prompts/04-characters-and-references.md#6-parcel-finch--reusable-brand-mascot-motion) |
| [Montage et prolongation · 6](prompts/05-editing-and-extension.md) | [1. Blue Hour Conversion — day-to-night architectural edit](prompts/05-editing-and-extension.md#1-blue-hour-conversion--day-to-night-architectural-edit) · [2. First Snow — controlled weather replacement](prompts/05-editing-and-extension.md#2-first-snow--controlled-weather-replacement) · [3. Clean Plate — remove one distracting object](prompts/05-editing-and-extension.md#3-clean-plate--remove-one-distracting-object) · [4. Practical Miniature — change rendering style, keep motion](prompts/05-editing-and-extension.md#4-practical-miniature--change-rendering-style-keep-motion) · [5. Beyond the Gate — continue a travel shot](prompts/05-editing-and-extension.md#5-beyond-the-gate--continue-a-travel-shot) · [6. Turntable Loop — repair a product animation into a seamless cycle](prompts/05-editing-and-extension.md#6-turntable-loop--repair-a-product-animation-into-a-seamless-cycle) |

<a id="featured-prompts"></a>

## Des prompts illustrés à copier et à adapter

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. Bouteille en verre marin : comparer des mouvements maîtrisés

**Réglages image vers vidéo:** 5s · 16:9 · 720p · [Image de départ : ouvrir et enregistrer](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/fr-FR/sea-glass-bottle.txt)

```text
Conservez l’unique bouteille en verre marin dépoli sur la pierre claire, son bouchon cylindrique, sa face avant vierge sans inscription, le niveau d’eau, l’horizon et l’éclairage latéral doux. La bouteille ne bouge jamais.
Pendant cinq secondes, effectuez un lent déplacement latéral de la caméra vers la droite, sur une distance ne dépassant pas la largeur d’une bouteille.
Une petite goutte d’eau descend sur la face avant et s’arrête à la base. À l’arrière-plan, les vagues se déplacent doucement dans le flou. Gardez des reflets cohérents avec la caméra et la source lumineuse.
Son : uniquement le ressac lointain ; ni musique, voix, choc de verre ou éclaboussures exagérées.
Ni coupe ni zoom. Préservez la silhouette de la bouteille, l’alignement du bouchon, la texture du verre et le nombre d’objets.
Évitez les logos générés, les changements du niveau de liquide, les bords déformés, les objets flottants ou les nouveaux accessoires.
Gardez un cadre stable pendant la dernière seconde.
```

[Retour à l’index des catégories](#find-the-right-prompt) · [Aperçu des exemples illustrés](#visual-index)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. Itinéraire bleu : suivi d’un livreur dans un marché pluvieux

**Réglages image vers vidéo:** 10s · 16:9 · 1080p · [Image de départ : ouvrir et enregistrer](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/fr-FR/blue-route.txt)

[Source : Flaq AI](docs/ATTRIBUTION.md)

```text
Préservez le livreur, la moto électrique cobalt, le coffre de livraison, le marché surélevé, les auvents translucides, la passerelle en acier mouillée, l’éclairage et la palette nocturne fournis. Créez un seul travelling bas et continu, ancré dans le réel, avec masse, adhérence, pluie et suspension crédibles.

0–3s : la moto accélère doucement depuis sa position initiale. Le pneu arrière projette un fin éventail d’eau ; la suspension se comprime sur un joint de drainage. La caméra suit à côté et légèrement derrière, à hauteur de roue, à la même vitesse et sans secousses violentes.

3–7s : le livreur s’incline dans une large courbe à gauche. Les auvents plient dans le vent, la vapeur sort des étals et les lumières chaudes du décor s’étirent doucement dans les reflets mouillés. Gardez les deux roues rondes et en contact avec le sol.

7–10s : la moto se redresse et rejoint une partie ouverte plus lumineuse du marché. La caméra recule d’un demi-mètre pour révéler le chemin, puis maintient un cadre final stable.

Son : sifflement réaliste du moteur électrique, projections d’eau, pluie sur les auvents, voix discrètes du marché, un choc de suspension. Ni musique, dialogue, sirènes ou explosions.

Continuité : tenue exacte, casque, géométrie de la moto, coffre, panneaux bleus et disposition du marché. Ni transformation du véhicule, roues déformées, collisions, armes, panneaux lisibles, logos, téléportation de caméra ou accélération impossible.
```

[Retour à l’index des catégories](#find-the-right-prompt) · [Aperçu des exemples illustrés](#visual-index)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. Le pain au miel : histoire de boulangerie miniature

**Réglages image vers vidéo:** 9s · 16:9 · 1080p · [Image de départ : ouvrir et enregistrer](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/fr-FR/honey-loaf.txt)

[Source : Flaq AI](docs/ATTRIBUTION.md)

```text
Conservez la boulangerie en forme de poire, les trois boulangers miniatures, costumes, visages, pain au miel, four, fenêtre, mousse, trèfle, lune, matières tactiles du stop motion et contraste chaud-froid.

0–3s : partez de la composition large fournie, avec un rythme discret de stop motion artisanal. Deux boulangers soulèvent ensemble le pain chaud ; leurs mains restent au contact de la planche en bois. Un petit nuage de farine monte, le feu du four vacille et le troisième boulanger ouvre le guichet de service.

3–7s : les deux font quatre pas prudents et synchronisés vers le guichet. Le pain a un poids crédible et s’abaisse légèrement entre eux. Dehors, une feuille de trèfle libère une goutte de rosée et deux lucioles passent à différentes profondeurs. La caméra décrit un arc doux de cinq degrés vers la droite.

7–9s : ils glissent la planche sur le comptoir, échangent des sourires soulagés et la lueur du four se stabilise. Terminez avec les trois personnages visibles et le pain au centre.

Son : petits pas sur le bois, léger crépitement du four, grincement de planche, discrets insectes nocturnes, une petite clochette au guichet. Ni dialogue, narration, musique ou texte.

Continuité : préservez le nombre de personnages, leurs visages, l’échelle, les couleurs des tenues, la forme de poire, la disposition intérieure et la texture artisanale. Ni boulangers supplémentaires, images 3D brillantes, membres en caoutchouc, accessoires flottants, pain fondant, coupes, logos ou personnages ressemblant à ceux de franchises.
```

[Retour à l’index des catégories](#find-the-right-prompt) · [Aperçu des exemples illustrés](#visual-index)

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. Retrouvailles au port : un seul moment d’émotion

**Réglages image vers vidéo:** 10s · 16:9 · 720p · [Image de départ : ouvrir et enregistrer](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/fr-FR/harbor-reunion.txt)

```text
Conservez les deux adultes, leurs visages, les vêtements bleu marine et crème, le ponton en bois et la douce lumière matinale de l’image fournie. Gardez les deux personnages dans le même plan moyen large.
0–3 secondes : la personne à gauche remarque son ami qui arrive et fait un petit pas. Ses épaules se détendent ; son ami répond par un sourire discret. Gardez les mains visibles et détendues.
3–7 secondes : la personne à gauche dit en français naturel : « Tu es là. » Son ami hoche une fois la tête. La réplique reste sobre, sans pleurs ni expressions faciales exagérées.
7–10 secondes : tous deux regardent le bateau amarré. Maintenez la dernière seconde pour permettre un raccord vers le plan suivant.
Caméra : une seule avancée douce, sans contrechamp ni coupe.
Son : voix proche et intelligible, clapotis du port et mouette lointaine ; ni musique ni sous-titres.
Fixez les deux identités, les vêtements, la géométrie du ponton, la position du bateau et la direction de la lumière matinale.
Évitez les personnes supplémentaires, les gestes théâtraux, les visages lissés, les doigts en trop et les sauts de caméra.
```

[Retour à l’index des catégories](#find-the-right-prompt) · [Aperçu des exemples illustrés](#visual-index)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. Première gorgée : avis authentique d’une créatrice au café

**Réglages image vers vidéo:** 10s · 9:16 · 1080p · [Image de départ : ouvrir et enregistrer](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/fr-FR/first-sip.txt)

[Source : Flaq AI](docs/ATTRIBUTION.md)

```text
Animez la photo de café fournie comme un avis sincère de créatrice filmé caméra à la main. Préservez son visage, son âge, sa texture de peau, ses cheveux, son pull vert mousse, la tasse, la pâtisserie, la fenêtre et la disposition de la table.

0–3s : léger flottement naturel de caméra à la main. Elle finit une gorgée, baisse la tasse en céramique d’environ dix centimètres, expire avec un petit sourire et détourne le regard de la fenêtre vers la caméra. La vapeur monte en volutes et les traînées de pluie se rejoignent lentement sur la vitre derrière elle.

3–8s : elle dit, en français naturel et d’une voix détendue : « Crémeux, pas trop sucré… et on sent vraiment l’avoine. » Gardez un ton spontané, avec une toute petite pause après « sucré ». Synchronisez précisément les lèvres et gardez la tasse stable dans sa main.

8–10s : elle acquiesce légèrement et regarde la pâtisserie tandis que la caméra se stabilise.

Son : voix proche enregistrée au téléphone, ambiance calme de café, buse à vapeur lointaine, pluie douce, contact de la tasse en céramique. La voix reste devant, l’ambiance discrète. Ni musique de fond ni sous-titres.

Continuité : ni embellissement du visage, changement de tenue, doigts supplémentaires, modification de la tasse ou des aliments, apparition de personnes au fond, logos ou gestes exagérés d’influenceuse.
```

[Retour à l’index des catégories](#find-the-right-prompt) · [Aperçu des exemples illustrés](#visual-index)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. La ligne du sel à l’aube : documentaire de voyage

**Réglages image vers vidéo:** 12s · 16:9 · 1080p · [Image de départ : ouvrir et enregistrer](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/fr-FR/salt-line.txt)

[Source : Flaq AI](docs/ATTRIBUTION.md)

```text
Animez la scène côtière de marais salants fournie comme un documentaire de voyage d’observation respectueux. Préservez les deux ouvriers, le train crème et ocre, les bassins, les collines calcaires, bâtiments, mer, direction du lever du soleil et palette de film atténuée.

0–4s : plan large fixe. Les ouvriers inspectent le canal : l’un guide un outil en bois dans la saumure peu profonde, l’autre maintient la séparation. L’eau ondule en réaction à l’outil et à la brise matinale. Le train approche à vitesse mesurée au second plan.

4–9s : la caméra panoramique lentement à droite pour suivre le train. Les roues restent alignées sur les rails ; l’espacement des voitures et le rythme des fenêtres restent constants. Un léger voile de brume marine dérive derrière lui, tandis que le soleil éclaire progressivement les cristaux de sel au premier plan.

9–12s : le train poursuit vers la côte et le panoramique s’arrête en douceur. Un ouvrier se redresse, s’étire naturellement et regarde la voie. Maintenez les deux dernières secondes pour un point de montage.

Son : doux bourdonnement électrique du train, rythme des roues aux joints, brise sur l’eau peu profonde, mouettes lointaines, outil en bois dans la saumure. Ni narration, musique, foule ou klaxon dramatique.

Continuité : travail réaliste, anatomie stable, paysage fixe, train inchangé, reflets et physique de l’eau plausibles. Ni silhouette urbaine moderne, mise en scène touristique, nouveaux bâtiments, logos, panneaux lisibles, couleurs de carte postale saturées ou ciel en accéléré.
```

[Retour à l’index des catégories](#find-the-right-prompt) · [Aperçu des exemples illustrés](#visual-index)

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. Carte postale côtière : animez une image préparée

**Réglages image vers vidéo:** 5s · 9:16 · 720p · [Image de départ : ouvrir et enregistrer](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/fr-FR/coastal-postcard.txt)

```text
Animez cette carte postale côtière à trois cases sans modifier sa disposition ni ses bordures. Conservez exactement tous les objets et les couleurs. Dans la case supérieure, une fine volute de vapeur monte de la tasse.
Dans la case centrale, l’eau du port ondule doucement et le soleil scintille à sa surface.
Dans la case inférieure, seul le coin de papier déjà présent se soulève légèrement puis retombe sous une brise légère.
Gardez chaque mouvement dans sa case. Toutes les cases restent visibles pendant les cinq secondes.
Caméra : fixe, sans zoom, panoramique, coupe ni transition entre les cases.
Son : eau calme et léger froissement de papier ; ni dialogue, musique, légendes ou texte ajouté.
Préservez l’anse de la tasse, le cadre de la fenêtre, les marques de la carte, les dimensions des cases et l’ordre de lecture.
Évitez de fusionner les cases, d’inventer une nouvelle scène, de redessiner les lettres ou de déplacer des objets au-delà des bordures.
Terminez avec le coin de papier au repos et la composition initiale intacte.
```

[Retour à l’index des catégories](#find-the-right-prompt) · [Aperçu des exemples illustrés](#visual-index)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. Halo d’agrumes : film de parfum haut de gamme

**Réglages image vers vidéo:** 8s · 16:9 · 1080p · [Image de départ : ouvrir et enregistrer](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/fr-FR/citrus-halo.txt)

[Source : Flaq AI](docs/ATTRIBUTION.md)

```text
Préservez le design du flacon fourni, les proportions du verre, le bouchon, le socle en calcaire, l’écorce de pamplemousse, le décor ivoire chaud et la lumière latérale dorée. Créez un élégant film de produit de huit secondes.

0–2.5s : commencez par une composition macro presque fixe. La caméra avance très lentement. Les perles de condensation accrochent la lumière ; deux gouttes glissent naturellement sur le verre froid. L’écorce de pamplemousse se soulève du socle comme portée par une brise de studio maîtrisée.

2.5–6s : l’écorce forme une seule spirale gracieuse autour du flacon, sans toucher ni masquer le bouchon. De fines particules de brume d’agrumes traversent le contre-jour. Réfraction et caustiques se déplacent physiquement dans le verre épais ; le flacon reste parfaitement rigide.

6–8s : l’écorce retrouve sa courbe initiale, la caméra s’arrête en douceur et un reflet spéculaire lumineux parcourt une fois le bord du flacon. Terminez sur un plan produit épuré.

Son : uniquement des bruitages de studio proches — léger mouvement du ruban d’écorce, deux gouttes d’eau nettes et délicate résonance de verre. Ni voix, musique ou texte.

Continuité : ne modifiez ni la silhouette du flacon, ni les facettes du bouchon, le niveau du liquide, le socle, la palette ou l’arche du fond. Aucune étiquette, logo, fruit supplémentaire, flacon flottant, géométrie instable, saut de caméra ou explosion artificielle de paillettes.
```

[Retour à l’index des catégories](#find-the-right-prompt) · [Aperçu des exemples illustrés](#visual-index)

<a id="learn-from-official-and-community-examples"></a>

## Apprenez à partir des créations officielles et communautaires

Les publications sources indiquent le créateur et la version du modèle. Ouvrez les originaux pour les visionner ; les conseils ci-dessous décrivent des méthodes, sans prétendre que nous avons reproduit ces vidéos.

### [Séquence officielle 1.5 Preview : Grok / Heavy Pulp](https://x.com/grok/status/2062225080843747351)

[![Séquence officielle 1.5 Preview : Grok / Heavy Pulp](https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg)](https://x.com/grok/status/2062225080843747351)

Apprenez à préparer une bande-annonce en plans courts séparés. Distinguez les images de Preview de celles du modèle 1.5 publié.

### [Court métrage terminé : JSFILMZ](https://x.com/JSFILMZ0412/status/2062480692835938771)

L’auteur évoque un film de 2,5 minutes et les limites du jeu d’acteur généré. Commencez par un échange calme ; construisez les histoires plus longues avec plusieurs plans montés.

### [Préparer l’image avant l’animation : GENEL](https://x.com/genel_ai/status/2061382998873034825)

[![Préparer l’image avant l’animation : GENEL](https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg)](https://x.com/genel_ai/status/2061382998873034825)

Le créateur indique avoir réalisé un collage avec ChatGPT Images 2.0, puis l’avoir animé avec Grok Imagine Video 1.5. Notre exercice de carte postale fixe les bordures et attribue un seul mouvement à chaque case.

### [Comparaison contrôlée : JSFILMZ](https://x.com/JSFILMZ0412/status/2061117682515050669)

Utilisez la même image source et des réglages comparables. Vérifiez la géométrie, le mouvement et le son plutôt que de reprendre un ancien classement. Notre exercice de la bouteille isole ces variables.

<details>
<summary>Observations d’images et limites de vérification</summary>

Le 24 septembre 2026, nous avons examiné des images dans les lecteurs X originaux : pour le clip officiel, vers 3,6 s (casque et armée), 19,8 s (gros plan sur un visage) et 34,6 s (ville côtière en flammes) ; pour GENEL, vers 0,05 s (garde-corps en bord de mer), 4,9 s (passage à niveau) et 12 s (main à contre-jour). Étudiez les changements d’échelle des plans du clip officiel et la cohérence de la lumière côtière entre les plans de GENEL. Notre carte postale à cases fixes est un exercice différent. Il s’agit d’images échantillonnées, pas de tests complets du mouvement ou du son.

</details>

[Sources et notes de visionnage (en anglais)](docs/COMMUNITY.md)

<a id="writing-guide"></a>

<a id="bibliothèque-complète"></a>

<a id="principes-rapides"></a>

<a id="test-multilingue-partagé--latelier-de-lampe-en-céramique"></a>

## Documentation de référence

[Référence de rédaction](docs/guides/fr-FR.md) · [Référence des réglages et des commandes](docs/workflows/fr-FR.md) · [SeaImagine](https://seaimagine.com/fr/model/grok-imagine-1-5/)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

<a id="multilingual-prompts"></a>

## Collection et attribution

38 recettes distinctes en anglais au total : 35 recettes reprises et ces 3 nouveaux exercices. Les traductions n’ajoutent pas de nouveaux scénarios.

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/fr/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
