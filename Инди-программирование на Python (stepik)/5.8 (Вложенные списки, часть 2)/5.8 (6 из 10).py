# Задача:
# https://i.gyazo.com/adb8e6a576128024fefd260f9bc770c4.png

# Решение:
n, m = map(int, input().split())
triangle = [list(map(int, input().split())) for i in range(n)]
triangle.reverse()
for i in range(n):
    triangle[i].reverse()
for i in range(1, n):
    for j in range(1, m):
        triangle[i][j] = triangle[i-1][j] + triangle[i][j-1]
triangle.reverse()
for i in range(n):
    triangle[i].reverse()
    print(*triangle[i])

# Альтернатива (not mine):
# n, m = map(int, input().split())
# trangle = [(list(map(int, input().split()))) for _ in range(n)]
#
# for i in reversed(range(n - 1)):
#     for j in reversed(range(m - 1)):
#         trangle[i][j] = trangle[i][j+1] + trangle[i+1][j]
#
# for i in range(0, n):
#     for j in range(0, m):
#         print(trangle[i][j], end=' ')
#     print()
