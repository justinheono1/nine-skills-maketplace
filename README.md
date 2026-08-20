# Nine Skills — Marketplace nội bộ Nine Feng Shui

Kho skill dùng chung cho cả team Nine. Cài 1 lần, anh Hậu sửa ở đây rồi push →
mọi người chạy `update` là có bản mới.

## Skill hiện có

| Skill | Mô tả |
|---|---|
| `dashboard-la-so` | Dựng dashboard trực quan 1 trang (.html) cho lá số Tử Vi để gửi khách. |

---

## Cách cài (cho mọi người trong Nine) — làm 1 lần

Mở Claude Code, gõ 2 lệnh:

```
/plugin marketplace add <GITHUB_OWNER>/nine-skills-marketplace
/plugin install dashboard-la-so@nine-skills
```

> Thay `<GITHUB_OWNER>` bằng tên tài khoản/tổ chức GitHub của anh Hậu
> (ví dụ repo `https://github.com/justinhau/nine-skills-marketplace`
> thì gõ `justinhau/nine-skills-marketplace`).

Nếu repo để **private**: mỗi người cần được mời vào repo (Settings → Collaborators)
và đã đăng nhập GitHub trên máy họ. Repo **public** thì ai có link cũng cài được.

---

## Cách nhận bản cập nhật (khi anh Hậu sửa skill)

Mỗi người chỉ cần thỉnh thoảng chạy:

```
/plugin marketplace update nine-skills
```

Rồi Claude Code kéo bản mới nhất từ GitHub về. (Skill này KHÔNG ghim version,
nên mỗi lần anh Hậu push là bản mới sẵn sàng — không cần đổi số version.)

---

## Cách anh Hậu chỉnh sửa & phát hành

1. Sửa file skill trong `plugins/dashboard-la-so/skills/dashboard-la-so/`.
2. Commit + push:
   ```bash
   cd ~/Desktop/nine-skills-marketplace
   git add -A
   git commit -m "Cập nhật skill dashboard-la-so"
   git push
   ```
3. Báo team chạy `/plugin marketplace update nine-skills`.

## Cấu trúc repo

```
nine-skills-marketplace/
├── .claude-plugin/
│   └── marketplace.json          # danh mục marketplace
└── plugins/
    └── dashboard-la-so/
        ├── .claude-plugin/
        │   └── plugin.json       # manifest plugin
        └── skills/
            └── dashboard-la-so/  # skill thật
                ├── SKILL.md
                ├── finalize.py
                └── assets/
```
