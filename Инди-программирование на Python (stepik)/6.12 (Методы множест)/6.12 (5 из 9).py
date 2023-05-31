# Задание:
# https://i.gyazo.com/daf97de0f3cfdbc44e4e2a54f0f47b27.png

# Решение:
x = input().lower().split(',')
y = set()
for i in x:
    if i not in y:
        y.add(i)
        print("НЕТ")
    else:
        print("ДА")



