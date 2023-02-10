# Задача:
# https://i.gyazo.com/fc804bc88ea734705ae6721ad0ec9338.png

# Решение:
a, b = int(input()), int(input())
max_sum = 0
num = 0
for i in range(a, b + 1):
    sum = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum += j
    if sum >= max_sum:
        num = i
        max_sum = sum
print(num, max_sum)
