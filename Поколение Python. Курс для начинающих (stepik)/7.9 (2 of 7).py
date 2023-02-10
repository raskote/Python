# Задача:
# https://i.gyazo.com/a2f274747b4e9e5cebb4c79e9698f2a9.png

# Решение:
n = 5
tot = 0
netot = int(tot/2)
for i in range(2, n+2):
    for j in range(1,i):
        tot += 1
        print(j, end=" ")
    print()