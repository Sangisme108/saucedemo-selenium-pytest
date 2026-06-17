# Báo cáo thực hành kiểm thử tự động với Selenium

## 1. Giới thiệu Selenium

Selenium là một công cụ mã nguồn mở dùng để tự động hóa thao tác trên trình duyệt web. Selenium cho phép viết script để mô phỏng hành vi người dùng như mở trang web, nhập dữ liệu, nhấn nút, kiểm tra nội dung hiển thị và xác nhận kết quả bằng các câu lệnh kiểm thử.

Trong bài thực hành này, Selenium được kết hợp với Python và Pytest để xây dựng các test case kiểm thử tự động cho website SauceDemo.

## 2. Website được kiểm thử

- Website: <https://www.saucedemo.com/>
- Mục đích kiểm thử: kiểm tra chức năng đăng nhập, hiển thị danh sách sản phẩm và thêm sản phẩm vào giỏ hàng.

Tài khoản dùng để kiểm thử:

- Username: `standard_user`
- Password: `secret_sauce`

## 3. Công cụ sử dụng

Project sử dụng các công cụ và thư viện sau:

- Python: ngôn ngữ lập trình dùng để viết test script.
- Selenium: thư viện tự động hóa trình duyệt web.
- Pytest: framework dùng để tổ chức và chạy test case.
- webdriver-manager: thư viện tự động tải và quản lý ChromeDriver.
- Google Chrome: trình duyệt dùng để chạy kiểm thử.

## 4. Cấu trúc project

```text
saucedemo-selenium-pytest/
├── tests/
│   └── test_saucedemo.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 5. Cách cài đặt

Bước 1: Clone hoặc tải project về máy.

```bash
git clone <link-repository-github>
cd saucedemo-selenium-pytest
```

Bước 2: Tạo môi trường ảo Python.

```bash
python -m venv .venv
```

Bước 3: Kích hoạt môi trường ảo.

Trên Windows:

```bash
.venv\Scripts\activate
```

Trên macOS hoặc Linux:

```bash
source .venv/bin/activate
```

Bước 4: Cài đặt thư viện cần thiết.

```bash
pip install -r requirements.txt
```

## 6. Cách chạy test

Chạy toàn bộ test case bằng lệnh:

```bash
pytest -v
```

Sau khi chạy, Pytest sẽ hiển thị kết quả `PASSED` hoặc `FAILED` cho từng test case.

## 7. Mô tả test case

### TC01: Đăng nhập thành công

- Mục tiêu: kiểm tra người dùng có thể đăng nhập thành công với tài khoản hợp lệ.
- Dữ liệu test:
  - Username: `standard_user`
  - Password: `secret_sauce`
- Các bước thực hiện:
  1. Mở website SauceDemo.
  2. Nhập username và password hợp lệ.
  3. Nhấn nút Login.
  4. Kiểm tra người dùng được chuyển đến trang sản phẩm.
- Kết quả mong đợi:
  - URL có chứa `inventory.html`.
  - Tiêu đề trang hiển thị là `Products`.

### TC02: Kiểm tra danh sách sản phẩm sau khi đăng nhập

- Mục tiêu: kiểm tra danh sách sản phẩm được hiển thị sau khi đăng nhập thành công.
- Các bước thực hiện:
  1. Đăng nhập vào website bằng tài khoản hợp lệ.
  2. Chờ danh sách sản phẩm hiển thị.
  3. Kiểm tra số lượng sản phẩm trên trang.
- Kết quả mong đợi:
  - Trang có ít nhất một sản phẩm.
  - Tên sản phẩm đầu tiên được hiển thị.

### TC03: Thêm sản phẩm Sauce Labs Backpack vào giỏ hàng

- Mục tiêu: kiểm tra chức năng thêm sản phẩm vào giỏ hàng.
- Các bước thực hiện:
  1. Đăng nhập vào website bằng tài khoản hợp lệ.
  2. Nhấn nút Add to cart của sản phẩm Sauce Labs Backpack.
  3. Kiểm tra biểu tượng giỏ hàng.
- Kết quả mong đợi:
  - Số lượng sản phẩm trong giỏ hàng hiển thị là `1`.

## 8. Kết quả mong đợi chung

Khi chạy lệnh:

```bash
pytest -v
```

Kết quả mong đợi:

```text
tests/test_saucedemo.py::test_tc01_login_successfully PASSED
tests/test_saucedemo.py::test_tc02_product_list_displayed_after_login PASSED
tests/test_saucedemo.py::test_tc03_add_backpack_to_cart PASSED
```

Toàn bộ 3 test case đều chạy thành công.

## 9. Hướng dẫn chèn ảnh minh họa kết quả chạy test

Sau khi chạy lệnh `pytest -v`, có thể chụp màn hình terminal hiển thị kết quả test và lưu ảnh vào thư mục `screenshots`.

Ví dụ:

```text
saucedemo-selenium-pytest/
└── screenshots/
    └── pytest-result.png
```

Sau đó chèn ảnh vào README bằng cú pháp Markdown:

```markdown
![Kết quả chạy test](screenshots/pytest-result.png)
```

Khi đẩy project lên GitHub, ảnh minh họa sẽ được hiển thị trực tiếp trong file README nếu đường dẫn ảnh chính xác.

## 10. Ghi chú

- Cần cài đặt Google Chrome trên máy trước khi chạy test.
- Lần chạy đầu tiên có thể mất thêm thời gian vì `webdriver-manager` cần tải ChromeDriver phù hợp.
- Nếu Chrome hoặc ChromeDriver thay đổi phiên bản, `webdriver-manager` sẽ tự động hỗ trợ quản lý driver.
