# Задача
# https://i.gyazo.com/25a577187d33482e0c0d4508f288a199.png

# Решение:
mx = -1
s = 0
for _ in range(10):
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
print(s)
print(mx)