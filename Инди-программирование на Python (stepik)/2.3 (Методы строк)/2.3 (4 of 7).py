'''
Вывести сумму всех нечетных чисел от a до b
(включая обе границы)
'''
a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range (a, b + 1):
    if i%2!=0:
        s += i
print(s)
