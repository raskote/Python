# Задача:
# https://i.gyazo.com/703958c38c262fbdc835c455f9d758b4.png

# Решение:
n = int(input())
total = 0
for i in range(1, n+1):
    for j in range(i):
        total += 1
        print(total, end=" ")
    print()