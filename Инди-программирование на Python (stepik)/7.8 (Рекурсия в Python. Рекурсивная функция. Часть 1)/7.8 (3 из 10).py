# Задание:
# https://i.gyazo.com/52441a47fe00640680d30e5388028654.png

# Решение:
def back(n: int, li: list) -> None:
    if n > 0:
        print(li[n-1], end= " ")
        back(n - 1, li)

n = int(input())
li = [int(i) for i in input().split()]

back(n, li)