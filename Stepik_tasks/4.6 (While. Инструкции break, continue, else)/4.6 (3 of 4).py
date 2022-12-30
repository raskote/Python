# Задача:
# https://i.gyazo.com/040be7fecdf716f9279e52a9c51f35c4.png

# Решение:
n = int(input())
count = 0
while n != 1:
    if n%2==0:
        n /= 2
    else:
        n = 3*n+1
    count += 1
print(count)

# Альтернатива (not mine)
