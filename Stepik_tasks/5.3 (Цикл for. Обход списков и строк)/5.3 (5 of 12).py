# Задача:
# https://i.gyazo.com/ecd650ecfeca669121c50551c7a69ccf.png

# Решение:
n = input()
m = input().split()

for i in range(len(m)):
    if n in m[i]:
        print(m[i])

# Альтернатива_1 (not mine):
# letter = input()
# print(*[i for i in input().split() if letter in i], sep='\n')
