# Задание:
# https://i.gyazo.com/e259d0fb8741c7210630bd983fa5ad2f.png

# Решение:
def multiply(*args: int):
    pro = 1
    for i in args:
        pro *= i
    return pro

