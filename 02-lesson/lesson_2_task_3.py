import math

def square(side):
    area = side * side
    if not isinstance(side, int):
        return math.ceil(area)
    else:
        return area

s = float(input("Введите цифрами значение стороны квадрата: "))
result = square(s)
print(f"если сторона квадрата равна {s}, его площадь будет равна {result}")