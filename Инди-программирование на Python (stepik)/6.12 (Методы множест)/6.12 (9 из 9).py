# Задание:
# https://i.gyazo.com/9855872fb9749ac36ef2e9a5cc350a95.png

# Решение:
b = set()
for x in input():
    if x not in b:
        print(x, end='')
    b.add(x)

# Альтернатива (not mine):
# s = input()
# print(''.join(sorted(set(s), key=s.index)))