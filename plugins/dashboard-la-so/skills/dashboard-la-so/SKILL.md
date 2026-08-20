---
name: dashboard-la-so
description: Dựng dashboard trực quan một trang (HTML tự chứa) cho một lá số Tử Vi theo đúng nhận diện Nine Feng Shui, để anh Hậu gửi khách. Dùng skill này ngay SAU khi đã luận xong một lá số bằng skill luan-tu-vi (đã có bản Life Dossier Full .md). Kết quả là 1 file .html gồm bàn cờ 12 cung trực quan, các khối tóm tắt (chân dung, sự nghiệp/tài/hôn nhân, đại vận, lộ trình 12 tháng, điểm mạnh/rủi ro, hành động), toàn văn luận bấm-mở từng cung đầy đủ, và section thương hiệu Nine — có nút Sáng/Tối, in được. Gọi khi anh nói "dựng dashboard", "làm dashboard lá số", "dashboard cho khách X", hoặc muốn bản trực quan của một lá số đã luận.
---

# Dashboard lá số — Nine Feng Shui

Biến một bản luận Tử Vi (Life Dossier) thành **một trang dashboard trực quan, tự chứa (1 file .html)**, đúng nhận diện Nine Feng Shui, để anh Hậu gửi khách. Thiết kế (CSS, brand, bố cục) là **cố định** — chỉ **nội dung theo từng lá số** thay đổi.

## Khi nào dùng
Sau khi đã có **bản Life Dossier Full (.md)** của khách từ skill `luan-tu-vi` (nằm ở `huyen-hoc/output/report-la-so/<Tên khách>/`). Skill này KHÔNG tự luận — nó trực quan hoá bản luận đã có.

## Điều kiện đầu vào (đủ mới làm)
1. **Bản report .md** đầy đủ (Life Dossier Full) của khách — nguồn để sinh phần "Toàn văn luận giải".
2. **Dữ liệu 12 cung** (đã có sẵn khi luận): mỗi cung gồm tên cung, Địa Chi + ngũ hành, chính tinh + trạng thái (miếu/vượng/đắc/hãm), phụ tinh chính, Hóa (bản mệnh + đại vận + lưu niên), tuổi khởi đại vận, tháng nguyệt vận, và các dấu (Mệnh/Thân/Triệt/Tuần/Đại vận/Lưu Thái Tuế/Tiểu Hạn).
3. **Thông tin nền**: tên khách, ngày–giờ–năm sinh, giới, bản mệnh/cục, chủ mệnh/chủ thân, cách cục, năm xem.
4. **Logo**: `assets/nine-emblem.png` (đã kèm trong skill; là biểu tượng Nine đã tách nền trong suốt).

Thiếu report .md → dừng, bảo anh luận xong (skill `luan-tu-vi`) trước.

## Quy trình 4 bước

**Bước 1 — Copy template.**
```
cp "assets/template.html" "huyen-hoc/output/report-la-so/<Tên khách>/<Tên khách> — Dashboard lá số — <YYYY-MM-DD>.html"
```
Template đã chứa sẵn nội dung ví dụ của "Khách Mẫu" (nhân vật hư cấu) để thấy đúng khuôn. Việc của Mèo là **sửa các vùng nội dung** sang lá số mới.

**Bước 2 — Sửa nội dung theo lá số mới** (dùng Edit trên file vừa copy, theo mục "Bản đồ các vùng cần sửa" bên dưới). Đọc lại `assets/template.html` (hoặc file vừa copy) để thấy cấu trúc thật trước khi sửa. KHÔNG đụng vào `<style>`, section `class="brandsec"` (thương hiệu — cố định), và `<script>`.

**Bước 3 — Chạy finalize** (nhúng logo + sinh toàn văn luận đầy đủ từ .md):
```
python3 finalize.py "<đường dẫn file dashboard vừa sửa>" "<đường dẫn report .md>"
```
Script tự: thay 2 chỗ `{{LOGO}}` bằng logo base64; thay cả section `class="read"` bằng **toàn văn luận đầy đủ** sinh từ report .md (đủ 100%, không thiếu đoạn). In ra số phần đã sinh để đối chiếu.

**Bước 4 — Kiểm & giao.** Mở kiểm nhanh (có thể serve tĩnh bằng `python3 -m http.server` rồi dùng browser/JS), rồi gửi file cho anh (SendUserFile, display render). Báo anh đường dẫn file.

## Bản đồ các vùng cần sửa (chỉ nội dung, giữ nguyên class/thẻ)

Trong file (copy từ template), sửa các chỗ sau cho khách mới — bám đúng ví dụ có sẵn:

