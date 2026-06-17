# Selenium SauceDemo

## Giới thiệu Selenium

Selenium là công cụ dùng để tự động hóa trình duyệt web. Selenium có thể mô phỏng các thao tác của người dùng như mở trang web, nhập dữ liệu, bấm nút, kiểm tra nội dung hiển thị và xác nhận kết quả kiểm thử.

Trong bài thực hành này, Selenium được sử dụng với Python, Pytest và webdriver-manager để kiểm thử tự động website SauceDemo.

## Website dùng để kiểm thử

Trang web dùng để kiểm thử: https://www.saucedemo.com/

Tài khoản kiểm thử:

- Username: `standard_user`
- Password: `secret_sauce`

Ảnh trang web SauceDemo:

![Trang web SauceDemo](screenshots/saucedemo-home.png)

## Công cụ sử dụng

- Python
- Selenium
- Pytest
- webdriver-manager
- Google Chrome

## Cấu trúc project

```text
saucedemo-selenium-pytest/
├── tests/
│   └── test_saucedemo.py
├── screenshots/
├── requirements.txt
├── README.md
└── .gitignore
```

## Cách cài đặt

Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

File `requirements.txt` gồm:

```text
selenium
pytest
webdriver-manager
```

## Cách chạy test

Chạy toàn bộ test case bằng lệnh:

```bash
pytest -v
```

Kết quả chạy test:

![Kết quả chạy test](screenshots/pytest-result.png)

## Test case 01: Đăng nhập thành công

Mục tiêu: kiểm tra người dùng đăng nhập thành công bằng tài khoản hợp lệ.

Dữ liệu kiểm thử:

- Username: `standard_user`
- Password: `secret_sauce`

Các bước thực hiện:

1. Mở website SauceDemo.
2. Nhập username và password.
3. Nhấn nút Login.
4. Kiểm tra trang chuyển sang trang sản phẩm.

Kết quả mong đợi:

- URL có chứa `inventory.html`.
- Tiêu đề trang hiển thị là `Products`.

Ảnh minh họa kết quả đăng nhập:

![Đăng nhập thành công](screenshots/login-success.png)

Kết luận: chức năng đăng nhập hoạt động đúng khi sử dụng tài khoản hợp lệ.

## Test case 02: Kiểm tra danh sách sản phẩm

Mục tiêu: kiểm tra danh sách sản phẩm được hiển thị sau khi đăng nhập thành công.

Các bước thực hiện:

1. Đăng nhập vào website bằng tài khoản hợp lệ.
2. Chờ danh sách sản phẩm hiển thị.
3. Kiểm tra số lượng sản phẩm trên trang.

Kết quả mong đợi:

- Danh sách sản phẩm được hiển thị.
- Có ít nhất một sản phẩm xuất hiện trên trang.

Ảnh minh họa danh sách sản phẩm:

![Danh sách sản phẩm](screenshots/product-list.png)

Kết luận: sau khi đăng nhập, website hiển thị danh sách sản phẩm đúng như mong đợi.

## Test case 03: Thêm sản phẩm vào giỏ hàng

Mục tiêu: kiểm tra chức năng thêm sản phẩm Sauce Labs Backpack vào giỏ hàng.

Các bước thực hiện:

1. Đăng nhập vào website bằng tài khoản hợp lệ.
2. Nhấn nút Add to cart của sản phẩm Sauce Labs Backpack.
3. Kiểm tra số lượng sản phẩm trên biểu tượng giỏ hàng.

Kết quả mong đợi:

- Sản phẩm được thêm vào giỏ hàng.
- Số lượng trên giỏ hàng hiển thị là `1`.

Ảnh minh họa giỏ hàng:

![Thêm sản phẩm vào giỏ hàng](screenshots/cart-badge.png)

Kết luận: chức năng thêm sản phẩm vào giỏ hàng hoạt động đúng, số lượng sản phẩm trong giỏ hàng hiển thị chính xác.

## Kết quả mong đợi chung

Khi chạy lệnh `pytest -v`, cả 3 test case đều phải có trạng thái `PASSED`.

```text
tests/test_saucedemo.py::test_tc01_login_successfully PASSED
tests/test_saucedemo.py::test_tc02_product_list_displayed_after_login PASSED
tests/test_saucedemo.py::test_tc03_add_backpack_to_cart PASSED
```

Kết luận chung: website SauceDemo hoạt động đúng với các chức năng cơ bản gồm đăng nhập, hiển thị danh sách sản phẩm và thêm sản phẩm vào giỏ hàng.

## Hướng dẫn chèn ảnh minh họa

Sau khi chạy test, chụp màn hình kết quả và lưu vào thư mục `screenshots`.

Tên ảnh nên đặt như sau:

```text
screenshots/saucedemo-home.png
screenshots/pytest-result.png
screenshots/login-success.png
screenshots/product-list.png
screenshots/cart-badge.png
```

Sau đó thêm ảnh lên GitHub:

```bash
git add screenshots/
git commit -m "Add test screenshots"
git push
```

Khi ảnh đã được thêm đúng đường dẫn, GitHub sẽ hiển thị ảnh trực tiếp trong README.
