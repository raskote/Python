# Задача:
# https://i.gyazo.com/f9ce6d5136fd9288637548c476d4b453.png

# Решение:
n = int(input())
a,b,c = map(int, input().split())
li = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(a)
    li.append(row)
for i in range(n):
    for j in range(n):
        if i == j:
            li[i][j] = c
        if i > j:
            li[i][j] = b
    print(*li[i])