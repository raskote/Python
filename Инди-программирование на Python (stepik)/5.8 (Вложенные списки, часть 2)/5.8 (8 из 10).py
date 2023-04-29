# Задача:
# https://i.gyazo.com/7a9c5f0dccb1751c6fce4cecdb79378b.png

# Решение:
n, m = map(int, input().split())
li = [input() for i in range(n)]
flag = False
for i in range(n):
    for j in range(m):
        if li[i][j] in ['C', 'M', "Y"]:
            flag = True
if flag:
    print("#Color")
else:
    print("#Black&White")