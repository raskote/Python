# Задание:
# https://i.gyazo.com/5bde833a500b68dab950f61aa65055f5.png

# Решение:
def number_to_words(num):
    li_1 = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    li_2 = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    if 1 <= num <= 19:
        return(li_1[num-1])
    elif num in [20, 30, 40, 50, 60, 70, 80, 90]:
        return li_2[num//10-2]
    elif 21 <= num <= 99:
        return li_2[num//10-2] + " " +  li_1[num%10-1]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))