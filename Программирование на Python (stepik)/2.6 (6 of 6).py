# Задача:
# https://i.gyazo.com/712298b1ce4388d4ac7d0a87ad96c37b.png

# Решение:
n = int(input())
for i in range(1, n):
    print(i, end=" ")
    for j in range(n):
        print(j, end= " ")