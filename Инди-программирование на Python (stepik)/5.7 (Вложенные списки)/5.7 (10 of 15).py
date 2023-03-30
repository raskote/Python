# Задача:
# https://i.gyazo.com/f7791af0e0b2ef410526204323f2df75.png

# Решение:
n, m = map(int, input().split())
li = []
max_try, row, col = 0, 0, 0
for i in range(n):
    li.append([int(i) for i in input().split()])
for j in range(n):
    max_try
    for k in range(m):
        if max_try < li[j][k]:
            max_try = li[j][k]
            row = j
            col = k
print(max_try)
print(row, col)

# Альтернатива (not mine)
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(n)]
#
# b = [max(i) for i in a]
# print(max(b))
# print(b.index(max(b)), a[b.index(max(b))].index(max(b)))