# Задача:
# https://i.gyazo.com/e2d8d346d3c4a02f03a2e4d7df6ce112.png

# Решение:
n = int(input())
l = list(map(int, input().split()))
for i in range(1, n):
    x = l[i]
    j = i
    while j >=1 and l[j-1]>x:
        l[j] = l[j-1]
        j = j-1
    l[j] = x
print(*l)

# Альтернатива (not mine):
# n = int(input())
# d = list(map(int, input().split()))
# for i in range(1, n):
#     for j in range(i - 1, -1, -1):
#         if d[i] < d[j]:
#             continue
#         else:
#             j += 1
#             break
#     if d[j] > d[i]:
#         d.insert(j, d.pop(i))
# print(*d)