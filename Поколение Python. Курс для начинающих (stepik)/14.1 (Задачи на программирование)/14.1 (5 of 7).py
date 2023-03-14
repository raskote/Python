# Задание:
# https://i.gyazo.com/938b033f2a0de90b234c41a92e275f41.png

# Решение:
# объявление функции
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']
    if language == "ru":
        return lng_ru[number-1]
    elif language == "en":
        return lng_en[number-1]

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))

# Альтернативное решение (not mine):
# from calendar import month_name
# import locale
#
# # объявление функции
# def get_month(language, number):
#     if language == 'ru':
#         locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#     return month_name[number].lower()
#
#
# # считываем данные
# lan = input()
# num = int(input())
#
# # вызываем функцию
# print(get_month(lan, num))