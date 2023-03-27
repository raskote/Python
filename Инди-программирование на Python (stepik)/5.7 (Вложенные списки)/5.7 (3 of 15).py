# Задача:
# https://i.gyazo.com/3f1fac3566ea47e6e25551e145b0d8d8.png

# Решение:
n = int(input())
li = []
for i in range(n):
    li.append([int(i) for i in input().split()])
for j in range(n):
    for k in range(n):
        print(li[n-1-k][n-1-j], end= " ")
    print()











