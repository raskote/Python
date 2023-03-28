# Задача:
# https://i.gyazo.com/ded25c67bf5e32f695d500b8eb908794.png

# Решение:
n, m = map(int, input().split())
li = []
for i in range(n):
    li.append([int(i) for i in input().split()])
for j in range(n):
    for k in range(m):
        print(li[n-1-j][k], end= " ")
    print()







