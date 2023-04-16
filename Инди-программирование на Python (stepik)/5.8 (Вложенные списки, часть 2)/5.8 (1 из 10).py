# Задача:
# https://i.gyazo.com/792990f0964271c5e3923e7e1d4b3c9c.png

# Решение:
n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
new_li = []
max_sum = 0
for i in range(n):
    row = []
    for j in range(n-i):
        row.append(li[i][j])
    new_li.append(row)
for i in range(n):
    if new_li[i][-1] > max_sum:
        max_sum = new_li[i][-1]
print(max_sum)

# Альтернатива (not mine):
# n = int(input())
# mx = [list(map(int, input().split())) for i in range(n)]
# s = []
# for i in range(n):
#     s.append(mx[i][n-i-1])
# print(max(s))