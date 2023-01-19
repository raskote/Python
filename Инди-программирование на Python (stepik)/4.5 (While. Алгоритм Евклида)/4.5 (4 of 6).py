# Задача:
# Чему равен НОК чисел 35 и 5?

# Решение:
a = 35
b = 5
c, d = a, b
while b>0:
    a,b = b,a%b
print((abs(c*d))/a)

