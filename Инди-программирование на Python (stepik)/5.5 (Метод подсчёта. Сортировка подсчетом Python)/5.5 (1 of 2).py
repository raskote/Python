# Задача:
# https://i.gyazo.com/4f6cea25373162516a27fe0856958107.png

# Решение:
n = [int(i) for i in input()]
y = max(n) + 1
count = [0] * y
for i in n:
    count[i] += 1
for i in range(y):
    if count[i] > 0:
        print(i, count[i])

# Альтернатива (not mine):
# n = input()
# for i in range(10):
#     if str(i) in n:
#         print(i, n.count(str(i)))
