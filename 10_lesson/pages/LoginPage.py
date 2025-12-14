"""Страница авторизации магазина"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver) -> None:
        """Инициализация страницы авторизации.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input: Tuple[str, str] = (By.ID, "user-name")
        self.password_input: Tuple[str, str] = (By.ID, "password")
        self.login_button: Tuple[str, str] = (By.ID, "login-button")

    def open(self) -> None:
        """Открыть страницу авторизации."""
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str) -> None:
        """Ввести имя пользователя.

        Args:
            username: Имя пользователя
        """
        elem = self.wait.until(EC.visibility_of_element_located(
            self.username_input))
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password: str) -> None:
        """Ввести пароль.

        Args:
            password: Пароль
        """
        elem = self.wait.until(EC.visibility_of_element_located(
            self.password_input))
        elem.clear()
        elem.send_keys(password)

    def click_login(self) -> None:
        """Нажать кнопку входа."""
        self.wait.until(EC.element_to_be_clickable(
            self.login_button)).click()
