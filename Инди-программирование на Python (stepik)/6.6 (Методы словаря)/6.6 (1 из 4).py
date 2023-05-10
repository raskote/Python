# Задача:
# https://i.gyazo.com/28278d3688d4c04615060ae226c06616.png

# Решение:
users = {}
n = int(input())
while n > 0:
    x = input()
    if x in users:
        users[x] = users.get(x)+1
        print(x, users[x], sep="")
    else:
        print("OK")
        users.setdefault(x, 0)
    n -= 1
