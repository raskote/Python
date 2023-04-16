# Задача:
# https://i.gyazo.com/4ce2fad4e99816dd4610ca2b7a1a99a4.png

# Решение:
n, m = map(int, input().split())
triangle = [list(map(int, input().split())) for i in range(n)]
for i in range(1, n):
    for j in range(1, m):
        triangle[i][j] = triangle[i-1][j] + triangle[i][j-1]
for i in range(n):
    print(*triangle[i])