# Задача:
# https://i.gyazo.com/fc804bc88ea734705ae6721ad0ec9338.png

# Решение:
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end = "")
#     for j in range(1, i):
#         print(i-j, end = "")
#     print()

#Альтернатива (not mine):
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 2 * i):
#         print(min(j, 2 * i - j), end='')
#     print()