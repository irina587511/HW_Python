"""E2E тест шоппинг-флоу saucedemo.com."""
import allure
import pytest
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from conftest import firefox_driver


@allure.title("Полный шоппинг-флоу: логин → товары → корзина → оплата")
@allure.description("Авторизация → добавление 3 товаров → оформление → проверка суммы $58.29")
@allure.feature("E2E Shopping")
@allure.severity(allure.severity_level.BLOCKER)
def test_shopping_flow(firefox_driver):
    """Тест полного процесса покупки."""
    login_page = LoginPage(firefox_driver)
    products_page = ProductsPage(firefox_driver)
    cart_page = CartPage(firefox_driver)
    checkout_page = CheckoutPage(firefox_driver)

    with allure.step("Открыть страницу логина"):
        login_page.open()

    with allure.step("Ввести учетные данные standard_user"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")

    with allure.step("Выполнить вход в систему"):
        login_page.click_login()

    products_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    with allure.step("Добавить 3 товара в корзину"):
        for product_id in products_to_add:
            products_page.add_product_to_cart(product_id)

    with allure.step("Перейти в корзину"):
        products_page.go_to_cart()

    with allure.step("Начать оформление заказа"):
        cart_page.click_checkout()

    with allure.step("Заполнить данные покупателя и продолжить"):
        checkout_page.fill_checkout_info("Irina", "Maksimova", "214000")
        checkout_page.click_continue()

    with allure.step("Проверить итоговую сумму $58.29"):
        total = checkout_page.get_total()
        assert total == "58.29", f"Expected total $58.29 but got ${total}"
