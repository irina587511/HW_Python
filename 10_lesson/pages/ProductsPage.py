"""Страница каталога товаров магазина"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple


class ProductsPage:
    """Класс для работы со страницей каталога товаров."""

    def __init__(self, driver) -> None:
        """Инициализация страницы каталога.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self, product_id: str) -> None:
        """Добавить товар в корзину по ID кнопки.

        Args:
            product_id: ID кнопки добавления в корзину
        """
        add_btn: Tuple[str, str] = (By.ID, product_id)
        self.wait.until(EC.element_to_be_clickable(add_btn)).click()

    def go_to_cart(self) -> None:
        """Перейти в корзину."""
        cart_link: Tuple[str, str] = (By.CLASS_NAME, "shopping_cart_link")
        self.wait.until(EC.element_to_be_clickable(cart_link)).click()
