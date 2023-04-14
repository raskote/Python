# Задача:
# https://i.gyazo.com/c205ebeddb65cad7a6af8a88f6f7f188.png

# Решение:
# n, m = 3, 5
# li = ["***..", "..**.", "...**"]
n, m = map(int, input().split())
li = [input() for i in range(n)]
for k in range(n):
    li[k] = "."+li[k]+"."
extend = "".join(["." for i in range(m+2)])
li.insert(n, extend)
li.insert(0, extend)
count = 0
print(li)
for i in range(1, n+1):
    for j in range(1, m+1):
        if li[i][j] == ".":
            if li[i+1][j] != "*" and li[i][j+1] != "*" and li[i-1][j] != "*" and li[i][j-1] != "*":
                count += 1
print(count)

# Альтернатива (not mine):
# # put your python code here
# n, m = (int(i) for i in input().split())                 # ввод строки/стобцы
# a = [[str(j) for j in input()] for i in range(n)]        # ввод поля боя
# no_count = 0                                             # антисчетчик
# count = 0                                                # счетчик годных клеток
# for i in range(n):                                       # проход по строкам поля
#     for j in range(m):                                   # в нем проход по столбцам
#         if a[i][j] != '*':                               # если текущая клетка не корабль
#             for d in (-1, 1):                            # то проход по соседям сверху-снизу + слева-справа
#                 ai = i + d                               # и расчет адресов соседей сверху-снизу
#                 if 0 <= ai < n and a[ai][j] == '*':      # и если сосед в рамках поля и это корабль
#                         no_count += 1                    # тогда антисчетчик +1
#                 aj = j + d                               # и расчет адресов соседей слева-справа
#                 if 0 <= aj < m and a[i][aj] == '*':      # и если сосед в рамках поля и это корабль
#                         no_count += 1                    # тогда антисчетчик +1
#             count += 1 if no_count == 0 else 0           # если среди соседей нет кораблей то счетчик +1
#             no_count = 0                                 # антисчетчик = 0 и обход поля до самого конца
# print(count)