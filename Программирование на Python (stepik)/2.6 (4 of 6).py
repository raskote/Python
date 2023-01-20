# Задача:
# https://i.gyazo.com/dfbda78d09e521cef74dbe5d61bc2037.png

# Решение:
c = [int(y) for y in input().split()]
x = int(input())
a = []
for i in range(len(c)):
    if c[i] == x:
        a.append(i)
if len(a) == 0:
    print("Отсутствует")
else:
    print(*a)

# Альтернатива (not mine)
# lst = [int(i) for i in input().split()]
# x = int(input())
# for i in range(len(lst)):
#     if
# lst[i] == x:
# print(i, end=" ")
# if x not in lst:
#     print('Отсутствует')