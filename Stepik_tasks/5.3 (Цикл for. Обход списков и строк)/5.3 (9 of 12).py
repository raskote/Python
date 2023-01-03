# Задача:
# https://i.gyazo.com/fbce0857ab086f59186276dbc90b22d0.png

# Решение:
n = input()
chet = []
nechet = []
for i in range(0, len(n), 2):
    nechet.append(n[i])
    nechet = list(map(int, nechet))
for i in range(1, len(n), 2):
    chet.append(n[i])
    chet = list(map(int, chet))
if abs(sum(nechet)-sum(chet))%11==0:
    print("YES")
else:
    print("NO")

# Альтернатива (not mine)
# n = [int(i) for i in input()]
# print('NO' if (sum(n[1::2]) - sum(n[0::2])) % 11 else 'YES')