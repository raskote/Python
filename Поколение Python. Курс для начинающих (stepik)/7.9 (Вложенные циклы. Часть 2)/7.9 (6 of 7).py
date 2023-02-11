# Задача:
# https://i.gyazo.com/e7937da830703c933e4a938c439cad82.png

# Решение:
n = int(input())
prod = 1
sum = 0
for i in range(1, n+1):
    prod = 1
    for j in range(1, i+1):
        prod *= j
    sum += prod
print(sum)

#Альтернатива (mine):
# import math
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += math.factorial(i)
# print(sum)