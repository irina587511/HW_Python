from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get('http://the-internet.herokuapp.com/inputs')
sleep(5)

input_field = driver.find_element(By.TAG_NAME, 'input')
input_field.send_keys('Sky')
sleep(10)   #  пауза, чтобы увидеть результат

input_field.clear()
sleep(10)   #  пауза, чтобы увидеть результат

input_field.send_keys('Pro')
sleep(10)  #  пауза, чтобы увидеть результат

driver.quit()
