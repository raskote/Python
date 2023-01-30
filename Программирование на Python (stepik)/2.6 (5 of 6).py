# Задача:
# https://i.gyazo.com/bb307c095f42df23d8a682a96a17831c.png

# Решение:
b = []
n = []
while True:
    a = input()
    if a == "end":
        break
    else:
        b.append([int(x) for x in a.split()])
        continue
for i in b:
    # for j in b:
    print(b)
        # print(b[i][j])
