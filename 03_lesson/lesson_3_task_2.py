from smartphone import Smartphone

# Создаем каталог смартфонов
catalog = [
Smartphone("iPhone", "16 Pro", "+79112345897"),
Smartphone("Samsung", "Galaxy Z Fold 7", "+79116875898"),
Smartphone("Xiaomi", "Mi 15", "+79112345899"),
Smartphone("Google", "Pixel 9 ", "+79112345891"),
Smartphone("Huawei", "Pura 70 Ultra", "+79112345890")
]

# Печатаем каталог смартфонов
for smartphone in catalog:
    print(f"{smartphone.make} - {smartphone.model} - {smartphone.phone_number}")
