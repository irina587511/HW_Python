import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shopping_flow(driver):
    wait = WebDriverWait(driver, 10)
    url = "https://www.saucedemo.com/"
    driver.get(url)

    # Авторизация
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    products_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for product_id in products_to_add:
        btn = wait.until(EC.element_to_be_clickable((By.ID, product_id)))
        btn.click()

    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    # Заполняем форму данных
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Irina")
    driver.find_element(By.ID, "last-name").send_keys("Maksimova")
    driver.find_element(By.ID, "postal-code").send_keys("214000")

    driver.find_element(By.ID, "continue").click()

    total_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    # Текст обычно в формате: "Total: $58.29"
    total_value = total_text.split("$")[-1].strip()
    print(f"Полученная итоговая сумма: {total_value}")

    assert total_value == "58.29", f"Итоговая сумма ожидалась $58.29, полученная итоговая сумма ${total_value}"
