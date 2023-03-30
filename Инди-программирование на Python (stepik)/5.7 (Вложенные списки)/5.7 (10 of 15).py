# Задача:
# https://i.gyazo.com/f7791af0e0b2ef410526204323f2df75.png

# Решение:
n, m = map(int, input().split())
li = []
max_sum_row = 0
sum_row = 0
num_row = 0
for i in range(n):
    li.append([int(i) for i in input().split()])
for j in range(n):
    sum_row = 0
    for k in range(m):
        sum_row += li[j][k]
    if sum_row > max_sum_row:
        max_sum_row = sum_row
        num_row = j
print(max_sum_row)
print(num_row)

# Альтернатива (not mine)
# n, m = map(int, input().split())
# sum_list = []
# for i in range(n):
#     sum_list.append(sum(list(map(int, input().split()))))
# print(max(sum_list), sum_list.index(max(sum_list)), sep='\n')