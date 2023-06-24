# Задание:
# https://i.gyazo.com/46c39547e53c1d5daa30dfe8bbb24639.png

# Решение:
def ackermann (m: int, n: int):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m-1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n-1))

m, n = int(input()), int(input())
print(ackermann(m, n))