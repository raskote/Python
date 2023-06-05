# Задание:
# https://i.gyazo.com/dc50592259f88817dd1960f69aa5b3fc.png

# Решение:
def factorial(n):
    pr = 1
    for i in range(2, n+1):
        pr *= i
    return pr

