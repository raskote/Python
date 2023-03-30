# Задача:
# https://i.gyazo.com/e06bbe054665e167fefe09cf75a9da2a.png

# Решение:
n = int(input())
li = []
flag = True
for i in range(n):
    li.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(i):
        if li[i][j] != li[j][i]:
            flag = False
if flag == True:
    print("Yes")
else:
    print("No")