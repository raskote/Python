# Задача:
# https://i.gyazo.com/d9d2579c69903d4dd8ec65f88ef5bba4.png

# Решение:
n, m = map(int, input().split())
li = []
for i in range(n):
    li.append([int(i) for i in input().split()])
for j in range(n):
    for k in range(m):
        print(li[j][m-1-k], end= " ")
    print()








