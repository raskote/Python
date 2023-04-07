# Задача:
# https://i.gyazo.com/a8077546f7f621f31ff2d5acd499bffd.png

# Решение:
n, m = map(int, input().split())
count = 0
foto = [input() for i in range(n)]
input()
nega = [input() for i in range(n)]
for i in range(n):
    for j in range(m):
        if foto[i][j] == nega[i][j]:
            count += 1
print(count)