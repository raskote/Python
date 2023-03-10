# Задача:
# https://i.gyazo.com/c8ecb16e9835b0f5e073e03c0ead9b7e.png

# Решение:
# объявление функции
def convert_to_python_case(text):
    li = []
    li.append(text[0].lower())
    for i in range(1, len(text)):
        if text[i].isupper():
            li.append('_')
            li.append(text[i].lower())
        else:
            li.append(text[i].lower())
    return "".join(li)
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

# Альтернативное решение (not mine)
# def convert_to_python_case(text):
#     s = ''
#     for el in text:
#         if el.isupper():
#             s += '_'
#         s += el.lower()
#     return s[1:]
#
#
# print(convert_to_python_case(input()))