# Задание:
# https://i.gyazo.com/9c0c9f367079d734b72b83e022713b07.png

# Решение:
def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))