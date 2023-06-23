# Задание:
# https://i.gyazo.com/d74e707aa5e1157fe027ba1c2af962c4.png

# Решение:
def tribonacci(n: int):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

n = int(input())
print(tribonacci(n))