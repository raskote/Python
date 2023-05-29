# Задание:
# https://i.gyazo.com/33490cf20d43258ea043cbec8c3d0501.png

# Решение:
li = list(input())
se = []
for i in li:
    if i.isalpha and i not in [",", ".", " ", "{", "}"]:
        se.append(i)
print(len(set(se)))

# Альтернатива (not mine):
# print(len(set(input()) - set('{ },')))
