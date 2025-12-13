"""Страница корзины интернет-магазина"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Tuple


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver) -> None:
        """Инициализация страницы корзины.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.checkout_button: Tuple[str, str] = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """Нажать кнопку оформления заказа."""
        self.wait.until(EC.element_to_be_clickable(
            self.checkout_button)).click()

    def get_cart_items(self) -> List:
        """Получить список элементов корзины.

        Returns:
            List of WebElement objects в корзине
        """
        items_locator: Tuple[str, str] = (By.CLASS_NAME, "cart_item")
        return self.wait.until(
            EC.presence_of_all_elements_located(items_locator)
        )
