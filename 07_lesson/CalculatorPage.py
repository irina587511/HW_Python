from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)
        self.delay_input_locator = (By.ID, "delay")
        self.result_locator = (By.CSS_SELECTOR, "#calculator .screen")

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay_value):
        delay_input = (self.wait.until
                       (EC.presence_of_element_located
                        (self.delay_input_locator)
                        )
                       )
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def press_button(self, btn_text):
        btn_locator = (By.XPATH, f"//span[text()='{btn_text}']")
        btn = self.wait.until(EC.element_to_be_clickable(btn_locator))
        btn.click()

    def calculate_expression(self, expression_list):
        for btn in expression_list:
            self.press_button(btn)

    def get_result(self):
        return (
                self.wait.until(
                    EC.text_to_be_present_in_element(
                        self.result_locator, ""
                    )
                ) or self.driver.find_element(*self.result_locator).text
        )

    def wait_for_result(self, expected_result):
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.result_locator, str(expected_result)
            )
        )
        return self.driver.find_element(*self.result_locator).text
