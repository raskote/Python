# Задание:
# https://i.gyazo.com/4688551936e97887e75e5822482c5c1b.png

# Решение:
def list_sum_recursive(li: list, s: int = 0) -> int:
    if len(li) > 0:
        s += li[-1]
        li.pop(-1)
        return list_sum_recursive(li, s)
    else:
        return s

li = [int(i) for i in input().split()]
n = len(li)

print(list_sum_recursive(li))
