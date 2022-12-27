# Задача:
# https://i.gyazo.com/0f205f5edafcc21bec8ed3016f326d33.png

# Решение:
x = int(input())
summa = 1
while x > 0:
    summa *= x%10
    x = x // 10
print(summa)
