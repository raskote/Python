# Задача:
# Найдите сумму всех четырехзначных чисел, сумма цифр каждого из которых равна 20.

# Решение:
sum = 0
summa = 0
for b1 in range(1, 10):
    for b2 in range(0, 10):
        for b3 in range(0, 10):
            for b4 in range(0, 10):
                rez = b1+b2+b3+b4
                if rez == 20:
                    sum = str(b1)+str(b2)+str(b3)+str(b4)
                    summa += int(sum)
print(summa)

# Альтернатива (not mine):
# s = 0
# for i in range(1000, 10000):
#     if sum(map(int, str(i))) == 20:
#         s += i
# print(s)