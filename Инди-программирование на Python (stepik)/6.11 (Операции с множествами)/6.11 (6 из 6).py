# Задание:
# https://i.gyazo.com/ab2e049113bda1d0efe304a7bcc853de.png

# Решение:
n = int(input())
while n > 0:
    x = map(int, input().split())
    print(len(set(x)))
    n -= 1