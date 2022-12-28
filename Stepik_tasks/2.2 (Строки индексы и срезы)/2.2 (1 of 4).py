i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break #завершаем цикл
    if (a == 0) or (b == 0):
        continue # переходим к следующей итерации
    print(a * b)
    i += 1
else:
    print("Все пары чисел были прочитаны")