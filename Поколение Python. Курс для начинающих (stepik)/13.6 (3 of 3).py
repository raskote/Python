# Задача:
# https://i.gyazo.com/597af078c3172ae81b2ef58f59a6ba47.png

# Решение:
# объявление функции
def solve(a, b, c):
    import math
    d = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return min(x1, x2), max(x1, x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)