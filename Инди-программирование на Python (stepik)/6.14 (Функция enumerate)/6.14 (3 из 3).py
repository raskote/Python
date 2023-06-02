# Задание:
# https://i.gyazo.com/1349db4d4e6db280c0464a8c2936ac32.png

# Решение:
x = input()
summa = 0
for index, value in enumerate(reversed(x), 1):
    if index %2 == 0:
        value = int(value) * 2
        if value > 9:
            value -= 9
    summa = summa + int(value)
if summa % 10 == 0:
    print(True)
else:
    print(False)




