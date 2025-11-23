import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage


@pytest.fixture()
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.set_delay(45)
    calc_page.calculate_expression(["7", "+", "8", "="])
    result = calc_page.wait_for_result("15")
    assert result == "15", f"Expected result '15', but got '{result}'"