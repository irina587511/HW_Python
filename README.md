# HW_Python
Lessons_Python

Запуск тестов с генерацией данных для Allure

pytest --alluredir=allure-results

Или с подробным выводом:
pytest --alluredir=allure-results -v -s

Результат: Создается папка allure-results/ с XML/JSON файлами результатов тестов.

Просмотр сформированного Allure отчета
Автоматическое открытие в браузере 
allure serve allure-results
Результат: Отчет автоматически откроется в браузере по адресу http://localhost:5050