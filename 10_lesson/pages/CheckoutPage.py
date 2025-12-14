"""Страница оформления заказа магазина"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver) -> None:
        """Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_input: Tuple[str, str] = (By.ID, "first-name")
        self.last_name_input: Tuple[str, str] = (By.ID, "last-name")
        self.postal_code_input: Tuple[str, str] = (By.ID, "postal-code")
        self.continue_button: Tuple[str, str] = (By.ID, "continue")
        self.total_label: Tuple[str, str] = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_info(self, first_name: str, last_name: str,
                           postal_code: str) -> None:
        """Заполнить информацию о покупателе.

        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс
        """
        self.wait.until(EC.visibility_of_element_located(
            self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self) -> None:
        """Нажать кнопку 'Продолжить'."""
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """Получить итоговую сумму заказа.

        Returns:
            Строка с суммой (например, '58.29')
        """
        total_text = self.wait.until(
            EC.visibility_of_element_located(self.total_label)).text
        return total_text.split("$")[-1].strip()
