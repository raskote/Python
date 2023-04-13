# Задача:
# https://i.gyazo.com/c205ebeddb65cad7a6af8a88f6f7f188.png

# Решение:
# n, m = map(int, input().split())
# li = [input() for i in range(n)]
n, m = 4, 4
li = ["......",".****.", ".**...", ".*....", ".*....", "......"]
print(*li, sep = "\n")
new_li = []


count = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if li[i][j] == ".":
            if li[i+1][j] != "*" and li[i][j+1] != "*" and li[i+1][j+1] != "*" and li[i-1][j] != "*" and li[i][j-1] != "*" and li[i-1][j-1] != "*":
                count += 1
print(count)