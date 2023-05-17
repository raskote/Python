# Задача:
# https://i.gyazo.com/c34a5a2309dc280f830d5b2a5ad12443.png

# Решение:
l = list(map(int, input().split()))
li = [{} for i in range(len(l))]
n = len(l)-2
li[-1].setdefault(l[-2], l[-1])
while n > 0:
    li[n].setdefault(l[n-1], li[n+1])
    n -= 1
print(li[1])
