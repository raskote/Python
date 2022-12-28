# Задача:
# Какова сумма всех натуральных делителей числа 34?

# Решение:
n = 34
i = 1
sum = 0
while i <= n:
    if n%i == 0:
        sum += n//i
        i += 1
    else:
        i += 1
print(sum)

# Альтернатива (not mine):
# n = int(input())
# i = 1
# sum = 0
# while i <= n:
#     if n % i == 0:
#         sum += i
#     i += 1
# print(sum)