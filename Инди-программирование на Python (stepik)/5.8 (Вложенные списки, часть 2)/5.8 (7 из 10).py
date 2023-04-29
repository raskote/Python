# Задача:
# https://i.gyazo.com/030666280007f0c1e1b099e6e655715f.png

# Решение:
n, m = map(int, input().split())
li = []
start, first = 0, m
for i in range(n):
    row = [i for i in range(start, m)]
    li.append(row)
    start, m = m, m+first
for i in range(n):
    if i % 2 != 0:
        print(*li[i][::-1])
    else:
        print(*li[i])

# Альтернатива (not mine)
# n, m = map(int, input().split())
# for i in range(n):
#     if i % 2 == 0:
#         print(*list(range(i * m, i * m + m)))
#     else:
#         print(*list(range(i * m, i * m + m))[::-1])