# Задача:
# https://i.gyazo.com/6d913c6f975cd1eed9df378d3476ba8c.png

# Решение:
li = [input() for i in range(4)]
flag = True
for i in range(3):
    for j in range(3):
        if li[i][j] == li[i+1][j] and li[i][j] == li[i][j+1] and li[i][j] == li[i+1][j+1]:
            flag = False
if flag == True:
    print("Yes")
else:
    print("No")