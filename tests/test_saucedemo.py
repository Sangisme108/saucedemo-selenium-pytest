import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
IMAGE_DIR = Path(__file__).resolve().parents[1] / "images"


def save_screenshot(driver, file_name):
    """Luu anh minh hoa vao thu muc images."""
    IMAGE_DIR.mkdir(exist_ok=True)
    driver.save_screenshot(str(IMAGE_DIR / file_name))


@pytest.fixture
def driver():
    """Khoi tao va dong trinh duyet Chrome cho moi test case."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(5)

    yield browser

    browser.quit()


def login(driver):
    """Dang nhap vao SauceDemo bang tai khoan hop le."""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()


def test_tc01_login_successfully(driver):
    """TC01: Dang nhap thanh cong voi standard_user."""
    driver.get(BASE_URL)
    save_screenshot(driver, "01-saucedemo-home.png")

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    save_screenshot(driver, "02-tc01-login-success.png")


def test_tc02_product_list_displayed_after_login(driver):
    """TC02: Kiem tra danh sach san pham hien thi sau khi dang nhap."""
    login(driver)

    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    assert len(products) > 0
    assert driver.find_element(By.CLASS_NAME, "inventory_item_name").is_displayed()
    save_screenshot(driver, "03-tc02-product-list.png")


def test_tc03_add_backpack_to_cart(driver):
    """TC03: Them Sauce Labs Backpack vao gio hang va kiem tra so luong la 1."""
    login(driver)

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    add_button.click()

    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert cart_badge.text == "1"
    save_screenshot(driver, "04-tc03-add-cart.png")
