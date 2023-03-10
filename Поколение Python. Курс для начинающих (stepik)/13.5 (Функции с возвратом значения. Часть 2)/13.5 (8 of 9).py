# Задача:
# https://i.gyazo.com/24acdb064fcd1970efd26e2c3c21381b.png

# Решение:
# объявление функции
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return False if text else True


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))