"""Страница формы с различными типами данных."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Dict, List, Tuple


class FormPage:
    """Класс для работы со страницей формы."""

    def __init__(self, driver) -> None:
        """Инициализация страницы формы.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields: Dict[str, str] = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def open(self) -> None:
        """Открыть страницу формы."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_form(self) -> None:
        """Заполнить все поля формы тестовыми данными."""
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((By.NAME, field))).send_keys(value)

    def submit_form(self) -> None:
        """Отправить форму."""
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))).click()

    def get_field_class(self, field_id: str) -> str:
        """Получить CSS-класс поля формы.

        Args:
            field_id: ID поля

        Returns:
            Строка с CSS-классами
        """
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id)))
        return element.get_attribute("class")

    def check_zip_code_error(self) -> bool:
        """Проверить наличие ошибки в поле ZIP-кода.

        Returns:
            True если есть ошибка
        """
        return "alert-danger" in self.get_field_class("zip-code")

    def check_fields_success(self) -> bool:
        """Проверить успешное заполнение основных полей.

        Returns:
            True если все поля успешны
        """
        fields: List[str] = ['first-name', 'last-name', 'address', 'e-mail',
                             'phone', 'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    def check_form_submission(self) -> None:
        """Проверить корректность отправки формы."""
        assert self.check_zip_code_error()
        assert self.check_fields_success()
