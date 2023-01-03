# Задача:
# https://i.gyazo.com/a8af4e5bcbe1e2d2c46ab2991cbde805.png

# Решение:
n = input()
count = 0
sum = 0
for i in range(1, len(n)):
    if n[i].isdigit():
        count += 1
        sum += int(n[i])
print(count, sum)

# Альтернатива_1 (not mine)
a = [int(i) for i in input() if i.isdigit()]
print(len(a), sum(a))

# Альтернатива_2 (not mine)
s, n = list(input()), []
for i in s:
    if i.isdigit():
         n.append(int(i))
print(len(n), sum(n))