# Задача:
# https://i.gyazo.com/c2bffac9a29667c7944561e20d1481ce.png

# Решение:
li = [int(input()) for _ in range(int(input()))]
lst1 = []
lst2 = []
lst3 = []
lst = []
for i in range(len(li)):
    if li[i] < 0:
        lst1.append(li[i])
    elif li[i] == 0:
        lst2.append(li[i])
    else:
        lst3.append(li[i])
lst.extend(lst1)
lst.extend(lst2)
lst.extend(lst3)
print(*lst, sep='\n')

# Альтернатива (not mine):
# n = int(input())
# x = [int(input()) for _ in range(n)]
# [print(i) for i in x if i < 0]
# [print(i) for i in x if i == 0]
# [print(i) for i in x if i > 0]

