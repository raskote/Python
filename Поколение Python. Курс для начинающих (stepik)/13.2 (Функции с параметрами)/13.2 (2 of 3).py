# Задача:
# https://i.gyazo.com/a17729998a1269686e35a4a25d973f9a.png

# Решение:
# объявление функции
def print_fio(name, surname, patronymic):
    print(name[0].upper(), surname[0].upper(), patronymic[0].upper(), sep="")

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(surname, name, patronymic)