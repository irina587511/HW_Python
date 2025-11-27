from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self, product_id):
        add_btn = (By.ID, product_id)
        self.wait.until(
            EC.element_to_be_clickable(add_btn)).click()

    def go_to_cart(self):
        cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.wait.until(EC.element_to_be_clickable(cart_link)).click()
