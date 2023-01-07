# Задача:
# https://i.gyazo.com/6b2f91f4daa4e2d9da33a8e8136fcd1a.png

# Решение:
s = int(input())
stek = list(map(int, input().split()))
numbers = [0] * 201
for i in stek:
    numbers[i] += 1
for i in range(-100, 101):
    if numbers[i]:
        print((str(i) + ' ') * numbers[i], end = "")
