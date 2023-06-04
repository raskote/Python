# Задание:
# https://i.gyazo.com/7c11e4c044303f767c99e022dd529981.png

# Решение:
# объявление функции
def count_letter(text, letter):
    print(text.count(letter))

# считываем данные
text = input()
symbol = input()
# вызываем функцию
count_letter(text, symbol)