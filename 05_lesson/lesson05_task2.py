from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/dynamicid')
sleep(2)  #  короткая пауза для загрузки страницы

# Синяя кнопка на этой странице имеет класс btn-primary, используем его корректно
blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()

sleep(5)  #  пауза, чтобы увидеть результат клика

driver.quit()
