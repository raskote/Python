# Задача:
# https://i.gyazo.com/928649b17cbf0c9c303f2ed310aac914.png

# Решение:
# Функция
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result

# Считываем данные
total_li = []
for i in range(int(input())):
    num = [int(q) for q in input().split()]
    total_li = quick_merge(total_li, num)
print(*total_li)
