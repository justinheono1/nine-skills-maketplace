#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
finalize.py — hoàn tất dashboard lá số Nine Feng Shui.

Làm 2 việc máy-móc-dễ-sai mà không nên gõ tay:
  1) Nhúng logo (nine-emblem.png) dạng base64 vào mọi chỗ src="{{LOGO}}".
  2) Sinh TOÀN VĂN luận giải (section class="read") từ file report .md của khách,
     đảm bảo đầy đủ 100% như bản docx — không thiếu đoạn nào.

Cách dùng:
  python3 finalize.py <dashboard.html> <report.md> [emblem.png]

- <dashboard.html>: file dashboard đã điền nội dung 12 cung + tóm tắt cho khách
  (copy từ assets/template.html rồi sửa). Sửa tại chỗ (in-place).
- <report.md>: bản Life Dossier Full (.md) của khách — nguồn để sinh phần luận đầy đủ.
- [emblem.png]: mặc định assets/nine-emblem.png cạnh script.

Quy ước report .md (khớp skill luan-tu-vi, Format A):
  # Lá số ...            → tiêu đề (bỏ qua ở phần reading)
  # Phần N: <tên cung>   → mỗi phần thành 1 <details> (Phần 1 mở sẵn)
  ## <tên cung con>      → <h4> (đề mục cung trong Phần 3, 4)
  **Tên sao**            → <span class="star">
  *"câu phú"*            → <span class="phu"> (in nghiêng)
  ---                    → kết thúc phần luận (mọi thứ sau đó bị bỏ)
"""
import re, sys, base64, os

TOK = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")

def inline(t):
    out = []
    for p in TOK.split(t):
        if not p:
            continue
        if p.startswith("**") and p.endswith("**"):
            out.append('<span class="star">' + p[2:-2] + '</span>')
        elif p.startswith("*") and p.endswith("*"):
            out.append('<span class="phu">' + p[1:-1] + '</span>')
        else:
            out.append(p)
    return "".join(out)

def build_reading(md_path):
    lines = open(md_path, encoding="utf-8").read().split("\n")
    parts = []
    cur = None
    started = False
    for raw in lines:
        s = raw.strip()
        if s.startswith("# Phần"):
            started = True
            if cur:
                parts.append(cur)
            m = re.match(r"# Phần\s*(\d+):\s*(.+)", s)
            cur = {"idx": m.group(1), "title": m.group(2).strip(), "blocks": []}
            continue
        if not started:
            continue
        if s == "---":
            break
        if not s:
            continue
        if s.startswith("## "):
            cur["blocks"].append(("h4", inline(s[3:].strip())))
        elif s.startswith("#"):
            continue
        else:
            cur["blocks"].append(("p", inline(raw.rstrip())))
    if cur:
        parts.append(cur)

    det = []
    for i, pt in enumerate(parts):
        op = " open" if i == 0 else ""
        body = []
        for kind, html in pt["blocks"]:
            body.append(("      <h4>%s</h4>" if kind == "h4" else "      <p>%s</p>") % html)
        det.append(
            '    <details%s><summary><span class="ix">%s</span> %s <span class="plus">+</span></summary><div class="body">\n%s\n    </div></details>'
            % (op, pt["idx"].zfill(2), pt["title"], "\n".join(body)))
    section = (
        '  <section class="read">\n'
        '    <div class="sec-head"><span class="n">viii.</span><h2>Toàn văn luận giải</h2>'
        '<span class="k">bấm mở từng phần — bản đầy đủ</span></div>\n'
        + "\n".join(det) + "\n  </section>")
    return section, len(parts)

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    html_path = sys.argv[1]
    md_path = sys.argv[2]
    here = os.path.dirname(os.path.abspath(__file__))
    emb = sys.argv[3] if len(sys.argv) > 3 else os.path.join(here, "assets", "nine-emblem.png")

    html = open(html_path, encoding="utf-8").read()

    # 1) logo
    b64 = base64.b64encode(open(emb, "rb").read()).decode()
    datauri = "data:image/png;base64," + b64
    nlogo = html.count("{{LOGO}}")
    html = html.replace("{{LOGO}}", datauri)

    # 2) reading — thay section class="read" (marker hoặc section cũ) bằng bản đầy đủ
    section, nparts = build_reading(md_path)
    if "<!--READING-->" in html:
        html = html.replace("<!--READING-->", section)
        nread = 1
    else:
        html, nread = re.subn(r'  <section class="read">.*?</section>', lambda m: section, html, flags=re.S)

    open(html_path, "w", encoding="utf-8").write(html)
    print("OK: logo slots=%d | reading parts=%d | read section replaced=%d" % (nlogo, nparts, nread))
    if nlogo == 0:
        print("  ! Cảnh báo: không thấy {{LOGO}} — kiểm template có slot logo không.")
    if nread == 0:
        print("  ! Cảnh báo: không thay được section.read — cần có <!--READING--> hoặc <section class=\"read\">…</section>.")

if __name__ == "__main__":
    main()
