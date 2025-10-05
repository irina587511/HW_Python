from address import Address
from mailing import Mailing

to_addr = Address("564825", "Москва", "Ленина", "10", " - 5")
from_addr = Address("163758", "Санкт-Петербург", "Ленина", "20", " - 12")

mailing_instance = Mailing(to_addr, from_addr, 500.00, "TRACK123")

print(    f"Отправление {mailing_instance.track} из {mailing_instance.from_address.index}, {mailing_instance.from_address.city}, "
    f"{mailing_instance.from_address.street}, {mailing_instance.from_address.house} {mailing_instance.from_address.apartment} в "
    f"{mailing_instance.to_address.index}, {mailing_instance.to_address.city}, {mailing_instance.to_address.street}, "
    f"{mailing_instance.to_address.house} {mailing_instance.to_address.apartment}. Стоимость {mailing_instance.cost} рублей")
