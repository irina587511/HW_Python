"""Тесты для формы с различными типами данных."""
import allure
import pytest
from FormPage import FormPage
from conftest import chrome_driver


@allure.title("Проверка отправки формы с ошибкой ZIP-кода")
@allure.description("Заполнение формы → отправка → проверка ошибки ZIP и успеха остальных полей")
@allure.feature("Form Validation")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(chrome_driver):
    """Тест полного флоу отправки формы."""
    with allure.step("Открыть страницу формы"):
        form_page = FormPage(chrome_driver)
        form_page.open()

    with allure.step("Заполнить форму тестовыми данными"):
        form_page.fill_form()

    with allure.step("Отправить форму"):
        form_page.submit_form()

    with allure.step("Проверить результаты валидации"):
        form_page.check_form_submission()
