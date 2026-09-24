# Grok Imagine 1.5 프롬프트 모음 — 한국어

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 프롬프트 62개를 수록했으며, 그중 이미지 예제 8개는 15개 언어로 제공합니다. 분류별로 찾아보고 전체 프롬프트를 복사하세요.

![Grok Imagine 1.5 — 펼친 프롬프트 노트에서 신발, 전차, 종이 고래가 하나의 장면으로 이어지는 모습](assets/seaimagine-grok-hero.webp)

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine)를 바탕으로 재구성했으며 SeaImagine이 관리합니다. [MIT](LICENSE) 라이선스를 따르며 xAI와 독립된 프로젝트입니다. 콘셉트 이미지는 Grok으로 실험한 결과를 보여 주는 것이 아닙니다.

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## 분류 색인

[더 많은 프롬프트 보기(영어) · 62](docs/PROMPT_INDEX.md)

| 분류 | 장면 | 사용 모드 | 예시 |
| --- | --- | --- | --- |
| [제품과 광고 · 8](docs/PROMPT_INDEX.md#01-ads-and-products) | 스킨케어 접사 / 커피 / 주얼리 / 앱 광고 | 텍스트로 영상 생성 / 이미지로 영상 생성 / 참조 이미지로 영상 생성 | [바다 유리병 — 조건을 통제하며 움직임 비교하기](#case-sea-glass-bottle) · [시트러스 헤일로 — 고급 향수 제품 영상](#case-citrus-halo) |
| [영화적 스토리텔링 · 8](docs/PROMPT_INDEX.md#02-cinematic-storytelling) | 액션 / 로맨스 / 서스펜스 / SF / 애니메이션 | 텍스트로 영상 생성 / 이미지로 영상 생성 / 영상 연장 | [블루 루트 — 비 내리는 시장의 배달원 추적 숏](#case-blue-route) · [해안 엽서 — 구성을 정한 이미지를 움직이기](#case-coastal-postcard) |
| [소셜 콘텐츠와 일상 · 8](docs/PROMPT_INDEX.md#03-social-ugc) | 체험 후기 / 음식 / 피트니스 / 인터뷰 | 텍스트로 영상 생성 / 이미지로 영상 생성 / 참조 이미지로 영상 생성 | [첫 모금 — 자연스러운 카페 체험 리뷰](#case-first-sip) · [새벽의 염전 철도 — 여행 다큐멘터리](#case-salt-line) |
| [인물과 대화 · 7](docs/PROMPT_INDEX.md#04-characters-and-references) | 인물 / 의상 / 대화 / 군상 | 참조 이미지로 영상 생성 / 이미지로 영상 생성 | [항구에서의 재회 — 하나의 감정 변화에 집중하기](#case-harbor-reunion) |
| [시각적 변형과 이어 만들기 · 6](docs/PROMPT_INDEX.md#05-editing-and-extension) | 날씨 변경 / 불필요한 요소 제거 / 스타일 변경 / 이어 만들기 | 영상 편집 / 영상 연장 | — |
| [만족감을 주는 재질과 소리 · 6](docs/PROMPT_INDEX.md#07-satisfying-materials) | 모래 누르기 / 동박 / 물방울 / 마블링 | 텍스트로 영상 생성 | — |
| [공간과 건축 · 6](docs/PROMPT_INDEX.md#08-spaces-and-transformations) | 펼쳐지는 가구 / 안뜰 / 주택 단면 | 텍스트로 영상 생성 | — |
| [미니어처와 초현실 · 7](docs/PROMPT_INDEX.md#09-miniature-and-surreal) | 찻잔 나룻배 / 서랍 속 빗속 풍경 / 종이 달 | 텍스트로 영상 생성 / 이미지로 영상 생성 | [허니 로프 — 미니어처 빵집 이야기](#case-honey-loaf) |
| [패션과 퍼포먼스 · 6](docs/PROMPT_INDEX.md#10-fashion-and-performance) | 치맛자락 / 망토 / 옷깃 투사 / 춤 동작 | 텍스트로 영상 생성 | — |

[이미지 예제](#featured-prompts) · [SeaImagine에서 만들기](#create-with-seaimagine)

<a id="visual-index"></a>

<a id="featured-prompts"></a>

## 복사하고 바꿔 쓸 수 있는 이미지 프롬프트

8개 예제에 전체 프롬프트와 시작 프레임 이미지를 제공합니다. 이미지는 구상용이며 검증된 영상 결과가 아닙니다.

출처가 Flaq AI로 표시된 다섯 예제는 원래 길이와 해상도를 유지합니다. 나머지 세 예제는 SeaImagine의 현재 옵션에 맞춰 작성했습니다. 원본 예제를 SeaImagine에서 사용할 때는 5/10/15초와 480p/720p를 선택하고 동작의 시간 배분을 다시 정하세요.

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. 바다 유리병 — 조건을 통제하며 움직임 비교하기

![바다 유리병 — 조건을 통제하며 움직임 비교하기](assets/seaimagine-sea-glass-bottle.webp)

**이미지로 영상 만들기 설정:** 5s · 16:9 · 720p · [시작 프레임 — 열어서 저장](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/ko-KR/sea-glass-bottle.txt)

```text
밝은 돌 표면 위에 놓인 반투명 무광 바다 유리병 하나, 원통형 뚜껑,
인쇄가 없는 빈 앞면, 액체 높이, 수평선, 부드러운 측면광을 유지한다. 병은 절대 움직이지 않는다.
5초 동안 카메라를 오른쪽으로 천천히 이동하며 이동 거리는 병 하나의 너비를 넘지 않는다.
작은 물방울 하나가 병 앞면을 따라 내려가 바닥에서 멈춘다. 배경의 바닷물결은 초점이 흐린 상태에서 부드럽게 움직인다.
반사는 카메라와 광원의 위치에 맞게 일관성을 유지한다.
소리: 멀리서 들리는 파도 소리만 넣는다. 음악, 목소리, 유리 충돌음, 과장된 물 튀는 소리는 없다.
컷 전환이나 줌은 없다. 병의 윤곽, 뚜껑 정렬, 유리 질감, 사물 개수를 유지한다.
로고 생성, 액체 높이 변화, 가장자리 휘어짐, 사물 떠오름, 새 소품 추가를 피한다.
마지막 1초는 안정된 화면을 유지한다.
```

[분류 색인으로 돌아가기](#find-the-right-prompt)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. 블루 루트 — 비 내리는 시장의 배달원 추적 숏

![블루 루트 — 비 내리는 시장의 배달원 추적 숏](assets/rainy-market-courier-video.webp)

**이미지로 영상 만들기 설정:** 10s · 16:9 · 1080p · [시작 프레임 — 열어서 저장](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/ko-KR/blue-route.txt)

[출처: Flaq AI](docs/ATTRIBUTION.md)

```text
제공된 배달원, 코발트색 전기 오토바이, 화물 상자, 고가 시장, 반투명 차양, 젖은 강철 통로, 조명, 밤의 색상을 유지한다. 무게, 타이어 접지력, 비, 서스펜션이 설득력 있게 느껴지는 현실적인 낮은 시점의 연속 추적 숏 하나를 만든다.

0–3초: 오토바이가 원래 자세에서 부드럽게 가속한다. 뒷바퀴가 얇은 부채꼴 물보라를 일으키고, 배수 이음매를 지날 때 서스펜션이 눌린다. 카메라는 바퀴 높이에서 오토바이 옆의 약간 뒤쪽을 같은 속도로 따라가며 심하게 흔들리지 않는다.

3–7초: 배달원이 몸을 기울여 넓은 왼쪽 커브를 돈다. 차양이 바람에 휘고, 음식 노점에서 김이 흘러나오며, 따뜻한 현장 조명이 젖은 반사면에 부드러운 빛줄기를 만든다. 두 바퀴는 둥근 형태로 지면에 닿아 있어야 한다.

7–10초: 오토바이가 바로 서서 시장의 더 밝고 열린 구역으로 향한다. 카메라가 반 미터 뒤처져 앞쪽 길을 드러낸 뒤 안정된 마지막 화면을 유지한다.

소리: 현실적인 전기 모터의 높은 구동음, 물보라, 차양에 떨어지는 비, 작은 시장 사람 소리, 한 번의 서스펜션 충격음. 배경 음악, 대사, 사이렌, 폭발은 없다.

연속성 고정: 운전자 옷, 헬멧, 오토바이 형태, 화물 상자, 파란 패널, 시장 배치를 정확히 유지한다. 차량 변형, 바퀴 왜곡, 충돌, 무기, 읽을 수 있는 간판, 로고, 순간 이동 카메라, 불가능한 속도 변화는 없다.
```

[분류 색인으로 돌아가기](#find-the-right-prompt)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. 허니 로프 — 미니어처 빵집 이야기

![허니 로프 — 미니어처 빵집 이야기](assets/pear-bakery-miniature-video.webp)

**이미지로 영상 만들기 설정:** 9s · 16:9 · 1080p · [시작 프레임 — 열어서 저장](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/ko-KR/honey-loaf.txt)

[출처: Flaq AI](docs/ATTRIBUTION.md)

```text
배 모양 집의 빵집, 미니어처 제빵사 세 명, 의상, 얼굴, 꿀빵, 오븐, 창문, 이끼, 클로버, 달, 손으로 만질 수 있을 듯한 스톱모션 재료, 따뜻하고 차가운 색의 대비를 유지한다.

0–3초: 제공된 넓은 구도에서 미세한 수작업 스톱모션 리듬으로 시작한다. 두 제빵사가 따뜻한 꿀빵을 함께 들어 올리며 손은 나무판에 붙어 있다. 작은 밀가루 먼지가 피고, 오븐 불이 깜박이며, 세 번째 제빵사가 판매 창을 연다.

3–7초: 두 사람이 창문을 향해 조심스럽게 발을 맞춰 네 걸음 걷는다. 빵에는 실제 같은 무게가 있어 둘 사이에서 약간 처진다. 바깥에서는 클로버 잎 하나에서 이슬 한 방울이 떨어지고 반딧불이 두 마리가 서로 다른 깊이에서 지나간다. 카메라가 오른쪽으로 부드럽게 5도 돌아간다.

7–9초: 나무판을 카운터 위로 밀어 올리고 안도한 미소를 주고받으며, 오븐 빛이 잔잔해진다. 세 인물이 모두 보이고 빵이 중앙에 오도록 끝낸다.

소리: 나무 위의 작은 발소리, 오븐의 부드러운 타닥거림, 판자 삐걱거림, 희미한 밤벌레, 판매 창의 작은 종소리 한 번. 대사, 내레이션, 음악, 글자는 없다.

연속성 고정: 인물 수, 얼굴 디자인, 크기 비율, 옷 색, 배 모양, 실내 배치, 수공예 질감을 유지한다. 추가 제빵사, 번들거리는 컴퓨터 그래픽, 고무 같은 팔다리, 떠 있는 소품, 녹는 빵, 컷 전환, 로고, 유명 시리즈를 닮은 캐릭터 디자인은 없다.
```

[분류 색인으로 돌아가기](#find-the-right-prompt)

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. 항구에서의 재회 — 하나의 감정 변화에 집중하기

![항구에서의 재회 — 하나의 감정 변화에 집중하기](assets/seaimagine-harbor-reunion.webp)

**이미지로 영상 만들기 설정:** 10s · 16:9 · 720p · [시작 프레임 — 열어서 저장](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/ko-KR/harbor-reunion.txt)

```text
제공된 이미지 속 성인 두 명, 각자의 얼굴, 남색과 크림색 옷, 나무 부두, 부드러운 아침 빛을 유지한다.
두 사람을 계속 같은 미디엄 와이드 구도 안에 둔다.
0–3초: 왼쪽 사람이 도착한 친구를 알아보고 한 걸음 작게 앞으로 나온다.
어깨의 긴장이 풀리고, 친구는 잔잔한 미소로 답한다. 손은 보이게 두고 자연스럽게 힘을 뺀다.
3–7초: 왼쪽 사람이 자연스러운 한국어로 “왔구나.”라고 말한다. 친구는 한 번 고개를 끄덕인다.
대사는 담담하게 말하며 울거나 과장된 표정을 짓지 않는다.
7–10초: 두 사람 모두 정박한 배를 바라본다. 다음 숏으로 연결할 수 있도록 마지막 1초는 화면을 유지한다.
카메라: 한 번만 부드럽게 다가간다. 역방향 숏이나 컷 전환은 넣지 않는다.
소리: 가까이서 또렷하게 들리는 대사, 잔잔한 항구 물소리, 멀리서 들리는 갈매기 소리. 음악이나 자막은 없다.
두 사람의 정체성, 옷, 부두 구조, 배의 위치, 아침 빛의 방향을 고정한다.
인물 추가, 과장된 몸짓, 과도한 얼굴 보정, 손가락 추가, 카메라의 갑작스러운 도약을 피한다.
```

[분류 색인으로 돌아가기](#find-the-right-prompt)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. 첫 모금 — 자연스러운 카페 체험 리뷰

<a href="assets/cozy-cafe-ugc-video.webp"><img src="assets/cozy-cafe-ugc-video.webp" width="480" alt="첫 모금 — 자연스러운 카페 체험 리뷰"></a>

**이미지로 영상 만들기 설정:** 10s · 9:16 · 1080p · [시작 프레임 — 열어서 저장](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/ko-KR/first-sip.txt)

[출처: Flaq AI](docs/ATTRIBUTION.md)

```text
제공된 카페 사진을 솔직한 크리에이터 체험 리뷰로 움직이며 손으로 든 카메라 느낌을 살린다. 인물의 얼굴, 나이, 피부 질감, 머리카락, 이끼색 스웨터, 컵, 페이스트리, 창문, 테이블 배치를 유지한다.

0–3초: 자연스럽고 부드러운 핸드헬드 흔들림. 여성이 한 모금을 마친 뒤 도자기 컵을 약 10센티미터 내리고, 살짝 웃으며 숨을 내쉬고, 창밖에서 카메라로 시선을 돌린다. 김이 피어오르고 뒤쪽 유리의 빗물 자국이 천천히 합쳐진다.

3–8초: 편안하고 자연스러운 한국어로 “부드럽고 많이 달지 않아요. 귀리 맛도 제대로 느껴져요.”라고 말한다. 일상적인 말투로 “달지 않아요” 뒤에서 아주 잠깐 쉰다. 입 움직임을 대사에 정확히 맞추고 손에 든 컵을 안정적으로 유지한다.

8–10초: 여성이 만족스럽게 작게 고개를 끄덕이고, 카메라가 안정되면서 페이스트리를 내려다본다.

소리: 가까이서 스마트폰으로 녹음한 목소리, 조용한 카페 공간음, 멀리서 들리는 우유 스팀기, 부드러운 빗소리, 도자기 컵이 닿는 소리. 목소리를 앞에 두고 환경음은 낮게 유지한다. 배경 음악과 자막은 없다.

연속성 고정: 얼굴 미화, 옷 변경, 손가락 추가, 컵이나 음식 재설계, 배경 인물 출현, 로고, 과장된 인플루언서 몸짓은 없다.
```

[분류 색인으로 돌아가기](#find-the-right-prompt)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. 새벽의 염전 철도 — 여행 다큐멘터리

![새벽의 염전 철도 — 여행 다큐멘터리](assets/coastal-salt-train-documentary.webp)

**이미지로 영상 만들기 설정:** 12s · 16:9 · 1080p · [시작 프레임 — 열어서 저장](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/ko-KR/salt-line.txt)

[출처: Flaq AI](docs/ATTRIBUTION.md)

```text
제공된 해안 염전 장면을 노동자를 존중하는 관찰형 여행 다큐멘터리로 움직인다. 작업자 두 명, 크림색과 황토색 기차, 염전, 석회암 언덕, 건물, 바다, 일출 방향, 차분한 필름 색상을 유지한다.

0–4초: 고정된 넓은 화면. 작업자가 수로 점검을 계속한다. 한 명은 얕은 소금물 속으로 나무 도구를 움직이고 다른 한 명은 칸막이를 잡아 준다. 물결은 도구와 아침 바람에 반응한다. 중경에서 기차가 차분한 속도로 다가온다.

4–9초: 카메라가 기차를 따라 천천히 오른쪽으로 팬한다. 바퀴는 레일에 맞추고 객차 간격과 창문 배열의 리듬은 일정하게 유지한다. 얇은 해무가 기차 뒤로 흐르며 햇빛이 전경의 소금 결정에 점차 닿는다.

9–12초: 기차가 해안 쪽으로 지나가고 카메라 팬이 부드럽게 멈춘다. 작업자 한 명이 일어나 자연스럽게 기지개를 켜고 철로를 바라본다. 편집 지점으로 쓸 수 있도록 마지막 2초를 유지한다.

소리: 부드러운 전기철도 구동음, 규칙적인 바퀴 이음매 소리, 얕은 물 위를 지나는 바람, 먼 갈매기, 소금물 속을 움직이는 나무 도구. 내레이션, 음악, 군중 소리, 극적인 경적은 없다.

연속성 고정: 현실적인 노동 동작, 안정된 신체 구조, 고정된 풍경, 변하지 않는 기차 디자인, 타당한 반사와 물의 물리적 움직임. 현대 도시 스카이라인, 연출된 관광객, 새 건물, 로고, 읽을 수 있는 간판, 지나치게 채도 높은 엽서 색감, 타임랩스 하늘은 없다.
```

[분류 색인으로 돌아가기](#find-the-right-prompt)

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. 해안 엽서 — 구성을 정한 이미지를 움직이기

<a href="assets/seaimagine-coastal-postcard.webp"><img src="assets/seaimagine-coastal-postcard.webp" width="480" alt="해안 엽서 — 구성을 정한 이미지를 움직이기"></a>

**이미지로 영상 만들기 설정:** 5s · 9:16 · 720p · [시작 프레임 — 열어서 저장](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/ko-KR/coastal-postcard.txt)

```text
세 칸으로 구성된 해안 엽서를 레이아웃이나 테두리를 바꾸지 않고 움직인다.
모든 사물과 색을 그대로 유지한다. 위 칸에서는 컵에서 가느다란 김 한 줄기가 올라온다.
가운데 칸에서는 항구 물결이 잔잔하게 일고 수면에 햇빛이 반짝인다.
아래 칸에서는 원래 있던 종이의 한쪽 모서리만 산들바람에 살짝 들렸다가 내려앉는다.
각 움직임은 해당 칸 안에만 머문다. 5초 내내 모든 칸이 보이게 한다.
카메라: 고정. 줌, 팬, 컷 전환, 칸 사이의 장면 전환은 없다.
소리: 잔잔한 물소리와 종이가 가볍게 바스락거리는 소리. 대사, 음악, 자막, 추가 글자는 없다.
컵 손잡이, 창틀, 지도 표시, 각 칸의 크기, 읽는 순서를 유지한다.
칸이 합쳐지거나 새 장면이 생기지 않게 하고, 글자를 다시 그리거나 사물이 테두리를 넘어 움직이지 않게 한다.
마지막에는 종이 모서리가 내려앉고 원래 구도가 온전히 유지된다.
```

[분류 색인으로 돌아가기](#find-the-right-prompt)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. 시트러스 헤일로 — 고급 향수 제품 영상

![시트러스 헤일로 — 고급 향수 제품 영상](assets/citrus-fragrance-product-video.webp)

**이미지로 영상 만들기 설정:** 8s · 16:9 · 1080p · [시작 프레임 — 열어서 저장](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/ko-KR/citrus-halo.txt)

[출처: Flaq AI](docs/ATTRIBUTION.md)

```text
제공된 병 디자인, 유리 비율, 뚜껑, 석회암 받침대, 자몽 껍질, 따뜻한 아이보리색 세트, 황금빛 측면광을 유지한다. 우아한 8초 제품 영상을 만든다.

0–2.5초: 거의 고정된 매크로 구도로 시작한다. 카메라는 아주 천천히 앞으로 이동한다. 맺힌 물방울이 빛을 받고, 두 방울이 차가운 유리 표면을 자연스럽게 흘러내린다. 자몽 껍질은 조절된 스튜디오 바람에 실리듯 받침대에서 떠오른다.

2.5–6초: 껍질이 병 주위를 우아한 나선으로 한 바퀴 돈다. 뚜껑에 닿거나 가리지 않는다. 미세한 감귤 안개 입자가 역광을 지난다. 두꺼운 유리 안에서 굴절과 집광 무늬가 물리적으로 자연스럽게 움직인다. 병 자체는 완전히 단단하게 유지된다.

6–8초: 껍질이 원래의 곡선 모양으로 내려앉고, 카메라가 부드럽게 멈춘다. 밝은 정반사 하이라이트가 병 가장자리를 한 번 지난다. 깔끔한 제품 대표 화면으로 끝낸다.

소리: 가까운 스튜디오 효과음만 사용한다. 띠 모양 껍질의 부드러운 움직임, 또렷한 물방울 소리 두 번, 섬세한 유리 울림. 목소리, 음악, 글자는 없다.

연속성 고정: 병 윤곽, 뚜껑의 각 면, 액체 높이, 받침대, 색상, 배경 아치를 바꾸지 않는다. 라벨, 로고, 추가 과일, 떠 있는 병, 형태 흔들림, 카메라 점프, 인위적인 반짝임 폭발은 없다.
```

[분류 색인으로 돌아가기](#find-the-right-prompt)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

## 선택한 장면을 SeaImagine에서 만들어 보세요

위의 유리병 제품 영상, 항구 대화, 움직이는 엽서 중 하나를 골라 이미지와 프롬프트 전문을 SeaImagine의 Grok Imagine 1.5에서 활용해 보세요. 제품 영상에서는 재질을, 인물 영상에서는 연기를, 레이아웃 애니메이션에서는 구도를 살펴볼 수 있습니다.

[제품의 질감](#case-sea-glass-bottle) · [인물 대화](#case-harbor-reunion) · [레이아웃 애니메이션](#case-coastal-postcard)

[![SeaImagine · Grok Imagine 1.5](assets/seaimagine-interface.jpg)](https://seaimagine.com/ko/model/grok-imagine-1-5/)

실제 화면: 유리병 프롬프트 입력 완료, 720p · 5초 · 16:9. 시작 이미지는 아직 업로드하지 않았으며 영상도 생성하지 않았습니다.

**[SeaImagine으로 이 장면 만들기](https://seaimagine.com/ko/model/grok-imagine-1-5/)**

<a id="learn-from-official-and-community-examples"></a>

<a id="writing-guide"></a>

<a id="공통-다국어-테스트-도자기-조명-공방"></a>

<a id="빠른-작성-원칙"></a>

<a id="전체-프롬프트-라이브러리"></a>

## 참고 자료

[작성 참고](docs/guides/ko-KR.md) · [설정 및 조작 참고](docs/workflows/ko-KR.md) · [SeaImagine](https://seaimagine.com/ko/model/grok-imagine-1-5/)

[출처](docs/COMMUNITY.md) · [X / YouTube](docs/SOCIAL_INSPIRATION.md)

<a id="multilingual-prompts"></a>

## 모음과 출처

영어 프롬프트 총 62개: 원본 저장소의 35개와 자체 작성 27개입니다. 최신 24개는 소셜 미디어 소재를 참고해 새로 작성했으며 생성 결과는 검증하지 않았습니다. 번역은 새 장면으로 집계하지 않습니다.

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/ko/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
