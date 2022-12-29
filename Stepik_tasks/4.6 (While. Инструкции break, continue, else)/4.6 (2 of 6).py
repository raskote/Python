# Задача:
# https://i.gyazo.com/279ea5a80a1ea36f2b6288cb09efa409.png

# Решение:
a,b = int(input()), int(input())
while a <= b:
    if a == 777:
        break
    if a%2==0 or a%3==0:
        a += 1
        continue
    print(a)
    a += 1


