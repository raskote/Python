# Задача:
# https://i.gyazo.com/50fe2e9498e9baec686951ac3af895a6.png

# Решение:
li = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# for i in range(5):
#     li.append([int(i) for i in input().split()])
print(li)
for j in range(5):
    for k in range(5):
        if li[j][k] == 1:
            print(abs(j-2)+abs(k-2))














