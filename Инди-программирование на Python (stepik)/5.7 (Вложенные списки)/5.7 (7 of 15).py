# Задача:
# https://i.gyazo.com/d361c6866ec631c8b076179b2ba299f2.png

# Решение:
n, m = map(int, input().split())
li = []
sum_row = 0
sum_col = 0
for i in range(n):
    li.append([int(i) for i in input().split()])
for j in range(n):
    sum_row = 0
    for k in range(m):
        sum_row += li[j][k]
    print(sum_row, end = " ")
print()
for v in range(m):
    sum_col = 0
    for b in range(n):
        sum_col += li[b][v]
    print(sum_col, end = " ")

# Альтернатива (not_mine):
# row, col = map(int, input().split())
# matrix = [list(map(int, input().split())) for row in range(row)]
# for row in matrix:
# 	print(sum(row), end=' ')
# print()
# for x in range(col):
# 	print(sum([row[x] for row in matrix]), end=' ')














