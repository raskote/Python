# Задача:
# https://i.gyazo.com/1cfd6151a057a4b39afc436dcb8fe532.png

# Решение:
n = int(input())
pr = 1
for i in range(n):
    if n == 0:
        print(1)
        break
    pr += i * pr
print(pr)

# Альтернатива (not mine)
# n = int(input())
# s = 1
# for i in range(1, n+1):
#     s *= i
# print(s)