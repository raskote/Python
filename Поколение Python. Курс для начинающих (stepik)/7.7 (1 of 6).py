# Задача
# https://i.gyazo.com/25a577187d33482e0c0d4508f288a199.png

# Решение:
count = 0
p = 1
for i in range(10):
    x = int(input())
    if x > 0:
        p *= x
        count += 1
if count:
    print(count)
    print(p)
else:
    print('NO')