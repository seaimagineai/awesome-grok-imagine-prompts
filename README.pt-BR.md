# Biblioteca de prompts do Grok Imagine 1.5 — Português (Brasil)

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 38 prompts, incluindo 8 exemplos ilustrados disponíveis em 15 idiomas. Navegue por categoria e copie os prompts completos.

![Grok Imagine 1.5 — Caderno de prompts aberto com um tênis, um bonde e uma baleia de papel no mesmo cenário](assets/seaimagine-grok-hero.webp)

Adaptada de [Flaq AI](https://github.com/flaqai/awesome-grok-imagine) e mantida pela SeaImagine. Licença [MIT](LICENSE). Não é um projeto oficial da xAI. As imagens conceituais não são resultados verificados do Grok.

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## Índice de categorias

| Objetivo | Exemplos ilustrados |
| --- | --- |
| Anúncios de produtos | [Garrafa de vidro marinho: comparação de movimentos controlados](#case-sea-glass-bottle) · [Halo cítrico: filme de uma fragrância premium](#case-citrus-halo) |
| Ação cinematográfica | [Rota azul: acompanhamento de um entregador no mercado chuvoso](#case-blue-route) |
| Histórias de fantasia | [O pão com mel: história de uma padaria em miniatura](#case-honey-loaf) |
| Diálogos de personagens | [Reencontro no porto: um único momento de emoção](#case-harbor-reunion) |
| Vídeos de estilo de vida | [Primeiro gole: avaliação autêntica de uma criadora no café](#case-first-sip) |
| Filmes de viagem | [A linha do sal ao amanhecer: documentário de viagem](#case-salt-line) |
| Composições animadas | [Cartão-postal litorâneo: anime uma imagem planejada](#case-coastal-postcard) |

[Exemplos ilustrados](#featured-prompts) · [Trabalhos oficiais e da comunidade](#learn-from-official-and-community-examples) · [Referência de configurações e uso](#writing-guide)

<a id="visual-index"></a>

### Visão geral dos exemplos ilustrados

8 exemplos com prompts completos e imagens do quadro inicial. As imagens ilustram conceitos; não são resultados de vídeo verificados.

Os cinco exemplos marcados como “Fonte: Flaq AI” preservam a duração e a resolução originais; os outros três usam as opções atuais do SeaImagine. Para usar um exemplo da fonte no SeaImagine, escolha 5/10/15 segundos e 480p/720p e reescreva suas ações cronometradas.

| | |
| --- | --- |
| <a href="#case-sea-glass-bottle"><img src="assets/seaimagine-sea-glass-bottle.webp" height="180" alt="Garrafa de vidro marinho: comparação de movimentos controlados"></a><br>[1. Garrafa de vidro marinho: comparação de movimentos controlados](#case-sea-glass-bottle)<br>5s · 16:9 · 720p | <a href="#case-blue-route"><img src="assets/rainy-market-courier-video.webp" height="180" alt="Rota azul: acompanhamento de um entregador no mercado chuvoso"></a><br>[2. Rota azul: acompanhamento de um entregador no mercado chuvoso](#case-blue-route)<br>10s · 16:9 · 1080p |
| <a href="#case-honey-loaf"><img src="assets/pear-bakery-miniature-video.webp" height="180" alt="O pão com mel: história de uma padaria em miniatura"></a><br>[3. O pão com mel: história de uma padaria em miniatura](#case-honey-loaf)<br>9s · 16:9 · 1080p | <a href="#case-harbor-reunion"><img src="assets/seaimagine-harbor-reunion.webp" height="180" alt="Reencontro no porto: um único momento de emoção"></a><br>[4. Reencontro no porto: um único momento de emoção](#case-harbor-reunion)<br>10s · 16:9 · 720p |
| <a href="#case-first-sip"><img src="assets/cozy-cafe-ugc-video.webp" height="180" alt="Primeiro gole: avaliação autêntica de uma criadora no café"></a><br>[5. Primeiro gole: avaliação autêntica de uma criadora no café](#case-first-sip)<br>10s · 9:16 · 1080p | <a href="#case-salt-line"><img src="assets/coastal-salt-train-documentary.webp" height="180" alt="A linha do sal ao amanhecer: documentário de viagem"></a><br>[6. A linha do sal ao amanhecer: documentário de viagem](#case-salt-line)<br>12s · 16:9 · 1080p |
| <a href="#case-coastal-postcard"><img src="assets/seaimagine-coastal-postcard.webp" height="180" alt="Cartão-postal litorâneo: anime uma imagem planejada"></a><br>[7. Cartão-postal litorâneo: anime uma imagem planejada](#case-coastal-postcard)<br>5s · 9:16 · 720p | <a href="#case-citrus-halo"><img src="assets/citrus-fragrance-product-video.webp" height="180" alt="Halo cítrico: filme de uma fragrância premium"></a><br>[8. Halo cítrico: filme de uma fragrância premium](#case-citrus-halo)<br>8s · 16:9 · 1080p |

**Veja mais prompts (em inglês) · 30**

| Categoria | Índice de exemplos |
| --- | --- |
| [Anúncios e produtos · 6](prompts/01-ads-and-products.md) | [1. Dew Drop Laboratory — skincare serum macro](prompts/01-ads-and-products.md#1-dew-drop-laboratory--skincare-serum-macro) · [2. Cold Brew Eclipse — coffee launch film](prompts/01-ads-and-products.md#2-cold-brew-eclipse--coffee-launch-film) · [3. Street-to-Studio — performance shoe demonstration](prompts/01-ads-and-products.md#3-street-to-studio--performance-shoe-demonstration) · [4. Doorstep Dinner — food delivery social ad](prompts/01-ads-and-products.md#4-doorstep-dinner--food-delivery-social-ad) · [5. Silver Current — artisan jewelry reveal](prompts/01-ads-and-products.md#5-silver-current--artisan-jewelry-reveal) · [6. One Tap Away — clean mobile app promo](prompts/01-ads-and-products.md#6-one-tap-away--clean-mobile-app-promo) |
| [Histórias cinematográficas · 6](prompts/02-cinematic-storytelling.md) | [1. Last Tram Note — restrained urban romance](prompts/02-cinematic-storytelling.md#1-last-tram-note--restrained-urban-romance) · [2. Room 407 — quiet hotel mystery](prompts/02-cinematic-storytelling.md#2-room-407--quiet-hotel-mystery) · [3. Glasshouse Pursuit — grounded parkour action](prompts/02-cinematic-storytelling.md#3-glasshouse-pursuit--grounded-parkour-action) · [4. Tidekeeper — coastal fantasy ritual](prompts/02-cinematic-storytelling.md#4-tidekeeper--coastal-fantasy-ritual) · [5. Paper Moon Delivery — hand-drawn animation](prompts/02-cinematic-storytelling.md#5-paper-moon-delivery--hand-drawn-animation) · [6. Europa Signal — hard-science discovery](prompts/02-cinematic-storytelling.md#6-europa-signal--hard-science-discovery) |
| [Redes sociais e estilo de vida · 6](prompts/03-social-ugc.md) | [1. Shelf Test — honest skincare mini-review](prompts/03-social-ugc.md#1-shelf-test--honest-skincare-mini-review) · [2. Twelve-Minute Noodles — one-pan recipe reel](prompts/03-social-ugc.md#2-twelve-minute-noodles--one-pan-recipe-reel) · [3. First Set — realistic morning fitness log](prompts/03-social-ugc.md#3-first-set--realistic-morning-fitness-log) · [4. One Question, One Corner — street interview](prompts/03-social-ugc.md#4-one-question-one-corner--street-interview) · [5. Clay Cup Morning — tactile pottery ASMR](prompts/03-social-ugc.md#5-clay-cup-morning--tactile-pottery-asmr) · [6. Umbrella Reset — seamless pet comedy loop](prompts/03-social-ugc.md#6-umbrella-reset--seamless-pet-comedy-loop) |
| [Personagens e referências · 6](prompts/04-characters-and-references.md) | [1. Harbor Cartographer — consistent character introduction](prompts/04-characters-and-references.md#1-harbor-cartographer--consistent-character-introduction) · [2. Linen Set — virtual try-on walk test](prompts/04-characters-and-references.md#2-linen-set--virtual-try-on-walk-test) · [3. Counter Demo — product placement without redesign](prompts/04-characters-and-references.md#3-counter-demo--product-placement-without-redesign) · [4. Two Voices, One Repair — synchronized dialogue scene](prompts/04-characters-and-references.md#4-two-voices-one-repair--synchronized-dialogue-scene) · [5. Sunday Table — consistent three-person ensemble](prompts/04-characters-and-references.md#5-sunday-table--consistent-three-person-ensemble) · [6. Parcel Finch — reusable brand mascot motion](prompts/04-characters-and-references.md#6-parcel-finch--reusable-brand-mascot-motion) |
| [Edição e extensão · 6](prompts/05-editing-and-extension.md) | [1. Blue Hour Conversion — day-to-night architectural edit](prompts/05-editing-and-extension.md#1-blue-hour-conversion--day-to-night-architectural-edit) · [2. First Snow — controlled weather replacement](prompts/05-editing-and-extension.md#2-first-snow--controlled-weather-replacement) · [3. Clean Plate — remove one distracting object](prompts/05-editing-and-extension.md#3-clean-plate--remove-one-distracting-object) · [4. Practical Miniature — change rendering style, keep motion](prompts/05-editing-and-extension.md#4-practical-miniature--change-rendering-style-keep-motion) · [5. Beyond the Gate — continue a travel shot](prompts/05-editing-and-extension.md#5-beyond-the-gate--continue-a-travel-shot) · [6. Turntable Loop — repair a product animation into a seamless cycle](prompts/05-editing-and-extension.md#6-turntable-loop--repair-a-product-animation-into-a-seamless-cycle) |

<a id="featured-prompts"></a>

## Prompts ilustrados para copiar e adaptar

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. Garrafa de vidro marinho: comparação de movimentos controlados

**Configurações de imagem para vídeo:** 5s · 16:9 · 720p · [Quadro inicial: abrir e salvar](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/pt-BR/sea-glass-bottle.txt)

```text
Preserve a única garrafa de vidro marinho fosco sobre a pedra clara, sua tampa cilíndrica, a frente vazia sem impressão, o nível da água, o horizonte e a luz lateral suave. A garrafa nunca se move.
Durante cinco segundos, deslize lentamente a câmera para a direita, no máximo a largura de uma garrafa.
Uma pequena gota de água desce pela frente e para na base. Ao fundo, as ondas do mar se movem suavemente, desfocadas. Mantenha os reflexos coerentes com a câmera e a fonte de luz.
Áudio: apenas ondas distantes; sem música, voz, impacto de vidro ou respingos exagerados.
Sem cortes nem zoom. Preserve a silhueta da garrafa, o alinhamento da tampa, a textura do vidro e a quantidade de objetos.
Evite gerar logotipos, mudar o nível do líquido, deformar bordas, fazer objetos flutuarem ou adicionar acessórios.
Mantenha o enquadramento estável durante o último segundo.
```

[Voltar ao índice de categorias](#find-the-right-prompt) · [Visão geral dos exemplos ilustrados](#visual-index)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. Rota azul: acompanhamento de um entregador no mercado chuvoso

**Configurações de imagem para vídeo:** 10s · 16:9 · 1080p · [Quadro inicial: abrir e salvar](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/pt-BR/blue-route.txt)

[Fonte: Flaq AI](docs/ATTRIBUTION.md)

```text
Preserve o entregador, a moto elétrica azul-cobalto, o baú, o mercado elevado, os toldos translúcidos, a passarela de aço molhada, a iluminação e a paleta noturna. Crie uma única tomada baixa e contínua de acompanhamento, realista, com massa, aderência dos pneus, chuva e suspensão convincentes.

0–3s: a moto acelera suavemente da posição existente. O pneu traseiro desloca um leque fino de água; a suspensão comprime ao passar uma junta de drenagem. A câmera acompanha ao lado e um pouco atrás, na altura das rodas, mantendo a velocidade sem tremer violentamente.

3–7s: o entregador se inclina numa curva ampla à esquerda. Os toldos se flexionam com o vento, o vapor sai das barracas de comida e as luzes quentes do cenário deixam rastros suaves nos reflexos molhados. Mantenha as duas rodas redondas e em contato com o chão.

7–10s: a moto se endireita e segue para uma parte aberta e mais iluminada do mercado. A câmera recua meio metro, revelando o caminho à frente, e mantém um quadro final estável.

Áudio: zumbido realista do motor elétrico, água espirrando, chuva nos toldos, vozes discretas do mercado e uma batida da suspensão. Sem trilha, diálogo, sirenes ou explosões.

Continuidade: roupa e capacete exatos, geometria da moto, baú, painéis azuis e disposição do mercado. Sem transformação do veículo, deformação das rodas, colisões, armas, placas legíveis, logotipos, teletransporte da câmera ou mudanças impossíveis de velocidade.
```

[Voltar ao índice de categorias](#find-the-right-prompt) · [Visão geral dos exemplos ilustrados](#visual-index)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. O pão com mel: história de uma padaria em miniatura

**Configurações de imagem para vídeo:** 9s · 16:9 · 1080p · [Quadro inicial: abrir e salvar](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/pt-BR/honey-loaf.txt)

[Fonte: Flaq AI](docs/ATTRIBUTION.md)

```text
Mantenha a padaria em forma de pera, os três padeiros em miniatura, trajes, rostos, pão com mel, forno, janela, musgo, trevo, lua, materiais táteis de stop motion e contraste entre cores quentes e frias.

0–3s: comece na composição ampla fornecida, com cadência sutil de stop motion artesanal. Dois padeiros levantam juntos o pão com mel quente; as mãos permanecem em contato com a tábua de madeira. Uma pequena nuvem de farinha sobe, o fogo do forno tremula e o terceiro padeiro abre a janela de atendimento.

3–7s: a dupla dá quatro passos cuidadosos e sincronizados até a janela. O pão tem peso convincente e desce um pouco entre eles. Lá fora, uma folha de trevo solta uma gota de orvalho e dois vaga-lumes passam em profundidades diferentes. A câmera faz um arco suave de cinco graus à direita.

7–9s: eles deslizam a tábua sobre o balcão, trocam sorrisos de alívio e o brilho do forno se estabiliza. Termine com os três personagens visíveis e o pão centralizado.

Áudio: pequenos passos na madeira, crepitar suave do forno, rangido da tábua, insetos noturnos discretos e um pequeno sino na janela de atendimento. Sem diálogo, narração, música ou texto.

Continuidade: preserve a quantidade de personagens, desenho dos rostos, escala, cores das roupas, formato de pera, disposição do cômodo e textura artesanal. Sem padeiros extras, computação gráfica brilhante, membros de borracha, objetos flutuantes, pão derretendo, cortes, logotipos ou personagens semelhantes aos de franquias.
```

[Voltar ao índice de categorias](#find-the-right-prompt) · [Visão geral dos exemplos ilustrados](#visual-index)

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. Reencontro no porto: um único momento de emoção

**Configurações de imagem para vídeo:** 10s · 16:9 · 720p · [Quadro inicial: abrir e salvar](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/pt-BR/harbor-reunion.txt)

```text
Preserve os dois adultos, seus rostos, as roupas azul-marinho e creme, o píer de madeira e a luz suave da manhã da imagem fornecida. Mantenha os dois personagens no mesmo plano médio aberto.
0–3 segundos: a pessoa à esquerda percebe o amigo chegando e dá um pequeno passo. Seus ombros relaxam; o amigo responde com um sorriso discreto. Mantenha as mãos visíveis e relaxadas.
3–7 segundos: a pessoa à esquerda diz, em português brasileiro natural: “Você veio.” O amigo faz um único aceno afirmativo com a cabeça. A fala deve ser contida, sem choro nem expressões faciais exageradas.
7–10 segundos: ambos olham para o barco atracado. Mantenha o último segundo para permitir um corte para o próximo plano.
Câmera: uma única aproximação suave, sem contraplano e sem cortes.
Áudio: voz próxima e compreensível, água suave do porto e uma gaivota distante; sem música nem legendas.
Fixe as duas identidades, as roupas, a geometria do píer, a posição do barco e a direção da luz da manhã.
Evite pessoas extras, gestos dramáticos, rostos alisados, dedos extras e saltos de câmera.
```

[Voltar ao índice de categorias](#find-the-right-prompt) · [Visão geral dos exemplos ilustrados](#visual-index)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. Primeiro gole: avaliação autêntica de uma criadora no café

**Configurações de imagem para vídeo:** 10s · 9:16 · 1080p · [Quadro inicial: abrir e salvar](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/pt-BR/first-sip.txt)

[Fonte: Flaq AI](docs/ATTRIBUTION.md)

```text
Anime a foto do café como uma avaliação sincera de uma criadora, filmada com câmera na mão. Preserve rosto, idade, textura da pele, cabelo, suéter verde-musgo, xícara, doce, janela e disposição da mesa.

0–3s: leve oscilação natural de câmera na mão. Ela termina um gole, baixa a xícara de cerâmica cerca de dez centímetros, solta o ar com um pequeno sorriso e olha da janela de volta para a câmera. O vapor sobe em espirais e os rastros de chuva se unem lentamente no vidro atrás dela.

3–8s: ela diz, em português brasileiro natural e tom descontraído: “Cremoso, não muito doce… e dá mesmo pra sentir a aveia.” Mantenha a fala casual, com uma pequena pausa depois de “doce”. Sincronize bem os lábios e mantenha a xícara firme na mão.

8–10s: ela faz um pequeno aceno de aprovação e olha para o doce enquanto a câmera se estabiliza.

Áudio: voz próxima de celular, ambiente tranquilo de café, vaporizador de leite distante, chuva suave e contato da xícara de cerâmica. Voz em primeiro plano; ambiente baixo. Sem música de fundo nem legendas.

Continuidade: sem embelezar o rosto, trocar roupas, adicionar dedos, redesenhar a xícara ou a comida, fazer pessoas surgirem ao fundo, logotipos ou gestos exagerados de influenciadora.
```

[Voltar ao índice de categorias](#find-the-right-prompt) · [Visão geral dos exemplos ilustrados](#visual-index)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. A linha do sal ao amanhecer: documentário de viagem

**Configurações de imagem para vídeo:** 12s · 16:9 · 1080p · [Quadro inicial: abrir e salvar](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/pt-BR/salt-line.txt)

[Fonte: Flaq AI](docs/ATTRIBUTION.md)

```text
Anime a cena das salinas costeiras como um documentário de viagem observacional e respeitoso. Preserve os dois trabalhadores, o trem creme e ocre, os tanques de sal, as colinas de calcário, os prédios, o mar, a direção do nascer do sol e a paleta cinematográfica suave.

0–4s: plano aberto fixo. Os trabalhadores continuam inspecionando o canal: um move uma ferramenta de madeira na salmoura rasa enquanto o outro firma a divisória. As ondulações respondem à ferramenta e à brisa da manhã. O trem se aproxima em velocidade moderada no plano intermediário.

4–9s: a câmera faz uma panorâmica lenta à direita para seguir o trem. As rodas continuam alinhadas aos trilhos; o espaçamento dos vagões e o ritmo das janelas permanecem constantes. Um véu leve de névoa marinha passa atrás enquanto a luz do sol alcança aos poucos os cristais de sal em primeiro plano.

9–12s: o trem segue em direção à costa e a panorâmica para suavemente. Um trabalhador se levanta, se alonga naturalmente e olha para a linha. Mantenha os dois segundos finais para permitir um ponto de edição.

Áudio: leve zumbido elétrico ferroviário, ritmo das rodas nas juntas, brisa sobre água rasa, gaivotas distantes e ferramenta de madeira na salmoura. Sem narração, música, multidão ou buzina dramática.

Continuidade: trabalho realista, anatomia estável, paisagem fixa, design do trem inalterado, reflexos e física da água plausíveis. Sem horizonte urbano moderno, encenação turística, prédios novos, logotipos, placas legíveis, cores de cartão-postal supersaturadas ou céu acelerado.
```

[Voltar ao índice de categorias](#find-the-right-prompt) · [Visão geral dos exemplos ilustrados](#visual-index)

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. Cartão-postal litorâneo: anime uma imagem planejada

**Configurações de imagem para vídeo:** 5s · 9:16 · 720p · [Quadro inicial: abrir e salvar](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/pt-BR/coastal-postcard.txt)

```text
Anime este cartão-postal litorâneo de três painéis sem mudar a disposição ou as bordas. Preserve exatamente todos os objetos e cores. No painel superior, uma fina espiral de vapor sobe da xícara.
No painel central, a água do porto ondula suavemente e a luz do sol brilha na superfície.
No painel inferior, apenas a ponta de papel já existente se levanta um pouco e volta a repousar com uma brisa leve.
Mantenha cada movimento dentro do próprio painel. Todos os painéis permanecem visíveis durante os cinco segundos.
Câmera: fixa, sem zoom, panorâmica, cortes ou transições entre painéis.
Áudio: água calma e um leve ruído de papel; sem diálogo, música, legendas ou texto adicional.
Preserve a alça da xícara, a moldura da janela, as marcações do mapa, as dimensões dos painéis e a ordem de leitura.
Evite fundir painéis, inventar uma nova cena, redesenhar letras ou mover objetos através das bordas.
Termine com a ponta de papel em repouso e a composição original intacta.
```

[Voltar ao índice de categorias](#find-the-right-prompt) · [Visão geral dos exemplos ilustrados](#visual-index)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. Halo cítrico: filme de uma fragrância premium

**Configurações de imagem para vídeo:** 8s · 16:9 · 1080p · [Quadro inicial: abrir e salvar](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/pt-BR/citrus-halo.txt)

[Fonte: Flaq AI](docs/ATTRIBUTION.md)

```text
Preserve o design do frasco fornecido, as proporções do vidro, a tampa, o pedestal de calcário, a casca de toranja, o cenário marfim quente e a luz lateral dourada. Crie um elegante filme de produto de oito segundos.

0–2.5s: comece com uma composição macro quase fixa. A câmera avança muito lentamente. Gotas de condensação captam a luz; duas gotas escorrem naturalmente pelo vidro frio. A casca de toranja se ergue do pedestal como se fosse levada por uma brisa de estúdio controlada.

2.5–6s: a casca completa uma espiral graciosa ao redor do frasco sem tocar nem ocultar a tampa. Pequenas partículas de névoa cítrica atravessam a contraluz. Refração e cáusticas se movem de forma fisicamente coerente pelo vidro espesso; o frasco permanece totalmente rígido.

6–8s: a casca volta à curva original, a câmera para suavemente e um reflexo especular brilhante percorre uma vez a borda do frasco. Termine com um enquadramento limpo de destaque do produto.

Áudio: apenas efeitos de estúdio próximos — movimento suave da tira de casca, duas gotas de água nítidas e uma delicada ressonância de vidro. Sem voz, música ou texto.

Continuidade: não altere a silhueta do frasco, as facetas da tampa, o nível do líquido, o pedestal, a paleta ou o arco ao fundo. Sem rótulos, logotipos, frutas extras, frasco flutuante, geometria instável, saltos de câmera ou explosão artificial de brilhos.
```

[Voltar ao índice de categorias](#find-the-right-prompt) · [Visão geral dos exemplos ilustrados](#visual-index)

<a id="learn-from-official-and-community-examples"></a>

## Aprenda com trabalhos oficiais e da comunidade

As publicações originais identificam o criador e a versão do modelo. Abra os originais para assistir; as observações práticas abaixo descrevem métodos, sem afirmar que reproduzimos os vídeos.

### [Sequência oficial de 1.5 Preview: Grok / Heavy Pulp](https://x.com/grok/status/2062225080843747351)

[![Sequência oficial de 1.5 Preview: Grok / Heavy Pulp](https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg)](https://x.com/grok/status/2062225080843747351)

Aprenda a planejar um trailer em planos curtos separados. Diferencie as imagens de Preview das produzidas pelo modelo 1.5 lançado.

### [Curta-metragem concluído: JSFILMZ](https://x.com/JSFILMZ0412/status/2062480692835938771)

O autor relata um filme de 2,5 minutos e comenta os limites da atuação gerada. Pratique primeiro uma conversa tranquila; monte histórias mais longas com planos editados.

### [Planejamento da imagem antes da animação: GENEL](https://x.com/genel_ai/status/2061382998873034825)

[![Planejamento da imagem antes da animação: GENEL](https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg)](https://x.com/genel_ai/status/2061382998873034825)

O criador relata ter feito uma colagem com ChatGPT Images 2.0 e depois a animado com Grok Imagine Video 1.5. Nosso exercício do cartão-postal mantém as bordas fixas e atribui apenas um movimento a cada painel.

### [Comparação controlada: JSFILMZ](https://x.com/JSFILMZ0412/status/2061117682515050669)

Use a mesma imagem de origem e configurações comparáveis. Verifique geometria, movimento e áudio em vez de copiar uma classificação antiga. Nosso exercício da garrafa isola essas variáveis.

<details>
<summary>Observações de quadros e limites da verificação</summary>

Em 24 de setembro de 2026, examinamos alguns quadros nos players originais do X: no clipe oficial, por volta de 3,6 s (capacete e exército), 19,8 s (rosto em close) e 34,6 s (cidade à beira-mar em chamas); no de GENEL, por volta de 0,05 s (guarda-corpo à beira-mar), 4,9 s (passagem de nível) e 12 s (mão em contraluz). Observe as mudanças de escala dos planos no clipe oficial e a luz costeira consistente entre planos separados de GENEL. Nosso cartão-postal de painéis fixos é um exercício diferente. São amostras de quadros, não testes completos de movimento ou áudio.

</details>

[Fontes e observações sobre a visualização (em inglês)](docs/COMMUNITY.md)

<a id="writing-guide"></a>

<a id="biblioteca-completa"></a>

<a id="regras-rápidas"></a>

<a id="teste-multilíngue-compartilhado-ateliê-de-luminária-em-cerâmica"></a>

## Material de referência

[Referência de escrita](docs/guides/pt-BR.md) · [Referência de configurações e uso](docs/workflows/pt-BR.md) · [SeaImagine](https://seaimagine.com/pt/model/grok-imagine-1-5/)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

<a id="multilingual-prompts"></a>

## Coleção e atribuição

38 receitas distintas em inglês no total: 35 herdadas e estes 3 exercícios novos. As traduções não acrescentam novos cenários.

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/pt/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
