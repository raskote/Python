# Задача:
# Программа получает на вход натуральное число N.

# Решение:
n = int(input())
i = 1
sum = 0
while i <= n:
    if n%i == 0:
        sum += n//i
        i += 1
    else:
        i += 1
print(sum)
