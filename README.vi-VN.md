# Thư viện câu lệnh Grok Imagine 1.5 — Tiếng Việt

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 65 câu lệnh, trong đó 11 ví dụ có hình được cung cấp bằng 15 ngôn ngữ. Duyệt theo danh mục và sao chép toàn bộ câu lệnh.

![Grok Imagine 1.5 — Sổ câu lệnh mở ra với giày, tàu điện và cá voi giấy trong cùng một khung cảnh](assets/seaimagine-grok-hero.webp)

Chuyển thể từ [Flaq AI](https://github.com/flaqai/awesome-grok-imagine), do SeaImagine duy trì theo giấy phép [MIT](LICENSE) và độc lập với xAI. Ảnh ý tưởng không thể hiện kết quả thử nghiệm thực tế bằng Grok.

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## Mục lục danh mục

[Xem thêm câu lệnh (tiếng Anh) · 65](docs/PROMPT_INDEX.md)

| Danh mục | Cảnh | Chế độ | Ví dụ |
| --- | --- | --- | --- |
| [Sản phẩm và quảng cáo · 8](docs/PROMPT_INDEX.md#01-ads-and-products) | Cận cảnh mỹ phẩm / cà phê / trang sức / quảng cáo ứng dụng | Văn bản thành video / Ảnh thành video / Ảnh tham chiếu thành video | [Chai thủy tinh biển — so sánh chuyển động có kiểm soát biến số](#case-sea-glass-bottle) · [Vầng sáng cam chanh — phim sản phẩm nước hoa cao cấp](#case-citrus-halo) |
| [Kể chuyện điện ảnh · 7](docs/PROMPT_INDEX.md#02-cinematic-storytelling) | Hành động / lãng mạn / hồi hộp / khoa học viễn tưởng / hoạt hình | Văn bản thành video / Ảnh thành video / Kéo dài video | [Tuyến đường xanh — cảnh bám theo người giao hàng ở chợ mưa](#case-blue-route) |
| [Mạng xã hội và đời sống · 8](docs/PROMPT_INDEX.md#03-social-ugc) | Chia sẻ trải nghiệm / ẩm thực / thể hình / phỏng vấn | Văn bản thành video / Ảnh thành video / Ảnh tham chiếu thành video | [Ngụm đầu tiên — đánh giá quán cà phê tự nhiên](#case-first-sip) · [Tuyến đường muối lúc bình minh — phim tài liệu du lịch](#case-salt-line) |
| [Nhân vật và hội thoại · 7](docs/PROMPT_INDEX.md#04-characters-and-references) | Nhân vật / trang phục / hội thoại / cảnh đông người | Ảnh tham chiếu thành video / Ảnh thành video | [Bánh răng cuối — cuộc đối thoại của người sửa đồng hồ](#case-clockwork-dialogue) |
| [Biến đổi hình ảnh và nối tiếp · 7](docs/PROMPT_INDEX.md#05-editing-and-extension) | Đổi thời tiết / xóa chi tiết / đổi phong cách / nối tiếp | Chỉnh sửa video / Kéo dài video / Ảnh thành video | [Mưa vào hành lang — chuyển biến thời tiết liền mạch](#case-rainlit-arcade) |
| [Chất liệu và âm thanh thư giãn · 7](docs/PROMPT_INDEX.md#07-satisfying-materials) | Ép cát / lá đồng / giọt nước / tạo vân cẩm thạch | Văn bản thành video / Ảnh thành video | [Vườn hổ phách — một lát trong suốt](#case-amber-orchard) |
| [Không gian và kiến trúc · 7](docs/PROMPT_INDEX.md#08-spaces-and-transformations) | Nội thất mở ra / sân trong / mặt cắt ngôi nhà | Văn bản thành video / Ảnh thành video | [Mở giếng trời — nhà kính cơ khí](#case-unfolding-atrium) |
| [Thế giới thu nhỏ và siêu thực · 7](docs/PROMPT_INDEX.md#09-miniature-and-surreal) | Phà trong tách trà / mưa trong ngăn kéo / mặt trăng giấy | Văn bản thành video / Ảnh thành video | [Ổ bánh mật ong — câu chuyện tiệm bánh tí hon](#case-honey-loaf) |
| [Thời trang và trình diễn · 7](docs/PROMPT_INDEX.md#10-fashion-and-performance) | Tà váy / áo choàng / hình chiếu trên cổ áo / bước nhảy | Văn bản thành video / Ảnh thành video | [Quỹ đạo cobalt — một vòng thời trang cao cấp](#case-cobalt-orbit) |

[Ví dụ có hình](#featured-prompts) · [Sáng tạo với SeaImagine](#create-with-seaimagine)

<a id="visual-index"></a>

<a id="featured-prompts"></a>

## Câu lệnh có hình để sao chép và điều chỉnh

Cả 11 ví dụ có prompt đầy đủ và ảnh tham chiếu. Ảnh thể hiện ý tưởng, không phải kết quả video đã kiểm chứng.

Năm ví dụ ghi nguồn Flaq AI giữ nguyên thời lượng và độ phân giải gốc; sáu ví dụ còn lại được viết theo các tùy chọn hiện tại của SeaImagine. Khi dùng ví dụ gốc trên SeaImagine, hãy chọn 5/10/15 giây và 480p/720p, rồi sắp xếp lại thời gian cho các hành động.

<a id="case-sea-glass-bottle"></a>

<a id="seaimagine-sea-glass-bottle"></a>

### 1. Chai thủy tinh biển — so sánh chuyển động có kiểm soát biến số

![Chai thủy tinh biển — so sánh chuyển động có kiểm soát biến số](assets/seaimagine-sea-glass-bottle.webp)

**Thiết lập tạo video từ ảnh:** 5s · 16:9 · 720p · [Khung hình đầu — mở và lưu](assets/seaimagine-sea-glass-bottle.webp) · [TXT](prompts/text/vi-VN/sea-glass-bottle.txt)

```text
Giữ nguyên một chai thủy tinh biển mờ duy nhất trên mặt đá màu nhạt, nắp hình trụ,
mặt trước trống không in chữ, mức chất lỏng, đường chân trời và ánh sáng bên dịu. Chai không bao giờ di chuyển.
Trong năm giây, cho máy quay trượt chậm sang phải, không quá bề ngang một chai.
Một giọt nước nhỏ chảy xuống mặt trước và dừng ở đáy. Sóng biển ở hậu cảnh chuyển động nhẹ trong vùng ngoài nét.
Giữ phản xạ nhất quán với máy quay và nguồn sáng.
Âm thanh: chỉ có tiếng sóng từ xa; không nhạc, giọng nói, tiếng va chạm thủy tinh hoặc tiếng nước bắn quá mức.
Không cắt cảnh hay thu phóng. Giữ nguyên đường bao chai, vị trí thẳng hàng của nắp, chất liệu thủy tinh và số vật thể.
Tránh tạo logo, thay đổi mức chất lỏng, làm cong mép, vật thể lơ lửng hoặc thêm đạo cụ.
Giữ khung hình ổn định trong giây cuối.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-blue-route"></a>

<a id="3-blue-route--rain-market-courier-tracking-shot"></a>

### 2. Tuyến đường xanh — cảnh bám theo người giao hàng ở chợ mưa

![Tuyến đường xanh — cảnh bám theo người giao hàng ở chợ mưa](assets/rainy-market-courier-video.webp)

**Thiết lập tạo video từ ảnh:** 10s · 16:9 · 1080p · [Khung hình đầu — mở và lưu](assets/rainy-market-courier-video.webp) · [TXT](prompts/text/vi-VN/blue-route.txt)

[Nguồn: Flaq AI](docs/ATTRIBUTION.md)

```text
Giữ nguyên người giao hàng, xe máy điện xanh cobalt, thùng hàng, khu chợ trên cao, mái che xuyên sáng, lối đi thép ướt, ánh sáng và bảng màu ban đêm. Tạo một cảnh bám theo liên tục ở góc thấp, chân thực về khối lượng, độ bám lốp, mưa và hệ thống giảm xóc.

0–3s: xe tăng tốc êm từ tư thế sẵn có. Lốp sau đẩy một lớp nước mỏng hình quạt; giảm xóc nén khi qua khe thoát nước. Máy quay bám bên cạnh và hơi sau xe ở độ cao bánh, cùng tốc độ mà không rung mạnh.

3–7s: người giao hàng nghiêng qua một khúc cua trái rộng. Mái che cong theo gió, hơi nước cuộn từ quầy thức ăn và ánh đèn thật trong cảnh tạo vệt ấm dịu trong phản xạ mặt đường ướt. Giữ cả hai bánh tròn và tiếp xúc mặt đất.

7–10s: xe thẳng lại và đi về phần chợ sáng, thoáng hơn. Máy quay lùi lại nửa mét so với xe, lộ đường phía trước, rồi giữ khung hình kết ổn định.

Âm thanh: tiếng rít động cơ điện chân thực, nước bắn, mưa trên mái che, tiếng người trong chợ nhỏ và một tiếng giảm xóc va trầm. Không nhạc, đối thoại, còi báo động hoặc nổ.

Khóa tính liên tục: giữ chính xác trang phục người lái, mũ bảo hiểm, hình dạng xe, thùng hàng, tấm ốp xanh và bố cục chợ. Không xe biến hình, bánh méo, va chạm, vũ khí, biển đọc được, logo, máy quay dịch chuyển tức thời hoặc thay đổi tốc độ phi lý.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-honey-loaf"></a>

<a id="4-the-honey-loaf--miniature-bakery-story"></a>

### 3. Ổ bánh mật ong — câu chuyện tiệm bánh tí hon

![Ổ bánh mật ong — câu chuyện tiệm bánh tí hon](assets/pear-bakery-miniature-video.webp)

**Thiết lập tạo video từ ảnh:** 9s · 16:9 · 1080p · [Khung hình đầu — mở và lưu](assets/pear-bakery-miniature-video.webp) · [TXT](prompts/text/vi-VN/honey-loaf.txt)

[Nguồn: Flaq AI](docs/ATTRIBUTION.md)

```text
Giữ nguyên tiệm bánh trong ngôi nhà hình quả lê, ba thợ bánh tí hon, trang phục, khuôn mặt, ổ bánh mật ong, lò, cửa sổ, rêu, cỏ ba lá, mặt trăng, vật liệu hoạt hình chụp từng khung hình có cảm giác sờ được và tương phản màu ấm lạnh.

0–3s: bắt đầu với bố cục rộng đã cho, có nhịp hoạt hình chụp từng khung hình thủ công nhẹ. Hai thợ cùng nâng ổ bánh mật ong ấm; tay luôn tiếp xúc với tấm gỗ. Một ít bột bay lên, lửa lò lập lòe và người thứ ba mở cửa bán hàng.

3–7s: hai người bước bốn bước cẩn thận, đồng bộ về phía cửa. Ổ bánh có trọng lượng thuyết phục, hơi trĩu xuống giữa họ. Bên ngoài, một lá cỏ ba lá nhả một giọt sương và hai đom đóm trôi qua ở độ sâu khác nhau. Máy quay đi vòng nhẹ năm độ sang phải.

7–9s: họ trượt tấm gỗ lên quầy, mỉm cười nhẹ nhõm với nhau và ánh lò dịu lại. Kết thúc với cả ba nhân vật đều thấy rõ, ổ bánh ở giữa.

Âm thanh: bước chân nhỏ trên gỗ, lò tí tách nhẹ, tấm gỗ kẽo kẹt, côn trùng đêm khe khẽ và một tiếng chuông nhỏ ở cửa bán hàng. Không đối thoại, thuyết minh, nhạc hoặc chữ.

Khóa tính liên tục: giữ số nhân vật, thiết kế mặt, tỷ lệ, màu quần áo, hình quả lê, bố trí phòng và chất liệu thủ công. Không thêm thợ bánh, đồ họa máy tính bóng loáng, tay chân như cao su, đạo cụ lơ lửng, bánh chảy, cắt cảnh, logo hoặc thiết kế nhân vật giống loạt tác phẩm nổi tiếng.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-clockwork-dialogue"></a>

<a id="seaimagine-clockwork-dialogue"></a>

### 4. Bánh răng cuối — cuộc đối thoại của người sửa đồng hồ

![Bánh răng cuối — cuộc đối thoại của người sửa đồng hồ](assets/clockwork-dialogue.png)

**Thiết lập tạo video từ ảnh:** 10s · 16:9 · 720p · [Khung hình đầu — mở và lưu](assets/clockwork-dialogue.png) · [TXT](prompts/text/vi-VN/clockwork-dialogue.txt)

```text
Biến ảnh mẫu thành cảnh phim tiết chế dài 10 giây. Giữ hai thợ phục chế trưởng thành, đồng hồ thiên văn đồng thau mở, một bánh răng rời và đài quan sát dưới trăng. Người phụ nữ tóc ngắn mặc đồ xanh đậm ở bên trái; người đàn ông tóc bạc đeo tạp dề vàng đất ở bên phải. Khung hình từ thắt lưng trở lên qua bàn làm việc.

0–3g: giữ cảnh hai người, tiến máy gần như không nhận thấy. Cô nhìn đồng hồ, hỏi nhỏ bằng tiếng Việt: “Nó sẽ chạy đúng giờ chứ?” Ông nhìn cơ cấu đồng hồ. Chỉ cô nói, môi khớp lời. Đồng hồ đã tích tắc chậm và khẽ từ đầu.

3–7g: ông giữ tay thả lỏng, bất động, tập trung nghe đồng hồ một nhịp rồi đáp bằng tiếng Việt: “Giờ thì được rồi.” Chỉ môi ông chuyển động ở câu này. Ông không chạm bánh răng; nó luôn đứng yên. Bộ thoát thấy được tiếp tục dao động đều.

7–10g: cô nhìn từ đồng hồ sang ông, mỉm cười nhẹ nhõm. Ông đáp lại ánh mắt. Kết ở khoảng lặng chung, tiếng đồng hồ giữa họ và ánh trăng lạnh viền vai.

Âm thanh: lời thoại gần, khô; suốt cảnh là tích tắc nhẹ đều trong căn phòng rỗng. Không nhạc, lời chồng nhau hay tiếng bánh răng di chuyển.

Bánh răng luôn tách khỏi đồng hồ, không ai lắp hoặc xoay nó. Giữ cấu trúc bàn tay, ruột đồng hồ, trang phục, hướng mắt, vị trí trái/phải. Tích tắc không do cử chỉ kích hoạt. Không thêm dụng cụ hoặc bánh răng, phụ đề, cắt cảnh, cử chỉ quá mức.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-first-sip"></a>

<a id="2-first-sip--authentic-café-ugc-review"></a>

### 5. Ngụm đầu tiên — đánh giá quán cà phê tự nhiên

<a href="assets/cozy-cafe-ugc-video.webp"><img src="assets/cozy-cafe-ugc-video.webp" width="480" alt="Ngụm đầu tiên — đánh giá quán cà phê tự nhiên"></a>

**Thiết lập tạo video từ ảnh:** 10s · 9:16 · 1080p · [Khung hình đầu — mở và lưu](assets/cozy-cafe-ugc-video.webp) · [TXT](prompts/text/vi-VN/first-sip.txt)

[Nguồn: Flaq AI](docs/ATTRIBUTION.md)

```text
Làm chuyển động ảnh quán cà phê được cung cấp thành một bài đánh giá chân thực của người sáng tạo với máy quay cầm tay. Giữ nguyên khuôn mặt, tuổi, kết cấu da, tóc, áo len xanh rêu, cốc, bánh ngọt, cửa sổ và bố trí bàn.

0–3s: máy quay cầm tay trôi nhẹ tự nhiên. Cô ấy uống xong một ngụm, hạ cốc gốm khoảng mười centimét, thở ra với nụ cười nhỏ và chuyển mắt từ cửa sổ về máy quay. Hơi nước cuộn lên, các vệt mưa trên kính phía sau từ từ nhập vào nhau.

3–8s: cô ấy nói bằng tiếng Việt tự nhiên, thoải mái: “Béo mịn, không ngọt quá — mà còn cảm nhận rõ vị yến mạch nữa.” Giữ giọng trò chuyện đời thường, ngừng rất ngắn sau “ngọt quá”. Khớp chuyển động môi sát lời nói và giữ cốc ổn định trong tay.

8–10s: cô ấy gật nhẹ tỏ ý hài lòng rồi nhìn xuống bánh khi máy quay ổn định lại.

Âm thanh: giọng nói gần thu bằng điện thoại, nền âm thanh quán yên tĩnh, máy đánh sữa bằng hơi từ xa, mưa nhẹ và tiếng cốc gốm chạm bề mặt. Giọng nói ở phía trước, âm thanh môi trường nhỏ. Không nhạc nền và phụ đề.

Khóa tính liên tục: không làm đẹp khuôn mặt, đổi quần áo, thêm ngón tay, thiết kế lại cốc hoặc đồ ăn, người tự xuất hiện ở hậu cảnh, logo hay cử chỉ kiểu người nổi tiếng trên mạng quá mức.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-salt-line"></a>

<a id="5-salt-line-at-dawn--travel-documentary"></a>

### 6. Tuyến đường muối lúc bình minh — phim tài liệu du lịch

![Tuyến đường muối lúc bình minh — phim tài liệu du lịch](assets/coastal-salt-train-documentary.webp)

**Thiết lập tạo video từ ảnh:** 12s · 16:9 · 1080p · [Khung hình đầu — mở và lưu](assets/coastal-salt-train-documentary.webp) · [TXT](prompts/text/vi-VN/salt-line.txt)

[Nguồn: Flaq AI](docs/ATTRIBUTION.md)

```text
Làm chuyển động cảnh ruộng muối ven biển đã cho thành phim tài liệu du lịch quan sát, tôn trọng người lao động. Giữ nguyên hai công nhân, tàu màu kem và vàng đất, ô muối, đồi đá vôi, nhà, biển, hướng bình minh và bảng màu phim dịu.

0–4s: khung rộng cố định. Công nhân tiếp tục kiểm tra mương: một người đưa dụng cụ gỗ qua nước muối nông, người kia giữ vách ngăn. Gợn nước phản ứng với dụng cụ và gió sớm. Tàu tiến đến với tốc độ vừa phải ở trung cảnh.

4–9s: máy quay lia chậm sang phải theo tàu. Bánh luôn thẳng với ray; khoảng cách toa và nhịp cửa sổ nhất quán. Một màn sương biển mỏng trôi phía sau trong khi nắng dần bắt vào tinh thể muối ở tiền cảnh.

9–12s: tàu đi qua về hướng bờ biển và máy quay nhẹ nhàng ngừng lia. Một công nhân đứng lên, vươn người tự nhiên và nhìn về đường ray. Giữ hai giây cuối làm điểm dựng.

Âm thanh: tiếng ù điện nhẹ của tàu, bánh qua mối nối đều nhịp, gió trên nước nông, hải âu xa và dụng cụ gỗ chuyển động trong nước muối. Không thuyết minh, nhạc, đám đông hoặc còi kịch tính.

Khóa tính liên tục: lao động chân thực, giải phẫu ổn định, cảnh quan cố định, thiết kế tàu không đổi, phản xạ và vật lý nước hợp lý. Không đường chân trời đô thị hiện đại, khách du lịch tạo dáng dàn dựng, nhà mới, logo, biển đọc được, màu bưu thiếp quá bão hòa hoặc bầu trời tua nhanh.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-rainlit-arcade"></a>

<a id="seaimagine-rainlit-arcade"></a>

### 7. Mưa vào hành lang — chuyển biến thời tiết liền mạch

![Mưa vào hành lang — chuyển biến thời tiết liền mạch](assets/rainlit-arcade.png)

**Thiết lập tạo video từ ảnh:** 10s · 16:9 · 720p · [Khung hình đầu — mở và lưu](assets/rainlit-arcade.png) · [TXT](prompts/text/vi-VN/rainlit-arcade.txt)

```text
Dùng hành lang Art Deco vắng người làm đúng khung đầu cho cảnh thời tiết 10 giây. Giữ gạch xanh đậm, nẹp đồng, sàn terrazzo, dãy vòm, đèn ấm bên trái. Cửa ra phố xa vẫn xanh chạng vạng. Sàn khởi đầu khô, giữ phản chiếu dịu vốn có trên đá bóng; máy quay từ trong hướng ra cửa.

0–3g: bố cục kiến trúc cố định, không lia hay zoom. Ngoài ngưỡng xa, gió thổi mưa chéo qua phố. Những giọt đầu vượt cửa, chỉ làm sẫm terrazzo sát ngưỡng. Tiền cảnh hoàn toàn khô.

3–7g: gió mạnh lên, đưa mưa nhỏ sâu hơn cùng hướng. Mép ướt không đều tiến từ xa tới giữa; giọt mới nối rõ vào mảng ướt sẵn. Vũng nhỏ nông hình thành trong vùng ướt. Giữ phản chiếu dịu ban đầu; ở vùng ướt, mưa phá phản chiếu đèn trái thành vệt sáng ấm rung động.

7–10g: đợt bụi nước cuối tới gần giữa sàn rồi chậm lại. Dải gần máy nhất vẫn khô. Mưa dịu; vòng gợn chồng nhau giảm trong vũng nông, phản chiếu ấm lắng lại. Giữ các vòm nguyên dạng trước cửa xanh.

Âm thanh: mưa ngoài trước, rồi tiếng giọt gõ đá gần dần, một luồng gió trầm, tiếng vọng hành lang nhẹ. Không sấm, nhạc, tiếng người.

Đường nước tới phải liên tục và thấy được: không cả sàn bỗng bóng ướt, không vũng xuất hiện trước mép ướt. Nước nông, đèn ổn định, máy ngang, đường kiến trúc cứng. Không người, cây mới, biển mới, chớp, ngập, cắt cảnh, thay đổi bề mặt.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-amber-orchard"></a>

<a id="seaimagine-amber-orchard"></a>

### 8. Vườn hổ phách — một lát trong suốt

![Vườn hổ phách — một lát trong suốt](assets/amber-orchard.png)

**Thiết lập tạo video từ ảnh:** 10s · 16:9 · 720p · [Khung hình đầu — mở và lưu](assets/amber-orchard.png) · [TXT](prompts/text/vi-VN/amber-orchard.txt)

```text
Tạo cận cảnh chất liệu siêu thực 10 giây từ ảnh mẫu. Giữ quả lê thủy tinh hổ phách trong suốt trên đĩa đá đen, bọt khí nhỏ và sợi vàng mảnh bên trong. Một dao hẹp vào từ phải, mũi chạm sườn phải quả lê như ảnh mẫu. Không mặt hoặc tay. Lê là vật kính tưởng tượng cứng nhưng cắt được gọn: chất liệu phi thực có chủ ý, hình học phải nhất quán.

0–3g: góc macro chéo ba phần tư cố định, thấy toàn bộ lê và đĩa. Ánh sáng bên ấm lộ sợi bên trong. Dao rút khỏi điểm chạm, nâng lên trên mặt cắt phải, rồi canh một nhát dọc lấy lát ngoài mỏng, cuống vẫn trên thân lớn.

3–7g: một nhát xuống liên tục. Lưỡi qua sườn phải tới khi vừa chạm đĩa. Một mặt cắt sạch tiến cùng lưỡi; chỉ một lát tách ra. Thân lê đứng thẳng. Lát nghiêng nhẹ ra phải, lộ mặt hổ phách nhẵn, rồi tựa vào đĩa không vỡ.

7–10g: nhấc dao thẳng lên khỏi lê rồi giữ yên. Máy chỉ tiến chút để thấy hai mặt cắt khớp nhau. Kết với thân lớn, một lát rời và dao đều rõ trong khung.

Âm thanh: tiếng tinh thể cọ mảnh khi cắt, một tiếng lanh canh sáng khi lát chạm đá, dư âm tự nhiên ngắn. Không nhạc hoặc lời.

Bọt và sợi cố định trong từng khối rắn. Giữ độ trong, dáng lê ngoài chỗ cắt, vị trí đĩa. Không nhát thứ hai, lát nhân đôi, mảnh vụn, nhân lỏng, tan chảy, sợi mới, mảnh lơ lửng, cắt cảnh.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-unfolding-atrium"></a>

<a id="seaimagine-unfolding-atrium"></a>

### 9. Mở giếng trời — nhà kính cơ khí

![Mở giếng trời — nhà kính cơ khí](assets/unfolding-atrium.png)

**Thiết lập tạo video từ ảnh:** 10s · 16:9 · 720p · [Khung hình đầu — mở và lưu](assets/unfolding-atrium.png) · [TXT](prompts/text/vi-VN/unfolding-atrium.txt)

```text
Biến mô hình kiến trúc gỗ óc chó và đồng thau thành cảnh mở cơ cấu chính xác 10 giây. Giữ bệ đá xám, thang mini, dương xỉ dày. Mái kính cong gồm đúng hai nửa cong gắn vào trục bản lề cố định trên sống mái giữa. Ban đầu cả hai đóng; nội thất đã thấy qua kính.

0–3g: toàn mô hình ở góc chéo ba phần tư gần. Ánh ấm lướt vân gỗ và ống bản lề đồng nhỏ. Máy bắt đầu nâng chậm liên tục, nhìn nhẹ xuống sân trong. Mái đóng một nhịp rồi mép hiên ngoài bắt đầu nâng; sống mái không tách.

3–7g: hai cánh quay lên cùng tốc độ đều quanh bản lề sống mái cố định. Mép hiên ngoài nâng lên, lộ sân có cây phía dưới. Chuyển động cơ khí kiểm soát; mỗi cánh giữ độ cong và khung đồng cứng. Máy nâng vừa đủ thấy khoảng thang; toàn bệ luôn trong khung.

7–10g: cánh giảm tốc tới góc mở bằng nhau, dừng không nảy. Giữ tán dương xỉ và thang mini trong khung mái mở. Một mảng sáng ngày dịu vào sâu hơn; cây không động. Kết với cấu trúc mở rõ ràng.

Âm thanh: tiếng bánh răng nhỏ đồng bộ mái, hai tiếng chốt dừng gần đồng thời, rồi nền phòng yên. Không nhạc hay giọng nói.

Giữ đúng hai cánh, trục bản lề sống mái cố định, cùng nội thất. Không gì mọc, mở ra từ khoảng trống hoặc đổi tỷ lệ. Không tấm mái trượt, kính rời, kim loại uốn, phòng mới, bệ mở, người, cắt cảnh.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-cobalt-orbit"></a>

<a id="seaimagine-cobalt-orbit"></a>

### 10. Quỹ đạo cobalt — một vòng thời trang cao cấp

![Quỹ đạo cobalt — một vòng thời trang cao cấp](assets/cobalt-orbit.png)

**Thiết lập tạo video từ ảnh:** 10s · 16:9 · 720p · [Khung hình đầu — mở và lưu](assets/cobalt-orbit.png) · [TXT](prompts/text/vi-VN/cobalt-orbit.txt)

```text
Biến người mẫu trưởng thành hư cấu trong ảnh thành chân dung thời trang toàn thân 10 giây. Giữ tóc đen ngắn, khuyên đĩa đồng, váy xếp ly xanh cobalt điêu khắc. Giữ phòng bê tông tròn trống, giếng trời trên, sàn sạch. Ban đầu đối diện máy, hai chân chạm sàn, tay thả lỏng. Khung từ đầu tới sàn, đủ rộng cho váy.

0–3g: máy hoàn toàn đứng yên. Dừng chính diện ngắn rồi xoay chậm theo chiều kim đồng hồ nhìn từ trên, bước nhỏ có kiểm soát tại chỗ. Vai dẫn tự nhiên; váy ly nặng theo trễ nhẹ. Giây ba đạt góc nghiêng một phần tư vòng rõ.

3–7g: tiếp tục cùng hướng, nhịp sàn diễn bình thản. Lưng rõ gần giây năm, nghiêng phía kia gần giây bảy. Giữ tâm tại cùng vị trí sàn. Ly mở khép nhẹ khi vải quanh chân; gấu chạm sàn, không nâng thành đĩa ngang. Khuyên chỉ đung đưa ít.

7–10g: hoàn tất đúng một vòng 360 độ ở giây chín, lại chính diện. Chân dừng trước, chuyển động cuối của váy dừng sau. Giữ tư thế chính diện một giây còn lại, nhìn ống kính điềm tĩnh.

Âm thanh: bước nhẹ trên bê tông, vải sột soạt tiết chế, nền phòng trầm. Không nhạc, thoại, vỗ tay.

Giữ danh tính, cấu tạo váy gốc, cơ thể liền mạch hợp lý dưới áo. Đầu, tay, gấu luôn thấy. Hướng sáng giếng trời và nền cố định. Không máy quay vòng, xoay thêm, cắt cảnh, đổi màu vải, gấu bay, phụ kiện mới, thân thể biến dạng đàn hồi.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 11. Vầng sáng cam chanh — phim sản phẩm nước hoa cao cấp

![Vầng sáng cam chanh — phim sản phẩm nước hoa cao cấp](assets/citrus-fragrance-product-video.webp)

**Thiết lập tạo video từ ảnh:** 8s · 16:9 · 1080p · [Khung hình đầu — mở và lưu](assets/citrus-fragrance-product-video.webp) · [TXT](prompts/text/vi-VN/citrus-halo.txt)

[Nguồn: Flaq AI](docs/ATTRIBUTION.md)

```text
Giữ nguyên thiết kế chai, tỷ lệ thủy tinh, nắp, bệ đá vôi, vỏ bưởi chùm, bối cảnh màu ngà ấm và ánh sáng bên vàng trong ảnh. Tạo một phim sản phẩm thanh lịch dài tám giây.

0–2.5s: bắt đầu với bố cục macro gần như cố định. Máy quay tiến vào rất chậm. Các hạt nước ngưng tụ bắt sáng; hai giọt trượt tự nhiên xuống lớp kính lạnh. Vỏ bưởi chùm nhấc khỏi bệ như được nâng bởi luồng gió studio có kiểm soát.

2.5–6s: vỏ hoàn thành một vòng xoắn duyên dáng quanh chai mà không chạm hoặc che nắp. Các hạt sương cam chanh li ti đi qua ánh sáng ngược. Khúc xạ và các vệt tụ sáng di chuyển đúng vật lý qua lớp kính dày; bản thân chai hoàn toàn cứng, không biến dạng.

6–8s: vỏ hạ về đường cong ban đầu, máy quay nhẹ nhàng dừng lại, và một vệt phản xạ sáng lướt đúng một lần dọc mép chai. Kết thúc bằng khung hình chủ đạo sản phẩm gọn sạch.

Âm thanh: chỉ có hiệu ứng thu gần trong studio — tiếng dải vỏ chuyển động nhẹ, hai tiếng giọt nước trong rõ và cộng hưởng thủy tinh tinh tế. Không giọng nói, nhạc hoặc chữ.

Khóa tính liên tục: không đổi đường bao chai, các mặt nắp, mức chất lỏng, bệ, bảng màu hoặc vòm phía sau. Không nhãn, logo, quả thêm vào, chai lơ lửng, hình dạng rung méo, máy quay nhảy vị trí hoặc bùng nổ lấp lánh nhân tạo.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="seaimagine-browser-workflow"></a>

<a id="create-with-seaimagine"></a>

## Đưa cảnh bạn chọn vào SeaImagine

<a href="https://seaimagine.com/vi/model/grok-imagine-1-5/"><img src="assets/seaimagine-logo.png" width="64" height="64" alt="SeaImagine"></a>

Từ độ trong của chai thủy tinh, biểu cảm nhỏ trong đối thoại thợ sửa đồng hồ đến nếp váy khi xoay: chọn ảnh tham chiếu cùng prompt và tiếp tục sáng tạo trên trang Grok Imagine 1.5 của SeaImagine.

[Chất liệu chai](#case-sea-glass-bottle) · [Đối thoại thợ đồng hồ](#case-clockwork-dialogue) · [Váy xoay](#case-cobalt-orbit)

[![Sản phẩm, chất liệu, kiến trúc và thời trang gặp nhau trong một không gian sáng tạo liền mạch. Hình ảnh ý tưởng thương hiệu nguyên bản của SeaImagine.](assets/seaimagine-creative-atrium.png)](https://seaimagine.com/vi/model/grok-imagine-1-5/)

Sản phẩm, chất liệu, kiến trúc và thời trang gặp nhau trong một không gian sáng tạo liền mạch. Hình ảnh ý tưởng thương hiệu nguyên bản của SeaImagine.

**[Tạo cảnh này bằng SeaImagine](https://seaimagine.com/vi/model/grok-imagine-1-5/)**

<a id="learn-from-official-and-community-examples"></a>

<a id="writing-guide"></a>

<a id="bài-kiểm-tra-đa-ngôn-ngữ-xưởng-đèn-gốm"></a>

<a id="nguyên-tắc-nhanh"></a>

<a id="thư-viện-đầy-đủ"></a>

## Tài liệu tham khảo

[Tham khảo cách viết](docs/guides/vi-VN.md) · [Tài liệu tham khảo về cài đặt và thao tác](docs/workflows/vi-VN.md) · [SeaImagine](https://seaimagine.com/vi/model/grok-imagine-1-5/)

[Nguồn](docs/COMMUNITY.md) · [X / YouTube](docs/SOCIAL_INSPIRATION.md)

<a id="multilingual-prompts"></a>

## Bộ sưu tập và ghi nguồn

Tổng 65 prompt tiếng Anh khác nhau: 35 từ kho gốc và 30 nguyên bản mới. Bản dịch không tính là cảnh mới. Prompt mới chưa được kiểm chứng bằng lần tạo thực tế.

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/vi/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
