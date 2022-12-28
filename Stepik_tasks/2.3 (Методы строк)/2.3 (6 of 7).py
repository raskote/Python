'''
Вывести сумму всех нечетных чисел от a до b
(включая обе границы)
'''
a, b = (int(i) for i in input().split())
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)
