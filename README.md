# Job Application Tracker (Flask)

Ứng dụng web giúp bạn theo dõi quá trình ứng tuyển: thêm/sửa/xoá công việc, lọc theo trạng thái, và xem thống kê tổng quan.

> **Demo**:   
> trang web của tôi: `https://job-tracker-85ku.onrender.com`

---

## ✨ Tính năng chính

- **CRUD Job**: Công ty, Vị trí, Trạng thái, Ngày nộp, Ghi chú
- **Lọc theo trạng thái** ngay trên trang danh sách
- **Thống kê** tổng số job, phân bổ theo trạng thái, thống kê theo tháng
- **API JSON**: `GET /api/jobs`
- **Bảo mật form** với CSRF (Flask-WTF)
- **UI gọn** với CSS thuần (không framework CSS)

---

## 🧰 Tech stack

- **Flask** (App Factory + Blueprints)
- **Flask-SQLAlchemy** (ORM) với **SQLite** cho dev (dễ chạy)
- **Flask-WTF** (forms + CSRF)
- **Jinja2** (templates), **Gunicorn** (prod server khi deploy)

---

## 🗂️ Cấu trúc thư mục
job-tracker/
├── app/
│ ├── init.py # tạo app, init db, csrf, register blueprint
│ ├── models/
│ │ ├── init.py
│ │ └── job.py # Job model
│ ├── routes/
│ │ ├── init.py
│ │ ├── main.py # routes UI: /, /add, /edit, /delete, /statistics
│ │ └── api.py # routes API: /api/jobs
│ ├── forms/
│ │ ├── init.py
│ │ └── job_form.py # JobForm (WTForms)
│ ├── utils/
│ │ ├── init.py
│ │ └── statistics.py # hàm thống kê
│ ├── templates/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── add_job.html
│ │ ├── edit_job.html
│ │ └── statistics.html
│ └── static/
│ └── style.css
├── instance/ # chứa jobs.db (tự tạo)
│ └── .gitkeep
├── tests/ # khung test (tuỳ chọn)
├── config.py
├── requirements.txt
├── run.py
└── Procfile # (tuỳ chọn, cho Render/Heroku)

## ⚙️ Cấu hình & biến môi trường
`config.py` đọc env nếu có, fallback SQLite local.
- `SECRET_KEY` – bắt buộc khi deploy (tạo bằng: `python -c "import secrets; print(secrets.token_hex(32))"`)
- `DATABASE_URL` – (tuỳ chọn) Postgres URL khi muốn dữ liệu bền trên Render

## 🚀 Chạy local
```bash
python -m venv venv
venv\Scripts\activate             # Windows (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt

# tạo DB (tự động nếu run.py có db.create_all())
python run.py
# mở http://127.0.0.1:5000

- Giải thích sơ đồ kiến trúc:

- Giao diện Người dùng: Bao gồm các trang web mà người dùng tương tác trực tiếp
- Frontend: Xử lý logic phía client, đảm bảo dữ liệu hợp lệ trước khi gửi đến server
- Backend: Xử lý nghiệp vụ chính, bao gồm API, kiểm tra dữ liệu và xử lý lỗi
- Lưu trữ:
- Database: Lưu trữ thông tin việc làm và trạng thái ứng tuyển
- Hệ thống tệp: Có thể lưu trữ CV, cover letter hoặc các tài liệu khác
- Các mũi tên thể hiện luồng dữ liệu:

- Khi người dùng gửi mẫu đơn mới → Frontend kiểm tra → Backend xử lý → Lưu vào Database
- Khi xem danh sách → Frontend yêu cầu → Backend lấy từ Database → Hiển thị cho người dùng
- Khi có lỗi → Backend thông báo lại cho Frontend → Hiển thị cho người dùng

docs\Sơ đồ cấu trúc .png
docs\Example of website.png