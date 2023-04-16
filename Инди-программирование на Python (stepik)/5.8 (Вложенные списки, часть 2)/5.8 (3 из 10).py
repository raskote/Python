# Задача:
# https://i.gyazo.com/d50b3bc1be1411c12ed72dacc1adaa0b.png

# Решение:
n = int(input())
a_li, b_li = [], []
count = 0
for i in range(n):
    a, b = map(int, input().split())
    a_li.append(a)
    b_li.append(b)
for i in range(n):
    for j in range(n):
        if a_li[i] == b_li[j]:
            count += 1
print(count)

# Альтернатива (not_mine)
# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]
# count = 0
# for i in range(n):
#     for j in range(n):
#         if a[i][0] == a[j][1]:
#             count += 1
# print(count)
