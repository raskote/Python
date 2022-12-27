# Задача:
# https://i.gyazo.com/904f5e1c0cfd1a8f62645b396b517144.png

# Решение:
x = int(input())
count = 0
while x > 0:
    if x%10 == 7:
        count += 1
    x = x // 10
print(count)

# Альтернатива (not mine):
# print(input().count('7'))
