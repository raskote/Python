# Задача:
# На вход программе поступает список из целых чисел.
# Ваша задача найти в данном списке наименьшее положительное значение.
# В случае, если положительных значений нет, выведите строку "Empty"

# Решение:
# n = list(map(int,input().split()))
# new_n=[]
# for i in range(len(n)):
#     if n[i] > 0:
#         new_n.append(n[i])
# if len(new_n)>0:
#     print(min(new_n))
# else:
#     print("Empty")

# Альтернатива_1 (mine):
n = list(map(int,input().split()))
n.sort()
for i in range(len(n)):
    if n[0] <= 0:
        n.pop(0)
if len(n) > 0:
    print(n[0])
else:
    print("Empty")

# Альтернатива_2 (not mine):
# print((sorted([i for i in map(int, input().split()) if i > 0]) + ['Empty'])[0])