1. `<title>Lá số <Tên khách></title>` và slogan giữ nguyên (`Hiểu thời · Chọn đúng nhịp · Hành động phù hợp`).
2. **Hero**: `<h1>` tiêu đề lá số (VD "Lá số <Tên> — <định danh gợi hình>"); `<p class="sub">` câu mở (giữ nguyên câu "bản đồ địa hình…" được).
3. **factstrip**: 7 ô `.fact` (Sinh, Giới, Bản mệnh, Mệnh, Thân, Đại vận, Năm xem).
4. **Bàn cờ** `.board`: 12 ô `.cell` + 1 `.corners` (giữ đúng thứ tự DOM = địa bàn: Tỵ, Ngọ, Mùi, Thân, Thìn, [corners], Dậu, Mão, Tuất, Dần, Sửu, Tý, Hợi). Xem "Cấu trúc 1 ô cung".
5. **Chân dung** (`sec ii`): 3 thẻ `.card` (tag, h3, p, q).
6. **Sự nghiệp/Tài/Hôn nhân** (`sec iii`): 4 thẻ.
7. **Đại vận** (`sec iv`): `.lead` + 2 thẻ (vế sáng / rủi ro).
8. **12 tháng** (`sec v`): 12 ô `.mo` (thêm class `hot`/`soft` cho tháng nóng/nhẹ; `.flag` nhãn góc).
9. **Điểm mạnh/rủi ro** (`sec vi`): 2 `.card` (`.good`/`.risk`) với các `<li>`.
10. **Hành động** (`sec vii`): 4 `.act` (b tiêu đề + span mô tả).
11. **Toàn văn luận** (`sec viii`, `class="read"`): **KHÔNG sửa tay** — để finalize.py sinh từ .md. (Có thể thay cả section bằng `<!--READING-->` cho gọn trước khi chạy finalize.)
12. **Footer**: `<p class="meta">NINE FENG SHUI · Lá số <Tên khách></p>`.

### Cấu trúc 1 ô cung (.cell)
```
<div class="cell mark-menh"><span class="age">5 · T1</span><div class="cung">Mệnh</div>
  <div class="major">Thái Âm<span class="st ham">Hãm</span></div>
  <div class="stars">Văn Khúc · Đào Hoa · Thiên Hỉ<br/><span class="hoa khoa">Hóa Khoa</span> · <span class="hoa quyen">ĐV Quyền</span></div>
  <span class="chi">Mão · Mộc</span><span class="pips"><span class="pip menh">Mệnh</span></span></div>
```
- `.age` = "<tuổi khởi đại vận> · T<tháng nguyệt vận>".
- `.cung` = tên cung (Mệnh, Phúc Đức…). `.major` = chính tinh; badge trạng thái: `st mieu|vuong|dac` (cát, xanh) / `st ham` (hung, đỏ).
- `.stars` = phụ tinh; Hóa dùng span `hoa loc|quyen|khoa|ky`.
- `.chi` = "<Chi> · <Ngũ hành cung>".
- `.pips` = dấu: `pip menh` / `pip than` / `pip trietv` (Triệt) / `pip tuanv` (Tuần) / `pip dv` (Đại vận) / `pip month` / `pip` (mặc định, VD Lưu T.Tuế, Tiểu Hạn, LN Mệnh).
- Class ô: `mark-menh` (viền Mệnh) / `mark-than` (viền Thân) / `mark-dv` (viền Đại vận). Cung không dấu thì không thêm.

## Quy tắc thiết kế (KHÔNG đổi)
- Nhận diện Nine: lục thẫm `#2E5A40` + than chì `#2B312C` + vàng đồng `#C2A15E`; nền kem (sáng) / lục-than thẫm (tối). **Giao diện Tối**: đề mục/tên cung/slogan tự chuyển **màu cam** (`--head`); **giao diện Sáng**: giữ lục brand. Đây là hành vi có sẵn trong CSS — không cần đụng.
- Mã màu ngũ hành theo legend lá số: Kim xám · Mộc lục · Thủy lam · Hỏa đỏ · Thổ vàng.
- Chữ: Cormorant Garamond (tiêu đề) + Be Vietnam Pro (thân), fallback Georgia/system.
- Body luận **canh đều 2 biên**; phú nôm **chỉ in nghiêng, cùng cỡ body** (không thu nhỏ). Đề mục cung trong phần luận **to hơn body**.
- Section thương hiệu (Tầm nhìn/Sứ mệnh/6 Giá trị cốt lõi) là **cố định** — lấy từ brand-kit, giữ nguyên cho mọi khách.
- Chi tiết brand: `huyen-hoc/brand/brand-kit.md`.

## Lưu trữ
File dashboard lưu cùng chỗ report của khách: `huyen-hoc/output/report-la-so/<Tên khách>/`. Nếu anh muốn cả bản trên Drive: upload lên folder khách trong `la-so-khach` (xem cách trong skill `luan-tu-vi` mục 9).

## Đồng bộ skill (khi sửa skill này)
Bản master ở `huyen-hoc/skill-goc/dashboard-la-so/`; bản chạy ở `~/.claude/skills/dashboard-la-so/`. Sửa master rồi copy sang bản chạy (giống các skill huyền học khác).

## Tài liệu kèm (assets/)
- `template.html` — khung thiết kế + ví dụ Khách Mẫu (copy ra rồi sửa).
- `nine-emblem.png` — logo Nine đã tách nền (finalize nhúng base64).
- `example-report.md` — ví dụ report Full (Khách Mẫu, hư cấu) để đối chiếu định dạng .md đầu vào.
- `finalize.py` — nhúng logo + sinh toàn văn luận từ .md.
