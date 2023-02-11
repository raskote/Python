Задача:
https://i.gyazo.com/a8de0a9f58d42bda03441673d1660921.png

Решение:
a,b = int(input()), int(input())
# a, b = 2,15
for i in range(a,b+1):
    count = 0
    for j in range(1, i+1):
        if i%j == 0:
            count +=1
    if count == 2:
        print(i)
