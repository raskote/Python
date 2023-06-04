# Задание:
# https://i.gyazo.com/58120e21a8e794acdfd7dec0e6f511bc.png

# Решение:
# объявление функции
def is_between(name, surname, middlename):
    print(True if min(surname, middlename) <= name <= max(surname, middlename) else False)

# считываем данные
a, b, c = map(int, input().split())

# вызываем функцию
is_between(a, b, c)