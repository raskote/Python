# Задача:
# https://i.gyazo.com/801e428df2592c773d340efb2f4a54d1.png

# Решение:
n, x = map(int, input().split())
li = []
count = 0
for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        row.append(i*j)
    li.append(row)
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j] == x:
            count += 1
print(count)
