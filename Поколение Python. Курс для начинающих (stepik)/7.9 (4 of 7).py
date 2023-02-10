# Задача:
# https://i.gyazo.com/b09f504cd5caf9c128435f2f9ff940b8.png

# Решение:
n = int(input())
for i in range(1, n+1):
    count = 0
    for j in range(1, i+1):
        if i%j == 0:
            count += 1
    print(i, '+'*count, sep="")