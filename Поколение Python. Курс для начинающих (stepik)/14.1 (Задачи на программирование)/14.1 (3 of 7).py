# Задание:
# https://i.gyazo.com/d43f693681d7f05514cd3e146c5e8872.png

# Решение:
def compute_binom(n, k):
    import math
    return int(math.factorial(n)/(math.factorial(k)*(math.factorial(n-k))))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
