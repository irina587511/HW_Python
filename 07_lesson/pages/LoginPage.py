from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        elem = self.wait.until(EC.visibility_of_element_located(self.username_input))
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.wait.until(EC.visibility_of_element_located(self.password_input))
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        