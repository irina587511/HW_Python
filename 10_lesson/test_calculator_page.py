"""Тесты медленного калькулятора."""
import allure
import pytest
from CalculatorPage import CalculatorPage
from conftest import chrome_driver


@allure.title("Тест медленного калькулятора 7+8=15")
@allure.description("Установка задержки 45с → выражение 7+8= → проверка результата")
@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(chrome_driver):
    """Тест вычисления 7+8 с задержкой."""
    with allure.step("Открыть калькулятор"):
        calc_page = CalculatorPage(chrome_driver)
        calc_page.open()

    with allure.step("Установить задержку 45 секунд"):
        calc_page.set_delay(45)

    with allure.step("Выполнить выражение 7+8="):
        calc_page.calculate_expression(["7", "+", "8", "="])

    with allure.step("Проверить результат равен 15"):
        result = calc_page.wait_for_result("15")
        assert result == "15", f"Expected result '15', but got '{result}'"
