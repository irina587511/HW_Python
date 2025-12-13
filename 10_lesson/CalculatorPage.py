"""Страница медленного калькулятора."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Tuple


class CalculatorPage:
    """Класс для работы с медленным калькулятором."""

    def __init__(self, driver) -> None:
        """Инициализация страницы калькулятора.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)
        self.delay_input_locator: Tuple[str, str] = (By.ID, "delay")
        self.result_locator: Tuple[str, str] = (By.CSS_SELECTOR, "#calculator .screen")

    def open(self) -> None:
        """Открыть страницу калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_value: int) -> None:
        """Установить задержку для кнопок.

        Args:
            delay_value: Значение задержки в секундах
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.delay_input_locator))
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def press_button(self, btn_text: str) -> None:
        """Нажать кнопку калькулятора.

        Args:
            btn_text: Текст кнопки (например, '7', '+', '=')
        """
        btn_locator: Tuple[str, str] = (By.XPATH, f"//span[text()='{btn_text}']")
        btn = self.wait.until(EC.element_to_be_clickable(btn_locator))
        btn.click()

    def calculate_expression(self, expression_list: List[str]) -> None:
        """Выполнить математическое выражение.

        Args:
            expression_list: Список кнопок для нажатия (например, ['7', '+', '8', '='])
        """
        for btn in expression_list:
            self.press_button(btn)

    def get_result(self) -> str:
        """Получить результат вычисления.

        Returns:
            Строка с результатом
        """
        return (self.wait.until(
            EC.text_to_be_present_in_element(self.result_locator, "")
        ) or self.driver.find_element(*self.result_locator).text)

    def wait_for_result(self, expected_result: str) -> str:
        """Ожидать и получить результат.

        Args:
            expected_result: Ожидаемый результат

        Returns:
            Строка с результатом
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.result_locator, str(expected_result))
        )
        return self.driver.find_element(*self.result_locator).text

