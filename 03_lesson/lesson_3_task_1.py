from user import User
# Создаем экземпляр класса User
my_user = User("Ирина", "Максимова")
# Вызываем методы и выводим результаты
print(my_user.get_first_name())# Ожидаемый результат: "Ирина"
print(my_user.get_last_name())# Ожидаемый результат: "Максимова"
print(my_user.get_user_info())# Ожидаемый результат: "first_name: Ирина, last_name: Максимова"
