# Задача:
# Посчитайте при помощи метода, рассказанного в видео, значение НОДа чисел 345 и 555

# Решение:
a = 345
b = 555
while b>0:
    a,b = b,a%b
print(a)
