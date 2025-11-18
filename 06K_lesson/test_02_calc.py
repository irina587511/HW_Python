import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    # Используем ChromeDriverManager для автоматического управления и скачивания chromedriver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    wait = WebDriverWait(driver, 50)  # Ожидание результата до 50 секунд (без sleep)

    # Ввод значения 45 в поле с id="delay"
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажатие кнопок 7, +, 8, =
    for btn_text in ["7", "+", "8", "="]:
        button = driver.find_element(By.XPATH, f"//span[text()='{btn_text}']")
        button.click()

    # Ожидаем появления результата "15" в окне калькулятора
    result_locator = (By.CSS_SELECTOR, "#calculator .screen")
    wait.until(EC.text_to_be_present_in_element(result_locator, "15"))

    result_text = driver.find_element(*result_locator).text
    print(f"Результат вычисления: {result_text}")
    assert result_text == "15", f"Ожидался результат 15, получено {result_text}"

