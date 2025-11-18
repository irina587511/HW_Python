from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(browser, 30, 0.1)

# Ждем, пока на странице появится не менее 4 картинок и все они загрузятся (naturalWidth > 0)
def all_images_loaded(browser):
    imgs =browser.find_elements(By.TAG_NAME, "img")
    if len(imgs) < 4:
        return False
    return all(img.get_attribute("naturalWidth") != '0' for img in imgs[:4])

wait.until(all_images_loaded)

imgs = browser.find_elements(By.TAG_NAME, "img")
src_value = imgs[2].get_attribute("src")
print("src 3-й картинки:", src_value)

browser.quit()
