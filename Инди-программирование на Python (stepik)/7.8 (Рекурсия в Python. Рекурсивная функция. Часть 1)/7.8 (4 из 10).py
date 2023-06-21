# Задание:
# https://i.gyazo.com/3f19c56b23c989e66ee193a3605ec1ab.png

# Решение:
def double_fact(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return double_fact(n-2) * n

print(double_fact(5))