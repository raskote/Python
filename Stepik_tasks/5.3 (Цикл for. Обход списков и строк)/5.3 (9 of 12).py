# Задача:
# https://i.gyazo.com/afbe65cd69b983786757cc951bd5aaf3.png

# Решение:
n = list(map(str, input().lower()))
print(n)
x = []
for i in n:
    x.append(n.count(i))
print(max(x))
