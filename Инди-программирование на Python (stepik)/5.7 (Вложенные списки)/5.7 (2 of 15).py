# Задача:
# https://i.gyazo.com/647fb4c10a6b0b5aae7f211d409f68bb.png

# Решение:
n = int(input())
li = []
for i in range(n):
    li.append([int(i) for i in input().split()])
for j in range(n):
    for k in range(n):
        print(li[k][j], end= " ")
    print()



