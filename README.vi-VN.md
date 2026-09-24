# Thư viện câu lệnh Grok Imagine 1.5 — Tiếng Việt

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md) · [Español](README.es-ES.md) · [Français](README.fr-FR.md) · [Deutsch](README.de-DE.md) · [Português](README.pt-BR.md) · [Italiano](README.it-IT.md) · [Русский](README.ru-RU.md) · [العربية](README.ar.md) · [Bahasa Indonesia](README.id-ID.md) · [ไทย](README.th-TH.md) · [Tiếng Việt](README.vi-VN.md)

> 62 câu lệnh, trong đó 8 ví dụ có hình được cung cấp bằng 15 ngôn ngữ. Duyệt theo danh mục và sao chép toàn bộ câu lệnh.

![Grok Imagine 1.5 — Sổ câu lệnh mở ra với giày, tàu điện và cá voi giấy trong cùng một khung cảnh](assets/seaimagine-grok-hero.webp)

Chuyển thể từ [Flaq AI](https://github.com/flaqai/awesome-grok-imagine), do SeaImagine duy trì theo giấy phép [MIT](LICENSE) và độc lập với xAI. Ảnh ý tưởng không thể hiện kết quả thử nghiệm thực tế bằng Grok.

<a id="find-the-right-prompt"></a>

<a id="prompt-library"></a>

## Mục lục danh mục

[Xem thêm câu lệnh (tiếng Anh) · 62](docs/PROMPT_INDEX.md)

| Danh mục | Cảnh | Chế độ | Ví dụ |
| --- | --- | --- | --- |
| [Sản phẩm và quảng cáo · 8](docs/PROMPT_INDEX.md#01-ads-and-products) | Cận cảnh mỹ phẩm / cà phê / trang sức / quảng cáo ứng dụng | Văn bản thành video / Ảnh thành video / Ảnh tham chiếu thành video | [Chai thủy tinh biển — so sánh chuyển động có kiểm soát biến số](#case-sea-glass-bottle) · [Vầng sáng cam chanh — phim sản phẩm nước hoa cao cấp](#case-citrus-halo) |
| [Kể chuyện điện ảnh · 8](docs/PROMPT_INDEX.md#02-cinematic-storytelling) | Hành động / lãng mạn / hồi hộp / khoa học viễn tưởng / hoạt hình | Văn bản thành video / Ảnh thành video / Kéo dài video | [Tuyến đường xanh — cảnh bám theo người giao hàng ở chợ mưa](#case-blue-route) · [Bưu thiếp ven biển — làm chuyển động ảnh đã lên bố cục](#case-coastal-postcard) |
| [Mạng xã hội và đời sống · 8](docs/PROMPT_INDEX.md#03-social-ugc) | Chia sẻ trải nghiệm / ẩm thực / thể hình / phỏng vấn | Văn bản thành video / Ảnh thành video / Ảnh tham chiếu thành video | [Ngụm đầu tiên — đánh giá quán cà phê tự nhiên](#case-first-sip) · [Tuyến đường muối lúc bình minh — phim tài liệu du lịch](#case-salt-line) |
| [Nhân vật và hội thoại · 7](docs/PROMPT_INDEX.md#04-characters-and-references) | Nhân vật / trang phục / hội thoại / cảnh đông người | Ảnh tham chiếu thành video / Ảnh thành video | [Gặp lại ở bến cảng — chỉ một chuyển biến cảm xúc](#case-harbor-reunion) |
| [Biến đổi hình ảnh và nối tiếp · 6](docs/PROMPT_INDEX.md#05-editing-and-extension) | Đổi thời tiết / xóa chi tiết / đổi phong cách / nối tiếp | Chỉnh sửa video / Kéo dài video | — |
| [Chất liệu và âm thanh thư giãn · 6](docs/PROMPT_INDEX.md#07-satisfying-materials) | Ép cát / lá đồng / giọt nước / tạo vân cẩm thạch | Văn bản thành video | — |
| [Không gian và kiến trúc · 6](docs/PROMPT_INDEX.md#08-spaces-and-transformations) | Nội thất mở ra / sân trong / mặt cắt ngôi nhà | Văn bản thành video | — |
| [Thế giới thu nhỏ và siêu thực · 7](docs/PROMPT_INDEX.md#09-miniature-and-surreal) | Phà trong tách trà / mưa trong ngăn kéo / mặt trăng giấy | Văn bản thành video / Ảnh thành video | [Ổ bánh mật ong — câu chuyện tiệm bánh tí hon](#case-honey-loaf) |
| [Thời trang và trình diễn · 6](docs/PROMPT_INDEX.md#10-fashion-and-performance) | Tà váy / áo choàng / hình chiếu trên cổ áo / bước nhảy | Văn bản thành video | — |

[Ví dụ có hình](#featured-prompts) · [Sáng tạo với SeaImagine](#create-with-seaimagine)

<a id="visual-index"></a>

<a id="featured-prompts"></a>

## Câu lệnh có hình để sao chép và điều chỉnh

8 ví dụ kèm câu lệnh đầy đủ và ảnh khung hình đầu. Ảnh minh họa ý tưởng, không phải kết quả video đã được kiểm chứng.

Năm ví dụ ghi nguồn Flaq AI giữ nguyên thời lượng và độ phân giải gốc; ba ví dụ còn lại được viết theo các tùy chọn hiện tại của SeaImagine. Khi dùng ví dụ gốc trên SeaImagine, hãy chọn 5/10/15 giây và 480p/720p, rồi sắp xếp lại thời gian cho các hành động.

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

<a id="case-harbor-reunion"></a>

<a id="seaimagine-harbor-reunion"></a>

### 4. Gặp lại ở bến cảng — chỉ một chuyển biến cảm xúc

![Gặp lại ở bến cảng — chỉ một chuyển biến cảm xúc](assets/seaimagine-harbor-reunion.webp)

**Thiết lập tạo video từ ảnh:** 10s · 16:9 · 720p · [Khung hình đầu — mở và lưu](assets/seaimagine-harbor-reunion.webp) · [TXT](prompts/text/vi-VN/harbor-reunion.txt)

```text
Giữ nguyên hai người trưởng thành, khuôn mặt của họ, trang phục xanh hải quân và màu kem,
cầu cảng gỗ cùng ánh sáng ban mai dịu trong ảnh được cung cấp. Luôn giữ cả hai trong cùng bố cục trung rộng.
0–3 giây: người bên trái nhận ra người bạn vừa đến và bước một bước nhỏ về phía trước.
Vai thả lỏng; người bạn đáp lại bằng một nụ cười nhẹ. Giữ bàn tay trong khung hình với tư thế thư giãn.
3–7 giây: người bên trái nói bằng tiếng Việt tự nhiên: “Cậu đến rồi.” Người bạn gật đầu một lần.
Nói nhẹ nhàng, không khóc hoặc biểu cảm khuôn mặt quá mức.
7–10 giây: cả hai nhìn về chiếc thuyền đang neo. Giữ khung hình trong giây cuối để nối sang cảnh quay tiếp theo.
Máy quay: chỉ tiến vào nhẹ nhàng một lần, không đổi sang góc ngược và không cắt cảnh.
Âm thanh: lời nói gần, rõ ràng, tiếng nước cảng nhẹ và tiếng hải âu từ xa; không nhạc hay phụ đề.
Giữ nhất quán nhận dạng hai người, trang phục, hình dạng cầu cảng, vị trí thuyền và hướng ánh sáng ban mai.
Tránh thêm người, cử chỉ kịch tính, làm mịn mặt, ngón tay thừa và máy quay nhảy vị trí.
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

<a id="case-coastal-postcard"></a>

<a id="seaimagine-coastal-postcard"></a>

### 7. Bưu thiếp ven biển — làm chuyển động ảnh đã lên bố cục

<a href="assets/seaimagine-coastal-postcard.webp"><img src="assets/seaimagine-coastal-postcard.webp" width="480" alt="Bưu thiếp ven biển — làm chuyển động ảnh đã lên bố cục"></a>

**Thiết lập tạo video từ ảnh:** 5s · 9:16 · 720p · [Khung hình đầu — mở và lưu](assets/seaimagine-coastal-postcard.webp) · [TXT](prompts/text/vi-VN/coastal-postcard.txt)

```text
Làm chuyển động bưu thiếp ven biển ba ô này mà không đổi bố cục hoặc đường viền.
Giữ nguyên chính xác mọi vật thể và màu sắc. Ở ô trên, một làn hơi mảnh bốc lên từ chiếc cốc.
Ở ô giữa, nước cảng gợn nhẹ và ánh nắng lấp lánh trên mặt nước.
Ở ô dưới, chỉ góc tờ giấy có sẵn hơi nhấc lên rồi hạ xuống trong gió nhẹ.
Mỗi chuyển động chỉ diễn ra trong ô của nó. Tất cả các ô luôn hiển thị suốt năm giây.
Máy quay: cố định, không thu phóng, không lia, không cắt cảnh hoặc chuyển cảnh giữa các ô.
Âm thanh: tiếng nước nhẹ và tiếng giấy sột soạt khẽ; không lời thoại, nhạc, phụ đề hay chữ thêm vào.
Giữ nguyên quai cốc, khung cửa sổ, ký hiệu bản đồ, kích thước các ô và thứ tự đọc.
Tránh gộp ô, tạo cảnh mới, vẽ lại chữ hoặc để vật thể di chuyển qua đường viền.
Kết thúc khi góc giấy đã nằm yên và bố cục gốc vẫn nguyên vẹn.
```

[Quay lại mục lục danh mục](#find-the-right-prompt)

<a id="case-citrus-halo"></a>

<a id="1-citrus-halo--premium-fragrance-product-film"></a>

### 8. Vầng sáng cam chanh — phim sản phẩm nước hoa cao cấp

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

Chọn video sản phẩm chai thủy tinh, hội thoại ở bến cảng hoặc bưu thiếp chuyển động ở trên, rồi dùng hình ảnh và câu lệnh đầy đủ trong Grok Imagine 1.5 trên SeaImagine. Khám phá chất liệu ở cảnh sản phẩm, diễn xuất trong hội thoại và bố cục trong đồ họa chuyển động.

[Chất liệu sản phẩm](#case-sea-glass-bottle) · [Hội thoại nhân vật](#case-harbor-reunion) · [Bố cục chuyển động](#case-coastal-postcard)

[![SeaImagine · Grok Imagine 1.5](assets/seaimagine-interface.jpg)](https://seaimagine.com/vi/model/grok-imagine-1-5/)

Giao diện thực tế: đã nhập câu lệnh chai thủy tinh, 720p · 5 giây · 16:9. Chưa tải ảnh mở đầu lên và chưa tạo video.

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

62 lời nhắc tiếng Anh khác nhau: 35 từ kho gốc và 27 bản tự viết. 24 bản mới nhất lấy cảm hứng từ chủ đề trên mạng xã hội, chưa được kiểm chứng bằng việc tạo video. Bản dịch không được tính là cảnh mới.

[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine](https://seaimagine.com/vi/model/grok-imagine-1-5/) · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)
