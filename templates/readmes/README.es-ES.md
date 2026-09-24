# SeaImagine · Grok Imagine 1.5 — Español

{{LANGUAGE_NAV}}

> 38 recetas en inglés: 35 adaptadas de Flaq AI y 3 ejercicios nuevos de SeaImagine. Guías en 15 idiomas; las traducciones no se cuentan como escenas nuevas.

![SeaImagine · Grok Imagine 1.5 · Prompt Library](assets/seaimagine-grok-hero.webp)

SeaImagine adapta esta colección de Flaq AI con atribución. No es un proyecto oficial de xAI. Las imágenes conceptuales no son resultados verificados de Grok. [Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [MIT](LICENSE)

{{LOCALIZED_CORE}}

## 1. Cosecha de luz: anuncio de aceite de oliva

**Modo:** imagen a vídeo · **Salida:** 8 s · 16:9 · 1080p

```text
Conservar la botella original sin marca, su vidrio verde, tapón, etiqueta, nivel de aceite, plato
de piedra clara, rama de olivo, fondo marfil y luz lateral de la imagen de origen. La botella
permanece rígida, vertical y en el mismo punto durante todo el plano.

0–3 s: macro casi fijo con un avance de cámara de cuatro centímetros. Una gota de aceite recorre
lentamente el pico vertedor y cae sobre el plato; la rama responde a una brisa suave. 3–6 s: una
franja de luz solar atraviesa el vidrio y proyecta una caústica físicamente creíble sobre la piedra.
Dos hojas giran ligeramente sin desprenderse. 6–8 s: la cámara se detiene, la caústica se suaviza
y el último segundo queda limpio para el plano final de producto.

Audio: una gota densa, roce de hojas, ambiente tranquilo de olivar y una resonancia mínima de
vidrio. Sin voz, música ni subtítulos.

Continuidad: forma y escala de la botella, etiqueta y ortografía, tapón, color y nivel del aceite,
rama, sombras y dirección de luz. Evitar botella flotante, etiqueta mutada, aceitunas nuevas,
salpicadura exagerada, brillo mágico, logo añadido, corte de cámara o marca de agua.
```


## Diseñado para Grok Imagine Video 1.5

- Clips de 1 a 15 segundos con una acción principal clara.
- Primer encuadre definido antes del movimiento en texto a vídeo.
- Dirección centrada en movimiento, cámara, física y sonido para imagen a vídeo.
- Referencias asignadas con etiquetas como `<IMAGE_0>` y `<AUDIO_0>`.
- Bloqueos explícitos de identidad, vestuario, geometría del producto, etiqueta e iluminación.
- Ediciones redactadas como una orden de cambio: qué se modifica y qué queda intacto.

Según la [documentación actual de generación de vídeo de xAI](https://docs.x.ai/developers/model-capabilities/video/generation), texto a vídeo e imagen a vídeo admiten hasta 1080p; referencia a vídeo llega hasta 720p. La [guía de referencias](https://docs.x.ai/developers/model-capabilities/video/reference-to-video) indica un máximo de siete imágenes y tres voces predefinidas. Revisión: **24 de septiembre de 2026**.

## Plantilla recomendada

```text
[Modo y salida] Imagen a vídeo, 8 segundos, 16:9.
[Bloqueo de origen] Mantener sujeto, materiales, color, iluminación y composición.
[Acción] Una acción principal y movimientos secundarios discretos en pelo, tela, reflejos o fondo.
[Cámara] Un único movimiento continuo, motivado y con foco estable.
[Física] Peso, contacto, inercia, viento, agua o tela solo cuando sean relevantes.
[Audio] Ambiente, foley, diálogo y música con una prioridad de mezcla clara.
[Continuidad] No cambiar identidad, ropa, forma del producto, etiqueta ni relaciones espaciales.
[Evitar] Dedos extra, deformación, deriva facial, saltos de cámara, subtítulos o logos nuevos.
[Final] Terminar con un encuadre estable durante el último segundo.
```

## Prompts originales en español

- [Cosecha de luz — anuncio de aceite de oliva](i18n/prompts.es-ES.md#1-cosecha-de-luz-anuncio-de-aceite-de-oliva)
- [Último puesto — documental de mercado](i18n/prompts.es-ES.md#2-último-puesto-mini-documental-de-mercado)
- [Una sola toma — sesión acústica UGC](i18n/prompts.es-ES.md#3-una-sola-toma-sesión-acústica-ugc)
- [Lino y sombra — lookbook con referencias](i18n/prompts.es-ES.md#4-lino-y-sombra-lookbook-con-referencias)

## Biblioteca completa

- [Anuncios y productos](prompts/01-ads-and-products.md)
- [Narrativa cinematográfica](prompts/02-cinematic-storytelling.md)
- [Redes sociales, UGC y estilo de vida](prompts/03-social-ugc.md)
- [Personajes y referencias](prompts/04-characters-and-references.md)
- [Edición, extensión y transformaciones](prompts/05-editing-and-extension.md)

## Preguntas frecuentes

### ¿Puedo escribir el prompt en español?

Sí. Escribe la dirección visual en el idioma que te permita ser más preciso. Para diálogo, conserva la frase exacta entre comillas e indica idioma, variante, tono, energía, pausas y prioridad en la mezcla.

### ¿Cómo mantengo un rostro o producto estable?

Usa pocas referencias con funciones distintas: identidad, cuerpo/vestuario, producto y localización. Repite solo los rasgos que no deben cambiar y reduce el número de acciones y movimientos de cámara.

### ¿Cómo creo una historia de más de 15 segundos?

Divídela en planos de 6–12 segundos. Termina cada plano en una pose estable y continúa desde el último fotograma, o genera el siguiente con las mismas referencias y móntalos después.

## Contribuir

Consulta [CONTRIBUTING.md](CONTRIBUTING.md). Se aceptan obras originales o adaptaciones autorizadas con atribución. Indica si se han probado y comparte solo materiales que tengas derecho a usar. No importes contenido sin permiso ni elimines la atribución.

## Crear con SeaImagine

[Grok Imagine 1.5 · SeaImagine]({{PRODUCT_URL}})

Sube la imagen inicial, pega un prompt de movimiento y elige los ajustes disponibles. Revisa rostros, manos, forma del producto y sonido antes de descargar.

[SeaImagine](docs/SEAIMAGINE.md) · [xAI](docs/OFFICIAL.md) · [X / Community](docs/COMMUNITY.md) · [15 languages](docs/LANGUAGES.md)
