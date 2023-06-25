# Задание:
# https://i.gyazo.com/da9e3c5be97331d3ea3ab85aa0669f01.png

# Решение:
def flatten(li: list, s: list = []) -> int:
    if len(li) > 0:
        s.extend(li[-1])
        li.pop(-1)
        return flatten(li, s)
    else:
        return s

li = [1, [2, 3, [4]], 5]
print(flatten(li))

