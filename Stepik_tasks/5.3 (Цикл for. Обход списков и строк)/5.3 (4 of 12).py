# Задача:
# https://i.gyazo.com/49ff64e12662d3b26fdb9a258c38cd2a.png

# Решение:
n = int(input())
word = []
for i in range(n):
    word.append(input())
print(word)

# Альтернатива_1 (not mine):
# print([input() for _ in range(int(input()))])

# Альтернатива_2 (not mine):
# n = int(input())
# a = [input() for _ in range(n)]
# print(a)