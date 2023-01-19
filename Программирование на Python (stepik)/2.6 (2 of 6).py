# Задача:
# https://i.gyazo.com/b1b3cb65a94f28e918dcc314390e2cfc.png

# Решение:
a = 0
sum_square = 0
while True:
    x = int(input())
    a += x
    sum_square += int(x ** 2)
    if a == 0:
        break
print(int(sum_square))

# Альтернатива (not mine):
# s=[int(input())]
# while sum(s)!=0: s.append(int(input()))
# print(sum([i**2 for i in s]))