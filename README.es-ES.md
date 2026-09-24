# Biblioteca de prompts de Grok Imagine 1.5 — Español

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 38 prompts, incluidos 8 ejemplos ilustrados disponibles en 15 idiomas. Explora por categoría y copia los prompts completos.

![Grok Imagine 1.5 — Cuaderno de prompts abierto: una zapatilla, un tranvía y una ballena de papel en un mismo escenario](assets/seaimagine-grok-hero.webp)

Adaptada de [Flaq AI](https://github.com/flaqai/awesome-grok-imagine) y mantenida por SeaImagine. Licencia [MIT](LICENSE). No es un proyecto oficial de xAI. Las imágenes conceptuales no son resultados verificados de Grok.

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## Índice de categorías

| Objetivo | Ejemplos ilustrados |
| --- | --- |
| Anuncios de productos | [Botella de vidrio marino: compara movimientos controlados](#case-sea-glass-bottle) · [Halo cítrico: vídeo de una fragancia de alta gama](#case-citrus-halo) |
| Acción cinematográfica | [Ruta azul: seguimiento de un repartidor en un mercado lluvioso](#case-blue-route) |
| Historias fantásticas | [El pan de miel: historia de una panadería en miniatura](#case-honey-loaf) |
| Diálogos de personajes | [Reencuentro en el puerto: un solo momento emotivo](#case-harbor-reunion) |
| Vídeos de estilo de vida | [Primer sorbo: reseña auténtica de una creadora en una cafetería](#case-first-sip) |
| Películas de viajes | [La línea de la sal al amanecer: documental de viajes](#case-salt-line) |
| Composiciones animadas | [Postal de la costa: anima una imagen planificada](#case-coastal-postcard) |

[Ejemplos ilustrados](#featured-prompts) · [Trabajos oficiales y de la comunidad](#learn-from-official-and-community-examples) · [Referencia de ajustes y uso](#writing-guide)

<a id="visual-index"></a>

### Vista rápida de los ejemplos ilustrados

8 ejemplos con prompts completos e imágenes del fotograma inicial. Las imágenes ilustran conceptos; no son resultados de vídeo verificados.

Los cinco casos identificados como «Fuente: Flaq AI» conservan su duración y resolución originales; los otros tres usan las opciones actuales de SeaImagine. Para usar un caso de la fuente en SeaImagine, elige 5/10/15 segundos y 480p/720p y reescribe sus acciones cronometradas.

| | |
| --- | --- |
| <a href="#case-sea-glass-bottle"><img src="assets/seaimagine-sea-glass-bottle.webp" height="180" alt="Botella de vidrio marino: compara movimientos controlados"></a><br>[1. Botella de vidrio marino: compara movimientos controlados](#case-sea-glass-bottle)<br>5s · 16:9 · 720p | <a href="#case-blue-route"><img src="assets/rainy-market-courier-video.webp" height="180" alt="Ruta azul: seguimiento de un repartidor en un mercado lluvioso"></a><br>[2. Ruta azul: seguimiento de un repartidor en un mercado lluvioso](#case-blue-route)<br>10s · 16:9 · 1080p |
| <a href="#case-honey-loaf"><img src="assets/pear-bakery-miniature-video.webp" height="180" alt="El pan de miel: historia de una panadería en miniatura"></a><br>[3. El pan de miel: historia de una panadería en miniatura](#case-honey-loaf)<br>9s · 16:9 · 1080p | <a href="#case-harbor-reunion"><img src="assets/seaimagine-harbor-reunion.webp" height="180" alt="Reencuentro en el puerto: un solo momento emotivo"></a><br>[4. Reencuentro en el puerto: un solo momento emotivo](#case-harbor-reunion)<br>10s · 16:9 · 720p |
| <a href="#case-first-sip"><img src="assets/cozy-cafe-ugc-video.webp" height="180" alt="Primer sorbo: reseña auténtica de una creadora en una cafetería"></a><br>[5. Primer sorbo: reseña auténtica de una creadora en una cafetería](#case-first-sip)<br>10s · 9:16 · 1080p | <a href="#case-salt-line"><img src="assets/coastal-salt-train-documentary.webp" height="180" alt="La línea de la sal al amanecer: documental de viajes"></a><br>[6. La línea de la sal al amanecer: documental de viajes](#case-salt-line)<br>12s · 16:9 · 1080p |
| <a href="#case-coastal-postcard"><img src="assets/seaimagine-coastal-postcard.webp" height="180" alt="Postal de la costa: anima una imagen planificada"></a><br>[7. Postal de la costa: anima una imagen planificada](#case-coastal-postcard)<br>5s · 9:16 · 720p | <a href="#case-citrus-halo"><img src="assets/citrus-fragrance-product-video.webp" height="180" alt="Halo cítrico: vídeo de una fragancia de alta gama"></a><br>[8. Halo cítrico: vídeo de una fragancia de alta gama](#case-citrus-halo)<br>8s · 16:9 · 1080p |

**Explora más prompts (en inglés) · 30**

| Categoría | Índice de ejemplos |
| --- | --- |
| [Anuncios y productos · 6](prompts/01-ads-and-products.md) | [1. Dew Drop Laboratory — skincare serum macro](prompts/01-ads-and-products.md#1-dew-drop-laboratory--skincare-serum-macro) · [2. Cold Brew Eclipse — coffee launch film](prompts/01-ads-and-products.md#2-cold-brew-eclipse--coffee-launch-film) · [3. Street-to-Studio — performance shoe demonstration](prompts/01-ads-and-products.md#3-street-to-studio--performance-shoe-demonstration) · [4. Doorstep Dinner — food delivery social ad](prompts/01-ads-and-products.md#4-doorstep-dinner--food-delivery-social-ad) · [5. Silver Current — artisan jewelry reveal](prompts/01-ads-and-products.md#5-silver-current--artisan-jewelry-reveal) · [6. One Tap Away — clean mobile app promo](prompts/01-ads-and-products.md#6-one-tap-away--clean-mobile-app-promo) |
| [Historias cinematográficas · 6](prompts/02-cinematic-storytelling.md) | [1. Last Tram Note — restrained urban romance](prompts/02-cinematic-storytelling.md#1-last-tram-note--restrained-urban-romance) · [2. Room 407 — quiet hotel mystery](prompts/02-cinematic-storytelling.md#2-room-407--quiet-hotel-mystery) · [3. Glasshouse Pursuit — grounded parkour action](prompts/02-cinematic-storytelling.md#3-glasshouse-pursuit--grounded-parkour-action) · [4. Tidekeeper — coastal fantasy ritual](prompts/02-cinematic-storytelling.md#4-tidekeeper--coastal-fantasy-ritual) · [5. Paper Moon Delivery — hand-drawn animation](prompts/02-cinematic-storytelling.md#5-paper-moon-delivery--hand-drawn-animation) · [6. Europa Signal — hard-science discovery](prompts/02-cinematic-storytelling.md#6-europa-signal--hard-science-discovery) |
| [Redes sociales y estilo de vida · 6](prompts/03-social-ugc.md) | [1. Shelf Test — honest skincare mini-review](prompts/03-social-ugc.md#1-shelf-test--honest-skincare-mini-review) · [2. Twelve-Minute Noodles — one-pan recipe reel](prompts/03-social-ugc.md#2-twelve-minute-noodles--one-pan-recipe-reel) · [3. First Set — realistic morning fitness log](prompts/03-social-ugc.md#3-first-set--realistic-morning-fitness-log) · [4. One Question, One Corner — street interview](prompts/03-social-ugc.md#4-one-question-one-corner--street-interview) · [5. Clay Cup Morning — tactile pottery ASMR](prompts/03-social-ugc.md#5-clay-cup-morning--tactile-pottery-asmr) · [6. Umbrella Reset — seamless pet comedy loop](prompts/03-social-ugc.md#6-umbrella-reset--seamless-pet-comedy-loop) |
| [Personajes y referencias · 6](prompts/04-characters-and-references.md) | [1. Harbor Cartographer — consistent character introduction](prompts/04-characters-and-references.md#1-harbor-cartographer--consistent-character-introduction) · [2. Linen Set — virtual try-on walk test](prompts/04-characters-and-references.md#2-linen-set--virtual-try-on-walk-test) · [3. Counter Demo — product placement without redesign](prompts/04-characters-and-references.md#3-counter-demo--product-placement-without-redesign) · [4. Two Voices, One Repair — synchronized dialogue scene](prompts/04-characters-and-references.md#4-two-voices-one-repair--synchronized-dialogue-scene) · [5. Sunday Table — consistent three-person ensemble](prompts/04-characters-and-references.md#5-sunday-table--consistent-three-person-ensemble) · [6. Parcel Finch — reusable brand mascot motion](prompts/04-characters-and-references.md#6-parcel-finch--reusable-brand-mascot-motion) |
| [Edición y extensión · 6](prompts/05-editing-and-extension.md) | [1. Blue Hour Conversion — day-to-night architectural edit](prompts/05-editing-and-extension.md#1-blue-hour-conversion--day-to-night-architectural-edit) · [2. First Snow — controlled weather replacement](prompts/05-editing-and-extension.md#2-first-snow--controlled-weather-replacement) · [3. Clean Plate — remove one distracting object](prompts/05-editing-and-extension.md#3-clean-plate--remove-one-distracting-object) · [4. Practical Miniature — change rendering style, keep motion](prompts/05-editing-and-extension.md#4-practical-miniature--change-rendering-style-keep-motion) · [5. Beyond the Gate — continue a travel shot](prompts/05-editing-and-extension.md#5-beyond-the-gate--continue-a-travel-shot) · [6. Turntable Loop — repair a product animation into a seamless cycle](prompts/05-editing-and-extension.md#6-turntable-loop--repair-a-product-animation-into-a-seamless-cycle) |

<a id="featured-prompts"></a>

## Prompts ilustrados para copiar y adaptar

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. Botella de vidrio marino: compara movimientos controlados

**Ajustes de imagen a vídeo:** 5s · 16:9 · 720p · [Fotograma inicial: abrir y guardar](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/es-ES/sea-glass-bottle.txt)

```text
Conserva la única botella de vidrio marino esmerilado sobre la piedra clara, su tapón cilíndrico, el frontal vacío sin impresiones, el nivel del agua, el horizonte y la suave luz lateral. La botella no se mueve en ningún momento.
Durante cinco segundos, desplaza lentamente la cámara hacia la derecha, como máximo la anchura de una botella.
Una pequeña gota de agua baja por el frontal y se detiene en la base. Las olas del mar al fondo se mueven suavemente desenfocadas. Mantén los reflejos coherentes con la cámara y la fuente de luz.
Audio: solo oleaje lejano; sin música, voz, golpes de cristal ni salpicaduras exageradas.
Sin cortes ni zoom. Conserva la silueta de la botella, la alineación del tapón, la textura del vidrio y la cantidad de objetos.
Evita generar logotipos, cambiar el nivel del líquido, doblar los bordes, hacer flotar objetos o añadir accesorios.
Mantén un encuadre estable durante el último segundo.
```

[Volver al índice de categorías](#find-the-right-prompt) · [Vista rápida de los ejemplos ilustrados](#visual-index)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. Ruta azul: seguimiento de un repartidor en un mercado lluvioso

**Ajustes de imagen a vídeo:** 10s · 16:9 · 1080p · [Fotograma inicial: abrir y guardar](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/es-ES/blue-route.txt)

[Fuente: Flaq AI](docs/ATTRIBUTION.md)

```text
Conserva al repartidor, la moto eléctrica azul cobalto, la caja de carga, el mercado elevado, los toldos translúcidos, la pasarela de acero mojada, la iluminación y la paleta nocturna de la imagen. Crea un único plano de seguimiento bajo y continuo, realista, con masa, agarre de neumáticos, lluvia y suspensión convincentes.

0–3s: la moto acelera suavemente desde la posición existente. La rueda trasera levanta un fino abanico de agua; la suspensión se comprime al pasar una junta de desagüe. La cámara acompaña la moto desde un lateral y ligeramente por detrás, a la altura de las ruedas, igualando su velocidad sin sacudidas violentas.

3–7s: el repartidor se inclina en una curva amplia a la izquierda. Los toldos se flexionan con el viento, sale vapor de los puestos de comida y las luces cálidas del lugar dejan trazos suaves en los reflejos mojados. Mantén ambas ruedas redondas y en contacto con el suelo.

7–10s: la moto se endereza y avanza hacia una zona abierta más luminosa del mercado. La cámara retrocede medio metro, descubre la ruta por delante y mantiene un encuadre final estable.

Audio: zumbido realista de motor eléctrico, agua salpicada, lluvia sobre toldos, voces discretas del mercado y un golpe de suspensión. Sin banda sonora, diálogo, sirenas ni explosiones.

Continuidad: conserva exactamente ropa, casco, geometría de la moto, caja de carga, paneles azules y distribución del mercado. Sin transformación del vehículo, ruedas deformadas, choques, armas, letreros legibles, logotipos, teletransporte de cámara ni cambios imposibles de velocidad.
```

[Volver al índice de categorías](#find-the-right-prompt) · [Vista rápida de los ejemplos ilustrados](#visual-index)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. El pan de miel: historia de una panadería en miniatura

**Ajustes de imagen a vídeo:** 9s · 16:9 · 1080p · [Fotograma inicial: abrir y guardar](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/es-ES/honey-loaf.txt)

[Fuente: Flaq AI](docs/ATTRIBUTION.md)

```text
Conserva la panadería en forma de pera, los tres panaderos en miniatura, trajes, rostros, pan de miel, horno, ventana, musgo, trébol, luna, materiales táctiles de animación stop motion y contraste entre colores cálidos y fríos.

0–3s: empieza con la composición amplia proporcionada y una cadencia sutil de stop motion artesanal. Dos panaderos levantan juntos el pan de miel caliente; sus manos permanecen en contacto con la tabla de madera. Se eleva una pequeña nube de harina, parpadea el fuego del horno y el tercer panadero abre la ventanilla de servicio.

3–7s: la pareja da cuatro pasos cuidadosos y sincronizados hacia la ventana. El pan transmite un peso creíble y baja un poco entre ellos. Fuera, una hoja de trébol suelta una gota de rocío y dos luciérnagas pasan a distintas profundidades. La cámara describe un arco suave de cinco grados hacia la derecha.

7–9s: deslizan la tabla sobre el mostrador, intercambian sonrisas de alivio y el resplandor del horno se estabiliza. Termina con los tres personajes visibles y el pan centrado.

Audio: pequeños pasos en la madera, crepitar suave del horno, crujido de la tabla, insectos nocturnos tenues y una campanilla en la ventanilla. Sin diálogo, narración, música ni texto.

Continuidad: conserva el número de personajes, diseño facial, escala, colores del vestuario, forma de pera, distribución del interior y textura artesanal. Sin panaderos extra, gráficos 3D brillantes, extremidades de goma, accesorios flotantes, pan que se derrite, cortes de cámara, logotipos ni personajes que imiten franquicias.
```

[Volver al índice de categorías](#find-the-right-prompt) · [Vista rápida de los ejemplos ilustrados](#visual-index)

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. Reencuentro en el puerto: un solo momento emotivo

**Ajustes de imagen a vídeo:** 10s · 16:9 · 720p · [Fotograma inicial: abrir y guardar](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/es-ES/harbor-reunion.txt)

```text
Conserva a los dos adultos, sus rostros, la ropa azul marino y crema, el muelle de madera y la suave luz de la mañana de la imagen. Mantén a ambos personajes en el mismo plano medio amplio.
0–3 segundos: la persona de la izquierda ve llegar a su amigo y da un pequeño paso. Sus hombros se relajan; su amigo responde con una sonrisa discreta. Mantén las manos visibles y relajadas.
3–7 segundos: la persona de la izquierda dice en español natural: «Has venido». Su amigo asiente una vez. La frase debe sonar contenida, sin llanto ni expresiones faciales exageradas.
7–10 segundos: ambos miran hacia el barco amarrado. Mantén el último segundo para permitir un corte al siguiente plano.
Cámara: un único acercamiento suave, sin contraplano ni cortes.
Audio: voz cercana e inteligible, agua suave del puerto y una gaviota lejana; sin música ni subtítulos.
Fija las dos identidades, la ropa, la geometría del muelle, la posición del barco y la dirección de la luz matinal.
Evita personas adicionales, gestos dramáticos, rostros alisados, dedos extra y saltos de cámara.
```

[Volver al índice de categorías](#find-the-right-prompt) · [Vista rápida de los ejemplos ilustrados](#visual-index)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. Primer sorbo: reseña auténtica de una creadora en una cafetería

**Ajustes de imagen a vídeo:** 10s · 9:16 · 1080p · [Fotograma inicial: abrir y guardar](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/es-ES/first-sip.txt)

[Fuente: Flaq AI](docs/ATTRIBUTION.md)

```text
Anima la foto de cafetería proporcionada como una reseña sincera de una creadora, grabada cámara en mano. Conserva su rostro, edad, textura de piel, pelo, jersey verde musgo, taza, pastel, ventana y distribución de la mesa.

0–3s: ligero movimiento natural de cámara en mano. Ella termina un sorbo, baja la taza de cerámica unos diez centímetros, exhala con una leve sonrisa y aparta la mirada de la ventana para mirar a cámara. El vapor asciende en espirales y los rastros de lluvia se unen lentamente en el cristal detrás de ella.

3–8s: dice, en español natural y con voz relajada de conversación: «Cremoso, no muy dulce… y se nota la avena». Mantén un tono informal, con una pequeña pausa tras «dulce». Sincroniza bien los labios y mantén la taza firme en su mano.

8–10s: asiente suavemente en señal de aprobación y mira el pastel mientras la cámara se estabiliza.

Audio: voz cercana de móvil, ambiente tranquilo de cafetería, vaporizador de leche lejano, lluvia suave y contacto de la taza de cerámica. La voz domina; el ambiente queda bajo. Sin música de fondo ni subtítulos.

Continuidad: sin embellecer el rostro, cambiar el vestuario, añadir dedos, rediseñar la taza o la comida, hacer aparecer gente al fondo, añadir logotipos ni gestos exagerados de influencer.
```

[Volver al índice de categorías](#find-the-right-prompt) · [Vista rápida de los ejemplos ilustrados](#visual-index)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. La línea de la sal al amanecer: documental de viajes

**Ajustes de imagen a vídeo:** 12s · 16:9 · 1080p · [Fotograma inicial: abrir y guardar](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/es-ES/salt-line.txt)

[Fuente: Flaq AI](docs/ATTRIBUTION.md)

```text
Anima la escena de salinas costeras proporcionada como un documental de viajes observacional y respetuoso. Conserva a los dos trabajadores, el tren crema y ocre, las salinas, las colinas de piedra caliza, los edificios, el mar, la dirección del amanecer y la paleta cinematográfica apagada.

0–4s: plano general fijo. Los trabajadores siguen inspeccionando el canal: uno mueve una herramienta de madera por la salmuera poco profunda mientras el otro sujeta la separación. Las ondas responden a la herramienta y a la brisa matinal. El tren se acerca a velocidad moderada en el plano intermedio.

4–9s: la cámara panea lentamente a la derecha siguiendo el tren. Las ruedas permanecen alineadas con los raíles; la separación entre vagones y el ritmo de las ventanas son constantes. Un velo ligero de bruma marina pasa detrás mientras la luz del sol ilumina gradualmente los cristales de sal del primer plano.

9–12s: el tren continúa hacia la costa y el paneo se detiene suavemente. Un trabajador se incorpora, se estira de forma natural y mira hacia la vía. Mantén los dos últimos segundos como punto de montaje.

Audio: suave zumbido eléctrico ferroviario, ritmo de las ruedas sobre las juntas, brisa sobre el agua somera, gaviotas lejanas y herramienta de madera moviéndose en la salmuera. Sin narración, música, multitud ni bocina dramática.

Continuidad: trabajo realista, anatomía estable, paisaje fijo, diseño del tren intacto, reflejos y física del agua plausibles. Sin horizonte urbano moderno, puesta en escena turística, edificios nuevos, logotipos, letreros legibles, colores de postal sobresaturados ni cielo acelerado.
```

[Volver al índice de categorías](#find-the-right-prompt) · [Vista rápida de los ejemplos ilustrados](#visual-index)

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. Postal de la costa: anima una imagen planificada

**Ajustes de imagen a vídeo:** 5s · 9:16 · 720p · [Fotograma inicial: abrir y guardar](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/es-ES/coastal-postcard.txt)

```text
Anima esta postal costera de tres paneles sin cambiar su distribución ni sus bordes. Conserva exactamente todos los objetos y colores. En el panel superior, una fina voluta de vapor asciende de la taza.
En el panel central, el agua del puerto ondula suavemente y el sol destella en la superficie.
En el panel inferior, solo la esquina de papel ya presente se eleva ligeramente y vuelve a reposar con una brisa leve.
Mantén cada movimiento dentro de su panel. Los tres paneles deben permanecer visibles durante los cinco segundos.
Cámara: fija, sin zoom, paneo, cortes ni transiciones entre paneles.
Audio: agua tranquila y un suave crujido de papel; sin diálogo, música, subtítulos ni texto añadido.
Conserva el asa de la taza, el marco de la ventana, las marcas del mapa, las dimensiones de los paneles y el orden de lectura.
Evita fusionar paneles, inventar otra escena, redibujar letras o mover objetos a través de los bordes.
Termina con la esquina del papel en reposo y la composición original intacta.
```

[Volver al índice de categorías](#find-the-right-prompt) · [Vista rápida de los ejemplos ilustrados](#visual-index)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. Halo cítrico: vídeo de una fragancia de alta gama

**Ajustes de imagen a vídeo:** 8s · 16:9 · 1080p · [Fotograma inicial: abrir y guardar](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/es-ES/citrus-halo.txt)

[Fuente: Flaq AI](docs/ATTRIBUTION.md)

```text
Conserva el diseño de la botella proporcionada, las proporciones del vidrio, el tapón, el pedestal de piedra caliza, la piel de pomelo, el decorado marfil cálido y la luz lateral dorada. Crea un elegante vídeo de producto de ocho segundos.

0–2.5s: empieza con una composición macro casi fija. La cámara avanza muy lentamente. Las gotas de condensación captan la luz; dos gotas resbalan de forma natural por el vidrio frío. La piel de pomelo se eleva del pedestal como impulsada por una brisa de estudio controlada.

2.5–6s: la piel completa una espiral elegante alrededor de la botella sin tocar ni ocultar el tapón. Partículas diminutas de bruma cítrica cruzan el contraluz. La refracción y las cáusticas se desplazan de forma físicamente coherente por el vidrio grueso; la botella permanece completamente rígida.

6–8s: la piel recupera su curva original, la cámara se detiene suavemente y un reflejo especular brillante recorre una sola vez el borde de la botella. Termina con un plano principal limpio del producto.

Audio: solo efectos de estudio cercanos: movimiento suave de la tira de piel, dos gotas de agua nítidas y una delicada resonancia de vidrio. Sin voz, música ni texto.

Continuidad: no alteres la silueta de la botella, las facetas del tapón, el nivel del líquido, el pedestal, la paleta ni el arco del fondo. Sin etiquetas, logotipos, fruta extra, botella flotante, geometría inestable, saltos de cámara ni explosiones artificiales de destellos.
```

[Volver al índice de categorías](#find-the-right-prompt) · [Vista rápida de los ejemplos ilustrados](#visual-index)

<a id="learn-from-official-and-community-examples"></a>

## Aprende de trabajos oficiales y de la comunidad

Las publicaciones originales identifican al creador y la versión del modelo. Ábrelas para ver los vídeos; las notas prácticas de abajo describen métodos y no afirman que hayamos reproducido los vídeos.

### [Secuencia oficial de 1.5 Preview: Grok / Heavy Pulp](https://x.com/grok/status/2062225080843747351)

[![Secuencia oficial de 1.5 Preview: Grok / Heavy Pulp](https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg)](https://x.com/grok/status/2062225080843747351)

Aprende a planificar un tráiler con planos cortos separados. Distingue las imágenes de Preview de las del modelo 1.5 publicado.

### [Cortometraje terminado: JSFILMZ](https://x.com/JSFILMZ0412/status/2062480692835938771)

El autor habla de una película de 2,5 minutos y comenta los límites de la actuación generada. Practica primero un intercambio tranquilo; construye historias más largas montando varios planos.

### [Planificar la imagen antes de animarla: GENEL](https://x.com/genel_ai/status/2061382998873034825)

[![Planificar la imagen antes de animarla: GENEL](https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg)](https://x.com/genel_ai/status/2061382998873034825)

El creador explica que hizo un collage con ChatGPT Images 2.0 y después lo animó con Grok Imagine Video 1.5. Nuestro ejercicio de la postal mantiene fijos los bordes y asigna un solo movimiento a cada panel.

### [Comparación controlada: JSFILMZ](https://x.com/JSFILMZ0412/status/2061117682515050669)

Usa una misma imagen de origen y ajustes comparables. Examina la geometría, el movimiento y el audio en lugar de copiar una clasificación antigua. Nuestro ejercicio de la botella aísla esas variables.

<details>
<summary>Observaciones de fotogramas y límites de verificación</summary>

El 24 de septiembre de 2026 examinamos fotogramas de los reproductores originales de X: del vídeo oficial, aproximadamente en 3,6 s (casco y ejército), 19,8 s (primer plano de un rostro) y 34,6 s (ciudad costera en llamas); de GENEL, aproximadamente en 0,05 s (barandilla junto al mar), 4,9 s (paso a nivel) y 12 s (mano a contraluz). Observa los cambios de escala de plano del vídeo oficial y la luz costera coherente entre los distintos planos de GENEL. Nuestra postal de paneles fijos es un ejercicio diferente. Son fotogramas muestreados, no pruebas completas de movimiento o audio.

</details>

[Fuentes y notas de visualización (en inglés)](docs/COMMUNITY.md)

<a id="writing-guide"></a>

<a id="1-cosecha-de-luz-anuncio-de-aceite-de-oliva"></a>

<a id="biblioteca-completa"></a>

<a id="contribuir"></a>

<a id="cómo-creo-una-historia-de-más-de-15-segundos"></a>

<a id="cómo-mantengo-un-rostro-o-producto-estable"></a>

<a id="plantilla-recomendada"></a>

<a id="preguntas-frecuentes"></a>

<a id="prompts-originales-en-español"></a>

<a id="puedo-escribir-el-prompt-en-español"></a>

## Material de referencia

[Referencia de escritura](docs/guides/es-ES.md) · [Referencia de ajustes y uso](docs/workflows/es-ES.md) · [SeaImagine](https://seaimagine.com/es/model/grok-imagine-1-5/)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

<a id="multilingual-prompts"></a>

## Colección y atribución

38 recetas distintas en inglés en total: 35 heredadas y estos 3 ejercicios nuevos. Las traducciones no añaden escenarios nuevos.

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/es/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
