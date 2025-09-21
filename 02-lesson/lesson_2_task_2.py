def is_year_leap(year):
    return True if year % 4 == 0 else False

ye = int (input ("Введите год цифрами: "))
result = is_year_leap(ye)
print(f"год {ye} : {result}")
