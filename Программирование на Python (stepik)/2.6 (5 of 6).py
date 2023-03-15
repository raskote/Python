# Задача:
# https://i.gyazo.com/bb307c095f42df23d8a682a96a17831c.png

# Решение:
b = []
c = []
while True:
    a = input()
    if a == "end":
        break
    else:
        b.append([int(x) for x in a.split()])
        c.append([int(x) for x in a.split()])
        continue
for i in range(len(b)):
    for j in range(len(b[i])):
        c[i][j] = (b[i-1][j] + b[i-len(b)+1][j] + b[i][j-1] + b[i][j-len(b[i])+1])

for k in range(len(c)):
    print(*c[k])