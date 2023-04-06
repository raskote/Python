# Задача:
# https://i.gyazo.com/6d913c6f975cd1eed9df378d3476ba8c.png

# Решение:
# li = [input() for i in range(4)]
li = ['BWBW', 'BBWB', 'WWBB', 'BWWW']
print(li)

for i in range(3):
    for j in range(3):
        if li[i][j] == li[j+1][]