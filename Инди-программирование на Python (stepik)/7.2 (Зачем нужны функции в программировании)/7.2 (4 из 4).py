# Задание:
# https://i.gyazo.com/d88aa6f8bc766155968083ca62e64f68.png

# Решение:
# объявление функции
def print_initials(name, surname, middlename):
    print(f'{surname.title()} {name[0].upper()}.{middlename[0].upper()}.')

# считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print_initials(name, surname, middlename)