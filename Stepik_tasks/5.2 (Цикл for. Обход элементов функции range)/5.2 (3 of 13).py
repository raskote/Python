# Задача:
# https://i.gyazo.com/bb4df5c4613092a2b6c6efc62d2ffd51.png

# Решение:
n = int(input())
for i in range(n, 0, -1):
    print(i)

# Альтернатива (not mine)
# print(*range(0, 501, 5), sep='\n')