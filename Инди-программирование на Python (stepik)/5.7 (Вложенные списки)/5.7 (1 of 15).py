# Задача:
# https://i.gyazo.com/c089965a9c652dace05c750e1856952e.png

# Решение:
n = int(input())
li = []
for i in range(n):
    li.append([int(i) for i in input().split()])
sum = 0
for j in range(n):
    for k in range(n):
        if j == k:
            sum += li[j][k]
print(sum)

# Решение (not mine):
# n = int(input())
# s = 0
# for i in range(n):
#     s += int(input().split()[i])
# print(s)
