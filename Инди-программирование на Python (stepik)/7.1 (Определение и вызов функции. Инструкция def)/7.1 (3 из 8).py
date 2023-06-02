# Задание:
# https://i.gyazo.com/59622a30804384cee43b807934da798d.png

# Решение:
def summa_n(t):
    summa = 0
    for i in range(1, t+1):
        summa += i
    print(f'Я знаю, что сумма чисел от 1 до {t} равна {summa}')
