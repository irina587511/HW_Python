from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/classattr')
sleep(5)  #  короткая пауза для загрузки страницы

blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()

sleep(10)   #   пауза, чтобы увидеть результат клика

driver.quit()
