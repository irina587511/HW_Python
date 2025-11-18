import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    edge_driver_path = r"C:\Users\irina\Desktop\Python\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_fill_form_and_validate_colors(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    zip_div = driver.find_element(By.ID, "zip-code")
    zip_class = zip_div.get_attribute("class")
    assert "alert-danger" in zip_class, "Поле Zip code не подсвечено красным (alert-danger)"

    valid_field_ids = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]

    all_valid = True
    for field_id in valid_field_ids:
        elem = driver.find_element(By.ID, field_id)
        elem_class = elem.get_attribute("class")
        if "alert-success" not in elem_class:
            all_valid = False
            print(f"Поле {field_id} не подсвечено зеленым (alert-success), текущий класс: {elem_class}")

    assert all_valid, "Некоторые поля не подсвечены зеленым (alert-success) как ожидается."

    print("Проверка пройдена: поле Zip code подсвечено красным, остальные поля зелёным.")
