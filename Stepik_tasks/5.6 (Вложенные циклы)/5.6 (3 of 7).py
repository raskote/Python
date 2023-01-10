# Задача:
# https://i.gyazo.com/bd23d4be75aba4602ae29d6e33669922.png

# Решение:
n = list(map(int, input().split()))
for i in range(0, len(n)):
    for j in range(1, n[i]+1):
        print("*", end = "")
    print()

# Альтернатива_1 (not mine):
# a = input().split()
# for i in a:
#     print('*' * int(i))

# Альтернатива_2 (not mine):
# lst = list(map(int, input().split()))
# for i in lst:
#     for j in range(i):
#         print('*', end='')
#     print()