# Задача:
# https://i.gyazo.com/e2d8d346d3c4a02f03a2e4d7df6ce112.png

# Решение:
n = int(input())
l = list(map(int, input().split()))
for i in range(2, n):
    x = l[i]
    j = i
    while j >=1 and l[j-1]>x:
        l[j] = l[j-1]
        j = j-1
    l[j] = x
print(*l)