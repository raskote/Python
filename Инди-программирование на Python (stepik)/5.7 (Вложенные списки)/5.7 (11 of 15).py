# Задача:
# https://i.gyazo.com/f046986ad445f8d47891c3e1f48a5c49.png

# Решение:
n, m = map(int, input().split())
li = [list(map(int, input().split())) for i in range(n)]
max_num = [max(i) for i in li] # определяем максимальные числа в подстроках
print("Максимальное число в каждой подстроке:", max_num)
sum_row = [sum(i) for i in li] # определяем суммы подстрок
print("Суммы всех подстрок:", sum_row)
max_row = max([sum(i) for i in li]) # определяем максимальную сумму
print("Максимальная сумма строки среди всех строк:", max_row)
maxx_num = max([i for i in max_num]) # определяем самое максимальное число в списке
print("Максимальное число в списке максимальных чисел подстрок:", maxx_num)
# print("Первое вхождение в список максимального:", max_num.index(maxx_num))
# last_occurence = (len(max_num) -1) - list(reversed(max_num)).index(maxx_num) # определяем последнее вхождение максимального числа в список подстрок
# print("Последнее вхождение в список максимального:", last_occurence)
max_sum = 0
if max_num.count(maxx_num) > 1:     # если количество этого максимального числа больше одного, тогда
    print("Максимальное число:", maxx_num, "Количество максимальных чисел:", max_num.count(maxx_num))
    if maxx_num in li[sum_row.index(max_row)]:  # если максимальное число в подсписке с максимальной суммой строки
        print('Индекс подстроки с максимальной суммой:', sum_row.index(max_row))           # выводим индекс строки, где максимальная сумма
    else:
        for i in range(len(max_num)):
            if max_num[i] == maxx_num and max_sum < sum_row[i]:
                max_sum = sum_row[i]
        print("Номер подстроки в которой находится максимальная сумма, среди строк где есть эта сумма:", sum_row.index(max_sum))
else:
    print("Индекс подстроки, где находится максимальное число:", max_num.index(maxx_num))



