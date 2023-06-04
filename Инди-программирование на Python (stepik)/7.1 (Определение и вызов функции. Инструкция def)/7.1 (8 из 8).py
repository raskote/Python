# Задание:
# https://i.gyazo.com/f483a2c846a267360fa3342a1801ffea.png

# Решение:
def count_letters(stringa):
    N = [i for i in stringa if i.isupper()]
    K = [i for i in stringa if i.islower()]
    print(f'Количество заглавных символов: {len(N)}')
    print(f'Количество строчных символов: {len(K)}')

count_letters("ПриветСтарина")