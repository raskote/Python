# Задача:
# https://i.gyazo.com/3ec51ab32631bf1bed93473683a8ffdd.png

# Решение:
x = int(input())
minimum = 9
maximum = 0
while x > 0:
    if x%10 < minimum:
        minimum = x%10
    if x%10 > maximum:
        maximum = x%10
    x = x // 10
print(minimum, '\n', maximum, sep="")

# Альтернатива (not mine):
s = sorted(input())
print(s[0], s[-1], sep = '\n')