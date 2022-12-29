# Задача:
# Чему равен НОК чисел 75 и 120?

# Решение:
a, b = map(int, input().split())
c, d = a, b
while b>0:
    a,b = b,a%b
print(int((abs(c*d))/a))

