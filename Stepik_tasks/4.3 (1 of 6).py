# Задача:
# https://i.gyazo.com/1cc1ea9b84144022d5a268d3004276c8.png

# Решение:
x = int(input())
while x > 0:
    print(x%10)
    x = x // 10

# Альтернатива (not mine):
# print('\n'.join(input()[::-1]))