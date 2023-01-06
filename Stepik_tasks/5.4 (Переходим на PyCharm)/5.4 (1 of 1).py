# Задание:
# https://i.gyazo.com/8543e48de2f29624db5565af6a5344ff.png

# Решение:
n = input().split()
stek = []
stek_kek = []
for i in range(len(n)):
    if n[i].lower() not in stek:
        stek.append(n[i].lower())
        stek_kek.append(n[i])
print(*stek_kek)