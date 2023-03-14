# Задание:
# https://i.gyazo.com/485c814c9a265f8c4f67cbe8263365ae.png

# Решение:
# объявление функции
def is_magic(date):
    return int(date[:2]) * int(date[3:5]) == int(date[-2:])

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))