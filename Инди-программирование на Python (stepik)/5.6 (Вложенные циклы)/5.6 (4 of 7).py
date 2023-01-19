# Задача:
# https://i.gyazo.com/9cee9526e898a823333f7685623a2c58.png

# Решение:
n = int(input())
sum = 0
for p in range(n+1, 2*n):
    count = 1
    for i in range(1, int(p**0.5)+1):
        if p%i == 0:
            count += 1
    if count == 2:
        sum += 1
print(sum)

# Альтернатива_1 (not mine):
# n = int(input())
# a = 0
# for i in range(n + 1, n * 2):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         a += 1
# print(a)
