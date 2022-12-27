# Задача:
# https://i.gyazo.com/1187e1c882c45d8f7ce614b74fc39432.png

# Решение:
x = int(input())
summa = 0
while x > 0:
    summa = summa + x%10
    x = x // 10
print(summa)

# Альтернатива (not mine):
# print(sum(map(int, list(input()))))