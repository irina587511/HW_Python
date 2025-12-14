from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("http://uitestingplayground.com/textinput")

my_button = browser.find_element(By.CSS_SELECTOR, '#newButtonName')
my_button.send_keys('SkyPro')

blue_button = browser.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

content = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(content)

browser.quit()
